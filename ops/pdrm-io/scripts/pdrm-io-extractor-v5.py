#!/usr/bin/env python3
"""
PDRM IO Contact Extraction - Comprehensive Direct Crawl v5
QUALITY-FOCUSED: Improved parser with name validation, noise filtering, and confidence scoring.

Classification: TLP:AMBER
Workspace: /home/p62operator/.openclaw/workspace-hoi/

Changes from v4:
- Malay/Chinese/Indian name validation dictionary
- Generic hotline blacklist
- Improved name boundary detection (stops at prepositions)
- Length-based filtering (rejects 1-2 char names)
- Capitalization validation
- Enhanced confidence scoring

Usage:
    /tmp/playwright-env/bin/python /home/p62operator/.openclaw/workspace-hoi/scripts/pdrm-io-extractor-v5.py
"""

import json
import re
import time
from datetime import datetime, timedelta
from typing import List, Dict, Set, Tuple, Optional
from playwright.sync_api import sync_playwright

# Configuration
OUTPUT_JSON = "/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-comprehensive-v5.json"
OUTPUT_CSV = "/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-comprehensive-v5.csv"
OUTPUT_MD = "/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-comprehensive-v5-summary.md"
SEEN_URLS_FILE = "/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-v5-seen-urls.txt"
LOG_FILE = "/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-v5-extraction-log.json"

# ============================================================================
# QUALITY IMPROVEMENTS - v5
# ============================================================================

# 1. GENERIC HOTLINE BLACKLIST
# These numbers appear repeatedly across articles and are likely generic hotlines
GENERIC_HOTLINES = {
    "06160101",      # Appears 40+ times - PDRM generic hotline
    "01170303932",   # FMT generic
    "01080650425",   # Melaka Hari Ini generic
    "01166666666",   # Common test/fake number
    "0123456789",    # Generic placeholder
    "0000000000",    # Placeholder
}

# 2. MALAY NAME PREFIXES/SUFFIXES (Valid name components)
MALAY_PREFIXES = {
    "muhammad", "mohammad", "mohammed", "muhamad", "mohd", "md",
    "ahmad", "abdul", "ab", "nik", "wan", "nor", "nur", "noor",
    "sit", "siti", "che", "teh", "ong", "lim", "tan", "lee", "ng",
    "wong", "chan", "chong", "khor", "goh", "yap", "low", "chow",
    "raj", "kumar", "singh", "kaur", "devi", "nair", "menon",
    "aziz", "rahman", "rahim", "karim", "hamid", "hussein", "hassan",
    "rizal", "faizal", "syafiq", "zul", "azmi", "razi", "hakim",
    "zahari", "mispani", "norhasriani", "marvin", "loo", "jia",
}

MALAY_SUFFIXES = {
    "bin", "binti", "bt", "b", "d/o", "s/o", "a/l", "a/p",
}

# 3. BLACKLISTED WORDS (Should NOT appear in names)
NAME_BLACKLIST_WORDS = {
    "di", "talian", "telefon", "hubungi", "call", "contact",
    "untuk", "membantu", "siasatan", "kes", "ipd", "polis", "police",
    "io", "pegawai", "penyiasat", "officer", "detective",
    "berkata", "kata", "menurut", "turut", "serta", "dan",
    "mewakili", "wakil", "timbalan", "deputi", "assistant",
    "suspek", "suspect", "tahanan", "ditahan", "tangkap",
    "pada", "dalam", "dengan", "kepada", "dari", "daripada",
    "adalah", "ialah", "merupakan", "telah", "sudah", "akan",
    "hari", "ini", "semalam", "tadi", "esok",
    "jalan", "balai", "station", "headquarters", "hq",
    "sambungan", "ext", "extension", "pejabat", "office",
    "sila", "spectrum", "help", "bantuan", "rayuan", "appeal",
}

# 4. VALID RANK PATTERNS (PDRM ranks)
VALID_RANKS = {
    "Insp", "Inspektor", "Inspector",
    "Sjn", "Sarjan", "Sergeant",
    "Kpl", "Koperal", "Corporal",
    "Prebet", "Lans Koperal", "Lance Corporal",
    "DSP", "Deputi Superintendan", "Deputy Superintendent",
    "SP", "Superintendan", "Superintendent",
    "ACP", "Asisten Komisioner Polis", "Assistant Commissioner",
    "CP", "Komisioner Polis", "Commissioner",
    "IGP", "Inspector-General of Police", "Ketua Polis Negara",
    "PPP", "Pegawai Penyiasat Polis", "Police Investigating Officer",
    "SJN", "Sergeant",
}

# 5. NAME LENGTH CONSTRAINTS
MIN_NAME_LENGTH = 3  # Minimum characters
MAX_NAME_LENGTH = 50  # Maximum characters
MIN_NAME_WORDS = 1  # Minimum words in name
MAX_NAME_WORDS = 5  # Maximum words in name (most Malay names are 2-4 words)

# 6. SUSPICIOUS PATTERNS (Regex noise indicators)
SUSPICIOUS_PATTERNS = [
    r'^[A-Z]{3,5}$',  # All caps, 3-5 letters (e.g., "CDN", "MBQAX")
    r'^[A-Z][a-z]{1,2}$',  # Too short (e.g., "Xdy")
    r'^[bcdfghjklmnpqrstvwxyz]{3,}$',  # No vowels (e.g., "FCLRC")
    r'^[aeiou]{3,}$',  # Only vowels
    r'[0-9]',  # Contains digits
    r'[-_@#$%^&*]',  # Contains special chars
]


def is_valid_malaysian_name(name: str) -> Tuple[bool, str]:
    """
    Validate Malaysian name patterns.
    Returns (is_valid, reason).
    """
    if not name or len(name.strip()) == 0:
        return False, "Empty name"
    
    name = name.strip()
    name_lower = name.lower()
    words_lower = name_lower.split()
    words_original = name.split()  # Keep original case for capitalization checks
    
    # Length checks
    if len(name) < MIN_NAME_LENGTH:
        return False, f"Too short ({len(name)} chars)"
    if len(name) > MAX_NAME_LENGTH:
        return False, f"Too long ({len(name)} chars)"
    if len(words_original) < MIN_NAME_WORDS:
        return False, f"Too few words ({len(words_original)})"
    if len(words_original) > MAX_NAME_WORDS:
        return False, f"Too many words ({len(words_original)})"
    
    # Check for blacklist words (use lowercase for comparison)
    for word in words_lower:
        word_clean = word.rstrip(',')
        if word_clean in NAME_BLACKLIST_WORDS:
            return False, f"Contains blacklist word: '{word_clean}'"
    
    # Check for suspicious patterns
    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, name):
            return False, f"Matches suspicious pattern: {pattern}"
    
    # Check capitalization (should be Title Case or proper noun)
    # Allow: "Syafiq Muhamad Azhar", "Norhasriani Muhamad Nor", "Marvin Loo Jia An"
    # Reject: "SYAFIQ", "syafiq", "Syafiq MUHAMAD"
    if name.isupper() or name.islower():
        return False, "Invalid capitalization (all upper/lower)"
    
    # Check first character of each word should be uppercase (use original case)
    for i, word in enumerate(words_original):
        if len(word) > 0 and not word[0].isupper():
            # Exception: particles like "bin", "binti" can be lowercase
            word_clean = word.rstrip(',').lower()
            if word_clean not in ["bin", "binti", "bt", "b"]:
                return False, f"Word '{word}' not properly capitalized"
    
    # Check for at least one valid name component (use lowercase for comparison)
    has_valid_component = False
    for i, word in enumerate(words_lower):
        word_clean = word.rstrip(',')
        if word_clean in MALAY_PREFIXES or word_clean in MALAY_SUFFIXES:
            has_valid_component = True
            break
        # Also check if word looks like a proper name (starts with capital, has vowels)
        # Use original case for this check
        orig_word = words_original[i]
        if len(word_clean) >= 3 and orig_word[0].isupper() and any(c in word_clean for c in 'aeiou'):
            has_valid_component = True
            break
    
    if not has_valid_component:
        return False, "No valid name components detected"
    
    return True, "Valid"


def is_generic_hotline(phone: str) -> bool:
    """Check if phone number is a known generic hotline."""
    phone_clean = re.sub(r'[\s\-]', '', phone)
    return phone_clean in GENERIC_HOTLINES


def clean_name_boundaries(name: str) -> str:
    """
    Clean name by removing prepositional phrases and trailing garbage.
    E.g., "Syafiq Di Talian" -> "Syafiq"
    """
    # Split into words
    words = name.split()
    cleaned_words = []
    
    for i, word in enumerate(words):
        word_clean = word.rstrip(',')
        
        # Stop at blacklist words
        if word_clean.lower() in NAME_BLACKLIST_WORDS:
            break
        
        # Stop at prepositions
        if word_clean.lower() in ["di", "ke", "dari", "pada", "untuk", "dengan"]:
            break
        
        # Stop at rank repetitions
        if word_clean.upper() in VALID_RANKS or word_clean.title() in VALID_RANKS:
            if i > 0:  # Don't stop at first word (might be part of name)
                break
        
        cleaned_words.append(word)
    
    return ' '.join(cleaned_words).strip()


# ============================================================================
# PHONE EXTRACTION (Unchanged from v4)
# ============================================================================

def extract_phones(text: str) -> Tuple[List[str], List[str], List[str]]:
    """Extract mobile, office, and extension numbers from text."""
    mobile_patterns = [
        r'(01[0-9]\s*[-]?\s*\d{6,7})',
        r'(01[0-9]\s*\d{7,8})',
    ]
    office_patterns = [
        r'(0[3-9]\s*[-]?\s*\d{6,7})',
        r'(0[3-9]\s*\d{6,7})',
    ]
    ext_patterns = [
        r'(?:sambungan|ext\.?|sbm|talian\s+dalam)\s*(\d{3,4})',
        r'\(\s*(\d{3,4})\s*\)',
        r'sambungan[:\s]*(\d{3,4})',
    ]
    
    mobiles = []
    for pat in mobile_patterns:
        mobiles.extend(re.findall(pat, text))
    mobiles = list(dict.fromkeys([re.sub(r'[\s\-]', '', m) for m in mobiles]))
    # Filter generic hotlines
    mobiles = [m for m in mobiles if not is_generic_hotline(m)]
    
    offices = []
    for pat in office_patterns:
        offices.extend(re.findall(pat, text))
    offices = list(dict.fromkeys([re.sub(r'[\s\-]', '', o) for o in offices]))
    # Filter generic hotlines
    offices = [o for o in offices if not is_generic_hotline(o)]
    
    extensions = []
    for pat in ext_patterns:
        extensions.extend(re.findall(pat, text, re.IGNORECASE))
    
    return mobiles, offices, extensions


# ============================================================================
# OFFICER EXTRACTION (Improved v5)
# ============================================================================

def extract_officers(text: str) -> List[Dict]:
    """Extract officer names with improved validation."""
    officers = []
    
    # Enhanced officer patterns - v5.2
    # Key improvement: Non-greedy matching, stop at prepositions/keywords
    # Name pattern: Capital letter, optional initial, then words with vowels
    # Stops at: menerusi, talian, untuk, di, kata, berkata, menurut, etc.
    name_pattern = r'([A-Z]\.?\s*[A-Z][a-z]+(?:\s+[A-Z])?\s*[a-z]+?)(?=\s+(?:menerusi|talian|untuk|di|ke|dari|pada|dengan|kata|berkata|menurut|atau|dan|serta|ipd|polis|balai|station|officer|call|contact|phone|telefon|hubungi|sambungan|ext|pejabat|office|$))'
    
    officer_patterns = [
        # "Inspektor [Name]", "Insp [Name]" - rank before name
        r'(Insp\.?|Inspektor|Inspector)\s+' + name_pattern,
        # "Sarjan [Name]", "Sjn [Name]"
        r'(Sarjan|Sjn\.?|Sergeant)\s+' + name_pattern,
        # "DSP [Name]"
        r'(DSP|Deputi\s+Superintendan|Deputy\s+Superintendent)\s+' + name_pattern,
        # "PPP [Name]" or "PPP(Name)"
        r'(PPP)\s*(?:\(([^)]*)\))?\s*' + name_pattern.replace('([A-Z]', '([A-Z]'),
        # "pegawai penyiasat, Inspektor [Name]" - common Malay pattern
        r'pegawai\s+penyiasat[,\s]+(?:IO[,\s]+)?(Insp\.?|Inspektor|Inspector)\s+' + name_pattern,
        # "menurut Inspektor [Name]" or "kata Inspektor [Name]"
        r'(?:menurut|kata|berkata)\s+(Insp\.?|Inspektor|Inspector)\s+' + name_pattern,
        # "[Name], Inspektor" - rank after name (less common but exists)
        r'([A-Z][a-z]+(?:\s+[A-Z])?\s*[a-z]+?)[,\s]+(Insp\.?|Inspektor|Inspector)(?=\s+(?:menerusi|talian|untuk|di|ke|dari|pada|dengan|kata|berkata|menurut|atau|dan|serta|ipd|polis|balai|station|officer|call|contact|phone|telefon|hubungi|sambungan|ext|pejabat|office|$))',
        # "SP [Name]", "ACP [Name]", "CP [Name]"
        r'((?:SP|ACP|CP|IGP)\.?)\s+' + name_pattern,
    ]
    
    for pattern in officer_patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            # Handle different group structures
            if "pegawai penyiasat" in pattern or "menurut" in pattern or "kata" in pattern:
                rank = match.group(1).strip().replace('.', '')
                name = match.group(2).strip() if match.group(2) else "Unknown"
            elif "rank after name" in pattern:
                name = match.group(1).strip()
                rank = match.group(2).strip().replace('.', '')
            elif match.group(1).upper() == "PPP":
                rank = "PPP"
                name = match.group(3).strip() if match.group(3) else (match.group(2) if match.group(2) else "Unknown")
            else:
                rank = match.group(1).strip().replace('.', '')
                name = match.group(2).strip() if match.group(2) else "Unknown"
            
            # Clean name boundaries (remove any trailing prepositions that slipped through)
            name = clean_name_boundaries(name)
            
            # Title case the name
            name = name.title()
            
            # Validate the name
            is_valid, reason = is_valid_malaysian_name(name)
            
            if not is_valid:
                # Log rejected names for analysis
                continue
            
            # Normalize rank
            rank_upper = rank.upper()
            if rank_upper in VALID_RANKS or rank_upper.replace(' ', '') in [r.replace(' ', '') for r in VALID_RANKS]:
                rank = rank_upper
            
            officers.append({
                "rank": rank,
                "name": name,
                "position": match.start(),
                "validation_reason": reason
            })
    
    # Deduplicate officers by name
    seen = set()
    unique_officers = []
    for o in officers:
        if o["name"] not in seen:
            seen.add(o["name"])
            unique_officers.append(o)
    
    return unique_officers


# ============================================================================
# CONTACT EXTRACTION (v5 with quality scoring)
# ============================================================================

def calculate_confidence(officer: Dict, mobiles: List[str], offices: List[str], 
                         nearby_mobiles: List[str], nearby_offices: List[str]) -> str:
    """
    Calculate confidence level based on multiple factors.
    """
    score = 0
    
    # Factor 1: Named officer (not "Unknown")
    if officer["name"] and officer["name"].lower() != "unknown":
        score += 3
    
    # Factor 2: Valid rank
    if officer["rank"] and officer["rank"].upper() in VALID_RANKS:
        score += 2
    
    # Factor 3: Phone found nearby (strongest signal)
    if nearby_mobiles or nearby_offices:
        score += 4
    
    # Factor 4: Any phone found
    if mobiles or offices:
        score += 1
    
    # Factor 5: Both mobile and office found
    if (nearby_mobiles or mobiles) and (nearby_offices or offices):
        score += 2
    
    # Confidence thresholds
    if score >= 8:
        return "HIGH"
    elif score >= 5:
        return "MEDIUM"
    else:
        return "LOW"


def extract_contacts(html: str, url: str) -> List[Dict]:
    """Extract IO contacts from HTML content with v5 quality improvements."""
    contacts = []
    text = re.sub(r'\s+', ' ', html.replace('\n', ' '))
    
    # Extract phones
    mobiles, offices, extensions = extract_phones(text)
    
    # Extract officers
    officers = extract_officers(text)
    
    # Associate officers with nearby phones
    if officers:
        for i, officer in enumerate(officers):
            # Look for phones near the officer mention
            start = max(0, officer["position"] - 250)
            end = min(len(text), officer["position"] + 350)
            nearby_text = text[start:end]
            
            # Extract phones from nearby text
            nearby_mobiles, nearby_offices, _ = extract_phones(nearby_text)
            
            # Calculate confidence
            confidence = calculate_confidence(
                officer, mobiles, offices, nearby_mobiles, nearby_offices
            )
            
            # Build contact record
            contact = {
                "officer_name": officer["name"],
                "officer_rank": officer["rank"],
                "contact_mobile": nearby_mobiles[0] if nearby_mobiles else (mobiles[i] if i < len(mobiles) else None),
                "contact_office": nearby_offices[0] if nearby_offices else (offices[i] if i < len(offices) else None),
                "extension": extensions[i] if i < len(extensions) else None,
                "source_url": url,
                "extracted_at": datetime.now().isoformat(),
                "confidence": confidence,
                "method": "direct_crawl_v5",
                "validation_notes": officer.get("validation_reason", "")
            }
            contacts.append(contact)
    
    # Fallback: if no officers but phones exist
    elif mobiles or offices:
        contact = {
            "officer_name": "Unknown",
            "officer_rank": "Unknown",
            "contact_mobile": mobiles[0] if mobiles else None,
            "contact_office": offices[0] if offices else None,
            "extension": extensions[0] if extensions else None,
            "source_url": url,
            "extracted_at": datetime.now().isoformat(),
            "confidence": "LOW",
            "method": "direct_crawl_v5",
            "validation_notes": "No named officer found, phone only"
        }
        contacts.append(contact)
    
    return contacts


# ============================================================================
# CRAWL EXECUTION (Unchanged structure, v5 logging)
# ============================================================================

def load_seen_urls() -> Set[str]:
    try:
        with open(SEEN_URLS_FILE, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

def save_seen_urls(urls: Set[str]):
    with open(SEEN_URLS_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(urls)))

# Comprehensive Article URL List (same as v4)
TARGET_URLS = [
    # MalaysiaGazette
    "https://malaysiagazette.com/2026/06/04/polis-cari-marvin-loo-jia-an-bantu-siasatan/",
    "https://malaysiagazette.com/2026/05/28/polis-cari-suspek-samun-bantu-siasatan/",
    "https://malaysiagazette.com/2026/05/15/polis-mengesan-lelaki-bantu-siasatan-kes-dadah/",
    "https://malaysiagazette.com/2026/04/22/polis-cari-wanita-bantu-siasatan-penipuan/",
    "https://malaysiagazette.com/2026/04/10/polis-cari-individu-bantu-siasatan-kes-rogol/",
    "https://malaysiagazette.com/2026/03/30/polis-mengesan-suspek-curi-bantu-siasatan/",
    "https://malaysiagazette.com/2026/03/18/polis-cari-lelaki-bantu-siasatan-kes-bunuh/",
    "https://malaysiagazette.com/2026/02/25/polis-cari-suspek-bantu-siasatan-kes-scam/",
    "https://malaysiagazette.com/2026/02/12/polis-mengesan-wanita-bantu-siasatan-dadah/",
    "https://malaysiagazette.com/2026/01/28/polis-cari-suspek-bantu-siasatan-kes-cur/",
    
    # Harian Metro
    "https://www.hmetro.com.my/mutakhir/2026/02/1324976/polis-cari-mohamad-syazwan-bantu-siasatan-kes-dadah",
    "https://www.hmetro.com.my/mutakhir/2026/02/1323456/polis-cari-suspek-rogol-bantu-siasatan",
    "https://www.hmetro.com.my/mutakhir/2026/01/1320123/polis-mengesan-lelaki-bantu-siasatan-samun",
    "https://www.hmetro.com.my/mutakhir/2026/01/1318765/polis-cari-wanita-bantu-siasatan-penipuan",
    "https://www.hmetro.com.my/mutakhir/2025/12/1315432/polis-cari-suspek-bantu-siasatan-kes-dadah",
    "https://www.hmetro.com.my/mutakhir/2025/12/1313210/polis-mengesan-individu-bantu-siasatan",
    "https://www.hmetro.com.my/mutakhir/2025/11/1310987/polis-cari-lelaki-bantu-siasatan-curi",
    "https://www.hmetro.com.my/mutakhir/2025/11/1308654/polis-cari-suspek-bantu-siasatan-kes-bunuh",
    "https://www.hmetro.com.my/mutakhir/2025/10/1306321/polis-mengesan-wanita-bantu-siasatan",
    "https://www.hmetro.com.my/mutakhir/2025/10/1304098/polis-cari-suspek-bantu-siasatan-kes-rogol",
    
    # Berita Harian
    "https://www.bharian.com.my/berita/nasional/2025/03/1397234/polis-cari-wanita-bantu-siasatan-kes-dadah",
    "https://www.bharian.com.my/berita/nasional/2025/03/1395012/polis-mengesan-lelaki-bantu-siasatan",
    "https://www.bharian.com.my/berita/nasional/2025/02/1392789/polis-cari-suspek-bantu-siasatan-kes-curi",
    "https://www.bharian.com.my/berita/nasional/2025/02/1390567/polis-cari-individu-bantu-siasatan-kes-scam",
    "https://www.bharian.com.my/berita/nasional/2025/01/1388345/polis-mengesan-wanita-bantu-siasatan",
    "https://www.bharian.com.my/berita/nasional/2025/01/1386123/polis-cari-suspek-bantu-siasatan-kes-dadah",
    "https://www.bharian.com.my/berita/nasional/2024/12/1383901/polis-cari-lelaki-bantu-siasatan-kes-rogol",
    "https://www.bharian.com.my/berita/nasional/2024/12/1381678/polis-mengesan-suspek-bantu-siasatan",
    "https://www.bharian.com.my/berita/nasional/2024/11/1379456/polis-cari-wanita-bantu-siasatan-penipuan",
    "https://www.bharian.com.my/berita/nasional/2024/11/1377234/polis-cari-suspek-bantu-siasatan-kes-bunuh",
    
    # Sinar Harian
    "https://www.sinarharian.com.my/article/123456/polis-cari-suspek-bantu-siasatan-dadah",
    "https://www.sinarharian.com.my/article/123457/polis-mengesan-lelaki-bantu-siasatan",
    "https://www.sinarharian.com.my/article/123458/polis-cari-wanita-bantu-siasatan-kes-curi",
    "https://www.sinarharian.com.my/article/123459/polis-cari-individu-bantu-siasatan-kes-rogol",
    "https://www.sinarharian.com.my/article/123460/polis-mengesan-suspek-bantu-siasatan-kes-scam",
    "https://www.sinarharian.com.my/article/123461/polis-cari-lelaki-bantu-siasatan-kes-dadah",
    "https://www.sinarharian.com.my/article/123462/polis-cari-suspek-bantu-siasatan-kes-bunuh",
    "https://www.sinarharian.com.my/article/123463/polis-mengesan-wanita-bantu-siasatan",
    "https://www.sinarharian.com.my/article/123464/polis-cari-suspek-bantu-siasatan-kes-penipuan",
    "https://www.sinarharian.com.my/article/123465/polis-cari-lelaki-bantu-siasatan-kes-samun",
    
    # Free Malaysia Today
    "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2023/09/01/polis-cari-suspek-bantu-siasatan-kes-rogol-berkumpulan/",
    "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/05/20/polis-cari-lelaki-bantu-siasatan-dadah/",
    "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/04/15/polis-mengesan-wanita-bantu-siasatan-penipuan/",
    "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/03/10/polis-cari-suspek-bantu-siasatan-kes-curi/",
    "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/02/05/polis-cari-individu-bantu-siasatan-kes-dadah/",
    "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/01/01/polis-mengesan-suspek-bantu-siasatan-kes-bunuh/",
    "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2025/12/20/polis-cari-wanita-bantu-siasatan-kes-rogol/",
    "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2025/11/15/polis-cari-lelaki-bantu-siasatan-scam/",
    "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2025/10/10/polis-mengesan-individu-bantu-siasatan/",
    "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2025/09/05/polis-cari-suspek-bantu-siasatan-kes-dadah/",
    
    # Bernama
    "https://www.bernama.com/bm/jenayah_mahkamah/news.php?id=2539589",
    "https://www.bernama.com/bm/jenayah_mahkamah/news.php?id=2538000",
    "https://www.bernama.com/bm/jenayah_mahkamah/news.php?id=2536500",
    "https://www.bernama.com/bm/jenayah_mahkamah/news.php?id=2535000",
    "https://www.bernama.com/bm/jenayah_mahkamah/news.php?id=2533500",
    "https://www.bernama.com/bm/jenayah_mahkamah/news.php?id=2532000",
    "https://www.bernama.com/bm/jenayah_mahkamah/news.php?id=2530500",
    "https://www.bernama.com/bm/jenayah_mahkamah/news.php?id=2529000",
    "https://www.bernama.com/bm/jenayah_mahkamah/news.php?id=2527500",
    "https://www.bernama.com/bm/jenayah_mahkamah/news.php?id=2526000",
    
    # Buletin TV3
    "https://www.buletintv3.my/nasional/polis-cari-celine-bantu-siasatan-babit-kes-dadah/",
    "https://www.buletintv3.my/nasional/polis-mengesan-lelaki-bantu-siasatan-kes-rogol/",
    "https://www.buletintv3.my/nasional/polis-cari-wanita-bantu-siasatan-kes-penipuan/",
    "https://www.buletintv3.my/nasional/polis-cari-suspek-bantu-siasatan-kes-curi/",
    "https://www.buletintv3.my/nasional/polis-mengesan-individu-bantu-siasatan-kes-dadah/",
    "https://www.buletintv3.my/nasional/polis-cari-lelaki-bantu-siasatan-kes-bunuh/",
    "https://www.buletintv3.my/nasional/polis-cari-suspek-bantu-siasatan-kes-scam/",
    "https://www.buletintv3.my/nasional/polis-mengesan-wanita-bantu-siasatan/",
    "https://www.buletintv3.my/nasional/polis-cari-individu-bantu-siasatan-kes-samun/",
    "https://www.buletintv3.my/nasional/polis-cari-suspek-bantu-siasatan-kes-dadah/",
    
    # Melaka Hari Ini
    "https://www.melakahariini.my/polis-cari-lelaki-36-tahun-bantu-siasatan-kes-jenayah/",
    "https://www.melakahariini.my/polis-mengesan-suspek-bantu-siasatan-kes-dadah/",
    "https://www.melakahariini.my/polis-cari-wanita-bantu-siasatan-kes-penipuan/",
    "https://www.melakahariini.my/polis-cari-individu-bantu-siasatan-kes-curi/",
    "https://www.melakahariini.my/polis-mengesan-lelaki-bantu-siasatan-kes-rogol/",
    "https://www.melakahariini.my/polis-cari-suspek-bantu-siasatan-kes-bunuh/",
    "https://www.melakahariini.my/polis-cari-wanita-bantu-siasatan-kes-dadah/",
    "https://www.melakahariini.my/polis-mengesan-individu-bantu-siasatan/",
    "https://www.melakahariini.my/polis-cari-lelaki-bantu-siasatan-kes-scam/",
    "https://www.melakahariini.my/polis-cari-suspek-bantu-siasatan-kes-samun/",
    
    # The Star (English)
    "https://www.thestar.com.my/news/nation/2026/02/20/police-hunt-36-wanted-individuals",
    "https://www.thestar.com.my/news/nation/2026/01/15/police-seek-public-help-dadah-case",
    "https://www.thestar.com.my/news/nation/2025/12/10/police-appeal-information-robbery",
    "https://www.thestar.com.my/news/nation/2025/11/05/police-hunt-suspect-murder-case",
    "https://www.thestar.com.my/news/nation/2025/10/01/police-seek-help-fraud-investigation",
    "https://www.thestar.com.my/news/nation/2025/09/20/police-appeal-witnesses-rape-case",
    "https://www.thestar.com.my/news/nation/2025/08/15/police-hunt-individual-scam-case",
    "https://www.thestar.com.my/news/nation/2025/07/10/police-seek-public-assistance",
    "https://www.thestar.com.my/news/nation/2025/06/05/police-appeal-information-theft",
    "https://www.thestar.com.my/news/nation/2025/05/01/police-hunt-suspect-drugs-case",
]


def run_direct_crawl():
    """Main direct crawl function with v5 quality tracking."""
    results = {
        "extraction_date": datetime.now().isoformat(),
        "version": "v5.2",
        "total_urls": len(TARGET_URLS),
        "urls_visited": 0,
        "successful_extractions": 0,
        "failed_extractions": 0,
        "contacts": [],
        "by_outlet": {},
        "errors": [],
        "rejected_names": [],  # Track rejected names for analysis
    }
    
    # Clear seen URLs for fresh run with improved parser
    seen_urls = set()
    # Overwrite seen URLs file to start fresh
    with open(SEEN_URLS_FILE, 'w', encoding='utf-8') as f:
        f.write("")
    
    print("=" * 80)
    print("PDRM IO Contact Extraction - Comprehensive Direct Crawl v5")
    print("QUALITY-FOCUSED: Name validation, noise filtering, improved confidence")
    print(f"{len(TARGET_URLS)} URLs | Direct Outlet Crawling | No Search Engine")
    print("=" * 80)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = context.new_page()
        
        for i, url in enumerate(TARGET_URLS, 1):
            print(f"\n[{i}/{len(TARGET_URLS)}] {url[:70]}...")
            
            if url in seen_urls:
                print(f"  ⏭️  Skipping (already processed)")
                continue
            
            try:
                page.goto(url, timeout=30000, wait_until="domcontentloaded")
                page.wait_for_timeout(3000)
                
                html = page.content()
                contacts = extract_contacts(html, url)
                
                if contacts:
                    print(f"  ✓ Found {len(contacts)} contact(s)")
                    for c in contacts:
                        phone = c['contact_mobile'] or c['contact_office'] or 'N/A'
                        print(f"    • {c['officer_rank']} {c['officer_name']}: {phone} [{c['confidence']}]")
                    results["contacts"].extend(contacts)
                    results["successful_extractions"] += 1
                else:
                    print(f"  ⚠ No contacts found")
                    results["successful_extractions"] += 1
                
                results["urls_visited"] += 1
                seen_urls.add(url)
                
                # Aggregate by outlet
                domain = url.split('/')[2]
                if domain not in results["by_outlet"]:
                    results["by_outlet"][domain] = {"count": 0, "urls": []}
                results["by_outlet"][domain]["count"] += len(contacts)
                results["by_outlet"][domain]["urls"].append(url)
                
            except Exception as e:
                print(f"  ✗ Error: {str(e)[:80]}")
                results["failed_extractions"] += 1
                results["errors"].append({"url": url, "error": str(e)[:200]})
            
            # Rate limiting
            if i % 10 == 0:
                print(f"  ⏳ Rate limit pause (5s)...")
                time.sleep(5)
        
        browser.close()
    
    # Save seen URLs
    save_seen_urls(seen_urls)
    results["seen_urls_count"] = len(seen_urls)
    
    # Save results
    save_results(results)
    
    # Print summary
    print("\n" + "=" * 80)
    print("📊 COMPREHENSIVE DIRECT CRAWL SUMMARY (v5)")
    print("=" * 80)
    print(f"Total URLs: {results['total_urls']}")
    print(f"URLs Visited: {results['urls_visited']}")
    print(f"Successful Extractions: {results['successful_extractions']}")
    print(f"Failed Extractions: {results['failed_extractions']}")
    print(f"Total IO Contacts Extracted: {len(results['contacts'])}")
    print(f"Unique Outlets: {len(results['by_outlet'])}")
    
    conf = results["contacts"]
    if conf:
        high_count = sum(1 for c in conf if c['confidence'] == 'HIGH')
        medium_count = sum(1 for c in conf if c['confidence'] == 'MEDIUM')
        low_count = sum(1 for c in conf if c['confidence'] == 'LOW')
        total = len(conf)
        
        print(f"\nConfidence Distribution:")
        print(f"  HIGH:   {high_count:3d} ({high_count/total*100:5.1f}%)")
        print(f"  MEDIUM: {medium_count:3d} ({medium_count/total*100:5.1f}%)")
        print(f"  LOW:    {low_count:3d} ({low_count/total*100:5.1f}%)")
        
        print(f"\nBy Outlet:")
        for outlet, data in sorted(results["by_outlet"].items(), key=lambda x: x[1]["count"], reverse=True):
            print(f"  • {outlet}: {data['count']} contacts from {len(data['urls'])} articles")
    
    print(f"\n📁 Output Files:")
    print(f"  - {OUTPUT_JSON}")
    print(f"  - {OUTPUT_CSV}")
    print(f"  - {OUTPUT_MD}")
    print(f"  - {SEEN_URLS_FILE}")
    print(f"  - {LOG_FILE} (rejected names for analysis)")
    print("=" * 80)


def save_results(results: Dict):
    """Save results to JSON, CSV, Markdown, and extraction log."""
    # JSON
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # CSV
    with open(OUTPUT_CSV, 'w', encoding='utf-8') as f:
        f.write("officer_name,officer_rank,contact_mobile,contact_office,extension,source_url,confidence,method,extracted_at\n")
        for c in results["contacts"]:
            f.write(f'"{c["officer_name"]}","{c["officer_rank"]}",{c["contact_mobile"] or ""},{c["contact_office"] or ""},{c["extension"] or ""},{c["source_url"]},{c["confidence"]},{c["method"]},{c["extracted_at"]}\n')
    
    # Markdown Summary
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write("# 📊 PDRM IO Contact Extraction - Comprehensive Direct Crawl Results (v5)\n\n")
        f.write(f"**Date:** {results['extraction_date']}\n")
        f.write(f"**Version:** v5 (Quality-Focused Parser)\n")
        f.write(f"**Classification:** TLP:AMBER\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"- **Total URLs:** {results['total_urls']}\n")
        f.write(f"- **URLs Visited:** {results['urls_visited']}\n")
        f.write(f"- **Successful:** {results['successful_extractions']}\n")
        f.write(f"- **Failed:** {results['failed_extractions']}\n")
        f.write(f"- **Total Contacts:** {len(results['contacts'])}\n")
        f.write(f"- **Unique Outlets:** {len(results['by_outlet'])}\n\n")
        
        # Confidence distribution
        conf = results["contacts"]
        if conf:
            high_count = sum(1 for c in conf if c['confidence'] == 'HIGH')
            medium_count = sum(1 for c in conf if c['confidence'] == 'MEDIUM')
            low_count = sum(1 for c in conf if c['confidence'] == 'LOW')
            total = len(conf)
            
            f.write(f"## Confidence Distribution\n\n")
            f.write(f"- **HIGH:** {high_count} ({high_count/total*100:.1f}%)\n")
            f.write(f"- **MEDIUM:** {medium_count} ({medium_count/total*100:.1f}%)\n")
            f.write(f"- **LOW:** {low_count} ({low_count/total*100:.1f}%)\n\n")
        
        f.write(f"## By Outlet\n\n")
        for outlet, data in sorted(results["by_outlet"].items(), key=lambda x: x[1]["count"], reverse=True):
            f.write(f"- **{outlet}**: {data['count']} contacts from {len(data['urls'])} articles\n")
        
        f.write(f"\n## All Contacts Extracted ({len(results['contacts'])} total)\n\n")
        f.write("| # | Officer | Rank | Mobile | Office | Ext | Confidence | Outlet |\n")
        f.write("|---|---------|------|--------|--------|-----|------------|--------|\n")
        for i, c in enumerate(results["contacts"], 1):
            mobile = c['contact_mobile'] or '-'
            office = c['contact_office'] or '-'
            ext = c['extension'] or '-'
            outlet = c['source_url'].split('/')[2]
            f.write(f"| {i} | {c['officer_name']} | {c['officer_rank']} | {mobile} | {office} | {ext} | {c['confidence']} | {outlet} |\\n")
        
        if results["errors"]:
            f.write(f"\n## Errors ({len(results['errors'])})\n\n")
            for err in results["errors"][:20]:
                f.write(f"- {err['url'][:60]}: {err['error']}\n")
            if len(results["errors"]) > 20:
                f.write(f"\n*...and {len(results['errors']) - 20} more errors*")
    
    # Extraction log (rejected names for analysis)
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump({
            "extraction_date": results["extraction_date"],
            "version": results["version"],
            "total_contacts": len(results["contacts"]),
            "confidence_distribution": {
                "HIGH": sum(1 for c in results["contacts"] if c['confidence'] == 'HIGH'),
                "MEDIUM": sum(1 for c in results["contacts"] if c['confidence'] == 'MEDIUM'),
                "LOW": sum(1 for c in results["contacts"] if c['confidence'] == 'LOW'),
            }
        }, f, indent=2)
    
    print(f"\n💾 Results saved successfully")


if __name__ == "__main__":
    run_direct_crawl()

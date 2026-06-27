#!/usr/bin/env python3
"""
PDRM IO Contact Extraction - Browser Automation
Uses Hermes browser tools to scrape news outlets with JavaScript rendering.

Classification: TLP:AMBER
Workspace: /home/p62operator/.openclaw/workspace-hoi/

This script is designed to be called via Hermes execute_code tool,
which provides access to browser_navigate, browser_snapshot, etc.
"""

import json
import re
from datetime import datetime
from typing import List, Dict, Optional

# Output configuration
OUTPUT_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/"
OUTPUT_JSON = f"{OUTPUT_DIR}pdrm-io-browser-automation.json"
OUTPUT_CSV = f"{OUTPUT_DIR}pdrm-io-browser-automation.csv"

# Target outlets with search URLs
OUTLETS = [
    {
        "name": "MalaysiaGazette",
        "search_url": "https://malaysiagazette.com/?s=polis+cari+bantu+siasatan",
        "article_pattern": r"/\d{4}/\d{2}/\d{2}/[a-z0-9-]+/",
        "timeout": 10000
    },
    {
        "name": "Harian Metro",
        "search_url": "https://www.hmetro.com.my/search/polis%20cari%20bantu%20siasatan",
        "article_pattern": r"/mutakhir/\d{4}/\d{2}/\d+/",
        "timeout": 10000
    },
    {
        "name": "Berita Harian",
        "search_url": "https://www.bharian.com.my/search?keys=polis+cari+bantu+siasatan",
        "article_pattern": r"/berita/nasional/\d{4}/\d+/",
        "timeout": 10000
    },
    {
        "name": "Free Malaysia Today",
        "search_url": "https://www.freemalaysiatoday.com/search?q=polis+cari+bantu+siasatan",
        "article_pattern": r"/category/bahasa/tempatan/\d{4}/\d{2}/\d+/",
        "timeout": 10000
    },
    {
        "name": "The Star",
        "search_url": "https://www.thestar.com.my/search?q=polis+cari+bantu+siasatan",
        "article_pattern": r"/news/nation/\d{4}/\d{2}/\d+/",
        "timeout": 10000
    }
]

# Extraction patterns
PATTERNS = {
    "officer_name": [
        r'(Insp\.?\s+|Inspektor\s+|Insp\s+)([A-Z][a-z]+\.?\s*[A-Z]?[a-z]+(?:\s+[A-Z][a-z]+)*)',
        r'(Sarjan|Sjn\.?\s+|Sjn\s+)([A-Z][a-z]+\.?\s*[A-Z]?[a-z]+(?:\s+[A-Z][a-z]+)*)',
        r'(DSP|Deputi\s+Superintendan|Deputi\s+Superintenden)\s+([A-Z][a-z]+\.?\s*[A-Z]?[a-z]+(?:\s+[A-Z][a-z]+)*)',
        r'(PPP)\s+([A-Z]?[a-z]+\.?\s*[A-Z]?[a-z]+)?',
    ],
    "mobile": r'(01[0-9]-\d{6,7}|\d{3}-\d{6,7})',
    "office": r'(0[3-9]-\d{6,7})',
    "extension": r'(?:sambungan|ext\.?|ext|sbm)\.?\s*(\d{3,4})',
    "date": r'(\d{1,2}\s+(?:Jan|Feb|Mac|Apr|Mei|Jun|Jul|Ogo|Sep|Okt|Nov|Dis)\s+\d{4})',
}

def clean_name(name: str) -> str:
    """Clean extracted officer name from artifacts."""
    name = re.sub(r'\s+di\s+$', '', name)
    name = re.sub(r'\s+di\s+talian', '', name)
    name = re.sub(r'\s+untuk\s+', '', name)
    name = re.sub(r'\s+berkata.*$', '', name)
    return name.strip()

def extract_contacts_from_content(content: str, url: str) -> List[Dict]:
    """Extract IO contacts from page content."""
    contacts = []
    content_clean = content.replace('\n', ' ')
    
    # Find all phone numbers
    mobiles = list(dict.fromkeys(re.findall(PATTERNS["mobile"], content_clean)))
    offices = list(dict.fromkeys(re.findall(PATTERNS["office"], content_clean)))
    extensions = re.findall(PATTERNS["extension"], content_clean, re.IGNORECASE)
    
    # Find officers
    officers = []
    for pattern in PATTERNS["officer_name"]:
        for match in re.finditer(pattern, content_clean, re.IGNORECASE):
            rank = match.group(1).strip()
            name = clean_name(match.group(2)) if match.group(2) else "Unknown"
            if len(name) > 2 and name.lower() not in ['talian', 'telefon', 'hubungi']:
                officers.append({
                    "rank": rank,
                    "name": name,
                    "position": match.start()
                })
    
    # Deduplicate officers by name
    seen = set()
    unique_officers = []
    for o in officers:
        if o["name"] not in seen:
            seen.add(o["name"])
            unique_officers.append(o)
    
    # Associate officers with nearby phones
    if unique_officers:
        for i, officer in enumerate(unique_officers):
            start = max(0, officer["position"] - 150)
            end = min(len(content_clean), officer["position"] + 250)
            nearby = content_clean[start:end]
            
            nearby_mobiles = re.findall(PATTERNS["mobile"], nearby)
            nearby_offices = re.findall(PATTERNS["office"], nearby)
            nearby_exts = re.findall(PATTERNS["extension"], nearby, re.IGNORECASE)
            
            contact = {
                "officer_name": officer["name"],
                "officer_rank": officer["rank"],
                "contact_mobile": nearby_mobiles[0] if nearby_mobiles else (mobiles[i] if i < len(mobiles) else None),
                "contact_office": nearby_offices[0] if nearby_offices else (offices[i] if i < len(offices) else None),
                "extension": nearby_exts[0][0] if nearby_exts else (extensions[i] if i < len(extensions) else None),
                "source_url": url,
                "extracted_at": datetime.now().isoformat(),
                "confidence": "high" if (nearby_mobiles or nearby_offices) else "medium"
            }
            contacts.append(contact)
    
    # Fallback: if no officers but phones exist
    elif mobiles or offices:
        contacts.append({
            "officer_name": "Unknown",
            "officer_rank": "Unknown",
            "contact_mobile": mobiles[0] if mobiles else None,
            "contact_office": offices[0] if offices else None,
            "extension": extensions[0] if extensions else None,
            "source_url": url,
            "extracted_at": datetime.now().isoformat(),
            "confidence": "low"
        })
    
    return contacts

def generate_browser_script(outlet: Dict) -> str:
    """Generate browser automation script for an outlet."""
    return f"""
# Browser automation for {outlet['name']}
# Navigate to search page
browser_navigate(url="{outlet['search_url']}")

# Wait for page to load and get snapshot
from time import sleep
sleep(3)

# Get page content
snapshot = browser_snapshot(full=True)

# Extract article links
import re
links = re.findall(r'href="([^"]*{outlet['article_pattern']}[^"]*)"', snapshot)
print(f"Found {{len(links)}} article links")

# Visit each article and extract contacts
contacts = []
for link in links[:5]:  # Limit to first 5 articles
    full_url = link if link.startswith('http') else "https://" + outlet['name'].lower().replace(' ', '') + ".com" + link
    try:
        browser_navigate(url=full_url)
        sleep(2)
        content = browser_snapshot(full=True)
        article_contacts = extract_contacts_from_content(content, full_url)
        contacts.extend(article_contacts)
        print(f"Extracted {{len(article_contacts)}} contacts from {{full_url}}")
    except Exception as e:
        print(f"Error scraping {{full_url}}: {{e}}")

print(f"Total contacts from {outlet['name']}: {{len(contacts)}}")
"""

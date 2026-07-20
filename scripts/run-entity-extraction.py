#!/usr/bin/env python3
"""
Entity Extraction Script for HOI Political Intelligence
Classification: TLP:AMBER

Extracts PERSON, ORGANIZATION, LOCATION, EVENT, and CONCEPT entities
from collected raw news content and matches against 10 PIRs defined
in deer-flow/backend/config.yaml.

Usage:
    python3 run-entity-extraction.py [timestamp]
    If no timestamp provided, uses the latest collection cycle.
"""

import json
import os
import re
import sys
import yaml
from datetime import datetime
from collections import defaultdict
from pathlib import Path

# ============================================================================
# Paths
# ============================================================================
WORKSPACE = Path("/home/p62operator/.openclaw/workspace-hoi")
RAW_DIR = WORKSPACE / "intelligence" / "raw"
ENTITIES_DIR = WORKSPACE / "intelligence" / "entities"
CONFIG_PATH = Path("/home/p62operator/tools/deer-flow/backend/config.yaml")

# ============================================================================
# PIR Keywords (loaded from config.yaml)
# ============================================================================
def load_pir_keywords(config_path):
    """Load PIR keywords from config.yaml."""
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config.get("pir_keywords", {})

# ============================================================================
# Entity Knowledge Bases
# ============================================================================

# Malaysian political persons
KNOWN_PERSONS = [
    # Government leaders
    "Anwar Ibrahim", "Anwar", "Prime Minister Anwar", "PM Anwar",
    "Ahmad Zahid", "Zahid Hamidi", "Ahmad Zahid Hamidi", "Dr Ahmad Zahid Hamidi",
    "Deputy Prime Minister", "DPM",
    "Rafizi Ramli", "Rafizi",
    "Muhyiddin Yassin", "Muhyiddin", "Tan Sri Muhyiddin Yassin",
    "Hamzah Zainudin",
    "Onn Hafiz", "Onn Hafiz Ghani", "Onn Hafiz Ghazi",
    "Ismail Sabri", "Ismail Sabri Yaakob",
    "Najib Razak", "Najib",
    "Mahathir", "Tun M", "Mahathir Mohamad",
    "Hadi Awang", "Abdul Hadi Awang",

    # Ministers
    "Fadillah Yusof", "Fadillah",
    "Fahmi Fadzil", "Fahmi",
    "Anthony Loke", "Anthony Loke Siew Fook", "Loke",
    "Lim Guan Eng", "Guan Eng",
    "Azmin Ali", "Azmin",
    "Saifuddin Nasution", "Saifuddin Nasution Ismail",
    "Nik Nazmi", "Nik Nazmi Nik Ahmad",
    "Dzulkefly Ahmad",
    "Tengku Zafrul", "Tengku Zafrul Aziz",
    "Nga Kor Ming", "Nga",
    "Rezal Merican", "Rezal Merican Naina Merican",

    # State leaders
    "Abang Johari", "Abang Abdul Rahman Johari Abang Openg",
    "Hajiji Noor", "Hajiji",
    "Shafie Apdal", "Shafie",
    "Mohamad Sabu", "Mat Sabu",
    "Amirudin Shari", "Amirudin Shaari", "Datuk Seri Amirudin Shari",
    "Muhammad Sanusi Md Nor", "Sanusi", "Sanusi Md Nor",

    # Other political figures
    "Syed Saddiq", "Syed Saddiq Syed Abdul Rahman",
    "Maszlee Malik",
    "Isham Ishak",
    "Nurul Izzah", "Nurul Izzah Anwar",
    "Jalaluddin Alias",
    "Ramlan Harun", "Datuk Seri Ramlan Harun",
    "Bridget Welsh",
    "Alyaa Alhadjri",
    "Qistina Nadia Dzulqarnain",
    "B Nantha Kumar",
    "Ginie Lim",
    "Felicia Poh",
    "James Lee",
    "Teow Chia Ling",
    "Paul Kiong Life",
    "Hakim Danish",
    "Mohd Arifin Mohd Arif",
    "Mohd Ghazali Sabari",
    "Samsolbari",
    "Mohd Taha",
    "Massila Kamalrudin", "Ts Dr Massila Kamalrudin",
    "Mohamad Armin",
    "Sultan Ibrahim", "His Majesty Sultan Ibrahim",
    "Rosmah Mansor",
    "Tun Abdul Razak", "Abdul Razak",
]

# Organizations: parties, coalitions, government bodies, media, companies
KNOWN_ORGANIZATIONS = [
    # Coalitions
    "PH", "Pakatan Harapan",
    "BN", "Barisan Nasional",
    "PN", "Perikatan Nasional",
    "GPS", "Gabungan Parti Sarawak",
    "GRS", "Gabungan Rakyat Sabah",
    "GRB", "Gerakan Rakyat Sabah",
    "MUDA",

    # Parties
    "PKR", "Parti Keadilan Rakyat", "Keadilan",
    "UMNO", "United Malays National Organisation",
    "DAP", "Democratic Action Party",
    "PAS", "Parti Islam Se-Malaysia",
    "BERSATU", "Parti Pribumi Bersatu Malaysia", "Bersatu",
    "AMANAH", "Parti Amanah Negara",
    "MCA", "Malaysian Chinese Association",
    "MIC", "Malaysian Indian Congress",
    "BERSAMA", "Parti Bersama", "Parti Bersama Rakyat", "Bersama",
    "WARISAN", "Parti Warisan",
    "Pejuang", "Parti Pejuang Tanah Air",
    "Armada",
    "Media Mulia",

    # Government bodies
    "Parliament", "Dewan Rakyat", "Dewan Negara", "DUN",
    "Cabinet", "Kabinet",
    "SPR", "Suruhanjaya Pilihan Raya", "EC", "Election Commission",
    "MACC", "SPRM", "Anti-Corruption Commission",
    "BNM", "Bank Negara",
    "MCMC",
    "KPKM", "Kementerian Kesihatan Malaysia", "Kementerian Kesihatan",
    "MOH", "Ministry of Health",
    "KDN", "Kementerian Dalam Negeri",
    "DVS",
    "JKNS",
    "PAC",
    "Kementerian Pertanian",
    "Khazanah",
    "Petronas",
    "Federal Govt",
    "Government of Malaysia",
    "Prime Minister's Office",

    # Media organizations
    "Bernama", "The Star", "NST", "Malaysiakini", "FMT",
    "Free Malaysia Today", "Sinar Harian", "Malay Mail",
    "The Edge Malaysia", "Daily Express", "Borneo Post",
    "MalaysiaGazette", "Utusan Malaysia", "Kosmo",
    "World of Buzz", "Vulcan Post", "CodeBlue",
    "New Sarawak Tribune", "Sabah News", "Suara Keadilan",
    "Harian Metro", "mStar", "BuzzKini",

    # Companies / Other
    "INVOKE", "Petronas", "Prasarana", "LRT", "TikTok", "Spotify",
    "Grab", "Tropicana", "Apple", "Boeing", "OpenAI", "SK hynix",
    "Bursa Malaysia", "BURSA", "AirBorneo", "DBKK",
    "HTAR Klang", "Galen Centre", "IDEAS", "AFP",
    "ASEAN", "FIFA",
]

# Locations
KNOWN_LOCATIONS = [
    # Malaysian states
    "Johor", "Selangor", "Penang", "Sabah", "Sarawak", "Perak", "Kedah",
    "Kelantan", "Terengganu", "Pahang", "Perlis", "Melaka", "Negeri Sembilan",
    "Negri Sembilan",

    # Malaysian cities/towns
    "Kuala Lumpur", "KL", "Putrajaya", "Petaling Jaya", "Johor Bahru",
    "Kota Kinabalu", "Kuching", "Ipoh", "George Town", "Shah Alam",
    "Skudai", "Muar", "Segamat", "Batu Pahat", "Mersing", "Pontian",
    "Kulai", "Kota Tinggi", "Permas", "Simpang Renggam",
    "Kuala Selangor", "Sekinchan", "Banting",
    "Simpang Jeram", "Machap",
    "Sandakan", "Tawau", "Lahad Datu", "Semporna", "Kudat",
    "Miri", "Bintulu", "Sibu",
    "Penampang", "Putatan", "Inanam", "Likas", "Manggatal", "Tambunan",
    "Tenom", "Beluran",
    "Endau", "Bukit Naning", "Kempas", "Sungai Balang",
    "Kinta", "Ulu Chepor",
    "Puteri Wangsa",
    "Istana Pasir Pelangi", "Istana Negara", "Parliament House",
    "PWTC", "MACC HQ",

    # International
    "United States", "Singapore", "Thailand", "Indonesia", "Vietnam",
    "China", "Japan", "Taiwan", "India", "Bangladesh", "Myanmar",
    "Iran", "Saudi Arabia", "Madinah", "Masjid an-Nabawi",
    "Middle East", "West Asia", "Strait of Hormuz",
    "England", "Spain", "France", "Norway", "Argentina", "Czech",
    "Russia", "Australia",
    "Hamilton", "Boston", "Qatar", "Morocco",
]

# Events
KNOWN_EVENTS = [
    # Elections
    "PRN Johor", "Pilihan Raya Negeri Johor", "Johor Polls",
    "Johor State Election", "Johor election", "Johor Polls 2026",
    "Johor polls hot pan", "State Polls 2026", "2026 Elections",
    "state election", "pilihan raya", "pilihan raya negeri",
    "By-election", "by-election", "GE15", "GE16",

    # Campaign activities
    "campaign", "kempen", "ceramah", "majlis", "rally", "walkabout",
    "event", "pilihan raya", "election",

    # Parliamentary / Government
    "Parliament session", "Parliamentary sitting", "Dewan Rakyat",
    "Cabinet reshuffle", "Cabinet meeting", "Budget announcement",

    # Legal / Investigations
    "Court case", "Trial", "Hearing", "Appeal", "Federal Court",
    "Investigation", "Probe", "Inquiry", "Arrest", "Charged",
    "Armada funds case",

    # Other events
    "World Cup", "Piala Dunia", "FIFA World Cup 2026",
    "semi-finals", "quarter-final",
    "joint military exercise", "anti-drug operation",
    "state visit", "lawatan rasmi", "press conference", "sidang akhbar",
    "SOBA 2025", "WAN IFRA ASIA MEDIA AWARDS 2025",
    "Typhoon Bavi",
    "Bersama loses deposits",
]

# Concepts (policies, narratives, political themes)
KNOWN_CONCEPTS = [
    # PIR-related concepts
    "defection", "defection cascade", "grassroots", "branch chief",
    "third force", "youth voter", "cost of living", "undecided voters",
    "PKR unity", "damage control", "solo bid", "56 seats",
    "seat negotiation", "PH pact", "BERSAMA membership",
    "candidate recruitment", "Sabah PKR", "BN Johor", "PKR Johor",

    # Government policies
    "MADANI", "Ekonomi MADANI", "Malaysia MADANI", "Malaysia Madani",
    "Keluarga Malaysia", "NETR", "National Energy Transition",
    "Unity Government", "unity government",
    "Reformasi",
    "Kleptocracy",
    "Anti-hopping law", "anti-hopping law",
    "Subsidy rationalisation", "subsidy rationalisation",
    "Undi18", "Automatic voter registration",
    "Digital economy", "Digital transformation", "digital transformation",

    # Political themes
    "politics of hatred", "racism", "perkauman", "perpaduan",
    "national unity", "turnout", "voter turnout",

    # Economic concepts
    "Inflation", "inflation", "budget cuts", "food subsidies",
    "fertiliser price", "pork supply", "subsidised diesel",
    "renewable energy", "AI", "artificial intelligence",

    # Healthcare concepts
    "health insurance", "MediAsas", "MHIT", "medical inflation",
    "doctor shortage", "emergency triage", "community pharmacies",
    "harm reduction", "abortion", "women's rights", "gender equality",

    # Other
    "immigrant rights", "copyright", "copyright Act",
    "constituency", "hot pan", "deposits",
    "deals damage", "wake-up call", "wiped out",
    "MCA trumps DAP", "healthcare facilities", "water supply",
    "transport", "state visit",
]

# ============================================================================
# Entity Extraction Functions
# ============================================================================

def extract_entities_from_text(text):
    """Extract entities using pattern matching against known entity lists."""
    entities = {
        "PERSON": set(),
        "ORGANIZATION": set(),
        "LOCATION": set(),
        "EVENT": set(),
        "CONCEPT": set()
    }

    if not text:
        return entities

    # Extract PERSON entities
    for person in KNOWN_PERSONS:
        if re.search(r'\b' + re.escape(person) + r'\b', text, re.IGNORECASE):
            entities["PERSON"].add(person)

    # Extract ORGANIZATION entities
    for org in KNOWN_ORGANIZATIONS:
        if re.search(r'\b' + re.escape(org) + r'\b', text, re.IGNORECASE):
            entities["ORGANIZATION"].add(org)

    # Extract LOCATION entities
    for loc in KNOWN_LOCATIONS:
        if re.search(r'\b' + re.escape(loc) + r'\b', text, re.IGNORECASE):
            entities["LOCATION"].add(loc)

    # Extract EVENT entities
    for event in KNOWN_EVENTS:
        if re.search(r'\b' + re.escape(event) + r'\b', text, re.IGNORECASE):
            entities["EVENT"].add(event)

    # Extract CONCEPT entities
    for concept in KNOWN_CONCEPTS:
        if re.search(r'\b' + re.escape(concept) + r'\b', text, re.IGNORECASE):
            entities["CONCEPT"].add(concept)

    return entities

def _entity_to_str(entity):
    """Convert entity value (str or dict) to a string."""
    if isinstance(entity, str):
        return entity
    elif isinstance(entity, dict):
        # Try common keys for the entity name
        for key in ("name", "value", "text", "title", "entity", "label"):
            if key in entity and entity[key]:
                return str(entity[key])
        return str(entity)
    else:
        return str(entity)

def extract_from_pre_collected(source_entities_data):
    """Extract entities from pre-collected entity data in the source JSON."""
    entities = {
        "PERSON": set(),
        "ORGANIZATION": set(),
        "LOCATION": set(),
        "EVENT": set(),
        "CONCEPT": set()
    }

    if not isinstance(source_entities_data, dict):
        return entities

    for entity_type, values in source_entities_data.items():
        if not isinstance(values, list):
            continue
        for entity in values:
            entity_str = _entity_to_str(entity)
            if not entity_str:
                continue
            if entity_type in ["politicians", "candidates"]:
                entities["PERSON"].add(entity_str)
            elif entity_type == "constituencies":
                entities["LOCATION"].add(entity_str)
            elif entity_type == "coalitions":
                entities["ORGANIZATION"].add(entity_str)
            elif entity_type == "events":
                entities["EVENT"].add(entity_str)
            elif entity_type == "hot_seats":
                entities["LOCATION"].add(entity_str)

    return entities

def match_pir_keywords(text, pir_keywords):
    """Match PIR keywords against text content."""
    pir_matches = defaultdict(list)
    if not text:
        return dict(pir_matches)

    text_lower = text.lower()

    for pir_id, keywords in pir_keywords.items():
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword.lower()) + r'\b', text_lower):
                if keyword not in pir_matches[pir_id]:
                    pir_matches[pir_id].append(keyword)

    return dict(pir_matches)

def extract_dynamic_entities(text):
    """Extract additional entities using regex patterns for better coverage."""
    entities = {
        "PERSON": set(),
        "ORGANIZATION": set(),
        "LOCATION": set(),
        "EVENT": set(),
        "CONCEPT": set()
    }

    if not text:
        return entities

    # Extract titles + names (Datuk/Datuk Seri/Tan Sri/Tun + Name)
    title_patterns = [
        r'(Datuk\s+Seri\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
        r'(Tan\s+Sri\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
        r'(Tun\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
        r'(Datuk\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
    ]
    for pattern in title_patterns:
        for match in re.findall(pattern, text):
            if match and len(match) > 8:
                entities["PERSON"].add(match)

    # Extract constituency references (N## format)
    for match in re.findall(r'\b(N\d{1,2}\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', text):
        entities["LOCATION"].add(match)

    # Extract event patterns
    event_patterns = [
        r'(State\s+election|State\s+polls|PRN\s+\w+)',
        r'(General\s+Election|GE\d+|By[-\s]?election)',
        r'(Parliament\s+session|Parliamentary\s+sitting)',
        r'(Cabinet\s+reshuffle|Cabinet\s+meeting)',
        r'(Budget\s+\d{4})',
    ]
    for pattern in event_patterns:
        for match in re.findall(pattern, text):
            normalized = match.strip()
            if normalized and normalized.lower() not in [e.lower() for e in entities["EVENT"]]:
                entities["EVENT"].add(normalized)

    return entities

# ============================================================================
# Main Processing
# ============================================================================

def find_latest_timestamp():
    """Find the latest collection timestamp from raw directory."""
    files = os.listdir(RAW_DIR)
    timestamps = set()
    for f in files:
        # Extract timestamp prefix (e.g., 2026-07-14T081151+08)
        match = re.match(r'(\d{4}-\d{2}-\d{2}T\d{6}Z)_', f)
        if match:
            timestamps.add(match.group(1))
    if not timestamps:
        return None
    return sorted(timestamps, reverse=True)[0]

def process_collection(timestamp, pir_keywords):
    """Process all source files for a given collection timestamp."""
    all_entities = {
        "PERSON": set(),
        "ORGANIZATION": set(),
        "LOCATION": set(),
        "EVENT": set(),
        "CONCEPT": set()
    }

    all_pir_matches = defaultdict(set)
    source_breakdown = []

    # Find all individual source JSON files for this timestamp
    source_files = sorted([
        f for f in os.listdir(RAW_DIR)
        if f.startswith(f"{timestamp}_") and f.endswith(".json")
        and "political_collection" not in f
        and "source_manifest" not in f
    ])

    # Also find the combined collection file
    combined_file = f"{timestamp}_political_collection_25sources_OPERATIONAL.json"
    combined_path = os.path.join(RAW_DIR, combined_file)
    has_combined = os.path.exists(combined_path)

    if not source_files and not has_combined:
        print(f"ERROR: No source files found for timestamp {timestamp}")
        return None

    # If we have the combined file, prefer it (contains all sources with full_content)
    if has_combined:
        print(f"Processing combined collection: {combined_file}")
        with open(combined_path, 'r', encoding='utf-8') as f:
            combined_data = json.load(f)

        results = combined_data.get("results", [])
        print(f"  Found {len(results)} source results in combined file")

        for source in results:
            source_name = source.get("source", "Unknown")
            source_status = source.get("status", "unknown")
            source_intel_score = source.get("intelligence_score", 0)
            source_pol_headlines = source.get("political_headlines_count", 0)
            source_entities_data = source.get("entities", {})
            full_content = source.get("full_content", "")
            headlines = source.get("headlines", [])
            political_headlines = source.get("political_headlines", [])

            # Combine all text
            all_text = full_content + " " + " ".join(headlines) + " " + " ".join(political_headlines)

            # Extract from pre-collected entities
            pre_entities = extract_from_pre_collected(source_entities_data)

            # Extract from text content
            text_entities = extract_entities_from_text(all_text)

            # Extract dynamic entities
            dynamic_entities = extract_dynamic_entities(all_text)

            # Merge all extracted entities
            source_all_entities = {
                "PERSON": pre_entities["PERSON"] | text_entities["PERSON"] | dynamic_entities["PERSON"],
                "ORGANIZATION": pre_entities["ORGANIZATION"] | text_entities["ORGANIZATION"],
                "LOCATION": pre_entities["LOCATION"] | text_entities["LOCATION"] | dynamic_entities["LOCATION"],
                "EVENT": pre_entities["EVENT"] | text_entities["EVENT"] | dynamic_entities["EVENT"],
                "CONCEPT": text_entities["CONCEPT"] | dynamic_entities["CONCEPT"],
            }

            # Aggregate into global set
            for entity_type, entity_set in source_all_entities.items():
                all_entities[entity_type].update(entity_set)

            # PIR matching for this source
            source_pir_matches = match_pir_keywords(all_text, pir_keywords)
            for pir_id, keywords in source_pir_matches.items():
                all_pir_matches[pir_id].update(keywords)

            # Build source breakdown entry
            entity_counts = {k: len(v) for k, v in source_all_entities.items()}
            entity_types_found = [k for k, v in source_all_entities.items() if len(v) > 0]

            source_breakdown.append({
                "source": source_name,
                "status": source_status,
                "intelligence_score": source_intel_score,
                "political_headlines_count": source_pol_headlines,
                "content_length": len(full_content),
                "entities_found": entity_counts,
                "entity_types_found": sorted(entity_types_found),
                "pir_matches": source_pir_matches
            })

            print(f"  {source_name}: {sum(entity_counts.values())} entities "
                  f"(P:{entity_counts['PERSON']} O:{entity_counts['ORGANIZATION']} "
                  f"L:{entity_counts['LOCATION']} E:{entity_counts['EVENT']} "
                  f"C:{entity_counts['CONCEPT']}) "
                  f"| PIRs: {list(source_pir_matches.keys()) if source_pir_matches else 'none'}")

    else:
        # Process individual source files
        print(f"Processing {len(source_files)} individual source files")
        for source_file in source_files:
            source_path = os.path.join(RAW_DIR, source_file)
            print(f"  Processing: {source_file}")

            with open(source_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            source_name = data.get("source", "Unknown")
            source_status = data.get("status", "unknown")
            source_intel_score = data.get("intelligence_score", 0)
            source_pol_headlines = data.get("political_headlines_count", 0)
            source_entities_data = data.get("entities", {})
            full_content = data.get("full_content", "")
            headlines = data.get("headlines", [])
            political_headlines = data.get("political_headlines", [])

            all_text = full_content + " " + " ".join(headlines) + " " + " ".join(political_headlines)

            pre_entities = extract_from_pre_collected(source_entities_data)
            text_entities = extract_entities_from_text(all_text)
            dynamic_entities = extract_dynamic_entities(all_text)

            source_all_entities = {
                "PERSON": pre_entities["PERSON"] | text_entities["PERSON"] | dynamic_entities["PERSON"],
                "ORGANIZATION": pre_entities["ORGANIZATION"] | text_entities["ORGANIZATION"],
                "LOCATION": pre_entities["LOCATION"] | text_entities["LOCATION"] | dynamic_entities["LOCATION"],
                "EVENT": pre_entities["EVENT"] | text_entities["EVENT"] | dynamic_entities["EVENT"],
                "CONCEPT": text_entities["CONCEPT"] | dynamic_entities["CONCEPT"],
            }

            for entity_type, entity_set in source_all_entities.items():
                all_entities[entity_type].update(entity_set)

            source_pir_matches = match_pir_keywords(all_text, pir_keywords)
            for pir_id, keywords in source_pir_matches.items():
                all_pir_matches[pir_id].update(keywords)

            entity_counts = {k: len(v) for k, v in source_all_entities.items()}
            entity_types_found = [k for k, v in source_all_entities.items() if len(v) > 0]

            source_breakdown.append({
                "source": source_name,
                "status": source_status,
                "intelligence_score": source_intel_score,
                "political_headlines_count": source_pol_headlines,
                "content_length": len(full_content),
                "entities_found": entity_counts,
                "entity_types_found": sorted(entity_types_found),
                "pir_matches": source_pir_matches
            })

    # Count collection stats
    total_sources = len(source_breakdown)
    successful_sources = sum(1 for s in source_breakdown if s["status"] == "success")
    failed_sources = sum(1 for s in source_breakdown if s["status"] == "failed")

    return {
        "entities": {k: sorted(list(v)) for k, v in all_entities.items()},
        "pir_matches": {k: sorted(list(v)) for k, v in all_pir_matches.items()},
        "source_breakdown": source_breakdown,
        "total_sources": total_sources,
        "successful_sources": successful_sources,
        "failed_sources": failed_sources,
    }

def main():
    # Load PIR keywords from config.yaml
    print("=" * 70)
    print("ENTITY EXTRACTION - HOI Political Intelligence")
    print("Classification: TLP:AMBER")
    print("=" * 70)

    pir_keywords = load_pir_keywords(CONFIG_PATH)
    print(f"\nPIR Keywords loaded from: {CONFIG_PATH}")
    print(f"  PIRs defined: {len(pir_keywords)}")
    for pir_id, keywords in sorted(pir_keywords.items()):
        print(f"  {pir_id}: {', '.join(keywords)}")

    # Determine collection timestamp
    if len(sys.argv) > 1:
        timestamp = sys.argv[1]
    else:
        timestamp = find_latest_timestamp()

    if not timestamp:
        print("ERROR: No collection timestamps found in raw directory!")
        return

    print(f"\nProcessing collection cycle: {timestamp}")

    # Process the collection
    results = process_collection(timestamp, pir_keywords)
    if not results:
        print("ERROR: No results extracted!")
        return

    # Build output matching established format
    extraction_timestamp = datetime.utcnow().isoformat() + "Z"
    collection_file = f"{timestamp}_political_collection_25sources_OPERATIONAL.json"

    entity_counts = {k: len(v) for k, v in results["entities"].items()}
    total_entities = sum(entity_counts.values())

    output_data = {
        "extraction_timestamp": extraction_timestamp,
        "source_collection": collection_file,
        "source_timestamp": timestamp,
        "skill_used": "entity-extraction",
        "skill_path": "skills/research/political-monitoring (entity-extraction / Phase 2)",
        "pir_source": str(CONFIG_PATH),
        "pir_keywords_loaded": dict(pir_keywords),
        "extraction_summary": {
            "total_entities": total_entities,
            "entity_counts": entity_counts,
            "pir_coverage": {
                "pirs_with_matches": len(results["pir_matches"]),
                "total_pirs": len(pir_keywords),
                "coverage_percentage": round(len(results["pir_matches"]) / len(pir_keywords) * 100, 1)
            },
            "collection_stats": {
                "total_sources": results["total_sources"],
                "successful": results["successful_sources"],
                "failed": results["failed_sources"]
            }
        },
        "entities": results["entities"],
        "pir_analysis": results["pir_matches"],
        "source_breakdown": results["source_breakdown"]
    }

    # Save output
    ENTITIES_DIR.mkdir(parents=True, exist_ok=True)
    output_filename = f"{timestamp}_entities_extracted.json"
    output_path = ENTITIES_DIR / output_filename

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    # Print summary
    print("\n" + "=" * 70)
    print("ENTITY EXTRACTION COMPLETE")
    print("=" * 70)
    print(f"  Collection: {timestamp}")
    print(f"  Extraction: {extraction_timestamp}")
    print(f"  Sources: {results['total_sources']} total "
          f"({results['successful_sources']} success, {results['failed_sources']} failed)")
    print(f"\n  Total entities: {total_entities}")
    print(f"    PERSON:       {entity_counts['PERSON']}")
    print(f"    ORGANIZATION: {entity_counts['ORGANIZATION']}")
    print(f"    LOCATION:     {entity_counts['LOCATION']}")
    print(f"    EVENT:        {entity_counts['EVENT']}")
    print(f"    CONCEPT:      {entity_counts['CONCEPT']}")
    print(f"\n  PIR Coverage: {len(results['pir_matches'])}/{len(pir_keywords)} "
          f"({round(len(results['pir_matches']) / len(pir_keywords) * 100, 1)}%)")
    for pir_id in sorted(pir_keywords.keys()):
        if pir_id in results["pir_matches"]:
            print(f"    {pir_id}: {', '.join(results['pir_matches'][pir_id])}")
        else:
            print(f"    {pir_id}: (no matches)")
    print(f"\n  Output: {output_path}")
    print("=" * 70)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Entity Extraction Script for Political News Collection
Extracts PERSON, ORGANIZATION, LOCATION, EVENT, and CONCEPT entities
from collected Malaysian political news content.
"""

import json
import re
import os
from datetime import datetime

# Malaysian political entities database
MALAYSIAN_POLITICIANS = [
    "Anwar Ibrahim", "Ahmad Zahid Hamidi", "Hadi Awang", "Muhyiddin Yassin",
    "Rafizi Ramli", "Fahmi Fadzil", "Saifuddin Nasution", "Anthony Loke",
    "Lim Guan Eng", "Onn Hafiz Ghani", "Rezal Merican", "Fadillah Yusof", "Tengku Zafrul"
]

# Political parties and coalitions (ORGANIZATION, not PERSON)
MALAYSIAN_PARTIES = [
    "DAP", "PKR", "UMNO", "PAS", "BERSATU", "AMANAH", "MCA", "MIC", "GPS", "GRS", "PH", "BN", "PN"
]

MALAYSIAN_LOCATIONS = [
    "Malaysia", "Kuala Lumpur", "Putrajaya", "Selangor", "Johor", "Penang",
    "Perak", "Sabah", "Sarawak", "Kedah", "Kelantan", "Terengganu", "Pahang",
    "Negeri Sembilan", "Melaka", "Perlis", "Parliament", "Istana Negara"
]

MALAYSIAN_ORGS = [
    "Government of Malaysia", "Prime Minister's Office", "Parliament",
    "SPRM", "MACC", "BNM", "Khazanah", "Petronas", "Bernama",
    "Parti Keadilan Rakyat", "United Malays National Organisation",
    "Democratic Action Party", "Parti Islam Se-Malaysia"
]

def extract_entities_from_text(text):
    """Extract entities using pattern matching and keyword detection."""
    entities = {
        "PERSON": [],
        "ORGANIZATION": [],
        "LOCATION": [],
        "EVENT": [],
        "CONCEPT": []
    }
    
    # Extract PERSON entities (Malaysian politicians)
    for name in MALAYSIAN_POLITICIANS:
        if re.search(r'\b' + re.escape(name) + r'\b', text, re.IGNORECASE):
            entities["PERSON"].append(name)
    
    # Extract ORGANIZATION entities
    for org in MALAYSIAN_ORGS:
        if re.search(r'\b' + re.escape(org) + r'\b', text, re.IGNORECASE):
            entities["ORGANIZATION"].append(org)
    
    # Extract political parties as ORGANIZATION
    for party in MALAYSIAN_PARTIES:
        if re.search(r'\b' + re.escape(party) + r'\b', text):
            if party not in entities["ORGANIZATION"]:
                entities["ORGANIZATION"].append(party)
    
    # Extract LOCATION entities
    for loc in MALAYSIAN_LOCATIONS:
        if re.search(r'\b' + re.escape(loc) + r'\b', text, re.IGNORECASE):
            entities["LOCATION"].append(loc)
    
    # Extract EVENT entities (patterns) - case sensitive for better accuracy
    event_patterns = [
        r'(Parliament\s+session|Parliamentary\s+sitting|Dewan\s+Rakyat)',
        r'(Press\s+[Cc]onference|Press\s+[Bb]riefing)',
        r'(General\s+Election|GE\d+|By[-\s]?election)',
        r'(Party\s+Assembly|General\s+Assembly|UMNO\s+General\s+Assembly)',
        r'([Cc]ourt\s+case|[Tt]rial|[Hh]earing)',
        r'([Ii]nvestigation|[Pp]robe|[Ii]nquiry)',
        r'(Budget\s+\d{4}|Budget\s+announcement)',
        r'(Cabinet\s+reshuffle|Cabinet\s+meeting)',
        r'(State\s+election|PRN\s+\w+)'
    ]
    for pattern in event_patterns:
        for match in re.findall(pattern, text):
            # Normalize case for display
            normalized = match.strip()
            if normalized and normalized.lower() not in [e.lower() for e in entities["EVENT"]]:
                entities["EVENT"].append(normalized)
    
    # Extract CONCEPT entities (policies, narratives)
    concept_patterns = [
        r'(MADANI|Ekonomi\s+MADANI|Malaysia\s+Madani)',
        r'(Keluarga\s+Malaysia)',
        r'(NETR|National\s+Energy\s+Transition)',
        r'(Reformasi)',
        r'(Unity\s+Government)',
        r'(Kleptocracy)',
        r'(Anti[-\s]?hopping\s+law)',
        r'(Subsidy\s+rationalisation)',
        r'(Cost\s+of\s+living|Inflation)',
        r'(Digital\s+economy|Digital\s+transformation)'
    ]
    for pattern in concept_patterns:
        for match in re.findall(pattern, text, re.IGNORECASE):
            if match not in entities["CONCEPT"]:
                entities["CONCEPT"].append(match)
    
    # Deduplicate
    for key in entities:
        entities[key] = list(set(entities[key]))
    
    return entities

def main():
    # Read combined content
    with open('/tmp/combined_content.txt', 'r') as f:
        content = f.read()
    
    # Extract entities
    entities = extract_entities_from_text(content)
    
    # Create extraction report
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H%M%SZ")
    extraction_report = {
        "extraction_id": f"ext_{timestamp.replace('-', '').replace(':', '').replace('T', '_').replace('Z', '')}",
        "extraction_timestamp": timestamp,
        "source_files": [
            "2026-06-17T000121Z_bernama.json",
            "2026-06-17T000121Z_malaysiakini.json",
            "2026-06-17T000121Z_thestar.json",
            "2026-06-17T000121Z_nst.json",
            "2026-06-17T000121Z_fmt.json",
            "2026-06-17T000121Z_dailyexpress.json",
            "2026-06-17T000121Z_borneopost.json"
        ],
        "sources_count": 7,
        "content_size_chars": len(content),
        "entities": {
            "PERSON": {"count": len(entities["PERSON"]), "items": sorted(entities["PERSON"])},
            "ORGANIZATION": {"count": len(entities["ORGANIZATION"]), "items": sorted(entities["ORGANIZATION"])},
            "LOCATION": {"count": len(entities["LOCATION"]), "items": sorted(entities["LOCATION"])},
            "EVENT": {"count": len(entities["EVENT"]), "items": sorted(entities["EVENT"])},
            "CONCEPT": {"count": len(entities["CONCEPT"]), "items": sorted(entities["CONCEPT"])}
        },
        "total_entities": sum(len(v) for v in entities.values()),
        "raw_content_file": "/tmp/combined_content.txt"
    }
    
    # Save extraction report
    output_dir = "/home/p62operator/.openclaw/workspace-hoi/intelligence/entities"
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(output_dir, f"{timestamp}_entities.json")
    with open(output_file, 'w') as f:
        json.dump(extraction_report, f, indent=2)
    
    # Print summary
    print("=" * 60)
    print("ENTITY EXTRACTION COMPLETE")
    print("=" * 60)
    print(f"Timestamp: {timestamp}")
    print(f"Sources processed: {extraction_report['sources_count']}")
    print(f"Content size: {extraction_report['content_size_chars']:,} chars")
    print(f"Total entities extracted: {extraction_report['total_entities']}")
    print()
    print("Entity Breakdown:")
    for entity_type, data in extraction_report["entities"].items():
        print(f"  {entity_type}: {data['count']}")
        for item in data['items'][:10]:  # Show first 10
            print(f"    - {item}")
        if data['count'] > 10:
            print(f"    ... and {data['count'] - 10} more")
    print()
    print(f"Output saved to: {output_file}")
    print("=" * 60)

if __name__ == "__main__":
    main()

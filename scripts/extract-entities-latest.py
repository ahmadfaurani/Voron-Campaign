#!/usr/bin/env python3
"""
Entity Extraction Script for Political News Collection
Political Monitoring Workstream - HOI Agent
Classification: TLP:AMBER

Extracts entities from collected news content and saves structured results.
Usage: python3 extract-entities.py [timestamp]
       If no timestamp provided, uses the latest collection directory.
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

WORKSPACE = Path("/home/p62operator/.openclaw/workspace-hoi")
RAW_DIR = WORKSPACE / "intelligence" / "raw"
ENTITIES_DIR = WORKSPACE / "intelligence" / "entities"

# Malaysian Political Entity Databases
PERSON_KEYWORDS = [
    # Government leaders
    "Anwar Ibrahim", "Anwar", "Prime Minister", "PM",
    "Ahmad Zahid", "Zahid Hamidi", "Deputy Prime Minister", "DPM",
    "Rafizi Ramli", "Rafizi",
    "Muhyiddin Yassin", "Muhyiddin",
    "Hamzah Zainudin",
    "Onn Hafiz", "Onn",
    "Ismail Sabri",
    "Najib Razak", "Najib",
    "Mahathir", "Tun M",
    
    # Ministers
    "Fadillah Yusof", "Fadillah",
    "Fahmi Fadzil", "Fahmi",
    "Anthony Loke", "Loke",
    "Lim Guan Eng", "Guan Eng",
    "Azmin Ali", "Azmin",
    
    # State leaders
    "Menteri Besar", "MB",
    "Chief Minister",
    
    # Generic
    "Minister", "Deputy Minister", "Senator", "MP", "Member of Parliament"
]

ORG_KEYWORDS = [
    # Coalitions
    "PH", "Pakatan Harapan", "Pakatan Rakyat",
    "BN", "Barisan Nasional",
    "PN", "Perikatan Nasional",
    "GPS", "Gabungan Parti Sarawak",
    "GRS", "Gabungan Rakyat Sabah",
    
    # Parties
    "PKR", "Parti Keadilan Rakyat", "Keadilan",
    "UMNO", "United Malays National Organisation",
    "DAP", "Democratic Action Party",
    "PAS", "Parti Islam Se-Malaysia",
    "BERSATU", "Parti Pribumi Bersatu Malaysia",
    "AMANAH", "Parti Amanah Negara",
    "MCA", "Malaysian Chinese Association",
    "MIC", "Malaysian Indian Congress",
    "BERSAMA",
    
    # Government bodies
    "Parliament", "Dewan Rakyat", "Dewan Negara",
    "Cabinet", "Kabinet",
    "SPR", "Suruhanjaya Pilihan Raya",
    "SPRM", "MACC", "Anti-Corruption Commission",
    "Bank Negara", "BNM",
    "GLC", "Government-linked company",
    
    # Media
    "Bernama", "The Star", "NST", "Malaysiakini", "FMT", "Free Malaysia Today"
]

LOCATION_KEYWORDS = [
    # States
    "Johor", "Selangor", "Penang", "Sabah", "Sarawak", "Perak", "Kedah",
    "Kelantan", "Terengganu", "Pahang", "Perlis", "Melaka", "Negeri Sembilan",
    
    # Cities
    "Kuala Lumpur", "KL", "Putrajaya", "Petaling Jaya", "Johor Bahru",
    "Kota Kinabalu", "Kuching", "Ipoh", "George Town", "Shah Alam",
    
    # Landmarks
    "Parliament House", "Istana Negara", "PWTC", "MACC HQ"
]

EVENT_KEYWORDS = [
    "Parliament session", "Dewan Rakyat sitting", "Budget debate",
    "General Assembly", "AGM", "party congress",
    "Press conference", "Press briefing",
    "Court case", "Trial", "Appeal", "Federal Court",
    "Investigation", "Probe", "SPRM investigation",
    "Election", "GE15", "PRN", "By-election",
    "Scandal", "Corruption", "Arrest", "Charged"
]

CONCEPT_KEYWORDS = [
    "MADANI", "Ekonomi MADANI", "Malaysia MADANI",
    "NETR", "National Energy Transition Roadmap",
    "Keluarga Malaysia",
    "Reformasi",
    "Unity Government",
    "Kleptocracy",
    "Subsidy rationalisation",
    "Cost of living",
    "Anti-hopping law",
    "Undi18", "Automatic voter registration"
]

def extract_entities_from_text(text, source_name):
    """Extract entities from text using keyword matching."""
    entities = {
        "PERSON": [],
        "ORGANIZATION": [],
        "LOCATION": [],
        "EVENT": [],
        "CONCEPT": []
    }
    
    # Normalize text for matching
    text_lower = text.lower()
    
    # Extract PERSON entities
    for keyword in PERSON_KEYWORDS:
        if keyword.lower() in text_lower:
            pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            matches = list(pattern.finditer(text))
            if matches and keyword not in [e["name"] for e in entities["PERSON"]]:
                match = matches[0]
                start = max(0, match.start() - 100)
                end = min(len(text), match.end() + 100)
                context = text[start:end].replace("\n", " ")
                
                entities["PERSON"].append({
                    "name": keyword,
                    "mention_count": len(matches),
                    "context": context[:200],
                    "source": source_name
                })
    
    # Extract ORGANIZATION entities
    for keyword in ORG_KEYWORDS:
        if keyword.lower() in text_lower:
            pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            matches = list(pattern.finditer(text))
            if matches and keyword not in [e["name"] for e in entities["ORGANIZATION"]]:
                match = matches[0]
                start = max(0, match.start() - 100)
                end = min(len(text), match.end() + 100)
                context = text[start:end].replace("\n", " ")
                
                entities["ORGANIZATION"].append({
                    "name": keyword,
                    "mention_count": len(matches),
                    "context": context[:200],
                    "source": source_name
                })
    
    # Extract LOCATION entities
    for keyword in LOCATION_KEYWORDS:
        if keyword.lower() in text_lower:
            pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            matches = list(pattern.finditer(text))
            if matches and keyword not in [e["name"] for e in entities["LOCATION"]]:
                match = matches[0]
                start = max(0, match.start() - 100)
                end = min(len(text), match.end() + 100)
                context = text[start:end].replace("\n", " ")
                
                entities["LOCATION"].append({
                    "name": keyword,
                    "mention_count": len(matches),
                    "context": context[:200],
                    "source": source_name
                })
    
    # Extract EVENT entities
    for keyword in EVENT_KEYWORDS:
        if keyword.lower() in text_lower:
            pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            matches = list(pattern.finditer(text))
            if matches and keyword not in [e["name"] for e in entities["EVENT"]]:
                match = matches[0]
                start = max(0, match.start() - 100)
                end = min(len(text), match.end() + 100)
                context = text[start:end].replace("\n", " ")
                
                entities["EVENT"].append({
                    "name": keyword,
                    "mention_count": len(matches),
                    "context": context[:200],
                    "source": source_name
                })
    
    # Extract CONCEPT entities
    for keyword in CONCEPT_KEYWORDS:
        if keyword.lower() in text_lower:
            pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            matches = list(pattern.finditer(text))
            if matches and keyword not in [e["name"] for e in entities["CONCEPT"]]:
                match = matches[0]
                start = max(0, match.start() - 100)
                end = min(len(text), match.end() + 100)
                context = text[start:end].replace("\n", " ")
                
                entities["CONCEPT"].append({
                    "name": keyword,
                    "mention_count": len(matches),
                    "context": context[:200],
                    "source": source_name
                })
    
    return entities

def merge_entities(all_entities):
    """Merge entities from multiple sources, aggregating mention counts."""
    merged = {
        "PERSON": {},
        "ORGANIZATION": {},
        "LOCATION": {},
        "EVENT": {},
        "CONCEPT": {}
    }
    
    for entities in all_entities:
        for category, items in entities.items():
            for item in items:
                name = item["name"]
                if name not in merged[category]:
                    merged[category][name] = {
                        "name": name,
                        "mention_count": 0,
                        "sources": [],
                        "contexts": []
                    }
                merged[category][name]["mention_count"] += item["mention_count"]
                if item["source"] not in merged[category][name]["sources"]:
                    merged[category][name]["sources"].append(item["source"])
                if item["context"] not in merged[category][name]["contexts"]:
                    merged[category][name]["contexts"].append(item["context"][:200])
    
    # Convert to sorted lists
    result = {}
    for category, items in merged.items():
        result[category] = sorted(
            [{"name": k, **v} for k, v in items.items()],
            key=lambda x: x["mention_count"],
            reverse=True
        )
    
    return result

def main():
    # Get timestamp from argument or find latest collection
    if len(sys.argv) > 1:
        timestamp = sys.argv[1]
        collection_dir = RAW_DIR / timestamp
    else:
        # Find latest collection directory
        dirs = sorted([d for d in RAW_DIR.iterdir() if d.is_dir()], key=lambda x: x.name, reverse=True)
        if dirs:
            collection_dir = dirs[0]
            timestamp = collection_dir.name
        else:
            print("No collection directories found!")
            return
    
    print("=" * 60)
    print("ENTITY EXTRACTION - Political News Collection")
    print("Classification: TLP:AMBER")
    print("=" * 60)
    print(f"\nCollection: {timestamp}")
    print(f"Directory: {collection_dir}")
    
    # Find markdown files (content) or JSON files (Firecrawl format)
    collection_files = list(collection_dir.glob("*.md"))
    if not collection_files:
        collection_files = list(collection_dir.glob("*.json"))
    
    if not collection_files:
        print(f"No collection files found in {collection_dir}")
        return
    
    print(f"\nProcessing {len(collection_files)} collection files...")
    
    all_entities = []
    collection_summary = []
    
    for file_path in collection_files:
        print(f"\n  Processing: {file_path.name}")
        source_name = file_path.stem  # Initialize source_name
        
        try:
            # Extract source name from filename
            source_name = file_path.stem.replace(f"{timestamp}_", "").replace("_", " ").title()
            
            if file_path.suffix == ".md":
                # Read markdown content directly
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            else:
                # Read JSON and extract markdown
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                if "data" in data and "markdown" in data["data"]:
                    content = data["data"]["markdown"]
                elif "content" in data:
                    content = data["content"]
                else:
                    content = str(data)[:50000]
            
            # Extract entities
            entities = extract_entities_from_text(content, source_name)
            all_entities.append(entities)
            
            # Summary
            entity_counts = {cat: len(ents) for cat, ents in entities.items()}
            total_entities = sum(entity_counts.values())
            
            collection_summary.append({
                "source": source_name,
                "file": file_path.name,
                "content_length": len(content),
                "entities_found": total_entities,
                "breakdown": entity_counts
            })
            
            print(f"    Content: {len(content):,} chars")
            print(f"    Entities: {total_entities} (P:{entity_counts['PERSON']} O:{entity_counts['ORGANIZATION']} L:{entity_counts['LOCATION']} E:{entity_counts['EVENT']} C:{entity_counts['CONCEPT']})")
            
        except Exception as e:
            print(f"    ERROR: {e}")
            collection_summary.append({
                "source": source_name,
                "file": file_path.name,
                "status": "error",
                "error": str(e)
            })
    
    # Merge all entities
    print("\n" + "=" * 60)
    print("MERGING ENTITIES ACROSS SOURCES")
    print("=" * 60)
    
    merged_entities = merge_entities(all_entities)
    
    # Create output
    output = {
        "extraction_timestamp": datetime.utcnow().isoformat() + "Z",
        "collection_timestamp": timestamp,
        "sources_processed": len(collection_summary),
        "collection_summary": collection_summary,
        "merged_entities": merged_entities,
        "totals": {
            "PERSON": len(merged_entities["PERSON"]),
            "ORGANIZATION": len(merged_entities["ORGANIZATION"]),
            "LOCATION": len(merged_entities["LOCATION"]),
            "EVENT": len(merged_entities["EVENT"]),
            "CONCEPT": len(merged_entities["CONCEPT"]),
            "TOTAL": sum(len(v) for v in merged_entities.values())
        }
    }
    
    # Save to entities directory
    ENTITIES_DIR.mkdir(parents=True, exist_ok=True)
    output_file = ENTITIES_DIR / f"{timestamp}-entities.json"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Entity extraction complete!")
    print(f"   Output saved to: {output_file}")
    print(f"\n   TOTAL ENTITIES EXTRACTED: {output['totals']['TOTAL']}")
    print(f"   - PERSON: {output['totals']['PERSON']}")
    print(f"   - ORGANIZATION: {output['totals']['ORGANIZATION']}")
    print(f"   - LOCATION: {output['totals']['LOCATION']}")
    print(f"   - EVENT: {output['totals']['EVENT']}")
    print(f"   - CONCEPT: {output['totals']['CONCEPT']}")
    
    # Print top entities
    print("\n" + "=" * 60)
    print("TOP ENTITIES BY MENTION COUNT")
    print("=" * 60)
    
    print("\n📍 TOP PERSONS:")
    for person in merged_entities["PERSON"][:10]:
        print(f"   • {person['name']} ({person['mention_count']} mentions from {len(person['sources'])} sources)")
    
    print("\n🏢 TOP ORGANIZATIONS:")
    for org in merged_entities["ORGANIZATION"][:10]:
        print(f"   • {org['name']} ({org['mention_count']} mentions from {len(org['sources'])} sources)")
    
    print("\n📍 TOP LOCATIONS:")
    for loc in merged_entities["LOCATION"][:10]:
        print(f"   • {loc['name']} ({loc['mention_count']} mentions from {len(loc['sources'])} sources)")
    
    return output

if __name__ == "__main__":
    main()

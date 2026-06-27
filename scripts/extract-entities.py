#!/usr/bin/env python3
"""
Entity Extraction Script
Extracts political entities from collected Malaysian news content
Uses LLM-based extraction via DeerFlow API or local processing
"""

import json
import re
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Configuration
INPUT_DIR = Path("/home/p62operator/.openclaw/workspace-hoi/intelligence/raw")
OUTPUT_DIR = Path("/home/p62operator/.openclaw/workspace-hoi/intelligence/entities")

# Entity categories based on political-monitoring skill
ENTITY_CATEGORIES = {
    "PERSON": {
        "keywords": ["PM", "DPM", "Minister", "Deputy Minister", "MP", "Senator", "President", 
                    "Secretary-General", "Chairman", "CEO", "Ambassador", "MB", "EXCO",
                    "Assemblyman", "Assemblywoman", "Chief Minister", "Governor", "Yang di-Pertuan"],
        "malaysian_names": ["Anwar", "Ibrahim", "Ahmad Zahid", "Fadillah", "Rafizi", "Ramkarpal",
                           "Muhyiddin", "Hadi Awang", "Zahid Hamidi", "Najib", "Mahathir"]
    },
    "ORGANIZATION": {
        "keywords": ["Ministry", "Department", "Agency", "Bernama", "PKR", "UMNO", "DAP", "PAS",
                    "BERSATU", "AMANAH", "MCA", "MIC", "GPS", "GRS", "PH", "BN", "PN", "MUDA",
                    "Petronas", "Khazanah", "SPRM", "PDRM", "Parliament", "Dewan Rakyat"],
        "coalitions": ["PH", "BN", "PN", "GPS", "GRS", "Pakatan Harapan", "Barisan Nasional", 
                      "Perikatan Nasional", "Gagasan Rakyat Sabah"]
    },
    "LOCATION": {
        "keywords": ["Malaysia", "Kuala Lumpur", "Selangor", "Johor", "Penang", "Sabah", "Sarawak",
                    "Perak", "Kedah", "Kelantan", "Terengganu", "Pahang", "Perlis", "Melaka",
                    "Negeri Sembilan", "Putrajaya", "Labuan", "Bintulu", "Kuching", "Kota Kinabalu"],
        "constituencies": ["parliament", "constituency", "DUN", "state assembly"]
    },
    "EVENT": {
        "keywords": ["election", "poll", "vote", "press conference", "Parliament session",
                    "assembly", "congress", "summit", "visit", "meeting", "launch", "announcement",
                    "scandal", "investigation", "court case", "arrest", "raid"],
        "political_events": ["Johor State Election", "party assembly", "general election", "GE15"]
    },
    "CONCEPT": {
        "keywords": ["policy", "reform", "governance", "corruption", "transparency", "accountability",
                    "economy", "subsidy", "tax", "budget", "development", "infrastructure",
                    "unity", "coalition", "defection", "crisis", "stability", "narrative"]
    }
}

# Priority Intelligence Requirements (PIRs) from the skill
PIR_KEYWORDS = {
    "PIR-1": ["PKR", "Johor", "defection", "stability", "state election"],
    "PIR-2": ["BERSAMA", "third force", "new party", "movement"],
    "PIR-3": ["Rafizi", "INVOKE", "faction", "reform"],
    "PIR-4": ["BN", "Johor", "UMNO", "position"],
    "PIR-5": ["youth", "voter", "undi18", "young"],
    "PIR-6": ["PKR", "unity", "reconciliation", "internal"],
    "PIR-7": ["Onn Hafiz", "ambition", "seats"],
    "PIR-8": ["BERSAMA", "growth", "membership", "recruitment"],
    "PIR-9": ["PH", "pact", "seat", "negotiation", "coalition"],
    "PIR-10": ["Sabah", "PKR", "cascade", "GRB"]
}

def extract_entities_from_text(text, source_name):
    """Extract entities from text using pattern matching"""
    entities = {
        "PERSON": [],
        "ORGANIZATION": [],
        "LOCATION": [],
        "EVENT": [],
        "CONCEPT": []
    }
    
    # Simple pattern-based extraction
    # Person names (capitalized words, especially Malaysian politician names)
    person_pattern = r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\b'
    for match in re.finditer(person_pattern, text):
        name = match.group(1)
        # Filter out common non-person matches
        if not any(word in name.upper() for word in ["THE", "AND", "FOR", "WITH", "FROM", "MINISTRY", "PARLIAMENT"]):
            if name not in entities["PERSON"]:
                entities["PERSON"].append(name)
    
    # Organizations
    for keyword in ENTITY_CATEGORIES["ORGANIZATION"]["keywords"]:
        if keyword.lower() in text.lower():
            # Find the actual casing in text
            pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            for match in pattern.finditer(text):
                org_name = text[match.start():match.end()]
                if org_name not in entities["ORGANIZATION"]:
                    entities["ORGANIZATION"].append(org_name)
    
    # Locations
    for keyword in ENTITY_CATEGORIES["LOCATION"]["keywords"]:
        if keyword.lower() in text.lower():
            pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            for match in pattern.finditer(text):
                loc_name = text[match.start():match.end()]
                if loc_name not in entities["LOCATION"]:
                    entities["LOCATION"].append(loc_name)
    
    # Events
    for keyword in ENTITY_CATEGORIES["EVENT"]["keywords"]:
        if keyword.lower() in text.lower():
            pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            for match in pattern.finditer(text):
                event_word = text[match.start():match.end()]
                if event_word not in entities["EVENT"]:
                    entities["EVENT"].append(event_word)
    
    # Concepts
    for keyword in ENTITY_CATEGORIES["CONCEPT"]["keywords"]:
        if keyword.lower() in text.lower():
            pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            for match in pattern.finditer(text):
                concept_word = text[match.start():match.end()]
                if concept_word not in entities["CONCEPT"]:
                    entities["CONCEPT"].append(concept_word)
    
    return entities

def match_pir(entities, text):
    """Match extracted entities to Priority Intelligence Requirements"""
    pir_matches = defaultdict(list)
    text_lower = text.lower()
    
    for pir_id, keywords in PIR_KEYWORDS.items():
        for keyword in keywords:
            if keyword.lower() in text_lower:
                pir_matches[pir_id].append(keyword)
    
    return dict(pir_matches)

def process_collection_file(collection_file):
    """Process the combined collection file and extract entities"""
    print(f"Processing: {collection_file.name}")
    
    with open(collection_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    all_entities = {
        "PERSON": set(),
        "ORGANIZATION": set(),
        "LOCATION": set(),
        "EVENT": set(),
        "CONCEPT": set()
    }
    
    pir_matches = defaultdict(list)
    source_summaries = []
    
    # Process each source
    sources = data.get("sources", [])
    for source in sources:
        if not source.get("success"):
            continue
        
        source_name = source.get("name", "unknown")
        content = source.get("content", "")
        
        if not content:
            continue
        
        # Extract entities from this source
        entities = extract_entities_from_text(content, source_name)
        
        # Merge into all_entities
        for category, entity_list in entities.items():
            all_entities[category].update(entity_list)
        
        # Match PIRs
        source_pirs = match_pir(entities, content)
        for pir_id, keywords in source_pirs.items():
            pir_matches[pir_id].extend(keywords)
        
        # Source summary
        source_summaries.append({
            "name": source_name,
            "content_length": len(content),
            "entities_found": sum(len(v) for v in entities.values()),
            "pir_matches": list(source_pirs.keys())
        })
    
    # Convert sets to lists for JSON serialization
    final_entities = {k: list(v) for k, v in all_entities.items()}
    
    # Deduplicate PIR matches
    final_pirs = {k: list(set(v)) for k, v in pir_matches.items()}
    
    return {
        "extraction_timestamp": datetime.utcnow().isoformat() + "Z",
        "collection_timestamp": data.get("collection_timestamp", "unknown"),
        "sources_processed": len(source_summaries),
        "total_entities": {k: len(v) for k, v in final_entities.items()},
        "entities": final_entities,
        "pir_matches": final_pirs,
        "source_summaries": source_summaries
    }

def main():
    print("=" * 60)
    print("ENTITY EXTRACTION")
    print(f"Timestamp: {datetime.utcnow().isoformat()}Z")
    print("=" * 60)
    
    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Find the latest collection file
    collection_files = list(INPUT_DIR.glob("*_political_collection.json"))
    if not collection_files:
        print("ERROR: No political collection files found")
        return None
    
    # Get the most recent collection file
    latest_collection = max(collection_files, key=lambda x: x.stat().st_mtime)
    
    # Process the collection
    result = process_collection_file(latest_collection)
    
    if result:
        # Save entity extraction results
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H%M%SZ")
        output_file = OUTPUT_DIR / f"{timestamp}_entities.json"
        
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print(f"\nEntities extracted:")
        for category, count in result["total_entities"].items():
            print(f"  {category}: {count}")
        
        print(f"\nPIR matches:")
        for pir_id, keywords in result["pir_matches"].items():
            print(f"  {pir_id}: {', '.join(keywords[:5])}{'...' if len(keywords) > 5 else ''}")
        
        print(f"\nOutput saved: {output_file.name}")
        print("=" * 60)
        
        return result
    
    return None

if __name__ == "__main__":
    result = main()
    
    if result:
        # Print sample entities for verification
        print("\nSample extracted entities:")
        print(f"  PERSON: {result['entities']['PERSON'][:10]}")
        print(f"  ORGANIZATION: {result['entities']['ORGANIZATION'][:10]}")
        print(f"  LOCATION: {result['entities']['LOCATION'][:10]}")

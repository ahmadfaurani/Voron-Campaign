#!/usr/bin/env python3
"""
VoronDRQ Stakeholder Name Extraction Script
Extracts C-suite and stakeholder names from annual reports, LinkedIn, and corporate websites
TLP:AMBER - Commercial Intelligence
"""

import csv
import json
import subprocess
from pathlib import Path
from datetime import datetime

# Configuration
WORKSPACE = Path("/home/p62operator/.openclaw/workspace-hoi")
VORON_DIR = WORKSPACE / "Voron-Campaign"
PROSPECT_CSV = VORON_DIR / "prospects" / "prospect-database-7stakeholders.csv"
OUTPUT_FILE = VORON_DIR / "prospects" / "stakeholder-names-extracted.csv"
OPENOSINT_ENV = WORKSPACE / "openosint-activate.sh"

# Tier 1 Banks with known websites
BANKS = {
    "Maybank Berhad": {
        "domain": "maybank.com.my",
        "search_terms": ["Maybank CFO", "Maybank CIO", "Maybank Group Chief"],
    },
    "CIMB Bank Berhad": {
        "domain": "cimb.com",
        "search_terms": ["CIMB CFO", "CIMB CIO", "CIMB Chief Financial"],
    },
    "Hong Leong Bank Berhad": {
        "domain": "hlbb.com.my",
        "search_terms": ["Hong Leong Bank CFO", "HLBB CIO"],
    },
    "RHB Bank Berhad": {
        "domain": "rhbbank.com",
        "search_terms": ["RHB Bank CFO", "RHB CIO"],
    },
    "AmBank (M) Berhad": {
        "domain": "ambankgroup.com",
        "search_terms": ["AmBank CFO", "AmBank CIO"],
    },
    "Bank Islam Malaysia Berhad": {
        "domain": "bankislam.com.my",
        "search_terms": ["Bank Islam CFO", "Bank Islam CIO"],
    },
    "OCBC Bank (Malaysia) Berhad": {
        "domain": "ocbc.com.my",
        "search_terms": ["OCBC Malaysia CFO", "OCBC CIO"],
    },
    "UOB Malaysia Berhad": {
        "domain": "uob.com.my",
        "search_terms": ["UOB Malaysia CFO", "UOB CIO"],
    },
}

STAKEHOLDER_ROLES = ["CISO", "GRC", "CFO", "CRO", "Compliance", "CIO", "Audit"]

def run_openosint_search(query):
    """Run OpenOSINT web search for stakeholder names"""
    try:
        cmd = [
            "bash", "-c",
            f"source {OPENOSINT_ENV} && openosint --provider openai search-dorks-live '{query}'"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        return result.stdout
    except Exception as e:
        return f"ERROR: {e}"

def extract_names_from_search(search_results, bank_name, role):
    """Extract potential names from search results"""
    names = []
    # Simple pattern matching for Malaysian names
    # e.g., "Dato' Abdul Rahman", "Tan Sri Lee", "Dr. Sarah Wong"
    import re
    patterns = [
        r"(Dato'|Datuk|Tan Sri|Dr\.|Mr\.|Ms\.)\s+([A-Z][a-z]+\s+)+[A-Z][a-z]+",
        r"([A-Z][a-z]+\s+[A-Z][a-z]+)",
    ]
    for pattern in patterns:
        matches = re.findall(pattern, search_results)
        for match in matches:
            if isinstance(match, tuple):
                name = "".join(match)
            else:
                name = match
            # Filter out common false positives
            if not any(x in name.lower() for x in ["bank", "berhad", "company", "limited"]):
                names.append(name)
    return names[:3]  # Limit to top 3 candidates per role

def main():
    print("=== VoronDRQ Stakeholder Name Extraction ===")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Input: {PROSPECT_CSV}")
    print(f"Output: {OUTPUT_FILE}")
    print()
    
    # Read existing prospect database
    prospects = []
    with open(PROSPECT_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            prospects.append(row)
    
    print(f"Loaded {len(prospects)} institutions")
    print()
    
    # Process only Tier 1 banks first (top 10)
    tier1_banks = list(BANKS.keys())[:8]
    print(f"Extracting names for {len(tier1_banks)} Tier 1 banks...")
    print()
    
    extraction_results = []
    
    for bank_name in tier1_banks:
        print(f"→ Processing: {bank_name}")
        bank_info = BANKS[bank_name]
        bank_data = {
            "Institution": bank_name,
            "CISO": "",
            "GRC": "",
            "CFO": "",
            "CRO": "",
            "Compliance": "",
            "CIO": "",
            "Audit": "",
            "Source": "",
            "Confidence": "",
        }
        
        # Search for each stakeholder role
        for role in STAKEHOLDER_ROLES:
            search_query = f"{bank_name} {role} 2024 2025"
            print(f"  - Searching: {role}")
            
            # Run search
            results = run_openosint_search(search_query)
            
            # Extract names
            names = extract_names_from_search(results, bank_name, role)
            
            if names:
                bank_data[role] = names[0]  # Take top candidate
                bank_data["Source"] = "OpenOSINT search"
                bank_data["Confidence"] = "MEDIUM"
                print(f"    ✓ Found: {names[0]}")
            else:
                print(f"    - No name found")
        
        extraction_results.append(bank_data)
        print()
    
    # Write results
    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ["Institution"] + STAKEHOLDER_ROLES + ["Source", "Confidence"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(extraction_results)
    
    print(f"=== Extraction Complete ===")
    print(f"Output: {OUTPUT_FILE}")
    print(f"Institutions processed: {len(extraction_results)}")
    print(f"Total stakeholder slots: {len(extraction_results) * 7}")
    
    # Count filled slots
    filled = sum(1 for row in extraction_results for role in STAKEHOLDER_ROLES if row[role])
    print(f"Names extracted: {filled}/{len(extraction_results) * 7}")

if __name__ == "__main__":
    main()

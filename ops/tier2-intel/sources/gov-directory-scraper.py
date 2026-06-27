#!/usr/bin/env python3
"""
HOI Agent — Government Directory Scraper
Operation: TIER2-INTEL
Purpose: Extract agency names, types, websites from Malaysian government portals
Classification: TLP:AMBER
"""

import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import os

# Configuration
OUTPUT_DIR = "../evidence/Agency-Profiles/"
LOG_FILE = "../evidence/chain-of-custody.log"
OUTPUT_CSV = "../evidence/Agency-Profiles/raw-agencies.csv"

# Target URLs (Malaysian Government Directories)
TARGET_URLS = [
    {
        "name": "MyGovernment Portal - Federal Agencies",
        "url": "https://www.malaysia.gov.my/portal/content/30002",
        "type": "Federal"
    },
    {
        "name": "JDN - Digital Negara Agencies",
        "url": "https://www.jdn.gov.my/",
        "type": "Federal"
    },
    {
        "name": "NACSA - Critical Infrastructure List",
        "url": "https://www.nacsa.gov.my/",
        "type": "Critical Infrastructure"
    }
]

# Agency categories for classification
AGENCY_CATEGORIES = {
    "Kementerian": "Ministry",
    "Jabatan": "Department",
    "Agensi": "Agency",
    "Lembaga": "Board/Authority",
    "Suruhanjaya": "Commission",
    "Majlis": "Council",
    "Institut": "Institute",
    "Universiti": "University",
    "Negeri": "State"
}

def log_action(action, agency_name="", status=""):
    """Log action to chain-of-custody file"""
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    log_entry = f"[{timestamp}] HOI-Agent | {action} | {agency_name} | {status}\n"
    
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)
    
    print(f"LOG: {log_entry.strip()}")

def classify_agency(name):
    """Classify agency type based on name prefix"""
    for prefix, category in AGENCY_CATEGORIES.items():
        if prefix.lower() in name.lower():
            return category
    return "Other"

def extract_agencies_from_url(url_data):
    """Extract agency list from a government portal URL"""
    agencies = []
    
    try:
        print(f"Scraping: {url_data['name']} ({url_data['url']})")
        log_action("SCRAPER_START", url_data['name'], "In Progress")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (HOI-Agent; Intelligence Collection; TLP:AMBER)'
        }
        
        response = requests.get(url_data['url'], headers=headers, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Try to find agency listings (common patterns)
        agency_elements = soup.find_all(['li', 'div', 'a'], class_=lambda x: x and ('agency' in x.lower() or 'department' in x.lower() or 'jabatan' in x.lower()))
        
        for element in agency_elements[:50]:  # Limit to 50 per source
            text = element.get_text(strip=True)
            if len(text) > 10 and len(text) < 200:  # Filter noise
                agency_name = text
                agency_type = classify_agency(agency_name)
                
                agencies.append({
                    "name": agency_name,
                    "type": agency_type,
                    "source": url_data['name'],
                    "source_url": url_data['url'],
                    "category": url_data['type'],
                    "confidence": "Medium",
                    "collection_date": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
                })
        
        log_action("SCRAPER_COMPLETE", url_data['name'], f"Extracted {len(agencies)} agencies")
        
    except Exception as e:
        log_action("SCRAPER_ERROR", url_data['name'], str(e))
        print(f"Error scraping {url_data['url']}: {str(e)}")
    
    return agencies

def save_to_csv(agencies, output_file):
    """Save extracted agencies to CSV"""
    if not agencies:
        print("No agencies to save")
        return
    
    fieldnames = ['name', 'type', 'source', 'source_url', 'category', 'confidence', 'collection_date']
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(agencies)
    
    print(f"Saved {len(agencies)} agencies to {output_file}")
    log_action("CSV_SAVED", "All Agencies", f"{len(agencies)} records")

def main():
    """Main execution"""
    print("=" * 60)
    print("HOI Agent — Government Directory Scraper")
    print("Operation: TIER2-INTEL")
    print("Classification: TLP:AMBER")
    print("=" * 60)
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    all_agencies = []
    
    # Scrape each target URL
    for url_data in TARGET_URLS:
        agencies = extract_agencies_from_url(url_data)
        all_agencies.extend(agencies)
    
    # Deduplicate by agency name
    seen = set()
    unique_agencies = []
    for agency in all_agencies:
        if agency['name'] not in seen:
            seen.add(agency['name'])
            unique_agencies.append(agency)
    
    print(f"\nTotal unique agencies: {len(unique_agencies)}")
    
    # Save to CSV
    save_to_csv(unique_agencies, OUTPUT_CSV)
    
    # Summary
    print("\n" + "=" * 60)
    print("SCRAPING COMPLETE")
    print("=" * 60)
    print(f"Total agencies extracted: {len(unique_agencies)}")
    print(f"Output file: {OUTPUT_CSV}")
    print(f"Log file: {LOG_FILE}")
    
    # Category breakdown
    categories = {}
    for agency in unique_agencies:
        cat = agency['type']
        categories[cat] = categories.get(cat, 0) + 1
    
    print("\nCategory Breakdown:")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}")

if __name__ == "__main__":
    main()

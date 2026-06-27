#!/usr/bin/env python3
"""
PDRM IO Contact Extraction Script
Uses Firecrawl API to scrape Malaysian news outlets for police appeal articles
with Investigating Officer contact details.

Classification: TLP:AMBER
Workspace: /home/p62operator/.openclaw/workspace-hoi/
"""

import json
import requests
import re
from datetime import datetime
from typing import Optional

FIRECRAWL_BASE = "http://localhost:3002"
OUTPUT_FILE = "/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-firecrawl-results.json"

# Target outlets and search URLs (using site search or category pages)
TARGETS = [
    {
        "name": "malaysiagazette",
        "search_url": "https://malaysiagazette.com/?s=polis+cari+bantu+siasatan",
        "domain": "malaysiagazette.com"
    },
    {
        "name": "hmetro",
        "search_url": "https://www.hmetro.com.my/search/polis%20cari%20bantu%20siasatan",
        "domain": "hmetro.com.my"
    },
    {
        "name": "bernama",
        "search_url": "https://www.bernama.com/bm/search.php?q=polis+cari",
        "domain": "bernama.com"
    },
    {
        "name": "buletintv3",
        "search_url": "https://www.buletintv3.my/nasional?query=polis+cari",
        "domain": "buletintv3.my"
    },
    {
        "name": "freemalaysiatoday",
        "search_url": "https://www.freemalaysiatoday.com/search/polis+cari",
        "domain": "freemalaysiatoday.com"
    },
    {
        "name": "melakahariini",
        "search_url": "https://www.melakahariini.my/?s=polis+cari",
        "domain": "melakahariini.my"
    }
]

# Known article URLs from previous extraction (for re-scraping and validation)
KNOWN_ARTICLES = [
    "https://malaysiagazette.com/2026/06/04/polis-cari-marvin-loo-jia-an-bantu-siasatan/",
    "https://www.buletintv3.my/nasional/polis-cari-celine-bantu-siasatan-babit-kes-dadah/",
    "https://www.melakahariini.my/polis-cari-lelaki-36-tahun-bantu-siasatan-kes-jenayah/",
    "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2023/09/01/polis-cari-suspek-bantu-siasatan-kes-rogol-berkumpulan/",
    "https://www.thestar.com.my/news/nation/2026/02/20/police-hunt-36-wanted-individuals"
]

def scrape_url(url: str) -> Optional[dict]:
    """Scrape a single URL using Firecrawl API v1"""
    try:
        response = requests.post(
            f"{FIRECRAWL_BASE}/v1/scrape",
            json={
                "url": url,
                "formats": ["markdown"],
                "onlyMainContent": True,
                "waitFor": 2000
            },
            timeout=30
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("success") and "data" in data:
                return data["data"]
        else:
            print(f"Error scraping {url}: {response.status_code} - {response.text[:200]}")
            return None
    except Exception as e:
        print(f"Exception scraping {url}: {e}")
        return None

def extract_io_contacts(content: str, url: str) -> list:
    """Extract IO contact details from article content"""
    contacts = []
    
    # Pattern for officer names with ranks
    officer_patterns = [
        r'(Insp\.|Inspektor|Sarjan|Sjn\.|DSP|Deputi Superintendan|PPP)\s+([A-Z][a-z]+\.?\s*[A-Z][a-z]+)',
        r'(Insp\.|Inspektor|Sarjan|Sjn\.|DSP)\s+([A-Z][A-Z\s]+[A-Z])',
    ]
    
    # Phone number patterns
    mobile_pattern = r'(01[0-9]-\d{6,7})'
    office_pattern = r'(0[3-9]-\d{6,7})'
    ext_pattern = r'(sambungan|ext\.?|ext)\s*(\d{3,4})'
    
    # Extract officers
    officers = []
    for pattern in officer_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        for match in matches:
            rank = match[0]
            name = match[1]
            officers.append({"rank": rank, "name": name})
    
    # Extract phone numbers
    mobiles = re.findall(mobile_pattern, content)
    offices = re.findall(office_pattern, content)
    extensions = re.findall(ext_pattern, content, re.IGNORECASE)
    
    # Try to associate officers with phone numbers
    if officers:
        for i, officer in enumerate(officers):
            contact = {
                "officer_name": officer["name"],
                "officer_rank": officer["rank"],
                "contact_mobile": mobiles[i] if i < len(mobiles) else None,
                "contact_office": offices[i] if i < len(offices) else (offices[0] if offices else None),
                "extension": extensions[i][1] if i < len(extensions) and extensions else None,
                "source_url": url,
                "extracted_at": datetime.now().isoformat()
            }
            contacts.append(contact)
    elif mobiles or offices:
        # No officer name found, but phone numbers exist
        contact = {
            "officer_name": "Unknown",
            "officer_rank": "Unknown",
            "contact_mobile": mobiles[0] if mobiles else None,
            "contact_office": offices[0] if offices else None,
            "extension": extensions[0][1] if extensions else None,
            "source_url": url,
            "extracted_at": datetime.now().isoformat()
        }
        contacts.append(contact)
    
    return contacts

def main():
    results = {
        "extraction_date": datetime.now().isoformat(),
        "total_articles": 0,
        "total_contacts": 0,
        "by_outlet": {},
        "contacts": []
    }
    
    print("=" * 60)
    print("PDRM IO Contact Extraction - Firecrawl")
    print("=" * 60)
    
    # First, scrape known articles
    print(f"\n📰 Scraping {len(KNOWN_ARTICLES)} known articles...")
    for url in KNOWN_ARTICLES:
        print(f"  → {url}")
        data = scrape_url(url)
        if data and "markdown" in data:
            contacts = extract_io_contacts(data["markdown"], url)
            if contacts:
                print(f"     ✓ Found {len(contacts)} contact(s)")
                results["contacts"].extend(contacts)
                results["total_articles"] += 1
                results["total_contacts"] += len(contacts)
            else:
                print(f"     ⚠ No contacts found")
        else:
            print(f"     ✗ Failed to scrape")
    
    # Then, try search result pages (limited)
    print(f"\n🔍 Attempting search result pages...")
    for target in TARGETS[:3]:  # Limit to first 3 outlets
        print(f"  → {target['name']}: {target['search_url']}")
        data = scrape_url(target['search_url'])
        if data and "markdown" in data:
            # Extract any links from the search results
            links = re.findall(r'https?://[^\s<>"{}|\\^`\[\]]+', data["markdown"])
            article_links = [l for l in links if target['domain'] in l and 'polis' in l.lower()]
            print(f"     Found {len(article_links)} potential article links")
            
            # Scrape first 2 article links
            for article_url in article_links[:2]:
                print(f"        → {article_url}")
                article_data = scrape_url(article_url)
                if article_data and "markdown" in article_data:
                    contacts = extract_io_contacts(article_data["markdown"], article_url)
                    if contacts:
                        print(f"           ✓ Found {len(contacts)} contact(s)")
                        results["contacts"].extend(contacts)
                        results["total_articles"] += 1
                        results["total_contacts"] += len(contacts)
    
    # Aggregate by outlet
    for contact in results["contacts"]:
        domain = contact["source_url"].split('/')[2]
        if domain not in results["by_outlet"]:
            results["by_outlet"][domain] = {"count": 0, "contacts": []}
        results["by_outlet"][domain]["count"] += 1
        results["by_outlet"][domain]["contacts"].append(contact)
    
    # Save results
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print("\n" + "=" * 60)
    print("📊 EXTRACTION SUMMARY")
    print("=" * 60)
    print(f"Total Articles Processed: {results['total_articles']}")
    print(f"Total IO Contacts Found:  {results['total_contacts']}")
    print(f"\nBy Outlet:")
    for outlet, data in results["by_outlet"].items():
        print(f"  • {outlet}: {data['count']} contacts")
    print(f"\n💾 Results saved to: {OUTPUT_FILE}")
    print("=" * 60)

if __name__ == "__main__":
    main()

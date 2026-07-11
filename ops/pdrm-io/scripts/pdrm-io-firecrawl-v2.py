#!/usr/bin/env python3
"""
PDRM IO Contact Extraction Script v2
Improved regex patterns for better officer name and phone number extraction.

Classification: TLP:AMBER
Workspace: /home/p62operator/.openclaw/workspace-hoi/
"""

import json
import requests
import re
from datetime import datetime
from typing import Optional, List, Dict

FIRECRAWL_BASE = "http://localhost:3002"
OUTPUT_FILE = "/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-firecrawl-v2.json"

# Known article URLs to scrape
KNOWN_ARTICLES = [
    "https://malaysiagazette.com/2026/06/04/polis-cari-marvin-loo-jia-an-bantu-siasatan/",
    "https://www.buletintv3.my/nasional/polis-cari-celine-bantu-siasatan-babit-kes-dadah/",
    "https://www.melakahariini.my/polis-cari-lelaki-36-tahun-bantu-siasatan-kes-jenayah/",
    "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2023/09/01/polis-cari-suspek-bantu-siasatan-kes-rogol-berkumpulan/",
    "https://www.hmetro.com.my/mutakhir/2026/02/1324976/polis-cari-mohamad-syazwan-bantu-siasatan-kes-dadah",
    "https://www.bharian.com.my/berita/nasional/2025/03/1397234/polis-cari-wanita-bantu-siasatan-kes-dadah",
    "https://www.sinarharian.com.my/article/123456/berita/nasional/polis-cari-lelaki-bantu-siasatan",
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
                "waitFor": 3000
            },
            timeout=45
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("success") and "data" in data:
                return data["data"]
            else:
                print(f"  API error: {data}")
                return None
        else:
            print(f"  HTTP {response.status_code}: {response.text[:150]}")
            return None
    except Exception as e:
        print(f"  Exception: {e}")
        return None

def extract_io_contacts_v2(content: str, url: str) -> List[dict]:
    """
    Improved extraction with better pattern matching for Malay police articles.
    """
    contacts = []
    
    # Clean content
    content_clean = content.replace('\n', ' ').replace('  ', ' ')
    
    # Better officer patterns - capture full names with various formats
    officer_patterns = [
        # Insp. Name format
        r'(Insp\.|Inspektor|Insp)\s+([A-Z][a-z]+\.?\s*[A-Z]?[a-z]+\s*(?:[A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)?)',
        # Sarjan Name format
        r'(Sarjan|Sjn\.|Sjn)\s+([A-Z][a-z]+\.?\s*[A-Z]?[a-z]+\s*(?:[A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)?)',
        # DSP format
        r'(DSP|Deputi Superintendan|Deputi Superintenden)\s+([A-Z][a-z]+\.?\s*[A-Z]?[a-z]+\s*(?:[A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)?)',
        # PPP (Pegawai Penyiasat Polis)
        r'(PPP)\s+([A-Z]?[a-z]+\.?\s*[A-Z]?[a-z]+)?',
    ]
    
    # Phone patterns - more flexible
    mobile_pattern = r'(01[0-9]-\d{6,7}|\d{3}-\d{6,7})'
    office_pattern = r'(0[3-9]-\d{6,7}|\d{2,3}-\d{6,7})'
    ext_pattern = r'(?:sambungan|ext\.?|ext|sbm)\.?\s*(\d{3,4})'
    
    # Find all phone numbers first
    mobiles = re.findall(mobile_pattern, content)
    offices = re.findall(office_pattern, content)
    extensions = re.findall(ext_pattern, content, re.IGNORECASE)
    
    # Filter out duplicates while preserving order
    mobiles = list(dict.fromkeys(mobiles))
    offices = list(dict.fromkeys(offices))
    
    # Find officers
    officers = []
    for pattern in officer_patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            rank = match.group(1)
            name = match.group(2).strip()
            # Clean up name - remove common artifacts
            name = re.sub(r'\s+di\s+$', '', name)  # Remove "di" at end
            name = re.sub(r'\s+di\s+talian', '', name)  # Remove "di talian"
            name = re.sub(r'\s+untuk\s+', '', name)  # Remove "untuk"
            if len(name) > 3 and name.lower() not in ['talian', 'telefon', 'hubungi', 'orang']:
                officers.append({"rank": rank, "name": name, "position": match.start()})
    
    # Remove duplicate officers (same name)
    seen_names = set()
    unique_officers = []
    for officer in officers:
        if officer["name"] not in seen_names:
            seen_names.add(officer["name"])
            unique_officers.append(officer)
    
    # Try to associate officers with nearby phone numbers
    if unique_officers:
        for i, officer in enumerate(unique_officers):
            # Look for phone numbers within 200 chars of officer mention
            start_pos = max(0, officer["position"] - 100)
            end_pos = min(len(content), officer["position"] + 200)
            nearby_text = content[start_pos:end_pos]
            
            nearby_mobiles = re.findall(mobile_pattern, nearby_text)
            nearby_offices = re.findall(office_pattern, nearby_text)
            nearby_exts = re.findall(ext_pattern, nearby_text, re.IGNORECASE)
            
            contact = {
                "officer_name": officer["name"],
                "officer_rank": officer["rank"],
                "contact_mobile": nearby_mobiles[0] if nearby_mobiles else (mobiles[i] if i < len(mobiles) else None),
                "contact_office": nearby_offices[0] if nearby_offices else (offices[i] if i < len(offices) else None),
                "extension": nearby_exts[0][0] if nearby_exts else (extensions[i] if i < len(extensions) else None),
                "source_url": url,
                "extracted_at": datetime.now().isoformat(),
                "confidence": "high" if nearby_mobiles or nearby_offices else "medium"
            }
            contacts.append(contact)
    
    # If no officers found but phones exist, create generic contact
    elif mobiles or offices:
        contact = {
            "officer_name": "Unknown",
            "officer_rank": "Unknown",
            "contact_mobile": mobiles[0] if mobiles else None,
            "contact_office": offices[0] if offices else None,
            "extension": extensions[0] if extensions else None,
            "source_url": url,
            "extracted_at": datetime.now().isoformat(),
            "confidence": "low"
        }
        contacts.append(contact)
    
    return contacts

def main():
    results = {
        "extraction_date": datetime.now().isoformat(),
        "total_articles": 0,
        "total_contacts": 0,
        "contacts_by_confidence": {"high": 0, "medium": 0, "low": 0},
        "by_outlet": {},
        "contacts": [],
        "failed_urls": []
    }
    
    print("=" * 70)
    print("PDRM IO Contact Extraction v2 - Firecrawl")
    print("=" * 70)
    
    # Scrape known articles
    print(f"\n📰 Scraping {len(KNOWN_ARTICLES)} articles...")
    for i, url in enumerate(KNOWN_ARTICLES, 1):
        print(f"\n[{i}/{len(KNOWN_ARTICLES)}] {url}")
        data = scrape_url(url)
        
        if data and "markdown" in data:
            contacts = extract_io_contacts_v2(data["markdown"], url)
            if contacts:
                print(f"  ✓ Found {len(contacts)} contact(s):")
                for c in contacts:
                    print(f"    • {c['officer_rank']} {c['officer_name']}: {c['contact_mobile'] or c['contact_office'] or 'N/A'} [{c['confidence']}]")
                results["contacts"].extend(contacts)
                results["total_articles"] += 1
                results["total_contacts"] += len(contacts)
                for c in contacts:
                    results["contacts_by_confidence"][c["confidence"]] += 1
            else:
                print(f"  ⚠ No contacts found in content")
        else:
            print(f"  ✗ Failed to scrape")
            results["failed_urls"].append(url)
    
    # Aggregate by outlet
    for contact in results["contacts"]:
        domain = contact["source_url"].split('/')[2]
        if domain not in results["by_outlet"]:
            results["by_outlet"][domain] = {"count": 0, "contacts": []}
        results["by_outlet"][domain]["count"] += 1
        results["by_outlet"][domain]["contacts"].append(contact)
    
    # Save results
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print("\n" + "=" * 70)
    print("📊 EXTRACTION SUMMARY")
    print("=" * 70)
    print(f"Articles Successfully Processed: {results['total_articles']}/{len(KNOWN_ARTICLES)}")
    print(f"Total IO Contacts Extracted:   {results['total_contacts']}")
    print(f"\nConfidence Breakdown:")
    print(f"  • High:   {results['contacts_by_confidence']['high']}")
    print(f"  • Medium: {results['contacts_by_confidence']['medium']}")
    print(f"  • Low:    {results['contacts_by_confidence']['low']}")
    print(f"\nBy Outlet:")
    for outlet, data in sorted(results["by_outlet"].items(), key=lambda x: x[1]["count"], reverse=True):
        print(f"  • {outlet}: {data['count']} contacts")
    if results["failed_urls"]:
        print(f"\n⚠ Failed URLs ({len(results['failed_urls'])}):")
        for url in results["failed_urls"][:5]:
            print(f"    - {url}")
    print(f"\n💾 Results saved to: {OUTPUT_FILE}")
    print("=" * 70)

if __name__ == "__main__":
    main()

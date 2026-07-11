#!/usr/bin/env python3
"""
PDRM IO Contact Extraction - Quick Test (Tier 1 Only)
Test run with 15 core queries to validate comprehensive crawler.

Classification: TLP:AMBER
"""

import json
import re
import time
from datetime import datetime
from typing import List, Dict, Set
from playwright.sync_api import sync_playwright

OUTPUT_JSON = "/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-test-results.json"
OUTPUT_CSV = "/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-test.csv"
SEEN_URLS = "/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-test-seen-urls.txt"

# Tier 1 Only - 15 core queries
SEARCH_QUERIES = [
    "polis cari bantu siasatan site:malaysiagazette.com",
    "polis cari bantu siasatan site:hmetro.com.my",
    "polis cari bantu siasatan site:bharian.com.my",
    "polis mengesan bantu siasatan site:malaysiagazette.com",
    "polis cari diperlukan site:hmetro.com.my",
    "polis cari suspek site:bharian.com.my",
    "polis mengesan suspek site:sinarharian.com.my",
    "polis cari orang ramai site:freemalaysiatoday.com",
    "polis cari lelaki site:bernama.com",
    "polis cari wanita site:malaysiagazette.com",
    "polis cari individu site:hmetro.com.my",
    "polis cari segera site:bharian.com.my",
    "polis mengesan segera site:sinarharian.com.my",
    "polis cari maklumat site:freemalaysiatoday.com",
    "polis cari kerjasama site:bernama.com",
]

# Pre-seeded known article URLs (fallback if search fails)
KNOWN_URLS = [
    "https://malaysiagazette.com/2026/06/04/polis-cari-marvin-loo-jia-an-bantu-siasatan/",
    "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2023/09/01/polis-cari-suspek-bantu-siasatan-kes-rogol-berkumpulan/",
    "https://www.hmetro.com.my/mutakhir/2026/02/1324976/polis-cari-mohamad-syazwan-bantu-siasatan-kes-dadah",
    "https://www.bharian.com.my/berita/nasional/2025/03/1397234/polis-cari-wanita-bantu-siasatan-kes-dadah",
    "https://www.buletintv3.my/nasional/polis-cari-celine-bantu-siasatan-babit-kes-dadah/",
    "https://www.melakahariini.my/polis-cari-lelaki-36-tahun-bantu-siasatan-kes-jenayah/",
]

def extract_urls_from_search(page, query):
    """Extract URLs from Google search results with better selectors."""
    urls = []
    page.wait_for_timeout(5000)  # Wait longer for results
    
    # Try multiple selector strategies
    strategies = [
        # Strategy 1: Generic link extraction
        lambda: [el.get_attribute('href') for el in page.query_selector_all('a[href*="http"]')],
        # Strategy 2: Search result specific
        lambda: [el.get_attribute('href') for el in page.query_selector_all('div.g a, a.dCSwpd, a.C8nzq')],
        # Strategy 3: Text content search
        lambda: [el.get_attribute('href') for el in page.query_selector_all('a') if any(site in (el.get_attribute('href') or '') for site in ['malaysiagazette', 'hmetro', 'bharian', 'sinarharian', 'freemalaysiatoday', 'bernama'])],
    ]
    
    for strategy in strategies:
        try:
            links = strategy()
            for href in links:
                if href and not href.startswith('http') and href.startswith('/'):
                    continue  # Skip relative URLs
                if href and any(site in href for site in ['malaysiagazette.com', 'hmetro.com.my', 'bharian.com.my', 'sinarharian.com.my', 'freemalaysiatoday.com', 'bernama.com', 'buletintv3.my', 'melakahariini.my']):
                    # Clean URL
                    clean_url = href.split('&')[0]
                    if '/search?' not in clean_url and '/url?' not in clean_url:
                        if clean_url not in urls:
                            urls.append(clean_url)
        except Exception as e:
            continue
    
    return urls[:20]

def extract_contacts(html, url):
    """Extract IO contacts from HTML."""
    contacts = []
    text = re.sub(r'\s+', ' ', html.replace('\n', ' '))
    
    # Phone patterns
    mobile_patterns = [r'(01[0-9]\s*-\s*\d{6,7})', r'(01[0-9]\s*\d{7,8})']
    office_patterns = [r'(0[3-9]\s*-\s*\d{6,7})', r'(0[3-9]\s*\d{6,7})']
    
    mobiles = list(dict.fromkeys([m.replace(' ', '') for pat in mobile_patterns for m in re.findall(pat, text)]))
    offices = list(dict.fromkeys([o.replace(' ', '') for pat in office_patterns for o in re.findall(pat, text)]))
    
    # Officer patterns
    officer_patterns = [
        r'(Insp\.?\s+|Inspektor\s+)([A-Z][a-z]+(?:\s+[A-Z])?\s*[a-z]+)',
        r'(Sarjan|Sjn\.?\s+)([A-Z][a-z]+(?:\s+[A-Z])?\s*[a-z]+)',
        r'(DSP|Deputi\s+Superintendan)(?:\s+)?([A-Z][a-z]+)?',
    ]
    
    for pattern in officer_patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            rank = match.group(1).strip().replace('.', '')
            name = match.group(2).strip().title() if match.group(2) else "Unknown"
            # Clean artifacts
            name = re.sub(r'\s+di\s+.*$', '', name)
            name = re.sub(r'\s+untuk\s+.*$', '', name)
            name = re.sub(r'\s+berkata.*$', '', name)
            if len(name) > 2 and name.lower() not in ['talian', 'telefon', 'hubungi', 'ipd', 'polis']:
                contacts.append({
                    "officer_name": name,
                    "officer_rank": rank,
                    "contact_mobile": mobiles[0] if mobiles else None,
                    "contact_office": offices[0] if offices else None,
                    "source_url": url,
                    "extracted_at": datetime.now().isoformat(),
                    "confidence": "high" if (mobiles or offices) else "medium",
                    "method": "test_tier1"
                })
    
    # Fallback for articles with phones but no named officers
    if not contacts and (mobiles or offices):
        contacts.append({
            "officer_name": "Unknown",
            "officer_rank": "Unknown",
            "contact_mobile": mobiles[0] if mobiles else None,
            "contact_office": offices[0] if offices else None,
            "source_url": url,
            "extracted_at": datetime.now().isoformat(),
            "confidence": "low",
            "method": "test_tier1"
        })
    
    return contacts

def main():
    results = {
        "date": datetime.now().isoformat(),
        "queries": len(SEARCH_QUERIES),
        "urls_visited": 0,
        "contacts": [],
        "by_outlet": {},
        "errors": []
    }
    seen = set()
    all_urls = set()
    
    print("=" * 70)
    print("PDRM IO Comprehensive Crawl - TIER 1 TEST RUN")
    print("15 Queries | Core 'polis cari' patterns")
    print("=" * 70)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = context.new_page()
        
        print("\n📋 PHASE 1: Collecting URLs from Search Results")
        print("-" * 70)
        
        for i, query in enumerate(SEARCH_QUERIES, 1):
            print(f"  [{i}/{len(SEARCH_QUERIES)}] {query[:55]}...")
            try:
                search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}&num=20"
                page.goto(search_url, timeout=30000, wait_until="domcontentloaded")
                page.wait_for_timeout(5000)
                
                urls = extract_urls_from_search(page, query)
                for url in urls:
                    if url not in seen and url not in all_urls:
                        all_urls.add(url)
                        print(f"    → Found: {url[:70]}...")
                
            except Exception as e:
                print(f"    ✗ Error: {str(e)[:80]}")
                results["errors"].append({"query": query, "error": str(e)[:100]})
            
            time.sleep(3)  # Rate limiting
        
        # Add known URLs as fallback
        print(f"\n📊 URLs from search: {len(all_urls)}")
        print(f"➕ Adding {len(KNOWN_URLS)} known URLs as fallback...")
        for url in KNOWN_URLS:
            if url not in all_urls:
                all_urls.add(url)
        
        print(f"\n📊 Total URLs to process: {len(all_urls)}")
        
        print("\n📋 PHASE 2: Extracting Contacts from Articles")
        print("-" * 70)
        
        for i, url in enumerate(sorted(all_urls), 1):
            print(f"\n[{i}/{len(all_urls)}] {url[:65]}...")
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
                else:
                    print(f"  ⚠ No contacts found")
                
                results["urls_visited"] += 1
                seen.add(url)
                
                # Aggregate by outlet
                domain = url.split('/')[2]
                if domain not in results["by_outlet"]:
                    results["by_outlet"][domain] = {"count": 0, "urls": []}
                results["by_outlet"][domain]["count"] += len(contacts)
                results["by_outlet"][domain]["urls"].append(url)
                
            except Exception as e:
                print(f"  ✗ Error: {str(e)[:80]}")
                results["errors"].append({"url": url, "error": str(e)[:100]})
            
            # Rate limiting
            if i % 5 == 0:
                print(f"  ⏳ Rate limit pause (5s)...")
                time.sleep(5)
        
        browser.close()
    
    # Save results
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    with open(OUTPUT_CSV, 'w', encoding='utf-8') as f:
        f.write("officer_name,officer_rank,contact_mobile,contact_office,source_url,confidence,method,extracted_at\n")
        for c in results["contacts"]:
            f.write(f'"{c["officer_name"]}","{c["officer_rank"]}",{c["contact_mobile"] or ""},{c["contact_office"] or ""},{c["source_url"]},{c["confidence"]},{c["method"]},{c["extracted_at"]}\n')
    
    with open(SEEN_URLS, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(seen)))
    
    # Print summary
    print("\n" + "=" * 70)
    print("📊 TEST RUN SUMMARY")
    print("=" * 70)
    print(f"Queries Executed: {results['queries']}")
    print(f"URLs Visited: {results['urls_visited']}")
    print(f"Successful Extractions: {sum(1 for c in results['contacts'])}")
    print(f"Total IO Contacts: {len(results['contacts'])}")
    print(f"Unique Outlets: {len(results['by_outlet'])}")
    
    if results["by_outlet"]:
        print(f"\nBy Outlet:")
        for outlet, data in sorted(results["by_outlet"].items(), key=lambda x: x[1]["count"], reverse=True):
            print(f"  • {outlet}: {data['count']} contacts from {len(data['urls'])} articles")
    
    conf = results["contacts"]
    if conf:
        print(f"\nConfidence Distribution:")
        print(f"  HIGH: {sum(1 for c in conf if c['confidence']=='high')}")
        print(f"  MEDIUM: {sum(1 for c in conf if c['confidence']=='medium')}")
        print(f"  LOW: {sum(1 for c in conf if c['confidence']=='low')}")
    
    print(f"\n💾 Results saved to:")
    print(f"  - {OUTPUT_JSON}")
    print(f"  - {OUTPUT_CSV}")
    print(f"  - {SEEN_URLS}")
    print("=" * 70)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
PDRM IO Contact Extraction - Comprehensive Search Crawler v3
Uses 100+ search queries across 15+ Malaysian news outlets.

Classification: TLP:AMBER
Workspace: /home/p62operator/.openclaw/workspace-hoi/

Usage:
    /tmp/playwright-env/bin/python /home/p62operator/.openclaw/workspace-hoi/scripts/pdrm-io-comprehensive-crawler.py
"""

import json
import re
import time
from datetime import datetime
from typing import List, Dict, Set
from playwright.sync_api import sync_playwright

# Configuration
OUTPUT_JSON = "/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-comprehensive-results.json"
OUTPUT_CSV = "/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-comprehensive.csv"
OUTPUT_MD = "/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-comprehensive-summary.md"
SEEN_URLS_FILE = "/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-seen-urls.txt"

# Search Engine Base URLs
SEARCH_ENGINES = {
    "Google": "https://www.google.com/search?q=",
    "Bing": "https://www.bing.com/search?q=",
    "DuckDuckGo": "https://duckduckgo.com/?q=",
}

# Target Outlets (for site-specific searches)
TARGET_OUTLETS = [
    "malaysiagazette.com",
    "hmetro.com.my",
    "bharian.com.my",
    "sinarharian.com.my",
    "freemalaysiatoday.com",
    "bernama.com",
    "thestar.com.my",
    "nst.com.my",
    "malaysiakini.com",
    "vibes88.com",
    "malaymail.com",
    "theedgemarkets.com",
    "codeblue.galencentre.org",
    "buletintv3.my",
    "melakahariini.my",
]

# 100+ Comprehensive Search Queries (organized by tier)
SEARCH_QUERIES = {
    # Tier 1: Highest Yield - Core Police Appeal (15 queries)
    "tier1_core": [
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
    ],
    
    # Tier 2: Officer Rank Specific (12 queries)
    "tier2_ranks": [
        "Inspektor bantu siasatan telefon site:malaysiagazette.com",
        "Insp bantu siasatan hubungi site:hmetro.com.my",
        "DSP bantu siasatan talian site:bharian.com.my",
        "Deputi Superintendan siasatan site:sinarharian.com.my",
        "Sarjan bantu siasatan telefon site:freemalaysiatoday.com",
        "Sjn bantu siasatan hubungi site:bernama.com",
        "PPP bantu siasatan talian site:malaysiagazette.com",
        "pegawai penyiasat telefon site:hmetro.com.my",
        "Pegawai Penyiasat hubungi site:bharian.com.my",
        "Ketua Polis Daerah cari site:sinarharian.com.my",
        "KPD bantu siasatan site:freemalaysiatoday.com",
        "Ketua Jabatan siasatan telefon site:bernama.com",
    ],
    
    # Tier 3: Crime Type Specific (15 queries)
    "tier3_crimes": [
        "polis cari dadah telefon site:malaysiagazette.com",
        "polis cari narkotik hubungi site:hmetro.com.my",
        "polis cari rogol telefon site:bharian.com.my",
        "polis cari liwat siasatan site:sinarharian.com.my",
        "polis cari cabul hubungi site:freemalaysiatoday.com",
        "polis cari curi telefon site:bernama.com",
        "polis cari samun hubungi site:malaysiagazette.com",
        "polis cari rompakan telefon site:hmetro.com.my",
        "polis cari bunuh siasatan site:bharian.com.my",
        "polis cari mati siasatan site:sinarharian.com.my",
        "polis cari hilang telefon site:freemalaysiatoday.com",
        "polis cari orang hilang hubungi site:bernama.com",
        "polis cari penipuan telefon site:malaysiagazette.com",
        "polis cari scam hubungi site:hmetro.com.my",
        "polis cari jenayah komersial talian site:bharian.com.my",
    ],
    
    # Tier 4: Contact Detail Patterns (12 queries)
    "tier4_contact": [
        "bantu siasatan telefon 01 site:malaysiagazette.com",
        "bantu siasatan talian 01 site:hmetro.com.my",
        "bantu siasatan hubungi 01 site:bharian.com.my",
        "siasatan talian telefon site:sinarharian.com.my",
        "siasatan nombor telefon site:freemalaysiatoday.com",
        "siasatan no telefon site:bernama.com",
        "maklumat telefon polis site:malaysiagazette.com",
        "maklumat hubungi polis site:hmetro.com.my",
        "sila hubungi polis telefon site:bharian.com.my",
        "boleh menghubungi polis talian site:sinarharian.com.my",
        "talian panas polis siasatan site:freemalaysiatoday.com",
        "hotline polis siasatan site:bernama.com",
    ],
    
    # Tier 5: Call-to-Action Phrases (10 queries)
    "tier5_appeal": [
        "orang ramai yang mempunyai maklumat site:malaysiagazette.com",
        "orang ramai diminta hubungi site:hmetro.com.my",
        "orang ramai dialu-alukan hubungi site:bharian.com.my",
        "mana-mana pihak maklumat hubungi site:sinarharian.com.my",
        "siapa yang mempunyai maklumat site:freemalaysiatoday.com",
        "sesiapa yang mempunyai maklumat site:bernama.com",
        "orang ramai boleh menghubungi site:malaysiagazette.com",
        "orang ramai digalakkan hubungi site:hmetro.com.my",
        "kerjasama orang ramai dipohon site:bharian.com.my",
        "pertolongan orang ramai dipohon site:sinarharian.com.my",
    ],
    
    # Tier 6: Investigation Status (10 queries)
    "tier6_status": [
        "bantu siasatan kes site:malaysiagazette.com",
        "dalam siasatan polis site:hmetro.com.my",
        "siasatan lanjut polis site:bharian.com.my",
        "siasatan sedang dijalankan site:sinarharian.com.my",
        "polis sedang mengesan site:freemalaysiatoday.com",
        "polis sedang mencari site:bernama.com",
        "dikehendaki bantu siasatan site:malaysiagazette.com",
        "diperlukan bantu siasatan site:hmetro.com.my",
        "ditahan bantu siasatan site:bharian.com.my",
        "direman bantu siasatan site:sinarharian.com.my",
    ],
    
    # Tier 7: Regional/State Specific (10 queries)
    "tier7_regional": [
        "polis cari Johor telefon site:malaysiagazette.com",
        "polis cari Melaka telefon site:hmetro.com.my",
        "polis cari KL telefon site:bharian.com.my",
        "polis cari Selangor telefon site:sinarharian.com.my",
        "polis cari Perlis telefon site:freemalaysiatoday.com",
        "polis cari Kedah telefon site:bernama.com",
        "polis cari Penang telefon site:malaysiagazette.com",
        "polis cari Pulau Pinang telefon site:hmetro.com.my",
        "polis cari Sabah telefon site:bharian.com.my",
        "polis cari Sarawak telefon site:sinarharian.com.my",
    ],
    
    # Tier 8: English Language (8 queries)
    "tier8_english": [
        "police hunt Malaysia contact site:thestar.com.my",
        "police seek Malaysia information site:nst.com.my",
        "police appeal Malaysia call site:malaymail.com",
        "wanted police Malaysia telephone site:thestar.com.my",
        "investigating officer Malaysia contact site:nst.com.my",
        "police investigation Malaysia hotline site:freemalaysiatoday.com",
        "help police Malaysia enquiries site:thestar.com.my",
        "contact police Malaysia information site:nst.com.my",
    ],
    
    # Tier 9: Advanced Combined (10 queries)
    "tier9_advanced": [
        "polis cari bantu siasatan Inspektor 01 site:malaysiagazette.com",
        "polis mengesan bantu siasatan DSP telefon site:hmetro.com.my",
        "pegawai penyiasat talian 01 Malaysia site:bharian.com.my",
        "orang ramai hubungi polis 01 telefon site:sinarharian.com.my",
        "dadah Inspektor telefon bantu siasatan site:freemalaysiatoday.com",
        "rogol polis cari telefon hubungi site:bernama.com",
        "curi polis mengesan talian siasatan site:malaysiagazette.com",
        "jenayah polis cari pegawai penyiasat telefon site:hmetro.com.my",
        "IPD polis cari bantu siasatan telefon site:bharian.com.my",
        "balai polis cari suspek hubungi site:sinarharian.com.my",
    ],
}

def load_seen_urls() -> Set[str]:
    """Load previously seen URLs to avoid duplicates."""
    try:
        with open(SEEN_URLS_FILE, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

def save_seen_urls(urls: Set[str]):
    """Save seen URLs to file."""
    with open(SEEN_URLS_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(urls)))

def extract_article_urls_from_search(page, query: str) -> List[str]:
    """Extract article URLs from search results page."""
    urls = []
    
    # Wait for results to load
    page.wait_for_timeout(3000)
    
    # Try different search engine result selectors
    selectors = [
        'a[href*="malaysiagazette.com"]',
        'a[href*="hmetro.com.my"]',
        'a[href*="bharian.com.my"]',
        'a[href*="sinarharian.com.my"]',
        'a[href*="freemalaysiatoday.com"]',
        'a[href*="bernama.com"]',
        'a[href*="thestar.com.my"]',
        'a[href*="nst.com.my"]',
        'a[href*="malaysiakini.com"]',
        'a[href*="vibes88.com"]',
        'a[href*="buletintv3.my"]',
        'a[href*="melakahariini.my"]',
    ]
    
    for selector in selectors:
        try:
            elements = page.query_selector_all(selector)
            for el in elements:
                try:
                    href = el.get_attribute('href')
                    if href and '/article' in href or '/news' in href or '/berita' in href or '/mutakhir' in href or '/nasional' in href or '/jenayah' in href:
                        # Clean URL
                        href = href.split('&')[0].split('?')[0] if '?' in href else href
                        if href not in urls:
                            urls.append(href)
                except:
                    continue
        except:
            continue
    
    return urls[:20]  # Limit to top 20 results per query

def extract_contacts_from_html(html: str, url: str) -> List[Dict]:
    """Extract IO contacts from HTML content (v2 improved patterns)."""
    contacts = []
    text = re.sub(r'\s+', ' ', html.replace('\n', ' '))
    
    # Phone patterns
    mobile_patterns = [r'(01[0-9]\s*-\s*\d{6,7})', r'(01[0-9]\s*\d{7,8})']
    office_patterns = [r'(0[3-9]\s*-\s*\d{6,7})', r'(0[3-9]\s*\d{6,7})']
    ext_patterns = [r'(?:sambungan|ext\.?|sbm|talian\s+dalam)\s*(\d{3,4})', r'\(\s*(\d{3,4})\s*\)']
    
    # Officer patterns
    officer_patterns = [
        r'(Insp\.?\s+|Inspektor\s+)([A-Z][a-z]+(?:\s+[A-Z])?\s*[a-z]+(?:\s+[A-Z][a-z]+)*)',
        r'(Sarjan|Sjn\.?\s+)([A-Z][a-z]+(?:\s+[A-Z])?\s*[a-z]+(?:\s+[A-Z][a-z]+)*)',
        r'(DSP|Deputi\s+Superintendan)\s+([A-Z][a-z]+(?:\s+[A-Z])?\s*[a-z]+(?:\s+[A-Z][a-z]+)*)',
        r'(PPP)\s*(?:\(.*?\))?\s*([A-Z]?[a-z]+)?',
    ]
    
    # Extract phones
    mobiles = []
    for pat in mobile_patterns:
        mobiles.extend(re.findall(pat, text))
    mobiles = list(dict.fromkeys([m.replace(' ', '') for m in mobiles]))
    
    offices = []
    for pat in office_patterns:
        offices.extend(re.findall(pat, text))
    offices = list(dict.fromkeys([o.replace(' ', '') for o in offices]))
    
    extensions = []
    for pat in ext_patterns:
        extensions.extend(re.findall(pat, text, re.IGNORECASE))
    
    # Extract officers
    officers = []
    for pattern in officer_patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            rank = match.group(1).strip()
            name = match.group(2).strip() if match.group(2) else "Unknown"
            # Clean artifacts
            name = re.sub(r'\s+di\s+.*$', '', name)
            name = re.sub(r'\s+untuk\s+.*$', '', name)
            name = re.sub(r'\s+berkata.*$', '', name)
            name = re.sub(r'\s+membantu.*$', '', name)
            if len(name) > 2 and name.lower() not in ['talian', 'telefon', 'hubungi', 'ipd', 'polis']:
                officers.append({"rank": rank, "name": name.title(), "position": match.start()})
    
    # Deduplicate
    seen = set()
    unique_officers = []
    for o in officers:
        if o["name"] not in seen:
            seen.add(o["name"])
            unique_officers.append(o)
    
    # Associate with nearby phones
    if unique_officers:
        for i, officer in enumerate(unique_officers):
            start = max(0, officer["position"] - 250)
            end = min(len(text), officer["position"] + 350)
            nearby = text[start:end]
            
            nearby_mobiles = []
            for pat in mobile_patterns:
                nearby_mobiles.extend(re.findall(pat, nearby))
            nearby_mobiles = [m.replace(' ', '') for m in nearby_mobiles]
            
            nearby_offices = []
            for pat in office_patterns:
                nearby_offices.extend(re.findall(pat, nearby))
            nearby_offices = [o.replace(' ', '') for o in nearby_offices]
            
            contact = {
                "officer_name": officer["name"],
                "officer_rank": officer["rank"].replace('.', '').strip(),
                "contact_mobile": nearby_mobiles[0] if nearby_mobiles else (mobiles[i] if i < len(mobiles) else None),
                "contact_office": nearby_offices[0] if nearby_offices else (offices[i] if i < len(offices) else None),
                "extension": extensions[i] if i < len(extensions) else None,
                "source_url": url,
                "extracted_at": datetime.now().isoformat(),
                "confidence": "high" if (nearby_mobiles or nearby_offices) else "medium",
                "method": "playwright_comprehensive_v3",
                "search_query": "comprehensive_crawl"
            }
            contacts.append(contact)
    
    # Fallback
    elif mobiles or offices:
        contacts.append({
            "officer_name": "Unknown",
            "officer_rank": "Unknown",
            "contact_mobile": mobiles[0] if mobiles else None,
            "contact_office": offices[0] if offices else None,
            "extension": extensions[0] if extensions else None,
            "source_url": url,
            "extracted_at": datetime.now().isoformat(),
            "confidence": "low",
            "method": "playwright_comprehensive_v3",
            "search_query": "comprehensive_crawl"
        })
    
    return contacts

def run_comprehensive_crawl():
    """Main comprehensive crawl function."""
    results = {
        "extraction_date": datetime.now().isoformat(),
        "total_queries": 0,
        "total_urls_visited": 0,
        "successful_extractions": 0,
        "failed_extractions": 0,
        "contacts": [],
        "by_outlet": {},
        "by_tier": {},
        "errors": [],
        "seen_urls": []
    }
    
    seen_urls = load_seen_urls()
    all_article_urls = set()
    
    print("=" * 80)
    print("PDRM IO Contact Extraction - Comprehensive Search Crawler v3")
    print("100+ Queries | 15+ Outlets | Full Coverage")
    print("=" * 80)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = context.new_page()
        
        # Phase 1: Search each query and collect article URLs
        print("\n📋 PHASE 1: Collecting Article URLs from Search Results")
        print("-" * 80)
        
        for tier_name, queries in SEARCH_QUERIES.items():
            print(f"\n🔍 {tier_name.upper()} ({len(queries)} queries)")
            results["total_queries"] += len(queries)
            tier_contacts = []
            
            for i, query in enumerate(queries, 1):
                print(f"  [{i}/{len(queries)}] {query[:60]}...")
                
                try:
                    # Navigate to Google search
                    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
                    page.goto(search_url, timeout=30000, wait_until="domcontentloaded")
                    page.wait_for_timeout(3000)
                    
                    # Extract article URLs from search results
                    article_urls = extract_article_urls_from_search(page, query)
                    
                    for url in article_urls:
                        if url not in seen_urls and url not in all_article_urls:
                            all_article_urls.add(url)
                    
                except Exception as e:
                    print(f"    ✗ Search error: {str(e)[:80]}")
                    results["errors"].append({"query": query, "error": str(e)[:200]})
            
            # Small delay between tiers
            time.sleep(2)
        
        print(f"\n📊 Total Unique Article URLs Collected: {len(all_article_urls)}")
        
        # Phase 2: Visit each article and extract contacts
        print("\n📋 PHASE 2: Extracting IO Contacts from Articles")
        print("-" * 80)
        
        for i, url in enumerate(sorted(all_article_urls), 1):
            print(f"\n[{i}/{len(all_article_urls)}] {url[:70]}...")
            
            try:
                page.goto(url, timeout=30000, wait_until="domcontentloaded")
                page.wait_for_timeout(3000)
                
                html = page.content()
                contacts = extract_contacts_from_html(html, url)
                
                if contacts:
                    print(f"  ✓ Found {len(contacts)} contact(s)")
                    for c in contacts:
                        phone = c['contact_mobile'] or c['contact_office'] or 'N/A'
                        print(f"    • {c['officer_rank']} {c['officer_name']}: {phone} [{c['confidence']}]")
                    results["contacts"].extend(contacts)
                    results["successful_extractions"] += 1
                else:
                    print(f"  ⚠ No contacts found")
                    results["successful_extractions"] += 1  # Page loaded successfully
                
                results["total_urls_visited"] += 1
                seen_urls.add(url)
                
                # Aggregate by outlet
                domain = url.split('/')[2]
                if domain not in results["by_outlet"]:
                    results["by_outlet"][domain] = {"count": 0, "contacts": []}
                results["by_outlet"][domain]["count"] += len(contacts)
                results["by_outlet"][domain]["contacts"].extend(contacts)
                
            except Exception as e:
                print(f"  ✗ Error: {str(e)[:80]}")
                results["failed_extractions"] += 1
                results["errors"].append({"url": url, "error": str(e)[:200]})
            
            # Rate limiting
            if i % 10 == 0:
                print(f"  ⏳ Rate limit pause...")
                time.sleep(5)
        
        browser.close()
    
    # Save seen URLs
    save_seen_urls(seen_urls)
    results["seen_urls"] = sorted(list(seen_urls))
    
    # Save results
    save_results(results)
    
    # Print summary
    print("\n" + "=" * 80)
    print("📊 COMPREHENSIVE CRAWL SUMMARY")
    print("=" * 80)
    print(f"Total Queries Executed: {results['total_queries']}")
    print(f"Total URLs Visited: {results['total_urls_visited']}")
    print(f"Successful Extractions: {results['successful_extractions']}")
    print(f"Failed Extractions: {results['failed_extractions']}")
    print(f"Total IO Contacts Extracted: {len(results['contacts'])}")
    print(f"Unique Outlets: {len(results['by_outlet'])}")
    
    conf = results["contacts"]
    print(f"\nConfidence Distribution:")
    print(f"  HIGH: {sum(1 for c in conf if c['confidence']=='high')}")
    print(f"  MEDIUM: {sum(1 for c in conf if c['confidence']=='medium')}")
    print(f"  LOW: {sum(1 for c in conf if c['confidence']=='low')}")
    
    print(f"\n📁 Output Files:")
    print(f"  - {OUTPUT_JSON}")
    print(f"  - {OUTPUT_CSV}")
    print(f"  - {OUTPUT_MD}")
    print(f"  - {SEEN_URLS_FILE}")
    print("=" * 80)

def save_results(results: Dict):
    """Save results to JSON, CSV, and Markdown."""
    # JSON
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # CSV
    with open(OUTPUT_CSV, 'w', encoding='utf-8') as f:
        f.write("officer_name,officer_rank,contact_mobile,contact_office,extension,source_url,confidence,method,search_query\n")
        for c in results["contacts"]:
            f.write(f'"{c["officer_name"]}","{c["officer_rank"]}",{c["contact_mobile"] or ""},{c["contact_office"] or ""},{c["extension"] or ""},{c["source_url"]},{c["confidence"]},{c["method"]},{c["search_query"]}\n')
    
    # Markdown Summary
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write("# 📊 PDRM IO Contact Extraction - Comprehensive Crawl Results\n\n")
        f.write(f"**Date:** {results['extraction_date']}\n")
        f.write(f"**Classification:** TLP:AMBER\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"- **Total Queries:** {results['total_queries']}\n")
        f.write(f"- **URLs Visited:** {results['total_urls_visited']}\n")
        f.write(f"- **Successful:** {results['successful_extractions']}\n")
        f.write(f"- **Failed:** {results['failed_extractions']}\n")
        f.write(f"- **Total Contacts:** {len(results['contacts'])}\n")
        f.write(f"- **Unique Outlets:** {len(results['by_outlet'])}\n\n")
        
        f.write(f"## By Outlet\n\n")
        for outlet, data in sorted(results["by_outlet"].items(), key=lambda x: x[1]["count"], reverse=True):
            f.write(f"- **{outlet}**: {data['count']} contacts\n")
        
        f.write(f"\n## All Contacts Extracted ({len(results['contacts'])} total)\n\n")
        f.write("| # | Officer | Rank | Mobile | Office | Ext | Confidence | Outlet |\n")
        f.write("|---|---------|------|--------|--------|-----|------------|--------|\n")
        for i, c in enumerate(results["contacts"], 1):
            mobile = c['contact_mobile'] or '-'
            office = c['contact_office'] or '-'
            ext = c['extension'] or '-'
            outlet = c['source_url'].split('/')[2]
            f.write(f"| {i} | {c['officer_name']} | {c['officer_rank']} | {mobile} | {office} | {ext} | {c['confidence']} | {outlet} |\n")
        
        if results["errors"]:
            f.write(f"\n## Errors ({len(results['errors'])})\n\n")
            for err in results["errors"][:20]:  # Show first 20 errors
                f.write(f"- {err.get('url') or err.get('query')}: {err['error']}\n")
            if len(results["errors"]) > 20:
                f.write(f"\n*...and {len(results['errors']) - 20} more errors*")
    
    print(f"\n💾 Results saved successfully")

if __name__ == "__main__":
    run_comprehensive_crawl()

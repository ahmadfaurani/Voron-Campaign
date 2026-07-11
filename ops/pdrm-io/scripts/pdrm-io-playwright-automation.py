#!/usr/bin/env python3
"""
PDRM IO Contact Extraction - Playwright Browser Automation
Uses Playwright for headless browser scraping with JavaScript rendering.

Classification: TLP:AMBER
Workspace: /home/p62operator/.openclaw/workspace-hoi/

Requirements:
- playwright (pip install playwright)
- playwright install (browsers)

Usage:
    python3 /home/p62operator/.openclaw/workspace-hoi/scripts/pdrm-io-playwright-automation.py
"""

import json
import re
from datetime import datetime
from typing import List, Dict, Optional
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

# Configuration
OUTPUT_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/"
OUTPUT_JSON = f"{OUTPUT_DIR}pdrm-io-playwright-results.json"
OUTPUT_CSV = f"{OUTPUT_DIR}pdrm-io-playwright.csv"
OUTPUT_MD = f"{OUTPUT_DIR}pdrm-io-playwright-summary.md"

# Target articles (known URLs that timed out with Firecrawl)
TARGET_ARTICLES = [
    "https://malaysiagazette.com/2026/06/04/polis-cari-marvin-loo-jia-an-bantu-siasatan/",
    "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2023/09/01/polis-cari-suspek-bantu-siasatan-kes-rogol-berkumpulan/",
    "https://www.hmetro.com.my/mutakhir/2026/02/1324976/polis-cari-mohamad-syazwan-bantu-siasatan-kes-dadah",
    "https://www.bharian.com.my/berita/nasional/2025/03/1397234/polis-cari-wanita-bantu-siasatan-kes-dadah",
    "https://www.sinarharian.com.my/article/123456/berita/nasional/polis-cari-lelaki-bantu-siasatan",
]

# Search URLs for discovery
SEARCH_URLS = [
    {"name": "MalaysiaGazette", "url": "https://malaysiagazette.com/?s=polis+cari+bantu+siasatan"},
    {"name": "Harian Metro", "url": "https://www.hmetro.com.my/search/polis%20cari%20bantu%20siasatan"},
    {"name": "Berita Harian", "url": "https://www.bharian.com.my/search?keys=polis+cari+bantu+siasatan"},
    {"name": "Free Malaysia Today", "url": "https://www.freemalaysiatoday.com/search?q=polis+cari+bantu+siasatan"},
]

def clean_name(name: str) -> str:
    """Clean extracted officer name from artifacts."""
    name = re.sub(r'\s+di\s+$', '', name)
    name = re.sub(r'\s+di\s+talian', '', name)
    name = re.sub(r'\s+untuk\s+', '', name)
    name = re.sub(r'\s+berkata.*$', '', name)
    name = re.sub(r'\s+untuk\s+talian.*$', '', name)
    return name.strip()

def extract_contacts_from_html(html: str, url: str) -> List[Dict]:
    """Extract IO contacts from HTML content."""
    contacts = []
    text = html.replace('\n', ' ').replace('\r', ' ')
    
    # Phone patterns
    mobile_pattern = r'(01[0-9]-\d{6,7}|\d{3}-\d{6,7})'
    office_pattern = r'(0[3-9]-\d{6,7})'
    ext_pattern = r'(?:sambungan|ext\.?|ext|sbm)\.?\s*(\d{3,4})'
    
    # Officer patterns
    officer_patterns = [
        (r'(Insp\.?\s+|Inspektor\s+|Insp\s+)([A-Z][a-z]+\.?\s*[A-Z]?[a-z]+(?:\s+[A-Z][a-z]+)*)', 'Insp.'),
        (r'(Sarjan|Sjn\.?\s+|Sjn\s+)([A-Z][a-z]+\.?\s*[A-Z]?[a-z]+(?:\s+[A-Z][a-z]+)*)', 'Sarjan'),
        (r'(DSP|Deputi\s+Superintendan|Deputi\s+Superintenden)\s+([A-Z][a-z]+\.?\s*[A-Z]?[a-z]+(?:\s+[A-Z][a-z]+)*)', 'DSP'),
        (r'(PPP)\s+([A-Z]?[a-z]+\.?\s*[A-Z]?[a-z]+)?', 'PPP'),
    ]
    
    # Extract all phones
    mobiles = list(dict.fromkeys(re.findall(mobile_pattern, text)))
    offices = list(dict.fromkeys(re.findall(office_pattern, text)))
    extensions = re.findall(ext_pattern, text, re.IGNORECASE)
    
    # Extract officers
    officers = []
    for pattern, default_rank in officer_patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            rank = match.group(1).strip()
            name = clean_name(match.group(2)) if match.group(2) else "Unknown"
            if len(name) > 2 and name.lower() not in ['talian', 'telefon', 'hubungi', 'orang', 'ramai']:
                officers.append({"rank": rank, "name": name, "position": match.start()})
    
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
            start = max(0, officer["position"] - 200)
            end = min(len(text), officer["position"] + 300)
            nearby = text[start:end]
            
            nearby_mobiles = re.findall(mobile_pattern, nearby)
            nearby_offices = re.findall(office_pattern, nearby)
            nearby_exts = re.findall(ext_pattern, nearby, re.IGNORECASE)
            
            contact = {
                "officer_name": officer["name"],
                "officer_rank": officer["rank"],
                "contact_mobile": nearby_mobiles[0] if nearby_mobiles else (mobiles[i] if i < len(mobiles) else None),
                "contact_office": nearby_offices[0] if nearby_offices else (offices[i] if i < len(offices) else None),
                "extension": nearby_exts[0][0] if nearby_exts else (extensions[i] if i < len(extensions) else None),
                "source_url": url,
                "extracted_at": datetime.now().isoformat(),
                "confidence": "high" if (nearby_mobiles or nearby_offices) else "medium",
                "method": "playwright_browser"
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
            "method": "playwright_browser"
        })
    
    return contacts

def scrape_with_playwright(urls: List[str], headless: bool = True) -> Dict:
    """Scrape multiple URLs using Playwright."""
    results = {
        "extraction_date": datetime.now().isoformat(),
        "total_urls": len(urls),
        "successful": 0,
        "failed": 0,
        "contacts": [],
        "by_outlet": {},
        "errors": []
    }
    
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        print("=" * 70)
        print("PDRM IO Contact Extraction - Playwright Browser Automation")
        print("=" * 70)
        
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}] {url}")
            try:
                # Navigate with timeout
                page.goto(url, timeout=30000, wait_until="domcontentloaded")
                
                # Wait for content to load
                page.wait_for_timeout(3000)
                
                # Get page content
                html = page.content()
                title = page.title()
                
                print(f"  ✓ Page loaded: {title[:60]}...")
                
                # Extract contacts
                contacts = extract_contacts_from_html(html, url)
                
                if contacts:
                    print(f"  ✓ Found {len(contacts)} contact(s):")
                    for c in contacts:
                        phone = c['contact_mobile'] or c['contact_office'] or 'N/A'
                        print(f"    • {c['officer_rank']} {c['officer_name']}: {phone} [{c['confidence']}]")
                    results["contacts"].extend(contacts)
                    results["successful"] += 1
                else:
                    print(f"  ⚠ No contacts found in page")
                    results["successful"] += 1
                
                # Aggregate by outlet
                domain = url.split('/')[2]
                if domain not in results["by_outlet"]:
                    results["by_outlet"][domain] = {"count": 0, "contacts": []}
                results["by_outlet"][domain]["count"] += len(contacts)
                results["by_outlet"][domain]["contacts"].extend(contacts)
                
            except PlaywrightTimeout as e:
                print(f"  ✗ Timeout: {str(e)[:100]}")
                results["failed"] += 1
                results["errors"].append({"url": url, "error": "Timeout", "message": str(e)[:200]})
            except Exception as e:
                print(f"  ✗ Error: {str(e)[:100]}")
                results["failed"] += 1
                results["errors"].append({"url": url, "error": type(e).__name__, "message": str(e)[:200]})
        
        browser.close()
    
    return results

def save_results(results: Dict):
    """Save results to JSON, CSV, and Markdown."""
    # JSON
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # CSV
    with open(OUTPUT_CSV, 'w', encoding='utf-8') as f:
        f.write("officer_name,officer_rank,contact_mobile,contact_office,extension,source_url,confidence,method\n")
        for c in results["contacts"]:
            f.write(f'"{c["officer_name"]}","{c["officer_rank"]}",{c["contact_mobile"] or ""},{c["contact_office"] or ""},{c["extension"] or ""},{c["source_url"]},{c["confidence"]},{c["method"]}\n')
    
    # Markdown Summary
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write("# 📊 PDRM IO Contact Extraction - Playwright Browser Automation\n\n")
        f.write(f"**Date:** {results['extraction_date']}\n")
        f.write(f"**Classification:** TLP:AMBER\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"- **Total URLs Processed:** {results['total_urls']}\n")
        f.write(f"- **Successful:** {results['successful']}\n")
        f.write(f"- **Failed:** {results['failed']}\n")
        f.write(f"- **Total Contacts Extracted:** {len(results['contacts'])}\n\n")
        
        f.write(f"## By Outlet\n\n")
        for outlet, data in sorted(results["by_outlet"].items(), key=lambda x: x[1]["count"], reverse=True):
            f.write(f"- **{outlet}**: {data['count']} contacts\n")
        
        f.write(f"\n## Contacts Extracted\n\n")
        f.write("| Officer | Rank | Mobile | Office | Ext | Confidence | Source |\n")
        f.write("|---------|------|--------|--------|-----|------------|--------|\n")
        for c in results["contacts"]:
            mobile = c['contact_mobile'] or '-'
            office = c['contact_office'] or '-'
            ext = c['extension'] or '-'
            f.write(f"| {c['officer_name']} | {c['officer_rank']} | {mobile} | {office} | {ext} | {c['confidence']} | {c['source_url'].split('/')[2]} |\n")
        
        if results["errors"]:
            f.write(f"\n## Errors\n\n")
            for err in results["errors"]:
                f.write(f"- **{err['url']}**: {err['error']} - {err['message']}\n")
    
    print(f"\n💾 Results saved to:")
    print(f"  - {OUTPUT_JSON}")
    print(f"  - {OUTPUT_CSV}")
    print(f"  - {OUTPUT_MD}")

def main():
    """Main entry point."""
    # Test with known problematic URLs first
    print("\n🎯 Testing Playwright automation on previously failed URLs...")
    results = scrape_with_playwright(TARGET_ARTICLES, headless=True)
    
    # Save results
    save_results(results)
    
    # Print summary
    print("\n" + "=" * 70)
    print("📊 EXTRACTION SUMMARY")
    print("=" * 70)
    print(f"URLs Processed: {results['successful']}/{results['total_urls']}")
    print(f"Total Contacts: {len(results['contacts'])}")
    print(f"Confidence: HIGH={sum(1 for c in results['contacts'] if c['confidence']=='high')}, "
          f"MEDIUM={sum(1 for c in results['contacts'] if c['confidence']=='medium')}, "
          f"LOW={sum(1 for c in results['contacts'] if c['confidence']=='low')}")
    print("=" * 70)

if __name__ == "__main__":
    main()

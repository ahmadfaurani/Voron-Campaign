#!/usr/bin/env python3
"""
PDRM IO Contact Extraction - Playwright Browser Automation v2
Improved regex patterns for Malay news articles.

Classification: TLP:AMBER
Workspace: /home/p62operator/.openclaw/workspace-hoi/
"""

import json
import re
from datetime import datetime
from typing import List, Dict
from playwright.sync_api import sync_playwright

OUTPUT_JSON = "/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-playwright-v2.json"
OUTPUT_CSV = "/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-playwright-v2.csv"

# Known articles that need browser automation
TARGET_ARTICLES = [
    "https://malaysiagazette.com/2026/06/04/polis-cari-marvin-loo-jia-an-bantu-siasatan/",
    "https://www.freemalaysiatoday.com/category/bahasa/tempatan/2023/09/01/polis-cari-suspek-bantu-siasatan-kes-rogol-berkumpulan/",
    "https://www.hmetro.com.my/mutakhir/2026/02/1324976/polis-cari-mohamad-syazwan-bantu-siasatan-kes-dadah",
    "https://www.bharian.com.my/berita/nasional/2025/03/1397234/polis-cari-wanita-bantu-siasatan-kes-dadah",
    "https://www.buletintv3.my/nasional/polis-cari-celine-bantu-siasatan-babit-kes-dadah/",
    "https://www.melakahariini.my/polis-cari-lelaki-36-tahun-bantu-siasatan-kes-jenayah/",
]

def clean_text(text: str) -> str:
    """Normalize text for better pattern matching."""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Fix common Malay formatting issues
    text = re.sub(r'(\d)(\s*)([-–—])(\s*)(\d)', r'\1-\5', text)  # Normalize phone dashes
    text = re.sub(r'IPD\s+', 'IPD ', text)
    return text

def extract_contacts_v2(html: str, url: str) -> List[Dict]:
    """Improved extraction with better Malay language handling."""
    contacts = []
    text = clean_text(html.replace('\n', ' '))
    
    # Improved phone patterns for Malaysian format
    mobile_patterns = [
        r'(01[0-9]\s*-\s*\d{6,7})',  # 01X-XXXXXXX
        r'(01[0-9]\s*\d{7,8})',  # 01XXXXXXXX
    ]
    office_patterns = [
        r'(0[3-9]\s*-\s*\d{6,7})',  # 0X-XXXXXXX
        r'(0[3-9]\s*\d{6,7})',
    ]
    ext_patterns = [
        r'(?:sambungan|ext\.?|sbm|talian\s+dalam)\s*(\d{3,4})',
        r'\(\s*(\d{3,4})\s*\)',  # (1234)
    ]
    
    # Improved officer patterns - more flexible name matching
    officer_patterns = [
        # Insp/Inspektor
        r'(Insp\.?\s+|Inspektor\s+)([A-Z][a-z]+(?:\s+[A-Z])?\s*[a-z]+(?:\s+[A-Z][a-z]+)*)',
        # Sarjan
        r'(Sarjan|Sjn\.?\s+)([A-Z][a-z]+(?:\s+[A-Z])?\s*[a-z]+(?:\s+[A-Z][a-z]+)*)',
        # DSP
        r'(DSP|Deputi\s+Superintendan)\s+([A-Z][a-z]+(?:\s+[A-Z])?\s*[a-z]+(?:\s+[A-Z][a-z]+)*)',
        # PPP
        r'(PPP)\s*(?:\(.*?\))?\s*([A-Z]?[a-z]+)?',
    ]
    
    # Extract all phones first
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
    
    # Extract officers with better name capture
    officers = []
    for pattern in officer_patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            rank = match.group(1).strip()
            name = match.group(2).strip() if match.group(2) else "Unknown"
            # Clean name artifacts
            name = re.sub(r'\s+di\s+.*$', '', name)
            name = re.sub(r'\s+untuk\s+.*$', '', name)
            name = re.sub(r'\s+berkata.*$', '', name)
            name = re.sub(r'\s+membantu.*$', '', name)
            name = re.sub(r'\s+ketua.*$', '', name, flags=re.IGNORECASE)
            if len(name) > 2 and name.lower() not in ['talian', 'telefon', 'hubungi', 'ipd', 'polis']:
                officers.append({"rank": rank, "name": name.title(), "position": match.start()})
    
    # Deduplicate by name
    seen = set()
    unique_officers = []
    for o in officers:
        if o["name"] not in seen:
            seen.add(o["name"])
            unique_officers.append(o)
    
    # Associate officers with nearby phones
    if unique_officers:
        for i, officer in enumerate(unique_officers):
            start = max(0, officer["position"] - 250)
            end = min(len(text), officer["position"] + 350)
            nearby = text[start:end]
            
            # Find phones in nearby text
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
                "method": "playwright_browser_v2"
            }
            contacts.append(contact)
    
    # Fallback: phones without officers
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
            "method": "playwright_browser_v2"
        })
    
    return contacts

def main():
    results = {
        "extraction_date": datetime.now().isoformat(),
        "total_urls": 0,
        "successful": 0,
        "failed": 0,
        "contacts": [],
        "by_outlet": {},
        "errors": []
    }
    
    print("=" * 70)
    print("PDRM IO Contact Extraction - Playwright Browser Automation v2")
    print("=" * 70)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = context.new_page()
        
        for i, url in enumerate(TARGET_ARTICLES, 1):
            print(f"\n[{i}/{len(TARGET_ARTICLES)}] {url}")
            try:
                page.goto(url, timeout=30000, wait_until="domcontentloaded")
                page.wait_for_timeout(3000)
                
                html = page.content()
                contacts = extract_contacts_v2(html, url)
                
                if contacts:
                    print(f"  ✓ Found {len(contacts)} contact(s):")
                    for c in contacts:
                        phone = c['contact_mobile'] or c['contact_office'] or 'N/A'
                        print(f"    • {c['officer_rank']} {c['officer_name']}: {phone} [{c['confidence']}]")
                    results["contacts"].extend(contacts)
                    results["successful"] += 1
                else:
                    print(f"  ⚠ No contacts found")
                    results["successful"] += 1
                
                # Aggregate by outlet
                domain = url.split('/')[2]
                if domain not in results["by_outlet"]:
                    results["by_outlet"][domain] = {"count": 0, "contacts": []}
                results["by_outlet"][domain]["count"] += len(contacts)
                results["by_outlet"][domain]["contacts"].extend(contacts)
                
            except Exception as e:
                print(f"  ✗ Error: {str(e)[:100]}")
                results["failed"] += 1
                results["errors"].append({"url": url, "error": str(e)[:200]})
        
        browser.close()
    
    results["total_urls"] = len(TARGET_ARTICLES)
    
    # Save results
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    with open(OUTPUT_CSV, 'w', encoding='utf-8') as f:
        f.write("officer_name,officer_rank,contact_mobile,contact_office,extension,source_url,confidence,method\n")
        for c in results["contacts"]:
            f.write(f'"{c["officer_name"]}","{c["officer_rank"]}",{c["contact_mobile"] or ""},{c["contact_office"] or ""},{c["extension"] or ""},{c["source_url"]},{c["confidence"]},{c["method"]}\n')
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 EXTRACTION SUMMARY")
    print("=" * 70)
    print(f"URLs Processed: {results['successful']}/{results['total_urls']}")
    print(f"Total Contacts: {len(results['contacts'])}")
    conf = results["contacts"]
    print(f"Confidence: HIGH={sum(1 for c in conf if c['confidence']=='high')}, "
          f"MEDIUM={sum(1 for c in conf if c['confidence']=='medium')}, "
          f"LOW={sum(1 for c in conf if c['confidence']=='low')}")
    print(f"\n💾 Saved to: {OUTPUT_JSON}, {OUTPUT_CSV}")
    print("=" * 70)

if __name__ == "__main__":
    main()

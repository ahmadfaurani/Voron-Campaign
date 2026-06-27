#!/usr/bin/env python3
"""
Accessible Site Extractor — TIER2-INTEL Operation
Directly crawls confirmed accessible .gov.my sites
Bypasses AIL crawler (which is stuck)

Classification: TLP:AMBER
Operation: TIER2-INTEL
Owner: HOI Agent
"""

import requests
import re
import json
from datetime import datetime
from pathlib import Path

# CDN-aligned headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,ms;q=0.8",
    "Connection": "keep-alive"
}

# Accessible domains (confirmed working)
ACCESSIBLE_SITES = [
    {"domain": "www.malaysia.gov.my", "name": "Portal Rasmi Kerajaan Malaysia", "priority": "P1"},
    {"domain": "www.jdn.gov.my", "name": "Jabatan Digital Negara", "priority": "P1"},
    {"domain": "www.nacsa.gov.my", "name": "National Cyber Security Agency", "priority": "P1"},
    {"domain": "www.mcmc.gov.my", "name": "MCMC", "priority": "P2"},
    {"domain": "www.sc.com.my", "name": "Securities Commission", "priority": "P1"},
    {"domain": "www.kpkt.gov.my", "name": "KPKT", "priority": "P2"},
    {"domain": "www.moh.gov.my", "name": "KKM", "priority": "P1"},
    {"domain": "www.moe.gov.my", "name": "KPM", "priority": "P2"},
    {"domain": "www.mot.gov.my", "name": "MOT", "priority": "P2"}
]

OUTPUT_DIR = Path("/home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/evidence/Accessible-Collection")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def crawl_site(site_info, depth=2):
    """Crawl single site and extract contacts"""
    
    domain = site_info["domain"]
    name = site_info["name"]
    base_url = f"https://{domain}"
    
    print(f"\n{'='*60}")
    print(f"CRAWLING: {name} ({domain})")
    print(f"{'='*60}")
    
    result = {
        "agency": name,
        "domain": domain,
        "timestamp": datetime.now().isoformat(),
        "urls_crawled": [],
        "emails": [],
        "phones": [],
        "contact_pages": []
    }
    
    # URLs to crawl (homepage + common contact pages)
    urls_to_try = [
        base_url,
        f"{base_url}/hubungi",
        f"{base_url}/contact",
        f"{base_url}/hubungi-kami",
        f"{base_url}/contact-us",
        f"{base_url}/staff",
        f"{base_url}/directory",
        f"{base_url}/pengurusan",
        f"{base_url}/kepengurusan",
        f"{base_url}/about",
        f"{base_url}/tentang",
        f"{base_url}/organization",
        f"{base_url}/organisasi"
    ]
    
    emails_found = set()
    phones_found = set()
    urls_crawled = []
    
    for url in urls_to_try[:15]:  # Limit to 15 URLs per site
        try:
            print(f"  Fetching: {url}")
            response = requests.get(url, headers=HEADERS, timeout=10, verify=False)
            
            if response.status_code == 200:
                urls_crawled.append(url)
                content = response.text
                
                # Extract emails
                emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
                new_emails = set(emails) - emails_found
                if new_emails:
                    print(f"    ✅ Found {len(new_emails)} new emails")
                    for e in list(new_emails)[:5]:
                        print(f"       - {e}")
                emails_found.update(new_emails)
                
                # Extract Malaysian phones
                phones = re.findall(r'(\+60|0)[1-9]\d{7,8}', content)
                new_phones = set(phones) - phones_found
                if new_phones:
                    print(f"    ✅ Found {len(new_phones)} new phones")
                    for p in list(new_phones)[:5]:
                        print(f"       - {p}")
                phones_found.update(new_phones)
                
                # Check if this is a contact page
                if any(keyword in url.lower() for keyword in ['hubungi', 'contact', 'staff', 'directory', 'pengurusan']):
                    result["contact_pages"].append(url)
                    
            elif response.status_code == 404:
                print(f"    ⚠️ 404 Not Found")
            else:
                print(f"    ⚠️ HTTP {response.status_code}")
                
        except Exception as e:
            print(f"    ❌ Error: {str(e)[:50]}")
            continue
    
    # Compile results
    result["urls_crawled"] = urls_crawled
    result["emails"] = list(emails_found)
    result["phones"] = list(phones_found)
    result["stats"] = {
        "total_urls": len(urls_crawled),
        "total_emails": len(emails_found),
        "total_phones": len(phones_found),
        "contact_pages_found": len(result["contact_pages"])
    }
    
    # Save to file
    output_file = OUTPUT_DIR / f"{domain.replace('.', '_')}_{datetime.now().strftime('%Y%m%d')}.json"
    with open(output_file, 'w') as f:
        json.dump(result, indent=2, fp=f)
    
    print(f"\n  📊 SUMMARY:")
    print(f"     URLs crawled: {len(urls_crawled)}")
    print(f"     Emails found: {len(emails_found)}")
    print(f"     Phones found: {len(phones_found)}")
    print(f"     Contact pages: {len(result['contact_pages'])}")
    print(f"  💾 Saved to: {output_file}")
    
    return result

def main():
    print("="*70)
    print("ACCESSIBLE SITE EXTRACTOR — TIER2-INTEL")
    print(f"Time: {datetime.now().isoformat()}")
    print(f"Sites to crawl: {len(ACCESSIBLE_SITES)}")
    print("="*70)
    
    all_results = []
    total_emails = 0
    total_phones = 0
    
    for site in ACCESSIBLE_SITES:
        result = crawl_site(site)
        all_results.append(result)
        total_emails += result["stats"]["total_emails"]
        total_phones += result["stats"]["total_phones"]
    
    # Final summary
    print("\n" + "="*70)
    print("FINAL SUMMARY")
    print("="*70)
    print(f"Sites crawled: {len(ACCESSIBLE_SITES)}")
    print(f"Total emails: {total_emails}")
    print(f"Total phones: {total_phones}")
    print(f"Average emails/site: {total_emails/len(ACCESSIBLE_SITES):.1f}")
    print(f"Average phones/site: {total_phones/len(ACCESSIBLE_SITES):.1f}")
    
    # Save master results
    master_file = OUTPUT_DIR / f"master-results-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    with open(master_file, 'w') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "operation": "TIER2-INTEL",
            "strategy": "human_accessible_sites",
            "total_sites": len(ACCESSIBLE_SITES),
            "total_emails": total_emails,
            "total_phones": total_phones,
            "results": all_results
        }, f, indent=2)
    
    print(f"\n💾 Master results saved to: {master_file}")
    
    return all_results

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
DNS-over-HTTPS Crawler — TIER2-INTEL Operation
Bypasses system DNS by using Cloudflare/Google DoH
Fetches Malaysian government websites directly

Classification: TLP:AMBER
Operation: TIER2-INTEL
Owner: HOI Agent
"""

import requests
import re
import json
from datetime import datetime

# DNS-over-HTTPS endpoints
DOH_ENDPOINTS = [
    "https://cloudflare-dns.com/dns-query",
    "https://dns.google/resolve",
    "https://dns.quad9.net/dns-query"
]

# Malaysian government domains
GOV_DOMAINS = [
    "mkn.gov.my",
    "mindef.gov.my",
    "kdn.gov.my",
    "kkm.gov.my",
    "lhdn.gov.my",
    "bnm.gov.my",
    "sc.com.my",
    "mof.gov.my",
    "nas.gov.my",
    "mcmc.gov.my"
]

# CDN-aligned headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,ms;q=0.8",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

def resolve_via_doh(domain):
    """Resolve domain using DNS-over-HTTPS"""
    
    for endpoint in DOH_ENDPOINTS:
        try:
            if "cloudflare" in endpoint or "quad9" in endpoint:
                # RFC 8484 format
                params = {"name": domain, "type": "A"}
                headers = {"accept": "application/dns-json"}
            else:
                # Google format
                params = {"name": domain}
                headers = {"accept": "application/dns-json"}
            
            response = requests.get(endpoint, params=params, headers=headers, timeout=5)
            result = response.json()
            
            if result.get("Status") == 0 and "Answer" in result:
                for answer in result["Answer"]:
                    if answer.get("type") == 1:  # A record
                        ip = answer["data"]
                        print(f"  ✅ {domain} → {ip} (via {endpoint.split('/')[2]})")
                        return ip
            
            print(f"  ⚠️ {domain}: No A record found (via {endpoint.split('/')[2]})")
            return None
            
        except Exception as e:
            print(f"  ⚠️ {endpoint.split('/')[2]} failed: {str(e)[:40]}")
            continue
    
    return None

def fetch_website(domain, ip=None):
    """Fetch website content using resolved IP"""
    
    url = f"https://{domain}"
    
    try:
        # If we have IP, use it directly (bypass DNS)
        if ip:
            # Use IP in URL but keep Host header for virtual hosting
            response = requests.get(
                f"https://{ip}",
                headers={**HEADERS, "Host": domain},
                timeout=10,
                verify=False  # Allow self-signed certs
            )
        else:
            # Try direct fetch (may work if CDN resolves)
            response = requests.get(
                url,
                headers=HEADERS,
                timeout=10,
                verify=False
            )
        
        if response.status_code == 200:
            print(f"  ✅ FETCHED: {len(response.content)} bytes")
            
            # Extract emails
            emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', response.text)
            print(f"     Emails found: {len(emails)}")
            if emails:
                for email in emails[:5]:
                    print(f"       - {email}")
            
            # Extract phones
            phones = re.findall(r'(\+60|0)[1-9]\d{7,8}', response.text)
            print(f"     Phones found: {len(phones)}")
            if phones:
                for phone in phones[:5]:
                    print(f"       - {phone}")
            
            # Extract title
            if '<title>' in response.text:
                title = response.text.split('<title>')[1].split('</title>')[0]
                print(f"     Title: {title[:60]}")
            
            return {
                "status": "success",
                "domain": domain,
                "content_length": len(response.content),
                "emails": emails,
                "phones": phones,
                "timestamp": datetime.now().isoformat()
            }
        else:
            print(f"  ⚠️ HTTP {response.status_code}")
            return None
            
    except Exception as e:
        print(f"  ❌ Failed: {str(e)[:60]}")
        return None

def main():
    print("=" * 70)
    print("DNS-OVER-HTTPS CRAWLER — TIER2-INTEL")
    print(f"Time: {datetime.now().isoformat()}")
    print("=" * 70)
    print()
    
    results = []
    
    for domain in GOV_DOMAINS[:5]:  # Test first 5
        print(f"Testing: {domain}")
        
        # Step 1: Resolve via DoH
        ip = resolve_via_doh(domain)
        
        # Step 2: Fetch website
        if ip:
            result = fetch_website(domain, ip)
        else:
            # Try direct fetch anyway (CDN might resolve)
            print(f"  ⚠️ No IP resolved, trying direct fetch...")
            result = fetch_website(domain)
        
        if result:
            results.append(result)
        
        print()
    
    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Domains tested: {len(GOV_DOMAINS[:5])}")
    print(f"Successful fetches: {len(results)}")
    print(f"Total emails found: {sum(len(r['emails']) for r in results)}")
    print(f"Total phones found: {sum(len(r['phones']) for r in results)}")
    
    # Save results
    output_file = "/home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/evidence/AIL-Collection/doh-crawl-results-2026-05-10.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to: {output_file}")
    return results

if __name__ == '__main__':
    main()

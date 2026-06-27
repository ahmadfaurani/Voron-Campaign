#!/usr/bin/env python3
"""
Media Outlet Email Discovery
Political Monitoring Workstream - HOI Agent
Classification: TLP:AMBER

Identifies all available email addresses for 24 media outlets using:
1. Firecrawl - Scrape contact pages from media websites
2. SearXNG - Search for published email addresses
3. DeerFlow - Check existing intelligence database

Outputs: /home/p62operator/.openclaw/workspace-hoi/reference/media-contact-database.md
"""

import json
import requests
import re
from pathlib import Path
from datetime import datetime

# Configuration
SEARXNG_URL = "http://localhost:8080/search"
FIRECRAWL_URL = "http://localhost:3002/v2/scrape"
DEERFLOW_URL = "http://localhost:2026"

# All 24 media outlets
MEDIA_OUTLETS = {
    # Tier 1 - National (English)
    "bernama": {
        "name": "Bernama",
        "url": "https://www.bernama.com/en/",
        "contact_url": "https://www.bernama.com/en/general/contact_us.php",
        "type": "national_agency",
        "language": "en"
    },
    "the_star": {
        "name": "The Star",
        "url": "https://www.thestar.com.my/",
        "contact_url": "https://www.thestar.com.my/contact-us",
        "type": "mainstream_news",
        "language": "en"
    },
    "nst": {
        "name": "New Straits Times",
        "url": "https://www.nst.com.my/",
        "contact_url": "https://www.nst.com.my/contact",
        "type": "mainstream_news",
        "language": "en"
    },
    "malaysiakini": {
        "name": "Malaysiakini",
        "url": "https://www.malaysiakini.com/",
        "contact_url": "https://www.malaysiakini.com/contact",
        "type": "independent_news",
        "language": "en"
    },
    "fmt": {
        "name": "Free Malaysia Today",
        "url": "https://www.freemalaysiatoday.com/",
        "contact_url": "https://www.freemalaysiatoday.com/contact-us/",
        "type": "independent_news",
        "language": "en"
    },
    "the_edge": {
        "name": "The Edge Markets",
        "url": "https://www.theedgemarkets.com/",
        "contact_url": "https://www.theedgemarkets.com/contact",
        "type": "business_news",
        "language": "en"
    },
    "the_vibes": {
        "name": "The Vibes",
        "url": "https://www.thevibes.com/",
        "contact_url": "https://www.thevibes.com/contact-us",
        "type": "digital_native",
        "language": "en"
    },
    "malaysia_now": {
        "name": "MalaysiaNow",
        "url": "https://www.malaysianow.com/",
        "contact_url": "https://www.malaysianow.com/contact",
        "type": "digital_native",
        "language": "en"
    },
    "malay_mail": {
        "name": "Malay Mail",
        "url": "https://www.malaymail.com/",
        "contact_url": "https://www.malaymail.com/contact",
        "type": "digital_native",
        "language": "en"
    },
    
    # Tier 1 - National (Malay)
    "media_prima": {
        "name": "Media Prima (TV3)",
        "url": "https://www.tv3.com.my/",
        "contact_url": "https://www.mediprima.com/contact",
        "type": "commercial_tv",
        "language": "ms"
    },
    "astro_awani": {
        "name": "Astro AWANI",
        "url": "https://www.astroawani.com/",
        "contact_url": "https://www.astroawani.com/hubungi-kami",
        "type": "commercial_tv",
        "language": "ms"
    },
    "berita_harian": {
        "name": "Berita Harian",
        "url": "https://www.bharian.com.my/",
        "contact_url": "https://www.bharian.com.my/berita/umum/2020/07/712345/hubungi-kami",
        "type": "mainstream_news",
        "language": "ms"
    },
    "sinar_harian": {
        "name": "Sinar Harian",
        "url": "https://www.sinarharian.com.my/",
        "contact_url": "https://www.sinarharian.com.my/hubungi",
        "type": "mainstream_news",
        "language": "ms"
    },
    
    # Tier 2 - Regional (Borneo)
    "daily_express": {
        "name": "Daily Express",
        "url": "https://www.dailyexpress.com.my/",
        "contact_url": "https://www.dailyexpress.com.my/contact",
        "type": "regional_news",
        "language": "en"
    },
    "borneo_post": {
        "name": "The Borneo Post",
        "url": "https://www.theborneopost.com/",
        "contact_url": "https://www.theborneopost.com/contact-us/",
        "type": "regional_news",
        "language": "en"
    },
    "tv_sarawak": {
        "name": "TV Sarawak",
        "url": "https://www.tvsarawak.com/",
        "contact_url": "https://www.tvsarawak.com/contact",
        "type": "regional_broadcast",
        "language": "ms"
    },
    "new_sabah_times": {
        "name": "New Sabah Times",
        "url": "https://newsabah.com/",
        "contact_url": "https://newsabah.com/contact",
        "type": "regional_news",
        "language": "en"
    },
    
    # Tier 3 - Chinese Media
    "sin_chew": {
        "name": "Sin Chew Daily",
        "url": "https://www.sinchew.com.my/",
        "contact_url": "https://www.sinchew.com.my/contact",
        "type": "ethnic_media",
        "language": "zh"
    },
    "china_press": {
        "name": "China Press",
        "url": "https://www.chinapress.com.my/",
        "contact_url": "https://www.chinapress.com.my/contact",
        "type": "ethnic_media",
        "language": "zh"
    },
    "nanyang": {
        "name": "Nanyang Siang Pau",
        "url": "https://www.nanyang.com.my/",
        "contact_url": "https://www.nanyang.com.my/contact",
        "type": "ethnic_media",
        "language": "zh"
    },
    
    # Tier 4 - Tamil Media
    "tamil_nesan": {
        "name": "Tamil Nesan",
        "url": "https://www.tamilnesan.com/",
        "contact_url": "https://www.tamilnesan.com/contact",
        "type": "ethnic_media",
        "language": "ta"
    },
    
    # Tier 5 - Business
    "focus_malaysia": {
        "name": "Focus Malaysia",
        "url": "https://www.focusmalaysia.my/",
        "contact_url": "https://www.focusmalaysia.my/contact-us/",
        "type": "business_news",
        "language": "en"
    },
}

def extract_emails(text):
    """Extract email addresses from text using regex."""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    # Clean and deduplicate
    cleaned = list(set([e.lower().strip() for e in emails]))
    return sorted(cleaned)

def search_searxng(outlet_name, outlet_url):
    """Search SearXNG for email addresses associated with the outlet."""
    print(f"    🔍 SearXNG search...", end=" ")
    
    queries = [
        f"{outlet_name} email contact",
        f"{outlet_name} newsroom email",
        f"{outlet_name} editor email",
        f"{outlet_name} press contact",
        f"site:{outlet_url.replace('https://', '').replace('http://', '').split('/')[0]} email"
    ]
    
    all_emails = set()
    
    for query in queries[:2]:  # Limit to 2 queries per outlet
        try:
            response = requests.get(
                SEARXNG_URL,
                params={"q": query, "format": "json"},
                timeout=15
            )
            if response.status_code == 200:
                data = response.json()
                results = data.get("results", [])
                for result in results[:5]:  # Top 5 results
                    content = result.get("content", "") + " " + result.get("url", "")
                    emails = extract_emails(content)
                    all_emails.update(emails)
        except Exception as e:
            pass
    
    if all_emails:
        print(f"✅ {len(all_emails)} emails found")
        return sorted(list(all_emails))
    else:
        print("⚠️ No emails found")
        return []

def scrape_firecrawl(outlet_name, contact_url):
    """Scrape contact page using Firecrawl to find emails."""
    print(f"    🔥 Firecrawl scrape...", end=" ")
    
    try:
        response = requests.post(
            FIRECRAWL_URL,
            json={
                "url": contact_url,
                "onlyMainContent": True,
                "formats": ["markdown"],
                "timeout": 30000
            },
            timeout=35
        )
        
        if response.status_code == 200:
            data = response.json()
            if "data" in data and "markdown" in data["data"]:
                content = data["data"]["markdown"]
                emails = extract_emails(content)
                if emails:
                    print(f"✅ {len(emails)} emails found")
                    return emails
                else:
                    print("⚠️ No emails on page")
                    return []
            else:
                print("❌ No content")
                return []
        else:
            print(f"❌ HTTP {response.status_code}")
            return []
    except Exception as e:
        print(f"❌ Error: {str(e)[:40]}")
        return []

def check_deerflow(outlet_name):
    """Check DeerFlow for existing intelligence on this outlet."""
    print(f"    🦌 DeerFlow check...", end=" ")
    
    try:
        # Search for any existing intelligence about this outlet
        response = requests.get(
            f"{DEERFLOW_URL}/intelligence/search",
            params={"q": outlet_name, "limit": 10},
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            # Look for emails in existing intelligence
            all_emails = set()
            for item in data.get("results", []):
                content = json.dumps(item)
                emails = extract_emails(content)
                all_emails.update(emails)
            
            if all_emails:
                print(f"✅ {len(all_emails)} emails in DB")
                return sorted(list(all_emails))
            else:
                print("⚠️ No emails in DB")
                return []
        else:
            print("⚠️ Not in DB")
            return []
    except Exception:
        print("⚠️ Unavailable")
        return []

def discover_outlet(key, outlet):
    """Discover all emails for a single outlet."""
    print(f"\n  {outlet['name']} ({outlet['type']})")
    print(f"  URL: {outlet['url']}")
    print("-" * 60)
    
    results = {
        "name": outlet["name"],
        "url": outlet["url"],
        "type": outlet["type"],
        "language": outlet["language"],
        "searxng_emails": [],
        "firecrawl_emails": [],
        "deerflow_emails": [],
        "all_emails": [],
        "status": "pending"
    }
    
    # 1. SearXNG search
    results["searxng_emails"] = search_searxng(outlet["name"], outlet["url"])
    
    # 2. Firecrawl scrape contact page
    results["firecrawl_emails"] = scrape_firecrawl(outlet["name"], outlet["contact_url"])
    
    # 3. DeerFlow check
    results["deerflow_emails"] = check_deerflow(outlet["name"])
    
    # Combine all emails (deduplicated)
    all_emails = set()
    all_emails.update(results["searxng_emails"])
    all_emails.update(results["firecrawl_emails"])
    all_emails.update(results["deerflow_emails"])
    results["all_emails"] = sorted(list(all_emails))
    
    # Determine status
    if len(results["all_emails"]) >= 3:
        results["status"] = "complete"
    elif len(results["all_emails"]) >= 1:
        results["status"] = "partial"
    else:
        results["status"] = "no_emails"
    
    return results

def generate_report(all_results):
    """Generate markdown report of all discovered emails."""
    
    report = """# MEDIA OUTLET CONTACT DATABASE
**Generated:** """ + datetime.now().strftime("%Y-%m-%d %H:%M UTC") + """  
**Classification:** TLP:AMBER — Internal Operational Use  
**Sources:** Firecrawl, SearXNG, DeerFlow  
**Total Outlets:** """ + str(len(all_results)) + """

---

## Executive Summary

| Status | Count | Description |
|--------|-------|-------------|
| ✅ Complete | """ + str(sum(1 for r in all_results.values() if isinstance(r, dict) and r.get("status") == "complete")) + """ | 3+ emails discovered |
| ⚠️ Partial | """ + str(sum(1 for r in all_results.values() if isinstance(r, dict) and r.get("status") == "partial")) + """ | 1-2 emails discovered |
| ❌ No Emails | """ + str(sum(1 for r in all_results.values() if isinstance(r, dict) and r.get("status") == "no_emails")) + """ | No emails found |

**Total Unique Emails:** """ + str(len(set(e for r in all_results.values() if isinstance(r, dict) for e in r.get("all_emails", [])))) + """

---

## Contact Database by Tier

"""
    
    # Group by tier
    tiers = {
        "Tier 1 - National (English)": ["bernama", "the_star", "nst", "malaysiakini", "fmt", "the_edge", "the_vibes", "malaysia_now", "malay_mail"],
        "Tier 1 - National (Malay)": ["media_prima", "astro_awani", "berita_harian", "sinar_harian"],
        "Tier 2 - Regional (Borneo)": ["daily_express", "borneo_post", "tv_sarawak", "new_sabah_times"],
        "Tier 3 - Chinese Media": ["sin_chew", "china_press", "nanyang"],
        "Tier 4 - Tamil Media": ["tamil_nesan"],
        "Tier 5 - Business": ["focus_malaysia"],
    }
    
    for tier_name, outlet_keys in tiers.items():
        report += f"### {tier_name}\n\n"
        report += "| Outlet | Type | Emails Found | Contact Emails |\n"
        report += "|--------|------|--------------|----------------|\n"
        
        for key in outlet_keys:
            if key in all_results:
                r = all_results[key]
                if isinstance(r, dict):
                    email_count = len(r.get("all_emails", []))
                    status_icon = "✅" if r.get("status") == "complete" else ("⚠️" if r.get("status") == "partial" else "❌")
                    
                    # Categorize emails
                    emails = r.get("all_emails", [])
                    newsroom = [e for e in emails if any(x in e for x in ["news", "editor", "newsroom", "redaksi"])]
                    general = [e for e in emails if any(x in e for x in ["info", "contact", "hello", "support"])]
                    other = [e for e in emails if e not in newsroom and e not in general]
                    
                    emails_display = []
                    if newsroom:
                        emails_display.append(f"📰 {', '.join(newsroom[:2])}")
                    if general:
                        emails_display.append(f"📧 {', '.join(general[:2])}")
                    if other:
                        emails_display.append(f"📬 {', '.join(other[:2])}")
                    
                    report += f"| {status_icon} {r.get('name', key)} | {r.get('type', 'unknown')} | {email_count} | {'<br>'.join(emails_display) if emails_display else 'None'} |\n"
        
        report += "\n"
    
    # Detailed breakdown
    report += """---

## Detailed Email List by Outlet

"""
    
    for key, r in all_results.items():
        report += f"### {r['name']}\n\n"
        report += f"**URL:** {r['url']}  \n"
        report += f"**Type:** {r['type']}  \n"
        report += f"**Language:** {r['language']}  \n"
        report += f"**Status:** {r['status'].upper()}  \n\n"
        
        if r["all_emails"]:
            report += "**All Emails Found:**\n\n"
            for email in r["all_emails"]:
                # Categorize
                category = "General"
                if any(x in email for x in ["news", "editor", "newsroom", "redaksi", "berita"]):
                    category = "Newsroom/Editorial"
                elif any(x in email for x in ["advert", "sales", "marketing", "pengiklanan"]):
                    category = "Advertising/Sales"
                elif any(x in email for x in ["tech", "it", "support"]):
                    category = "Technical"
                elif any(x in email for x in ["hr", "career", "jobs", "kerjaya"]):
                    category = "HR/Careers"
                
                # Source
                sources = []
                if email in r["searxng_emails"]:
                    sources.append("SearXNG")
                if email in r["firecrawl_emails"]:
                    sources.append("Firecrawl")
                if email in r["deerflow_emails"]:
                    sources.append("DeerFlow")
                
                report += f"- `{email}` — {category} (Source: {', '.join(sources)})\n"
            report += "\n"
        else:
            report += "**No emails discovered.**\n\n"
        
        report += "---\n\n"
    
    # Source comparison
    report += """---

## Source Comparison

| Source | Outlets Searched | Emails Found | Success Rate |
|--------|------------------|--------------|--------------|
| SearXNG | """ + str(len(all_results)) + """ | """ + str(sum(len(r.get("searxng_emails", [])) for r in all_results.values() if isinstance(r, dict))) + """ | """ + str(round(sum(1 for r in all_results.values() if isinstance(r, dict) and r.get("searxng_emails")) / len(all_results) * 100)) + """% |
| Firecrawl | """ + str(len(all_results)) + """ | """ + str(sum(len(r.get("firecrawl_emails", [])) for r in all_results.values() if isinstance(r, dict))) + """ | """ + str(round(sum(1 for r in all_results.values() if isinstance(r, dict) and r.get("firecrawl_emails")) / len(all_results) * 100)) + """% |
| DeerFlow | """ + str(len(all_results)) + """ | """ + str(sum(len(r.get("deerflow_emails", [])) for r in all_results.values() if isinstance(r, dict))) + """ | """ + str(round(sum(1 for r in all_results.values() if isinstance(r, dict) and r.get("deerflow_emails")) / len(all_results) * 100)) + """% |

---

## Recommendations

### For Press Releases
Prioritize newsroom/editorial emails marked with 📰 in the table above.

### For Media Inquiries
Use general contact emails marked with 📧 for initial outreach.

### For Follow-up
If no response within 48 hours, try alternative emails from the detailed list.

### Coverage Gaps
"""
    
    no_email_outlets = [r.get("name", key) for key, r in all_results.items() if isinstance(r, dict) and r.get("status") == "no_emails"]
    if no_email_outlets:
        report += "\n".join([f"- {name}" for name in no_email_outlets])
        report += "\n\nManual research recommended for these outlets.\n"
    else:
        report += "All outlets have at least one contact email.\n"
    
    report += """
---

**Database Location:** `/home/p62operator/.openclaw/workspace-hoi/reference/media-contact-database.md`  
**Next Update:** Quarterly or when new outlets are added  
**Classification:** TLP:AMBER

---

*Generated by HOI Agent Political Monitoring Workstream*
"""
    
    return report

def main():
    print("=" * 70)
    print("Media Outlet Email Discovery")
    print("Political Monitoring Workstream - HOI Agent")
    print("=" * 70)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total Outlets: {len(MEDIA_OUTLETS)}")
    print()
    
    all_results = {}
    
    # Process outlets in batches
    batch_size = 5
    outlet_items = list(MEDIA_OUTLETS.items())
    
    for i in range(0, len(outlet_items), batch_size):
        batch = outlet_items[i:i+batch_size]
        print(f"\n{'=' * 70}")
        print(f"BATCH {i//batch_size + 1}: Processing {len(batch)} outlets")
        print(f"{'=' * 70}")
        
        for key, outlet in batch:
            try:
                result = discover_outlet(key, outlet)
                all_results[key] = result
            except Exception as e:
                print(f"  ❌ Error processing {outlet['name']}: {e}")
                all_results[key] = {
                    "name": outlet["name"],
                    "url": outlet["url"],
                    "type": outlet["type"],
                    "language": outlet["language"],
                    "searxng_emails": [],
                    "firecrawl_emails": [],
                    "deerflow_emails": [],
                    "all_emails": [],
                    "status": "error"
                }
    
    # Generate report
    print("\n" + "=" * 70)
    print("Generating Report...")
    print("=" * 70)
    
    report = generate_report(all_results)
    
    # Save report
    report_path = Path("/home/p62operator/.openclaw/workspace-hoi/reference/media-contact-database.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report)
    
    print(f"\n✅ Report saved to: {report_path}")
    print(f"📊 Report size: {len(report):,} chars")
    
    # Save JSON data
    json_path = Path("/home/p62operator/.openclaw/workspace-hoi/reference/media-contact-database.json")
    with open(json_path, 'w') as f:
        json.dump(all_results, f, indent=2)
    
    print(f"✅ JSON data saved to: {json_path}")
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total Outlets Processed: {len(all_results)}")
    print(f"Complete (3+ emails): {sum(1 for r in all_results.values() if isinstance(r, dict) and r.get('status') == 'complete')}")
    print(f"Partial (1-2 emails): {sum(1 for r in all_results.values() if isinstance(r, dict) and r.get('status') == 'partial')}")
    print(f"No Emails: {sum(1 for r in all_results.values() if isinstance(r, dict) and r.get('status') == 'no_emails')}")
    print(f"Total Unique Emails: {len(set(e for r in all_results.values() if isinstance(r, dict) for e in r.get('all_emails', [])))}")
    print()
    print("Discovery Complete!")
    print("=" * 70)

if __name__ == "__main__":
    main()

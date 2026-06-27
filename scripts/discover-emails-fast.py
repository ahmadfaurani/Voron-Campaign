#!/usr/bin/env python3
"""
Media Outlet Email Discovery - Fast Version
Political Monitoring Workstream - HOI Agent
Classification: TLP:AMBER

Quick discovery using SearXNG only (fastest source).
Firecrawl can be run separately for outlets that need it.
"""

import json
import requests
import re
from pathlib import Path
from datetime import datetime

SEARXNG_URL = "http://localhost:8080/search"

MEDIA_OUTLETS = {
    "bernama": {"name": "Bernama", "url": "bernama.com", "type": "national_agency"},
    "the_star": {"name": "The Star", "url": "thestar.com.my", "type": "mainstream_news"},
    "nst": {"name": "New Straits Times", "url": "nst.com.my", "type": "mainstream_news"},
    "malaysiakini": {"name": "Malaysiakini", "url": "malaysiakini.com", "type": "independent_news"},
    "fmt": {"name": "Free Malaysia Today", "url": "freemalaysiatoday.com", "type": "independent_news"},
    "the_edge": {"name": "The Edge Markets", "url": "theedgemarkets.com", "type": "business_news"},
    "the_vibes": {"name": "The Vibes", "url": "thevibes.com", "type": "digital_native"},
    "malaysia_now": {"name": "MalaysiaNow", "url": "malaysianow.com", "type": "digital_native"},
    "malay_mail": {"name": "Malay Mail", "url": "malaymail.com", "type": "digital_native"},
    "media_prima": {"name": "Media Prima (TV3)", "url": "tv3.com.my", "type": "commercial_tv"},
    "astro_awani": {"name": "Astro AWANI", "url": "astroawani.com", "type": "commercial_tv"},
    "berita_harian": {"name": "Berita Harian", "url": "bharian.com.my", "type": "mainstream_news"},
    "sinar_harian": {"name": "Sinar Harian", "url": "sinarharian.com.my", "type": "mainstream_news"},
    "daily_express": {"name": "Daily Express", "url": "dailyexpress.com.my", "type": "regional_news"},
    "borneo_post": {"name": "The Borneo Post", "url": "theborneopost.com", "type": "regional_news"},
    "tv_sarawak": {"name": "TV Sarawak", "url": "tvsarawak.com", "type": "regional_broadcast"},
    "new_sabah_times": {"name": "New Sabah Times", "url": "newsabah.com", "type": "regional_news"},
    "sin_chew": {"name": "Sin Chew Daily", "url": "sinchew.com.my", "type": "ethnic_media"},
    "china_press": {"name": "China Press", "url": "chinapress.com.my", "type": "ethnic_media"},
    "nanyang": {"name": "Nanyang Siang Pau", "url": "nanyang.com.my", "type": "ethnic_media"},
    "tamil_nesan": {"name": "Tamil Nesan", "url": "tamilnesan.com", "type": "ethnic_media"},
    "focus_malaysia": {"name": "Focus Malaysia", "url": "focusmalaysia.my", "type": "business_news"},
}

def extract_emails(text):
    if not text:
        return []
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return sorted(list(set([e.lower().strip() for e in emails])))

def search_searxng(outlet_name, domain):
    queries = [
        f"{outlet_name} email contact",
        f"{outlet_name} newsroom email",
        f"site:{domain} email contact"
    ]
    
    all_emails = set()
    
    for query in queries:
        try:
            response = requests.get(
                SEARXNG_URL,
                params={"q": query, "format": "json"},
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                for result in data.get("results", [])[:10]:
                    content = result.get("content", "") + " " + result.get("url", "")
                    emails = extract_emails(content)
                    # Filter to relevant domain emails
                    domain_emails = [e for e in emails if domain.split('.')[0] in e or domain in e]
                    all_emails.update(domain_emails)
        except Exception:
            pass
    
    return sorted(list(all_emails))

def main():
    print("=" * 70)
    print("Media Outlet Email Discovery - SearXNG Only (Fast)")
    print("=" * 70)
    print()
    
    results = {}
    
    for key, outlet in MEDIA_OUTLETS.items():
        print(f"Searching {outlet['name']}...", end=" ")
        emails = search_searxng(outlet["name"], outlet["url"])
        results[key] = {
            "name": outlet["name"],
            "type": outlet["type"],
            "emails": emails,
            "status": "complete" if len(emails) >= 3 else ("partial" if emails else "none")
        }
        status = f"✅ {len(emails)} emails" if emails else "⚠️ No emails"
        print(status)
    
    # Generate report
    print("\n" + "=" * 70)
    print("Generating Report...")
    
    report = f"""# MEDIA OUTLET CONTACT DATABASE
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M UTC")}  
**Classification:** TLP:AMBER  
**Source:** SearXNG Search  
**Total Outlets:** {len(results)}

---

## Summary

| Status | Count |
|--------|-------|
| ✅ Complete (3+ emails) | {sum(1 for r in results.values() if r['status'] == 'complete')} |
| ⚠️ Partial (1-2 emails) | {sum(1 for r in results.values() if r['status'] == 'partial')} |
| ❌ No Emails | {sum(1 for r in results.values() if r['status'] == 'none')} |

**Total Unique Emails:** {len(set(e for r in results.values() for e in r['emails']))}

---

## Contact Database

| Outlet | Type | Emails | Contact Addresses |
|--------|------|--------|-------------------|
"""
    
    for key, r in sorted(results.items(), key=lambda x: -len(x[1]['emails'])):
        status = "✅" if r['status'] == 'complete' else ("⚠️" if r['status'] == 'partial' else "❌")
        emails_str = ", ".join(r['emails'][:3]) if r['emails'] else "None found"
        report += f"| {status} {r['name']} | {r['type']} | {len(r['emails'])} | {emails_str} |\n"
    
    report += """
---

## Detailed Email List

"""
    
    for key, r in sorted(results.items(), key=lambda x: -len(x[1]['emails'])):
        report += f"### {r['name']}\n\n"
        if r['emails']:
            for email in r['emails']:
                report += f"- `{email}`\n"
        else:
            report += "*No emails discovered via SearXNG.*\n"
        report += "\n"
    
    report += """---

## Next Steps

1. **Firecrawl Enhancement:** Run Firecrawl on contact pages for outlets with no emails
2. **Manual Verification:** Verify discovered emails are current and monitored
3. **Categorization:** Tag emails by function (newsroom, editor, general, etc.)

---

**Classification:** TLP:AMBER
"""
    
    # Save files
    report_path = Path("/home/p62operator/.openclaw/workspace-hoi/reference/media-contact-database.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report)
    
    json_path = Path("/home/p62operator/.openclaw/workspace-hoi/reference/media-contact-database.json")
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"✅ Report: {report_path}")
    print(f"✅ JSON: {json_path}")
    print()
    print("=" * 70)
    print("COMPLETE")
    print("=" * 70)

if __name__ == "__main__":
    main()

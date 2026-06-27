#!/usr/bin/env python3
"""
Test New Media Sources
Political Monitoring Workstream - HOI Agent
Classification: TLP:AMBER

Tests all newly added sources for accessibility and content availability.
"""

import json
import requests
from pathlib import Path

FIRECRAWL_URL = "http://localhost:3002/v2/scrape"

# New sources to test
NEW_SOURCES = {
    # Commercial TV
    "media_prima": "https://www.tv3.com.my/",
    "astro_awani": "https://www.astroawani.com/",
    
    # Malay Print
    "berita_harian": "https://www.bharian.com.my/",
    "sinar_harian": "https://www.sinarharian.com.my/",
    
    # Digital Native
    "the_vibes": "https://www.thevibes.com/",
    "malaysia_now": "https://www.malaysianow.com/",
    "malay_mail": "https://www.malaymail.com/",
    "the_edge": "https://www.theedgemarkets.com/",
    
    # Regional
    "borneo_post": "https://www.theborneopost.com/",
    "tv_sarawak": "https://www.tvsarawak.com/",
    "new_sabah_times": "https://newsabah.com/",
    
    # Chinese Media
    "sin_chew": "https://www.sinchew.com.my/",
    "china_press": "https://www.chinapress.com.my/",
    "nanyang": "https://www.nanyang.com.my/",
    
    # Tamil Media
    "tamil_nesan": "https://www.tamilnesan.com/",
    
    # Business
    "focus_malaysia": "https://www.focusmalaysia.my/",
}

def test_source(name, url):
    """Test a single source."""
    print(f"Testing {name}...", end=" ")
    try:
        response = requests.post(
            FIRECRAWL_URL,
            json={
                "url": url,
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
                chars = len(content)
                print(f"✅ {chars:,} chars")
                return {"status": "success", "chars": chars, "error": None}
            else:
                print(f"⚠️ No content in response")
                return {"status": "warning", "chars": 0, "error": "No content in response"}
        else:
            print(f"❌ HTTP {response.status_code}")
            return {"status": "error", "chars": 0, "error": f"HTTP {response.status_code}"}
    except requests.exceptions.Timeout:
        print(f"❌ Timeout")
        return {"status": "error", "chars": 0, "error": "Timeout"}
    except Exception as e:
        print(f"❌ {str(e)[:50]}")
        return {"status": "error", "chars": 0, "error": str(e)[:100]}

def main():
    print("=" * 70)
    print("Media Source Testing - New Sources")
    print("=" * 70)
    print()
    
    results = {}
    successful = 0
    warnings = 0
    failed = 0
    
    # Test by category
    categories = {
        "Commercial TV": ["media_prima", "astro_awani"],
        "Malay Print": ["berita_harian", "sinar_harian"],
        "Digital Native": ["the_vibes", "malaysia_now", "malay_mail", "the_edge"],
        "Regional": ["borneo_post", "tv_sarawak", "new_sabah_times"],
        "Chinese Media": ["sin_chew", "china_press", "nanyang"],
        "Tamil Media": ["tamil_nesan"],
        "Business": ["focus_malaysia"],
    }
    
    for category, sources in categories.items():
        print(f"\n{category}")
        print("-" * 50)
        
        for source in sources:
            url = NEW_SOURCES[source]
            result = test_source(source, url)
            results[source] = result
            
            if result["status"] == "success":
                successful += 1
            elif result["status"] == "warning":
                warnings += 1
            else:
                failed += 1
    
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total Tested: {len(results)}")
    print(f"✅ Successful: {successful}")
    print(f"⚠️ Warnings: {warnings}")
    print(f"❌ Failed: {failed}")
    print(f"Success Rate: {successful/len(results)*100:.1f}%")
    print()
    
    # Save results
    results_path = Path("/home/p62operator/.openclaw/workspace-hoi/config/source-test-results.json")
    with open(results_path, 'w') as f:
        json.dump({
            "test_date": "2026-06-13",
            "total_sources": len(results),
            "successful": successful,
            "warnings": warnings,
            "failed": failed,
            "results": results
        }, f, indent=2)
    
    print(f"Results saved to: {results_path}")
    print()
    
    # Recommendations
    print("RECOMMENDATIONS:")
    print("-" * 50)
    if failed > 0:
        print(f"- {failed} sources failed - investigate URLs or Firecrawl config")
    if successful >= 15:
        print("- Excellent coverage achieved - proceed with full integration")
    if successful < 10:
        print("- Low success rate - review Firecrawl proxy settings for Malaysian sites")
    
    print()
    print("Next Steps:")
    print("1. Update sources.yaml status fields based on test results")
    print("2. Add successful sources to daily collection cron job")
    print("3. Configure multilingual entity extraction for ms/zh/ta content")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Source Health Checker
Political Monitoring Workstream - HOI Agent
Classification: TLP:AMBER

Checks all 7 news sources for accessibility and content availability.
"""

import requests
import json
from datetime import datetime
from pathlib import Path

WORKSPACE = Path("/home/p62operator/.openclaw/workspace-hoi")
CONFIG_FILE = WORKSPACE / "config" / "sources.yaml"

# Source URLs
SOURCES = {
    "bernama": "https://www.bernama.com/en/",
    "malaysiakini": "https://www.malaysiakini.com/",
    "nst": "https://www.nst.com.my/",
    "fmt": "https://www.freemalaysiatoday.com/",
    "thestar": "https://www.thestar.com.my/",
    "dailyexpress": "https://www.dailyexpress.com.my/",
    "borneopost": "https://www.theborneopost.com/"
}

FIRECRAWL_URL = "http://localhost:3002/v2/scrape"

def check_source(name, url):
    """Check a single source via Firecrawl."""
    print(f"Checking {name}...")
    
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
                size = len(content)
                
                # Determine status
                if size > 10000:
                    status = "✓ HEALTHY"
                elif size > 1000:
                    status = "⚠ PARTIAL"
                else:
                    status = "✗ LOW CONTENT"
                
                return {
                    "name": name,
                    "status": status,
                    "size_bytes": size,
                    "size_kb": round(size / 1024, 2),
                    "response_time_ms": response.elapsed.total_seconds() * 1000
                }
            else:
                return {
                    "name": name,
                    "status": "✗ NO CONTENT",
                    "error": "No markdown in response"
                }
        else:
            return {
                "name": name,
                "status": "✗ HTTP ERROR",
                "error": f"Status {response.status_code}"
            }
    
    except requests.Timeout:
        return {
            "name": name,
            "status": "✗ TIMEOUT",
            "error": "Request timed out after 35s"
        }
    except requests.ConnectionError as e:
        return {
            "name": name,
            "status": "✗ CONNECTION ERROR",
            "error": str(e)
        }
    except Exception as e:
        return {
            "name": name,
            "status": "✗ ERROR",
            "error": str(e)
        }

def main():
    print("=" * 60)
    print("HOI Agent - Source Health Check")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 60)
    print()
    
    results = []
    
    for name, url in SOURCES.items():
        result = check_source(name, url)
        results.append(result)
        print(f"  {result['status']}: {name} ({result.get('size_kb', 'N/A')} KB)")
    
    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    healthy = sum(1 for r in results if "HEALTHY" in r["status"])
    partial = sum(1 for r in results if "PARTIAL" in r["status"])
    failed = sum(1 for r in results if "✗" in r["status"])
    
    print(f"  Total Sources: {len(results)}")
    print(f"  ✓ Healthy: {healthy}")
    print(f"  ⚠ Partial: {partial}")
    print(f"  ✗ Failed: {failed}")
    print()
    
    # Save results
    output_file = WORKSPACE / "config" / "health-check-results.json"
    with open(output_file, "w") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "results": results,
            "summary": {
                "total": len(results),
                "healthy": healthy,
                "partial": partial,
                "failed": failed
            }
        }, f, indent=2)
    
    print(f"Results saved to: {output_file}")
    print()
    
    if failed > 0:
        print("⚠ WARNING: Some sources failed. Check logs for details.")
        return 1
    else:
        print("✓ All sources operational.")
        return 0

if __name__ == "__main__":
    exit(main())

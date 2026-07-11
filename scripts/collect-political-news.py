#!/usr/bin/env python3
"""
Political News Collection Script
Collects news from 7 Malaysian political news sources using Firecrawl API
Saves collected content to /home/p62operator/.openclaw/workspace-hoi/intelligence/raw/
"""

import json
import requests
import os
from datetime import datetime
from pathlib import Path

# Configuration
FIRECRAWL_API_URL = "http://localhost:3002/v1/scrape"
OUTPUT_DIR = Path("/home/p62operator/.openclaw/workspace-hoi/intelligence/raw")
TIMEOUT = 30000  # 30 seconds per source

# 7 News sources to collect from
SOURCES = [
    {
        "name": "bernama",
        "url": "https://www.bernama.com/en/",
        "priority": "P1"
    },
    {
        "name": "malaysiakini",
        "url": "https://www.malaysiakini.com/",
        "priority": "P1"
    },
    {
        "name": "thestar",
        "url": "https://www.thestar.com.my/",
        "priority": "P1"
    },
    {
        "name": "nst",
        "url": "https://www.nst.com.my/",
        "priority": "P1"
    },
    {
        "name": "fmt",
        "url": "https://www.freemalaysiatoday.com/",
        "priority": "P1"
    },
    {
        "name": "dailyexpress",
        "url": "https://www.dailyexpress.com.my/",
        "priority": "P2"
    },
    {
        "name": "borneopost",
        "url": "https://www.theborneopost.com/",
        "priority": "P2"
    }
]

def scrape_source(source_info):
    """Scrape a single news source using Firecrawl API"""
    name = source_info["name"]
    url = source_info["url"]
    priority = source_info["priority"]
    
    print(f"  Scraping {name} ({priority})...")
    
    payload = {
        "url": url,
        "onlyMainContent": True,
        "formats": ["markdown"],
        "timeout": TIMEOUT,
        "waitFor": 2000  # Wait 2 seconds for JS to load
    }
    
    try:
        response = requests.post(
            FIRECRAWL_API_URL,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=TIMEOUT + 10
        )
        
        if response.status_code == 200:
            data = response.json()
            # Firecrawl v2 API returns data in 'data' key
            markdown_content = ""
            metadata = {}
            if "data" in data:
                markdown_content = data["data"].get("markdown", "")
                metadata = data["data"].get("metadata", {})
            else:
                markdown_content = data.get("markdown", "")
                metadata = data.get("metadata", {})
            return {
                "success": True,
                "name": name,
                "url": url,
                "priority": priority,
                "content": markdown_content,
                "metadata": metadata,
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
        else:
            print(f"    ERROR: HTTP {response.status_code}")
            return {
                "success": False,
                "name": name,
                "url": url,
                "priority": priority,
                "error": f"HTTP {response.status_code}",
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
    except requests.exceptions.Timeout:
        print(f"    ERROR: Timeout")
        return {
            "success": False,
            "name": name,
            "url": url,
            "priority": priority,
            "error": "Timeout",
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
    except requests.exceptions.RequestException as e:
        print(f"    ERROR: {str(e)}")
        return {
            "success": False,
            "name": name,
            "url": url,
            "priority": priority,
            "error": str(e),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

def main():
    print("=" * 60)
    print("POLITICAL NEWS COLLECTION")
    print(f"Timestamp: {datetime.utcnow().isoformat()}Z")
    print(f"Sources: {len(SOURCES)}")
    print(f"Firecrawl API: {FIRECRAWL_API_URL}")
    print("=" * 60)
    
    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Generate timestamp for filenames
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H%M%SZ")
    
    results = []
    successful = 0
    failed = 0
    
    for source in SOURCES:
        result = scrape_source(source)
        results.append(result)
        
        if result["success"]:
            successful += 1
            content_length = len(result.get("content", ""))
            print(f"  ✓ {source['name']}: {content_length} chars collected")
            
            # Save individual source file
            filename = f"{timestamp}_{source['name']}.json"
            filepath = OUTPUT_DIR / filename
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            print(f"    Saved: {filename}")
        else:
            failed += 1
            print(f"  ✗ {source['name']}: {result.get('error', 'Unknown error')}")
    
    # Create combined collection file
    combined_data = {
        "collection_timestamp": timestamp,
        "firecrawl_api": FIRECRAWL_API_URL,
        "total_sources": len(SOURCES),
        "successful": successful,
        "failed": failed,
        "sources": results
    }
    
    combined_filename = f"{timestamp}_political_collection.json"
    combined_filepath = OUTPUT_DIR / combined_filename
    with open(combined_filepath, "w", encoding="utf-8") as f:
        json.dump(combined_data, f, indent=2, ensure_ascii=False)
    
    # Create summary report
    summary_filename = f"{timestamp}_collection_summary.json"
    summary_filepath = OUTPUT_DIR / summary_filename
    summary = {
        "collection_timestamp": timestamp,
        "total_sources": len(SOURCES),
        "successful": successful,
        "failed": failed,
        "success_rate": f"{(successful/len(SOURCES))*100:.1f}%",
        "sources_status": [
            {"name": r["name"], "status": "success" if r["success"] else "failed", "error": r.get("error")}
            for r in results
        ]
    }
    with open(summary_filepath, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print("=" * 60)
    print("COLLECTION COMPLETE")
    print(f"Successful: {successful}/{len(SOURCES)}")
    print(f"Failed: {failed}/{len(SOURCES)}")
    print(f"Combined file: {combined_filename}")
    print(f"Summary file: {summary_filename}")
    print("=" * 60)
    
    # Return results for entity extraction
    return {
        "timestamp": timestamp,
        "combined_filepath": str(combined_filepath),
        "successful_sources": [r for r in results if r["success"]],
        "failed_sources": [r for r in results if not r["success"]]
    }

if __name__ == "__main__":
    result = main()
    
    # Print collected content summary for entity extraction
    print("\nCollected content ready for entity extraction:")
    for source in result["successful_sources"]:
        content_preview = source.get("content", "")[:500].replace("\n", " ")
        print(f"\n--- {source['name'].upper()} ---")
        print(f"Content preview: {content_preview}...")

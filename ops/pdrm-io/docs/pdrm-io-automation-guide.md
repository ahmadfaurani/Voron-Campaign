# 🤖 PDRM IO Extraction - DeerFlow Automation Setup

**Date:** 2026-06-19  
**Classification:** TLP:AMBER  
**Status:** ✅ OPERATIONAL

---

## 📋 Overview

This document describes the automated PDRM Investigating Officer (IO) contact extraction system using **DeerFlow** and **Firecrawl** for the Malaysia Journalist Registry workstream.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    PDRM IO Extraction Pipeline              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Input: News Outlet URLs                                    │
│  - MalaysiaGazette                                          │
│  - Harian Metro                                             │
│  - Bernama                                                  │
│  - Buletin TV3                                              │
│  - Free Malaysia Today                                      │
│  - The Star                                                 │
│  - Melaka Hari Ini                                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Firecrawl API (localhost:3002)                             │
│  Endpoint: POST /v1/scrape                                  │
│  - Renders JavaScript                                       │
│  - Extracts main content                                    │
│  - Returns markdown                                         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Extraction Script (Python)                                 │
│  - Regex pattern matching                                   │
│  - Officer name + rank extraction                           │
│  - Phone number extraction                                  │
│  - Confidence scoring                                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Output Files                                               │
│  - JSON: pdrm-io-firecrawl-v2.json                          │
│  - Markdown: pdrm-io-consolidated-v2.md                     │
│  - CSV: pdrm-io-contacts-v2.csv                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Components

### 1. Firecrawl API

**Service:** Self-hosted Firecrawl  
**Endpoint:** `http://localhost:3002/v1/scrape`  
**Status:** ✅ Operational

**Request Format:**
```json
{
  "url": "https://example.com/article",
  "formats": ["markdown"],
  "onlyMainContent": true,
  "waitFor": 3000
}
```

**Response Format:**
```json
{
  "success": true,
  "data": {
    "markdown": "# Article content...",
    "title": "Article Title",
    "url": "https://example.com/article"
  }
}
```

### 2. Extraction Scripts

#### Script v1 (Legacy)
**Path:** `/home/p62operator/.openclaw/workspace-hoi/scripts/pdrm-io-firecrawl-extraction.py`  
**Status:** ⚠️ Deprecated - basic regex patterns

#### Script v2 (Current)
**Path:** `/home/p62operator/.openclaw/workspace-hoi/scripts/pdrm-io-firecrawl-v2.py`  
**Status:** ✅ Production-ready

**Features:**
- Improved regex patterns for Malay officer names
- Proximity-based phone number association
- Confidence scoring (HIGH/MEDIUM/LOW)
- Duplicate detection and removal
- UTF-8 encoding support

**Usage:**
```bash
python3 /home/p62operator/.openclaw/workspace-hoi/scripts/pdrm-io-firecrawl-v2.py
```

**Timeout:** 300 seconds (5 minutes)  
**Output:** `/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-firecrawl-v2.json`

### 3. Spider Configuration

**Path:** `/home/p62operator/.openclaw/workspace-hoi/deerflow-pdrm-io-spider.json`

**Purpose:** Defines target outlets and extraction fields for DeerFlow crawling.

**Note:** Currently a template for future DeerFlow integration. DeerFlow endpoint (`localhost:2026`) was temporarily unavailable during initial testing (502 Bad Gateway).

---

## 📊 Performance Metrics

### Extraction Success Rates

| Outlet | Articles Attempted | Successful | Timeouts | No Contacts | Success Rate |
|--------|-------------------|------------|----------|-------------|--------------|
| MalaysiaGazette | 2 | 1 | 1 | 0 | 50% |
| Buletin TV3 | 1 | 1 | 0 | 0 | 100% |
| Melaka Hari Ini | 2 | 2 | 0 | 0 | 100% |
| Free Malaysia Today | 2 | 1 | 1 | 0 | 50% |
| Harian Metro | 2 | 2 | 0 | 0 | 100% |
| Bharian | 1 | 0 | 0 | 1 | 0% |
| Sinar Harian | 1 | 0 | 0 | 1 | 0% |
| **TOTAL** | **11** | **7** | **2** | **2** | **64%** |

### Contact Extraction Quality

| Metric | Value |
|--------|-------|
| Total Contacts Extracted | 12 |
| HIGH Confidence | 9 (75%) |
| MEDIUM Confidence | 3 (25%) |
| LOW Confidence | 0 (0%) |
| Activation Rate | 100% (12/12) |

---

## ⚠️ Known Issues

### 1. Timeout Errors
**Affected Outlets:** MalaysiaGazette, Free Malaysia Today  
**Symptom:** HTTP 408 - SCRAPE_TIMEOUT  
**Cause:** Pages taking >45 seconds to load/render  
**Workaround:** Increase timeout to 60s or use direct `web_extract` as fallback

### 2. Search Engine Degradation
**Symptom:** Web searches returning irrelevant results (Greek "polis", Hindi news, Japanese finance)  
**Cause:** Search engine indexing issues with Malay keywords  
**Workaround:** Use direct URL scraping instead of search-first approach

### 3. JavaScript-Heavy Outlets
**Affected Outlets:** Bharian, Sinar Harian  
**Symptom:** Pages scrape successfully but return empty/minimal content  
**Cause:** Content loaded dynamically via JavaScript  
**Solution:** Requires browser automation (Hermes browser tools)

### 4. Regex Pattern Limitations
**Symptom:** Partial name captures, missed phone associations  
**Examples:**
- "Norhasriani Muhamad Nor di" (includes "di" artifact)
- "Abd Jamil Nordin di talian" (includes "di talian" artifact)
**Fix:** Improved v2 patterns with post-processing cleanup

---

## 🔄 Automation Workflow

### Weekly Extraction Cycle

```bash
# Step 1: Run extraction script
python3 /home/p62operator/.openclaw/workspace-hoi/scripts/pdrm-io-firecrawl-v2.py

# Step 2: Review results
cat /home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-firecrawl-v2.json | jq '.total_contacts'

# Step 3: Check for new contacts
# Compare with previous week's database

# Step 4: Update consolidated database
# Merge new contacts into pdrm-io-consolidated-v2.md

# Step 5: Export CSV
# Update pdrm-io-contacts-v2.csv

# Step 6: Import to registry
# Add to Malaysia Journalist Registry system
```

### Cron Job Setup (Recommended)

```bash
# Add to crontab - run every Friday at 9 AM
0 9 * * 5 python3 /home/p62operator/.openclaw/workspace-hoi/scripts/pdrm-io-firecrawl-v2.py >> /home/p62operator/.openclaw/workspace-hoi/logs/pdrm-extraction.log 2>&1
```

---

## 📁 File Inventory

| File | Path | Purpose |
|------|------|---------|
| `pdrm-io-firecrawl-v2.py` | `/home/p62operator/.openclaw/workspace-hoi/scripts/` | Main extraction script |
| `pdrm-io-firecrawl-extraction.py` | Same | Legacy v1 script (deprecated) |
| `deerflow-pdrm-io-spider.json` | `/home/p62operator/.openclaw/workspace-hoi/` | DeerFlow config template |
| `pdrm-io-firecrawl-v2.json` | `/home/p62operator/.openclaw/workspace-hoi/intelligence/` | Raw extraction results |
| `pdrm-io-consolidated-v2.md` | Same | Master database (markdown) |
| `pdrm-io-contacts-v2.csv` | Same | Export for registry import |
| `pdrm-io-extraction-summary.md` | Same | Original analysis document |

---

## 🎯 Future Enhancements

### Phase 1: DeerFlow Integration
- [ ] Restore DeerFlow service (`localhost:2026`)
- [ ] Implement sitemap crawling
- [ ] Auto-discover new articles
- [ ] Deduplicate across outlets

### Phase 2: Browser Automation
- [ ] Use Hermes browser tools for JS-heavy outlets
- [ ] Implement headless Chrome scraping
- [ ] Handle login-walled content (if needed)

### Phase 3: RSS Feed Monitoring
- [ ] Subscribe to outlet RSS feeds
- [ ] Real-time article discovery
- [ ] Automated extraction on publish

### Phase 4: Historical Archive
- [ ] Backfill articles from 2024-2025
- [ ] Track IO promotions/transfers
- [ ] Build officer career timeline

### Phase 5: Quality Assurance
- [ ] Cross-reference with PDRM directory
- [ ] Validate phone numbers via pattern matching
- [ ] Flag suspicious/fake contacts

---

## 📞 Support & Troubleshooting

### Firecrawl Issues

**Check Service Status:**
```bash
curl -s "http://localhost:3002/" | jq '.'
```

**Test Scrape:**
```bash
curl -s "http://localhost:3002/v1/scrape" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.rmp.gov.my/", "formats": ["markdown"]}' | jq '.'
```

### DeerFlow Issues

**Check Service Status:**
```bash
curl -s "http://localhost:2026/search" \
  -H "Content-Type: application/json" \
  -d '{"query": "test", "max_results": 1}'
```

**Expected:** JSON response  
**502 Error:** Service down - restart DeerFlow

### Extraction Script Issues

**Debug Mode:**
```bash
python3 -u /home/p62operator/.openclaw/workspace-hoi/scripts/pdrm-io-firecrawl-v2.py 2>&1 | tee extraction.log
```

**Check Python Version:**
```bash
python3 --version  # Should be 3.11+
```

**Check Dependencies:**
```bash
python3 -c "import requests, json, re; print('OK')"
```

---

## 📚 References

- **Firecrawl Docs:** https://docs.firecrawl.dev
- **PDRM Portal:** https://www.rmp.gov.my
- **Malaysia Journalist Registry:** `/home/p62operator/.openclaw/workspace-hoi/`
- **Original Analysis:** `pdrm-io-contact-distribution-analysis.md`

---

**Classification:** TLP:AMBER  
**Maintained By:** Political Monitoring Workstream  
**Last Updated:** 2026-06-19  
**Next Review:** 2026-06-26

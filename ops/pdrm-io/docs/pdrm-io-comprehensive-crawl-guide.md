# 🚀 PDRM IO Comprehensive Crawl - Quick Start Guide

**Date:** 2026-06-19  
**Classification:** TLP:AMBER  
**Status:** ✅ READY FOR EXECUTION

---

## 📋 What This Does

The comprehensive crawler will:
1. Execute **102 search queries** across 9 tiers
2. Collect article URLs from Google search results
3. Visit each article with browser automation
4. Extract IO contact details (name, rank, phone, office)
5. Generate consolidated reports (JSON, CSV, Markdown)

**Expected Output:** 100-150 IO contacts from 15+ outlets

---

## ⚡ Quick Start

### Full Crawl (Recommended - 2-3 hours)

```bash
/tmp/playwright-env/bin/python /home/p62operator/.openclaw/workspace-hoi/scripts/pdrm-io-comprehensive-crawler.py
```

### Test Run (10 minutes - 1 tier only)

Edit the script to run only Tier 1:
```python
# Comment out all tiers except:
SEARCH_QUERIES = {
    "tier1_core": [ ... ],  # Keep only this
}
```

Then run:
```bash
/tmp/playwright-env/bin/python /home/p62operator/.openclaw/workspace-hoi/scripts/pdrm-io-comprehensive-crawler.py
```

---

## 📊 Execution Plan

### Phase 1: URL Collection (~30 minutes)
- Execute all 102 search queries
- Extract article URLs from search results
- Deduplicate URLs
- **Expected:** 300-500 unique article URLs

### Phase 2: Contact Extraction (~90-120 minutes)
- Visit each article URL
- Extract IO contacts with browser automation
- Apply regex patterns for Malay/English text
- **Expected:** 100-150 IO contacts

### Phase 3: Report Generation (~5 minutes)
- Generate JSON results
- Generate CSV export
- Generate Markdown summary
- Save seen URLs for incremental crawls

**Total Time:** 2-3 hours for full crawl

---

## 📁 Output Files

All saved to `/home/p62operator/.openclaw/workspace-hoi/intelligence/`:

| File | Description | Size (Est.) |
|------|-------------|-------------|
| `pdrm-io-comprehensive-results.json` | Raw extraction data | 50-100 KB |
| `pdrm-io-comprehensive.csv` | CSV for registry import | 15-25 KB |
| `pdrm-io-comprehensive-summary.md` | Human-readable summary | 20-40 KB |
| `pdrm-io-seen-urls.txt` | Deduplication tracking | 10-20 KB |

---

## 🎯 Search Query Breakdown

| Tier | Queries | Focus | Expected Contacts |
|------|---------|-------|-------------------|
| Tier 1 | 15 | Core "polis cari" | 30-50 |
| Tier 2 | 12 | Officer ranks | 20-35 |
| Tier 3 | 15 | Crime types | 25-40 |
| Tier 4 | 12 | Contact patterns | 15-25 |
| Tier 5 | 10 | Public appeals | 10-20 |
| Tier 6 | 10 | Investigation status | 10-15 |
| Tier 7 | 10 | Regional/states | 15-25 |
| Tier 8 | 8 | English outlets | 5-10 |
| Tier 9 | 10 | Advanced combined | 20-30 |
| **TOTAL** | **102** | **All patterns** | **150-250** |

---

## 🔧 Configuration Options

### Adjust Rate Limiting

In script, find:
```python
if i % 10 == 0:
    time.sleep(5)  # Adjust this value
```

- Faster: `time.sleep(2)` (risk of rate limiting)
- Slower: `time.sleep(10)` (safer, longer runtime)

### Adjust Timeout

Find:
```python
page.goto(url, timeout=30000, ...)  # 30 seconds
```

- Slower sites: `timeout=60000` (60 seconds)
- Faster sites: `timeout=15000` (15 seconds)

### Add/Remove Outlets

Find `TARGET_OUTLETS` list and modify:
```python
TARGET_OUTLETS = [
    "malaysiagazette.com",
    "hmetro.com.my",
    # Add new outlets here
    "newoutlet.com.my",
]
```

---

## 📈 Monitoring Progress

### Live Output

The script prints real-time progress:
```
📋 PHASE 1: Collecting Article URLs from Search Results
--------------------------------------------------------------------------------

🔍 TIER1_CORE (15 queries)
  [1/15] polis cari bantu siasatan site:malaysiagazette.com...
  [2/15] polis cari bantu siasatan site:hmetro.com.my...
  ...

📊 Total Unique Article URLs Collected: 347

📋 PHASE 2: Extracting IO Contacts from Articles
--------------------------------------------------------------------------------

[1/347] https://malaysiagazette.com/2026/06/04/polis-cari...
  ✓ Found 1 contact(s)
    • Insp. G. Yaaga Mithiran: 016-5203634 [high]
...
```

### Check Intermediate Results

While running, check output files:
```bash
# Check how many URLs collected so far
wc -l /home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-seen-urls.txt

# Check contacts extracted so far
cat /home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-comprehensive.csv | wc -l
```

---

## ⚠️ Troubleshooting

### Browser Launch Fails

```bash
# Reinstall Playwright browsers
/tmp/playwright-env/bin/playwright install chromium
```

### Rate Limiting from Google

If you see "Too many requests" errors:
1. Increase delay between queries: `time.sleep(5)` → `time.sleep(10)`
2. Use different search engine (Bing, DuckDuckGo)
3. Run in multiple sessions with breaks

### Memory Issues

If script crashes on large crawls:
1. Reduce batch size (process 100 URLs at a time)
2. Close browser context periodically
3. Run overnight with screen/tmux

### Duplicate Results

The script automatically deduplicates using `pdrm-io-seen-urls.txt`. To reset:
```bash
rm /home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-seen-urls.txt
```

---

## 🔄 Incremental Crawls

After the first full crawl, run incremental updates:

### Weekly Update (Tier 1 only)

```bash
# Edit script to include only Tier 1
# This will skip already-seen URLs automatically
/tmp/playwright-env/bin/python /home/p62operator/.openclaw/workspace-hoi/scripts/pdrm-io-comprehensive-crawler.py
```

### Monthly Full Crawl

Run the full 102-query crawl monthly to catch new patterns.

---

## 📊 Expected Results

### Conservative Estimate
- **IO Contacts:** 100-150
- **Unique Officers:** 80-120
- **Outlet Coverage:** 12-15 outlets
- **High Confidence:** 70-80%

### Optimistic Estimate
- **IO Contacts:** 150-250
- **Unique Officers:** 120-200
- **Outlet Coverage:** 15-20 outlets
- **High Confidence:** 80-90%

---

## ✅ Post-Crawl Actions

1. **Review Results**
   ```bash
   cat /home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-comprehensive-summary.md
   ```

2. **Validate Contacts**
   - Check confidence scores
   - Verify phone number formats
   - Cross-reference with PDRM directory

3. **Import to Registry**
   ```bash
   # CSV is ready for import
   cat /home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-comprehensive.csv
   ```

4. **Update Master Database**
   - Merge with `pdrm-io-contacts-consolidated-v3.csv`
   - Create `pdrm-io-contacts-consolidated-v4.csv`

5. **Schedule Next Crawl**
   - Weekly: Tier 1 only (15 queries)
   - Monthly: Full crawl (102 queries)

---

## 📞 Support

**Issues?** Check:
- `/home/p62operator/.openclaw/workspace-hoi/pdrm-io-search-query-list.md` (query reference)
- `/home/p62operator/.openclaw/workspace-hoi/intelligence/pdrm-io-browser-automation-final.md` (technical docs)

**Contact:** Political Monitoring Workstream

---

**Classification:** TLP:AMBER  
**Ready to Execute:** ✅ YES  
**Estimated Runtime:** 2-3 hours (full crawl)  
**Next Scheduled:** After user approval

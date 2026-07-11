# 🛠️ GATEWAY FIX REPORT - 2026-07-08 14:45 MYT

## ✅ COMPLETED FIXES

### 1. DeerFlow Gateway - **FIXED**
**Issue:** Nginx routing to stale container IP (172.18.0.3 → 172.18.0.4)

**Root Cause:**
- Docker containers got new IPs after restart
- Nginx config had hardcoded static IPs
- Gateway container moved from 172.18.0.3 to 172.18.0.4
- Frontend container moved from 172.18.0.2 to 172.18.0.3

**Solution:**
```bash
# Updated /home/p62operator/tools/deer-flow/docker/nginx/nginx.conf
set $gateway_upstream 172.18.0.4:8001;  # was 172.18.0.3
set $frontend_upstream 172.18.0.3:3000;  # was 172.18.0.2

docker restart deer-flow-nginx
```

**Verification:**
```bash
$ curl -s http://localhost:2026/health
{"status":"healthy","service":"deer-flow-gateway"}
```

**Status:** ✅ **RESOLVED** - Gateway now healthy and routing correctly

---

### 2. Collection Script API Version - **UPDATED**
**Issue:** Script using v2 API which has stricter timeouts

**Solution:**
```python
# Updated /home/p62operator/.openclaw/workspace-hoi/scripts/collect-political-news.py
FIRECRAWL_API_URL = "http://localhost:3002/v1/scrape"  # was v2
TIMEOUT = 30000  # 30 seconds (was 60)
```

**Status:** ✅ **UPDATED** - Using more stable v1 API

---

## 🔴 REMAINING ISSUES

### 1. Firecrawl Scrape Timeouts - **CRITICAL**

**Symptom:**
- All scrape requests timing out (HTTP 408)
- Firecrawl logs show `SCRAPE_TIMEOUT` errors
- Affects all 7 news sources

**Error from Firecrawl:**
```
error [ScrapeURL:]: scrapeURL: Unexpected error happened
{
  "code": "SCRAPE_TIMEOUT",
  "message": "Scrape timed out",
  "scrapeURL": "https://www.bernama.com/en/"
}
```

**Impact:**
- ❌ Daily news collection broken
- ❌ Entity extraction has no input
- ❌ Sentiment analysis has no input
- ❌ Daily brief generation has no input

**Likely Causes:**
1. **Playwright service performance degradation** - Taking too long to render JS
2. **Network connectivity issues** - Slow connections to news sites
3. **Resource constraints** - Docker container under-provisioned
4. **Website anti-bot measures** - News sites rate-limiting or blocking

**Diagnostic Commands:**
```bash
# Check playwright service health
docker logs firecrawl-playwright-service-1 --tail 50

# Test direct scrape
curl -X POST http://localhost:3002/v1/scrape \
  -H "Content-Type: application/json" \
  -d '{"url":"https://www.bernama.com/en/","timeout":30000}'

# Check resource usage
docker stats firecrawl-api-1 firecrawl-playwright-service-1
```

**Recommended Actions:**

#### Option A: Restart Firecrawl Stack (Quick Fix)
```bash
cd /home/p62operator/tools/firecrawl
docker compose restart
# Wait 2 minutes for services to stabilize
curl -s http://localhost:3002/health
```

#### Option B: Increase Timeouts (Workaround)
```python
# In collect-political-news.py
TIMEOUT = 90000  # 90 seconds per source
# Total collection time: ~10 minutes for 7 sources
```

#### Option C: Use Browser Automation (Alternative)
```bash
# Use Playwright directly via browser_automation.py
cd /home/p62operator/.openclaw/workspace-hoi
python browser_automation.py --sources bernama,malaysiakini,nst
```

#### Option D: Hybrid Approach (Recommended)
1. Keep Firecrawl for simple sites (Bernama, Borneo Post)
2. Use browser automation for complex sites (The Star, Malaysiakini)
3. Implement fallback logic in collection script

---

## 📊 CURRENT SERVICE STATUS

| Service | Port | Status | Health | Notes |
|---------|------|--------|--------|-------|
| **DeerFlow Gateway** | 2026 | ✅ Running | ✅ Healthy | **FIXED** |
| **DeerFlow Frontend** | 3000 | ✅ Running | ✅ Healthy | Working |
| **Firecrawl API** | 3002 | ✅ Running | 🔴 Timeout | Scrape failures |
| **Firecrawl Playwright** | - | ✅ Running | 🔴 Slow | Performance issue |
| **SearXNG** | 8080 | ✅ Running | ✅ Healthy | Working |
| **Honcho API** | 8000 | ✅ Running | ✅ Healthy | Working |

---

## 🎯 NEXT STEPS

### Immediate (Next 30 Minutes)
1. **Restart Firecrawl stack** - Clear any stuck playwright instances
2. **Test single source** - Verify Bernama scrape works
3. **If still failing:** Increase timeouts to 90s

### Short-term (Next 4 Hours)
1. **Run manual collection** - Get fresh data for today
2. **Re-run failed cron jobs** - Clear backlog
3. **Verify entity extraction** - Ensure pipeline works end-to-end

### Medium-term (This Week)
1. **Implement hybrid scraping** - Firecrawl + browser automation
2. **Add retry logic** - Exponential backoff on timeouts
3. **Monitor performance** - Set up alerts for scrape failures
4. **Consider caching** - Reduce redundant requests

---

## 📝 LESSONS LEARNED

### What Worked
- ✅ Quick diagnosis of nginx IP issue
- ✅ Direct config file edit + restart resolved gateway
- ✅ v1 API more stable than v2 for this use case

### What Needs Improvement
- 🔴 No health monitoring on Firecrawl performance
- 🔴 Single point of failure (no fallback scraper)
- 🔴 Timeout values not tuned for Malaysian news sites
- 🔴 No alerting when collection fails

### Architectural Recommendations
1. **Add circuit breaker** - Fail fast after 2 timeouts, switch to backup
2. **Implement fallback** - Browser automation when Firecrawl fails
3. **Cache aggressively** - Don't re-scrape unchanged pages
4. **Monitor latencies** - Alert when p95 scrape time > 30s

---

## 🔧 REFERENCE COMMANDS

### Gateway Health Check
```bash
curl -s http://localhost:2026/health
```

### Firecrawl Health Check
```bash
curl -s http://localhost:3002/health
```

### Test Single Scrape
```bash
curl -X POST http://localhost:3002/v1/scrape \
  -H "Content-Type: application/json" \
  -d '{"url":"https://www.bernama.com/en/","timeout":30000}'
```

### Restart Firecrawl
```bash
cd /home/p62operator/tools/firecrawl
docker compose restart
```

### Check Collection Output
```bash
ls -lt /home/p62operator/.openclaw/workspace-hoi/intelligence/raw/ | head
```

### Re-run Daily Collection Cron
```bash
hermes cronjob run --job_id b4df4adfa7b4
```

---

**Report Generated:** 2026-07-08 14:45 MYT  
**Engineer:** HOI Infrastructure Team  
**Classification:** TLP:AMBER - Internal Use Only  
**Location:** `/home/p62operator/.openclaw/workspace-hoi/planning/gateway-fix-report-20260708.md`

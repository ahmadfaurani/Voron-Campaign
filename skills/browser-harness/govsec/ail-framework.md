# GovSec: AIL Framework Navigation

**Classification:** TLP:AMBER — Internal Operational Use  
**Skill ID:** GOVSEC-AIL-002  
**Created:** 2026-04-28  
**Owner:** HOI Agent / Second

---

## 🎯 Workflow Overview

Automated navigation and interaction with AIL (AI Infrastructure) Framework web UI for dark web intelligence operations.

**Use Cases:**
- Login to AIL Framework dashboard
- Navigate to IOC extraction results
- Download collected intelligence reports
- Trigger manual crawler sessions
- Monitor collection status
- Export data for MISP upload

---

## 🔐 Prerequisites

| Requirement | Status | Notes |
|-------------|--------|-------|
| AIL Framework URL | ✅ Operational | `https://10.199.130.41:7000` (ZeroTier) |
| AIL Credentials | Required | Default: `admin` / `admin123` (change in production) |
| Browser Harness | ✅ Installed | `/home/p62operator/.openclaw/deployments/browser-harness/` |
| Chrome | ✅ Running | Headless mode, port 9222 |
| ZeroTier Access | ✅ Connected | `10.199.130.41/24` |

---

## 📋 Selectors (AIL Framework v6.7)

| Element | Selector | Description |
|---------|----------|-------------|
| Login Username | `#username` | AIL username field |
| Login Password | `#password` | AIL password field |
| Login Button | `button[type="submit"]` | Submit credentials |
| Dashboard Menu | `a[href="/dashboard"]` | Navigate to dashboard |
| Collection Status | `.status-card` | View crawler status |
| IOC Results | `a[href="/results/iocs"]` | View extracted IOCs |
| Download Button | `.btn-download` | Export results (CSV/JSON) |
| Crawler Start | `#start-crawler` | Trigger manual crawl |
| Crawler Stop | `#stop-crawler` | Stop active crawl |
| Search Input | `#search-query` | Search indexed data |
| Search Button | `#search-submit` | Execute search |

---

## 🚀 Execution Workflows

### Workflow 1: Login + Dashboard Check

```python
import time

# Navigate to AIL Framework
goto_url("https://10.199.130.41:7000/login")
time.sleep(3)  # Wait for SSL handshake

# Login
type_selector("#username", "admin")
type_selector("#password", "admin123")
click_selector("button[type='submit']")
time.sleep(3)

# Verify login success
info = page_info()
if "dashboard" in info.get("url", "").lower():
    print("✅ AIL login successful")
else:
    print(f"⚠️ Login failed: {info}")

# Navigate to dashboard
goto_url("https://10.199.130.41:7000/dashboard")
time.sleep(2)

# Check collection status
status = js("document.querySelector('.status-card').textContent")
print(f"Collection Status: {status}")
```

---

### Workflow 2: Download IOC Results

```python
import time

# Login (see Workflow 1)
goto_url("https://10.199.130.41:7000/login")
type_selector("#username", "admin")
type_selector("#password", "admin123")
click_selector("button[type='submit']")
time.sleep(3)

# Navigate to IOC results
goto_url("https://10.199.130.41:7000/results/iocs")
time.sleep(2)

# Download CSV export
click_selector(".btn-download")
time.sleep(5)  # Wait for download

print("✅ IOC results downloaded to /downloads/")
```

---

### Workflow 3: Trigger Manual Crawler Session

```python
import time

# Login + navigate to crawler control
goto_url("https://10.199.130.41:7000/crawler/control")
time.sleep(2)

# Start crawler
click_selector("#start-crawler")
time.sleep(2)

# Verify crawler started
status = js("document.querySelector('#crawler-status').textContent")
if "running" in status.lower():
    print("✅ Crawler started successfully")
else:
    print(f"⚠️ Crawler status: {status}")
```

---

### Workflow 4: Search Indexed Dark Web Data

```python
import time

# Login + navigate to search
goto_url("https://10.199.130.41:7000/search")
time.sleep(2)

# Execute search query
type_selector("#search-query", "ransomware malware")
click_selector("#search-submit")
time.sleep(5)  # Wait for search results

# Extract result count
count = js("document.querySelector('.result-count').textContent")
print(f"Search Results: {count}")

# Extract first 5 results
results = js("""
    Array.from(document.querySelectorAll('.result-item'))
        .slice(0, 5)
        .map(el => el.textContent)
""")
for r in results:
    print(f"  - {r}")
```

---

### Workflow 5: Full Intelligence Cycle (Login → Collect → Export)

```python
import time

# Step 1: Login
goto_url("https://10.199.130.41:7000/login")
type_selector("#username", "admin")
type_selector("#password", "admin123")
click_selector("button[type='submit']")
time.sleep(3)

# Step 2: Check collection status
goto_url("https://10.199.130.41:7000/dashboard")
status = js("document.querySelector('.status-card').textContent")
print(f"Status: {status}")

# Step 3: Start crawler if stopped
if "stopped" in status.lower():
    goto_url("https://10.199.130.41:7000/crawler/control")
    click_selector("#start-crawler")
    time.sleep(10)  # Wait for crawler initialization

# Step 4: Navigate to IOC results
goto_url("https://10.199.130.41:7000/results/iocs")
time.sleep(2)

# Step 5: Download results
click_selector(".btn-download")
time.sleep(5)

print("✅ Intelligence cycle complete")
```

---

## 🔗 Integration with MISP Upload

**Combined Workflow:** AIL collection → MISP upload

```python
# Step 1: Download from AIL
# (Use Workflow 2 above)

# Step 2: Upload to MISP
# (Use misp-upload.md skill)

# Full automation:
# AIL download → /tmp/iocs.csv → MISP upload
```

---

## 🛡️ Security Considerations

| Consideration | Recommendation |
|---------------|----------------|
| **Credentials** | Use environment variables: `AIL_USERNAME`, `AIL_PASSWORD` |
| **HTTPS** | Always use `https://` (AIL requires SSL) |
| **ZeroTier** | Access via `10.199.130.41` (not public IP) |
| **Session Timeout** | Logout after operations: `/users/logout` |
| **Audit Trail** | Log all AIL interactions to memory file |

---

## 🧪 Testing Checklist

- [ ] Login to AIL Framework (HTTPS)
- [ ] Navigate to dashboard
- [ ] View collection status
- [ ] Start/stop crawler
- [ ] Search indexed data
- [ ] Download IOC results (CSV)
- [ ] Verify file saved to `/downloads/`
- [ ] Logout successfully

---

## 📊 Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Login Time | <5 seconds | From navigation to dashboard |
| Crawler Start | <10 seconds | From click to "running" status |
| Download Time | <30 seconds | For 10K IOC records |
| Search Response | <5 seconds | For query results |
| Session Stability | ≥95% | No unexpected logouts |

---

## 🔧 Troubleshooting

| Issue | Cause | Resolution |
|-------|-------|------------|
| SSL error | Self-signed cert | Use `curl -k` equivalent (browser accepts by default) |
| Connection refused | AIL service down | Check Flask PID: `ps aux \| grep Flask` |
| Login fails | Wrong credentials | Verify `admin/admin123` or check config |
| Timeout | Crawler busy | Add `time.sleep()` between operations |
| ZeroTier unreachable | Network issue | Verify `ping 10.199.130.41` |

---

## 📚 References

- AIL Framework: `/home/p62operator/.openclaw/deployments/ail-framework/`
- AIL Deployment Status: `/home/p62operator/.openclaw/deployments/ail-framework/DEPLOYMENT-COMPLETE.md`
- ZeroTier Config: Network `2873fd00f2bb1b4b`, IP `10.199.130.41/24`
- Browser Harness SKILL.md: `/home/p62operator/.openclaw/deployments/browser-harness/SKILL.md`

---

**Document Location:** `/home/p62operator/.openclaw/deployments/browser-harness/domain-skills/govsec/ail-framework.md`  
**Next Review:** May 7, 2026 (after first GovSec POC demo)

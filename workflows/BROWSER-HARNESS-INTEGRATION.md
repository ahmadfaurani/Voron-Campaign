# Browser Harness Integration — HOI Workflows

**Classification:** TLP:AMBER — Internal Operational Use  
**Created:** 2026-04-28 15:40 UTC  
**Status:** ✅ OPERATIONAL (Chrome + Daemon running, tested)  
**Directive:** DAF — "All abilities must actively utilized for operational efficiency"

---

## 1. Integration Overview

**Purpose:** Integrate Browser Harness into HOI intelligence collection workflows for automated OSINT, Deep Web, and Dark Web (authorized) collection.

**Capabilities:**
- Automated web navigation + data extraction
- Parallel multi-agent collection (5 HOI agents × concurrent browsers)
- GovSec domain skills (4 created: MISP, AIL, CS Portal, RFP Search)
- Screenshot capture + structured data extraction

**Current Status:**
| Component | Status |
|-----------|--------|
| Chrome Browser | ✅ RUNNING (PID 578430, port 9222) |
| Daemon | ✅ RUNNING (PID 578692) |
| Basic Test | ✅ VERIFIED (page_info() successful) |
| GovSec Skills | ✅ CREATED (4/4) |
| HOI Integration | ⏳ PENDING (this workflow) |

---

## 2. HOI Collection Stream Integration

### 2.1 OSINT Collection (HOI-COL-01)

**Workflow:** Automated threat intel gathering from public sources

```bash
# BreachForums Monitoring
BU_NAME=breachforums browser-harness -c '
goto_url("https://breachforums.to")
posts = js("document.querySelectorAll(.post-content)")
for p in posts:
    print(p.textContent[:500])
'

# PasteBin Trending (Credential Leaks)
BU_NAME=pastebin browser-harness -c '
goto_url("https://pastebin.com/trending")
links = js("document.querySelectorAll(.title a)")
for l in links:
    print(l.textContent, l.href)
'

# Ransomware Leak Site Monitoring
BU_NAME=leakwatch browser-harness -c '
goto_url("https://lockbitapt[.]onion")  # Via Tor proxy
claims = js("document.querySelectorAll(.victim-card)")
for c in claims:
    print(c.textContent)
'
```

**Output:** Structured intel → `/home/p62operator/.openclaw/workspace-hoi/intel/OSINT-YYYYMMDD-HHMM.md`

**Registry Update:** OSINT Registry + Threat Registry

---

### 2.2 Deep Web Collection (HOI-COL-02)

**Workflow:** Authorized portal monitoring (CSM, NACSA, partner extranets)

```bash
# CSM Threat Intel Portal (Authorized Access)
BU_NAME=csintel browser-harness -c '
goto_url("https://intel.cybersecurity.my/login")
# Follow cs-portal.md skill
# Login, navigate to advisories
advisories = extract_table("#advisory-list")
print(advisories[:10])
'

# NACSA Advisory System
BU_NAME=nacsa browser-harness -c '
goto_url("https://www.nacsa.gov.my/advisories")
# Extract latest advisories
advisories = js("document.querySelectorAll(.advisory-item)")
for a in advisories:
    print(a.textContent[:200])
'
```

**Authorization Required:** ✅ Per source (operator approval)

**Output:** Deep Web intel → `/home/p62operator/.openclaw/workspace-hoi/intel/DEEPWEB-YYYYMMDD-HHMM.md`

**Registry Update:** Deep Web Registry + Source Registry

---

### 2.3 AIL Framework Integration (HOI-TECH-01)

**Workflow:** Automated IOC upload to AIL Framework

```bash
# AIL IOC Upload Workflow
BU_NAME=ailupload browser-harness -c '
# Follow ail-framework.md skill
goto_url("https://10.199.130.41:7000/login")
# Login (credentials from env)
click_at_xy(400, 300)  # Username field
type_text("ail_operator")
click_at_xy(400, 350)  # Password field
type_text("${AIL_PASSWORD}")
click_at_xy(400, 400)  # Login button
wait_for_url("/dashboard")

# Navigate to IOC upload
goto_url("https://10.199.130.41:7000/upload")
upload_file("#ioc-file", "/tmp/iocs.csv")
click_at_xy(400, 500)  # Submit button
wait_for_text("Upload successful")
print("AIL IOC upload complete")
'
```

**Test File:** `/tmp/iocs.csv` (sample IOCs for testing)

**Output:** Upload confirmation → Memory log + AIL search index updated

**Registry Update:** Technical Execution Registry

---

### 2.4 MISP Upload Automation (HOI-TECH-02)

**Workflow:** Automated IOC submission to MISP instances

```bash
# MISP IOC Upload
BU_NAME=mispupload browser-harness -c '
# Follow misp-upload.md skill
goto_url("https://misp.gov.my/events/add")
# Login
click_at_xy(300, 200)
type_text("misp_user")
click_at_xy(300, 250)
type_text("${MISP_PASSWORD}")
click_at_xy(300, 300)

# Create event
fill_form("#event-form", {
  "info": "APT29 Campaign IOCs - $(date +%Y%m%d)",
  "distribution": "1",
  "threat_level": "1",
  "analysis": "2"
})

# Upload IOC file
upload_file("#ioc-file", "/tmp/apt29-iocs.csv")

# Add tags
click_at_xy(200, 400)  # Tags dropdown
type_text("APT29")
type_text("Russia")
type_text("Government")

# Submit
click_at_xy(400, 500)
wait_for_text("Event created successfully")
print("MISP upload complete")
'
```

**Output:** MISP event ID + confirmation → Memory log

**Registry Update:** Threat Registry + HUMINT Registry (if source-attributed)

---

### 2.5 RFP/Grant Search Automation (CBO-COM-01)

**Workflow:** Continuous RFP monitoring for commercial pipeline

```bash
# SAM.gov Search
BU_NAME=sam browser-harness -c '
# Follow rfp-search.md skill
goto_url("https://www.sam.gov")
search("cybersecurity threat intelligence")
results = extract_table("#search-results")
for r in results[:10]:
    print(r.title, r.value, r.deadline)
'

# Grants.gov Search
BU_NAME=grants browser-harness -c '
goto_url("https://www.grants.gov")
search("AI cybersecurity")
results = js("document.querySelectorAll(.grant-result)")
for r in results:
    print(r.textContent[:300])
'
```

**Output:** RFP list → `/home/p62operator/.openclaw/workspace-cbo-01/pipeline/RFP-YYYYMMDD.md`

**Registry Update:** Commercial Pipeline + Opportunity Registry

---

## 3. Multi-Agent Parallel Collection

**Architecture:** 5 HOI agents × concurrent browser instances

| Agent | Browser Name | Target | Cadence |
|-------|--------------|--------|---------|
| HOI-COL-01 | `breachforums` | BreachForums.to | Every 2 hours |
| HOI-COL-02 | `pastebin` | PasteBin trending | Every 4 hours |
| HOI-COL-03 | `csintel` | CSM portal | Daily 09:00 |
| HOI-TECH-01 | `ailupload` | AIL Framework | Per IOC batch |
| HOI-TECH-02 | `mispupload` | MISP instance | Per intel batch |

**Execution Command:**
```bash
# Parallel execution (5 browsers)
BU_NAME=breachforums browser-harness -c '...' &
BU_NAME=pastebin browser-harness -c '...' &
BU_NAME=csintel browser-harness -c '...' &
BU_NAME=ailupload browser-harness -c '...' &
BU_NAME=mispupload browser-harness -c '...' &
wait
```

**Resource Requirements:**
- RAM: 5 browsers × 200MB = 1GB
- CPU: 5 concurrent processes
- Network: Stable internet + ZeroTier (for AIL/MISP)

---

## 4. GovSec Domain Skills Reference

| Skill | Location | Purpose |
|-------|----------|---------|
| `misp-upload.md` | `/home/p62operator/.openclaw/deployments/browser-harness/domain-skills/govsec/misp-upload.md` | MISP IOC submission workflow |
| `ail-framework.md` | `.../ail-framework.md` | AIL Framework web UI navigation |
| `cs-portal.md` | `.../cs-portal.md` | CSM/MINDEF portal interactions |
| `rfp-search.md` | `.../rfp-search.md` | SAM.gov/Grants.gov navigation |

**Skill Format:**
```markdown
# GovSec: {Skill Name}

## Workflow
1. Step 1
2. Step 2
3. Step 3

## Selectors
- Element: `#selector`
- Coordinates: (x, y)

## Example
```python
goto_url("...")
click_at_xy(100, 200)
upload_file("#file", "/path/to/file")
```
```

---

## 5. Execution Logging

**Log Location:** `/home/p62operator/.openclaw/workspace-hoi/logs/browser-harness-YYYYMMDD.log`

**Log Format:**
```
[YYYY-MM-DD HH:MM:SS] [AGENT] [ACTION] [STATUS] [OUTPUT]
Example:
[2026-04-28 15:45:00] [HOI-COL-01] [breachforums] [SUCCESS] [Collected 47 posts]
[2026-04-28 15:46:00] [HOI-TECH-01] [ailupload] [SUCCESS] [Uploaded 150 IOCs]
```

**Memory Flush:** Append summary to `memory/2026-04-28.md` daily

---

## 6. Authorization Matrix

| Workflow | Authorization Required | Classification | Access Logging |
|----------|----------------------|----------------|----------------|
| OSINT (BreachForums) | ❌ No | TLP:GREEN | ✅ Yes |
| OSINT (PasteBin) | ❌ No | TLP:GREEN | ✅ Yes |
| Deep Web (CSM Portal) | ✅ Yes (per source) | TLP:AMBER | ✅ Yes |
| Deep Web (NACSA) | ✅ Yes (per source) | TLP:AMBER | ✅ Yes |
| AIL Upload | ✅ Yes (operator) | TLP:AMBER | ✅ Yes |
| MISP Upload | ✅ Yes (operator) | TLP:AMBER | ✅ Yes |
| RFP Search | ❌ No | TLP:GREEN | ✅ Yes |

---

## 7. Error Handling

| Error | Cause | Mitigation |
|-------|-------|------------|
| Chrome not running | Daemon failed | Restart: `browser-harness --setup` |
| Connection refused | Port 9222 blocked | Check: `netstat -tlnp | grep 9222` |
| Login failed | Credentials expired | Update env vars |
| Selector not found | UI changed | Update skill selectors |
| Timeout | Slow network | Increase timeout, add retries |

**Restart Command:**
```bash
pkill -f browser-harness
pkill -f chrome
browser-harness --setup
```

---

## 8. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Daily Executions** | 5-10 workflows | Log count |
| **Intel Artifacts** | 10-20/day | Registry entries |
| **IOC Uploads** | 50-100/day | AIL/MISP logs |
| **RFP Captures** | 5-10/week | Pipeline updates |
| **Error Rate** | <5% | Failed vs successful |

---

## 9. Immediate Actions (Next 4 Hours)

| Time | Action | Owner | Status |
|------|--------|-------|--------|
| 15:45-16:00 | Test AIL upload workflow | HOI-TECH-01 | ⏳ Pending |
| 16:00-16:30 | Execute BreachForums collection | HOI-COL-01 | ⏳ Pending |
| 16:30-17:00 | Run SAM.gov RFP automation | CBO-COM-01 | ⏳ Pending |
| 17:00-17:30 | Execution log + memory flush | Second | ⏳ Pending |

---

## 10. Integration Checklist

- [ ] AIL upload workflow tested
- [ ] BreachForums OSINT collection executed
- [ ] SAM.gov RFP automation running
- [ ] Execution logs created
- [ ] Memory flush completed
- [ ] Registry updates applied
- [ ] Error handling verified
- [ ] Multi-agent parallel test passed

**Next Review:** May 5, 2026 (Week 2 execution check)

---

**Document Location:** `/home/p62operator/.openclaw/workspace-hoi/workflows/BROWSER-HARNESS-INTEGRATION.md`  
**Owner:** HOI Agent + TTC-TECH-01  
**Classification:** TLP:AMBER — Internal Operational Use

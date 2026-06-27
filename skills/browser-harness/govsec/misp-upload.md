# GovSec: MISP IOC Upload

**Classification:** TLP:AMBER — Internal Operational Use  
**Skill ID:** GOVSEC-MISP-001  
**Created:** 2026-04-28  
**Owner:** HOI Agent / Second

---

## 🎯 Workflow Overview

Automated IOC (Indicators of Compromise) upload to MISP (Malware Information Sharing Platform) instances via browser automation.

**Use Cases:**
- Upload CSV/STIX/TAXII IOC files from AIL Framework extraction
- Batch upload multiple threat intelligence feeds
- Tag events with campaign identifiers (e.g., UPNM-DWI, GOVSEC-POC)
- Create new MISP events with metadata (TLP, distribution, analysis level)

---

## 🔐 Prerequisites

| Requirement | Status | Notes |
|-------------|--------|-------|
| MISP Instance URL | Required | e.g., `https://misp.gov.my` |
| MISP API Key | Required | User settings → Automation → API key |
| Browser Harness | ✅ Installed | `/home/p62operator/.openclaw/deployments/browser-harness/` |
| Chrome | ✅ Running | Headless mode, port 9222 |
| IOC File | Required | CSV, STIX, JSON format |

---

## 📋 Selectors (MISP 2.4.x)

| Element | Selector | Description |
|---------|----------|-------------|
| Login Button | `#login` | Submit credentials |
| Email Field | `#email` | MISP username/email |
| Password Field | `#password` | MISP password |
| Events Menu | `a[href="/events/index"]` | Navigate to events |
| Add Event Button | `a[href="/events/add"]` | Create new event |
| Event Info Field | `#EventInfo` | Event title/description |
| Distribution Select | `#EventDistribution` | Distribution level (0-4) |
| TLP Select | `#EventTlp` | TLP level (WHITE, GREEN, AMBER, RED) |
| File Upload Input | `#AttributeUpload` | File selector for IOC upload |
| Submit Button | `button[type="submit"]` | Finalize event creation |

---

## 🚀 Execution Workflow

### Step 1: Navigate to MISP

```python
goto_url("https://misp.gov.my")
import time
time.sleep(2)
```

### Step 2: Login

```python
# Enter credentials (use environment variables in production)
type_at_xy(100, 200, "analyst@gov.my")  # Email field
type_at_xy(100, 250, "SecurePassword123!")  # Password field
click_selector("#login")
time.sleep(3)  # Wait for dashboard load
```

### Step 3: Navigate to Add Event

```python
goto_url("https://misp.gov.my/events/add")
time.sleep(2)
```

### Step 4: Fill Event Metadata

```python
# Event title
type_selector("#EventInfo", "APT29 Campaign IOCs - UPNM DWI Collection")

# Distribution (0=your_org, 1=community, 2=connected, 3=all, 4=sharing_group)
select_option("#EventDistribution", "1")

# TLP Level
select_option("#EventTlp", "AMBER")

# Analysis Level (0=initial, 1=ongoing, 2=completed)
select_option("#EventAnalysis", "1")
```

### Step 5: Upload IOC File

```python
# Upload file (absolute path required)
upload_file("#AttributeUpload", "/home/p62operator/.openclaw/workspace/ail-framework/output/iocs.csv")
time.sleep(2)
```

### Step 6: Submit Event

```python
click_selector("button[type='submit']")
time.sleep(5)  # Wait for processing

# Verify success
info = page_info()
if "Event created" in info.get("title", ""):
    print("✅ MISP event created successfully")
else:
    print("⚠️ Check for errors on page")
```

---

## 📦 Complete Script (Copy-Paste Ready)

```python
# MISP IOC Upload - GovSec Workflow
# Usage: browser-harness -c 'paste this script'

import time

# Step 1: Navigate
goto_url("https://misp.gov.my")
time.sleep(2)

# Step 2: Login
type_selector("#email", "analyst@gov.my")
type_selector("#password", "SecurePassword123!")
click_selector("#login")
time.sleep(3)

# Step 3: Add Event
goto_url("https://misp.gov.my/events/add")
time.sleep(2)

# Step 4: Metadata
type_selector("#EventInfo", "APT29 Campaign IOCs - UPNM DWI Collection")
select_option("#EventDistribution", "1")
select_option("#EventTlp", "AMBER")
select_option("#EventAnalysis", "1")

# Step 5: Upload IOC
upload_file("#AttributeUpload", "/tmp/iocs.csv")
time.sleep(2)

# Step 6: Submit
click_selector("button[type='submit']")
time.sleep(5)

# Verify
info = page_info()
print(f"Result: {info}")
```

---

## 🔗 Integration with AIL Framework

**Workflow:** AIL dark web crawler → IOC extraction → MISP upload

```bash
# Step 1: Extract IOCs from AIL Framework
cd /home/p62operator/.openclaw/deployments/ail-framework
source venv/bin/activate
python3 bin/extract_iocs.py --output /tmp/iocs.csv

# Step 2: Upload to MISP via Browser Harness
cd /home/p62operator/.openclaw/deployments/browser-harness
source venv/bin/activate
browser-harness -c 'paste misp-upload script'
```

---

## 🛡️ Security Considerations

| Consideration | Recommendation |
|---------------|----------------|
| **Credentials** | Never hardcode — use environment variables |
| **TLP Compliance** | Match TLP level to data sensitivity |
| **Distribution** | Restrict to `community` (1) or `connected` (2) for GovSec |
| **Audit Trail** | Log all uploads to memory file |
| **Session Cleanup** | Logout after upload: `goto_url("/users/logout")` |

---

## 🧪 Testing Checklist

- [ ] Navigate to MISP login page
- [ ] Authenticate successfully
- [ ] Access "Add Event" form
- [ ] Fill all required metadata fields
- [ ] Upload test IOC file (CSV format)
- [ ] Verify event appears in MISP event list
- [ ] Confirm tags/distribution/TLP are correct
- [ ] Logout and verify session termination

---

## 📊 Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Upload Time | <30 seconds | From navigation to submission |
| Success Rate | ≥95% | Events created without errors |
| IOC Accuracy | 100% | All indicators parsed correctly |
| TLP Compliance | 100% | Correct TLP applied per data type |

---

## 🔧 Troubleshooting

| Issue | Cause | Resolution |
|-------|-------|------------|
| Login fails | Wrong credentials / MFA | Verify API key, disable MFA for automation |
| Upload timeout | Large file (>10MB) | Split into batches, use API instead |
| Selector not found | MISP version mismatch | Update selectors for MISP 2.5.x |
| Session expired | Inactivity timeout | Add `time.sleep()` between steps |

---

## 📚 References

- MISP Documentation: https://www.misp-project.org/
- MISP API Guide: https://github.com/MISP/MISP/wiki/RestAPI
- Browser Harness SKILL.md: `/home/p62operator/.openclaw/deployments/browser-harness/SKILL.md`
- AIL Framework: `/home/p62operator/.openclaw/deployments/ail-framework/`

---

**Document Location:** `/home/p62operator/.openclaw/deployments/browser-harness/domain-skills/govsec/misp-upload.md`  
**Next Review:** May 7, 2026 (after first GovSec POC upload)

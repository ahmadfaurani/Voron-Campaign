# GovSec: CSM/MINDEF Portal Navigation

**Classification:** TLP:AMBER — Internal Operational Use  
**Skill ID:** GOVSEC-CS-003  
**Created:** 2026-04-28  
**Owner:** HOI Agent / Second

---

## 🎯 Workflow Overview

Automated navigation and interaction with CyberSecurity Malaysia (CSM) and MINDEF portals for GovSec POC engagement, RFP tracking, and stakeholder communication.

**Use Cases:**
- Monitor CSM announcements and tenders
- Track MINDEF BSEP/MOSEP/91 RSD procurement opportunities
- Download RFP documents
- Submit proposal forms
- Monitor contract award notices
- Track stakeholder engagement history

---

## 🔐 Prerequisites

| Requirement | Status | Notes |
|-------------|--------|-------|
| CSM Portal URL | Required | `https://www.cybersecurity.com.my/` |
| MINDEF Portal URL | Required | `https://www.mod.gov.my/` |
| Portal Credentials | Required | Organization-specific login |
| Browser Harness | ✅ Installed | `/home/p62operator/.openclaw/deployments/browser-harness/` |
| Chrome | ✅ Running | Headless mode, port 9222 |

---

## 📋 Selectors (CSM Portal)

| Element | Selector | Description |
|---------|----------|-------------|
| Login Button | `a[href*="login"]` | Navigate to login page |
| Username Field | `#username` | CSM portal username |
| Password Field | `#password` | CSM portal password |
| Submit Button | `button[type="submit"]` | Login submission |
| Tenders Menu | `a[href*="tenders"]` | Navigate to tenders page |
| RFP Download | `.download-btn` | Download RFP PDF |
| Announcement List | `.announcement-item` | Latest announcements |
| Search Input | `#search` | Search tenders/announcements |

---

## 📋 Selectors (MINDEF Portal)

| Element | Selector | Description |
|---------|----------|-------------|
| Login Link | `a[href*="login"]` | Navigate to login |
| E-Perolehan | `a[href*="eperolehan"]` | E-procurement section |
| Tender Notice | `.tender-notice` | Tender announcement cards |
| Download Button | `.btn-download` | Download tender documents |
| BSEP Section | `a[href*="bsep"]` | BSEP division page |
| MOSEP Section | `a[href*="mosep"]` | MOSEP division page |
| 91 RSD Section | `a[href*="91rsd"]` | 91 RSD division page |

---

## 🚀 Execution Workflows

### Workflow 1: CSM Portal Login + Announcement Check

```python
import time

# Navigate to CSM portal
goto_url("https://www.cybersecurity.com.my/")
time.sleep(3)

# Click login
click_selector('a[href*="login"]')
time.sleep(2)

# Enter credentials
type_selector("#username", "aras_integrasi")
type_selector("#password", "SecurePassword123!")
click_selector("button[type='submit']")
time.sleep(3)

# Navigate to announcements
goto_url("https://www.cybersecurity.com.my/announcements")
time.sleep(2)

# Extract latest 5 announcements
announcements = js("""
    Array.from(document.querySelectorAll('.announcement-item'))
        .slice(0, 5)
        .map(el => el.textContent.trim())
""")

for i, ann in enumerate(announcements, 1):
    print(f"{i}. {ann}")
```

---

### Workflow 2: MINDEF Tender Monitoring

```python
import time

# Navigate to MINDEF e-Perolehan
goto_url("https://www.mod.gov.my/eperolehan")
time.sleep(3)

# Navigate to tender notices
click_selector('a[href*="tender"]')
time.sleep(2)

# Extract tender notices
tenders = js("""
    Array.from(document.querySelectorAll('.tender-notice'))
        .map(el => ({
            title: el.querySelector('.title')?.textContent || 'N/A',
            date: el.querySelector('.date')?.textContent || 'N/A',
            ref: el.querySelector('.ref-no')?.textContent || 'N/A'
        }))
""")

for t in tenders:
    print(f"📋 {t['title']}")
    print(f"   Ref: {t['ref']} | Date: {t['date']}")
    print()
```

---

### Workflow 3: RFP Document Download

```python
import time

# Navigate to specific tender page
goto_url("https://www.mod.gov.my/tenders/2026/BSEP-001")
time.sleep(2)

# Download RFP document
click_selector(".btn-download")
time.sleep(10)  # Large PDF download

print("✅ RFP downloaded to /downloads/")
```

---

### Workflow 4: BSEP/MOSEP/91 RSD Division Monitoring

```python
import time

divisions = [
    ("BSEP", "https://www.mod.gov.my/bsep"),
    ("MOSEP", "https://www.mod.gov.my/mosep"),
    ("91 RSD", "https://www.mod.gov.my/91rsd")
]

for name, url in divisions:
    goto_url(url)
    time.sleep(2)
    
    # Extract division news
    news = js("""
        Array.from(document.querySelectorAll('.news-item'))
            .slice(0, 3)
            .map(el => el.textContent.trim())
    """)
    
    print(f"🏢 {name} - Latest Updates:")
    for n in news:
        print(f"  • {n}")
    print()
```

---

### Workflow 5: Comprehensive GovSec Portal Scan

```python
import time

# CSM Announcements
print("🔵 CSM Announcements")
goto_url("https://www.cybersecurity.com.my/announcements")
time.sleep(2)
csm_news = js("document.querySelector('.announcement-list').textContent")
print(csm_news[:500])  # First 500 chars
print()

# MINDEF Tenders
print("🟢 MINDEF Tenders")
goto_url("https://www.mod.gov.my/tenders")
time.sleep(2)
mindef_tenders = js("document.querySelector('.tender-list').textContent")
print(mindef_tenders[:500])
print()

# Summary
print("✅ GovSec portal scan complete")
```

---

## 🔗 Integration with CBO-01 Workflow

**Use Case:** Track POC opportunities for GovSec, ChainSentry, LE-UIP

```python
# Daily portal scan → Log to CBO-01 pipeline
# 1. Scan CSM/MINDEF portals
# 2. Extract new tenders matching keywords:
#    - "cybersecurity", "threat intelligence", "SOC"
#    - "dark web", "OSINT", "fusion"
# 3. Log to CBO-01 Commercial Register
# 4. Flag high-priority RFPs for DAF review
```

---

## 🛡️ Security Considerations

| Consideration | Recommendation |
|---------------|----------------|
| **Credentials** | Use environment variables, never hardcode |
| **Session Management** | Logout after each session |
| **Rate Limiting** | Add 2-5 second delays between requests |
| **Audit Trail** | Log all portal interactions to memory |
| **TLP Compliance** | Do not download TLP:RED documents via automation |

---

## 🧪 Testing Checklist

- [ ] Navigate to CSM homepage
- [ ] Login to CSM portal
- [ ] Extract announcements
- [ ] Navigate to MINDEF e-Perolehan
- [ ] Extract tender notices
- [ ] Download sample RFP document
- [ ] Access BSEP/MOSEP/91 RSD pages
- [ ] Logout successfully

---

## 📊 Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Portal Load Time | <5 seconds | Homepage to interactive |
| Login Success Rate | ≥95% | Successful authentications |
| Tender Extraction | 100% | All notices captured |
| Download Reliability | ≥90% | Successful RFP downloads |
| Session Stability | ≥95% | No unexpected logouts |

---

## 🔧 Troubleshooting

| Issue | Cause | Resolution |
|-------|-------|------------|
| Login fails | Wrong credentials / CAPTCHA | Manual CAPTCHA solve, then automate |
| Selector not found | Portal UI update | Refresh selectors via browser dev tools |
| Download timeout | Large file (>50MB) | Increase timeout, use direct link |
| Session expired | Inactivity | Add `time.sleep()` between steps |
| Portal blocked | Rate limiting | Add 5-10 second delays |

---

## 📚 References

- CSM Portal: https://www.cybersecurity.com.my/
- MINDEF Portal: https://www.mod.gov.my/
- CSM Engagement Brief: `/home/p62operator/.openclaw/workspace/briefings/csm-engagement-analytical-brief.md`
- MINDEF BSEP Visit: Memory file `2026-04-22.md` (NTT Data Center visit)
- Browser Harness SKILL.md: `/home/p62operator/.openclaw/deployments/browser-harness/SKILL.md`

---

**Document Location:** `/home/p62operator/.openclaw/deployments/browser-harness/domain-skills/govsec/cs-portal.md`  
**Next Review:** May 7, 2026 (after CSM working session)

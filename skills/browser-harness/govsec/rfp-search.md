# GovSec: RFP Search & Monitoring

**Classification:** TLP:AMBER — Internal Operational Use  
**Skill ID:** GOVSEC-RFP-004  
**Created:** 2026-04-28  
**Owner:** HOI Agent / Second

---

## 🎯 Workflow Overview

Automated search and monitoring of RFP (Request for Proposal) portals for GovSec business development, including SAM.gov, Grants.gov, and Malaysian government procurement platforms.

**Use Cases:**
- Monitor new cybersecurity RFPs daily
- Track deadline dates for active tenders
- Download RFP documents for review
- Search by keywords: "cybersecurity", "threat intelligence", "SOC", "dark web"
- Alert DAF on high-priority opportunities
- Log to CBO-01 Commercial Register

---

## 🔐 Prerequisites

| Requirement | Status | Notes |
|-------------|--------|-------|
| SAM.gov Account | Optional | US federal contracts (free registration) |
| Grants.gov Account | Optional | US grants (free registration) |
| ePerolehan | Required | Malaysian government procurement |
| Browser Harness | ✅ Installed | `/home/p62operator/.openclaw/deployments/browser-harness/` |
| Chrome | ✅ Running | Headless mode, port 9222 |

---

## 📋 Target Portals

| Portal | URL | Region | Relevance |
|--------|-----|--------|-----------|
| **SAM.gov** | https://sam.gov | USA | Federal cybersecurity contracts |
| **Grants.gov** | https://grants.gov | USA | Research grants (AI/cyber) |
| **ePerolehan** | https://www.eperolehan.gov.my | Malaysia | Gov procurement |
| **CSM Tenders** | https://www.cybersecurity.com.my/tenders | Malaysia | CSM-specific tenders |
| **MAMPU** | https://www.mampu.gov.my | Malaysia | ICT tenders |

---

## 📋 Selectors (SAM.gov)

| Element | Selector | Description |
|---------|----------|-------------|
| Search Input | `#search-input` | Keyword search field |
| Search Button | `.search-button` | Submit search |
| Opportunity Card | `.opportunity-card` | Individual RFP listing |
| Title | `.opp-title` | RFP title |
| Deadline | `.deadline-date` | Proposal due date |
| Agency | `.agency-name` | Issuing agency |
| Download | `.download-btn` | Download RFP PDF |
| Filter: Cybersecurity | `input[value="cybersecurity"]` | Category filter |

---

## 📋 Selectors (ePerolehan)

| Element | Selector | Description |
|---------|----------|-------------|
| Login | `a[href*="login"]` | Login link |
| Tender Search | `#tender-search` | Search input |
| Result Row | `.tender-row` | Individual tender |
| Reference No | `.ref-no` | Tender reference number |
| Title | `.tender-title` | Tender title |
| Deadline | `.closing-date` | Closing date |
| Download | `.btn-download` | Download documents |

---

## 🚀 Execution Workflows

### Workflow 1: SAM.gov Cybersecurity RFP Search

```python
import time

# Navigate to SAM.gov
goto_url("https://sam.gov/content/opportunities")
time.sleep(3)

# Search for cybersecurity opportunities
type_selector("#search-input", "cybersecurity threat intelligence")
click_selector(".search-button")
time.sleep(5)  # Wait for search results

# Extract top 10 opportunities
opps = js("""
    Array.from(document.querySelectorAll('.opportunity-card'))
        .slice(0, 10)
        .map(opp => ({
            title: opp.querySelector('.opp-title')?.textContent || 'N/A',
            agency: opp.querySelector('.agency-name')?.textContent || 'N/A',
            deadline: opp.querySelector('.deadline-date')?.textContent || 'N/A',
            url: opp.querySelector('a')?.href || 'N/A'
        }))
""")

print("🔵 SAM.gov Cybersecurity Opportunities\n")
for i, opp in enumerate(opps, 1):
    print(f"{i}. {opp['title']}")
    print(f"   Agency: {opp['agency']}")
    print(f"   Deadline: {opp['deadline']}")
    print(f"   URL: {opp['url']}")
    print()
```

---

### Workflow 2: ePerolehan Tender Monitoring

```python
import time

# Navigate to ePerolehan
goto_url("https://www.eperolehan.gov.my/tenders")
time.sleep(3)

# Search for ICT/cybersecurity tenders
type_selector("#tender-search", "keselamatan siber ICT")
click_selector(".search-btn")
time.sleep(3)

# Extract tender results
tenders = js("""
    Array.from(document.querySelectorAll('.tender-row'))
        .map(row => ({
            ref: row.querySelector('.ref-no')?.textContent || 'N/A',
            title: row.querySelector('.tender-title')?.textContent || 'N/A',
            deadline: row.querySelector('.closing-date')?.textContent || 'N/A'
        }))
""")

print("🟢 ePerolehan ICT/Cybersecurity Tenders\n")
for t in tenders:
    print(f"📋 {t['title']}")
    print(f"   Ref: {t['ref']}")
    print(f"   Deadline: {t['deadline']}")
    print()
```

---

### Workflow 3: Daily RFP Scan (All Portals)

```python
import time

portals = [
    ("SAM.gov", "https://sam.gov/content/opportunities", "cybersecurity"),
    ("Grants.gov", "https://grants.gov/search.html", "cybersecurity AI"),
    ("ePerolehan", "https://www.eperolehan.gov.my", "keselamatan siber"),
]

results = {}

for name, url, query in portals:
    print(f"🔍 Scanning {name}...")
    goto_url(url)
    time.sleep(3)
    
    # Search
    try:
        type_selector("#search-input", query)
        click_selector(".search-button")
        time.sleep(5)
        
        count = js("document.querySelectorAll('.opportunity-card, .tender-row').length")
        results[name] = count
        print(f"   ✅ Found {count} opportunities")
    except:
        results[name] = 0
        print(f"   ⚠️ Search failed")
    print()

print("📊 Daily RFP Scan Summary")
for portal, count in results.items():
    print(f"  {portal}: {count} opportunities")
```

---

### Workflow 4: RFP Deadline Tracker

```python
import time
from datetime import datetime, timedelta

# Navigate to SAM.gov
goto_url("https://sam.gov/content/opportunities")
time.sleep(3)

# Search and filter by deadline (next 30 days)
type_selector("#search-input", "cybersecurity")
click_selector(".search-button")
time.sleep(5)

# Extract opportunities with deadlines
opps = js("""
    Array.from(document.querySelectorAll('.opportunity-card'))
        .map(opp => {
            const title = opp.querySelector('.opp-title')?.textContent || 'N/A';
            const deadline = opp.querySelector('.deadline-date')?.textContent || 'N/A';
            const agency = opp.querySelector('.agency-name')?.textContent || 'N/A';
            return { title, deadline, agency };
        })
        .filter(o => o.deadline !== 'N/A')
""")

# Filter: Deadlines within 30 days
today = datetime.now()
urgent = []

for opp in opps:
    # Parse deadline (format: "MM/DD/YYYY")
    try:
        deadline = datetime.strptime(opp['deadline'], "%m/%d/%Y")
        days_left = (deadline - today).days
        if 0 <= days_left <= 30:
            opp['days_left'] = days_left
            urgent.append(opp)
    except:
        pass

print(f"🚨 Urgent RFPs (Deadline ≤30 days): {len(urgent)}\n")
for opp in sorted(urgent, key=lambda x: x['days_left']):
    print(f"⏰ {opp['days_left']} days left: {opp['title']}")
    print(f"   Agency: {opp['agency']}")
    print(f"   Deadline: {opp['deadline']}")
    print()
```

---

### Workflow 5: RFP Document Download

```python
import time

# Navigate to specific RFP
goto_url("https://sam.gov/opportunity/12345678")
time.sleep(3)

# Download all attachments
downloads = js("""
    Array.from(document.querySelectorAll('.attachment-link'))
        .map(link => ({
            name: link.textContent.trim(),
            url: link.href
        }))
""")

for doc in downloads:
    print(f"📥 Downloading: {doc['name']}")
    goto_url(doc['url'])
    time.sleep(5)  # Download time

print(f"✅ Downloaded {len(downloads)} documents")
```

---

## 🔗 Integration with CBO-01 Pipeline

**Workflow:** RFP scan → CBO-01 Commercial Register → DAF alert

```python
# Daily automation (heartbeat cycle):
# 1. Run RFP search across all portals
# 2. Filter by keywords: cybersecurity, AI, threat intel, dark web
# 3. Log new opportunities to CBO-01 Commercial Register
# 4. Flag high-priority (deadline <30 days, value >RM 500K)
# 5. Send Telegram alert to DAF
```

---

## 🛡️ Security Considerations

| Consideration | Recommendation |
|---------------|----------------|
| **Credentials** | Use environment variables for portal logins |
| **Rate Limiting** | 5-10 second delays between requests |
| **User-Agent** | Rotate user-agents to avoid blocking |
| **Audit Trail** | Log all searches to CBO-01 pipeline |
| **Data Sensitivity** | Do not download TLP:RED documents via automation |

---

## 🧪 Testing Checklist

- [ ] SAM.gov search (cybersecurity keyword)
- [ ] Extract opportunity cards (title, agency, deadline)
- [ ] ePerolehan search (Malaysian tenders)
- [ ] Download sample RFP document
- [ ] Deadline filter (30-day window)
- [ ] Multi-portal scan (all 5 portals)
- [ ] Log results to CBO-01 register

---

## 📊 Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Portal Coverage | 5/5 portals | SAM, Grants, ePerolehan, CSM, MAMPU |
| Search Accuracy | ≥90% | Relevant RFPs captured |
| Download Success | ≥95% | Successful document retrieval |
| Deadline Accuracy | 100% | Correct date parsing |
| Alert Timeliness | <1 hour | New RFP → DAF notification |

---

## 🔧 Troubleshooting

| Issue | Cause | Resolution |
|-------|-------|------------|
| Search fails | CAPTCHA / bot detection | Add 10-15 second delays, rotate user-agent |
| Selector not found | Portal UI update | Refresh selectors via dev tools |
| Download blocked | Authentication required | Login first, then download |
| Deadline parse error | Date format mismatch | Add format fallbacks (MM/DD/YYYY, DD-MMM-YYYY) |
| Portal timeout | Server overload | Retry with exponential backoff |

---

## 📚 References

- SAM.gov: https://sam.gov/
- Grants.gov: https://grants.gov/
- ePerolehan: https://www.eperolehan.gov.my/
- CSM Tenders: https://www.cybersecurity.com.my/tenders
- MAMPU: https://www.mampu.gov.my/
- CBO-01 Commercial Register: `/home/p62operator/.openclaw/workspace-cbo-01/COMMERCIAL-REGISTER.md`
- Browser Harness SKILL.md: `/home/p62operator/.openclaw/deployments/browser-harness/SKILL.md`

---

**Document Location:** `/home/p62operator/.openclaw/deployments/browser-harness/domain-skills/govsec/rfp-search.md`  
**Next Review:** May 7, 2026 (after first RFP alert cycle)

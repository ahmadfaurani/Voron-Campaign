# Standard Operating Procedure — Phase 1 Intelligence Collection

**Operation:** TIER2-INTEL  
**Phase:** Phase 1 (Intelligence Collection)  
**Timeline:** May 10-12, 2026 (60 hours)  
**Owner:** HOI Agent  
**Classification:** TLP:AMBER

---

## 1. Objective

Collect intelligence on 100 Tier 2 agencies (Federal/State/Statutory) across 4 dimensions:
1. **Agency Profile** (name, type, mandate, leadership)
2. **Contact Intel** (name, title, email, phone)
3. **Threat Landscape** (breach history, APT targeting, compliance deadlines)
4. **Budget + Vendor** (budget cycle, current vendor, contract expiry)

---

## 2. Collection Workflow (Per Agency)

**Time Budget:** 15-20 minutes per agency × 100 agencies = 25-33 hours (parallelized to 60 hours)

### Step 1: Agency Profile (5 min)

```bash
# Automated scraper extracts:
- Agency name
- Agency type (Federal/State/Statutory)
- Mandate (1-sentence description)
- Parent ministry (if applicable)
- Website URL
```

**Sources:**
- MyGovernment Portal (malaysia.gov.my/agency-directory)
- Agency official website
- LinkedIn company page

**Output:**
```json
{
  "agency_name": "Jabatan Imigresen Malaysia",
  "agency_type": "Federal Department",
  "mandate": "Immigration control and border security",
  "parent_ministry": "Kementerian Dalam Negeri",
  "website": "https://www.imigresen.gov.my",
  "confidence": "High"
}
```

---

### Step 2: Leadership + Contact Intel (7 min)

```bash
# LinkedIn + portal scraping:
- DG / Director-General name
- CIO / IT Director name
- CISO / Security Head name (if available)
- Email pattern inference (name@domain.gov.my)
- Phone number (from portal contact page)
```

**Sources:**
- LinkedIn (company page + staff profiles)
- Agency "About Us" / "Leadership" page
- Government contact directory

**Output:**
```json
{
  "dg_name": "Datuk Mustafar Ali",
  "dg_title": "Director-General of Immigration",
  "cio_name": "[To be filled]",
  "cio_title": "Director of IT",
  "email_pattern": "firstname.lastname@imigresen.gov.my",
  "phone": "+603-8880-1000",
  "confidence": "Medium"
}
```

---

### Step 3: Threat Intel Correlation (5 min)

```bash
# News API + manual search:
- Recent breaches (last 12 months): Y/N + details
- Nation-state targeting: High/Medium/Low
- Compliance deadlines: PDPA, NACSA Act dates
- MyCERT incident reports: Count + type
```

**Sources:**
- MyCERT quarterly reports
- NACSA public statements
- News search (The Star, Cybersecurity Review)
- Unit 42 APT reports

**Output:**
```json
{
  "recent_breach": "No",
  "nation_state_targeting": "High (border security agency)",
  "compliance_deadline": "2026-Q4 (NACSA Act)",
  "mycert_incidents": "0 reported",
  "threat_score": 75,
  "confidence": "High"
}
```

---

### Step 4: Budget + Vendor Intel (3 min)

```bash
# ePerolehan + parliamentary records:
- Current security vendor (if known)
- Contract expiry (quarter + year)
- Budget cycle (Q1-Q4 2026)
- Anomaly flag (emergency funding: Y/N)
```

**Sources:**
- ePerolehan tender notices
- MyProcurement (Treasury)
- Parliamentary budget records

**Output:**
```json
{
  "current_vendor": "Unknown",
  "contract_expiry": "Unknown",
  "budget_cycle": "Q4 2026",
  "anomaly_flag": "No",
  "budget_score": 50,
  "confidence": "Low"
}
```

---

## 3. Automation Scripts

### Script 1: Gov Directory Scraper

**Location:** `/home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/sources/gov-directory-scraper.py`

**Purpose:** Extract agency names, types, websites from MyGovernment portal

**Usage:**
```bash
cd /home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/sources
python3 gov-directory-scraper.py --output ../evidence/Agency-Profiles/raw-agencies.csv
```

**Output:** CSV with 150-200 agencies (pre-filtering)

---

### Script 2: LinkedIn OSINT Collector

**Location:** `/home/p62operator/.openclaw/workspace-hoi/sources/linkedin-collector.py`

**Purpose:** Extract leadership names from LinkedIn company pages

**Usage:**
```bash
python3 linkedin-collector.py --agency "Jabatan Imigresen Malaysia" --output ../ops/tier2-intel/evidence/Agency-Profiles/001-Imigresen-leadership.json
```

**Output:** JSON with DG, CIO, CISO names + titles

---

### Script 3: Threat Intel Correlator

**Location:** `/home/p62operator/.openclaw/workspace-hoi/sources/threat-intel-correlator.py`

**Purpose:** Search MyCERT, NACSA, news for agency-specific incidents

**Usage:**
```bash
python3 threat-intel-correlator.py --agency "Jabatan Imigresen Malaysia" --output ../ops/tier2-intel/evidence/Threat-Intel/001-Imigresen-threat.json
```

**Output:** JSON with breach history, targeting status, threat score

---

### Script 4: Budget Anomaly Detector

**Location:** `/home/p62operator/.openclaw/workspace-hoi/models/budget-anomaly-detector.py`

**Purpose:** Flag unusual budget allocations (5-20x sector normal)

**Usage:**
```bash
python3 budget-anomaly-detector.py --input ../ops/tier2-intel/sources/budget-data.csv --output ../ops/tier2-intel/models/anomaly_results.csv
```

**Output:** CSV with flagged agencies (priority for urgent outreach)

---

## 4. Evidence Preservation

### File Naming Convention

```
[Priority]-[AgencyShortName]-[DataType]-[Date].md
Example: 001-Imigresen-Profile-2026-05-10.md
```

### Directory Structure

```
/home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/evidence/
├── Agency-Profiles/
│   ├── 001-Imigresen-Profile-2026-05-10.md
│   ├── 002-KKM-Profile-2026-05-10.md
│   └── ... (100 files)
├── Threat-Intel/
│   ├── 001-Imigresen-Threat-2026-05-10.md
│   └── ... (100 files)
└── Budget-Analysis/
    ├── 001-Imigresen-Budget-2026-05-10.md
    └── ... (100 files)
```

### Chain-of-Custody Log

**Location:** `/home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/evidence/chain-of-custody.log`

**Format:**
```
[Timestamp] [Collector] [Agency] [DataType] [Confidence] [Status]
2026-05-10 14:30 UTC | HOI-Agent | 001-Imigresen | Profile | High | Complete
2026-05-10 14:35 UTC | HOI-Agent | 001-Imigresen | Leadership | Medium | Complete
2026-05-10 14:40 UTC | HOI-Agent | 001-Imigresen | Threat-Intel | High | Complete
```

---

## 5. Quality Control Checkpoints

### Checkpoint 1: 25% Complete (25 agencies) — May 11, 08:00 UTC

**Review:**
- Contact completeness ≥80%?
- Threat intel accuracy ≥90%?
- Budget intel ≥70%?

**Action:** Adjust collection method if metrics not met.

---

### Checkpoint 2: 50% Complete (50 agencies) — May 11, 20:00 UTC

**Report to DAF + CBO-01:**
- Progress summary
- Gap analysis
- Timeline confidence (On track / At risk / Delayed)

---

### Checkpoint 3: 75% Complete (75 agencies) — May 12, 08:00 UTC

**Review:**
- Accelerate collection (parallelize more)
- Flag low-confidence items for manual review
- Prepare for Phase 2 processing

---

### Checkpoint 4: 100% Complete — May 12, 20:00 UTC

**Deliverable:**
- 100 agency profiles complete
- Evidence register populated
- Chain-of-custody log finalized
- Ready for Phase 2 (Processing + Scoring)

---

## 6. Escalation Protocol

| Issue | Severity | Escalation Path | Timeline |
|-------|----------|-----------------|----------|
| **Contact intel <80% after 50 agencies** | Medium | HOI → DAF (request CSM manual fill-in) | 4 hours |
| **Threat intel conflicts (CSM vs. HOI)** | High | HOI + Zaharudin (joint validation) | 2 hours |
| **Tooling failure (scraper broken)** | Medium | HOI → Manual fallback | 1 hour |
| **Timeline slip (>12 hours behind)** | High | HOI → DAF (compress Phase 2) | Immediate |

---

## 7. Output Format (Per Agency)

**Template:** `/home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/evidence/Agency-Profiles/TEMPLATE.md`

```markdown
---
**Agency:** [Name]
**Type:** Federal / State / Statutory
**Collection Date:** [Date]
**Collector:** HOI Agent
**Confidence:** High / Medium / Low
---

## 1. Agency Profile
- **Mandate:** [1 sentence]
- **Parent Ministry:** [If applicable]
- **Website:** [URL]
- **Employee Count:** [Approximate]

## 2. Leadership + Contact
- **DG:** [Name + Title]
- **CIO:** [Name + Title]
- **CISO:** [Name + Title]
- **Email Pattern:** [name@domain.gov.my]
- **Phone:** [Number]

## 3. Threat Intel
- **Recent Breach (12 months):** Y/N + details
- **Nation-State Targeting:** High/Medium/Low
- **Compliance Deadline:** [Date]
- **Threat Score:** XX/100

## 4. Budget + Vendor
- **Current Vendor:** [Name / Unknown]
- **Contract Expiry:** [Quarter + Year / Unknown]
- **Budget Cycle:** Q1-Q4 2026
- **Anomaly Flag:** Y/N

## 5. Sources
- [URL 1]
- [URL 2]
- [CSM validation: Pending/Confirmed]

## 6. Evidence Chain
- Collected: [Timestamp]
- Validated: [Timestamp / Pending]
- Stored: [File path]
```

---

**SOP Status:** ✅ **Active** (May 10, 2026 12:00 UTC)  
**Phase 1 Progress:** 0/100 agencies (0%)  
**Next Checkpoint:** May 11, 08:00 UTC (25% complete)

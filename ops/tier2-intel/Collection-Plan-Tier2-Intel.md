# HOI Collection Plan — OPERATION TIER2-INTEL

**Classification:** TLP:AMBER  
**Operation Codename:** TIER2-INTEL  
**Collection Lead:** HOI Agent  
**Mission Owner:** DAF (CBO-01 Commercialization Agent)  
**Timeline:** May 10-14, 2026 (96-hour sprint)  
**Status:** ⏳ **ACTIVE** (Phase 0 Complete, Phase 1 In Progress)

---

## 1. Collection Priority Intelligence Requirements (PIRs)

| PIR # | Requirement | Priority | Collection Method | Due Date | Status |
|-------|-------------|----------|-------------------|----------|--------|
| **PIR-01** | 100 Tier 2 agency profiles (Federal/State/Statutory) | P1 | Web scraping + OSINT | May 12, 20:00 UTC | ⏳ In Progress |
| **PIR-02** | Contact intel (name, title, email, phone) ≥80% complete | P1 | LinkedIn + gov portals | May 12, 20:00 UTC | ⏳ In Progress |
| **PIR-03** | Threat intel (breach history, APT targeting) ≥90% accurate | P1 | MyCERT + NACSA + news | May 12, 20:00 UTC | ⏳ In Progress |
| **PIR-04** | Budget intel (cycle timing, anomaly flags) ≥70% complete | P2 | ePerolehan + parliamentary records | May 12, 20:00 UTC | ⏳ Pending |
| **PIR-05** | CSM relationship warmth validation | P1 | Zaharudin Ahmad Darus input | May 11, 17:00 UTC | ⏳ Awaiting |
| **PIR-06** | Aras pipeline status enrichment | P1 | Farul Mohd Ghazali export | May 11, 17:00 UTC | ⏳ Awaiting |

---

## 2. Collection Sources

### Source Category 1: Government Directories (P1)

| Source | URL | Data Type | Collection Method | Status |
|--------|-----|-----------|-------------------|--------|
| **MyGovernment Portal** | malaysia.gov.my/agency-directory | Federal agency list | Web scraper | ⏳ Queued |
| **State Government Portals** | Each state .gov.my | State agency lists | Web scraper | ⏳ Queued |
| **NCI Critical Infrastructure** | Public directory | Sector operators | Manual + scraper | ⏳ Queued |
| **JDN (Jabatan Digital Negara)** | jdn.gov.my | RPSA 2026-2030 agencies | Web scraper | ⏳ Queued |

### Source Category 2: Leadership + Contact Intel (P1)

| Source | URL | Data Type | Collection Method | Status |
|--------|-----|-----------|-------------------|--------|
| **LinkedIn** | linkedin.com/company | DG, CIO, CISO names | HOI LinkedIn collector | ⏳ Queued |
| **Agency Official Portals** | agency.gov.my/en/about-us | Leadership profiles | Web scraper | ⏳ Queued |
| **Twitter/X** | twitter.com | Official accounts, leadership | HOI social collector | ⏳ Queued |
| **Facebook** | facebook.com | Agency pages, staff profiles | HOI social collector | ⏳ Queued |

### Source Category 3: Threat Intelligence (P1)

| Source | URL | Data Type | Collection Method | Status |
|--------|-----|-----------|-------------------|--------|
| **MyCERT Reports** | mycert.org.my | Breach reports, quarterly summaries | News API + manual | ✅ Active |
| **NACSA Statements** | nacsa.gov.my | Cyber-espionage investigations | News API | ✅ Active |
| **Cybersecurity Review** | cybersecurity-review.com | Malaysia breach news | RSS feed | ✅ Active |
| **The Star Tech** | thestar.com.my/tech | Cyber incident reporting | RSS feed | ✅ Active |
| **Unit 42 (Palo Alto)** | unit42.paloaltonetworks.com | APT campaign reports | Web fetch | ⏳ Queued |

### Source Category 4: Budget + Vendor Intel (P2)

| Source | URL | Data Type | Collection Method | Status |
|--------|-----|-----------|-------------------|--------|
| **ePerolehan Tender Notices** | eperolehan.gov.my | Security vendor contracts | Web scraper | ⏳ Queued |
| **MyProcurement (Treasury)** | myprocurement.treasury.gov.my | Tender advertisements | Web scraper | ⏳ Queued |
| **Parliamentary Budget Records** | parliament.gov.my | Budget allocations | Manual + scraper | ⏳ Queued |
| **TendersOnTime** | tendersontime.com | Security service tenders | API (if available) | ⏳ Queued |

### Source Category 5: CSM/Aras Input (P1)

| Source | Owner | Data Type | Collection Method | Status |
|--------|-------|-----------|-------------------|--------|
| **CSM Relationship Data** | Zaharudin Ahmad Darus | 40-50 accounts, warmth scores | Email intake | ⏳ Awaiting |
| **Aras Pipeline Export** | Farul Mohd Ghazali | 20-30 accounts, CRM status | Email intake | ⏳ Awaiting |
| **MINDEF Network Intel** | Hadri (via Lt Kol Rajeswari) | 10-15 defence-adjacent agencies | Email/WhatsApp intake | ⏳ Awaiting |

---

## 3. Collection Tools Deployed

| Tool | Purpose | Location | Status |
|------|---------|----------|--------|
| **PH0MBER** | OSINT reconnaissance (ip, whois, dns, username) | `/home/p62operator/.openclaw/workspace/research/phomber-lab/` | ⏳ Deploy May 12 |
| **Budget Anomaly Detector** | Flag emergency cyber funding | `/home/p62operator/.openclaw/workspace-hoi/models/budget-anomaly-detector.py` | ✅ Active |
| **Gov Directory Scraper** | Extract agency names, types, leadership | `/home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/sources/gov-directory-scraper.py` | ⏳ In Development |
| **LinkedIn OSINT Collector** | Extract leadership profiles | `/home/p62operator/.openclaw/workspace-hoi/sources/linkedin-collector.py` | ✅ Active |
| **News API Collector** | MyCERT, NACSA, breach reports | `/home/p62operator/.openclaw/workspace-hoi/sources/news-collector.py` | ✅ Active |
| **Evidence Register** | Chain-of-custody for intel artifacts | `/home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/evidence/` | ✅ Initialized |

---

## 4. Collection Timeline (96-Hour Sprint)

```
May 10 (Sun)         May 11 (Mon)         May 12 (Tue)         May 13 (Wed)         May 14 (Thu)
│                    │                    │                    │                    │
├─ Phase 0 ─┤        │                    │                    │                    │
│ Mobilization       │                    │                    │                    │
│ 11:00-12:00 UTC    │                    │                    │                    │
│                    ├─ Phase 1 ──────────┤                    │                    │
│                    │ Collection         │                    │                    │
│                    │ 08:00-20:00 UTC    │                    │                    │
│                    │ (60 hours total)   │                    │                    │
│                    │                    ├─ Phase 2 ──────────┤                    │
│                    │                    │ Processing         │                    │
│                    │                    │ 08:00-18:00 UTC    │                    │
│                    │                    │ (22 hours total)   │                    │
│                    │                    │                    ├─ Phase 3 ──────────┤
│                    │                    │                    │ Handoff            │
│                    │                    │                    │ 08:00-12:00 UTC    │
│                    │                    │                    │ (8 hours)          │
│                    │                    │                    │                    ├─ Phase 4 ──→
│                    │                    │                    │                    │ Monitoring
```

---

## 5. Intelligence Products (Deliverables)

| Product | Format | Audience | Due Date | Status |
|---------|--------|----------|----------|--------|
| **Intel Brief 001** | Markdown (5-10 pages) | DAF + CBO-01 | May 12, 18:00 UTC | ⏳ Pending |
| Tier 2 Overview — 100 account summary | | | | |
| **Intel Brief 002** | Markdown + PDF | DAF + CBO-01 | May 12, 20:00 UTC | ⏳ Pending |
| Threat Landscape — APT campaigns targeting Malaysia | | | | |
| **Intel Brief 003** | Markdown (validation request) | Zaharudin (CSM) | May 13, 10:00 UTC | ⏳ Pending |
| CSM Relationship Validation — 40-50 account review | | | | |
| **Intel Brief 004** | Markdown (validation request) | Farul (Aras) | May 13, 12:00 UTC | ⏳ Pending |
| Aras Pipeline Enrichment — 20-30 account review | | | | |
| **Intel Brief 005** | Markdown (20 one-pagers) | DAF (Final) | May 13, 18:00 UTC | ⏳ Pending |
| Top 20 Tier A Profiles — Full intelligence dossiers | | | | |
| **Master Intel Package** | CSV (100 rows, 20 columns) | CBO-01 | May 13, 18:00 UTC | ⏳ Pending |
| Unified account list with scoring | | | | |

---

## 6. Evidence Register

**Location:** `/home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/evidence/`

### Evidence Categories

| Category | Sub-Directory | File Count Target | Status |
|----------|---------------|-------------------|--------|
| **Agency Profiles** | `evidence/Agency-Profiles/` | 100 files (1 per agency) | ⏳ In Progress |
| **Threat Intel** | `evidence/Threat-Intel/` | 10-20 reports (MyCERT, NACSA, etc.) | ⏳ Pending |
| **Budget Analysis** | `evidence/Budget-Analysis/` | 20-30 anomaly reports | ⏳ Pending |

### Chain-of-Custody Format

```markdown
## Evidence Item: [Agency Name] Profile

**Evidence ID:** TIER2-AGY-001  
**Collection Date:** May 10, 2026 14:30 UTC  
**Collector:** HOI Agent (Automated OSINT)  
**Source:** [URL(s) used]  
**Method:** Web scraping + LinkedIn OSINT  
**Confidence:** High / Medium / Low  
**Validation:** Pending CSM review  

**Artifacts:**
- [ ] Leadership profile extracted
- [ ] Contact email inferred
- [ ] Threat intel correlated
- [ ] Budget intel flagged

**Storage:** `/home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/evidence/Agency-Profiles/001-[AgencyName].md`
```

---

## 7. Quality Control

### Confidence Scoring Matrix

| Confidence Level | Criteria | Action |
|-----------------|----------|--------|
| **High (≥90%)** | ≥3 independent sources confirm | Use in final intel package |
| **Medium (70-89%)** | 2 sources confirm, 1 gap | Flag for CSM validation |
| **Low (<70%)** | Single source or conflicting data | Exclude or mark "Unverified" |

### Validation Workflow

```
HOI Collection → Automated Scoring → CSM Validation (Zaharudin) → Final Confidence Assignment → CBO-01 Handoff
```

---

## 8. Risk Mitigation

| Risk | Mitigation | Owner |
|------|------------|-------|
| **Contact intel <80% complete** | HOI escalates to CSM for manual fill-in | HOI Agent |
| **Threat intel outdated** | Cross-validate with MyCERT + CSM | HOI Agent |
| **CSM/Aras data delayed** | Proceed with HOI OSINT only, mark gaps | CBO-01 |
| **Tooling failures** | Manual fallback research | HOI Agent |
| **Timeline slip** | Compress Phase 2 (parallel processing) | DAF |

---

## 9. Handoff Protocol (HOI → CBO-01)

**Handoff Date:** May 13, 18:00 UTC  
**Format:** CSV + Markdown one-pagers + Intelligence briefs  
**Location:** `/home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/handoff/`

### Acceptance Criteria

- [ ] 100 accounts profiled
- [ ] Contact info ≥80% complete
- [ ] Threat intel ≥90% accurate (CSM-validated)
- [ ] Budget analysis ≥70% complete
- [ ] Scoring rationale documented
- [ ] Source citations included
- [ ] Evidence register populated

### Handoff Package Contents

| File | Format | Size (Est.) |
|------|--------|-------------|
| `CBO-01-Intel-Package.csv` | CSV (100 rows, 20 cols) | ~50 KB |
| `TierA-OnePagers/` (20 files) | Markdown | ~200 KB |
| `Intel-Brief-001-Tier2-Overview.md` | Markdown | ~20 KB |
| `Intel-Brief-002-Threat-Landscape.md` | Markdown + PDF | ~50 KB |
| `anomaly_results.csv` | CSV (budget flags) | ~10 KB |
| `Source-Registry.md` | Markdown | ~15 KB |

---

**Collection Status:** ⏳ **ACTIVE** (Phase 0 Complete, Phase 1 In Progress)  
**Next Checkpoint:** May 11, 20:00 UTC (Phase 1 Midpoint — 50% collection complete)  
**Mission Owner:** DAF  
**Collection Lead:** HOI Agent

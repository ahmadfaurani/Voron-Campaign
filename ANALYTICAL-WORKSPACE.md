# HOI Intelligence Ops — Analytical Workspace

**Generated:** 2026-07-11  
**Classification:** TLP:AMBER  
**Repository:** `ahmadfaurani/hoi-intelligence-ops` (Private)  
**Commit:** `894c652` · **Tracked files:** 463 · **Branch:** `main`

---

## 1. Executive Summary

This workspace serves as the **sovereign intelligence operations** hub for a multi-domain intelligence apparatus spanning cybersecurity, political-electoral, government, law enforcement, financial, and media intelligence. The repository contains 11 distinct component clusters with 463 tracked files, supported by automated cron-driven pipelines and self-hosted infrastructure (DeerFlow, Firecrawl, SearXNG, OpenOSINT).

**Key findings:**
- **5 tightly coupled component pairs** (relevance ≥3.5/5.0) form the operational core
- **3 dormant workstreams** (Cyber Intel, Gov Tier2, PDRM IO) represent 60% of tracked files but are inactive
- **2 active operational workstreams** (PRN Johor, VoronDRQ) drive current intelligence production
- The Intelligence Pipeline is the **highest-coupled component** (avg 3.12/5.0) — it's the backbone

---

## 2. Component Inventory

### 2.1 Active Components

| ID | Component | Domain | Priority | Files | Status | Key Output |
|----|-----------|--------|----------|-------|--------|------------|
| **INTEL_PIPELINE** | Intelligence Collection Pipeline | D-ALL | P0 | 197 | ACTIVE | Daily briefs, narrative reports, sentiment analysis |
| **PRN_JOHOR** | PRN Johor 2026 Political Intelligence | D2 | P1 | 12 | ACTIVE | Constituency profiles, campaign manuals |
| **MEDIA_REGISTRY** | Media Intelligence & Journalist Registry | D2/D3 | P1 | 4 | ACTIVE | Media contact database, outlet expansion |
| **VORON_DRQ** | VoronDRQ Commercial Intelligence | D5 | P2 | 14 | ACTIVE | Prospect databases, stakeholder profiles, RMiT gaps |
| **OPENOSINT** | OpenOSINT Integration | D-ALL | P1 | 4 | ACTIVE | OSINT verification, infrastructure recon |
| **INFRA_CONFIG** | Infrastructure & Configuration | D-ALL | P0 | 19 | ACTIVE | Config, planning, infrastructure docs |

### 2.2 Dormant Components

| ID | Component | Domain | Priority | Files | Last Active | Status |
|----|-----------|--------|----------|-------|-------------|--------|
| **GOV_TIER2** | Government Tier2 Intelligence | D2 | P1 | 157 | May 10, 2026 | DORMANT |
| **PDRM_IO** | PDRM IO Intelligence | D4 | P1 | 34 | Jun 22, 2026 | DORMANT |
| **CYBER_INTEL** | Cybersecurity Intelligence | D1 | P1 | 10 | May 21, 2026 | DORMANT |
| **BUDGET_INTEL** | Government Budget Intelligence | D2/D5 | P2 | 6 | Apr 29, 2026 | DORMANT |
| **DOCUMENTATION** | Core Documentation | D-ALL | P0 | 6 | Jun 13, 2026 | STALE |

---

## 3. Component Details

### 3.1 Intelligence Collection Pipeline (INTEL_PIPELINE)
**Function:** Automated daily pipeline: news collection → entity extraction → sentiment analysis → narrative tracking → daily brief generation  
**Relevance Score:** 3.12/5.0 (highest — backbone component)  
**Status:** Active, cron-driven (last output Jul 11, 2026)  

**Pipeline stages:**
```
collect-political-news.py → intelligence/raw/
    ↓
extract-entities.py → intelligence/entities/
    ↓
sentiment-analysis.py → intelligence/sentiment-analysis/
    ↓
narrative-tracking-analysis.py → intelligence/narrative-tracking/
    ↓
generate-daily-brief.py → intelligence/briefs/
```

**Key files:**
- `scripts/collect-political-news.py` — Firecrawl v1 API, 7 sources, 30s timeout
- `scripts/extract-entities.py` / `extract-entities-latest.py` — NLP entity extraction
- `scripts/sentiment-analysis.py` — VADER sentiment (scale -3 to +3)
- `scripts/narrative-tracking-analysis.py` — 10 narrative clusters, velocity tracking
- `scripts/generate-daily-brief.py` — 7-section daily brief template

**Output volume:**
- 30 daily briefs (INTEL-008 → INTEL-034, Jun 13 → Jul 10)
- 96 narrative tracking reports (6-hourly, Jun 13 → Jul 11)
- 44 sentiment analysis reports (daily, Jun 28 → Jul 10)

**Dependencies:** `config/sources.yaml`, `config/sentiment-lexicon.yaml`, `config/narrative-clusters.yaml`, `config/pir-definitions.yaml`

---

### 3.2 PRN Johor 2026 Political Intelligence (PRN_JOHOR)
**Function:** Electoral intelligence for 20 priority DUN seats in Johor State Election  
**Relevance Score:** 2.44/5.0  
**Status:** Active, CVS framework operational (6 constituencies cleared)  

**Constituencies tracked:**
- **DEFEND:** N51 Bukit Batu (commits paused)
- **RECAPTURE:** N41 Puteri Wangsa
- **SWING:** N47 Kempas, N24 Senggarang, N03 Pemanis, N27 Layang-Layang, N01 Buloh Kasap, N54 Pulai Sebatang
- **EXPAND:** N07 Bukit Kepong
- **N/A:** N18 Sri Medan

**Key files:**
- `prn-johor-2026/swing-seats-campaign-manual.md` (21KB)
- `prn-johor-2026/swing-seats-demographic-data.md` (14KB)
- `constituency-analysis/03-pemanis-overview-20260627.md` (13KB)
- `constituency-analysis/8-layang-layang-190626.md` (6KB)
- `N07_Bukit_Kepong_Expanded_Report_*` (4 parts, 50KB+)
- `briefs/n17-skudai-analytical-report-2026-06-26.md` (30KB)
- `war-room-reports/n27-layang-layang-candidate-analysis-270626.md`

**Submodules:** `intelligence/prn-johor-2026/` (gitlink, 409 files), `intelligence/kempas/` (gitlink)

---

### 3.3 Cybersecurity Intelligence (CYBER_INTEL)
**Function:** National cyber posture, threat actor tracking, vulnerability intelligence  
**Relevance Score:** 1.88/5.0 (low coupling — standalone domain)  
**Status:** DORMANT since May 21, 2026

**Key files:**
- `intelligence/Intel-Brief-001-Malaysia-Digital-Dependency-2026-04-26.md`
- `intelligence/Intel-Brief-003-PhantomRPC-Latest-2026-04-30.md`
- `intelligence/Intel-Brief-004-KazSign-PQC-2026-04-30.md`
- `intelligence/Intel-Brief-005-Thunderbolt-Mozilla-2026-05-01.md`
- `intelligence/Intel-Brief-006-ml-intern-HuggingFace-2026-05-01.md`
- `intelligence/Intel-Brief-007-Threat-Actor-Registry-Webworm-2026-05-21.md`
- `intelligence/DISTRIBUTION/DirtyDecrypt-Distribution-Package.md`
- `intelligence/DISTRIBUTION/MSFT-Defender-ZeroDays-Distribution-Package.md`
- `intelligence/Brief-Prof-Rezal-Background-2026-04-30.md`

**Strongest coupling:** OPENOSINT (3.2) — OSINT tools support cyber reconnaissance

---

### 3.4 Government Tier2 Intelligence (GOV_TIER2)
**Function:** Systematic government agency profiling for OSINT collection  
**Relevance Score:** 2.64/5.0  
**Status:** DORMANT since May 10, 2026  
**Volume:** 144 agency profiles + execution plans + source scripts

**Key files:**
- `ops/tier2-intel/evidence/Agency-Profiles/` — 144 profiles (001-143 + template)
- `ops/tier2-intel/execution/MASTER-EXECUTION-PLAN-2026-05-10.md`
- `ops/tier2-intel/execution/CONTINGENCY-PLAN-DNS-BLOCKER-2026-05-10.md`
- `ops/tier2-intel/sources/gov-directory-scraper.py`
- `ops/tier2-intel/sources/doh-crawler.py`
- `ops/tier2-intel/sources/batch-processor.py`

**Strongest coupling:** OPENOSINT (3.2), BUDGET_INTEL (3.2), INFRA_CONFIG (3.2)

---

### 3.5 PDRM IO Intelligence (PDRM_IO)
**Function:** PDRM Information Operations: contact discovery, web crawling, directory extraction  
**Relevance Score:** 2.04/5.0  
**Status:** DORMANT since Jun 22, 2026

**Key files:**
- Root: `pdrm-io-100-search-queries.md`, `pdrm-io-automation-guide.md`, `pdrm-io-comprehensive-crawl-guide.md`, `pdrm-io-full-execution-summary.md`, `pdrm-io-search-expansion-summary.md`, `pdrm-io-search-query-list.md`
- Intelligence: `intelligence/pdrm-io-contact-database.md`, `intelligence/pdrm-contacts-directory.md`, 12+ summary/analysis files
- Scripts: 8 Python scripts (`pdrm-io-extractor-v5.py`, `pdrm-io-comprehensive-crawler.py`, etc.)

**Strongest coupling:** INTEL_PIPELINE (3.0) — shares collection framework

---

### 3.6 Media Intelligence & Journalist Registry (MEDIA_REGISTRY)
**Function:** Journalist registry for media relationship intelligence (TLP:AMBER)  
**Relevance Score:** 2.40/5.0  
**Status:** Active (submodule gitignored, cron-driven collection)

**Key files:**
- `intelligence/Malaysian-Media-Intelligence-Database.md`
- `JOURNALIST-FOCUS-IMPLEMENTATION.md`
- `MEDIA-OUTLET-EXPANSION.md`
- `config/MEDIA-EXPANSION-SUMMARY.md`
- `reference/media-contact-database.md`
- `scripts/discover-media-emails.py`, `scripts/discover-emails-fast.py`
- `scripts/test-journalist-focus.py`

**Target:** 600+ journalists across 27 Malaysian outlets  
**Strongest coupling:** INTEL_PIPELINE (3.6), PRN_JOHOR (3.4), OPENOSINT (3.0)

---

### 3.7 VoronDRQ Commercial Intelligence (VORON_DRQ)
**Function:** GRC platform targeting BNM-regulated financial institutions  
**Relevance Score:** 1.72/5.0 (low coupling — commercial domain)  
**Status:** Active (enrichment workflow, separate Voron-Campaign.git repo)

**Key files:**
- `campaign-operations-manual.md` (45KB)
- `collateral/battle-cards.md` (19KB)
- `collateral/email-templates.md` (21KB)
- `collateral/rmit-compliance-checklist.md` (25KB)
- `prospects/prospect-database-250.csv`, `prospects/prospect-database-7stakeholders.csv`
- `voron-stakeholders/prospect-database-enriched-v1.6.csv`
- `voron-campaign/prospects/STAKEHOLDER_ENRICHMENT_PLAN.md`
- `voron-campaign/scripts/enrich-stakeholders.py`

**Strongest coupling:** OPENOSINT (3.8) — verification and enrichment

---

### 3.8 OpenOSINT Integration (OPENOSINT)
**Function:** Automated OSINT: breach checks, Shodan, DNS, social presence  
**Relevance Score:** 2.78/5.0 (high — serves multiple workstreams)  
**Status:** Active (v2.23.0, integrated with cron jobs)

**Key files:**
- `OPENOSINT_INSTALLATION_SUMMARY.md`
- `OPENOSINT_INTEGRATION.md`
- `openosint-activate.sh`
- `openosint-targets.txt`
- `openosint-config.env` (gitignored — API keys)

**Strongest coupling:** VORON_DRQ (3.8), CYBER_INTEL (3.2), GOV_TIER2 (3.2)

---

### 3.9 Government Budget Intelligence (BUDGET_INTEL)
**Function:** ML-driven government budget analysis and anomaly detection  
**Relevance Score:** 1.62/5.0 (lowest — isolated domain)  
**Status:** DORMANT since Apr 29, 2026

**Key files:**
- `workflows/GOV-BUDGET-INTELLIGENCE.md`
- `workflows/budget_pipeline.py`
- `workflows/BUDGET-INTELLIGENCE-STATUS-REPORT.md`
- `models/budget_anomaly_detector.py`
- `models/sector_classifier.py`
- `models/isolation_forest_20260429_035745.pkl`

**Strongest coupling:** GOV_TIER2 (3.2) — shared government domain

---

### 3.10 Infrastructure & Configuration (INFRA_CONFIG)
**Function:** Core configuration, planning, and infrastructure documentation  
**Relevance Score:** 3.00/5.0 (high — serves all components)  
**Status:** Active (updated Jul 11, 2026)

**Key files:**
- `config/sources.yaml` (11KB — 7 news sources)
- `config/pir-definitions.yaml` (9KB — 10 PIRs)
- `config/narrative-clusters.yaml` (8KB — 10 narratives)
- `config/sentiment-lexicon.yaml` (7KB — sentiment rules)
- `planning/offensive-stack-review-20260708.md`
- `planning/gateway-fix-report-20260708.md`
- `planning/HOI-Improvement-Plan-Q2-2026.md`
- `planning/Political-Monitoring-Workstream-Review-2026-06-13.md`
- `workflows/BROWSER-HARNESS-INTEGRATION.md`
- `skills/browser-harness/govsec/` (4 files)

**Strongest coupling:** INTEL_PIPELINE (4.6), PRN_JOHOR (3.6), DOCUMENTATION (3.0)

---

### 3.11 Core Documentation (DOCUMENTATION)
**Function:** Repository navigation, agent specification, workspace manual  
**Relevance Score:** 1.88/5.0  
**Status:** STALE (last updated Jun 13, 2026)

**Key files:**
- `README.md`, `AGENT-SPEC.md` (65KB), `STRUCTURE-SUMMARY.md`
- `WORKSPACE-MANUAL.md`, `UPLOAD-SUMMARY.md`, `LICENSE`

**Action needed:** Update STRUCTURE-SUMMARY.md and WORKSPACE-MANUAL.md to reflect current state

---

## 4. Cross-Relevance Matrix

### 4.1 Coupling Tiers

**TIGHTLY COUPLED (≥3.5)** — Core operational dependencies:
- `INTEL_PIPELINE ↔ INFRA_CONFIG` — **4.6** (pipeline depends on all config files)
- `INTEL_PIPELINE ↔ PRN_JOHOR` — **4.4** (pipeline feeds political intelligence)
- `VORON_DRQ ↔ OPENOSINT` — **3.8** (enrichment verification)
- `INTEL_PIPELINE ↔ MEDIA_REGISTRY` — **3.6** (pipeline feeds media collection)
- `PRN_JOHOR ↔ INFRA_CONFIG` — **3.6** (constituency data depends on config)

**MODERATELY COUPLED (2.5–3.4)** — Functional relationships:
- `PRN_JOHOR ↔ MEDIA_REGISTRY` — 3.4 (media intelligence serves political ops)
- `CYBER_INTEL ↔ OPENOSINT` — 3.2 (OSINT supports cyber recon)
- `GOV_TIER2 ↔ OPENOSINT` — 3.2 (OSINT supports agency profiling)
- `GOV_TIER2 ↔ BUDGET_INTEL` — 3.2 (shared government domain)
- `GOV_TIER2 ↔ INFRA_CONFIG` — 3.2 (shared infrastructure)
- `INTEL_PIPELINE ↔ PDRM_IO` — 3.0 (shared collection framework)
- `INTEL_PIPELINE ↔ OPENOSINT` — 3.0 (pipeline integration)
- `MEDIA_REGISTRY ↔ OPENOSINT` — 3.0 (journalist verification)
- `OPENOSINT ↔ INFRA_CONFIG` — 3.0 (tooling infrastructure)
- `INFRA_CONFIG ↔ DOCUMENTATION` — 3.0 (meta-documentation)

**LOOSELY COUPLED (<2.5)** — Weak/no direct relationship:
- 27 pairs with minimal functional coupling
- Notable isolation: BUDGET_INTEL (avg 1.62), VORON_DRQ (avg 1.72)

### 4.2 Component Coupling Strength Ranking

| Rank | Component | Avg Score | Role |
|------|-----------|-----------|------|
| 1 | INTEL_PIPELINE | 3.12 | **Backbone** — feeds and depends on most components |
| 2 | INFRA_CONFIG | 3.00 | **Foundation** — serves all components |
| 3 | OPENOSINT | 2.78 | **Force multiplier** — enhances multiple workstreams |
| 4 | GOV_TIER2 | 2.64 | **Dormant hub** — large volume, moderate coupling |
| 5 | PRN_JOHOR | 2.44 | **Active operational** — current priority |
| 6 | MEDIA_REGISTRY | 2.40 | **Active support** — serves political + pipeline |
| 7 | PDRM_IO | 2.04 | **Dormant specialist** — law enforcement niche |
| 8 | DOCUMENTATION | 1.88 | **Stale meta** — needs refresh |
| 8 | CYBER_INTEL | 1.88 | **Dormant specialist** — cybersecurity niche |
| 10 | VORON_DRQ | 1.72 | **Commercial isolate** — separate repo, low coupling |
| 11 | BUDGET_INTEL | 1.62 | **Most isolated** — dormant, minimal integration |

---

## 5. Data Flow Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        INFRASTRUCTURE LAYER                          │
│  config/ │ planning/ │ workflows/ │ skills/ │ .gitignore              │
│  sources.yaml │ pir-definitions │ narrative-clusters │ lexicon       │
└──────────────────────────────────┬──────────────────────────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                              ▼
┌──────────────────────────┐          ┌──────────────────────────┐
│   COLLECTION PIPELINE     │          │    OSINT LAYER            │
│  (INTEL_PIPELINE)        │          │  (OPENOSINT)              │
│                          │          │                          │
│  collect-political-news  │          │  openosint-activate.sh    │
│         ↓                │          │  Shodan / DNS / Breach    │
│  extract-entities        │          │  Social presence check   │
│         ↓                │          └──────┬───────────┬───────┘
│  sentiment-analysis      │                 │           │
│         ↓                │                 │           │
│  narrative-tracking      │                 │           │
│         ↓                │                 │           │
│  generate-daily-brief    │                 │           │
└──────────┬───────────────┘                 │           │
           │                                 │           │
           ▼                                 ▼           ▼
┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────┐
│  POLITICAL INTEL     │  │  MEDIA INTEL          │  │  COMMERCIAL     │
│  (PRN_JOHOR)        │  │  (MEDIA_REGISTRY)    │  │  (VORON_DRQ)    │
│                      │  │                      │  │                  │
│  Constituency profs  │◄►│  Journalist registry │  │  Prospect DB    │
│  Campaign manuals   │  │  Outlet expansion    │  │  RMiT gaps      │
│  War room reports    │  │  Contact database    │  │  Battle cards   │
└──────────────────────┘  └──────────────────────┘  └──────────────────┘
                                   │
           ┌───────────────────────┼───────────────────────┐
           ▼                       ▼                       ▼
┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────┐
│  DORMANT: CYBER      │  │  DORMANT: GOV TIER2   │  │  DORMANT: PDRM   │
│  (CYBER_INTEL)      │  │  (GOV_TIER2)         │  │  (PDRM_IO)       │
│                      │  │                      │  │                  │
│  Intel Briefs 1-7    │  │  144 agency profiles  │  │  Contact DB      │
│  Distribution pkgs   │  │  Execution plans      │  │  Crawl guides    │
│  Threat assessments  │  │  Source scripts       │  │  8 extraction    │
│                      │  │                      │  │  scripts         │
└──────────────────────┘  └──────────────────────┘  └──────────────────┘
                                   │
                                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│  DORMANT: BUDGET INTEL (BUDGET_INTEL)                               │
│  ML models: budget_anomaly_detector.py, sector_classifier.py        │
│  Pipeline: budget_pipeline.py │ Status: BUDGET-INTELLIGENCE-STATUS  │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 6. Temporal Activity Map

```
Apr 26 ─── May 1 ─── May 10 ─── May 21 ─── Jun 13 ─── Jun 22 ─── Jul 11
  │          │        │          │          │          │        │
  ├─CYBER────┤        │          │          │          │        │
  │  Intel 001        │          │          │          │        │
  │          ├─CYBER──┤          │          │          │        │
  │          │ 003-006│          │          │          │        │
  │          │        ├─GOV──────┤          │          │        │
  │          │        │ TIER2    │          │          │        │
  │          │        │ 144 prof │          │          │        │
  │          │        │          ├─CYBER────┤          │        │
  │          │        │          │ 007      │          │        │
  │          │        │          │          ├─PIPELINE─┤        │
  │          │        │          │          │ ACTIVE   │        │
  │          │        │          │          │ ├─MEDIA──┤        │
  │          │        │          │          │ │ REGIST │        │
  │          │        │          │          │ ├─PRN────┤        │
  │          │        │          │          │ │ JOHOR  │        │
  │          │        │          │          │ │        ├─PDRM──┤│
  │          │        │          │          │ │        │ IO    ││
  │          │        │          │          │ │        │       ├VORON
  │          │        │          │          │ │        │       │ DRQ
  │          │        │          │          │ │        │       │  ├──OPENOSINT
  │          │        │          │          │ │        │       │  │  ACTIVE
  │          │        │          │          │ │        │       │  │
  ▼          ▼        ▼          ▼          ▼ ▼        ▼       ▼  ▼
 DORMANT: BUDGET_INTEL (Apr 29) ───────────────────────────────────→
```

**Timeline insights:**
- **Apr–May:** Cyber + Gov Tier2 + Budget Intel active (all now dormant)
- **Jun 13:** Pipeline activated, Media Registry + PRN Johor began
- **Jun 22:** PDRM IO last activity
- **Jul 8–11:** VoronDRQ + OpenOSINT integrated, pipeline infrastructure fixed
- **Current:** Pipeline + PRN Johor + Media Registry + VoronDRQ + OpenOSINT active

---

## 7. Architecture Observations

### 7.1 Strengths
- **Strong pipeline architecture** — automated collection → analysis → briefing chain
- **Config-driven design** — YAML configs enable quick source/narrative changes
- **CVS verification framework** — enforces multi-source truth validation
- **Separation of concerns** — commercial (VoronDRQ) kept in separate repo
- **OpenOSINT as force multiplier** — enhances 4+ workstreams

### 7.2 Weaknesses
- **Root-level clutter** — 31 items at root, many should be subdirectories
- **12 nested git repos without .gitmodules** — fragile submodule management
- **Stale documentation** — STRUCTURE-SUMMARY.md is from Jun 13, missing Jul work
- **6 VoronDRQ directory variants** — sprawl from iterative reorganization
- **Dormant components occupy 60% of tracked files** — Gov Tier2 alone is 144 files
- **No dependency manifest** — Python dependencies scattered across venvs

### 7.3 Coupling Insights
- **INTEL_PIPELINE is the keystone** — highest avg coupling (3.12), most components depend on it
- **OPENOSINT is the force multiplier** — enhances cyber (3.2), gov (3.2), media (3.0), voron (3.8)
- **BUDGET_INTEL is the most isolated** — 1.62 avg, candidate for archival or revival
- **VORON_DRQ is commercially isolated** — 1.72 avg, correctly separated in its own repo
- **PRN_JOHOR ↔ MEDIA_REGISTRY** — 3.4 coupling reflects shared political-media intelligence needs

---

## 8. Reorganization Priorities

See `REORGANIZATION-PLAN.md` for detailed restructuring recommendations.

| Priority | Action | Impact | Effort |
|----------|--------|--------|--------|
| P0 | Fix submodule configuration (add .gitmodules) | High | Low |
| P0 | Consolidate root-level clutter into organized dirs | High | Medium |
| P1 | Consolidate 6 VoronDRQ directories → 1 canonical | Medium | Medium |
| P1 | Update STRUCTURE-SUMMARY.md and WORKSPACE-MANUAL.md | Medium | Low |
| P2 | Archive or revive dormant components | Medium | Medium |
| P2 | Add requirements.txt or pyproject.toml | Low | Low |
| P3 | Consolidate PDRM IO files into dedicated subdirectory | Low | Low |

---

*This document is the master reference for the HOI Intelligence Ops workspace architecture. Update when structural changes occur.*

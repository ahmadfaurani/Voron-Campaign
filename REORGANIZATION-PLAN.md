# HOI Intelligence Ops — Reorganization Plan

**Generated:** 2026-07-11  
**Classification:** TLP:AMBER  
**Companion to:** `ANALYTICAL-WORKSPACE.md`, `ARCHITECTURE.md`

---

## 1. Current State Assessment

### 1.1 Root Directory (31 items)
```
/  (root)
├── .gitignore
├── LICENSE
├── README.md
├── AGENT-SPEC.md              ← 65KB agent specification
├── STRUCTURE-SUMMARY.md       ← STALE (Jun 13)
├── WORKSPACE-MANUAL.md        ← Workspace guide
├── UPLOAD-SUMMARY.md          ← Upload log
├── ANALYTICAL-WORKSPACE.md    ← NEW (this doc set)
├── ARCHITECTURE.md            ← NEW
├── REORGANIZATION-PLAN.md     ← NEW (this file)
├── campaign-operations-manual.md  ← 45KB VoronDRQ manual
├── JOURNALIST-FOCUS-IMPLEMENTATION.md
├── MEDIA-OUTLET-EXPANSION.md
├── BROWSER_AUTOMATION_SETUP.md
├── browser_automation.py
├── OPENOSINT_INSTALLATION_SUMMARY.md
├── OPENOSINT_INTEGRATION.md
├── openosint-activate.sh
├── openosint-targets.txt
├── pdrm-io-100-search-queries.md
├── pdrm-io-automation-guide.md
├── pdrm-io-comprehensive-crawl-guide.md
├── pdrm-io-full-execution-summary.md
├── pdrm-io-search-expansion-summary.md
├── pdrm-io-search-query-list.md
├── N07_Bukit_Kepong_Expanded_Report_20260627.md
├── N07_Bukit_Kepong_Expanded_Report_Part2_20260627.md
├── N07_Bukit_Kepong_Expanded_Report_Part3_20260627.md
├── N07_Bukit_Kepong_Expanded_Report_Part4_20260627.md
├── n27-layang-layang/         ← submodule gitlink
├── briefs/                    ← 1 file (n17-skudai)
├── entities/                  ← 1 file (skudai-n17)
├── constituency-analysis/     ← 2 files
├── collateral/               ← 3 files (VoronDRQ)
├── config/                   ← 5 YAML + 1 summary
├── intelligence/              ← 200+ files
├── models/                   ← 3 files (budget ML)
├── ops/                      ← 157+ files (Tier2)
├── planning/                 ← 6 files
├── prn-johor-2026/           ← 4 files
├── prospects/                ← 2 CSV files
├── reference/                ← 3 files
├── scripts/                  ← 27 files
├── skills/                   ← 4 files
├── sources/                  ← 1 file
├── templates/                ← 2 files
├── voron-campaign/           ← 3 files
├── voron-stakeholders/       ← 7 files (mostly deleted)
├── war-room-reports/         ← 1 file
└── workflows/                ← 4 files
```

### 1.2 Identified Problems

| # | Problem | Severity | Affected Components |
|---|---------|----------|-------------------|
| 1 | **No `.gitmodules`** — gitlink submodules will break on clone | CRITICAL | PRN_JOHOR, INFRA_CONFIG |
| 2 | **Root clutter** — 31 top-level items, 15 are loose files | HIGH | ALL |
| 3 | **6 VoronDRQ directory variants** — sprawl from iterative reorganization | HIGH | VORON_DRQ |
| 4 | **12 nested `.git` repos** without submodule config | HIGH | PRN_JOHOR, VORON_DRQ |
| 5 | **Stale documentation** — STRUCTURE-SUMMARY.md from Jun 13 | MEDIUM | DOCUMENTATION |
| 6 | **PDRM IO files scattered** — root + intelligence/ + scripts/ | MEDIUM | PDRM_IO |
| 7 | **No dependency manifest** — no requirements.txt/pyproject.toml | MEDIUM | INFRA_CONFIG |
| 8 | **Dormant components occupy 48% of tracked files** | LOW | GOV_TIER2, BUDGET_INTEL |
| 9 | **Duplicate N07 reports** — 4 parts at root instead of in constituency-analysis/ | LOW | PRN_JOHOR |

---

## 2. Proposed Target Structure

```
hoi-intelligence-ops/
│
├── .gitignore
├── .gitmodules                    ← NEW: register all submodules
├── LICENSE
├── README.md                      ← UPDATE: reflect new structure
├── AGENT-SPEC.md                  ← Keep at root (agent configuration)
│
├── ANALYTICAL-WORKSPACE.md        ← Master analytical reference
├── ARCHITECTURE.md                ← System architecture map
├── REORGANIZATION-PLAN.md         ← This document
├── STRUCTURE-SUMMARY.md           ← UPDATE: regenerate from current state
├── WORKSPACE-MANUAL.md            ← UPDATE: reflect new structure
│
├── config/                        ← Core configuration (unchanged)
│   ├── sources.yaml
│   ├── pir-definitions.yaml
│   ├── narrative-clusters.yaml
│   ├── sentiment-lexicon.yaml
│   └── MEDIA-EXPANSION-SUMMARY.md
│
├── scripts/                      ← Pipeline scripts (unchanged)
│   ├── collect-political-news.py
│   ├── extract-entities.py
│   ├── sentiment-analysis.py
│   ├── narrative-tracking-analysis.py
│   ├── generate-daily-brief.py
│   ├── discover-media-emails.py
│   ├── discover-emails-fast.py
│   ├── test-journalist-focus.py
│   ├── validate-sources.py
│   └── ... (27 total)
│
├── templates/                    ← Brief templates (unchanged)
│   ├── daily-brief-template.md
│   └── Intel-Brief-Template.md
│
├── intelligence/                  ← Intelligence products
│   ├── briefs/                    ← Daily briefs (INTEL-008 → INTEL-034)
│   ├── narrative-tracking/        ← 6-hourly narrative reports
│   ├── sentiment-analysis/        ← Daily sentiment reports
│   ├── cyber/                     ← MOVED: Intel-Brief-001-007, distribution pkgs
│   │   ├── Intel-Brief-001-Malaysia-Digital-Dependency-2026-04-26.md
│   │   ├── Intel-Brief-003-PhantomRPC-Latest-2026-04-30.md
│   │   ├── ...
│   │   ├── distribution/
│   │   │   ├── DirtyDecrypt-Distribution-Package.md
│   │   │   └── MSFT-Defender-ZeroDays-Distribution-Package.md
│   │   └── Brief-Prof-Rezal-Background-2026-04-30.md
│   ├── media/                     ← MOVED: media intel files
│   │   ├── Malaysian-Media-Intelligence-Database.md
│   │   ├── pdrm-io-contact-database.md
│   │   ├── pdrm-contacts-directory.md
│   │   └── pdrm-io-*.md (12+ files)
│   ├── prn-johor-2026/            ← Submodule (add to .gitmodules)
│   ├── kempas/                    ← Submodule (add to .gitmodules)
│   └── media-registry/            ← Gitignored submodule (journalist registry)
│
├── constituency-analysis/         ← Electoral intelligence
│   ├── n07-bukit-kepong/           ← MOVED: 4 N07 reports
│   │   ├── part1-expanded-report-20260627.md
│   │   ├── part2-expanded-report-20260627.md
│   │   ├── part3-expanded-report-20260627.md
│   │   └── part4-expanded-report-20260627.md
│   ├── 03-pemanis-overview-20260627.md
│   ├── 8-layang-layang-190626.md
│   ├── n17-skudai-analytical-report-2026-06-26.md  ← MOVED from briefs/
│   ├── skudai-n17.md              ← MOVED from entities/
│   ├── bukit-naning-candidate-profile-analysis.md ← MOVED from intelligence/
│   ├── bukit-naning-comprehensive-dossier-20260627.md ← MOVED
│   ├── war-room-reports/          ← MOVED from root
│   │   └── n27-layang-layang-candidate-analysis-270626.md
│   └── prn-johor-2026/            ← MOVED from root (campaign manuals)
│       ├── swing-seats-campaign-manual.md
│       ├── swing-seats-demographic-data.md
│       ├── n47-kempas/
│       │   ├── daily-tracking-report-d12-expanded.md
│       │   └── limitations-remediation-plan.md
│       └── n27-layang-layang/     ← Submodule (add to .gitmodules)
│
├── ops/                           ← Operations (unchanged structure)
│   ├── tier2-intel/               ← 144 agency profiles, execution plans
│   ├── OPERATIONAL_MANUAL.md
│   └── pdrm-io/                   ← NEW: consolidated PDRM IO docs
│       ├── 100-search-queries.md
│       ├── automation-guide.md
│       ├── comprehensive-crawl-guide.md
│       ├── full-execution-summary.md
│       ├── search-expansion-summary.md
│       └── search-query-list.md
│
├── voron/                         ← NEW: consolidated VoronDRQ
│   ├── campaign-operations-manual.md  ← MOVED from root
│   ├── collateral/                ← MOVED from root
│   │   ├── battle-cards.md
│   │   ├── email-templates.md
│   │   └── rmit-compliance-checklist.md
│   ├── prospects/                 ← MOVED from root
│   │   ├── prospect-database-250.csv
│   │   ├── prospect-database-7stakeholders.csv
│   │   └── STAKEHOLDER_ENRICHMENT_PLAN.md
│   ├── scripts/                   ← MOVED from voron-campaign/ + voron-stakeholders/
│   │   ├── enrich-stakeholders.py
│   │   ├── voron-stakeholder-enrichment.sh
│   │   ├── create_cimb_enriched_csv.py
│   │   ├── update_cimb_csv.py
│   │   ├── update_stakeholders_v1.4.py
│   │   ├── push-to-github.sh
│   │   └── collection-cronjob-setup.md
│   ├── Voron-Campaign/            ← Gitignored separate repo
│   └── enrichment/                ← Gitignored (LinkedIn exports, screenshots)
│
├── openosint/                     ← NEW: consolidated OpenOSINT
│   ├── INSTALLATION_SUMMARY.md
│   ├── INTEGRATION.md
│   ├── activate.sh
│   ├── targets.txt
│   └── browser-automation/        ← MOVED from root
│       ├── BROWSER_AUTOMATION_SETUP.md
│       └── browser_automation.py
│
├── workflows/                     ← Budget intel + browser harness
│   ├── GOV-BUDGET-INTELLIGENCE.md
│   ├── budget_pipeline.py
│   ├── BUDGET-INTELLIGENCE-STATUS-REPORT.md
│   └── BROWSER-HARNESS-INTEGRATION.md
│
├── models/                        ← ML models (unchanged)
│   ├── budget_anomaly_detector.py
│   ├── sector_classifier.py
│   └── isolation_forest_20260429_035745.pkl
│
├── planning/                      ← Planning documents (unchanged)
│   ├── HOI-Improvement-Plan-Q2-2026.md
│   ├── offensive-stack-review-20260708.md
│   ├── gateway-fix-report-20260708.md
│   ├── parser-quality-improvement-report-v5.2.md
│   ├── PHASE-1-COMPLETE-2026-06-13.md
│   └── Political-Monitoring-Workstream-Review-2026-06-13.md
│
├── reference/                     ← Reference data (unchanged)
│   ├── key-politicians.md
│   ├── malaysian-political-parties.md
│   └── media-contact-database.md
│
├── skills/                        ← Browser harness skills (unchanged)
│   └── browser-harness/govsec/
│
├── sources/                       ← Source registry (unchanged)
│   └── Source-Registry.md
│
└── UPLOAD-SUMMARY.md              ← Upload log (keep at root)
```

---

## 3. Reorganization Actions

### Phase 1: Critical Fixes (P0)

#### 3.1 Create `.gitmodules`

**Problem:** `intelligence/prn-johor-2026` and `intelligence/kempas` are tracked as gitlinks (160000 mode) but no `.gitmodules` file exists. Cloning the repo will fail to initialize these submodules.

**Action:**
```bash
# Create .gitmodules
cat > .gitmodules << 'EOF'
[submodule "intelligence/prn-johor-2026"]
    path = intelligence/prn-johor-2026
    url = https://github.com/ahmadfaurani/prn-johor-2026.git
    branch = main

[submodule "intelligence/kempas"]
    path = intelligence/kempas
    url = https://github.com/ahmadfaurani/kempas.git
    branch = main

[submodule "constituency-analysis/n27-layang-layang"]
    path = constituency-analysis/n27-layang-layang
    url = https://github.com/ahmadfaurani/n27-layang-layang.git
    branch = main
EOF

git add .gitmodules
git commit -m "fix: add .gitmodules for submodule registration"
```

**Note:** Verify actual remote URLs for each submodule before committing. Run `git submodule status` to check current state.

#### 3.2 Consolidate Root Files

**Problem:** 15 loose files at root level belong in organized subdirectories.

**Actions:**

| File(s) | Current | Target | Component |
|---------|---------|--------|-----------|
| `N07_Bukit_Kepong_Expanded_Report_*.md` (4 files) | `/` | `/constituency-analysis/n07-bukit-kepong/` | PRN_JOHOR |
| `pdrm-io-*.md` (6 files) | `/` | `/ops/pdrm-io/` | PDRM_IO |
| `campaign-operations-manual.md` | `/` | `/voron/` | VORON_DRQ |
| `JOURNALIST-FOCUS-IMPLEMENTATION.md` | `/` | `/intelligence/media/` | MEDIA_REGISTRY |
| `MEDIA-OUTLET-EXPANSION.md` | `/` | `/intelligence/media/` | MEDIA_REGISTRY |
| `BROWSER_AUTOMATION_SETUP.md` | `/` | `/openosint/browser-automation/` | OPENOSINT |
| `browser_automation.py` | `/` | `/openosint/browser-automation/` | OPENOSINT |
| `OPENOSINT_INSTALLATION_SUMMARY.md` | `/` | `/openosint/` | OPENOSINT |
| `OPENOSINT_INTEGRATION.md` | `/` | `/openosint/` | OPENOSINT |
| `openosint-activate.sh` | `/` | `/openosint/` | OPENOSINT |
| `openosint-targets.txt` | `/` | `/openosint/` | OPENOSINT |
| `collateral/` (3 files) | `/collateral/` | `/voron/collateral/` | VORON_DRQ |
| `prospects/` (2 files) | `/prospects/` | `/voron/prospects/` | VORON_DRQ |
| `briefs/n17-skudai-*.md` | `/briefs/` | `/constituency-analysis/` | PRN_JOHOR |
| `entities/skudai-n17.md` | `/entities/` | `/constituency-analysis/` | PRN_JOHOR |
| `war-room-reports/` | `/war-room-reports/` | `/constituency-analysis/war-room-reports/` | PRN_JOHOR |
| `prn-johor-2026/` | `/prn-johor-2026/` | `/constituency-analysis/prn-johor-2026/` | PRN_JOHOR |

---

### Phase 2: VoronDRQ Consolidation (P1)

#### 3.3 Merge 6 VoronDRQ Directory Variants

**Problem:** Six overlapping directories:
1. `voron-stakeholders/` — 7 tracked files (mostly enrichment scripts + 1 CSV)
2. `voron-campaign/` — 3 tracked files (scripts + enrichment plan)
3. `Voron-Campaign/` — separate repo (gitignored)
4. `voron-enrichment/` — gitignored (LinkedIn exports, screenshots)
5. `voron-prospects/` — gitignored (prospect data)
6. `vorondrq-rmit-campaign/` — gitignored (nested .git, 0 tracked files)

**Action:**
```bash
# 1. Create canonical voron/ directory
mkdir -p voron/collateral voron/prospects voron/scripts

# 2. Move tracked files
git mv campaign-operations-manual.md voron/
git mv collateral/* voron/collateral/
git mv prospects/* voron/prospects/
git mv voron-campaign/scripts/* voron/scripts/
git mv voron-campaign/prospects/STAKEHOLDER_ENRICHMENT_PLAN.md voron/prospects/
git mv voron-stakeholders/scripts/* voron/scripts/
git mv voron-stakeholders/collected-pages voron/
git mv voron-stakeholders/prospect-database-enriched-v1.6.csv voron/prospects/

# 3. Remove empty directories
rmdir voron-stakeholders/scripts voron-stakeholders
rmdir voron-campaign/scripts voron-campaign/prospects voron-campaign

# 4. Update .gitignore to reference new paths
# Voron-Campaign/  → voron/Voron-Campaign/
# voron-enrichment/ → voron/enrichment/
# voron-prospects/ → (remove, consolidated)
# vorondrq-rmit-campaign/ → (remove, empty)
```

---

### Phase 3: Intelligence Reorganization (P1)

#### 3.4 Organize Intelligence Files by Domain

**Problem:** Intelligence files are mixed at root of `intelligence/` — cyber briefs, media database, PDRM IO files, and candidate profiles are all at the same level.

**Action:**
```bash
# Cyber intelligence
mkdir -p intelligence/cyber intelligence/cyber/distribution
git mv intelligence/Intel-Brief-001-*.md intelligence/cyber/
git mv intelligence/Intel-Brief-003-*.md intelligence/cyber/
git mv intelligence/Intel-Brief-004-*.md intelligence/cyber/
git mv intelligence/Intel-Brief-005-*.md intelligence/cyber/
git mv intelligence/Intel-Brief-006-*.md intelligence/cyber/
git mv intelligence/Intel-Brief-007-*.md intelligence/cyber/
git mv intelligence/Brief-Prof-Rezal-*.md intelligence/cyber/
git mv intelligence/DISTRIBUTION/* intelligence/cyber/distribution/
rmdir intelligence/DISTRIBUTION

# Media intelligence
mkdir -p intelligence/media
git mv intelligence/Malaysian-Media-Intelligence-Database.md intelligence/media/
git mv intelligence/pdrm-io-*.md intelligence/media/
git mv intelligence/pdrm-contacts-directory.md intelligence/media/

# Electoral intelligence → constituency-analysis
git mv intelligence/bukit-naning-candidate-profile-analysis.md constituency-analysis/
git mv intelligence/bukit-naning-comprehensive-dossier-20260627.md constituency-analysis/
```

---

### Phase 4: Documentation Refresh (P1)

#### 3.5 Update STRUCTURE-SUMMARY.md and WORKSPACE-MANUAL.md

**Problem:** Both documents are stale (Jun 13), do not reflect:
- 30 new daily briefs (INTEL-027 → INTEL-034)
- 96 narrative tracking reports
- 44 sentiment analysis reports
- OpenOSINT integration
- VoronDRQ consolidation
- Analytical workspace documents

**Action:** Regenerate from current `git ls-files` output and this reorganization plan.

#### 3.6 Update README.md

**Problem:** README does not reference the analytical workspace or architecture documents.

**Action:** Add links to `ANALYTICAL-WORKSPACE.md`, `ARCHITECTURE.md`, and `REORGANIZATION-PLAN.md`.

---

### Phase 5: Dormant Component Management (P2)

#### 3.7 GOV_TIER2 — Keep or Archive?

**Current state:** 144 agency profiles + execution plans + source scripts. Last active May 10, 2026.

**Options:**

| Option | Pro | Con | Recommendation |
|--------|-----|-----|----------------|
| **Keep in place** | No disruption, profiles remain accessible | 34% of repo for dormant content | ✅ Keep — profiles are reference data |
| **Archive to branch** | Cleans main branch | Loses easy access | ❌ Profiles have long-term reference value |
| **Move to `archive/`** | Signals dormant status | Breaks references | Consider if repo grows >1000 files |

**Recommendation:** Keep in place. The 144 agency profiles are reference data with long-term value. Add a `STATUS.md` to `ops/tier2-intel/` noting dormant status and last active date.

#### 3.8 BUDGET_INTEL — Revive or Archive?

**Current state:** 3 Python files + 1 ML model + 3 docs. Last active Apr 29, 2026. Most isolated component (1.62 avg coupling).

**Options:**

| Option | Pro | Con | Recommendation |
|--------|-----|-----|----------------|
| **Keep in place** | No disruption | 1% of repo, dormant 3 months | ✅ Keep — low overhead |
| **Revive with new data** | Potential high value | Requires data pipeline work | Consider if budget cycle restarts |
| **Archive** | Signals dormant | Loses model artifacts | ❌ Model pickle is valuable |

**Recommendation:** Keep in place. The `isolation_forest` model is a trained artifact worth preserving. Add `STATUS.md` to `workflows/` noting dormant status.

#### 3.9 PDRM_IO — Revive or Archive?

**Current state:** 34 files across root + intelligence/ + scripts/. Last active Jun 22, 2026.

**Recommendation:** Consolidate into `ops/pdrm-io/` (Phase 1 action). The contact database has long-term reference value. Mark as dormant in `ops/pdrm-io/STATUS.md`.

#### 3.10 CYBER_INTEL — Keep or Archive?

**Current state:** 10 files. Last active May 21, 2026. Low coupling (1.88 avg).

**Recommendation:** Move to `intelligence/cyber/` (Phase 3 action). The Intel Briefs 001-007 are completed assessments with reference value. Mark as dormant in `intelligence/cyber/STATUS.md`.

---

### Phase 6: Infrastructure Hardening (P2)

#### 3.11 Add Dependency Manifest

**Problem:** No `requirements.txt` or `pyproject.toml`. Python dependencies scattered across multiple venvs.

**Action:** Create `requirements.txt` from the most common imports across scripts:
```
# Core pipeline
firecrawl-py>=1.0.0
vaderSentiment>=3.3.2
pyyaml>=6.0
requests>=2.28.0

# Entity extraction
spacy>=3.5.0
nltk>=3.8.0

# Browser automation
playwright>=1.40.0

# Data processing
pandas>=2.0.0
python-dotenv>=1.0.0

# Budget intelligence (dormant)
scikit-learn>=1.3.0
```

#### 3.12 Add STATUS.md to Dormant Components

Create status files for each dormant component:

```markdown
# Component Status: [NAME]
**Status:** DORMANT
**Last Active:** [DATE]
**Reason:** [WHY]
**Files:** [COUNT]
**Revival Plan:** [CONDITIONS TO RESTART]
```

---

## 4. Execution Sequence

```
Phase 1 (P0 — Critical)
├── 3.1  Create .gitmodules                    [~30 min]
├── 3.2  Consolidate root files                [~1 hour]
│
Phase 2 (P1 — High)
├── 3.3  Merge 6 VoronDRQ directories          [~45 min]
├── 3.4  Organize intelligence/ by domain      [~30 min]
├── 3.5  Update STRUCTURE-SUMMARY.md           [~30 min]
├── 3.6  Update README.md                      [~15 min]
│
Phase 3 (P2 — Medium)
├── 3.7  GOV_TIER2 status doc                  [~10 min]
├── 3.8  BUDGET_INTEL status doc               [~10 min]
├── 3.9  PDRM_IO consolidation + status        [~20 min]
├── 3.10 CYBER_INTEL status doc                [~10 min]
├── 3.11 Add requirements.txt                  [~15 min]
└── 3.12 Add STATUS.md files                   [~30 min]

Total estimated effort: ~5 hours
```

---

## 5. Component Relevance Score Summary

### 5.1 Coupling Matrix (Full)

Scores 0.0–5.0. Higher = more coupled.

```
                  INTEL  PRN   CYBER  GOV   PDRM  MEDIA  VORON  OSINT  BUDGET  INFRA  DOC
INTEL_PIPELINE      —    4.4   2.8   2.8   3.0   3.6   1.8   3.0   2.4   4.6   2.8
PRN_JOHOR          4.4    —    1.0   2.8   1.6   3.4   1.2   2.4   1.8   3.6   2.2
CYBER_INTEL        2.8   1.0    —    2.8   1.8   1.0   0.8   3.2   1.4   2.6   1.4
GOV_TIER2          2.8   2.8   2.8    —    2.8   2.6   1.4   3.2   3.2   3.2   1.6
PDRM_IO            3.0   1.6   1.8   2.8    —    2.6   1.0   2.8   0.8   2.6   1.4
MEDIA_REGISTRY     3.6   3.4   1.0   2.6   2.6    —    2.0   3.0   0.8   2.8   2.2
VORON_DRQ          1.8   1.2   0.8   1.4   1.0   2.0    —    3.8   1.2   2.6   1.4
OPENOSINT          3.0   2.4   3.2   3.2   2.8   3.0   3.8    —    1.6   3.0   1.8
BUDGET_INTEL       2.4   1.8   1.4   3.2   0.8   0.8   1.2   1.6    —    2.0   1.0
INFRA_CONFIG       4.6   3.6   2.6   3.2   2.6   2.8   2.6   3.0   2.0    —    3.0
DOCUMENTATION      2.8   2.2   1.4   1.6   1.4   2.2   1.4   1.8   1.0   3.0    —
```

### 5.2 Component Coupling Strength Ranking

| Rank | Component | Avg Score | Role | Architecture Action |
|------|-----------|-----------|------|---------------------|
| 1 | **INTEL_PIPELINE** | 3.12 | Backbone | Keep at `scripts/` + `intelligence/briefs/` |
| 2 | **INFRA_CONFIG** | 3.00 | Foundation | Keep at `config/` + `planning/` |
| 3 | **OPENOSINT** | 2.78 | Force multiplier | Consolidate to `openosint/` |
| 4 | **GOV_TIER2** | 2.64 | Dormant hub | Keep at `ops/tier2-intel/` |
| 5 | **PRN_JOHOR** | 2.44 | Active operational | Consolidate to `constituency-analysis/` |
| 6 | **MEDIA_REGISTRY** | 2.40 | Active support | Consolidate to `intelligence/media/` |
| 7 | **PDRM_IO** | 2.04 | Dormant specialist | Consolidate to `ops/pdrm-io/` |
| 8 | **DOCUMENTATION** | 1.88 | Stale meta | Update all docs |
| 8 | **CYBER_INTEL** | 1.88 | Dormant specialist | Move to `intelligence/cyber/` |
| 10 | **VORON_DRQ** | 1.72 | Commercial isolate | Consolidate to `voron/` |
| 11 | **BUDGET_INTEL** | 1.62 | Most isolated | Keep at `workflows/` + `models/` |

### 5.3 Architectural Clusters

Based on the coupling analysis, three natural clusters emerge:

**Cluster A: Political Intelligence Core** (avg intra-cluster: 3.7)
- INTEL_PIPELINE ↔ PRN_JOHOR (4.4)
- INTEL_PIPELINE ↔ MEDIA_REGISTRY (3.6)
- PRN_JOHOR ↔ MEDIA_REGISTRY (3.4)
- INTEL_PIPELINE ↔ INFRA_CONFIG (4.6)

→ These components should be co-located and co-versioned. The pipeline feeds political intelligence which feeds media registry needs.

**Cluster B: OSINT Verification Network** (avg intra-cluster: 3.2)
- VORON_DRQ ↔ OPENOSINT (3.8)
- CYBER_INTEL ↔ OPENOSINT (3.2)
- GOV_TIER2 ↔ OPENOSINT (3.2)

→ OpenOSINT serves as a shared verification layer. Consolidating its files to `openosint/` makes this explicit.

**Cluster C: Government Intelligence** (avg intra-cluster: 3.0)
- GOV_TIER2 ↔ BUDGET_INTEL (3.2)
- GOV_TIER2 ↔ INFRA_CONFIG (3.2)

→ Government intelligence components share domain knowledge. Keeping GOV_TIER2 at `ops/` and BUDGET_INTEL at `workflows/`+`models/` is appropriate.

**Isolated:** PDRM_IO (2.04 avg), DOCUMENTATION (1.88), VORON_DRQ (1.72), BUDGET_INTEL (1.62) — these have specialized domains with limited cross-component data flow.

---

## 6. Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Submodule URLs incorrect in .gitmodules | Medium | High | Verify with `git remote -v` in each submodule |
| Git history breaks during `git mv` | Low | High | All moves are reversible; commit in small batches |
| Script import paths break after reorganization | Medium | Medium | Scripts use relative paths; update if needed |
| Cron jobs reference old paths | Medium | High | Audit Hermes cron job configs for path references |
| Nested repos lose their remotes | Low | Medium | `.gitignore` already protects these; verify after moves |

---

## 7. Post-Reorganization Verification

```bash
# Verify all submodules initialize
git submodule update --init --recursive

# Verify no broken symlinks or missing files
git fsck --full

# Verify all tracked files are in expected locations
git ls-files | sort > /tmp/new-structure.txt
diff /tmp/old-structure.txt /tmp/new-structure.txt

# Verify cron jobs still reference correct paths
# (audit Hermes cron config for hoi-intelligence-ops paths)

# Verify scripts can find their config files
cd scripts/ && python3 -c "import yaml; yaml.safe_load(open('../config/sources.yaml'))"
```

---

*This plan is the roadmap for restructuring HOI Intelligence Ops. Execute phases in order; commit after each phase for safe rollback.*

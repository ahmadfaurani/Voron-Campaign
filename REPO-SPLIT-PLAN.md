# HOI Intelligence Ops — Repository Split Execution Plan

**Generated:** 2026-07-11  
**Classification:** TLP:AMBER  
**Companion to:** `ANALYTICAL-WORKSPACE.md`, `ARCHITECTURE.md`, `REORGANIZATION-PLAN.md`  
**Status:** PLANNING — Awaits user approval

---

## 1. Executive Summary

Split the `hoi-intelligence-ops` monorepo (463 files, 11 components) into **6 workstream-aligned repositories**, preserving git history for each component. The split is guided by the cross-relevance matrix: tightly coupled components stay together, loosely coupled components separate cleanly.

**Principle:** Each repo owns its own scripts, config, and outputs. Cross-repo dependencies are explicit (submodules or documented references).

---

## 2. Current State: Existing Repos on GitHub

Several workstream repos **already exist** on GitHub. The split plan must account for these:

| Existing Repo | Visibility | Purpose | Overlap with Monorepo |
|---------------|-----------|---------|----------------------|
| `ahmadfaurani/Voron-Campaign` | PUBLIC | VoronDRQ commercial intel | `campaign-operations-manual.md`, `collateral/`, `prospects/` — **already a clone** inside monorepo |
| `ahmadfaurani/malaysia-journalist-registry` | PRIVATE | Media relationship intelligence | `intelligence/media-registry/` submodule — **already linked** |
| `ahmadfaurani/PRN-Johor-2026-H` | PRIVATE | PRN Johor political intel | `intelligence/prn-johor-2026/` — **already a submodule** |
| `ahmadfaurani/N47---Kempas.-H` | PRIVATE | N47 Kempas constituency | `intelligence/kempas/` — **already a submodule** |
| `ahmadfaurani/N27---Layang-Layang.-H` | PRIVATE | N27 Layang-Layang | `n27-layang-layang/` — **already a submodule** |
| `ahmadfaurani/narrative-tracking-hoi` | PRIVATE | Narrative tracking | Overlaps `intelligence/narrative-tracking/` (96 files) |
| `ahmadfaurani/prn-johor-2026-cron` | PRIVATE | Cron job configs | Overlaps cron-related planning |
| `ahmadfaurani/HOI-Intelligence-Operations` | PUBLIC | Tier2 gov agency intel | Overlaps `ops/tier2-intel/` (157 files) — **this is the public version** |
| 30+ constituency repos | PRIVATE | Individual DUN seats | `n03-pemanis`, `n07-bukit-kepong`, `n14-bukit-naning`, etc. |

**Key insight:** The monorepo is already a hub that aggregates submodules + standalone work. The split formalizes this pattern.

---

## 3. Target Repository Architecture

### 3.1 Repository Map

```
                    ┌──────────────────────────────┐
                    │  hoi-intelligence-ops (CORE) │
                    │  Slim pipeline + config hub   │
                    │  ~160 files (down from 463)   │
                    └──────────────┬───────────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    │              │              │
                    ▼              ▼              ▼
          ┌────────────────┐ ┌──────────────┐ ┌──────────────────┐
          │ SUBMODULE       │ │ SUBMODULE    │ │ SUBMODULE        │
          │ prn-johor-2026  │ │ media-       │ │ narrative-       │
          │ -political      │ │ registry    │ │ tracking          │
          │ (EXISTING:      │ │ (EXISTING:  │ │ (EXISTING:        │
          │  PRN-Johor-     │ │  malaysia-  │ │  narrative-       │
          │  2026-H)        │ │  journalist-│ │  tracking-hoi)    │
          │                 │ │  registry)  │ │                   │
          └───────┬────────┘ └──────────────┘ └──────────────────┘
                  │
          ┌───────┼──────────────────────────────┐
          │       │      │      │      │         │
          ▼       ▼      ▼      ▼      ▼         ▼
       [N47]   [N27]  [N51]  [N03]  [N07]   [20+ more
       Kempas  Layang Batu  Pemanis Kepong  constituency
                                  repos]
                  
     ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
     │ Voron-Campaign   │  │ gov-intel        │  │ pdrm-io          │
     │ (EXISTING:       │  │ (EXISTING:       │  │ (NEW)             │
     │  Voron-Campaign) │  │  HOI-Intelligence│  │                   │
     │                  │  │  -Operations)   │  │                   │
     │ PUBLIC → PRIVATE │  │ PUBLIC → PRIVATE│  │ PRIVATE           │
     └──────────────────┘  └──────────────────┘  └──────────────────┘

     ┌──────────────────┐
     │ cyber-intel      │
     │ (NEW)             │
     │ PRIVATE           │
     └──────────────────┘
     
     ┌──────────────────┐
     │ openosint-config  │
     │ (NEW or stays in  │
     │  core as config)  │
     └──────────────────┘
```

### 3.2 Repository Specifications

---

#### Repo 1: `hoi-intelligence-ops` (SLIM CORE — stays)

**Purpose:** Automated intelligence pipeline + configuration hub  
**Coupling score:** 3.12 avg (keystone — serves all workstreams)  
**Existing:** ✅ This is the current repo, trimmed to ~160 files

**Contents:**
```
hoi-intelligence-ops/
├── .gitignore
├── .gitmodules                    ← NEW: register all submodules
├── LICENSE
├── README.md                      ← UPDATE: document new architecture
├── AGENT-SPEC.md
├── ANALYTICAL-WORKSPACE.md
├── ARCHITECTURE.md
├── REORGANIZATION-PLAN.md
├── REPO-SPLIT-PLAN.md             ← This file
├── STRUCTURE-SUMMARY.md           ← UPDATE
├── WORKSPACE-MANUAL.md            ← UPDATE
│
├── config/                        ← Core pipeline configuration
│   ├── sources.yaml
│   ├── pir-definitions.yaml
│   ├── narrative-clusters.yaml
│   └── sentiment-lexicon.yaml
│
├── scripts/                       ← Pipeline scripts ONLY
│   ├── collect-news.sh
│   ├── collect-political-news.py
│   ├── daily-collection-12outlets.py
│   ├── daily-collection-run.sh
│   ├── entity-extraction-run.py
│   ├── extract-entities.py
│   ├── extract-entities-latest.py
│   ├── generate-daily-brief.py
│   ├── narrative-tracking-analysis.py
│   ├── run-sentiment-analysis.py
│   ├── sentiment-analysis.py
│   ├── scrape_spr_2023_results.py
│   ├── validate-sources.py
│   ├── test_api.py
│   └── test-new-sources.py
│
├── templates/                     ← Brief templates
│   ├── daily-brief-template.md
│   └── Intel-Brief-Template.md
│
├── intelligence/                  ← Pipeline outputs (stays in core)
│   ├── briefs/                    ← Daily briefs INTEL-008 → INTEL-034
│   ├── narrative-tracking/        ← 96 reports → SUBMODULE to narrative-tracking-hoi
│   ├── sentiment-analysis/        ← 44 sentiment reports
│   ├── prn-johor-2026/            ← SUBMODULE (existing: PRN-Johor-2026-H)
│   └── kempas/                    ← SUBMODULE (existing: N47-Kempas-H)
│
├── planning/                      ← Infrastructure planning
│   ├── HOI-Improvement-Plan-Q2-2026.md
│   ├── offensive-stack-review-20260708.md
│   ├── gateway-fix-report-20260708.md
│   ├── parser-quality-improvement-report-v5.2.md
│   ├── PHASE-1-COMPLETE-2026-06-13.md
│   └── Political-Monitoring-Workstream-Review-2026-06-13.md
│
├── reference/                     ← Pipeline reference data
│   ├── key-politicians.md
│   └── malaysian-political-parties.md
│
├── sources/
│   └── Source-Registry.md
│
└── openosint/                     ← OpenOSINT config (stays in core)
    ├── INTEGRATION.md
    ├── INSTALLATION_SUMMARY.md
    ├── activate.sh
    ├── targets.txt
    └── browser-automation/
        ├── BROWSER_AUTOMATION_SETUP.md
        └── browser_automation.py
```

**Files removed from core:** ~303 (moved to other repos or already in submodules)
**Files remaining:** ~160

---

#### Repo 2: `PRN-Johor-2026-H` (EXISTING — expand)

**Purpose:** Electoral intelligence for Johor 2026  
**Coupling score:** 2.44 avg  
**Existing:** ✅ Already a submodule at `intelligence/prn-johor-2026/`  
**Action:** Absorb all constituency-analysis files from monorepo root

**Files to move INTO this repo:**
```
FROM monorepo → INTO PRN-Johor-2026-H:
├── constituency-analysis/
│   ├── 03-pemanis-overview-20260627.md
│   ├── 8-layang-layang-190626.md
│   ├── n17-skudai-analytical-report-2026-06-26.md  ← from briefs/
│   ├── skudai-n17.md                              ← from entities/
│   ├── bukit-naning-candidate-profile-analysis.md ← from intelligence/
│   ├── bukit-naning-comprehensive-dossier-20260627.md
│   ├── n07-bukit-kepong/                          ← 4 N07 reports from root
│   └── war-room-reports/
│       └── n27-layang-layang-candidate-analysis-270626.md
├── prn-johor-2026/                                ← from monorepo root
│   ├── swing-seats-campaign-manual.md
│   ├── swing-seats-demographic-data.md
│   └── n47-kempas/
│       ├── daily-tracking-report-d12-expanded.md
│       └── limitations-remediation-plan.md
└── n27-layang-layang/                             ← already submodule
```

**Submodules this repo owns:**
- `N47---Kempas.-H` (existing)
- `N27---Layang-Layang.-H` (existing)
- 30+ individual constituency repos (can be submodules or merged)

---

#### Repo 3: `malaysia-journalist-registry` (EXISTING — expand)

**Purpose:** Media intelligence & journalist registry  
**Coupling score:** 2.40 avg  
**Existing:** ✅ Already at `intelligence/media-registry/` (gitignored submodule)  
**Action:** Absorb media intelligence files from monorepo

**Files to move INTO this repo:**
```
FROM monorepo → INTO malaysia-journalist-registry:
├── Malaysian-Media-Intelligence-Database.md      ← from intelligence/
├── JOURNALIST-FOCUS-IMPLEMENTATION.md             ← from root
├── MEDIA-OUTLET-EXPANSION.md                      ← from root
├── config/MEDIA-EXPANSION-SUMMARY.md              ← from config/
├── reference/media-contact-database.md            ← from reference/
└── scripts/
    ├── discover-media-emails.py                   ← from scripts/
    ├── discover-emails-fast.py                    ← from scripts/
    └── test-journalist-focus.py                   ← from scripts/
```

---

#### Repo 4: `Voron-Campaign` (EXISTING — consolidate)

**Purpose:** VoronDRQ commercial GRC intelligence  
**Coupling score:** 1.72 avg (lowest — cleanest separation)  
**Existing:** ✅ Already a clone at `Voron-Campaign/` (gitignored)  
**Action:** Absorb all VoronDRQ files, flip PUBLIC → PRIVATE

**Files to move INTO this repo:**
```
FROM monorepo → INTO Voron-Campaign:
├── campaign-operations-manual.md                  ← from root (already in Voron-Campaign)
├── collateral/                                    ← from root (already in Voron-Campaign)
│   ├── battle-cards.md
│   ├── email-templates.md
│   └── rmit-compliance-checklist.md
├── prospects/                                     ← from root (already in Voron-Campaign)
│   ├── prospect-database-250.csv
│   ├── prospect-database-7stakeholders.csv
│   └── STAKEHOLDER_ENRICHMENT_PLAN.md             ← from voron-campaign/
├── scripts/                                       ← NEW: merge from multiple dirs
│   ├── enrich-stakeholders.py                     ← from voron-campaign/scripts/
│   ├── voron-stakeholder-enrichment.sh            ← from voron-campaign/scripts/
│   ├── create_cimb_enriched_csv.py                ← from voron-stakeholders/scripts/
│   ├── update_cimb_csv.py                         ← from voron-stakeholders/scripts/
│   ├── update_stakeholders_v1.4.py                ← from voron-stakeholders/scripts/
│   ├── push-to-github.sh                           ← from voron-stakeholders/scripts/
│   └── collection-cronjob-setup.md                ← from voron-stakeholders/scripts/
└── collected-pages/
    └── maybank-leaders-20260709.md                ← from voron-stakeholders/
```

**Security action:** Flip `Voron-Campaign` from PUBLIC to PRIVATE:
```bash
gh repo edit ahmadfaurani/Voron-Campaign --visibility private --accept-visibility-change-consequences
```

---

#### Repo 5: `gov-intel` (NEW — or rename `HOI-Intelligence-Operations`)

**Purpose:** Government agency intelligence + budget analysis  
**Coupling score:** GOV_TIER2 2.64, BUDGET_INTEL 1.62  
**Existing:** `HOI-Intelligence-Operations` (PUBLIC) — rename to `gov-intel` and make PRIVATE  
**Action:** Move Tier2 + Budget Intel content

**Files to move INTO this repo:**
```
FROM monorepo → INTO gov-intel:
├── ops/
│   ├── tier2-intel/                                ← 157 files (144 profiles + plans + scripts)
│   │   ├── evidence/Agency-Profiles/                ← 144 agency profiles
│   │   ├── execution/                              ← Master execution plan, contingency plan
│   │   ├── planning/                               ← OSINT process optimization
│   │   ├── research/                               ← Crawler optimization, process refinement
│   │   ├── sources/                                ← 4 source scripts
│   │   ├── Collection-Plan-Tier2-Intel.md
│   │   ├── SOP-Phase1-Collection.md
│   │   ├── Top20-Enrichment-Queue.md
│   │   ├── progress-dashboard.md
│   │   └── Quality-Scoring-Dashboard.md
│   └── OPERATIONAL_MANUAL.md
├── workflows/                                      ← Budget intelligence
│   ├── GOV-BUDGET-INTELLIGENCE.md
│   ├── budget_pipeline.py
│   ├── BUDGET-INTELLIGENCE-STATUS-REPORT.md
│   └── BROWSER-HARNESS-INTEGRATION.md
├── models/                                         ← ML models
│   ├── budget_anomaly_detector.py
│   ├── sector_classifier.py
│   └── isolation_forest_20260429_035745.pkl
└── skills/
    └── browser-harness/govsec/                      ← 4 files
```

**Security action:** Flip `HOI-Intelligence-Operations` from PUBLIC to PRIVATE:
```bash
gh repo edit ahmadfaurani/HOI-Intelligence-Operations --visibility private --accept-visibility-change-consequences
```

---

#### Repo 6: `cyber-intel` (NEW)

**Purpose:** Cybersecurity intelligence briefs  
**Coupling score:** 1.88 avg (standalone domain)  
**Existing:** ❌ New repo  
**Action:** Create and move cyber intel files

**Files to move INTO this repo:**
```
FROM monorepo → INTO cyber-intel:
├── Intel-Brief-001-Malaysia-Digital-Dependency-2026-04-26.md
├── Intel-Brief-003-PhantomRPC-Latest-2026-04-30.md
├── Intel-Brief-004-KazSign-PQC-2026-04-30.md
├── Intel-Brief-005-Thunderbolt-Mozilla-2026-05-01.md
├── Intel-Brief-006-ml-intern-HuggingFace-2026-05-01.md
├── Intel-Brief-007-Threat-Actor-Registry-Webworm-2026-05-21.md
├── Brief-Prof-Rezal-Background-2026-04-30.md
└── distribution/
    ├── DirtyDecrypt-Distribution-Package.md
    └── MSFT-Defender-ZeroDays-Distribution-Package.md
```

---

#### Repo 7: `pdrm-io` (NEW)

**Purpose:** PDRM Information Operations  
**Coupling score:** 2.04 avg  
**Existing:** ❌ New repo  
**Action:** Create and consolidate all PDRM IO files

**Files to move INTO this repo:**
```
FROM monorepo → INTO pdrm-io:
├── docs/
│   ├── 100-search-queries.md                       ← from root
│   ├── automation-guide.md                         ← from root
│   ├── comprehensive-crawl-guide.md               ← from root
│   ├── full-execution-summary.md                  ← from root
│   ├── search-expansion-summary.md                ← from root
│   └── search-query-list.md                       ← from root
├── intelligence/
│   ├── contact-database.md                         ← from intelligence/pdrm-io-*
│   ├── contacts-directory.md                      ← from intelligence/pdrm-*
│   ├── comprehensive-direct-summary.md
│   ├── comprehensive-v5-summary.md
│   ├── consolidated-v2.md
│   ├── contact-distribution-analysis.md
│   ├── contact-review-analysis.md
│   ├── direct-seen-urls.txt
│   ├── expanded-search-summary.md
│   ├── extraction-summary.md
│   ├── playwright-summary.md
│   ├── test-seen-urls.txt
│   ├── v5-seen-urls.txt
│   └── browser-automation-final.md
└── scripts/
    ├── browser-automation.py
    ├── comprehensive-crawler.py
    ├── comprehensive-direct.py
    ├── extractor-v5.py
    ├── firecrawl-extraction.py
    ├── firecrawl-v2.py
    ├── playwright-automation.py
    ├── playwright-v2.py
    └── test-tier1.py
```

---

## 4. File Migration Summary

| Target Repo | Source Location | File Count | Method |
|-------------|-----------------|------------|--------|
| `PRN-Johor-2026-H` | Root + intelligence/ + briefs/ + entities/ | ~15 | `git mv` + push to submodule |
| `malaysia-journalist-registry` | Root + intelligence/ + config/ + reference/ + scripts/ | ~7 | `git mv` + push to submodule |
| `Voron-Campaign` | Root + collateral/ + prospects/ + voron-*/ | ~14 | Copy (already partially in repo) |
| `gov-intel` | ops/ + workflows/ + models/ + skills/ | ~165 | `git subtree split` |
| `cyber-intel` | intelligence/ (Intel-Briefs + DISTRIBUTION) | ~10 | `git subtree split` |
| `pdrm-io` | Root + intelligence/ + scripts/ | ~34 | `git subtree split` |
| **Core (stays)** | scripts/ + config/ + templates/ + intelligence/briefs/ + planning/ | ~160 | Trim monorepo |

---

## 5. Execution Sequence

### Phase 1: Pre-Split Preparation (30 min)

```bash
# 1.1 Verify clean working tree
cd /home/p62operator/.openclaw/workspace-hoi/
git status --short  # must be empty

# 1.2 Create backup branch
git branch backup-pre-split

# 1.3 Record current file list for verification
git ls-files | sort > /tmp/pre-split-filelist.txt

# 1.4 Verify all submodule remotes are accessible
git submodule foreach 'git remote -v'
```

### Phase 2: Execute Step 1 Reorganization (1 hour)

Execute the directory consolidation from `REORGANIZATION-PLAN.md` Phase 1-3:
- Consolidate root files into organized directories
- Merge VoronDRQ directories
- Organize intelligence/ by domain

This creates clean directory boundaries that map 1:1 to target repos.

### Phase 3: Split Repositories (2-3 hours)

Split in **reverse priority order** — lowest coupling first (safest):

#### 3.1 Split `cyber-intel` (lowest risk — 10 files, 1.88 coupling, dormant)

```bash
cd /home/p62operator/.openclaw/workspace-hoi/

# Create new GitHub repo
gh repo create ahmadfaurani/cyber-intel --private --description "Cybersecurity Intelligence — TLP:AMBER"

# Extract files with history using git subtree
git subtree split --prefix=intelligence/cyber -b cyber-intel-branch

# Push to new repo
git push https://github.com/ahmadfaurani/cyber-intel.git cyber-intel-branch:main

# Remove from monorepo
git rm -r intelligence/cyber/
git commit -m "split: extract cyber-intel to separate repo"

# Clean up temp branch
git branch -D cyber-intel-branch
```

#### 3.2 Split `pdrm-io` (34 files, 2.04 coupling, dormant)

```bash
# Create new GitHub repo
gh repo create ahmadfaurani/pdrm-io --private --description "PDRM Information Operations — TLP:AMBER"

# Extract with history
git subtree split --prefix=ops/pdrm-io -b pdrm-io-branch
git push https://github.com/ahmadfaurani/pdrm-io.git pdrm-io-branch:main

# Remove from monorepo
git rm -r ops/pdrm-io/
git commit -m "split: extract pdrm-io to separate repo"
git branch -D pdrm-io-branch
```

#### 3.3 Split `gov-intel` (165 files, 2.64 coupling, dormant)

```bash
# Rename existing public repo and make private
gh repo edit ahmadfaurani/HOI-Intelligence-Operations --visibility private --accept-visibility-change-consequences
gh repo rename gov-intel --repo ahmadfaurani/HOI-Intelligence-Operations
# OR create new:
# gh repo create ahmadfaurani/gov-intel --private

# Extract with history
git subtree split --prefix=ops -b gov-intel-branch
git push https://github.com/ahmadfaurani/gov-intel.git gov-intel-branch:main

# Remove from monorepo
git rm -r ops/ workflows/ models/ skills/
git commit -m "split: extract gov-intel (ops, workflows, models, skills) to separate repo"
git branch -D gov-intel-branch
```

#### 3.4 Consolidate `Voron-Campaign` (14 files, 1.72 coupling)

```bash
# Flip public → private
gh repo edit ahmadfaurani/Voron-Campaign --visibility private --accept-visibility-change-consequences

# Copy remaining tracked files into Voron-Campaign clone
cd /home/p62operator/.openclaw/workspace-hoi/Voron-Campaign/
cp ../campaign-operations-manual.md .  # if not already there
cp -r ../collateral/* collateral/
cp -r ../prospects/* prospects/
cp -r ../voron-stakeholders/scripts/* scripts/
cp ../voron-stakeholders/collected-pages/ collected-pages/

# Commit and push
git add -A
git commit -m "consolidate: absorb all VoronDRQ files from monorepo"
git push origin main

# Remove from monorepo
cd /home/p62operator/.openclaw/workspace-hoi/
git rm campaign-operations-manual.md
git rm -r collateral/ prospects/ voron-stakeholders/ voron-campaign/
git commit -m "split: VoronDRQ files consolidated to Voron-Campaign repo"
```

#### 3.5 Expand `PRN-Johor-2026-H` (submodule — push files into it)

```bash
# Enter submodule
cd /home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/

# Copy constituency files from parent
cp ../../constituency-analysis/ . -r
cp ../../N07_Bukit_Kepong_*.md ./constituency-analysis/n07-bukit-kepong/
cp ../../briefs/n17-skudai-analytical-report-2026-06-26.md ./constituency-analysis/
cp ../../entities/skudai-n17.md ./constituency-analysis/
cp ../../war-room-reports/ ./constituency-analysis/ -r
cp ../../intelligence/bukit-naning-*.md ./constituency-analysis/
cp -r ../../prn-johor-2026/ ./constituency-analysis/prn-johor-2026/

# Commit and push
git add -A
git commit -m "consolidate: absorb constituency analysis from monorepo"
git push origin main

# Remove from parent monorepo
cd /home/p62operator/.openclaw/workspace-hoi/
git rm -r constituency-analysis/ prn-johor-2026/ war-room-reports/ briefs/ entities/
git rm intelligence/bukit-naning-*.md N07_Bukit_Kepong_*.md
git commit -m "split: constituency analysis moved to PRN-Johor-2026-H submodule"
```

#### 3.6 Expand `malaysia-journalist-registry` (submodule)

```bash
# Enter submodule (currently gitignored — unignore first)
cd /home/p62operator/.openclaw/workspace-hoi/intelligence/media-registry/

# Copy media intelligence files from parent
cp ../../intelligence/Malaysian-Media-Intelligence-Database.md .
cp ../../JOURNALIST-FOCUS-IMPLEMENTATION.md .
cp ../../MEDIA-OUTLET-EXPANSION.md .
cp ../../config/MEDIA-EXPANSION-SUMMARY.md .
cp ../../reference/media-contact-database.md .
mkdir -p scripts/
cp ../../scripts/discover-media-emails.py scripts/
cp ../../scripts/discover-emails-fast.py scripts/
cp ../../scripts/test-journalist-focus.py scripts/

# Commit and push
git add -A
git commit -m "consolidate: absorb media intelligence from monorepo"
git push origin main

# Remove from parent monorepo
cd /home/p62operator/.openclaw/workspace-hoi/
git rm intelligence/Malaysian-Media-Intelligence-Database.md
git rm JOURNALIST-FOCUS-IMPLEMENTATION.md MEDIA-OUTLET-EXPANSION.md
git rm config/MEDIA-EXPANSION-SUMMARY.md
git rm reference/media-contact-database.md
git rm scripts/discover-media-emails.py scripts/discover-emails-fast.py scripts/test-journalist-focus.py
git commit -m "split: media intelligence moved to malaysia-journalist-registry submodule"
```

### Phase 4: Core Repo Cleanup (30 min)

```bash
# 4.1 Update .gitmodules
# Add entries for any new submodules
# Ensure all existing submodule entries are correct

# 4.2 Update .gitignore
# Remove entries for directories that no longer exist
# Add entries for any new gitignored paths

# 4.3 Verify remaining file count
git ls-files | wc -l  # should be ~160

# 4.4 Update README.md with new architecture
# 4.5 Update STRUCTURE-SUMMARY.md
# 4.6 Update WORKSPACE-MANUAL.md
# 4.7 Commit cleanup
git add -A
git commit -m "cleanup: core repo trimmed to pipeline + config after workstream split"
git push origin main
```

### Phase 5: Verification (30 min)

```bash
# 5.1 Verify all repos are accessible
for repo in hoi-intelligence-ops PRN-Johor-2026-H malaysia-journalist-registry \
            Voron-Campaign gov-intel cyber-intel pdrm-io; do
    echo "--- $repo ---"
    gh repo view ahmadfaurani/$repo --json name,visibility 2>&1
done

# 5.2 Verify submodules still work
cd /home/p62operator/.openclaw/workspace-hoi/
git submodule update --init --recursive

# 5.3 Verify file count reconciliation
git ls-files | sort > /tmp/post-split-core.txt
echo "Core repo: $(wc -l < /tmp/post-split-core.txt) files (target: ~160)"

# 5.4 Verify no files lost
# Sum of all repo file counts should equal original 463
# (minus duplicates already in submodules)

# 5.5 Verify cron jobs still work
# Audit Hermes cron config for path references
# Update any cron jobs that reference old monorepo paths

# 5.6 Test pipeline
python3 scripts/collect-political-news.py --test
python3 scripts/extract-entities.py --test
```

---

## 6. Cron Job Impact Assessment

**Critical:** 23 Hermes cron jobs may reference paths in the monorepo. After the split, paths change.

| Cron Job | Current Path | Impact | Action |
|----------|-------------|--------|--------|
| Daily News Collection | `scripts/collect-political-news.py` | ✅ Stays in core | None |
| Entity Extraction | `scripts/extract-entities.py` | ✅ Stays in core | None |
| Sentiment Analysis | `scripts/sentiment-analysis.py` | ✅ Stays in core | None |
| Narrative Tracking | `scripts/narrative-tracking-analysis.py` | ✅ Stays in core | None |
| Daily Brief Generation | `scripts/generate-daily-brief.py` | ✅ Stays in core | None |
| VoronDRQ Enrichment | `voron-stakeholders/scripts/*` | ⚠️ Moves to Voron-Campaign | Update path |
| ServiceNow Watch | `voron-campaign/scripts/*` | ⚠️ Moves to Voron-Campaign | Update path |
| Prospect Database Monitor | `prospects/prospect-database-*.csv` | ⚠️ Moves to Voron-Campaign | Update path |
| Media Registry collection | `scripts/discover-media-emails.py` | ⚠️ Moves to malaysia-journalist-registry | Update path |

**Action required:** After split, audit all cron jobs with `cronjob action='list'` and update `workdir` for any jobs that reference moved files.

---

## 7. Security Actions

| Repo | Current | Target | Command |
|------|---------|--------|---------|
| `Voron-Campaign` | PUBLIC | **PRIVATE** | `gh repo edit ahmadfaurani/Voron-Campaign --visibility private` |
| `HOI-Intelligence-Operations` | PUBLIC | **PRIVATE** | `gh repo edit ahmadfaurani/HOI-Intelligence-Operations --visibility private` |
| `cyber-intel` | N/A | PRIVATE | Created with `--private` |
| `pdrm-io` | N/A | PRIVATE | Created with `--private` |

**All intelligence repos must be PRIVATE.** No exceptions.

---

## 8. Rollback Plan

If anything goes wrong:

```bash
# Restore from backup branch
cd /home/p62operator/.openclaw/workspace-hoi/
git checkout backup-pre-split
git branch -D main
git branch main
git checkout main

# Force push to GitHub (reverses all changes)
git push origin main --force

# Re-initialize submodules
git submodule update --init --recursive
```

**Rollback is always possible** because:
1. `backup-pre-split` branch preserves the original state
2. GitHub repos that received split content can be deleted
3. Submodule remotes are unchanged (we only pushed new commits to them)

---

## 9. Post-Split Architecture Summary

```
BEFORE (monorepo):
  hoi-intelligence-ops (463 files, 11 components, mixed concerns)

AFTER (workstream repos):
  hoi-intelligence-ops     ~160 files  (pipeline + config + briefs + planning)
  PRN-Johor-2026-H        ~420 files  (constituency analysis + submodules)
  malaysia-journalist-registry  ~270 files  (journalist registry + media scripts)
  Voron-Campaign           ~25 files  (commercial GRC + prospects + collateral)
  gov-intel               ~165 files  (144 agency profiles + budget ML + workflows)
  cyber-intel               ~10 files  (7 intel briefs + 2 distribution packages)
  pdrm-io                  ~34 files  (contact DB + 9 scripts + docs)
                          ──────────
                          ~1,084 files total (includes submodule duplicates)
```

**Benefits:**
- Each workstream is independently versionable
- Access control per workstream (some PRIVATE, some shared)
- Smaller clone size for specific workstreams
- Clearer ownership and history per workstream
- Easier to onboard collaborators to specific workstreams
- Pipeline repo stays lean — no dormant content cluttering it

**Trade-offs:**
- Cross-repo references need explicit documentation
- Submodule management overhead (already exists, just formalized)
- Cron job paths need updating
- Initial split requires ~4 hours of focused execution

---

## 10. Decision Points

Before execution, confirm:

1. **Voron-Campaign visibility:** Flip PUBLIC → PRIVATE? (Recommended: YES)
2. **HOI-Intelligence-Operations:** Rename to `gov-intel` + flip PRIVATE? (Recommended: YES)
3. **narrative-tracking-hoi:** Merge 96 narrative reports into existing repo, or keep in core? (Recommended: Keep in core — pipeline output)
4. **OpenOSINT:** Stay in core as `openosint/` config dir, or split to own repo? (Recommended: Stay in core — shared service)
5. **Execution order:** Start with cyber-intel (safest) or Voron-Campaign (already separate)? (Recommended: cyber-intel first)
6. **Execute now or after REORGANIZATION-PLAN.md Step 1?** (Recommended: Step 1 first, then split)

---

*This plan is Step 2 of the two-step restructuring process. Step 1 (directory consolidation) is documented in `REORGANIZATION-PLAN.md`. Execute Step 1 first to create clean directory boundaries, then execute this plan to split along those boundaries.*

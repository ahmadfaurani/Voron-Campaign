# HOI WORKSPACE — STRUCTURE SUMMARY

**Generated:** 2026-07-11  
**Classification:** TLP:AMBER  
**Workspace:** `/home/p62operator/.openclaw/workspace-hoi/`  
**Last Reorganized:** 2026-07-11 (Phase 1 directory consolidation)

---

## Directory Tree

```
/home/p62operator/.openclaw/workspace-hoi/
│
├── .gitmodules                              # Submodule registration (3 submodules)
├── .gitignore                               # Excludes secrets, nested repos, data files
├── AGENT-SPEC.md                            # Agent specification
├── README.md                                # Project overview
├── ANALYTICAL-WORKSPACE.md                  # 11-component inventory + 55-pair coupling matrix
├── ARCHITECTURE.md                          # Three-layer architecture (Infrastructure → Pipeline → Products)
├── REORGANIZATION-PLAN.md                   # 6-phase reorganization plan
├── REPO-SPLIT-PLAN.md                       # Repository split execution plan
├── STRUCTURE-SUMMARY.md                     # This file
├── WORKSPACE-MANUAL.md                      # Master documentation
├── UPLOAD-SUMMARY.md                        # Upload tracking
├── LICENSE                                  # License file
│
├── config/                                  # Pipeline configuration (5 files)
│   ├── sources.yaml                         # News source definitions
│   ├── pir-definitions.yaml                 # Priority Intelligence Requirements
│   ├── narrative-clusters.yaml              # Narrative tracking cluster definitions
│   ├── sentiment-lexicon.yaml               # Sentiment analysis lexicon
│   └── MEDIA-EXPANSION-SUMMARY.md           # Media outlet expansion summary
│
├── scripts/                                 # Pipeline scripts (18 files)
│   ├── collect-news.sh                      # News collection (shell)
│   ├── collect-political-news.py            # Political news collection
│   ├── daily-collection-12outlets.py        # Daily 12-outlet collection
│   ├── daily-collection-run.sh              # Daily collection runner
│   ├── discover-emails-fast.py              # Fast email discovery
│   ├── discover-media-emails.py             # Media email discovery
│   ├── entity-extraction-run.py             # Entity extraction runner
│   ├── extract-entities-latest.py           # Latest entity extraction
│   ├── extract-entities.py                  # Entity extraction
│   ├── generate-daily-brief.py              # Daily brief generation
│   ├── narrative-tracking-analysis.py       # Narrative tracking analysis
│   ├── run-sentiment-analysis.py            # Sentiment analysis runner
│   ├── scrape_spr_2023_results.py           # SPR 2023 results scraper
│   ├── sentiment-analysis.py                # Sentiment analysis
│   ├── test-journalist-focus.py             # Journalist focus testing
│   ├── test-new-sources.py                  # New source testing
│   ├── test_api.py                          # API testing
│   └── validate-sources.py                  # Source validation
│
├── intelligence/                            # Intelligence outputs
│   ├── briefs/                              # Daily Intelligence Briefs (30 files, INTEL-008 → INTEL-034)
│   ├── narrative-tracking/                  # Narrative velocity reports (96 files)
│   ├── sentiment-analysis/                  # Sentiment analysis reports (44 files)
│   ├── cyber/                               # Cybersecurity intelligence (9 files + STATUS.md)
│   │   ├── Intel-Brief-001 through 007      # 7 cyber intel briefs
│   │   ├── Brief-Prof-Rezal-Background       # Background brief
│   │   ├── distribution/                     # 2 distribution packages
│   │   └── STATUS.md                        # Component status: DORMANT
│   ├── media/                               # Media intelligence (3 files)
│   │   ├── JOURNALIST-FOCUS-IMPLEMENTATION.md
│   │   ├── MEDIA-OUTLET-EXPANSION.md
│   │   └── Malaysian-Media-Intelligence-Database.md
│   ├── prn-johor-2026/                      # SUBMODULE → ahmadfaurani/PRN-Johor-2026-H
│   └── kempas/                              # SUBMODULE → ahmadfaurani/N47---Kempas.-H
│
├── constituency-analysis/                   # Electoral intelligence (11 files)
│   ├── 03-pemanis-overview-20260627.md
│   ├── 8-layang-layang-190626.md
│   ├── n07-bukit-kepong/                    # 4 expanded reports
│   ├── n17-skudai-analytical-report-2026-06-26.md
│   ├── skudai-n17.md
│   ├── bukit-naning-candidate-profile-analysis.md
│   ├── bukit-naning-comprehensive-dossier-20260627.md
│   ├── prn-johor-2026/                      # 4 PRN Johor files (n47-kempas, swing-seats)
│   └── war-room-reports/                    # War room analysis
│
├── n27-layang-layang/                       # SUBMODULE → ahmadfaurani/N27---Layang-Layang.-H
│
├── ops/                                     # Operational intelligence
│   ├── OPERATIONAL_MANUAL.md
│   ├── tier2-intel/                         # Government Tier 2 intelligence (159 files)
│   │   ├── evidence/Agency-Profiles/        # 144+ agency profiles (001-144)
│   │   ├── execution/                       # Execution plans
│   │   ├── planning/                        # OSINT process optimization
│   │   ├── research/                        # Process refinement
│   │   └── sources/                         # Source scripts
│   └── pdrm-io/                             # PDRM Information Operations (30 files + STATUS.md)
│       ├── STATUS.md                        # Component status: DORMANT
│       ├── docs/                            # 6 documentation files
│       ├── intelligence/                    # 14 intelligence files
│       └── scripts/                        # 9 PDRM IO scripts
│
├── voron/                                   # VoronDRQ commercial GRC (16 files + STATUS.md)
│   ├── STATUS.md                            # Component status: ACTIVE (consolidated)
│   ├── campaign-operations-manual.md
│   ├── collateral/                          # 3 files (battle cards, email templates, compliance)
│   ├── prospects/                           # 4 files (prospect databases)
│   ├── scripts/                             # 7 enrichment scripts
│   └── collected-pages/                     # 1 OSINT collection file
│
├── openosint/                               # OpenOSINT CLI integration (6 files)
│   ├── openosint-activate.sh                # CLI activation script
│   ├── openosint-targets.txt                # Target list (gitignored from root, tracked here)
│   ├── OPENOSINT_INSTALLATION_SUMMARY.md
│   ├── OPENOSINT_INTEGRATION.md
│   └── browser-automation/                  # 2 files (setup guide + Python script)
│
├── planning/                                # Infrastructure planning (6 files)
├── reference/                               # Reference data (3 files)
├── sources/                                 # Source registry
├── models/                                  # ML models (3 files)
├── workflows/                               # Budget intelligence pipeline (4 files)
├── templates/                               # Intel brief templates (2 files)
└── skills/                                  # Browser harness skills (4 files)
```

---

## Submodules

| Submodule | Remote URL | Status |
|-----------|-----------|--------|
| `intelligence/prn-johor-2026` | `https://github.com/ahmadfaurani/PRN-Johor-2026-H.git` | Registered in `.gitmodules` |
| `intelligence/kempas` | `https://github.com/ahmadfaurani/N47---Kempas.-H.git` | Registered in `.gitmodules` |
| `n27-layang-layang` | `https://github.com/ahmadfaurani/N27---Layang-Layang.-H.git` | Registered in `.gitmodules` |

---

## Component Summary

| Component | Directory | Files | Avg Coupling | Status |
|-----------|-----------|-------|-------------|--------|
| INTEL_PIPELINE | `intelligence/briefs/` + `scripts/` + `config/` | ~53 | 3.12/5.0 | ACTIVE |
| INFRA_CONFIG | `config/` + `.gitignore` + `.gitmodules` | ~7 | 3.00/5.0 | ACTIVE |
| PRN_JOHOR | `constituency-analysis/` + submodules | ~11+ | 3.40/5.0 | ACTIVE |
| MEDIA_REGISTRY | `intelligence/media/` + `reference/` | ~6 | 2.80/5.0 | ACTIVE |
| DOCUMENTATION | Root `.md` files | ~10 | 2.60/5.0 | ACTIVE |
| OPENOSINT | `openosint/` | 6 | 2.78/5.0 | ACTIVE |
| GOV_TIER2 | `ops/tier2-intel/` | 159 | 2.64/5.0 | DORMANT |
| CYBER_INTEL | `intelligence/cyber/` | 9 | 1.88/5.0 | DORMANT |
| PDRM_IO | `ops/pdrm-io/` | 29 | 2.04/5.0 | DORMANT |
| VORON_DRQ | `voron/` | 16 | 1.72/5.0 | ACTIVE (consolidated) |
| BUDGET_INTEL | `models/` + `workflows/` | 7 | 1.62/5.0 | DORMANT |

**Total tracked files:** 471 (467 original + `.gitmodules` + 3 `STATUS.md` files + 1 `STATUS.md` in voron)

---

## Changes from Previous Structure (2026-07-11)

### Phase A: Submodule Registration
- Created `.gitmodules` for 3 existing gitlinks that had no mapping

### Phase B: Root File Consolidation (24 files moved)
- 4 N07 Bukit Kepong reports → `constituency-analysis/n07-bukit-kepong/`
- 6 PDRM IO docs → `ops/pdrm-io/docs/`
- 2 Media intelligence docs → `intelligence/media/`
- 6 OpenOSINT files → `openosint/`
- 1 brief → `constituency-analysis/`
- 1 entity file → `constituency-analysis/`
- 1 war room report → `constituency-analysis/war-room-reports/`
- 4 PRN Johor root files → `constituency-analysis/prn-johor-2026/`

### Phase C: VoronDRQ Consolidation (16 files moved)
- `campaign-operations-manual.md` → `voron/`
- `collateral/` (3 files) → `voron/collateral/`
- `prospects/` (2 files) → `voron/prospects/`
- `voron-campaign/` (3 files) → `voron/`
- `voron-stakeholders/` (7 files) → `voron/`

### Phase D: Intelligence Domain Organization (35 files moved)
- 9 cyber intel briefs → `intelligence/cyber/`
- 1 media intelligence file → `intelligence/media/`
- 2 electoral intelligence files → `constituency-analysis/`
- 14 PDRM IO intel files → `ops/pdrm-io/intelligence/`
- 9 PDRM IO scripts → `ops/pdrm-io/scripts/`

### Phase E: Documentation Updates
- README.md workspace structure updated
- STRUCTURE-SUMMARY.md regenerated (this file)
- STATUS.md created for dormant components (CYBER_INTEL, PDRM_IO, VORON_DRQ)

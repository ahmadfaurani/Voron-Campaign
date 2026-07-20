# Git Cross-Contamination Mitigation Plan
## Voron-Campaign (HCR-072) — Enforced 2026-07-20

## Problem Statement

The Voron-Campaign repo accumulated 108 crossover files from 4 unrelated workstreams (PRN Johor 2026, PDRM Info Ops, Weststar-RTI, HOI Political Intelligence) because:

1. **Root cause:** The Git Sync cronjob script (`sync-vorondrq-campaign.sh`) used `git add -A`, which stages ALL files in the working directory regardless of relevance.
2. **Contributing factor:** Multiple cronjobs write output to the shared parent workspace (`workspace-hoi/`), and some files leaked into the `vorondrq-rmit-campaign/` subdirectory.
3. **Contributing factor:** The `.gitignore` was overly broad — blocking `*.csv` and `*.json` (the repo's primary content) while not blocking unrelated workstream directories.

## Mitigation Measures Implemented

### 1. Scoped Git Add (Sync Script Fix)

**Before:** `git add -A` (stages everything)
**After:** Scoped `git add` with explicit path whitelist:

```bash
git add \
  campaign-operations-manual.md \
  prospects/ \
  collateral/ \
  operations/ \
  HCR-REGISTRY.md \
  README.md \
  LICENSE \
  .gitignore
```

Only these directories/files are staged. Any file outside this whitelist is ignored, even if physically present in the workspace.

**File:** `~/.hermes/scripts/sync-vorondrq-campaign.sh`

### 2. Hardened .gitignore

The `.gitignore` now explicitly blocks known crossover directories:

```
intelligence/
n27-layang-layang/
kempas/
prn-johor-2026/
narrative-tracking/
policing-publications/
sentiment-analysis/
entities/
briefs/
pdrm-io/
```

This is a **defense-in-depth** layer. Even if a future cronjob writes into one of these directories inside `vorondrq-rmit-campaign/`, git will ignore it.

### 3. Directory Structure Enforcement

The repo now has a fixed structure:
- `prospects/` — Prospect database CSVs
- `collateral/` — Campaign collateral (email templates, battle cards, RMiT checklist)
- `operations/` — ALL cronjob operational files (single audit folder)
- Root: `campaign-operations-manual.md`, `README.md`, `HCR-REGISTRY.md`, `LICENSE`

Any file not matching this structure will be immediately visible as an anomaly.

## Audit Checklist (Monthly)

1. Run `git ls-files | grep -v -E '^(prospects/|collateral/|operations/|campaign-operations-manual.md|README.md|HCR-REGISTRY.md|LICENSE|.gitignore)'` — should return empty.
2. Verify `sync-vorondrq-campaign.sh` contains scoped `git add` (not `git add -A`).
3. Check for empty directories left by cronjobs: `find . -type d -empty -not -path './.git/*'`
4. Verify no `.csv` or `.json` files are blocked by `.gitignore`.

## Crossover File Migration Log (2026-07-20)

| Source | Files | Destination Repo |
|--------|-------|-----------------|
| `intelligence/policing-publications/` | 28 | `ahmadfaurani/pdrm-io` |
| `intelligence/briefs/` (INTEL-035→047) | 13 | Already in `hoi-intelligence-ops` (parent workspace) |
| `intelligence/narrative-tracking/` | 35 | Already in `hoi-intelligence-ops` (parent workspace) |
| `intelligence/sentiment-analysis/` | 28 | Already in `hoi-intelligence-ops` (parent workspace) |
| `intelligence/entities/` | 2 | Already in `weststar-rti-workstream` |
| `scripts/run-entity-extraction.py` | 1 | `ahmadfaurani/hoi-intelligence-ops` |
| `n27-layang-layang/` | 0 (empty) | Deleted |
| `intelligence/prn-johor-2026/` | 0 (empty) | Deleted |
| `intelligence/kempas/` | 0 (empty) | Deleted |
| `HCR-REGISTRY.md` (HCR-096 entry) | 1 entry | Removed from registry |

**Total crossover files removed:** 108  
**Files remaining in repo:** 195 (all legitimate Voron Campaign content)

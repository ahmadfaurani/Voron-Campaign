# Voron-Campaign

**Classification:** TLP:AMBER  
**HCR:** HCR-072  
**Purpose:** VoronDRQ commercial GRC intelligence — stakeholder mapping, prospect database, and campaign operations for Malaysian financial institutions. Data collection to enable a successful marketing outreach campaign targeting key GRC stakeholders within Malaysia's compliance-driven financial institution landscape.

## Repository Structure

```
Voron-Campaign/
├── campaign-operations-manual.md          # 90-day execution playbook
├── prospects/
│   └── prospect-database-250.csv          # Full account database with contacts
├── collateral/
│   ├── email-templates.md                 # Email templates for all tiers
│   ├── battle-cards.md                    # Competitor battle cards
│   └── rmit-compliance-checklist.md       # Customer-facing RMiT guide
├── operations/                            # All cronjob operational files (audit trail)
│   ├── enrichment-reports/                # Enrichment cycle reports (v3.0→v5.15)
│   ├── monitoring-briefs/                 # Prospect database monitor briefs
│   ├── daily-enrichment/                   # Daily enrichment JSONL + summaries
│   ├── stakeholder-profiles/              # Per-bank leadership dossiers + session reports
│   ├── prospect-databases/                # Versioned prospect database CSVs (full history)
│   ├── analysis/                          # Diff analysis JSONs
│   ├── state-snapshots/                    # State snapshots + commit logs
│   ├── scripts/                           # Enrichment & update scripts
│   ├── collected-pages/                    # Scraped stakeholder pages
│   ├── email-drafts/                       # Commercial outreach email drafts
│   └── STATUS.md                          # Campaign status
├── HCR-REGISTRY.md                        # Hermes Created Repo registry
└── LICENSE
```

## Campaign Deployment Files

The GitHub repository contains all campaign collateral ready for deployment:

| File | Description |
|------|-------------|
| `prospects/prospect-database-250.csv` | Full account database with contacts |
| `collateral/email-templates.md` | Email templates for all tiers |
| `collateral/battle-cards.md` | Competitor battle cards |
| `collateral/rmit-compliance-checklist.md` | Customer-facing RMiT guide |
| `campaign-operations-manual.md` | 90-day execution playbook |

## Operations Audit Trail

All cronjob operational files are filed under `operations/` to enable audit checks of the data collection pipeline. This includes enrichment reports, monitoring briefs, daily enrichment logs, stakeholder profiles, versioned databases, analysis snapshots, and scripts.

## Prospect Database

Current version: **v5.15** — 205 institutions, enriched with GRC stakeholder contacts.

Daily enrichment runs via Hermes cron job. See `operations/scripts/` for enrichment pipeline.

## Git Contamination Prevention

This repo uses a scoped `.gitignore` that explicitly blocks non-Voron directories and file types. The Git Sync script uses scoped `git add` (not `git add -A`) to prevent crossover from other workstreams sharing the parent workspace.

## Split History

This repo was previously a monorepo (`hoi-intelligence-ops`) containing 538 files across 11 components. On 2026-07-13, it was split into 7 workstream repos. On 2026-07-20, 108 crossover files from unrelated workstreams (PRN Johor, PDRM, Weststar-RTI) were cleaned out and migrated to their respective repos.

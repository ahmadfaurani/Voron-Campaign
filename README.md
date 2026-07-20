# Voron-Campaign

**Classification:** TLP:AMBER  
**HCR:** HCR-072  
**Purpose:** VoronDRQ commercial GRC intelligence — stakeholder mapping, prospect database, and campaign operations for Malaysian financial institutions.

## Repository Structure

```
Voron-Campaign/
├── voron/                         # Campaign operations
│   ├── campaign-operations-manual.md
│   ├── collateral/                # Battle cards, email templates, RMIT checklist
│   ├── prospects/                 # Prospect databases (v1.6 → v2.8 enriched)
│   ├── scripts/                   # Enrichment & update scripts
│   └── collected-pages/           # Scraped stakeholder pages
├── stakeholders/                  # Bank stakeholder profiles (50 files)
│   ├── *-stakeholders-*.md        # Per-bank leadership dossiers
│   ├── prospect-database-*.csv    # Versioned prospect databases
│   └── CAMPAIGN-STATUS-*.md       # Campaign status reports
├── voron-stakeholders/            # Latest enriched prospect database
│   └── prospect-database-enriched-v2.8.csv
└── email-to-head-of-solution*.md  # Commercial outreach templates
```

## Split History

This repo was previously a monorepo (`hoi-intelligence-ops`) containing 538 files across 11 components. On 2026-07-13, it was split into 7 workstream repos:

| Target Repo | HCR | Files | Content |
|-------------|-----|-------|---------|
| Voron-Campaign (this repo) | HCR-072 | 81 | VoronDRQ stakeholder + prospect data |
| hoi-intelligence-ops | HCR-094 | 226 | Core pipeline (scripts, config, intelligence briefs) |
| gov-intel | HCR-093 | 170 | Tier2 gov agency profiles + budget intel |
| pdrm-io | HCR-092 | 30 | PDRM information operations |
| cyber-intel | HCR-091 | 10 | Cybersecurity intel briefs |
| PRN-Johor-2026-H | existing | 15 | Constituency analysis (absorbed) |
| malaysia-journalist-registry | existing | 5 | Media intel files (absorbed) |

## Prospect Database

Current version: **v2.8** — 205 institutions, 96 enriched (46.8% activation rate).

Daily enrichment runs via Hermes cron job. See `voron/scripts/` for enrichment pipeline.

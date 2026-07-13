# HOI Intelligence Operations

**Classification:** TLP:AMBER  
**HCR:** HCR-094 (succeeds HCR-072 monorepo)  
**Purpose:** Automated intelligence pipeline — news collection, entity extraction, sentiment analysis, narrative tracking, and daily brief generation for Malaysian political monitoring.

## Contents

```
hoi-intelligence-ops/
├── scripts/                       # Core pipeline
│   ├── collect-news.sh
│   ├── collect-political-news.py
│   ├── daily-collection-*.py/.sh
│   ├── extract-entities*.py
│   ├── generate-daily-brief.py
│   ├── narrative-tracking-analysis.py
│   ├── run-sentiment-analysis.py
│   ├── sentiment-analysis.py
│   ├── scrape_spr_2023_results.py
│   └── validate-sources.py
├── config/                        # Pipeline configuration
│   ├── sources.yaml
│   ├── pir-definitions.yaml
│   ├── narrative-clusters.yaml
│   └── sentiment-lexicon.yaml
├── intelligence/                   # Pipeline outputs
│   ├── briefs/                    # INTEL-008 → INTEL-034 daily briefs
│   ├── narrative-tracking/        # 96 narrative reports
│   └── sentiment-analysis/        # 44 sentiment reports
├── templates/                     # Brief templates
├── planning/                      # Infrastructure planning docs
├── openosint/                     # OpenOSINT config + browser automation
├── reference/                     # Key politicians, political parties
├── sources/                       # Source registry
└── reports/                       # Ad-hoc intel reports
```

## Provenance

Extracted from Voron-Campaign (HCR-072) monorepo on 2026-07-13. This is the core pipeline hub that was the original purpose of the monorepo before workstream split.

## Related Repos (split from same monorepo)

| Repo | HCR | Purpose |
|------|-----|---------|
| Voron-Campaign | HCR-072 | VoronDRQ commercial GRC intelligence |
| gov-intel | HCR-093 | Government agency profiles + budget intel |
| pdrm-io | HCR-092 | PDRM information operations |
| cyber-intel | HCR-091 | Cybersecurity intelligence briefs |
| PRN-Johor-2026-H | existing | Electoral constituency analysis |
| malaysia-journalist-registry | existing | Media intelligence + journalist registry |

# HOI Intelligence Ops — System Architecture

**Generated:** 2026-07-11  
**Classification:** TLP:AMBER  
**Companion to:** `ANALYTICAL-WORKSPACE.md`

---

## 1. Three-Layer Architecture

```
╔══════════════════════════════════════════════════════════════════════╗
║                     LAYER 3: INTELLIGENCE PRODUCTS                   ║
║                                                                      ║
║  ┌─────────────┐  ┌─────────────┐  ┌──────────┐  ┌───────────────┐  ║
║  │ Daily Briefs │  │ Constituency│  │ Narrative│  │ Sentiment     │  ║
║  │ INTEL-008→  │  │ Profiles   │  │ Reports  │  │ Reports       │  ║
║  │ INTEL-034  │  │ 20 DUN     │  │ 6-hourly │  │ Daily, VADER  │  ║
║  └──────┬──────┘  └──────┬─────┘  └────┬─────┘  └──────┬────────┘  ║
║         │                │             │               │            ║
╠═════════╪════════════════╪═════════════╪═══════════════╪════════════╣
║         │    LAYER 2: ANALYTICAL PIPELINE               │            ║
║         │                                              │            ║
║  ┌──────▼──────────────────────────────────────────────▼────────┐   ║
║  │                    INTEL_PIPELINE                             │   ║
║  │                                                              │   ║
║  │  ┌────────┐   ┌────────┐   ┌────────┐   ┌────────┐          │   ║
║  │  │Collect │──►│Extract │──►│Sentiment│──►│Narrative│─┐        │   ║
║  │  │News    │   │Entities│   │Analysis │   │Tracking │ │        │   ║
║  │  │7 srcs  │   │NLP     │   │VADER    │   │10 clstrs│ │        │   ║
║  │  └────────┘   └────────┘   └────────┘   └────────┘ │        │   ║
║  │                                              ┌─────▼─────┐   │   ║
║  │                                              │ Generate  │   │   ║
║  │                                              │ Daily     │   │   ║
║  │                                              │ Brief     │   │   ║
║  │                                              └───────────┘   │   ║
║  └──────────────────────────────────────────────────────────────┘   ║
║                                                                      ║
║  ┌─────────────────┐  ┌──────────────────────────────────────┐       ║
║  │  OPENOSINT      │  │  MEDIA_REGISTRY                      │       ║
║  │  v2.23.0        │  │  Journalist Registry                 │       ║
║  │  Breach/DNS/    │  │  27 outlets → 600+ journalists       │       ║
║  │  Shodan/Social  │  │  Article byline → contact extraction │       ║
║  └────────┬────────┘  └──────────────────┬───────────────────┘       ║
║           │                              │                          ║
╠═══════════╪══════════════════════════════╪══════════════════════════╣
║           │   LAYER 1: INFRASTRUCTURE     │                          ║
║           │                              │                          ║
║  ┌────────▼──────────────────────────────▼──────────────────────┐   ║
║  │                    INFRA_CONFIG                               │   ║
║  │                                                              │   ║
║  │  config/          │ planning/        │ workflows/            │   ║
║  │  sources.yaml     │ infra reviews   │ browser harness       │   ║
║  │  pir-definitions  │ improvement plan │ budget pipeline       │   ║
║  │  narrative-clstrs│ phase summaries  │ integration docs      │   ║
║  │  sentiment-lexicon│                 │                       │   ║
║  │                                                              │   ║
║  │  External Services:                                          │   ║
║  │  DeerFlow (2026) │ Firecrawl (3002) │ SearXNG (8080)        │   ║
║  │  OpenOSINT v2.23 │ GLM-5.2 via ARAS │ Docker (17 containers) │   ║
║  └──────────────────────────────────────────────────────────────┘   ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## 2. Data Flow Diagram

### 2.1 Active Pipeline Flow

```
                    EXTERNAL NEWS SOURCES (7)
                    ┌───────┬───────┬───────┬───────┐
                    │Bernama│Malay- │TheStar │NST    │ ...
                    │       │siankini│       │       │
                    └───┬───┴───┬───┴───┬───┴───┬───┘
                        │       │       │       │
                        ▼       ▼       ▼       ▼
                   ┌─────────────────────────────────┐
                   │  Firecrawl API (localhost:3002) │
                   │  v1/scrape endpoint             │
                   └───────────────┬─────────────────┘
                                   │ JSON
                                   ▼
                   ┌─────────────────────────────────┐
                   │  collect-political-news.py      │
                   │  scripts/                       │
                   │  Output: intelligence/raw/      │
                   └───────────────┬─────────────────┘
                                   │ .md files
                                   ▼
                   ┌─────────────────────────────────┐
                   │  extract-entities.py            │
                   │  scripts/                       │
                   │  Config: config/pir-defs.yaml   │
                   │  Output: intelligence/entities/  │
                   └───────────────┬─────────────────┘
                                   │ JSON entities
                    ┌──────────────┼──────────────┐
                    ▼              ▼              ▼
          ┌──────────────┐ ┌────────────┐ ┌──────────────┐
          │sentiment-    │ │narrative-  │ │generate-     │
          │analysis.py   │ │tracking-  │ │daily-brief.py│
          │VADER -3 to+3 │ │analysis.py│ │7-section     │
          │              │ │10 clusters│ │template      │
          └──────┬───────┘ └─────┬──────┘ └──────┬───────┘
                 │               │               │
                 ▼               ▼               ▼
    intelligence/sentiment/  intelligence/   intelligence/
    analysis/               narrative-      briefs/
                            tracking/       INTEL-0XX-*.md
```

### 2.2 OpenOSINT Verification Flow

```
    ┌─────────────────────────────────────────────────┐
    │                 OPENOSINT v2.23.0               │
    │                                                 │
    │  ┌──────────┐  ┌──────────┐  ┌──────────────┐  │
    │  │HaveIBeen │  │ Shodan   │  │ DNS/DMARC/   │  │
    │  │Pwned     │  │ Infra    │  │ SPF/DKIM    │  │
    │  │(breach)  │  │ Recon    │  │ checks      │  │
    │  └────┬─────┘  └────┬─────┘  └──────┬───────┘  │
    │       │             │              │           │
    │       └─────────────┴──────────────┘           │
    │                     │                          │
    │                     ▼                          │
    │           Verification Reports                  │
    └─────────────────────┬──────────────────────────┘
                          │
           ┌──────────────┼──────────────┐
           ▼              ▼              ▼
    ┌──────────────┐ ┌──────────┐ ┌──────────────┐
    │VORON_DRQ     │ │MEDIA_REG │ │CYBER_INTEL   │
    │RMiT gaps     │ │Journalist│ │Infra recon   │
    │Stakeholder   │ │breach    │ │Threat actor  │
    │verification  │ │checks    │ │verification  │
    └──────────────┘ └──────────┘ └──────────────┘
```

---

## 3. Component Dependency Graph

```
                    ┌─────────────────────┐
                    │   INFRA_CONFIG      │
                    │ (Foundation Layer)  │
                    │ config/ planning/   │
                    └────────┬────────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
            ▼                ▼                ▼
   ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
   │INTEL_PIPELINE│ │ OPENOSINT    │ │ DOCUMENTATION│
   │ (Backbone)   │ │ (Enhancer)   │ │ (Meta)       │
   └──────┬───────┘ └──────┬───────┘ └──────────────┘
          │                │
     ┌────┼────┐     ┌─────┼─────┐
     │    │    │     │     │     │
     ▼    ▼    ▼     ▼     ▼     ▼
┌──────┐┌──────┐┌─────────┐┌──────┐┌──────────┐
│PRN   ││MEDIA ││VORON_DRQ││CYBER ││GOV_TIER2 │
│JOHOR ││REG   ││         ││INTEL ││          │
└──┬───┘└──────┘└─────────┘└──────┘└──────────┘
   │
   ▼
┌──────────┐  ┌──────────┐
│PDRM_IO   │  │BUDGET_   │
│          │  │INTEL    │
└──────────┘  └──────────┘

Edge weights (relevance scores):
━━━━━ ≥3.5 (tight)   ─── 2.5-3.4 (moderate)   ··· <2.5 (loose)
```

---

## 4. Infrastructure Topology

```
┌─────────────────────────────────────────────────────────────────────┐
│                      SELF-HOSTED INFRASTRUCTURE                      │
│                      (17 Docker containers)                         │
│                                                                     │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │  APPLICATION LAYER                                              │ │
│  │                                                                 │ │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐   │ │
│  │  │ DeerFlow │  │ Firecrawl│  │ SearXNG  │  │ OpenOSINT    │   │ │
│  │  │ Gateway  │  │ API      │  │ Meta-    │  │ v2.23.0      │   │ │
│  │  │ :2026    │  │ :3002    │  │ search   │  │ CLI          │   │ │
│  │  │          │  │ v1 API   │  │ :8080    │  │              │   │ │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────────┘   │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │  DATA LAYER                                                     │ │
│  │                                                                 │ │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐   │ │
│  │  │PostgreSQL│  │ Redis    │  │ RabbitMQ │  │ Honcho API   │   │ │
│  │  │          │  │ Cache    │  │ Queue    │  │              │   │ │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────────┘   │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │  AI/ML LAYER                                                    │ │
│  │                                                                 │ │
│  │  ┌──────────────────────────────────────────────────────────┐ │ │
│  │  │ ARAS Integrasi API → GLM-5.2 (zai-org/GLM-5.2)           │ │ │
│  │  │ All 23 Hermes cron jobs, OpenOSINT, OpenWebUI aligned    │ │ │
│  │  └──────────────────────────────────────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │  PROXY/REVERSE PROXY                                            │ │
│  │  ┌──────────┐                                                   │ │
│  │  │ Nginx    │ Routes: /api → DeerFlow, /scrape → Firecrawl     │ │
│  │  └──────────┘                                                   │ │
│  └────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 5. Cron Job Topology (23 Jobs)

```
HOI Intelligence Pipeline (cron-driven):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  [06:00] Daily News Collection ──────────► intelligence/raw/
     │                                    (7 sources via Firecrawl)
     ▼
  [08:00] Entity Extraction ────────────► intelligence/entities/
     │                                    (NLP from raw news)
     ▼
  [08:00] Sentiment Analysis ───────────► intelligence/sentiment-analysis/
     │                                    (VADER, -3 to +3 scale)
     ▼
  [08:00] Narrative Tracking ───────────► intelligence/narrative-tracking/
     │                                    (10 clusters, 6-hourly)
     ▼
  [09:00] Daily Brief Generation ───────► intelligence/briefs/
     │                                    (INTEL-XXX-YYYY-MM-DD.md)
     ▼
  [06:00] VoronDRQ Daily Enrichment ─────► voron-enrichment/
     │                                    (LinkedIn, RMiT checks)
     ▼
  [Mon 09:00] ServiceNow Watch ──────────► voron-campaign/
     │                                    (Competitive intelligence)
     ▼
  [Every 6h] Prospect Database Monitor ──► prospect-database-7stakeholders.csv
                                          (203 institutions, 1,421 slots)
```

---

## 6. Repository File Distribution

```
463 tracked files across 11 components:

GOV_TIER2     ██████████████████████████████████████████████ 157 files (34%)
INTEL_PIPELINE████████████████████████████████████████████ 197 files (43%)
  (briefs:30  narrative:96  sentiment:44  scripts:27)
PDRM_IO       ██████████ 34 files (7%)
VORON_DRQ     ████ 14 files (3%)
INFRA_CONFIG  █████ 19 files (4%)
PRN_JOHOR     ███ 12 files (3%)
CYBER_INTEL   ██ 10 files (2%)
BUDGET_INTEL  █ 6 files (1%)
DOCUMENTATION █ 6 files (1%)
MEDIA_REGISTRY ▌ 4 files (1%)
OPENOSINT     ▌ 4 files (1%)

Active vs Dormant:
ACTIVE  ████████████████████████████████ 240 files (52%)
DORMANT ████████████████████████ 217 files (48%)
  (Dormant: GOV_TIER2 157 + PDRM_IO 34 + CYBER 10 + BUDGET 6 + DOC 6 + extras)
```

---

## 7. Submodule Architecture

```
Parent Repo: hoi-intelligence-ops
│
├── [GITLINK] intelligence/prn-johor-2026/ ──► separate repo (409 files)
│   ├── .git/ (nested)
│   ├── n11-puteri-wangsa/ (nested .git)
│   ├── n51-bukit-batu/ (nested .git)
│   ├── dashboard/ (React app, 179MB node_modules — gitignored)
│   ├── scraper-env/ (Playwright venv — gitignored)
│   └── .venv/ (Python venv — gitignored)
│
├── [GITLINK] intelligence/kempas/ ──► nested .git
│   └── campaign-operations/ candidate-profiles/ etc.
│
├── [GITLINK] n27-layang-layang/ ──► nested .git
│   └── candidate-profiles/ constituency-data/ etc.
│
├── [GITIGNORED] intelligence/media-registry/ ──► nested .git
│   └── 262 files (journalist registry)
│
├── [GITIGNORED] Voron-Campaign/ ──► separate repo (Voron-Campaign.git)
├── [GITIGNORED] integration-module/ ──► nested .git
├── [GITIGNORED] n03-pemanis-repo/ ──► nested .git
├── [GITIGNORED] n9-pir/ ──► nested .git
├── [GITIGNORED] narrative-tracking-workspace/ ──► nested .git
└── [GITIGNORED] vorondrq-rmit-campaign/ ──► nested .git

⚠️ NO .gitmodules FILE — gitlink submodules will fail on clone
```

---

## 8. Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **AI Model** | GLM-5.2 (via ARAS Integrasi) | Primary LLM for all operations |
| **Web Scraping** | Firecrawl v1 API (self-hosted :3002) | News collection, page extraction |
| **Sentiment** | VADER SentimentIntensityAnalyzer | Political sentiment scoring |
| **OSINT** | OpenOSINT v2.23.0 | Breach checks, Shodan, DNS, social |
| **Search** | SearXNG (:8080) | Meta-search aggregation |
| **Workflow** | DeerFlow (:2026) | Agent orchestration, gateway |
| **Database** | PostgreSQL | Persistent storage |
| **Cache** | Redis | Session/cache |
| **Queue** | RabbitMQ | Async task processing |
| **Browser** | Playwright (in venvs) | JS-rendered page automation |
| **Container** | Docker (17 containers) | Service isolation |
| **Reverse Proxy** | Nginx | Request routing |
| **Version Control** | Git + GitHub (private) | Code/intel storage |
| **Scheduling** | Hermes Cron (23 jobs) | Automated pipeline triggers |

---

*This architecture document maps the system topology. Refer to `ANALYTICAL-WORKSPACE.md` for component details and `REORGANIZATION-PLAN.md` for restructuring recommendations.*

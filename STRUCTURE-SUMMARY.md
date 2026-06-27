# HOI WORKSPACE — STRUCTURE SUMMARY

**Generated:** 2026-06-13  
**Classification:** TLP:AMBER  
**Workspace:** `/home/p62operator/.openclaw/workspace-hoi/`

---

## Directory Tree

```
/home/p62operator/.openclaw/workspace-hoi/
│
├── WORKSPACE-MANUAL.md                          # Master documentation (14 KB)
│
├── intelligence/                                # Core intelligence products
│   ├── briefs/                                  # Daily Intelligence Briefs
│   │   └── INTEL-008-E2E-Test.md                # First E2E test brief (3.5 KB)
│   │
│   ├── raw/                                     # Raw collected content
│   │   └── (auto-populated by cron)
│   │
│   ├── entities/                                # Extracted entities (JSON)
│   │   └── (auto-populated by cron)
│   │
│   ├── sentiment-analysis/                      # Sentiment reports
│   │   └── (auto-populated by cron)
│   │
│   ├── narrative-tracking/                      # Narrative velocity reports
│   │   └── (auto-populated by cron)
│   │
│   └── social-media/                            # Social media captures
│       └── (auto-populated by cron)
│
├── config/                                      # Configuration files (4 files)
│   ├── sources.yaml                             # 7 news sources (3.8 KB) ✓
│   ├── pir-definitions.yaml                     # 10 PIRs (9.0 KB) ✓
│   ├── narrative-clusters.yaml                  # 10 narratives (8.4 KB) ✓
│   └── sentiment-lexicon.yaml                   # Sentiment rules (7.0 KB) ✓
│
├── templates/                                   # Document templates
│   ├── daily-brief-template.md                  # 7-section brief (7.7 KB) ✓
│   └── Intel-Brief-Template.md                  # Legacy template
│
├── scripts/                                     # Utility scripts
│   ├── collect-news.sh                          # Manual collection (2.0 KB) ✓
│   └── validate-sources.py                      # Health checker (4.5 KB) ✓
│
├── reference/                                   # Reference materials
│   ├── malaysian-political-parties.md           # Party structure (5.3 KB) ✓
│   └── key-politicians.md                       # 20+ profiles (5.6 KB) ✓
│
├── planning/                                    # Workstream planning
│   ├── Political-Monitoring-Workstream-Review-2026-06-13.md  # Master review (19 KB)
│   └── PHASE-1-COMPLETE-2026-06-13.md           # Phase 1 summary (9.1 KB) ✓
│
├── archive/                                     # Historical data
│   └── 2026/
│       ├── 06/                                  # June 2026
│       ├── 07/                                  # July 2026
│       └── 08/                                  # August 2026
│
└── ops/                                         # Legacy ops (pre-existing)
    └── tier2-intel/                             # Existing Tier 2 intel
        └── (existing content)
```

---

## Files Created (Phase 1)

### Configuration (4 files, 28.2 KB)
| File | Size | Purpose |
|------|------|---------|
| `config/sources.yaml` | 3.8 KB | 7 news sources, Firecrawl settings |
| `config/pir-definitions.yaml` | 9.0 KB | 10 PIRs with keywords, thresholds |
| `config/narrative-clusters.yaml` | 8.4 KB | 10 narratives, correlations |
| `config/sentiment-lexicon.yaml` | 7.0 KB | Sentiment rules, emotions, framing |

### Templates (1 file, 7.7 KB)
| File | Size | Purpose |
|------|------|---------|
| `templates/daily-brief-template.md` | 7.7 KB | 7-section INTEL brief template |

### Scripts (2 files, 6.5 KB)
| File | Size | Purpose |
|------|------|---------|
| `scripts/collect-news.sh` | 2.0 KB | Manual collection trigger |
| `scripts/validate-sources.py` | 4.5 KB | Source health checker |

### Reference (2 files, 10.9 KB)
| File | Size | Purpose |
|------|------|---------|
| `reference/malaysian-political-parties.md` | 5.3 KB | Coalition structure, parties |
| `reference/key-politicians.md` | 5.6 KB | 20+ politician profiles |

### Planning (1 file, 9.1 KB)
| File | Size | Purpose |
|------|------|---------|
| `planning/PHASE-1-COMPLETE-2026-06-13.md` | 9.1 KB | Phase 1 completion summary |

### Intelligence Products (1 file, 3.5 KB)
| File | Size | Purpose |
|------|------|---------|
| `intelligence/briefs/INTEL-008-E2E-Test.md` | 3.5 KB | First E2E test brief |

### Master Documentation (1 file, 14.1 KB)
| File | Size | Purpose |
|------|------|---------|
| `WORKSPACE-MANUAL.md` | 14.1 KB | Complete workspace guide |

---

## Totals

**New Files Created:** 13  
**Total Size:** 83.8 KB  
**Directories Created:** 9 (`intelligence/*`, `config/`, `templates/`, `scripts/`, `reference/`, `archive/2026/*`)

---

## Cron Jobs (5 Scheduled)

| Job ID | Name | Schedule | Next Run |
|--------|------|----------|----------|
| `b4df4adfa7b4` | Daily News Collection | 00:00 UTC | 2026-06-14 00:00 |
| `6bf389346207` | Entity Extraction | 06:00 UTC | 2026-06-14 06:00 |
| `d7088d304782` | Sentiment Analysis | 08:00 UTC | 2026-06-14 08:00 |
| `e1da67dd2437` | Daily Brief Generation | 09:00 UTC | 2026-06-14 09:00 |
| `6012388aaebe` | Narrative Tracking | Every 4h | 2026-06-13 16:00 |

---

## Skills (6 Created)

**Location:** `/home/p62operator/tools/deer-flow/skills/public/political-monitoring/`

| Skill | Lines | Size | Status |
|-------|-------|------|--------|
| political-news-collection | 353 | 10.8 KB | ✅ |
| entity-extraction | 621 | 19.5 KB | ✅ |
| daily-brief-generator | 494 | 15.7 KB | ✅ |
| social-media-monitor | 412 | 14.0 KB | ✅ |
| narrative-tracking | 471 | 17.1 KB | ✅ |
| sentiment-analysis | 629 | 23.9 KB | ✅ |

**Total:** 2,980 lines, 101 KB

---

## Automated Pipeline

### Daily Flow (Starting 2026-06-14)

```
00:00 UTC ── Collect from 7 sources
              ↓ /intelligence/raw/YYYY-MM-DD/

06:00 UTC ── Extract entities (5 categories)
              ↓ /intelligence/entities/YYYY-MM-DD.json

08:00 UTC ── Analyze sentiment (-3 to +3)
              ↓ /intelligence/sentiment-analysis/YYYY-MM-DD.md

09:00 UTC ── Generate Daily Brief
              ↓ /intelligence/briefs/INTEL-XXX.md

Every 4h ─── Track 10 narratives
              ↓ /intelligence/narrative-tracking/YYYY-MM-DD-HH-00.md
```

---

## Access Points

### Manual Commands

```bash
# List cron jobs
hermes cronjob list

# Run collection manually
bash /home/p62operator/.openclaw/workspace-hoi/scripts/collect-news.sh

# Check source health
python3 /home/p62operator/.openclaw/workspace-hoi/scripts/validate-sources.py

# Run specific cron job
hermes cronjob run --job-id=b4df4adfa7b4  # Collection
hermes cronjob run --job-id=6bf389346207  # Extraction
hermes cronjob run --job-id=e1da67dd2437  # Brief generation
```

### File Locations

- **Briefs:** `/home/p62operator/.openclaw/workspace-hoi/intelligence/briefs/`
- **Configs:** `/home/p62operator/.openclaw/workspace-hoi/config/`
- **Scripts:** `/home/p62operator/.openclaw/workspace-hoi/scripts/`
- **Reference:** `/home/p62operator/.openclaw/workspace-hoi/reference/`
- **Skills:** `/home/p62operator/tools/deer-flow/skills/public/political-monitoring/`

---

## Status

**Phase 1:** ✅ COMPLETE (2026-06-13)  
**First Automated Brief:** 2026-06-14 09:00 UTC  
**Operational Status:** FULLY AUTOMATED

---

**HOI Agent Workspace — Operational Since 2026-06-13**  
**Classification:** TLP:AMBER

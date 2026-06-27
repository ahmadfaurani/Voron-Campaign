# HOI Agent Workspace — Political Monitoring Workstream

**Workspace ID:** HOI-PM-001  
**Classification:** TLP:AMBER — Internal Operational Use  
**Created:** 2026-06-13  
**Status:** ✅ OPERATIONAL (Phase 1 Complete)  
**Owner:** DeerFlow Political Monitoring Workstream

---

## Directory Structure

```
/home/p62operator/.openclaw/workspace-hoi/
│
├── intelligence/                    # Core intelligence products
│   ├── briefs/                      # Daily Intelligence Briefs (TLP:AMBER)
│   │   ├── INTEL-008-E2E-Test.md    # End-to-end test brief
│   │   └── INTEL-XXX-YYYY-MM-DD.md  # Daily briefs (auto-generated)
│   │
│   ├── raw/                         # Raw collected content
│   │   ├── 2026-06-13/              # Date-stamped collections
│   │   │   ├── bernama-20260613-0000.md
│   │   │   ├── malaysiakini-20260613-0000.md
│   │   │   └── ...
│   │   └── ...
│   │
│   ├── entities/                    # Extracted entities
│   │   ├── 2026-06-14-entities.json
│   │   └── ...
│   │
│   ├── sentiment-analysis/          # Sentiment reports
│   │   ├── 2026-06-14-daily-sentiment.md
│   │   └── ...
│   │
│   ├── narrative-tracking/          # Narrative velocity reports
│   │   ├── 2026-06-13-16-00-narrative.md
│   │   └── ...
│   │
│   └── social-media/                # Social media monitoring
│       ├── twitter-captures/
│       └── ...
│
├── planning/                        # Workstream planning & reviews
│   ├── Political-Monitoring-Workstream-Review-2026-06-13.md
│   ├── PHASE-1-COMPLETE-2026-06-13.md
│   ├── Phase-2-Plan.md
│   └── Roadmap-2026.md
│
├── config/                          # Configuration files
│   ├── sources.yaml                 # News source definitions
│   ├── pir-definitions.yaml         # Priority Intelligence Requirements
│   ├── narrative-clusters.yaml      # Narrative cluster definitions
│   ├── sentiment-lexicon.yaml       # Malaysian political sentiment lexicon
│   └── workspace-config.yaml        # Workspace-wide settings
│
├── templates/                       # Document templates
│   ├── daily-brief-template.md      # Daily Intel Brief template
│   ├── narrative-report-template.md # Narrative tracking template
│   ├── sentiment-report-template.md # Sentiment analysis template
│   └── entity-extraction-template.json
│
├── scripts/                         # Utility scripts
│   ├── collect-news.sh              # Manual collection trigger
│   ├── generate-brief.sh            # Manual brief generation
│   ├── export-pir-matches.py        # PIR matching export
│   └── validate-sources.py          # Source health checker
│
├── archive/                         # Historical data (organized by date)
│   ├── 2026/
│   │   ├── 06/                      # June 2026
│   │   ├── 07/                      # July 2026
│   │   └── 08/                      # August 2026
│   └── ...
│
└── reference/                       # Reference materials
    ├── malaysian-political-parties.md
    ├── key-politicians.md
    ├── media-outlets.md
    └── historical-timelines/
```

---

## Intelligence Products

### 1. Daily Intelligence Brief (INTEL-XXX)

**Frequency:** Daily at 09:00 UTC  
**Classification:** TLP:AMBER  
**Distribution:** DAF, CSM  
**Format:** 7-section markdown

**Sections:**
1. Executive Summary
2. PIR Updates (10 PIRs)
3. Entity Extraction Results
4. Sentiment Snapshot
5. Narrative Tracking Summary
6. Recommendations
7. System Status

**Filename Convention:** `INTEL-XXX-YYYY-MM-DD.md`
- `INTEL-001` to `INTEL-007`: Test briefs (Jun 7-13)
- `INTEL-008`: First automated brief (Jun 14)
- `INTEL-009+`: Daily automated briefs

---

### 2. Entity Extraction Reports

**Frequency:** Daily at 06:00 UTC  
**Format:** JSON + Markdown summary

**Entity Categories:**
- PERSON (politicians, officials, activists)
- ORGANIZATION (parties, coalitions, NGOs)
- LOCATION (states, constituencies, regions)
- EVENT (elections, scandals, party formations)
- CONCEPT (policies, narratives, ideologies)

**Output:** `/intelligence/entities/YYYY-MM-DD-entities.json`

---

### 3. Sentiment Analysis Reports

**Frequency:** Daily at 08:00 UTC  
**Format:** Markdown with charts

**Metrics:**
- Entity-level sentiment (-3 to +3)
- Party/coalition aggregate sentiment
- Sentiment velocity (rate of change)
- Anomaly detection (z-score > 2)
- Demographic segmentation

**Output:** `/intelligence/sentiment-analysis/YYYY-MM-DD-daily-sentiment.md`

---

### 4. Narrative Tracking Reports

**Frequency:** Every 4 hours (00:00, 04:00, 08:00, 12:00, 16:00, 20:00 UTC)  
**Format:** Markdown with velocity charts

**Narratives Tracked:** 10 clusters (NAR-01 to NAR-10)

**Metrics:**
- Narrative velocity (% change vs baseline)
- Sentiment trajectory
- Source propagation speed
- Lifecycle stage (Emergence, Growth, Peak, Decline, Exhausted)
- Inflection alerts (🟢 Yellow, 🟠 Orange, 🔴 Red)

**Output:** `/intelligence/narrative-tracking/YYYY-MM-DD-HH-00-narrative.md`

---

## Priority Intelligence Requirements (PIRs)

### PIR Definitions

| PIR ID | Focus Area | Key Questions | Status |
|--------|-----------|---------------|--------|
| **PIR-1** | PKR Johor Stability | Is PKR Johor facing defection crisis? What is grassroots sentiment? | ⏳ Active |
| **PIR-2** | BERSAMA Movement | What is BERSAMA's membership growth trajectory? Electoral impact? | ⏳ Active |
| **PIR-3** | Rafizi Faction | Is Rafizi challenging party leadership? INVOKE role? | ⏳ Active |
| **PIR-4** | BN Johor Position | How is BN Johor positioning vs BERSAMA? UMNO strategy? | ⏳ Active |
| **PIR-5** | Youth Voter Sentiment | What are undi18 priorities? Cost of living impact? | ⏳ Active |
| **PIR-6** | PKR Unity | Is PKR damage control effective? Reconciliation progress? | ⏳ Active |
| **PIR-7** | Onn Hafiz Strategy | Is Onn Hafiz pursuing solo bid? 56-seat strategy viable? | ⏳ Active |
| **PIR-8** | BERSAMA Growth | Membership numbers? Candidate recruitment? | ⏳ Active |
| **PIR-9** | PH Pact | Seat negotiation progress? Coalition stability? | ⏳ Active |
| **PIR-10** | Sabah Cascade | Is Sabah PKR facing defections? GRB expansion? | ⏳ Active |

---

## Narrative Clusters

### 10 Defined Narratives

| ID | Theme | Core Entities | Keywords |
|----|-------|---------------|----------|
| **NAR-01** | PKR Johor Crisis | PKR, Johor, branch chief | "PKR Johor", "defection", "grassroots revolt" |
| **NAR-02** | BERSAMA Movement | BERSAMA, third force | "Parti Bersama", "third force", "alternative" |
| **NAR-03** | Rafizi Faction | Rafizi, INVOKE | "Rafizi", "INVOKE", "party reform" |
| **NAR-04** | BN Johor Strategy | UMNO, BN Johor | "BN Johor", "UMNO strategy", "opposition" |
| **NAR-05** | Youth Voter | Youth, undi18 | "youth voter", "undi18", "cost of living" |
| **NAR-06** | PKR Unity | PKR unity, reconciliation | "PKR unity", "damage control", "reconciliation" |
| **NAR-07** | Onn Hafiz Ambition | Onn Hafiz, 56 seats | "Onn Hafiz", "56 seats", "solo bid" |
| **NAR-08** | BERSAMA Growth | BERSAMA membership | "BERSAMA membership", "recruitment" |
| **NAR-09** | PH Pact | PH, seat negotiation | "PH pact", "seat negotiation", "coalition" |
| **NAR-10** | Sabah Cascade | Sabah PKR, GRB | "Sabah PKR", "GRB", "defection cascade" |

---

## Automated Pipeline

### Daily Schedule (UTC)

```
00:00 ── News Collection
         ↓ Collect from 7 sources
         ↓ Save to /intelligence/raw/YYYY-MM-DD/

06:00 ── Entity Extraction
         ↓ Extract 5 entity categories
         ↓ Match against 10 PIRs
         ↓ Save to /intelligence/entities/

08:00 ── Sentiment Analysis
         ↓ Score all entities (-3 to +3)
         ↓ Detect anomalies
         ↓ Save to /intelligence/sentiment-analysis/

09:00 ── Daily Brief Generation
         ↓ Combine raw + entities + sentiment
         ↓ Generate 7-section brief
         ↓ Save to /intelligence/briefs/

12:00 ── Narrative Tracking (1st run)
         ↓ Analyze 10 narratives
         ↓ Calculate velocity
         ↓ Save to /intelligence/narrative-tracking/

16:00 ── Narrative Tracking (2nd run)
20:00 ── Narrative Tracking (3rd run)
00:00 ── Narrative Tracking (4th run, next day)
```

---

## News Sources

### Tier 1 (High Priority)

| Source | URL | Status | Notes |
|--------|-----|--------|-------|
| Bernama | https://www.bernama.com/en/ | ✅ Operational | National news agency |
| Malaysiakini | https://www.malaysiakini.com/ | ✅ Operational | Independent, critical |
| NST | https://www.nst.com.my/ | ✅ Operational | Pro-government lean |
| FMT | https://www.freemalaysiatoday.com/ | ✅ Operational | Independent, critical |

### Tier 2 (Regional Focus)

| Source | URL | Status | Notes |
|--------|-----|--------|-------|
| Daily Express | https://www.dailyexpress.com.my/ | ✅ Operational | Sabah focus |
| Borneo Post | https://www.theborneopost.com/ | ✅ Operational | Sarawak/Sabah |
| The Star | https://www.thestar.com.my/ | ⚠️ Partial | Politics section 404, using homepage |

---

## Sentiment Framework

### 7-Point Likert Scale

| Score | Label | Description | Example |
|-------|-------|-------------|---------|
| +3 | Very Positive | Strong endorsement | "historic achievement", "unanimous praise" |
| +2 | Positive | Favorable coverage | "welcomed", "supported", "approved" |
| +1 | Slightly Positive | Mild approval | "hopeful", "optimistic" |
| 0 | Neutral | Factual reporting | "announced", "stated", "scheduled" |
| -1 | Slightly Negative | Mild criticism | "questioned", "concerned", "doubted" |
| -2 | Negative | Critical coverage | "condemned", "failed", "controversy" |
| -3 | Very Negative | Strong condemnation | "scandal", "outrage", "crisis" |

### Sentiment Velocity Interpretation

| Velocity | Interpretation | Action |
|----------|---------------|--------|
| > +0.3/day | Rapid improvement | Monitor sustainability |
| +0.1 to +0.3/day | Gradual improvement | Track daily |
| -0.1 to +0.1/day | Stable | Weekly review |
| -0.3 to -0.1/day | Gradual decline | Monitor closely |
| < -0.3/day | Rapid deterioration | Crisis alert |

---

## Cron Jobs

### Scheduled Jobs (5 Total)

| Job ID | Name | Schedule | Toolsets |
|--------|------|----------|----------|
| `b4df4adfa7b4` | Daily News Collection | `0 0 * * *` | terminal, file |
| `6bf389346207` | Entity Extraction | `0 6 * * *` | terminal, file |
| `d7088d304782` | Sentiment Analysis | `0 8 * * *` | terminal, file |
| `e1da67dd2437` | Daily Brief Generation | `0 9 * * *` | terminal, file |
| `6012388aaebe` | Narrative Tracking | `0 */4 * * *` | terminal, file |

**Management Commands:**
```bash
# List all jobs
hermes cronjob list

# Pause a job
hermes cronjob pause --job-id=<job_id>

# Resume a job
hermes cronjob resume --job-id=<job_id>

# Run a job manually
hermes cronjob run --job-id=<job_id>

# Remove a job
hermes cronjob remove --job-id=<job_id>
```

---

## Integration Points

### HOI Workspace Integration

**Brief Distribution:**
- Primary: `/home/p62operator/.openclaw/workspace-hoi/intelligence/briefs/`
- Mirror: DAF internal distribution
- Archive: `/home/p62operator/.openclaw/workspace-hoi/archive/YYYY/MM/`

### External Systems

| System | Integration | Status |
|--------|-------------|--------|
| DeerFlow | Skills loaded | ✅ Active |
| Firecrawl | Scraping API | ✅ Active (port 3002) |
| SearXNG | Search backend | ✅ Active (port 8080) |
| Twitter API | Social media | ⏳ Pending (using fallback) |

---

## Security & Classification

### TLP Marking

All intelligence products are marked **TLP:AMBER**:
- Distribution limited to HOI team members
- Not for public release
- Internal operational use only

### Access Control

**Read Access:**
- DAF (DeerFlow Agent Framework)
- CSM (Chief of Staff — Monitoring)

**Write Access:**
- DeerFlow automated pipeline only
- Manual edits require approval

---

## Quality Assurance

### Data Quality Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Collection Success Rate | >95% | 100% (5/5 sources) |
| Entity Extraction Confidence | >0.75 | Pending first run |
| Sentiment Analysis Confidence | >0.75 | Pending first run |
| Brief Generation Time | <30 min | Pending first run |
| Narrative Tracking Latency | <5 min | Pending first run |

### Validation Checks

1. **Source Health:** Daily ping of all 7 sources
2. **Content Completeness:** Verify >10KB per source
3. **Entity Coverage:** Confirm 20+ entities per day
4. **Sentiment Range:** Verify -3 to +3 distribution
5. **Narrative Velocity:** Check for anomalies (>3x baseline)

---

## Disaster Recovery

### Backup Strategy

**Daily Backup:**
- `/intelligence/briefs/` → Archive by date
- `/intelligence/entities/` → JSON backup
- `/config/` → Version controlled

**Recovery Procedure:**
1. Restore from `/archive/YYYY/MM/`
2. Re-run cron jobs from last successful point
3. Validate brief continuity

### Fallback Modes

| Failure | Fallback |
|---------|----------|
| Firecrawl unavailable | SearXNG search fallback |
| DeerFlow gateway down | Manual skill execution |
| Cron job failure | Manual trigger via scripts/ |
| Source 404 | Alternative URL or skip |

---

## Contact & Support

**Workspace Path:** `/home/p62operator/.openclaw/workspace-hoi/`  
**Skills Path:** `/home/p62operator/tools/deer-flow/skills/public/political-monitoring/`  
**Cron Management:** `hermes cronjob` CLI

**Documentation:**
- Phase 1 Complete: `/planning/PHASE-1-COMPLETE-2026-06-13.md`
- Workstream Review: `/planning/Political-Monitoring-Workstream-Review-2026-06-13.md`

---

**HOI Agent Workspace — Operational Since 2026-06-13**  
**Next Automated Brief:** 2026-06-14 09:00 UTC

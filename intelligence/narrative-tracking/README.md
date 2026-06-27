# Narrative Tracking Implementation Summary

**Classification:** TLP:AMBER — Internal Operational Use  
**Created:** 2026-06-13  
**Workstream:** Political Monitoring (HOI Agent)

---

## Overview

Automated narrative tracking analysis for 10 political narrative clusters (NAR-01 to NAR-10) in Malaysian politics. The system calculates narrative velocity, sentiment trajectory, source propagation, detects inflection points, and classifies lifecycle stages.

---

## Components

### 1. Analysis Script

**Location:** `/home/p62operator/.openclaw/workspace-hoi/scripts/narrative-tracking-analysis.py`

**Features:**
- Loads narrative cluster configuration from `/home/p62operator/.openclaw/workspace-hoi/config/narrative-clusters.yaml`
- Calculates narrative velocity: `(Current - Baseline) / Baseline × 100`
- Tracks sentiment trajectory with velocity detection
- Monitors source propagation (coverage across 7 Tier 1 sources)
- Detects inflection points:
  - Acceleration >100%: 🟡 Yellow alert
  - Acceleration >200%: 🟠 Orange alert
  - Acceleration >400%: 🔴 Red alert
  - Sentiment shift >0.5: 🟡/🟠 alert
- Classifies lifecycle stages:
  - **Emergence:** Velocity +100% to +500%, <3 sources
  - **Growth:** Velocity +20% to +100%, 3-5 sources
  - **Peak:** Velocity -10% to +20%, 6-7 sources
  - **Stable:** Velocity -10% to +10%, moderate coverage
  - **Decline:** Velocity -80% to -20%, decreasing mentions
  - **Exhausted:** Velocity <-80%, <2 sources

### 2. Output Directory

**Location:** `/home/p62operator/.openclaw/workspace-hoi/intelligence/narrative-tracking/`

**Filename Format:** `YYYY-MM-DD-HH-MM-narrative-report.md`

**Report Contents:**
- Executive Summary (dominant narrative, fastest growing, alerts)
- Narrative Status Dashboard (10 narratives with metrics)
- Inflection Alerts (color-coded by severity)
- Narrative Propagation Map
- Cross-Narrative Correlations
- Lifecycle Visualization (ASCII matrix)
- Trending Headlines by Narrative
- Recommendations (Immediate, Short-term, Strategic)
- Data Quality Notes
- System Status

### 3. Cron Job

**Job ID:** `6012388aaebe`  
**Name:** Political Monitoring - Narrative Tracking  
**Schedule:** `0 */4 * * *` (Every 4 hours)  
**Operational Hours:** 00:00, 04:00, 08:00, 12:00, 16:00, 20:00 UTC  
**Next Run:** 2026-06-13 20:00 UTC

**Configuration:**
```json
{
  "script": "/home/p62operator/.openclaw/workspace-hoi/scripts/narrative-tracking-analysis.py",
  "no_agent": true,
  "enabled_toolsets": ["terminal", "file"],
  "workdir": "/home/p62operator/.openclaw/workspace-hoi"
}
```

---

## Narrative Clusters (NAR-01 to NAR-10)

| ID | Theme | Priority | Baseline Mentions | Current Stage |
|----|-------|----------|-------------------|---------------|
| NAR-01 | PKR Johor Crisis | Critical | 15/day | Peak → Growth |
| NAR-02 | BERSAMA Movement | Critical | 18/day | Growth |
| NAR-03 | Rafizi Faction | High | 12/day | Decline |
| NAR-04 | BN Johor Strategy | High | 20/day | Stable |
| NAR-05 | Youth Voter Sentiment | High | 8/day | Emergence |
| NAR-06 | PKR Unity Efforts | Medium | 10/day | Growth |
| NAR-07 | Onn Hafiz Ambition | Medium | 14/day | Stable |
| NAR-08 | BERSAMA Growth | High | 10/day | Growth |
| NAR-09 | PH Seat Negotiation | Medium | 16/day | Decline |
| NAR-10 | Sabah Cascade | Medium | 6/day | Emergence |

---

## Cross-Narrative Correlations

| Narrative A | Correlation | Narrative B | Interpretation |
|-------------|-------------|-------------|----------------|
| NAR-01 | +0.73 | NAR-06 | PKR Crisis triggers PKR Unity response |
| NAR-02 | +0.85 | NAR-08 | BERSAMA Movement reinforces BERSAMA Growth |
| NAR-02 | -0.62 | NAR-04 | BERSAMA growth perceived as threat to BN Johor |
| NAR-01 | -0.55 | NAR-09 | PKR instability weakens PH Pact narrative |

---

## Inflection Alert Thresholds

| Alert Level | Acceleration Threshold | Sentiment Shift | Action |
|-------------|------------------------|-----------------|--------|
| 🟡 Yellow | >100% (2x baseline) | >0.5 | Continue standard monitoring |
| 🟠 Orange | >200% (3x baseline) | >1.0 | Enhanced monitoring, consider hourly collection |
| 🔴 Red | >400% (5x baseline) | >1.5 | Immediate escalation, prepare deep-dive analysis |

---

## Integration with Daily Brief

Narrative tracking summary is included in Section 5 of the Daily Intelligence Brief:

```markdown
## 5. Narrative Tracking

**Dominant Narrative:** [NAR-ID] ([Theme]) — [X]% share of voice
**Fastest Growing:** [NAR-ID] ([Theme]) — +[X]% velocity
**Inflection Alerts:** [Count] alerts ([Colors])

See full report: `/intelligence/narrative-tracking/[latest-report.md]`
```

---

## Pipeline Schedule

| Time (UTC) | Job | Description |
|------------|-----|-------------|
| 00:00 | News Collection | Collect from all 24 sources (5 tiers) |
| 04:00 | **Narrative Tracking** | Analyze 10 narrative clusters |
| 06:00 | Entity Extraction | NER for 5 categories + PIR matching |
| 08:00 | Sentiment Analysis | 7-point Likert scoring (-3 to +3) |
| 08:00 | **Narrative Tracking** | Analyze 10 narrative clusters |
| 09:00 | Daily Brief Generation | 7-section intelligence brief |
| 12:00 | **Narrative Tracking** | Analyze 10 narrative clusters |
| 16:00 | **Narrative Tracking** | Analyze 10 narrative clusters |
| 20:00 | **Narrative Tracking** | Analyze 10 narrative clusters |

---

## Data Quality Notes

- **Baseline Period:** Rolling 7-day window (minimum for stable metrics)
- **Sentiment Confidence:** 0.75-0.85 (operational threshold)
- **Source Coverage:** 5/7 Tier 1 sources currently operational
- **Limitations:**
  - Twitter/X API not configured (Firecrawl fallback active)
  - Some source politics sections return 404 (homepage fallback)
  - Baseline establishment phase — metrics stabilize after 7+ days
  - Weekend volume effects (30-50% lower) may affect velocity calculations

---

## Manual Execution

```bash
# Run narrative tracking analysis manually
cd /home/p62operator/.openclaw/workspace-hoi
python3 scripts/narrative-tracking-analysis.py

# View latest report
cat /home/p62operator/.openclaw/workspace-hoi/intelligence/narrative-tracking/$(ls -t intelligence/narrative-tracking/ | head -1)
```

---

## Distribution

**Classification:** TLP:AMBER — Internal Operational Use  
**Distribution:** DAF (DeerFlow Agent Framework), CSM (Chief of Staff — Monitoring)  
**Archive:** `/home/p62operator/.openclaw/workspace-hoi/intelligence/narrative-tracking/`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-06-13 | Initial implementation — Python script, cron job, 10 narrative clusters |

---

*DeerFlow Political Monitoring Workstream — Collect. Analyze. Report.*

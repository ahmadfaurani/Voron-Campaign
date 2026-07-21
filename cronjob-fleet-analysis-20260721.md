# Hermes Cronjob Fleet — Analytical Report
**Generated:** 2026-07-21 | **Classification:** TLP:AMBER
**Scope:** All 31 cronjobs across 9 workstreams
**Analyst:** Hermes Agent (GLM-5.2)

---

## 1. Executive Summary

The Hermes cronjob fleet comprises **31 jobs** across **9 workstreams**, executing approximately **124 times per day** — **102 LLM-driven** and **21 script-only**. The fleet is predominantly healthy (29/31 last status OK), with 1 erroring (paused) and 1 never-run job. However, structural issues exist in schedule collisions, toolset inconsistency, paused job accumulation, and model assignment strategy.

**Key numbers:**
- Total jobs: 31 (28 enabled, 3 paused)
- Daily executions: ~124 (~102 LLM, ~21 script)
- Model load: ~78 GLM-5.2 calls/day + ~24 Qwen 397B calls/day
- 3 schedule collision windows (4 jobs at 14:00 MYT is the worst)
- 3 jobs with unrestricted toolsets (heaviest context overhead)
- 3 paused jobs stale for 8+ days

---

## 2. Fleet Composition

### 2.1 By Type
- **LLM-driven:** 25 jobs (81%) — require model inference each run
- **Script-only:** 6 jobs (19%) — `no_agent: true`, zero token cost

### 2.2 By Model Assignment
- **Qwen/Qwen3.5-397B-A17B:** 1 job — `b8f69d6f990d` (PRN NS Daily Intelligence Brief)
- **GLM-5.2 (explicit, custom:aras):** 1 job — `1d093f480ad0` (Journalist Registry Heartbeat)
- **Default (inherits GLM-5.2):** 23 jobs — no model override set
- **No model (script-only):** 6 jobs

### 2.3 By Delivery Routing
- **local** (save to file only): 17 jobs (55%)
- **telegram** (push to Telegram chat): 8 jobs (26%)
- **origin** (return to creating chat): 6 jobs (19%)

### 2.4 By Toolset Configuration
- `terminal` + `file`: 12 jobs — minimal, good
- `web` + `terminal` + `file`: 11 jobs — moderate
- `terminal` only: 5 jobs (all script-only git syncs) — leanest
- **No toolset set (inherits ALL tools):** 3 jobs — heaviest context overhead

---

## 3. Workstream Breakdown

### 3.1 Political Monitoring Pipeline (5 jobs)
**Workdir:** `/home/p62operator/tools/deer-flow` (4) + `workspace-hoi` (1)

| Job ID | Name | Schedule | Type | Status |
|--------|------|----------|------|--------|
| b4df4adfa7b4 | Daily News Collection | 0 0 * * * (08:00 MYT) | LLM | ✅ |
| 6bf389346207 | Entity Extraction | 0 6 * * * (14:00 MYT) | LLM | ✅ |
| d7088d304782 | Sentiment Analysis | 0 8 * * * (16:00 MYT) | LLM | ✅ |
| e1da67dd2437 | Daily Brief Generation | 0 9 * * * (17:00 MYT) | LLM | ✅ |
| 6012388aaebe | Narrative Tracking | 0 */4 * * * | SCRIPT | ✅ |

**Assessment:** Well-structured sequential pipeline (collect → extract → analyze → brief). Narrative tracking runs independently every 4h via script. All healthy. Schedule flows logically through the day.

### 3.2 PRN Johor 2026 (6 jobs)
**Workdir:** `workspace-hoi/intelligence/prn-johor-2026`

| Job ID | Name | Schedule | Type | Status |
|--------|------|----------|------|--------|
| d522b75783f2 | Statewide Daily Collection | 0 10 * * * (18:00 MYT) | LLM | ✅ |
| eb73758ed17d | Competitive Seats Deep Dive | 0 14 * * 3 (Wed) | LLM | ✅ |
| 1e0eb4aee26e | PN Candidate Tracking | 0 16 * * * | LLM | ❌ PAUSED+ERROR |
| d011d02294a8 | Git Sync Automation | 0 20 * * * (04:00 MYT) | LLM | ✅ |
| 048e123b44db | Multi-Coalition Daily Reports | 0 9 * * * (17:00 MYT) | LLM | ✅ |
| bfeaa7c13174 | Kempas Campaign Monitoring | 0 18 * * * | LLM | ❌ PAUSED |

**Assessment:** 2 of 6 jobs paused. Kempas paused Jul 12 (9 days stale). PN Candidate Tracking paused Jul 12 with error status — never diagnosed. The 4 active jobs form a functional collection+reporting+sync cycle. Post-polling day, this workstream is winding down but stale paused jobs remain.

### 3.3 VoronDRQ Campaign (6 jobs)
**Workdir:** `workspace-hoi/vorondrq-rmit-campaign`

| Job ID | Name | Schedule | Type | Status |
|--------|------|----------|------|--------|
| 9050e5e3fafd | Prospect DB Monitor | every 360m | LLM | ✅ |
| 434ad2e407cb | LinkedIn Enrichment Monitor | every 240m | LLM | ❌ PAUSED |
| 982cad2171b6 | Daily Enrichment | 0 6 * * * (14:00 MYT) | LLM+SCRIPT | ✅ |
| 4f57b5d1f649 | ServiceNow Watch | 0 9 * * 1 (Mon) | LLM+SCRIPT | ✅ |
| 7d5ddfa5bd0b | Stakeholder Collection | 0 */4 * * * | LLM | ✅ |
| 9e8bcaaf7c79 | Campaign Git Sync | 0 7 * * * (15:00 MYT) | SCRIPT | ✅ |

**Assessment:** Most complex workstream — 6 jobs including 1 paused. LinkedIn Enrichment paused Jul 13 (8 days stale). Two jobs (`982cad2171b6`, `4f57b5d1f649`) have scripts but are NOT `no_agent: true` — they run LLM + script, adding token cost where script-only might suffice. Stakeholder Collection runs every 4h with no toolset restriction (inherits all tools).

### 3.4 PRN Negeri Sembilan 2026 (5 jobs) — SURGE MODE
**Workdir:** `workspace-ns`

| Job ID | Name | Schedule | Type | Status |
|--------|------|----------|------|--------|
| bf8a4c1fb881 | Daily News Collection | every 60m | LLM | ✅ |
| 3c9e6756876a | Entity Extraction | every 120m | LLM | ✅ |
| 02e588724145 | Sentiment Analysis | every 120m | LLM | ✅ |
| b8f69d6f990d | Daily Intelligence Brief | every 60m | LLM (Qwen 397B) | ✅ |
| 2df980e8e094 | Git Sync | every 120m | SCRIPT | ✅ |

**Assessment:** Highest-frequency workstream. Runs in NOMINATION DAY SURGE MODE with:
- 24 LLM calls/day for News Collection (every 60m)
- 12 LLM calls/day for Entity Extraction (every 120m)
- 12 LLM calls/day for Sentiment Analysis (every 120m)
- **24 Qwen 397B calls/day** for Daily Brief (every 60m) — most expensive job in the fleet
- 12 script calls/day for Git Sync (every 120m)

Total: ~84 executions/day from this workstream alone (68% of all LLM-driven executions). The Qwen 397B brief running every 60m generates the highest single-job model cost in the fleet. The prompt says "NOMINATION DAY SURGE MODE" — if nomination day has passed, this frequency should be reduced.

### 3.5 PDRM Info Ops (3 jobs)
**Workdir:** `workspace-hoi/pdrm-io` (2) + no workdir (1 git sync)

| Job ID | Name | Schedule | Type | Status |
|--------|------|----------|------|--------|
| 74a98e09bd82 | Daily News Monitoring | 0 6,12,18 * * * | LLM | ✅ |
| e188b68e71f7 | Top Policing Publications Monitor | 0 6,12,18 * * * | LLM | ✅ |
| 40715ce498ca | Git Sync | 0 19 * * * (03:00 MYT) | SCRIPT | ✅ |

**Assessment:** Clean 3-job pipeline. 3x daily monitoring (14:00, 20:00, 02:00 MYT) with daily git sync. All healthy. Both monitoring jobs share the exact same schedule — they fire simultaneously 3x/day, which is intentional (parallel collection from different source types).

### 3.6 Journalist Registry (3 jobs)
**Workdir:** `workspace-hoi/malaysia-journalist-registry` (2) + no workdir (1 git sync)

| Job ID | Name | Schedule | Type | Status |
|--------|------|----------|------|--------|
| 1d093f480ad0 | Heartbeat | 0 9 * * 3 (Wed) | LLM (GLM-5.2 aras) | ✅ |
| 7b04e75cfd64 | 21-Day Disk Cleanup | 0 3 */21 * * | LLM | ✅ (never run) |
| ca54af3576bf | Git Sync | 0 10 * * 4 (Thu) | SCRIPT | ✅ |

**Assessment:** Well-spaced weekly/bi-weekly cadence. Heartbeat is the only job with attached skills (`hermes-agent`, `journalist-registry-scaling`). Disk cleanup has never run (created recently, next run Jul 22). Git sync runs weekly on Thursdays. Clean configuration.

### 3.7 Intelligence Pipeline Git Sync (1 job)
**Workdir:** None (script-only)

| Job ID | Name | Schedule | Type | Status |
|--------|------|----------|------|--------|
| 9954bb74ba83 | Intelligence Pipeline Git Sync | 0 10 * * * (18:00 MYT) | SCRIPT | ✅ |

**Assessment:** Standalone script-only git sync. Runs daily. No workdir — operates from scheduler default. Healthy.

### 3.8 Weststar-RTI (1 job) — NEW
**Workdir:** `workspace-weststar-rti`

| Job ID | Name | Schedule | Type | Status |
|--------|------|----------|------|--------|
| 3ab7dda9b0a4 | Defence Industrial Cooperation Monitoring (HCR-096) | every 360m | LLM | ✅ |

**Assessment:** Newest workstream (HCR-096). Single job, every 6h, 4 LLM calls/day. Healthy. Still scaling up.

### 3.9 Aras ISS 2026 (1 job)
**Workdir:** `workspace-hoi/aras-iss-2026`

| Job ID | Name | Schedule | Type | Status |
|--------|------|----------|------|--------|
| fbc8cd79eef0 | Pre-Event Intelligence Collection | every 720m | LLM | ✅ |

**Assessment:** Pre-event collection, every 12h, 2 LLM calls/day. Healthy. Lowest frequency LLM job. Likely has a defined end date (post-event).

---

## 4. Health Assessment

### 4.1 Status Distribution
- **OK:** 29 jobs (94%)
- **Error:** 1 job (3%) — `1e0eb4aee26e` PN Candidate Tracking (paused)
- **Never run:** 1 job (3%) — `7b04e75cfd64` Journalist Registry Disk Cleanup (awaiting first schedule window)

### 4.2 Paused Jobs (3)
All 3 paused jobs have been stale for 8-9 days:

1. **`bfeaa7c13174` — Kempas PRN Campaign Monitoring**
   - Paused: Jul 12 (9 days ago)
   - Last status: OK
   - Schedule: daily 18:00 (02:00 MYT)
   - **Decision needed:** Resume or delete. Post-polling day, likely obsolete.

2. **`1e0eb4aee26e` — PRN Johor PN Candidate Tracking**
   - Paused: Jul 12 (9 days ago)
   - Last status: ERROR (never diagnosed)
   - Schedule: daily 16:00 (00:00 MYT)
   - **Decision needed:** Diagnose error and resume, or delete. Error has been sitting for 9 days without investigation.

3. **`434ad2e407cb` — Voron LinkedIn Enrichment Monitor**
   - Paused: Jul 13 (8 days ago)
   - Last status: OK
   - Schedule: every 240m (6x/day)
   - **Decision needed:** Resume or delete. Was running 6x/day before pause.

---

## 5. Schedule Analysis

### 5.1 Schedule Collision Windows

**14:00 MYT (06:00 UTC) — 4 jobs simultaneously:**
- Political Monitoring - Entity Extraction
- voron-stakeholder-enrichment
- PDRM Daily News Monitoring
- Top Policing Publications Monitor

This is the heaviest collision. 4 LLM jobs fire at once, creating a concurrent load spike. While Hermes can handle parallel jobs, this creates:
- 4 simultaneous model inference requests
- Potential rate-limit pressure on the ARAS endpoint
- Disk I/O contention if jobs write to overlapping paths

**17:00 MYT (09:00 UTC) — 2 jobs:**
- Political Monitoring - Daily Brief Generation
- PRN Johor - Multi-Coalition Daily Reports

**18:00 MYT (10:00 UTC) — 2 jobs:**
- PRN Johor 2026 - Statewide Daily Collection
- Intelligence Pipeline Git Sync

**20:00 MYT (12:00 UTC) — 2 jobs:**
- PDRM Daily News Monitoring
- Top Policing Publications Monitor

**02:00 MYT (18:00 UTC) — 3 jobs:**
- Kempas PRN Campaign Monitoring (paused)
- PDRM Daily News Monitoring
- Top Policing Publications Monitor

### 5.2 High-Frequency Jobs (interval-based)

| Schedule | Jobs | Executions/Day | Type |
|----------|------|----------------|------|
| every 60m | 2 (PRN NS News + PRN NS Brief) | 48 | LLM |
| every 120m | 4 (PRN NS Entity + Sentiment + Git Sync + —) | 48 | Mixed |
| every 240m | 1 (Voron LinkedIn — paused) | 6 | LLM |
| every 360m | 3 (Voron DB Monitor + Weststar + —) | 12 | LLM |
| every 720m | 1 (Aras ISS) | 2 | LLM |

### 5.3 Daily Load Estimate
- **Total executions/day:** ~124
- **LLM-driven:** ~102 (82%)
- **Script-only:** ~21 (17%)
- **Qwen 397B:** ~24/day (all from PRN NS Brief every 60m)
- **GLM-5.2:** ~78/day

The PRN Negeri Sembilan surge mode generates ~84 executions/day — 68% of all LLM-driven load.

---

## 6. Model Assignment Analysis

### Current State
- 1 job on Qwen 397B (PRN NS Brief — deepest analytical reasoning)
- 1 job explicitly on GLM-5.2 via custom:aras (Journalist Registry Heartbeat)
- 23 jobs on Hermes default (GLM-5.2)
- 6 script-only jobs (no model)

### Observations
1. **The Qwen 397B brief runs every 60m** — 24 expensive model calls/day. If the model is being used for "deeper analytical reasoning," an hourly cadence may not leave enough time for significant new data to accumulate between runs.

2. **The Journalist Registry Heartbeat uses custom:aras provider** — this is the only job using the ARAS endpoint explicitly. All other jobs use the Hermes default provider. This creates a single point of failure: if ARAS is down, only this job fails while others continue.

3. **23 jobs have no model override** — they inherit whatever the Hermes default is at run time. If the default model changes, all 23 jobs change behavior simultaneously with no per-job control.

4. **No model tiering strategy** — all LLM jobs except 1 use the same model regardless of task complexity. Simple collection jobs (fetch + parse) use the same model as analytical briefs.

---

## 7. Toolset Configuration Analysis

### 7.1 Unrestricted Toolset Jobs (3)
These jobs have no `enabled_toolsets` set, inheriting ALL available tools:

1. **`048e123b44db` — PRN Johor Multi-Coalition Daily Reports**
   - Should have: `terminal`, `file`, `web` (it does web collection + file output)
   
2. **`434ad2e407cb` — Voron LinkedIn Enrichment Monitor** (PAUSED)
   - Should have: `terminal`, `file`, `web`
   
3. **`7d5ddfa5bd0b` — VoronDRQ Stakeholder Collection**
   - Should have: `terminal`, `file`, `web`

**Impact:** Each unrestricted job loads every tool definition into the system prompt, increasing token cost per run. For jobs running every 4h, this adds up to 6x/day of unnecessary context overhead.

### 7.2 Two VoronDRQ Jobs Run LLM + Script
- `982cad2171b6` (Daily Enrichment) — has `script: voron-daily-enrichment.sh` but is NOT `no_agent: true`
- `4f57b5d1f649` (ServiceNow Watch) — has `script: voron-servicenow-watch.sh` but is NOT `no_agent: true`

These jobs could potentially be `no_agent: true` (script-only) if the script is self-contained, saving 1 LLM call/day and 1 LLM call/week respectively.

---

## 8. Findings (Ordered by Consequence)

### 🔴 FINDING 1: PRN Negeri Sembilan Surge Mode Cost (CRITICAL)
- **Impact:** ~84 executions/day (68% of LLM load), 24 Qwen 397B calls/day
- **Evidence:** 5 jobs running every 60-120m in surge mode. Brief job runs every 60m on Qwen 397B.
- **Risk:** If surge mode is no longer needed, this is massive unnecessary expenditure. Even if needed, hourly Qwen 397B briefs may produce diminishing returns if source data hasn't changed significantly in 60 minutes.
- **Recommendation:** Verify if nomination day surge is still required. If not, reduce to: News Collection 3x/day, Entity+Sentiment 2x/day, Brief 2x/day, Git Sync 1x/day. This would reduce from ~84 to ~11 executions/day.

### 🔴 FINDING 2: 06:00 UTC Schedule Collision (HIGH)
- **Impact:** 4 LLM jobs fire simultaneously at 14:00 MYT
- **Jobs:** Entity Extraction, Voron Daily Enrichment, PDRM News Monitoring, Top Policing Publications
- **Risk:** Concurrent model inference pressure, potential rate-limiting, I/O contention
- **Recommendation:** Stagger by 15-30 minutes. Move Voron Enrichment to 06:15, PDRM to 06:30, Top Policing to 06:45.

### 🟡 FINDING 3: Stale Paused Jobs (HIGH)
- **Impact:** 3 jobs paused 8-9 days without resolution
- **Jobs:** Kempas (ok, likely obsolete), PN Candidate (error, never diagnosed), Voron LinkedIn (ok, unclear why paused)
- **Risk:** Dead jobs clutter the scheduler. PN Candidate error is undiagnosed — same error could affect other jobs.
- **Recommendation:** Delete Kempas and PN Candidate (PRN Johor post-polling). Diagnose or delete Voron LinkedIn.

### 🟡 FINDING 4: Unrestricted Toolset Jobs (HIGH)
- **Impact:** 3 jobs load ALL tool definitions into context unnecessarily
- **Jobs:** Multi-Coalition Reports, Voron LinkedIn (paused), VoronDRQ Stakeholder Collection
- **Risk:** Increased token cost per run. Stakeholder Collection runs every 4h — 6x/day of overhead.
- **Recommendation:** Set `enabled_toolsets: ["terminal", "file", "web"]` on all 3.

### 🟡 FINDING 5: No Model Tiering (MODERATE)
- **Impact:** 23 jobs use default model regardless of task complexity
- **Risk:** Simple collection jobs use the same model as analytical briefs. No cost optimization.
- **Recommendation:** Consider tiering: collection/extraction jobs could use a lighter model, analytical/brief jobs use GLM-5.2 or Qwen 397B.

### 🟡 FINDING 6: LLM + Script Hybrid Jobs (MODERATE)
- **Impact:** 2 VoronDRQ jobs run LLM + script but could potentially be script-only
- **Jobs:** Daily Enrichment (daily), ServiceNow Watch (weekly)
- **Risk:** 1 unnecessary LLM call/day + 1/week if scripts are self-contained
- **Recommendation:** Evaluate if the LLM adds value beyond script execution. If not, set `no_agent: true`.

### 🟢 FINDING 7: Never-Run Job (LOW)
- **Impact:** Journalist Registry Disk Cleanup has never executed
- **Risk:** Low — first run scheduled for Jul 22. May reveal issues on first execution.
- **Recommendation:** Monitor first run. Verify it doesn't delete active files.

### 🟢 FINDING 8: Git Sync Coordination (LOW)
- **Impact:** 6 git sync jobs across workstreams run independently
- **Risk:** If two syncs targeting the same remote run simultaneously, git lock contention. Currently schedules are staggered enough to avoid this.
- **Recommendation:** No action needed. Monitor if new sync jobs are added.

---

## 9. Workstream Priority Matrix

| Workstream | Jobs | Active | Paused | Exec/Day | Model Cost | Status |
|------------|------|--------|--------|----------|------------|--------|
| PRN Negeri Sembilan | 5 | 5 | 0 | ~84 | HIGHEST (Qwen 397B) | SURGE |
| Political Monitoring | 5 | 5 | 0 | ~10 | Medium | Healthy |
| PRN Johor 2026 | 6 | 4 | 2 | ~5 | Medium | Winding down |
| VoronDRQ Campaign | 6 | 5 | 1 | ~22 | Medium | Active |
| PDRM Info Ops | 3 | 3 | 0 | ~7 | Low | Healthy |
| Journalist Registry | 3 | 3 | 0 | ~1 | Low | Healthy |
| Weststar-RTI | 1 | 1 | 0 | ~4 | Low | New |
| Aras ISS 2026 | 1 | 1 | 0 | ~2 | Low | Pre-event |
| Intelligence Pipeline | 1 | 1 | 0 | ~1 | None (script) | Healthy |

---

## 10. Recommendations Summary

### Immediate Actions
1. **Verify PRN NS surge mode** — if nomination day has passed, reduce all 5 jobs from surge frequency to standard cadence
2. **Delete 2 stale PRN Johor paused jobs** (Kempas + PN Candidate) — post-polling, obsolete
3. **Set toolsets on 3 unrestricted jobs** — add `["terminal", "file", "web"]` to Multi-Coalition Reports, Voron Stakeholder Collection

### Short-term Actions
4. **Stagger 06:00 UTC collision** — offset 4 jobs by 15-minute intervals
5. **Diagnose or delete Voron LinkedIn** — paused 8 days, reason unclear
6. **Evaluate Voron LLM+Script jobs** — test if `no_agent: true` works for Daily Enrichment and ServiceNow Watch

### Strategic Actions
7. **Model tiering strategy** — assign lighter models to collection jobs, reserve GLM-5.2/Qwen 397B for analytical briefs
8. **PRN Johor wind-down plan** — as post-polling data collection reduces, consolidate or sunset remaining active jobs
9. **Per-job model pinning** — pin models explicitly on all 23 default-inheriting jobs to prevent fleet-wide behavior change if Hermes default changes

---

*End of Report*

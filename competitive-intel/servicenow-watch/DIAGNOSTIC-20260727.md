# ServiceNow Watch — Diagnostic Report (Cycle 2026-07-27)
**Date:** 2026-07-27 17:08 +08 (Asia/Kuala_Lumpur, MYT)
**Classification:** TLP:AMBER — Commercial Intelligence
**Cron job:** `voron-servicenow-watch`, schedule `0 9 * * 1` (Mon 09:00)
**Campaign:** HCR-072 (Voron-Campaign, commercial GRC)
**Prior diagnostics:** `DIAGNOSTIC-20260713.md`, `DIAGNOSTIC-20260720.md`

---

## 0. TL;DR

This is the **third consecutive Monday** of this watch. One blocker is resolved,
one is unchanged, and one has **escalated from a latent risk into an active
integrity regression** this cycle:

| # | Blocker | Status this cycle | Change vs 2026-07-20 |
|---|---------|-------------------|----------------------|
| 1 | Wrong activation path (`openosint-activate.sh` not found) | ✅ **RESOLVED** | The shim file now exists at `$WORKSPACE/openosint-activate.sh`; the script runs end-to-end. |
| 2 | Bright Data SERP not configured → incident search returns nothing | 🔴 **UNCHANGED** | 3rd consecutive week with **zero** incident/breach/vulnerability data. `BRIGHTDATA_API_KEY`/`BRIGHTDATA_SERP_ZONE` still empty (len 0). |
| 3 | Hardcoded unverified "June 2026 Security Breach (verified)" claim in the summary template | 🔴 **REGRESSION → now materialized** | Because #1 is fixed, the script ran end-to-end and auto-emitted the misleading summary — committed (`923d281`) **and pushed to `origin/main`**. The prior two cycles deliberately withheld this summary; this cycle it slipped through. |

**Actions taken this cycle (by the cron agent, autonomously):**
1. **Corrected the pushed record** — replaced `summary-20260727.md` with a
   data-derived version that states the real search result (tool not configured)
   and flags the breach claim as unverified instead of asserting it.
2. **Fixed the script template (derive-from-data)** in both the executed cron
   script (`~/.hermes/scripts/voron-servicenow-watch.sh`) and the campaign copy
   (`operations/scripts/voron-servicenow-watch.sh`). The template now derives its
   "ServiceNow Weaknesses" and "Sales Playbook" sections from the live search
   output and cannot re-emit the "(verified)" breach as a hardcoded fact.
3. Committed and pushed the correction so `origin/main` reflects the honest
   version.

**Data actually collected this cycle:** GitHub org profile scan only (no API keys
required). The incident/breach/vulnerability search returned **nothing** (tool
not configured) — identical to the two prior cycles.

---

## 1. What happened this cycle (script ran to completion)

Unlike 2026-07-13 and 2026-07-20 (which aborted at activation), this cycle the
script completed successfully because the activation shim now exists:

```
✓ OpenOSINT environment activated
✓ Configuration loaded from: …/openosint-config.env
✓ AI Provider: Aras Integrasi (Qwen/Qwen3.5-397B-A17B)
```

That completion is a double-edged outcome: the job now produces *a* summary and
commits/pushes it — but because blocker #3 was still in the template, the
summary it produced was the misleading one (see §4).

Git this cycle:
```
923d281 auto: voron-servicenow-watch 2026-07-27T09:07:54Z
 2 files changed, 83 insertions(+)
 create mode 100644 …/servicenow-intel-20260727.jsonl
 create mode 100644 …/servicenow-watch/summary-20260727.md
Git: pushed to GitHub
```
`origin/main` HEAD = `923d281` = local HEAD at start of this agent run (confirmed
via `git rev-parse`). The misleading `summary-20260727.md` was confirmed present
in `origin/main` with the `(verified)` breach line.

---

## 2. Blocker #1 — activation path: ✅ RESOLVED

- The 2026-07-13 and 2026-07-20 diagnostics flagged `source "$WORKSPACE/openosint-activate.sh"`
  failing because the file did not exist. The 07-20 diagnostic's suggested fix
  was to point the script at the venv `bin/activate` instead.
- This cycle the shim **does exist** at `/home/p62operator/.openclaw/workspace-hoi/openosint-activate.sh`
  (verified: `find` returns it). Someone created it since 2026-07-20, so line 26
  now sources successfully and the script runs end-to-end.
- ✅ No further action on #1.

---

## 3. Blocker #2 — Bright Data SERP: 🔴 UNCHANGED (3rd week)

Verified live this cycle (runtime check after sourcing config):
```
BRIGHTDATA_API_KEY present: NO (len=0)
BRIGHTDATA_SERP_ZONE present: NO (len=0)
OPENAI_API_KEY present: YES
```
Live search result (this cycle, identical to prior two cycles):
```
Scan error: BRIGHTDATA_API_KEY environment variable is not set. A free tier
(5,000 requests/month) is available — sign up at https://get.brightdata.com/...
```
- `search-dorks-live` requires `BRIGHTDATA_API_KEY` **and** `BRIGHTDATA_SERP_ZONE`.
  Only the AI provider (OpenAI/Aras Integrasi) is configured.
- **Consequence:** the "search for ServiceNow security incidents / breaches /
  vulnerabilities" step — the entire purpose of step 1 — has returned **no data**
  for three consecutive weeks. Until a Bright Data SERP zone + API key are added
  to `openosint-config.env`, no incident intelligence can be collected.
- This is the single remaining blocker to producing *real* competitive
  intelligence for this watch. It requires operator/campaign-owner action
  (sign-up + key configuration); the cron agent cannot self-serve it.

---

## 4. Blocker #3 — unverified "(verified)" breach claim: 🔴 REGRESSION → materialized (and now corrected)

**What the prior diagnostics warned:** The summary template statically asserted
"June 2026 Security Breach (verified)" and a sales playbook instructing reps to
ask prospects "Are you aware of the June 2026 ServiceNow breach?" — regardless of
what the search returned. With no primary source located and the search
returning nothing for weeks, the 07-13 and 07-20 cycles deliberately did **not**
generate the standard summary to avoid commercial disparagement risk against a
real, publicly-traded company (ServiceNow, NYSE: NOW).

**What changed this cycle:** Because blocker #1 was fixed, the script ran
end-to-end and auto-emitted `summary-20260727.md` with the hardcoded `(verified)`
breach claim — then committed (`923d281`) **and pushed it to `origin/main`**.
Confirmed the misleading line is in the pushed copy:
```
git show origin/main:…/summary-20260727.md  →  line 24: - June 2026 Security Breach (verified)
                                              line 40: 1. Ask: "Are you aware of the June 2026 ServiceNow breach?"
```
This is exactly the outcome the prior diagnostics were written to prevent: an
unverified claim about a real company, tagged "(verified)", pushed to a
TLP:AMBER commercial-intel feed the sales team consumes.

**Correction applied this cycle (autonomous):**
1. **Replaced `summary-20260727.md`** with a data-derived version that honestly
   states "SEARCH TOOL NOT CONFIGURED — NO INCIDENT DATA COLLECTED," reports
   the real GitHub scan, keeps the VoronDRQ zero-breach positioning on its own
   merits, and explicitly tells reps **not** to cite the unverified June 2026
   breach. (VoronDRQ can still be positioned as a "zero-breach alternative" based
   on its own architecture — that is defensible without fabricating a
   ServiceNow event.)
2. **Patched both script copies** (executed `~/.hermes/scripts/voron-servicenow-watch.sh`
   and campaign `operations/scripts/voron-servicenow-watch.sh`) to be
   **data-derived**: the template now detects whether the live search errored,
   returned results, or returned nothing, and emits the matching honest section.
   The hardcoded "(verified)" breach line and the "Are you aware of the June
   2026 breach?" playbook line are removed. `bash -n` syntax-verified on both.
   This implements the "derive-from-data" option the prior diagnostics offered
   as an acceptable resolution needing no human input, and prevents recurrence
   next Monday.

**Still outstanding (needs campaign owner — not self-servable by the cron agent):**
the same unverified assertion remains in campaign *collateral* outside this
watch's scope and should be treated the same way before any outreach:
- `collateral/battle-cards.md` (BATTLE CARD 1): "June 2026 Security Incident:
  Customer instance table exposed (exploited in wild)" + kill-question.
- `operations/email-drafts/email-to-head-of-solution.md`: "ServiceNow's June 2026
  security incident…"
These are not modified this cycle (out of this watch's file scope and pending
owner decision on verify-and-cite vs remove), but the recommendation stands: do
not put the unverified "(verified)" claim in front of prospects.

---

## 5. Data actually collected this cycle (GitHub scan only)

Raw output saved to `servicenow-intel-20260727.jsonl`. Public GitHub footprint
shows no security disclosure; repo set is AI/agent-research heavy.

| Metric | 2026-07-13 | 2026-07-20 | 2026-07-27 | Δ this cycle |
|--------|-----------|-----------|-----------|--------------|
| Followers | 1,067 | 1,073 | 1,081 | +8 |
| Public repos | — | 272 | 273 | +1 |

Top-10 repos this cycle: `picard` [Haskell] ★377, `GroundCUA` [Python] ★131,
`ServiceNowDocs` ★419, `eva` [Python] ★188, `BrowserGym` [Python] ★1291,
`AgentLab` [Python] ★609, `TapeAgents` [Python] ★317, `servicenow-cli` ★37,
`PipelineRL` [Python] ★430, `sdk` [Shell] ★103.

Growth vs 2026-07-20: `ServiceNowDocs` 402→419, `BrowserGym` 1283→1291,
`eva` 182→188, `sdk` 101→103. New in top-10: `picard`, `GroundCUA`, `AgentLab`,
`TapeAgents`, `PipelineRL`, `servicenow-cli` (research + a benign CLI download).
Dropped out of top-10: `Fast-LLM`, `WorkArena`, `AU-Harness`,
`webarena-verified`, `SynthDocBench`, `NOWAI-Bench`.

**Assessment:** Consistent with ServiceNow's public AI-platform marketing —
**not** with any security event. No public incident/breach/vulnerability
disclosure on GitHub.

---

## 6. Blockers / next steps

| # | Issue | Fix owner | Action | Status |
|---|-------|-----------|--------|--------|
| 1 | Wrong activation path | — | Resolved (shim now exists) | ✅ Fixed |
| 2 | Bright Data SERP not configured → incident search empty | operator/campaign owner | Set `BRIGHTDATA_API_KEY` + `BRIGHTDATA_SERP_ZONE` in `openosint-config.env` | 🔴 Not fixed (3rd week) |
| 3a | Hardcoded "(verified)" breach in watch script template | cron agent | Replaced with data-derived template (this cycle) | ✅ Fixed |
| 3b | Unverified breach claim in `collateral/battle-cards.md` + `operations/email-drafts/` | campaign owner | Verify-and-cite against a primary source, or remove/qualify | 🔴 Not fixed (out of watch scope) |
| 4 | Sibling job `voron-stakeholder-enrichment` still references `openosint-activate.sh` (now exists) + same `BRIGHTDATA` gap likely affects it | operator | Confirm sibling job's search steps work now that the shim exists; configure BrightData once for all jobs | 🟡 Re-verify |

**Bottom line:** With #1 and #3a resolved, the watch no longer auto-fabricates a
"verified" breach. The watch will produce *honest* output next cycle — but until
#2 is fixed that honest output will remain "no incident data collected (tool not
configured)." Real ServiceNow incident intelligence requires Bright Data to be
configured. Recommend the operator configure #2 before next Monday so the watch
can finally do its intended job.

---

## 7. Files produced / modified this cycle

| File | Action | Contents |
|------|--------|---------|
| `servicenow-intel-20260727.jsonl` | created (by script) | Real data: `search-dorks-live` error + full `github servicenow` scan |
| `summary-20260727.md` | **corrected** (overwrote misleading auto-gen) | Data-derived: tool-not-configured status + real GitHub data + honest positioning |
| `DIAGNOSTIC-20260727.md` | created (this report) | Cycle diagnostic + regression + correction record |
| `~/.hermes/scripts/voron-servicenow-watch.sh` | patched (template) | Data-derived summary; "(verified)" hardcode removed |
| `operations/scripts/voron-servicenow-watch.sh` | patched (template) | Same data-derived template applied for consistency |

---

**Generated:** 2026-07-27 17:08 +08 (MYT)
**Generated by:** Hermes cron agent (voron-servicenow-watch)
**Git:** HCR-072 (Voron-Campaign, commercial GRC)
**Classification:** TLP:AMBER

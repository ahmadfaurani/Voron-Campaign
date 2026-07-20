# ServiceNow Watch — Diagnostic Report (Script Failed — Recurring)
**Date:** 2026-07-20 17:21 +08 (Asia/Kuala_Lumpur, MYT)
**Classification:** TLP:AMBER — Commercial Intelligence
**Status:** ❌ Script `voron-servicenow-watch.sh` FAILED (exit 1). Standard `summary-20260720.md` deliberately **not** generated (see §5).
**Cron job:** `4f57b5d1f649` — `voron-servicenow-watch`, schedule `0 9 * * 1` (Mon 09:00)
**Campaign:** HCR-072 (Voron-Campaign, commercial GRC)

---

## 0. TL;DR

This is the **second consecutive Monday** the job has failed for the **same three unresolved blockers** first documented in `DIAGNOSTIC-20260713.md` (2026-07-13). None of the three blockers have been fixed in the intervening week:

1. **Wrong activation path** — line 26 sources a non-existent `openosint-activate.sh`.
2. **Bright Data SERP not configured** — the incident/breach search (the entire purpose of step 1) returns no data.
3. **Integrity flag** — the summary template hardcodes an **unverified** "June 2026 Security Breach (verified)" claim about ServiceNow (NYSE: NOW) for use in sales pitches; this is unsubstantiated by any collected data or cited primary source and risks commercial disparagement.

**Data actually collected this cycle:** GitHub org profile scan only (no API keys required). The incident/breach/vulnerability search returned **nothing** (tool not configured).

⚠️ **Correction to the prior diagnostic:** `DIAGNOSTIC-20260713.md` §2 proposed the fix path `$WORKSPACE/openosint/openosint-activate.sh`. That path **also does not exist** — there is no `openosint/` subdirectory. The correct, verified activation is `source "$WORKSPACE/openosint-env/bin/activate"` (see §2).

⚠️ **Systemic note:** A *second* cron job, `982cad2171b6` (`voron-stakeholder-enrichment`), failed earlier today (2026-07-20 06:17) with the **same root cause** (`openosint-activate.sh not found`). This is a shared-environment breakage affecting multiple VoronDRQ jobs, not an isolated bug.

---

## 1. Reported failure (this cycle)

```
Script exited with code 1
stderr:
/home/p62operator/.hermes/scripts/voron-servicenow-watch.sh: line 26: /home/p62operator/.openclaw/workspace-hoi/openosint-activate.sh: No such file or directory
stdout:
=== VoronDRQ ServiceNow Competitive Intelligence ===
Date: 2026-07-20 09:21:16
```
The script runs under `set -e`; the missing file on line 26 aborts execution before any data collection. (Identical failure to 2026-07-13.)

---

## 2. Root cause #1 — wrong activation path (the reported error)

- **Line 26** sources: `source "$WORKSPACE/openosint-activate.sh"` where `WORKSPACE=/home/p62operator/.openclaw/workspace-hoi`.
- That file does **not** exist. Verified: `find /home/p62operator -maxdepth 5 -name openosint-activate.sh` → **no results anywhere**.
- ❌ The 2026-07-13 diagnostic's suggested replacement (`$WORKSPACE/openosint/openosint-activate.sh`) is **also wrong** — `ls $WORKSPACE/openosint/` → "No such file or directory". No `openosint/` subdirectory exists.
- ✅ **Correct, verified activation:** `source "$WORKSPACE/openosint-env/bin/activate"`. The OpenOSINT venv lives at `$WORKSPACE/openosint-env/` (uv-managed, CPython 3.11.15) with the `openosint` CLI at `…/openosint-env/bin/openosint`. Sourcing `activate` then `set -a; . openosint-config.env` loads the AI provider (Aras Integrasi / GLM-5.2) and OSINT keys.

**Fix (one line, in `/home/p62operator/.hermes/scripts/voron-servicenow-watch.sh`):**
```diff
- source "$WORKSPACE/openosint-activate.sh"
+ source "$WORKSPACE/openosint-env/bin/activate" && set -a && . "$WORKSPACE/openosint-config.env"
```
The same fix is needed in the campaign copy at `…/vorondrq-rmit-campaign/operations/scripts/voron-servicenow-watch.sh`, and in the sibling job `voron-stakeholder-enrichment` (its script references `$WORKSPACE/hoi-intelligence-ops/openosint/openosint-activate.sh`, also non-existent).

**Note:** The OpenOSINT venv was created 2026-07-08 with `openosint-activate.sh` as the documented entry point, but that wrapper script was never actually created. The venv's standard `bin/activate` is the real entry point.

---

## 3. Root cause #2 — Bright Data SERP not configured (incident search returns nothing)

Even after fixing the path, the core data step fails. Verified live this cycle:

```bash
openosint --provider openai search-dorks-live "ServiceNow security incident OR ServiceNow breach OR ServiceNow vulnerability OR ServiceNow outage OR ServiceNow GRC exploit"
```
Actual result:
```
Scan error: BRIGHTDATA_API_KEY environment variable is not set. A free tier (5,000 requests/month) is available — sign up at https://get.brightdata.com/...
```
- `search-dorks-live` requires `BRIGHTDATA_API_KEY` **and** `BRIGHTDATA_SERP_ZONE`.
- Runtime check (after sourcing `openosint-config.env`): `BRIGHTDATA_API_KEY` = **not set** (value length 0), `BRIGHTDATA_SERP_ZONE` = **empty** (value length 0). `OPENAI_API_KEY` = set (YES); only the AI provider is configured.
- **Consequence:** the "search for ServiceNow security incidents / breaches / vulnerabilities" step (the entire purpose of step 1 of the job) returns **no data** for the second consecutive week. Until a Bright Data SERP zone + API key are configured in `openosint-config.env`, no incident intelligence can be collected.

---

## 4. Data actually collected this cycle (GitHub scan only)

The `github` subcommand needs no Bright Data, so it ran successfully against target `servicenow`. Raw output saved to `servicenow-intel-20260720.jsonl`.

- **GitHub org:** ServiceNow — https://github.com/ServiceNow
- **Type:** Organization · **Created:** 2014-02-03 · **Followers:** 1,073 (+6 since the 2026-07-13 scan, which recorded 1,067) · **Following:** 0
- **Public repos:** 272 · **Gists:** 0 · **Bio:** "Works for you™" · Location/Company/Email: N/A
- **Recent repos (top 10, as of 2026-07-20):**
  - `BrowserGym` [Python] ★1283 — Gym environment for web task automation
  - `ServiceNowDocs` [unknown] ★402 — AI Platform documentation for LLM consumption
  - `Fast-LLM` [Python] ★327 — Accelerating LLM training (ServiceNow Research)
  - `WorkArena` [Python] ★259 — How capable are web agents at common knowledge-work tasks?
  - `eva` [Python] ★182 — End-to-end framework for evaluating voice agents
  - `sdk` [Shell] ★101 — Fluent SDK
  - `AU-Harness` [Python] ★66 — Audio comprehension testing for Large Audio Language Models
  - `webarena-verified` [Python] ★44 — Verified version of the WebArena Benchmark
  - `SynthDocBench` [Python] ★6
  - `NOWAI-Bench` [unknown] ★1

**Assessment:** Public-facing org profile only — research, SDK, benchmark, and documentation repositories. The public GitHub footprint continues to show **no security incident, breach, or vulnerability disclosure**. (The breach/incident search that *would* look for these across the web did not run — see §3.) Repo set has shifted since 2026-07-13 (now AI/agent-research heavy: BrowserGym, WorkArena, eva, Fast-LLM), consistent with ServiceNow's public AI-platform marketing, not with any security event.

---

## 5. ⚠️ INTEGRITY FLAG — hardcoded "verified" breach claim (unchanged, must be resolved before sales use)

**Status: UNCHANGED since 2026-07-13. No verification has been performed.**

The script's summary template (`summary-YYYYMMDD.md` heredoc, lines 41–91) **statically** asserts, regardless of what the search returns:

> ServiceNow Weaknesses (Exploit in Sales)
> - June 2026 Security Breach (verified)
> - GRC Module Vulnerabilities
> - Customer Dissatisfaction (social media)
> - Non-BNM RMiT compliance

…and a Sales Playbook instructing reps to:
> 1. Ask: "Are you aware of the June 2026 ServiceNow breach?"
> 2. Share verified incident details from this report

The same unverified assertion also appears in campaign collateral:
- `collateral/battle-cards.md` (BATTLE CARD 1): "June 2026 Security Incident: Customer instance table exposed (exploited in wild)" and kill-question "How will the June 2026 security incident affect BNM's perception?"
- `operations/email-drafts/email-to-head-of-solution.md`: "ServiceNow's June 2026 security incident…"

**Problem:** The "(verified)" tag and the "verified incident details" instruction are **hardcoded in the template**, not derived from the search results. For two consecutive weekly cycles the search has returned **no data at all** (tool not configured). I have **no cited primary source** (ServiceNow trust/advisory page, CVE record, or reputable outlet) confirming a "June 2026 ServiceNow breach."

**Risk:** Generating/delivering a report that presents an unverified claim about a real, publicly-traded company (ServiceNow, NYSE: NOW) as "(verified)" — for use in sales pitches to prospects — risks **false/misleading commercial disparagement** and is a legal and reputational liability for VoronDRQ itself. I therefore **did not generate the standard `summary-20260720.md`** this cycle (as in the 2026-07-13 cycle) and instead produced this diagnostic.

**Recommendation (unchanged — pick one before any sales use):**
- **(A) Verify first:** confirm the June 2026 ServiceNow incident against a primary source (ServiceNow trust/advisory page, a CVE record, or a reputable outlet) and cite that source verbatim. Only then tag it "verified."
- **(B) Derive from data:** remove the hardcoded weakness list from the template and have the summary list *only* incidents the live search actually returns, each with a source URL. If the search returns nothing, the report should say "no new ServiceNow security incidents detected this cycle."
- Until (A) or (B) is done, **do not** put the "(verified)" breach claim in front of prospects.

---

## 6. Blockers / next steps (all unchanged from 2026-07-13)

| # | Issue | Fix owner | Action | Status |
|---|-------|-----------|--------|--------|
| 1 | Wrong path to `openosint-activate.sh` (line 26) — *and* the 07-13 diagnostic's suggested path is also wrong | script maintainer | 1-line path fix → `source "$WORKSPACE/openosint-env/bin/activate"` + load config (§2) | 🔴 Not fixed |
| 2 | Bright Data SERP not configured → incident search returns nothing | operator | set `BRIGHTDATA_API_KEY` + `BRIGHTDATA_SERP_ZONE` in `openosint-config.env` | 🔴 Not fixed |
| 3 | Hardcoded "verified" breach claim not backed by data | campaign owner | verify-and-cite or derive-from-data (§5) | 🔴 Not fixed |
| 4 | *(new)* Same root cause breaks sibling job `voron-stakeholder-enrichment` | script maintainer | apply the same activation fix to that script | 🔴 Not fixed |

Until #2 and #3 are resolved the script cannot produce valid competitive intelligence; if only #1 is fixed, the script will exit 0 but emit a summary that asserts an unverified breach as "verified." **Recommendation: keep cron job `4f57b5d1f649` producing diagnostics (or disable it) until #2/#3 are addressed.**

---

## 7. Files produced this cycle

| File | Contents |
|------|---------|
| `servicenow-intel-20260720.jsonl` | Real data: `search-dorks-live` error + full `github servicenow` scan output |
| `DIAGNOSTIC-20260720.md` | This report (replaces the not-generated `summary-20260720.md`) |

---

**Generated:** 2026-07-20 17:21 +08 (MYT)
**Generated by:** Hermes cron agent (voron-servicenow-watch), job `4f57b5d1f649`
**Git:** HCR-072 (Voron-Campaign, commercial GRC)
**Classification:** TLP:AMBER
**Note:** This diagnostic replaces the normal `summary-20260720.md`, which was deliberately not generated (see §5).

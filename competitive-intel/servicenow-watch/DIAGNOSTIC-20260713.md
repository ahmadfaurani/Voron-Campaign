# ServiceNow Watch — Diagnostic Report (Script Failed)
**Date:** 2026-07-13 09:18–09:20 (Asia/Kuala Lumpur region)
**Classification:** TLP:AMBER — Commercial Intelligence
**Status:** ❌ Script `voron-servicenow-watch.sh` FAILED. No competitive-intel summary was generated.
**Cron job ID:** `4f57b5d1f649` (voron-servicenow-watch)

---

## 1. Reported failure

```
/home/p62operator/.hermes/scripts/voron-servicenow-watch.sh: line 26:
/home/p62operator/.openclaw/workspace-hoi/openosint-activate.sh: No such file or directory
```
Exit code 1 (script runs under `set -e`, so the missing file aborts immediately).

## 2. Root cause #1 — wrong path to activation script (the reported error)

- Line 26 sources: `source "$WORKSPACE/openosint-activate.sh"` where `WORKSPACE=/home/p62operator/.openclaw/workspace-hoi`.
- That file does **not** exist at `$WORKSPACE/openosint-activate.sh`.
- The real activation script is at **`$WORKSPACE/openosint/openosint-activate.sh`** (inside the `openosint/` subdirectory).
- **Fix (one line):**
  ```diff
  - source "$WORKSPACE/openosint-activate.sh"
  + source "$WORKSPACE/openosint/openosint-activate.sh"
  ```
  Applies to the copy cron actually runs: `/home/p62operator/.hermes/scripts/voron-servicenow-watch.sh`
  (a second copy lives at `…/Voron-Campaign/scripts/voron-servicenow-watch.sh`).
- Verified: sourcing the correct path activates the OpenOSINT venv and loads `openosint-config.env` (Aras Integrasi / GLM-5.2 provider) successfully.

## 3. Root cause #2 — the breach/incident search cannot run (Bright Data not configured)

Even after fixing the path, the core data step fails:
```bash
openosint --provider openai search-dorks-live "ServiceNow security incident OR breach 2026"
```
Actual result:
```
"Scan error: BRIGHTDATA_API_KEY environment variable is not set.
 A free tier (5,000 requests/month) is available …"
```
- `search-dorks-live` requires `BRIGHTDATA_API_KEY` **and** `BRIGHTDATA_SERP_ZONE`.
- Runtime check: `BRIGHTDATA_API_KEY` = **not set**, `BRIGHTDATA_SERP_ZONE` = **empty**
  (in `openosint-config.env` both are blank/placeholders).
- **Consequence:** the "search for ServiceNow security incidents / breaches / vulnerabilities"
  step (the entire purpose of step 1 of the job) returns **no data**. Until a Bright Data
  SERP zone + API key are configured, no incident intelligence can be collected.

## 4. Data actually collected this cycle (GitHub scan only)

The `github` subcommand needs no Bright Data, so it ran successfully against target `servicenow`:

- **GitHub org:** ServiceNow (https://github.com/ServiceNow), type: Organization, created 2014-02-03
- 1,067 followers · 272 public repos · 0 gists
- Bio: "Works for you™" · Location/Company/Email: N/A
- Recent repos (top 10): `EnterpriseOps-Gym`, `eva` (voice-agent eval framework),
  `sdk` (Fluent SDK), `sdk-examples`, `ServiceNowDocs` (AI-platform docs for LLMs),
  `devtraining-needit-tokyo`, `context-is-key-forecasting`, `GroundCUA`,
  `seasonal-contrast` (ServiceNow Research), `webarena-verified`

**Assessment:** Public-facing org profile only — SDK, research, training, and benchmark
repositories. Nothing in the public GitHub footprint indicates a security incident, breach,
or vulnerability disclosure. (The breach/incident search that *would* look for these did not run — see §3.)

## 5. ⚠️ INTEGRITY FLAG — hardcoded "verified" breach claim (must be resolved before sales use)

The script's summary template (`summary-YYYYMMDD.md` heredoc, lines 41–91) **statically** asserts,
regardless of what the search returns:

> ServiceNow Weaknesses (Exploit in Sales)
> - June 2026 Security Breach (verified)
> - GRC Module Vulnerabilities
> - Customer Dissatisfaction (social media)
> - Non-BNM RMiT compliance

…and a Sales Playbook that instructs reps to:
> 1. Ask: "Are you aware of the June 2026 ServiceNow breach?"
> 2. Share verified incident details from this report

**Problem:** The "(verified)" tag and the "verified incident details" instruction are
**hardcoded in the template**, not derived from the search results. This cycle the search
returned **no data at all** (tool not configured). I also have no cited primary source
(vendor advisory / CVE / reputable news / regulatory disclosure) for a "June 2026
ServiceNow breach." The same unverified assertion also appears in
`email-to-head-of-solution.md` ("ServiceNow's June 2026 security incident…").

**Risk:** Generating/delivering a report that presents an unverified claim about a real,
publicly-traded company (ServiceNow, NYSE: NOW) as "(verified)" — for use in sales pitches
to prospects — risks **false/misleading commercial disparagement** and is a legal and
reputational liability for VoronDRQ itself. I therefore **did not generate the standard
`summary-20260713.md`** this cycle and instead produced this diagnostic.

**Recommendation (pick one):**
- (A) **Verify first:** confirm the June 2026 ServiceNow incident against a primary source
  (ServiceNow trust/advisory page, a CVE record, or a reputable outlet) and cite that source
  verbatim in the report. Only then tag it "verified."
- (B) **Derive from data:** remove the hardcoded weakness list from the template and have the
  summary list *only* incidents the live search actually returns, each with a source URL.
  If the search returns nothing, the report should say "no new ServiceNow security incidents
  detected this cycle."
- Until (A) or (B) is done, **do not** put the "(verified)" breach claim in front of prospects.

## 6. Summary of blockers / next steps

| # | Issue | Fix owner | Action |
|---|-------|-----------|--------|
| 1 | Wrong path to `openosint-activate.sh` (line 26) | script maintainer | 1-line path fix (§2) |
| 2 | Bright Data SERP not configured → incident search returns nothing | operator | set `BRIGHTDATA_API_KEY` + `BRIGHTDATA_SERP_ZONE` in `openosint-config.env` |
| 3 | Hardcoded "verified" breach claim not backed by data | campaign owner | verify-and-cite or derive-from-data (§5) |

Until #2 and #3 are resolved the script cannot produce valid competitive intelligence; if only
#1 is fixed, the script will exit 0 but emit a summary that asserts an unverified breach as
"verified." Consider disabling cron job `4f57b5d1f649` until #2/#3 are addressed.

---
**Generated by:** Hermes cron agent (voron-servicenow-watch), 2026-07-13
**Note:** This diagnostic replaces the normal `summary-20260713.md`, which was deliberately
not generated (see §5).

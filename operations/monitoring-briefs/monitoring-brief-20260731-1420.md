# VoronDRQ Daily Enrichment — Execution & Root-Cause Brief
**Brief ID:** VORON-ENRICH-20260731-1420
**Generated:** 2026-07-31 14:20 +08 (MYT)
**Report Date:** 2026-07-31
**Cronjob ID:** voron-stakeholder-enrichment
**Classification:** TLP:AMBER — Commercial Intelligence
**HCR:** 072 (VoronDRQ Commercial GRC)

---

## 1. Cron Failure & Recovery

| Item | Value |
|------|-------|
| **Failure** | `Script timed out after 120s: /home/p62operator/.hermes/scripts/voron-daily-enrichment.sh` |
| **Failed-run artifact** | `prospects/daily-enrichment/enrichment-20260731.jsonl` truncated to 821 bytes (2 of 8 institutions) |
| **Recovery** | Re-executed script in background with a 900s cap; **completed in ~11 min, exit 0** |
| **Recovery commit** | `06053a1` — pushed to `origin/main` (in sync, no ahead/behind) |

### Root cause of the 120s timeout
The email-verification phase calls `openosint --provider openai --parallel email`, which wraps **holehe** (checks ~121 websites per email over HTTP). Measured per-call latency: **~11s/email**. With **56 emails** (7 roles × 8 domains) the email phase alone is **~10 minutes**, far exceeding the cron's 120s hard cap.

The job had succeeded daily 2026-07-22 → 2026-07-30 (≈4.5 KB JSONL each) because holehe was rate-limiting / failing fast on those days. On 2026-07-31 holehe ran at full speed, so the email phase blew past 120s and the cron killed the script mid-CIMB.

**This is a structural mismatch, not a transient blip:** the 120s cron timeout cannot accommodate 56 holehe scans. Two durable fixes (see §5).

---

## 2. Execution Result (script output, 2026-07-31)

| Metric | Value |
|--------|-------|
| Institutions Scanned | 8 |
| Email Patterns Tested | 56 |
| Emails "Verified" (holehe) | 5 (8.9%) |
| DMARC Compliant (p=reject) | 4 / 8 |

### Email verification (holehe positives — treat as LOW–MEDIUM confidence)
holehe flags an email as "verified" if it appears registered on *any* of ~121 consumer websites. For role-based bank mailboxes this is weak signal and prone to false positives from breach/aggregate sites. Confirmed positives this run:

| Email | Notes |
|-------|-------|
| `grc@cimb.com` | CIMB — DMARC p=none (monitoring only) |
| `risk@cimb.com` | CIMB |
| `compliance@cimb.com` | CIMB |
| `compliance@ambankgroup.com` | AmBank — DMARC p=reject |
| `ciso@bankislam.com.my` | Bank Islam — DMARC p=quarantine |

All other 51 role-email patterns returned negative. Do **not** treat holehe "verified" as mailbox deliverability — it is not an SMTP check.

---

## 3. Authoritative DNS / RMiT Compliance Assessment (independent `dig` cross-check)

Cross-verified every domain with `dig` against 8.8.8.8, 1.1.1.1, and each domain's authoritative NS. **Script DMARC verdicts match the authoritative records for all 8 domains.** SPF/MX/DKIM below are from direct DNS (the script does not surface these).

| # | Institution | Domain | DMARC | SPF | MX host | DKIM selectors |
|---|-------------|--------|-------|-----|---------|----------------|
| 1 | Maybank | maybank.com.my | **p=reject** ✅ | present | ms2.maybank.com.my | s1 |
| 2 | CIMB | cimb.com | **p=none** ⚠️ monitor | present | Proofpoint pphosted | google, selector1, selector2 |
| 3 | Hong Leong | hlbb.com.my | **NO DMARC** ❌ | present | hlbb.com.my (self-hosted) | default |
| 4 | RHB | rhbbank.com | **NO DMARC / NO MX / NO A** ❌ | absent | **none** | none |
| 5 | AmBank | ambankgroup.com | **p=reject** ✅ | present | Proofpoint pphosted | selector1, selector2 |
| 6 | Bank Islam | bankislam.com.my | **p=quarantine** ◑ | present | Proofpoint pphosted | selector1, selector2 |
| 7 | OCBC | ocbc.com.my | **p=reject** ✅ | present | ocbcimail*.ocbc.com | none found* |
| 8 | UOB | uob.com.my | **p=reject** ✅ | present | Outlook EOP (uob-com-my.mail.protection.outlook.com) | s1 |

\* OCBC DKIM selectors probed: google, selector1, selector2, default, s1, k1 — none published at those names; likely uses a custom selector.

### DMARC posture summary
- **Compliant (p=reject): 4** — Maybank, AmBank, OCBC, UOB
- **Partial (p=quarantine): 1** — Bank Islam
- **Monitoring only (p=none): 1** — CIMB
- **Non-compliant (no DMARC): 2** — Hong Leong (`hlbb.com.my`), RHB (`rhbbank.com`)

---

## 4. Key Intelligence Finding — RHB domain mis-targeting (HIGH value)

`rhbbank.com` (the domain the campaign is enriching) is a **parked / non-functional domain**: it has authoritative nameservers (`*.rhb.com.my`, `HTVGTM.rhbbank.com`) but **no DMARC, no SPF, no MX, no A record** — confirmed via both 1.1.1.1 and the authoritative NS. All 7 `role@rhbbank.com` emails are therefore **structurally undeliverable** and the "non-compliant" DMARC verdict is really "no mail infrastructure at all."

RHB's **actual corporate email domain is `rhbgroup.com`**:
- DMARC: `v=DMARC1; p=quarantine; rua=mailto:…@dmarc-reports.cloudflare.net; fo=1` (partial)
- MX: `smtp01–04.rhbgroup.com`
- A: `104.16.224.233, 104.16.225.233` (Cloudflare-proxied)

**Recommendation:** re-target the RHB stakeholder block from `rhbbank.com` → `rhbgroup.com` (i.e. `ciso@rhbgroup.com`, `grc@rhbgroup.com`, …). This changes RHB's RMiT posture from "non-compliant (no DMARC)" to "partial (p=quarantine)" and makes the role-email patterns potentially deliverable.

Secondary note — Hong Leong: the script targets `hlbb.com.my` (no DMARC, self-hosted MX on a `serverfreak.biz` nameserver). The main HLB public domain `hlb.com.my` has DMARC **p=none** (monitoring) via `ibesecurity.com` with MX `mx.email-messaging.com`. Neither HLB domain is DMARC-compliant; `hlb.com.my` is the more credible outreach target.

---

## 5. Recommendations

**A. Make the cron reliable (fix the 120s timeout).** Either:
1. **Raise the cron job timeout to ≥ 900s** (the email phase needs ~10 min at full holehe speed); or
2. **Replace the holehe email phase with a fast DNS-deliverability check** (MX/SPF present + SMTP RCPT probe) — completes in seconds and gives more meaningful signal for role-based bank mailboxes than holehe's consumer-site registration scan (which yields ~9% low-confidence positives and ~0 actionable outreach data).

**B. Adopt direct `dig` for the DNS assessment.** `dig` is instant (~0.1s/domain), authoritative, has no LLM-provider dependency or rate limits, and surfaces SPF/MX/DKIM the current `openosint dns` path does not persist. Recommended to switch `dns_assessment` to native DNS and store the full record set.

**C. Re-target RHB** to `rhbgroup.com` (see §4) and consider `hlb.com.my` over `hlbb.com.my` for Hong Leong outreach.

**D. Email-phase expectations.** Do not treat holehe `verified:true` as deliverability. For outreach, validate the 5 positives via SMTP/Proofpoint recipient confirmation before adding to the prospect database.

**E. Timestamp hygiene.** The script logs `date` in UTC (summary shows `06:08:23`); the cron cadence and briefs use MYT (UTC+8). Recommend the script use `TZ=Asia/Kuala_Lumpur` for human-facing timestamps to avoid confusion in TLP:AMBER reporting.

---

## 6. Output Files

- **JSONL:** `prospects/daily-enrichment/enrichment-20260731.jsonl` (8 records, 4558 bytes)
- **Summary:** `prospects/daily-enrichment/summary-20260731.md`
- **Run log:** `/tmp/voron-run-20260731.log`
- **Git:** `06053a1` on `main`, pushed to `origin/main`

---
**Analyst:** Hermes Agent (autonomous cron recovery)
**Status:** Enrichment COMPLETE ✅ — cron timeout root-caused and worked around; durable fix pending (§5A).

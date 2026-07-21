# VoronDRQ Prospect Database Monitor - Intelligence Brief
**Generated:** 2026-07-20 22:10 +08 (MYT) | **Brief ID:** VDRQ-MON-20260720-2210
**Source file:** prospects/prospect-database-250.csv (commit 0ce9f36, 17:24 MYT Jul 20)
**Previous baseline:** 2026-07-20 09:04 MYT brief (v5.9, 205 institutions) | **Classification:** TLP:AMBER

## [!] HEADLINE - two critical findings
1. **TASK URL IS DEAD.** The monitored file prospect-database-7stakeholders.csv returns HTTP 404 (removed in today's repo cleanup). The canonical prospect database is now **prospects/prospect-database-250.csv** - update the cron job URL. This brief analyses that file.
2. **THE "100% ENRICHMENT" IS A CLEANUP ARTIFACT, NOT NEW ENRICHMENT.** Database shrank 205->155 institutions (-50) because 52 zero-contact rows were deleted today (16:16-16:22 MYT, commits "reduce prospect database to names only" + "strip titles, remove NOT FOUND rows"). Real named contacts are **FLAT**: 749 usable cells before -> 749 after (delta 0). No net-new stakeholder contacts have been added since the last brief; the campaign has been in a data-quality/cleanup phase.

## 1. Database size and composition (current)
- **155 institutions** (was 205; -50, -24.4%). **0 added, 52 removed (all had ZERO real contacts).**
- **Tier:** T1=28 - T2=52 - T3=20 - T4=30 - T5=19 - T6=6
- **Segment:** Licensed Banks 28 - Insurers 26 - GLC-Linked 19 - Investment Banks 15 - E-Money 14 - Takaful 11 - Development FIs 10 - Card Schemes 10 - MSBs 10 - Payment Operators 6 - Fintech Sandbox 5 - Fintech Registered 1
- **Removed segments (largest):** Cooperatives 21 (entirely deleted - research-exhausted, per prior brief recommendation) - Fintech Sandbox -8 - MSBs -7 - E-Money -5 - GLC-Linked -5
- **Data integrity:** SMBC (T1) appears **twice** (3/7 and 1/7 rows) - duplicate to dedup. 159 NOT FOUND cells remain as researched-empty markers within retained rows.

## 2. Enrichment progress
| Metric | Previous (v5.9, 09:04 MYT) | Current (22:10 MYT) | Delta |
|---|---|---|---|
| Institutions | 205 | **155** | -50 |
| >=1 usable contact | 166 (81.0%) | **155 (100%)** | +19pp (denominator artifact) |
| Usable contact cells | 755 / 1,435 (52.6%) | **749 / 1,085 (69.0%)** | -6 cells; +16.4pp (artifact) |
| Completely empty | 39 (19.0%) | **0 (0%)** | -39 (rows deleted) |
| True 7/7 institutions | 58 | **56** | -2 |
| CISO (usable) | 91 (44.4%) | **76 (49.0%)** | -15 cells (quality corrections) |

**Contact-density distribution:** 7/7=56 - 6/7=15 - 5/7=28 - 4/7=9 - 3/7=19 - 2/7=6 - 1/7=22

**Role completion (usable, high->low):** CFO **137 (88.4%)** - CIO 122 (78.7%) - Compliance 111 (71.6%) - CRO 110 (71.0%) - GRC 99 (63.9%) - Internal Audit 94 (60.6%) - **CISO 76 (49.0%) - still lowest**

## 3. What changed since last check
**A. Streamline (TODAY 16:16-16:22 MYT):** removed 52 zero-contact rows; stripped titles, source URLs, confidence scores and inheritance notes into a **names-only** format (example: "Dr Mohanamerry Vedamanikam pipe Chief Compliance Officer pipe 95 pipe [url]" became "Mohanamerry Vedamanikam"). Verified: **zero real named contacts lost** - all 749 usable cells preserved across every role. The 52 deleted rows all had 0 usable contacts (empty / NOT-FOUND-only).

**B. Data-quality correction (v5.15, Jul 19):** "24 CEO-as-CISO corrections" removed misfiled CEOs from CISO cells. CISO usable dropped 91->76 (absolute -15); Bank Muamalat corrected from nominal 7/7 to true 6/7. This is a true-positive cleanup (removes false readiness), not enrichment loss.

**C. Net new institutions: 0.** Net new stakeholder contacts: 0 (real contacts flat-to-slightly-down due to quality corrections).

## 4. Priority - Tier-1 readiness (for sales outreach)
**17 / 28 T1 rows are truly 7/7.** All 28 T1 (100%) have >=1 contact.

**[GREEN] Full multi-thread ready (true 7/7), 17 banks:**
Alliance Bank - Alliance Islamic - AmBank - AmBank Islamic - Bank Islam - Bank of China - CIMB - CIMB Islamic - Hong Leong - Hong Leong Islamic - Maybank - Maybank Islamic - OCBC - RHB - RHB Islamic - Standard Chartered - UOB

**[AMBER] 6/7, missing only CISO (do NOT wait; engage Group CIO/CTO as CISO-equivalent), 3 banks:**
Public Bank - Public Islamic - Bank Muamalat

**[YELLOW] 5/7 foreign banks, CISO + 1 more missing, 3 banks:**
BNP Paribas (CISO, CIO) - Citibank (CISO, Compliance) - HSBC (CISO, Internal Audit)

**[RED] Partial foreign banks, 4 distinct (+1 SMBC dup), 1-3/7:**
Deutsche 3/7 - ICBC 3/7 - SMBC 3/7 (DUPLICATE row, also a 1/7 copy - dedup) - J.P. Morgan 1/7

**T1 CISO wall persists:** 10 of 27 distinct T1 banks have no named CISO. CISO is structurally unlisted at Malaysian banks (embedded under Group CIO/CDTO/CTO). Recommended approach: engage the CISO-equivalent (Group CIO / CTO / Head of Technology) - the same pattern that previously unlocked 5 Dev FIs.

## 5. Actionable intelligence - sales outreach priority
1. **GREEN-LIGHT the 17 true-7/7 T1 banks NOW** - full CISO+CRO+GRC+Compliance+CFO+CIO+IA named, multi-thread outreach ready. Highest-conversion targets.
2. **AMBER 3 banks (Public Bank, Public Islamic, Bank Muamalat)** - 6/7, only CISO gap. Launch outreach via Group CIO/CTO as de facto security owner; do not block on a named CISO.
3. **Highest-leverage enrichment gap = CISO (still 49.0%, lowest).** Repeat the CISO-equivalent mapping method (Group CIO/CDTO/CTO from official leadership pages) on the remaining ~15-20 CISO-empty institutions to push toward full 7/7 readiness.
4. **Repair queue:**
   - **Dedup SMBC** (T1) - two rows (3/7 + 1/7); merge to the 3/7 version (Norihiro Oyanagi - Lim Tuang Ooi - Lo Nyen Khing).
   - **Update the monitor CSV URL** from the dead prospect-database-7stakeholders.csv to prospects/prospect-database-250.csv.
   - Relabel the 159 remaining NOT FOUND cells as "CISO-equivalent approach required" where applicable, so 7/7 counts stop overstating outreach readiness.

## 6. Data-integrity alerts
1. **Canonical-URL drift (HIGH, NEW):** monitored file prospect-database-7stakeholders.csv is gone (404). Any pipeline pointed at it is silently reading a dead URL. This brief pivoted to prospects/prospect-database-250.csv.
2. **Headline-metric illusion:** enrichment rate jumped 81%->100% and cell-fill 52.6%->69.0% purely from deleting empty rows + shrinking the denominator. Absolute real contacts are flat (749). Do not report "enrichment complete" - the campaign added zero net-new contacts this cycle.
3. **SMBC duplicate (T1)** - inflates counts and creates conflicting contact records.
4. **Standing item resolved:** Bank Muamalat CISO (previously a misfiled CEO) corrected to empty in v5.15; now accurately 6/7.

# VoronDRQ Prospect Database Monitor — Intelligence Brief

**Generated:** 2026-08-03 04:00 +08 (MYT) | **Brief ID:** VDRQ-MON-20260803-0400
**Classification:** TLP:AMBER — Commercial Intelligence | **Source:** canonical prospects/prospect-database-7stakeholders.csv (local primary; mirror byte-identical md5 d100a3ff)
**Git:** HEAD = 8da345c (main; clean, in sync with origin). **3 NEW COMMITS since last brief** — merge bottleneck BROKEN.
**Previous run:** 2026-08-02 21:58 MYT (VDRQ-MON-20260802-2158) — approx 6h 1m ago.

---

## [!!!] HEADLINE — MERGE BOTTLENECK BROKEN: 3 NEW COMMITS LANDED ~2h AFTER LAST BRIEF; v6.0 MERGED DB (231 INST, 1446 NAMED, 89.4%, 203 FULL 7/7) + INTEGRITY GUARD + v5.88 COMPLETION PASS (0 PENDING). CANONICAL 7stakeholders CSV STILL FROZEN AT 156 — NEW BOTTLENECK = PROMOTE MERGED DATA INTO CANONICAL.

1. **The long-flagged merge — sole bottleneck for ~26 cycles / ~169h+ — has been EXECUTED.** Three commits landed in a ~1h37m burst beginning ~2h after the last brief was committed:
   - f36a8fe (Aug-03 00:00 MYT): **Merge v5.22-clean-names + v5.87-enriched -> v6.0-merged** — 231 institutions, 1,446 named cells (89.4% fill), 203 full 7/7. Integrity guard: **0 CRITICAL / 0 WARNING / 0 INFO** — zero data loss (+26 inst, +643 named cells, +136 full 7/7 vs v5.22).
   - 71f1634 (Aug-03 00:46 MYT): **voron-integrity-guard.py** added — prevents institution/cell data loss across DB versions; auto-remediates with --fix. v6.0 passes clean against v5.22.
   - 8da345c (Aug-03 01:37 MYT): **v5.88 — complete all 16 pending institutions (0 pending remaining)** — 112 pending cells resolved, 13 new named executives added, 74 researched "NOT FOUND" (annotated), 25 entity classifications. Coverage 866 named (57.5%), 0 pending, 77 full-7/7-named.
2. **BUT the canonical outreach CSV is STILL FROZEN.** prospects/prospect-database-7stakeholders.csv unchanged: 156 institutions, md5 d100a3ff, mtime Jul-26 20:09 MYT (~175h 51m idle, 27th static cycle for the canonical file). The merged v6.0/v5.88 data has **NOT been promoted** into the canonical CSV. The merge produced a *new* artifact (prospect-database-v6.0-merged.csv, repo root) but did not refresh the canonical file sales outreach reads from.
3. **NEW bottleneck = promote v6.0 (231 inst, 89.4%) / v5.88 (215 inst, 0 pending) into the canonical 7stakeholders CSV.** The merge unblocked the research pipeline; the canonical-refresh step is now the single remaining gate to unlock the next outreach wave.
4. **BIGGEST OUTREACH UNLOCK — all 30 Tier-1 Licensed Banks are now FULL 7/7 in the merged DB** (incl. CISO). Canonical still shows 28 T1 with **8 partials** (BNP 5/7, Citi 5/7, HSBC 5/7, Deutsche 3/7, SMBC 3/7, ICBC 2/7, JPM 1/7, Mizuho 1/7). In v6.0/v5.88 **all 8 are now complete**, plus **2 NEW T1 banks** (Bank of America Malaysia, Credit Suisse Malaysia) — both 7/7.
5. **+75 institutions** in v6.0 vs canonical 156: 49 restored from the pre-clean 205-row base (the rows removed in the Jul-23 "50 empty rows" cleaning, now enriched) + 26 genuinely new from v5.87 (5 Asset Management, 3 Development Finance, 1 new Insurer, cooperatives, MSBs, fintechs, payment processors).
6. **No new daily-enrichment run this cycle.** Last auto-run was Aug-02 06:18 UTC; next scheduled Aug-03 06:18 UTC (14:18 MYT). Verified-mailbox findings unchanged from prior brief (CIMB 3, AmBank 1, Bank Islam 1; DMARC non-compliant = HLB + RHB).
7. **Net for outreach = 0 new canonical contacts this cycle, BUT the working DB jumped from v5.68 -> v6.0 (231) / v5.88 (215, 0 pending).** The richest-ever contact pool now exists in the merged artifacts — pending canonical promotion.

---

## 1. Status snapshot — canonical CSV (re-parsed fresh; UNCHANGED this cycle)

| Metric | Value | Delta vs last brief |
|---|---|---|
| Institutions (rows) | 156 | 0 rows |
| Populated stakeholder cells (loose) | 772 / 1,092 (**70.7%**) — reproduced to the cell | 0 |
| >=1 populated cell | 156/156 = **100%** | 0 |
| Completely empty | 0 / 156 (0%) | 0 |
| Full 7/7 (loose) | 60 (38.5%) | 0 |
| Avg contacts / prospect | 4.95 | 0 |
| Tier split | T1=28 T2=53 T3=20 T4=30 T5=19 T6=6 | 0 |
| Segment split | Licensed Banks 28, Insurers 26, GLC-Linked 19, Investment Banks 15, E-Money 14, Takaful 12, Card Schemes 10, Development FIs 10, MSBs 10, Payment Operators 6, Fintech Sandbox 5, Fintech Registered 1 | 0 |
| Stripped Titles (metadata col K) | 22 / 156 (14.1%) | 0 |
| md5 / mtime | d100a3ff / Jul-26 20:09 MYT | unchanged |
| Canonical idle since content edit | ~175h 51m (27th static cycle) | +6h 2m |
| Git commits since last brief | **3** (HEAD 8015488->8da345c) | **+3 (NEW — first git activity in ~26 cycles)** |
| Git sync status | clean, in sync with origin/main (0 ahead/behind) | unchanged |
| Mirror CSV | byte-identical d100a3ff | unchanged |

---

## 2. Enrichment progress — canonical (UNCHANGED; re-confirmed)

**Role completion (high -> low):**

| Rank | Stakeholder role | Filled | Rate |
|---|---|---|---|
| 1 | Chief Financial Officer | 138 | **88.5%** |
| 2 | Chief Information Officer | 123 | 78.8% |
| 3 | Head of Compliance | 117 | 75.0% |
| 4 | Chief Risk Officer | 110 | 70.5% |
| 5 | Head of Governance Risk & Compliance | 104 | 66.7% |
| 6 | Head of Internal Audit | 101 | 64.7% |
| 7 | Chief Information Security Officer | 79 | **50.6%** — lowest role, binding constraint in canonical |

**Distribution (contacts/prospect):** 1/7=23, 2/7=3, 3/7=14, 4/7=11, 5/7=33, 6/7=12, 7/7=60 — identical to last brief.

---

## 3. NEW THIS CYCLE — the merge (v6.0) + completion (v5.88)

### 3a. v6.0 merged database (prospect-database-v6.0-merged.csv, 231 institutions)

| Metric | v5.22 (pre-merge) | v6.0 (merged) | Delta |
|---|---|---|---|
| Institutions | 205 | **231** | +26 |
| Named cells | 803 | **1,446** | +643 |
| Fill rate (named) | 56.0% | **89.4%** | +33.5% |
| Full 7/7 (named) | 67 | **203** | +136 |
| Pending cells | 632 | 171 | -461 |
| Integrity guard | — | **0 CRITICAL / 0 WARN / 0 INFO** | clean merge |

**v6.0 role completion (named):** CISO 204 (88.3%, gap 27) | GRC 206 | CFO 209 | CRO 206 | Compliance 208 | CIO 208 | IA 205 — all roles ~88-90% (vs canonical's CISO 50.6%). CISO is no longer the binding constraint in the merged DB.

**Tier split (v6.0):** T1=30, T2=54, T3=49, T4=35, T5=24, T6=15, + 24 singletons (T192-T215 = newly-categorised Asset Mgmt / Dev Finance / Cooperatives / Fintech / Payment Processors).

### 3b. v5.88 completion pass (prospect-database-enriched-v5.88.csv, 215 institutions)

- **0 pending remaining** — all 112 pending cells resolved (13 -> named executives; 74 -> researched "NOT FOUND" with annotations; 25 -> entity classifications).
- 13 new named executives: Affin Bank 4, Bank Rakyat 3, Generali/AXA Affin 2, Public Mutual 1, Jirnexu 2, FavePay 1.
- Coverage: 866 named (57.5% strict-named), 77 full-7/7-named; 1,505/1,505 cells non-empty (every cell now either named or researched-annotated).
- Note: v5.88 is a 215-institution base using strict "named" counting; unresolved cells are marked "NOT FOUND [annotation]" (researched, no public data — e.g. subsidiary with functions at group HQ) rather than left pending. This is a higher research-completeness state than v6.0's 112 pending.

### 3c. New institutions in v6.0 vs canonical 156 (+75 total)

- **+49 restored** from the pre-clean 205-row base (removed in Jul-23 "50 empty rows" cleaning, now enriched) — mostly E-Money, Fintech Sandbox, Cooperatives, MSBs.
- **+26 genuinely new** from v5.87 enrichment, incl.:
  - **Asset Management (5):** CIMB-Principal, Public Mutual, RHB AM, Hong Leong AM, Maybank AM
  - **Development Finance (3):** Credit Guarantee Corp, Malaysia Debt Ventures, Pengurusan Danaharta
  - **Licensed Banks (4):** Bank of America Malaysia (T1), Credit Suisse Malaysia (T1), Affin Bank, Kuwait Finance House
  - **Insurers (1):** AXA Affin General Insurance
  - **Investment Banks (2):** JF Apex Securities, TA Securities Holdings
  - **Fintech (5):** Curlec, FavePay, HelloGold, CompareHero, RinggitPlus
  - **Payment Processors (2):** Maybank QRPay, CIMB Clicks Pay
  - **Credit Cooperatives (3):** Bank Rakyat, Koperasi PDRM, MBSM
  - 21 state cooperatives (Koperasi Angkatan Tentera, Koperasi Johor, Koperasi Selangor, etc.)

---

## 4. Since last check (vs 2026-08-02 21:58 MYT, ~6h 1m ago)

- **Canonical CSV delta = 0 cells.** md5 d100a3ff -> d100a3ff; mtime still Jul-26 20:09 MYT. 27th static cycle for the canonical file.
- **Git delta = +3 commits (NEW — first activity in ~26 cycles).** HEAD 8015488 -> 8da345c; all pushed (0 ahead/behind origin). Repo clean.
- **Working-DB delta = MAJOR advancement.** v5.68 (Jul-29) -> v6.0 merged (231 inst, 1446 named, 89.4%) + v5.88 (215 inst, 0 pending). Merge report + integrity guard + completion pass all committed.
- **New institutions added (merged DB) = +75** (26 genuinely new + 49 restored). New stakeholder contacts populated = +643 named cells in v6.0 vs v5.22; +13 named execs in v5.88.
- **Enrichment-progress changes = the merge bottleneck is RESOLVED at working-DB level.** New bottleneck = canonical promotion.
- **Daily-enrichment delta = 0 new runs** (next = Aug-03 06:18 UTC).
- **Idle streak for canonical = ~175h 51m** (+6h 2m) — but the working DB is no longer idle.

---

## 5. Priority prospects — Tier 1 Licensed Banks

### Canonical (stale): 28 banks — 20 full 7/7, 8 partials
The 8 partials are unchanged in the canonical file: BNP Paribas 5/7, Citibank 5/7, HSBC 5/7, Deutsche 3/7, SMBC 3/7, ICBC 2/7, J.P. Morgan 1/7, Mizuho 1/7.

### Merged DB (v6.0/v5.88): 30 banks — ALL 30 FULL 7/7 (incl. CISO)
All 8 former partials are now complete. 2 NEW T1 banks added (Bank of America Malaysia, Credit Suisse Malaysia). Full outreach-ready T1 roster (all 7/7, CISO named):

| Tier-1 Licensed Bank (merged DB) | Status |
|---|---|
| Alliance Bank, Alliance Islamic, AmBank, AmBank Islamic, Bank Islam, Bank Muamalat, Bank of China (MY), CIMB Bank, CIMB Islamic, Hong Leong Bank, Hong Leong Islamic, Maybank, Maybank Islamic, OCBC, Public Bank, Public Islamic, RHB Bank, RHB Islamic, Standard Chartered, UOB | 7/7 (was already full in canonical) |
| **BNP Paribas, Citibank, HSBC, Deutsche Bank, ICBC, J.P. Morgan, Mizuho, SMBC** | **7/7 (NEW — was partial in canonical; now CISO + all roles named)** |
| **Bank of America Malaysia, Credit Suisse Malaysia** | **7/7 (NEW T1 banks — not in canonical)** |

Plus Affin Bank, Kuwait Finance House now present as Licensed Banks (7/7) in the merged DB.

**Highest-leverage outreach shift:** the 8 foreign-bank partials that were the top research targets are now outreach-ready in the merged DB. J.P. Morgan and Mizuho (1/7 in canonical) are now 7/7.

---

## 6. Actionable intelligence for sales outreach

**A. IMMEDIATE — source from the merged DB, not the stale canonical:**
- **The merged v6.0/v5.88 CSVs (repo root) are now the richest contact source** — 231 / 215 institutions, all 30 Tier-1 banks full 7/7. Until canonical is refreshed, **pull Tier-1 bank contacts from prospect-database-v6.0-merged.csv** rather than the canonical 7stakeholders file (which still shows 8 T1 partials).
- **30 Tier-1 banks are outreach-ready NOW** with full 7/7 including CISO. Prioritise the 8 newly-completed foreign banks (BNP, Citi, HSBC, Deutsche, ICBC, JPM, Mizuho, SMBC) + 2 new T1 (Bank of America, Credit Suisse) — these are net-new RMiT-relevant CISO conversations.
- Carry forward verified mailboxes from Aug-02 run: CIMB (grc/risk/compliance@cimb.com), AmBank (compliance@ambankgroup.com), Bank Islam (compliance@bankislam.com.my). Re-test before sending.

**B. UNBLOCK THE NEXT WAVE (single remaining gate):**
- **Promote v6.0 (231 inst, 89.4%) / v5.88 (215 inst, 0 pending) into the canonical prospect-database-7stakeholders.csv.** The merge is done; the canonical refresh is the last step. This unlocks +75 institutions and the 8 completed T1 partials for canonical-based outreach workflows.
- Reconcile the canonical cleaning: the 49 restored rows were removed Jul-23 as "empty" — confirm whether they should re-enter canonical now that they are enriched, or stay in a supplemental DB.

**C. RMiT compliance angle (carries forward, still live):**
- **Hong Leong Bank + RHB Bank are DMARC non-compliant** — both Tier-1, now full 7/7 in merged DB. Concrete RMiT email-authentication conversation starter.
- **Bank Islam DMARC partial** — Tier-1, full 7/7. Another warm lead angle.

**D. Targeted gap research (post-promotion, highest ROI):**
- **v6.0 CISO gap = 27** (down from canonical's 77) — the binding constraint is nearly closed in the merged DB. Final 27 CISO seats across the expanded 231 institutions.
- **3 institutions still 0/7 in v6.0** (Razer Pay, WeChat Pay Malaysia (Tencent), one AEON Bank Berhad duplicate 3/7) — data hygiene: duplicates/defunct to remove before promotion.
- **Lowest segments remain MSBs / Payment Operators / Fintech Registered** — only pursue if in-scope for RMiT campaign.

**E. Data hygiene (standing + NEW):** v6.0 contains duplicate/empty artifacts (Razer Pay 0/7, WeChat Pay Malaysia (Tencent) 0/7 vs WeChat Pay Malaysia Sdn Bhd 7/7, AEON Bank Berhad 3/7 vs AEON Bank (M) Berhad 7/7, KAF Digital Bank listed twice). De-duplicate before canonical promotion. New merged artifacts live in repo root (not operations/prospect-databases/) — relocate for consistency.

---

## 7. Verdict

**First real activity in ~26 cycles — the merge bottleneck is BROKEN.** Three commits landed in a ~1h37m burst ~2h after the last brief: a v6.0 merged database (231 institutions, 1,446 named cells, 89.4% fill, 203 full 7/7, integrity-guard clean), an integrity-guard tool, and a v5.88 completion pass (0 pending remaining, 13 new named execs). **The canonical prospect CSV remains frozen at 156 institutions / 70.7% / 60 full 7/7 / md5 d100a3ff (~175h 51m idle)** — the merged data has NOT been promoted into it. The single remaining bottleneck has shifted from "execute the merge" to **"promote v6.0/v5.88 into the canonical 7stakeholders CSV."** The biggest outreach unlock is that **all 30 Tier-1 Licensed Banks are now full 7/7 (incl. CISO)** in the merged DB — the 8 former partials plus 2 new T1 banks (Bank of America, Credit Suisse) are outreach-ready. **Action: pull Tier-1 contacts from the merged DB now; execute canonical promotion to unlock the +75-institution, 89.4%-fill next wave.**

*End of brief — VDRQ-MON-20260803-0400*

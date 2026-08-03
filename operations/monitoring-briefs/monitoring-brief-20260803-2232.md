# VoronDRQ Prospect-Database Monitoring Brief

- **Generated:** 2026-08-03 22:32 +08 (MYT)
- **Report Date:** 2026-08-03
- **Brief ID:** VDRQ-MON-20260803-2232
- **Repo HEAD:** aef5509 (clean working tree)
- **Prior brief:** VDRQ-MON-20260803-1210 (HEAD a42df7c, ~10h22m ago)
- **Source:** `prospects/prospect-database-7stakeholders.csv` (canonical, monitored) + `prospect-database-canonical.csv` (new consolidated, repo root)

---

## TL;DR — what changed this cycle

**Major development: the long-standing merge bottleneck has been *partially* broken.** Since the last brief, the v6.0-merged + v5.88 + v5.90 working databases were consolidated into a **NEW `prospect-database-canonical.csv` at the repo root — 231 institutions, 1,185 named contacts, 73.3% fill, 123 fully-mapped (7/7)** (commits `c73f8f4` + `9be4220` + `f50e8f43`, landed 14:26–16:18 MYT today).

**However, the monitored canonical path (`prospects/prospect-database-7stakeholders.csv`) is still frozen at 156 institutions / md5 `d100a3ff` — byte-identical to the remote GitHub raw (verified), mtime Jul-26 20:09 MYT, now ~194.4h (8.10 days) idle — its 29th static cycle.** The consolidation landed in a *new* file, not by overwriting the monitored 7stakeholders path. So anyone reading the canonical monitored path still sees the stale 156-row file. **The remaining bottleneck is now a 1-step path swap + dead-entity cleanup**, not a data-merge.

- **Canonical (monitored) delta = 0 cells.** md5 `d100a3ff` -> `d100a3ff`; remote match confirmed; idle ~194.4h (+10.4h vs prior brief).
- **Git delta = +4 prospect-track commits (NEW).** HEAD `a42df7c` -> `aef5509`. Daily-enrichment ran (commit `8b0d11f`, 14:26 MYT). Repo clean.
- **New institutions added to the consolidated file = +75** (156 -> 231); **0 dropped** from the old 156.
- **New T1 banks added = +5** (AEON Digital Bank 7/7, Affin Bank 7/7, Credit Suisse 7/7, Bank of America 1/7, Kuwait Finance House 5/7).
- **Enrichment progress (consolidated): CISO coverage jumped 50.6% -> 66.7%; overall fill 70.7% -> 73.3%; full 7/7 60 -> 123 (+63, +14.7pp).**

---

## 1. Canonical database size & composition (monitored path — UNCHANGED)

`prospects/prospect-database-7stakeholders.csv` — **156 institutions**, 7 stakeholder role columns (D–J) + Stripped Titles metadata (K). MD5 `d100a3ff`, matches remote raw GitHub exactly.

| Metric | Value |
|---|---|
| Total institutions | 156 |
| Total contacts populated | 772 / 1,092 slots (70.7%) |
| >=1 contact | 156 / 156 (100.0%) |
| Fully mapped (7/7) | 60 (38.5%) |
| Completely empty | 0 |

**Tier breakdown:** T1=28 - T2=53 - T3=20 - T4=30 - T5=19 - T6=6
**Segment breakdown (top):** Licensed Banks 28 - Insurers 26 - GLC-Linked 19 - E-Money 14 - Investment Banks 15 - Takaful 12 - MSBs 10 - Development FIs 10 - Card Schemes 10 - Payment Operators 6 - Fintech Sandbox 5 - Fintech Registered 1

**Per-role completion (ranked):**
| Rank | Role | Filled | % |
|---|---|---|---|
| 1 | Chief Financial Officer | 138/156 | 88.5% |
| 2 | Chief Information Officer | 123/156 | 78.8% |
| 3 | Head of Compliance | 117/156 | 75.0% |
| 4 | Chief Risk Officer | 110/156 | 70.5% |
| 5 | Head of Governance Risk & Compliance | 104/156 | 66.7% |
| 6 | Head of Internal Audit | 101/156 | 64.7% |
| 7 | Chief Information Security Officer | 79/156 | **50.6% (lowest)** |

CISO remains the RMiT-binding role and the single biggest enrichment gap in the monitored file.

---

## 2. NEW consolidated database (repo root — the real progress this cycle)

`prospect-database-canonical.csv` — MD5 `75036934`, mtime Aug-03 16:18 MYT (~6h14m old). **231 institutions, 1,185 contacts / 1,617 slots (73.3%), 123 full 7/7 (53.2%), 211/231 have >=1 (91.3%), 20 still empty.**

| Tier | Inst | >=1 contact | Full 7/7 | Fill rate |
|---|---|---|---|---|
| 1 | 33 | 32 (97%) | 24 (73%) | 199/231 = 86.1% |
| 2 | 57 | 57 (100%) | 42 (74%) | 361/399 = 90.5% |
| 3 | 60 | 53 (88%) | 14 (23%) | 248/420 = 59.0% |
| 4 | 37 | 33 (89%) | 23 (62%) | 186/259 = 71.8% |
| 5 | 24 | 19 (79%) | 13 (54%) | 111/168 = 66.1% |
| 6 | 20 | 17 (85%) | 7 (35%) | 80/140 = 57.1% |

**Per-role completion (consolidated):** CIO 184/231 (79.7%) - CRO 180/231 (77.9%) - CFO 177/231 (76.6%) - HoGRC 174/231 (75.3%) - HoC 163/231 (70.6%) - CISO 154/231 (66.7%) - **HoIA 153/231 (66.2%, now lowest)**.
-> CISO rose from 50.6% -> 66.7% (+75 more CISOs); HoIA is now the weakest role by coverage.

**Institution delta vs monitored 156-file:** +75 added, 0 dropped. All 156 monitored institutions are present in the consolidated file.

---

## 3. Changes since last check (VDRQ-MON-20260803-1210)

- **Canonical monitored file: NO change** (md5 d100a3ff, +10.4h idle -> ~194.4h, 29th static cycle). Remote GitHub still matches local byte-for-byte.
- **New commits (prospect track) since HEAD a42df7c:**
  - `8b0d11f` auto daily-enrichment 2026-08-03T06:26:48Z (14:26 MYT)
  - `c73f8f4` **consolidate: single canonical prospect database — 231 institutions** (new file `prospect-database-canonical.csv`)
  - `9be4220` **strip NOT-FOUND bracketed context from v5.90 + v6.0-merged — 931 phantom cells cleaned to empty, 0 named/entity data loss, 40–47% size reduction**
  - `f50e8f43` **repair 24 broken tier values + sort canonical by Tier -> Segment -> Institution**
  - (+`0d3e9f4`, `aef5509` = servicenow-watch, unrelated to prospects)
- **New institutions added = +75** in the consolidated file (none added to the monitored path).
- **New stakeholder contacts populated (consolidated vs monitored) = +413** (772 -> 1,185). Of these, **+75 CISOs** is the standout (the RMiT-binding role).
- **Net progress = +5pp overall fill (70.7%->73.3%), +63 institutions at full 7/7 (60->123), +75 institutions in scope (156->231).**

---

## 4. Priority prospects — Tier 1 Licensed Banks

### Monitored file (stale): 28 banks — 20 full 7/7, 8 partials (UNCHANGED)
The 8 partials remain unchanged: BNP Paribas 5/7, Citibank 5/7, HSBC 5/7, Deutsche 3/7, ICBC 2/7, J.P. Morgan 1/7, Mizuho 1/7, SMBC 3/7.

### Consolidated file (FRESH — source Tier-1 outreach from HERE): 33 banks — 24 full 7/7, 86.1% fill
| Status | Banks |
|---|---|
| **7/7 full (24)** | Alliance Bank, Alliance Islamic, AmBank, AmBank Islamic, Bank Islam, Bank Muamalat, Bank of China (MY), CIMB Bank, CIMB Islamic, Hong Leong Bank, Hong Leong Islamic, Maybank, Maybank Islamic, OCBC, Public Bank, Public Islamic, RHB Bank, RHB Islamic, Standard Chartered, UOB, **AEON Digital Bank (NEW)**, **Affin Bank (NEW)**, **Credit Suisse Malaysia (NEW)**, **SMBC (was 3/7)** |
| **Partial** | BNP Paribas 5/7 - Citibank 5/7 - KFH Malaysia 5/7 (NEW) - HSBC 6/7 (was 5/7) - Deutsche 3/7 - ICBC 2/7 - Mizuho 4/7 (was 1/7) - Bank of America 1/7 (NEW) |
| **Empty** | **J.P. Morgan Chase 0/7** (was 1/7 in monitored — NOT-FOUND strip removed a phantom row; treat as a data-hygiene regression to re-research) |

**NEW T1 banks to prioritize:** AEON Digital Bank (7/7, outreach-ready), Affin Bank (7/7, outreach-ready), Credit Suisse Malaysia (7/7, outreach-ready), Bank of America Malaysia (1/7 — needs research), KFH Malaysia (5/7 — note: prior brief flagged KFH exiting the Malaysian market by end-2026 -> deprioritize despite fills).

---

## 5. Enrichment quick-wins & gaps (consolidated file)

**20 institutions still 0/7 (empty) — research/de-dup targets:**
- **T1:** J.P. Morgan Chase Bank Malaysia Berhad *(re-research — was 1/7, phantom stripped)*
- **T3 MSBs (7):** 2C2P, Billplz, CurrencyFair, G2G Online, I.Destinasi (IDSB), Money Match, ToyyibPay
- **T4 E-Money (4):** Alipay+ Malaysia (Ant Group), Razer Pay (Razer Fintech), WeChat Pay Malaysia (Tencent), WeChat Pay Malaysia Sdn Bhd *(last 2 look like duplicates — consolidate)*
- **T5 GLC (5):** Agensi Jaminan Kredit Mikro (AKM), Cradle Fund, Iskandar Waterfront City, Penang SDC (PSDC), Sabah SFC (SSFC)
- **T6 (3):** Stripe Payments Malaysia, KDI Save, SeaBank Malaysia

**Data-hygiene flags for pre-promotion cleanup:** duplicate/near-duplicate pairs in the consolidated file — `WeChat Pay Malaysia Sdn Bhd` vs `WeChat Pay Malaysia (Tencent)`, `KAF Digital Bank` vs `KAF Digital Bank Berhad`, `AEON Bank (M) Berhad` vs `AEON Bank Berhad`. Resolve before the canonical-path swap.

**Monitored-file near-complete (6/7) — 1 contact away (12 prospects):** AIA Berhad (HoIA), ASNB (CISO), Bank Rakyat (HoIA), Berjaya Sompo (CIO), CIMB/Khazanah (CISO), GX Bank + GXBank (CISO — duplicate pair), Great Eastern General (CISO), Hong Leong IB / MIDF / Public IB (all CISO), Sarawak SFC (CISO). **CISO dominates the 1-away gaps** — a single targeted CISO research pass closes ~9 of these.

---

## 6. Actionable intelligence for sales outreach

**A. SOURCE FROM THE CONSOLIDATED FILE, NOT THE STALE MONITORED PATH (critical):**
- The monitored `prospects/prospect-database-7stakeholders.csv` (156 inst, 70.7%) is now superseded by `prospect-database-canonical.csv` (231 inst, 73.3%). **Pull all outreach contacts from the repo-root consolidated file** until the path swap completes.
- **33 Tier-1 Licensed Banks available (24 full 7/7).** Prioritize the 3 NEW fully-mapped T1 banks for net-new RMiT-relevant conversations: **AEON Digital Bank, Affin Bank, Credit Suisse Malaysia** (all 7/7 incl. CISO).
- The 8 foreign-bank partials (BNP, Citi, HSBC, Deutsche, ICBC, Mizuho, SMBC, JPM) improved in the consolidated file (SMBC->7/7, HSBC->6/7, Mizuho->4/7) — re-pull before contacting.

**B. UNBLOCK THE FINAL STEP — canonical-path swap (was the merge bottleneck, now a 1-step cleanup):**
- The merge *did* happen (into `prospect-database-canonical.csv`). What remains: (1) de-duplicate the ~3–4 duplicate/near-duplicate pairs (WeChat Pay, KAF Digital Bank, AEON Bank); (2) drop confirmed-dead/dormant entities (Danaharta wound-down, TA Securities inactive — flagged prior brief); (3) replace `prospects/prospect-database-7stakeholders.csv` with the cleaned consolidated file so monitored workflows see the 231-inst reality. This is now hours of work, not a multi-pass enrichment.

**C. DEPRIORITIZE / data-hygiene signals (carried + reinforced):**
- **KFH Malaysia (5/7 in consolidated) is exiting the Malaysian market by end-2026 -> deprioritize** despite the new fills.
- **J.P. Morgan Chase regressed 1/7 -> 0/7** in the consolidated file (NOT-FOUND strip removed a phantom cell). Re-research if JPM is in active outreach scope; otherwise deprioritize as a foreign bank with no public Malaysia leadership.
- **WeChat Pay Malaysia (Tencent) 0/7 vs WeChat Pay Malaysia Sdn Bhd 0/7** — duplicate; keep one, drop the other.

**D. Highest-ROI targeted research (post-cleanup):**
- **CISO is still the binding RMiT role and the biggest gap.** Consolidated CISO = 154/231 (66.7%); ~77 CISO seats still open. A dedicated CISO pass (LinkedIn + annual reports + Playwright for JS-rendered leadership pages) closes the most near-complete prospects.
- **HoIA is now the lowest-completed role in the consolidated file (66.2%)** — worth a pass if internal-audit contacts are in outreach scope.
- **Tier 3 (MSBs) is the weakest tier** — 59.0% fill, 23% full 7/7, 7 institutions at 0/7. If MSBs are in the RMiT addressable market, this tier needs the most work.

---

## 7. Verdict

**The merge bottleneck is broken — but only halfway.** Three new commits this cycle (`c73f8f4` consolidate -> `9be4220` strip 931 phantom cells -> `f50e8f43` repair 24 tiers + sort) produced a fresh `prospect-database-canonical.csv` at the repo root: **231 institutions (+75), 1,185 contacts (+413), 73.3% fill (+5pp), 123 full 7/7 (+63), CISO 50.6%->66.7%.** This is real, material progress — the largest single-cycle jump in the campaign's recent history. **But it landed in a new file, not at the monitored canonical path**, which remains frozen at 156 inst / md5 `d100a3ff` / ~194.4h idle (29th static cycle) and byte-identical to remote GitHub. The remaining bottleneck is now a **cleanup-and-path-swap** (de-duplicate ~4 pairs, drop dead entities, overwrite the 7stakeholders file) — no further enrichment passes are required to unlock the 231-inst dataset for canonical-based workflows. **Outreach action today: pull Tier-1 bank contacts from the repo-root consolidated file (33 banks, 24 full 7/7 incl. 3 new fully-mapped T1: AEON Digital Bank, Affin Bank, Credit Suisse); deprioritize KFH Malaysia (exiting market) and the JPM 0/7 regression; execute the path swap + dead-entity cleanup to close the gap between the consolidated file and the monitored canonical.**

*End of brief — VDRQ-MON-20260803-2232*

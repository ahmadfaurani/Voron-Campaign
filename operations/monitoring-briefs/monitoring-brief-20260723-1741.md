# VoronDRQ Prospect Database Monitor — Intelligence Brief
**Generated:** 2026-07-23 17:41 +08 (MYT) | **Brief ID:** VDRQ-MON-20260723-1741
**Classification:** TLP:AMBER | **Source:** canonical `prospects/prospect-database-7stakeholders.csv` (156 rows, cleaned 206->156 on 2026-07-23, commit d53cfed 12:18 MYT)
**Previous run:** 2026-07-23 05:27 MYT (VDRQ-MON-20260723-0527 — tracked `prospect-database-250.csv`, 155 rows, 749 real contacts)
**Source URL:** not re-fetched this run; local canonical used per task directive.

## [!] HEADLINE
1. **Canonical file switched** from `prospect-database-250.csv` (155 rows, tracked since 20 Jul) to the **cleaned `prospect-database-7stakeholders.csv`** (156 rows), committed 12:18 MYT today (d53cfed, "206->156 rows"). The 05:27 brief's source-URL-404 problem is resolved — the 7stakeholders file is restored as canonical.
2. **Cleanup executed:** 50 all-empty rows purged (206->156); all 158 "NOT FOUND [notes]" placeholders replaced with empty cells (verified: 0 NOT FOUND remain); honorific titles (Datuk, Dato', Datin, Dr, Encik, Puan...) stripped into a new metadata column K ("Stripped Titles").
3. **+19 real stakeholder contacts** since the 05:27 baseline (749->768 real contacts; 70.3% of 1,092 cells). Gains concentrated in Internal Audit (+7), Compliance (+6), GRC (+5), CIO (+1). **CISO unchanged at 76 — still the weakest role (48.7%).**
4. **2 new institutions added** — Mizuho Bank (Malaysia) [T1 Licensed Bank, 1/7] and Zurich Takaful Malaysia [T2 Takaful, 1/7, the 12th takaful]. SMBC duplicate row removed (dedup). Net 155->156 rows.
5. **100% institution-level enrichment** — all 156 prospects have >=1 named contact; 0 dead rows. **57 institutions now full 7/7 (+1: Malaysia International Islamic Bank IB reached 7/7).**

## 1. Composition (156 rows, 156 distinct)
**Tier:** T1=28 | T2=53 | T3=20 | T4=30 | T5=19 | T6=6
**Segment:** Licensed Banks 28 | Insurers 26 | GLC-Linked 19 | Investment Banks 15 | E-Money 14 | **Takaful 12 (+1)** | Development FIs 10 | Card Schemes 10 | MSBs 10 | Payment Operators 6 | Fintech Sandbox 5 | Fintech Registered 1
**Columns:** 11 = Tier, Segment, Institution_Name, 7 stakeholder roles (D-J), Stripped Titles (K, metadata only).

## 2. Enrichment progress
- **Real named contacts:** 768 / 1,092 cells = **70.3%** (was 749/1,085 = 69.0% on 250.csv)
- **Institutions with >=1 contact:** 156/156 = **100%** | Completely empty: **0**
- **Full 7/7:** 57 (36.5%) | Partial 1-6/7: 99 | Distribution: 1/7=24, 2/7=2, 3/7=14, 4/7=11, 5/7=33, 6/7=15, 7/7=57
- **Role completion (high->low):** CFO 137 (87.8%) | CIO 123 (78.8%) | Compliance 117 (75.0%) | CRO 110 (70.5%) | GRC 104 (66.7%) | Internal Audit 101 (64.7%) | **CISO 76 (48.7% — lowest)**

## 3. Since last check (vs 05:27 baseline on 250.csv)
**New institutions (+2):**
- Mizuho Bank (Malaysia) Berhad — T1 Licensed Banks, 1/7 (foreign bank, new)
- Zurich Takaful Malaysia Berhad — T2 Takaful, 1/7 (12th takaful)
**Removed:** SMBC duplicate row (dedup; SMBC retained as single 3/7 row)
**New contacts (+19 real; +20 raw cells, ~2 inflated by Setel dup):**
- Malaysia International Islamic Bank IB — +6 (CFO, CIO, CRO, Compliance, GRC, IA) -> now **7/7 FULL**
- Sumitomo Mitsui (SMBC) — +CRO, +IA -> 3/7
- Maybank Investment Bank — +Compliance, +IA -> 5/7
- Johor Corporation (JCorp) — +Compliance, +IA -> 5/7
- Permodalan Negeri Selangor (PNSB) — +CRO, +Compliance -> 5/7
- Setel (PETRONAS Dagangan) — +Compliance, +GRC -> 5/7  [dup row, see alert #1]
- Setel by PETRONAS Dagangan Berhad — +Compliance, +GRC -> 5/7  [dup row, same company]
- Permodalan BSN Berhad (PBSNB) — +GRC -> 4/7
- Wise (TransferWise) Malaysia — +GRC -> 4/7
**Cleanup:** 158 "NOT FOUND" placeholders -> empty; 50 all-empty rows purged (206->156); titles stripped to col K.

## 4. Tier-1 priority (28 Licensed Banks — 100% have >=1 contact)
**GREEN 7/7 launch-ready (17):** Alliance, Alliance Islamic, AmBank, AmBank Islamic, Bank Islam, Bank of China, CIMB, CIMB Islamic, Hong Leong, Hong Leong Islamic, Maybank, Maybank Islamic, OCBC, RHB, RHB Islamic, Standard Chartered, UOB
**6/7 (3):** Public Bank | Public Islamic | Bank Muamalat  (all CISO-only gap)
**5/7 (3):** BNP Paribas | Citibank | HSBC
**3/7 (2):** Deutsche Bank | SMBC
**1/7 (3):** ICBC | J.P. Morgan | **Mizuho (NEW)**
Every Tier-1 gap is **CISO-centric** — CISO is the universal missing role across all 11 sub-7/7 Tier-1 banks. The foreign-bank CISO wall persists (ICBC, JPM, Mizuho, Deutsche, SMBC, BNP, Citi, HSBC all missing CISO).

## 5. Data-integrity alerts
1. **Setel semantic duplicate** — "Setel (PETRONAS Dagangan)" + "Setel by PETRONAS Dagangan Berhad" are the same company on two rows (both T4 E-Money, both 5/7, both received identical +Compliance/+GRC enrichment). Merge/dedup -> inflates new-contact count by ~2.
2. **CISO is the bottleneck role** — 48.7% (76/156), lowest of all 7 roles; unchanged since last run. Drives every Tier-1 gap.
3. **Foreign-bank CISO wall** — 8 of 11 sub-7/7 Tier-1 banks are foreign; all missing CISO. Fallback: approach Group CIO/CTO/CDTO as CISO-equivalent entry.
4. **Mizuho added at 1/7** — new Tier-1 bank with only 1 contact; immediate research target.
5. **File provenance** — canonical switched 250.csv -> 7stakeholders.csv mid-day (12:18 MYT). Auto-enrichment run 9a7eb47 at 14:19 MYT. Verify the cron source-URL now points to 7stakeholders.csv (05:27 brief flagged it as 404).

## 6. Actionable intelligence (sales outreach)
1. **Begin Tier-1 outreach NOW** — 17/28 Licensed Banks are full 7/7 and launch-ready. Top targets: **CIMB, Maybank** (full rosters, domestic champions); **Bank Muamalat** (6/7, CISO-only gap — near-ready).
2. **Near-ready (6/7, CISO-only):** Public Bank, Public Islamic, Bank Muamalat — fast-track once CISO confirmed; usable today via CRO/Head-of-Compliance as entry.
3. **CISO research sprint** — priority fill for 11 sub-7/7 Tier-1 banks; CISO is the single blocker for all. Foreign banks: use Group CIO/CTO/CDTO as CISO-equivalent.
4. **Repair queue:** (a) dedup Setel rows; (b) confirm cron URL = 7stakeholders.csv; (c) continue CISO fill (weakest role, +0 this cycle); (d) reconcile Mizuho roster (1/7).
5. **Enrichment momentum:** +19 real contacts this cycle (~12h). Internal Audit (+7) and Compliance (+6) moved most. CISO (+0) is the long-pole — needs a dedicated CISO-research pass to lift the 48.7% floor.

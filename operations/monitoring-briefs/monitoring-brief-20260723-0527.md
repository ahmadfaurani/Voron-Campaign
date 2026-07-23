# VoronDRQ Prospect Database Monitor — Intelligence Brief
**Generated:** 2026-07-23 05:27 +08 (MYT) | **Brief ID:** VDRQ-MON-20260723-0527
**Classification:** TLP:AMBER | **Source:** canonical `prospects/prospect-database-250.csv` (MD5 9ed07755707797a8897d6e5beca963da)
**Previous run:** 2026-07-22 11:14 MYT (VDRQ-MON-20260722-1114 — tracked v5.22 research file, 205 inst)
**Source URL:** task URL prospect-database-7stakeholders.csv = HTTP 404 (6th consecutive run) — canonical file RENAMED to prospect-database-250.csv.

## [!] HEADLINE
1. Source-URL 404 solved by rename: canonical deployment DB is now prospect-database-250.csv. Previous 5 runs tracked a 205-row research file instead. This run reports on the actual deployment file.
2. Canonical DB STREAMLINED 205 -> 155 institutions (commit 1d81ad6, 2026-07-20 16:22 MYT). All 45 empty/unlisted institutions (incl. 21 Cooperatives) PURGED. 100% of remaining institutions have >=1 named contact (0 dead prospects). Frozen ~61h.
3. Deployment file is 1 enrichment cycle BEHIND research file: v5.22 fills (Boost Bank CISO Shankar Krishnan, Soft Space CFO Rick Leong, 2026-07-21) NOT merged into deployment file. Verified: Boost Bank CISO still = NOT FOUND.
4. Zero new data since last check. No enrichment commit since v5.22 (~45h ago); only auto git-sync.

## 1. Composition (155 rows, 154 distinct — SMBC dup)
Tier: T1=28 T2=52 T3=20 T4=30 T5=19 T6=6
Segments: Licensed Banks 28, Insurers 26, GLC-Linked 19, Investment Banks 15, E-Money 14, Takaful 11, Dev FIs 10, Card Schemes 10, MSBs 10, Payment Ops 6, Fintech Sandbox 5, Fintech Registered 1. Cooperatives=0 (purged).

## 2. Enrichment (STRICT = real named contacts)
- Named cells: 749 / 1085 = 69.0% | Nominal (incl NOT FOUND): 908 = 83.7%
- Institutions w/ >=1 contact: 155/155 = 100% | Empty 0/7: 0
- Full 7/7 true: 56 (36.1%) | Nominal 7/7: 110 (71.0%)
- Role (high->low): CFO 137 (88.4%) > CIO 122 (78.7%) > Compliance 111 (71.6%) > CRO 110 (71.0%) > GRC 99 (63.9%) > IA 94 (60.6%) > CISO 76 (49.0% lowest)
- 159 NOT-FOUND audit-note cells remain (inflate nominal, NOT people)

## 3. Since last check
New institutions 0 | New contacts 0 | Corrections 0. Deployment file frozen since 2026-07-20 16:22 MYT. Pipeline stall ~45h.

## 4. Tier-1 priority (28 Licensed Banks)
[GREEN 7/7] 17: Alliance, Alliance Islamic, AmBank, AmBank Islamic, Bank Islam, Bank of China, CIMB, CIMB Islamic, Hong Leong, Hong Leong Islamic, Maybank, Maybank Islamic, OCBC, RHB, RHB Islamic, StanChart, UOB
[AMBER 5-6/7] 6: Public Bank 6/7, Public Islamic 6/7, Bank Muamalat 6/7 (all CISO), BNP 5/7, Citi 5/7, HSBC 5/7
[RED 1-3/7] 5: Deutsche 3/7, ICBC 3/7, SMBC 3/7, JPM 1/7, SMBC(dup) 1/7
Every T1 gap is CISO-centric. Foreign-bank CISO wall persists.

## 5. Data-integrity alerts
1. Source-URL 404 (6th run, resolved by rename) — fix cron URL to prospect-database-250.csv
2. Deployment/research divergence — merge v5.22 fills to deployment file
3. Duplicate SMBC Malaysia row x2 — dedup
4. 159 NOT-FOUND notes inflate nominal 7/7 to 110 vs true 56
5. Enrichment stall ~45h — health-check cron

## 6. Actionable intelligence
1. Deployment file 100% actionable — begin T1 outreach NOW. 17/28 T1 banks launch-ready.
2. Merge 2 missing v5.22 fills (Boost Bank CISO, Soft Space CFO) before outreach.
3. Foreign-bank CISO fallback: use Group CIO/CTO/CDTO as CISO-equivalent entry.
4. Repair queue: dedup SMBC, fix cron URL, merge v5.22, exclude NOT-FOUND from ready counts.
5. Top launch targets: CIMB, Maybank (full 7/7); Bank Muamalat (6/7, CISO-only gap).

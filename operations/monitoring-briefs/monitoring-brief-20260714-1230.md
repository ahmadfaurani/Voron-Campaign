# VoronDRQ Prospect Monitor — Intelligence Brief
**Run:** 2026-07-15 08:30 MYT (cron) · **Commit:** 1210a52 · **DB:** prospect-database-enriched-v3.6.csv
**Classification:** TLP:AMBER · **Status:** 🟢 CHANGE DETECTED (2 new commits since 07:10)

## Source note
Task URL `prospects/prospect-database-7stakeholders.csv` -> 404 (repo restructured to root).
Canonical enriched DB = `prospect-database-enriched-v3.6.csv` (HEAD=origin/main, in sync).

## Database size & composition
- **205 institutions** (unchanged — no new institutions added)
- Tiers: T1=29 · T2=53 · T3=49 · T4=35 · T5=24 · T6=15
- Top segments: Licensed Banks 29 · Insurers 26 · GLC-Linked 24 · Cooperatives 21 · E-Money 19

## Enrichment progress (v3.2 -> v3.6)
| Metric | Prev (07:10) | Now (12:30) | Delta |
|---|---|---|---|
| Prospects w/ >=1 contact | 83 | 92 | +9 |
| Enrichment rate | 40.5% | 44.9% | +4.4 pp |
| Contact cells filled | 345 / 1435 | 429 / 1435 | +84 net (+87 adds, -3 QA) |
| Cell fill rate | 24.0% | 29.9% | +5.9 pp |
| Fully enriched (7/7, all tiers) | 6 | 25 | +19 |
| Fully enriched (7/7, Tier 1) | 6 | 13 | +7 |
| Institutions touched this cycle | - | 55 | - |

## Stakeholder role completion (highest -> lowest)
| Role | Filled | % |
|---|---|---|
| Chief Financial Officer | 80 | 39.0% |
| Head of Compliance | 70 | 34.1% |
| Chief Risk Officer | 67 | 32.7% |
| Chief Information Officer | 66 | 32.2% |
| Head of GRC | 62 | 30.2% |
| Head of Internal Audit | 51 | 24.9% |
| Chief Information Security Officer | 33 | 16.1% (bottleneck) |

## New additions since last check
Commits: ad289ff (v3.5, 08:14Z - QBE Insurance 3/7 + Manulife CISO QA fix), 1210a52 (v3.6, 12:10Z - +31 roles across 9 fintech/payment institutions).
9 newly-populated institutions (was 0/7):
- TNG Digital (Touch'n Go eWallet) x3 entity rows -> 5/7 (CFO, CIO, CRO, Compliance, GRC - combined-role exec)
- Boost Bank Berhad -> 4/7 (CFO, CIO, Compliance, CRO)
- Ryt Bank (YTL Digital) x2 rows -> 4/7 (CFO, CRO, Compliance, CIO)
- PayNet Malaysia -> 2/7 (CFO, CIO)
- iPay88 x2 rows -> 1/7 (CISO)
+19 institutions reached complete 7/7 coverage (incl. Affin IB, Alliance Bank, Alliance IB, Alliance Islamic, AmBank, AmBank Islamic, AmInvestment Bank, BIMB IB, CIMB IB, Etiqa x3, GX Bank x2, Maybank, Maybank Islamic, OCBC, RHB IB).

## Priority prospects - Tier 1 banks NOW ready for outreach
7 Tier-1 banks just completed 7/7 (newly actionable for full multi-stakeholder outreach):
Alliance Bank · Alliance Islamic · AmBank · AmBank Islamic · Maybank · Maybank Islamic · OCBC Bank
(joining Bank Islam, CIMB Bank, CIMB Islamic, RHB Bank, RHB Islamic, Bank Muamalat = 13 T1 banks fully mapped)

Near-complete T1 (gap-fill to unlock): Bank of China, Hong Leong Bank, Hong Leong Islamic, Public Bank, Public Islamic, Std Chartered, UOB (all 6/7 - missing CISO) · HSBC (5/7).
T1 still empty (foreign, no public MY data): Credit Suisse · Mizuho · Sumitomo Mitsui BC.

## Recommended next actions
1. Launch outreach to the 7 newly-complete T1 banks (full C-suite mapped, multi-threaded engagement now possible).
2. CISO gap-fill sprint for 8 T1 banks at 5-6/7 (single-role blocking full coverage).
3. Takaful + Development FI enrichment via LinkedIn/annual reports (still thin).
4. E-money operators (ShopeePay, GrabPay, BigPay, Razer Pay, Setel, WeChat Pay) remain at 0/7.

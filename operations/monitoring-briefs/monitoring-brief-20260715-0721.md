# VoronDRQ Prospect Monitor — Brief 2026-07-15 07:21 UTC

Source: prospect-database-enriched-v3.9.csv (commit 3fea274, "Enrichment v3.9: Standard Chartered CISO, Great Eastern CEO, Tokio Marine CEO+CFO, Zurich Takaful CEO, Sun Life CEO")
Prev basis: v3.8 (commit 8bd5f8b, brief 2026-07-15 01:19 UTC)
URL note: Task URL prospects/prospect-database-7stakeholders.csv still 404 (repo restructured; root-level seed is un-enriched 205-row template). Canonical enriched DB = prospects/prospect-database-enriched-v3.9.csv, fetched from raw GitHub.

## 1. Database size and composition
- Total prospects: 205 (UNCHANGED — no new institutions). Raw CSV shows 206 rows but row #181 is a CSV-corruption ghost (empty name, Tier="CEO) [Official: sunlifemalaysia.com]") from an unescaped quote in the Sun Life row. Real institutions = 205.
- Tiers: T1=29  T2=53  T3=49  T4=35  T5=24  T6=15
- Segments: Licensed Banks 29 · Insurers 26 · GLC-Linked 24 · Cooperatives 21 · E-Money 19 · MSBs 17 · Investment Banks 15 · Fintech Sandbox 13 · Takaful 12 · Development FIs 11 · Card Schemes 10 · Payment Operators 6 · Fintech Registered 2

## 2. Enrichment progress (v3.8 to v3.9)
| Metric | v3.8 | v3.9 | Delta |
|---|---|---|---|
| Prospects with >=1 contact | 98 | 99 | +1 |
| Completely empty | 107 | 106 | -1 |
| Enrichment rate | 47.8% | 48.3% | +0.5 pp |
| Populated contact cells | 449 | 456 | +7 |
| Cell fill rate (of 1435) | 31.3% | 31.8% | +0.5 pp |
| Fully enriched (7/7) | 27 | 30 | +3 |
| T1 with >=1 contact | 29 | 29 | 0 |
| T1 fully enriched (7/7) | 15 | 16 | +1 |

## 3. Stakeholder role completion (highest to lowest)
1. CFO 84/205 (41.0%) — strongest, unchanged
2. Head of Compliance 70/205 (34.1%) — unchanged
3. CRO 68/205 (33.2%) — unchanged
4. CIO 68/205 (33.2%) — unchanged
5. Head of GRC 67/205 (32.7%) — was 66 (+1, but the +1 is a Zurich Life corruption fragment, not a real contact)
6. Head of Internal Audit 52/205 (25.4%) — unchanged
7. CISO 47/205 nominal (22.9%) — was 41 (+6) — weakest nominally, BUT 18 of 47 cells are CEO/Chairman/President misfiles -> TRUE CISO coverage = 29/205 (14.1%)

## 4. New additions since last check (commit 3fea274, 6 institutions, +7 nominal cells)
- **Standard Chartered Bank Malaysia Berhad — T1 — 6/7 -> 7/7** (+CISO Sivanathan Subramaniam). LEGITIMATE CISO. NOW FULLY ENRICHED and OUTREACH-READY.
- Great Eastern General Insurance (Malaysia) Berhad — T3 — 6/7 -> 7/7 (+CEO Jeremy Yeap Cheng Sun, misfiled in CISO column). Nominal full; CISO not real.
- Great Eastern Life Assurance (Malaysia) Berhad — T3 — 6/7 -> 7/7 (+CEO Dato Koh Yaw Hui, misfiled in CISO column). Nominal full; CISO not real.
- Tokio Marine Life Insurance Malaysia Bhd — T3 — 1/7 -> 2/7 (+CEO Kang Yu Fen, misfiled in CISO column).
- Zurich Life Insurance Malaysia Berhad — T3 — 1/7 -> 3/7 (CISO cell: CEO Florence Chang->Pauline Teoh; +GRC and +CFO cells are CSV-corruption fragments, NOT real contacts).
- Zurich Takaful Malaysia Berhad — T3 — 0/7 -> 1/7 (+CEO Nur Fatihah Mustafa, misfiled in CISO column). NEWLY POPULATED.
- Sun Life Malaysia Assurance Berhad — T3 — net 0 (CISO cell +CEO Ho Teck Seng misfiled; CFO cell removed — same CEO relocated). Row has CSV quoting corruption.

## 5. Data-quality regressions in v3.9 (action required)
1. CSV quoting corruption — Sun Life row: unescaped double-quote splits the row into a phantom 206th row (empty name, garbage Tier). Real count stays 205. Needs quote-escaping fix.
2. Column bleed — Zurich Life row: a misquoted multi-line cell spilled fragments into the GRC and CFO columns. 2 garbage cells counted as contacts. Needs repair.
3. CEO misfiled as CISO (5 new this round): Great Eastern General, Great Eastern Life, Tokio Marine, Zurich Takaful, Sun Life all had CEO names written into the CISO column. Not real CISOs — relabel/relocate.
4. Systemic CISO-column pollution (pre-existing): 18 of 47 nominal CISO cells hold CEO/Chairman/President data (incl. ASNB, CIMB-Khazanah, GX Bank, Tabung Haji, Manulife x2, Mizuho, Prudential, SMBC, Bank Muamalat). True CISO = 29 (14.1%), not 22.9%. Any "CISO-complete" claim from the raw column is unreliable.
5. Credit Suisse (Malaysia): CISO cell still holds a merger-status note (acquired by UBS) — not a contact. Reclassify/route to UBS Malaysia.

## 6. Tier 1 outreach status (29 banks) — REAL coverage basis
- 29/29 have >=1 nominal contact; 16 fully enriched (7/7 nominal); 0 truly empty.
- Newly fully enriched: **Standard Chartered** (real CISO added). 16 full = Alliance Bank, Alliance Islamic, AmBank, AmBank Islamic, Bank Islam, Bank Muamalat, CIMB Bank, CIMB Islamic, Hong Leong Bank, Hong Leong Islamic, Maybank, Maybank Islamic, OCBC, RHB Bank, RHB Islamic, **Standard Chartered (NEW)**.
- Real CISO present in 17 of 29 T1 banks (3 T1 CISO cells are CEO-misfiles).
- 6/7 partial — single-role lift to 7/7:
  - Missing only CISO (3): Public Bank, Public Islamic Bank, UOB Malaysia -> highest-ROI gap-fill
  - Missing only CIO (1): Bank of China (Malaysia)
- 5/7: HSBC (missing CISO + Internal Audit) — closest large T1 to full
- 3/7: Citibank, SMBC (data-quality caveats)
- 2/7: ICBC
- 1/7: BNP Paribas, Credit Suisse (status note), Deutsche Bank, J.P. Morgan, Mizuho (CEO misfiled)

## 7. Priority next actions (sales outreach prioritization)
1. GREEN-LIGHT outreach: Standard Chartered Malaysia — now fully enriched with real CISO (Sivanathan Subramaniam). Highest-priority newly-ready T1 account.
2. CISO gap-fill (highest ROI, 3 T1 banks at 6/7): Public Bank, Public Islamic, UOB Malaysia — one real CISO each lifts them to true 7/7. Prioritize CISO sourcing for these.
3. Bank of China: only missing CIO — single-role lift to 7/7.
4. HSBC: push 5/7 -> 7/7 (add real CISO + Head of Internal Audit).
5. Repair v3.9 data quality before relying on CISO metrics: fix Sun Life and Zurich Life CSV corruption (phantom row + column-bleed); relabel 5 CEO-misfiles out of CISO column; reclassify Credit Suisse (UBS acquisition).
6. Deep-enrich thin T1 foreign banks: Citibank (3/7), SMBC (3/7), ICBC (2/7), and the 1/7 cluster (BNP Paribas, Deutsche Bank, J.P. Morgan, Mizuho) — large gaps for outreach readiness.
7. CISO remains the true weakest role (14.1% real) — continue targeted CISO sourcing across all tiers; do not trust nominal CISO column without verifying the cell is an actual CISO.

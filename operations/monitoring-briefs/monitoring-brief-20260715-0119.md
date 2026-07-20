# VoronDRQ Prospect Monitor - Brief 2026-07-15 01:19 UTC

Source: prospect-database-enriched-v3.8.csv (commit 8bd5f8b, 2026-07-14 20:18 UTC)
Prev basis: v3.7 (commit bf8ecd9, brief 2026-07-14 19:14)
URL note: prospects/prospect-database-7stakeholders.csv still 404 - repo restructured to root; root-level seed is un-enriched (205 prospects, all-empty stakeholder cells). Canonical enriched DB tracked in local workspace git. Remote root seed fetched OK (21159 bytes, 205 rows).

## Database composition
- Total prospects: 205 (unchanged - no new institutions added)
- Tiers: T1=29 T2=53 T3=49 T4=35 T5=24 T6=15
- Segments: Licensed Banks 29, Insurers 26, GLC-Linked 24, Cooperatives 21, E-Money 19, MSBs 17, Investment Banks 15, Fintech Sandbox 13, Takaful 12, Development FIs 11, Card Schemes 10, Payment Operators 6, Fintech Registered 2

## Enrichment progress (v3.7 to v3.8)
- Prospects with at least 1 contact: 96 to 98 (+2) | Empty: 109 to 107 (-2)
- Enrichment rate: 46.8% to 47.8% (+1.0 pp)
- Contact cells: 444 to 449 (+5) | Cell fill rate: 30.9% to 31.3% (+0.4 pp)
- Fully enriched (7/7): 25 to 27 (+2)
- T1 with contacts: 27 to 29 (+2) | T1 fully enriched: 13 to 15 (+2)
- T1 empty: 2 to 0 (nominal)

## Stakeholder role completion (highest to lowest)
1. CFO 84/205 (41.0%) - strongest, unchanged
2. Head of Compliance 70/205 (34.1%) - unchanged
3. CRO 68/205 (33.2%) - unchanged
4. CIO 68/205 (33.2%) - unchanged
5. Head of GRC 66/205 (32.2%) - was 65 (+1)
6. Head of Internal Audit 52/205 (25.4%) - unchanged
7. CISO 41/205 (20.0%) - was 37 (+4) - weakest but biggest mover this round

## New additions since last check (5 institutions, +5 cells, all Tier 1)
- Hong Leong Bank Berhad - T1 - 6/7 to 7/7 (+CISO: Dr. Simon Hoh) - NOW FULLY ENRICHED
- Hong Leong Islamic Bank Berhad - T1 - 6/7 to 7/7 (+CISO: Dr. Simon Hoh, group-level) - NOW FULLY ENRICHED
- Credit Suisse (Malaysia) Berhad - T1 - 0/7 to 1/7 (cell = entity-status note: acquired by UBS, NOT a real person) - DATA QUALITY FLAG
- Mizuho Bank (Malaysia) Berhad - T1 - 0/7 to 1/7 (cell = CEO Daisuke Ihara, misfiled in CISO column) - DATA QUALITY FLAG
- Citibank Berhad - T1 - 2/7 to 3/7 (+GRC cell = CEO Vikram Singh, misfiled role)
- Also: HSBC GRC cell value updated (Brian McGuire title/sources refined) - count unchanged at 5/7

## Data quality flags (action required)
- Credit Suisse: CISO cell holds merger-status text, no contact person. Entity acquired by UBS. Recommend reclassify or route to UBS Malaysia; do NOT count as contacted for outreach.
- Mizuho: CEO name placed in CISO column (role misfiled). Real contact = Daisuke Ihara (CEO).
- Citibank: CEO name placed in GRC column (role misfiled). Real contacts = CEO Vikram Singh + CFO + CIO.
- SMBC Malaysia: 3 cells (CISO/GRC/CFO) appear to be fragments of one CEO record (Atsuhide Shiojiri) - parsing artifact, effectively 1 real contact at 3/7 nominal.
- HSBC: Brian McGuire holds 3 roles (CRO + Compliance + GRC) - dedup note, 1 person across 3 cells.

## Tier 1 outreach status (29 banks)
- 29/29 have at least 1 contact (nominal 100% coverage) - was 27/29
- 15 fully enriched (7/7) - was 13
- 14 partial, 0 empty (nominal)
- Fully enriched (15): Alliance Bank, Alliance Islamic, AmBank, AmBank Islamic, Bank Islam, CIMB Bank, CIMB Islamic, Hong Leong Bank (NEW), Hong Leong Islamic (NEW), Maybank, Maybank Islamic, OCBC, RHB Bank, RHB Islamic, Bank Muamalat
- 6/7 partial (5 banks): Bank of China (missing CIO), Public Bank (missing CISO), Public Islamic (missing CISO), Standard Chartered (missing CISO), UOB (missing CISO)
- 5/7: HSBC (missing CISO + Internal Audit)
- 3/7: Citibank, SMBC (data-quality caveats)
- 2/7: ICBC
- 1/7: BNP Paribas, Credit Suisse (status note), Deutsche Bank, J.P. Morgan, Mizuho (CEO)

## Priority next actions
1. CISO gap-fill for 4 T1 banks at 6/7 missing only CISO: Public Bank, Public Islamic, Standard Chartered, UOB - single-role lift to 7/7 (highest ROI, 4 banks)
2. Bank of China: only missing CIO - single-role lift to 7/7
3. Credit Suisse: resolve entity status (acquired by UBS) - reclassify or route outreach to UBS Malaysia
4. Fix misfiled CEO roles: Mizuho (CEO in CISO col), Citibank (CEO in GRC col), SMBC (CEO fragmented) - relabel and continue role-filling
5. HSBC: push 5/7 to 7/7 (add CISO + Internal Audit)
6. Citibank (3/7) and ICBC (2/7) - large T1 gaps, prioritize deeper enrichment
7. CISO remains weakest role overall (20.0%) - continue targeted CISO sourcing across all tiers

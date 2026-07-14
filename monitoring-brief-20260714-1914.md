# VoronDRQ Prospect Monitor — Brief 2026-07-14 19:14

Source: prospect-database-enriched-v3.7.csv (commit bf8ecd9 "v3.7: +11 stakeholder roles across 5 institutions")
Task URL note: prospects/prospect-database-7stakeholders.csv returns 404 — repo restructured to root; root-level seed is un-enriched. Canonical DB tracked in local workspace git.

## Database composition
- Total prospects: 205 (unchanged — no new institutions)
- Tiers: T1=29 T2=53 T3=49 T4=35 T5=24 T6=15
- Top segments: Licensed Banks 29, Insurers 26, GLC-Linked 24, Cooperatives 21, E-Money 19, MSBs 17, Investment Banks 15, Fintech Sandbox 13, Takaful 12, Development FIs 11, Card Schemes 10, Payment Operators 6, Fintech Registered 2

## Enrichment progress (v3.6 12:30 -> v3.7 16:14)
- Prospects with >=1 contact: 92 -> 96 (+4) | Empty: 113 -> 109
- Enrichment rate: 44.9% -> 46.8% (+1.9 pp)
- Contact cells: 429 -> 444 (+15) | Cell fill rate: 29.9% -> 30.9% (+1.0 pp)
- Fully enriched (7/7): 25 (unchanged) | T1 fully enriched: 13 (unchanged)
- T1 with contacts: 26 -> 27 (+1)

## Stakeholder role completion (highest -> lowest)
1. CFO 84/205 (41.0%) - strongest
2. Head of Compliance 70/205 (34.1%)
3. CRO 68/205 (33.2%)
4. CIO 68/205 (33.2%)
5. Head of GRC 65/205 (31.7%)
6. Head of Internal Audit 52/205 (25.4%)
7. CISO 37/205 (18.0%) - weakest, persistent gap

## New additions since last check (6 institutions, +15 cells)
- SMBC Malaysia - T1 - 0/7 -> 3/7 (was a flagged empty T1 target)
- PUNB - T3 DevFI - 0/7 -> 5/7
- Manulife Insurance - T2 - 2/7 -> 4/7
- MSIG Insurance - T2 - 1/7 -> 3/7
- Manulife Takaful - T2 - 0/7 -> 2/7
- Zurich Life Insurance - T2 - 0/7 -> 1/7

## Tier 1 outreach status (29 banks)
- 27/29 have contacts, 13 fully enriched, 14 partial, 2 empty
- Empty T1 (priority): Credit Suisse (Malaysia), Mizuho Bank (Malaysia)
- 6 T1 banks at 6/7 ALL missing only CISO: Bank of China, Hong Leong Bank, Hong Leong Islamic, Public Bank, Public Islamic, Standard Chartered, UOB
- HSBC Malaysia 5/7 (missing CISO + Internal Audit) - closest non-full to completion

## Priority next actions
1. CISO gap-fill for the 6 T1 banks at 6/7 - single-role lift to 7/7 (highest ROI)
2. Crack the 2 remaining empty T1 foreign banks: Credit Suisse, Mizuho
3. HSBC Malaysia -> push 5/7 to 7/7
4. Citibank (2/7) and ICBC (2/7) - large T1 gaps
5. T2 insurer continuation: Manulife Takaful, Zurich Life, MSIG

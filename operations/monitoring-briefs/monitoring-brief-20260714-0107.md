# VoronDRQ Prospect DB — Monitoring Brief
**Run:** 2026-07-15 08:30 MYT · **Source:** prospect-database-enriched-v3.2.csv · **Commit:** 318ae7b (v3.2)

## Database size & composition
- **Total prospects:** 205 (unchanged since last check — no new institutions)
- **By Tier:** T1=29 · T2=53 · T3=49 · T4=35 · T5=24 · T6=15
- **By Segment:** Licensed Banks 29 · Insurers 26 · GLC-Linked 24 · Cooperatives 21 · E-Money 19 · MSBs 17 · Investment Banks 15 · Takaful 12 · Fintech Sandbox 13 · Development FIs 11 · Card Schemes 10 · Payment Operators 6 · Fintech Registered 2

## Enrichment progress (current)
| Metric | Now | vs last check (v2.9) | Delta |
|---|---|---|---|
| Prospects w/ >=1 contact | 83 | 80 | **+3** |
| Enrichment rate | 40.5% | 39.0% | **+1.5pp** |
| Contact cells filled | 345 / 1435 | 322 | **+23** |
| Role fill rate | 24.0% | 22.4% | **+1.6pp** |
| Fully enriched (7/7) | 6 | 6 | — |

## Stakeholder role completion (highest to lowest)
| Role | Filled | Completion | Delta vs last |
|---|---|---|---|
| Chief Financial Officer | 74 | 36.1% | +1 |
| Head of Compliance | 58 | 28.3% | **+7** |
| Chief Information Officer | 58 | 28.3% | +6 |
| Chief Risk Officer | 57 | 27.8% | +4 |
| Head of Internal Audit | 46 | 22.4% | +5 |
| Chief Information Security Officer | 28 | 13.7% | — |
| Head of Governance Risk & Compliance | 24 | 11.7% | — |

**Insight:** Head of Compliance saw the largest absolute jump (+7) this cycle — the easiest role to source publicly (regulatory disclosures, LinkedIn). CISO and Head of GRC remain the two hardest-to-fill roles (flat at 13.7% / 11.7%) and are the bottleneck to pushing more institutions to 7/7.

## New additions since last check (v2.9 -> v3.2, 3 commits)
**No new institutions** added; 14 existing institutions enriched with **23 new contact cells**:

### Tier 1 banks with NEW contact data (priority for outreach)
| Institution | Before -> After | Newly filled role(s) |
|---|---|---|
| Maybank Berhad | 4/7 -> **6/7** | Head of Compliance, Head of Internal Audit |
| Public Bank Berhad | 3/7 -> **5/7** | Head of Compliance, Head of Internal Audit |
| Maybank Islamic Berhad | 4/7 -> **5/7** | Head of Internal Audit |
| Citibank Berhad | 1/7 -> 2/7 | Chief Information Officer |
| ICBC (Malaysia) Berhad | 1/7 -> 2/7 | Head of Compliance |
| **BNP Paribas Malaysia** | 0/7 -> **1/7** | Chief Financial Officer (Kevin Wong) |
| **Deutsche Bank (Malaysia)** | 0/7 -> **1/7** | Chief Risk Officer (Surabhi Agarwal) |
| **J.P. Morgan Chase Malaysia** | 0/7 -> **1/7** | Head of Compliance (Gail Koh De Josselin) |

-> **3 Tier-1 foreign banks opened from zero** in v3.2 — BNP Paribas, Deutsche Bank, J.P. Morgan now each have a first named contact (low confidence, LinkedIn-sourced). These are warm leads: a single verified contact unlocks Tier-1 outreach.

### Tier 2+ upgrades
| Institution | Before -> After | Notes |
|---|---|---|
| Hong Leong Assurance | 1/7 -> **4/7** | +3 (biggest single jump) |
| Khazanah Nasional | 2/7 -> **5/7** | +3 |
| SME Bank | 2/7 -> **5/7** | +3 |
| Syarikat Takaful Malaysia | 3/7 -> **5/7** | +2 |
| Bank Rakyat | 3/7 -> 4/7 | +1 |
| BSN | 3/7 -> 4/7 | +1 |

## Tier 1 bank coverage snapshot (29 institutions)
- **Fully enriched (7/7): 6** — Bank Islam, Bank Muamalat, CIMB, CIMB Islamic, RHB, RHB Islamic
- **With contacts: 26 / 29** (90%) — up from 23 at last check
- **Still empty (0/7): 3** — Credit Suisse (MY), Mizuho Bank (MY), Sumitomo Mitsui (MY)
- **1-2 contacts (thin): 4** — BNP Paribas (1), Deutsche (1), J.P. Morgan (1)

## Actionable recommendations for sales outreach prioritization
1. **Maybank and Public Bank are now outreach-ready** (6/7 and 5/7) — flagship Tier-1 domestic banks with near-complete stakeholder maps. Prioritise multi-threaded outreach to CISO/CIO/CRO/Compliance.
2. **Open the 3 newly-started foreign Tier-1 banks** — BNP Paribas, Deutsche, J.P. Morgan each have exactly one named contact. Validate via official source, then expand to adjacent roles (single-thread risk).
3. **Credit Suisse / Mizuho / Sumitomo Mitsui remain blind** — zero contacts. These are the hardest Tier-1 gaps; consider deprioritising or sourcing via parent-group leadership.
4. **Close the 6/7 -> 7/7 gap on Maybank** — only Head of GRC missing; one lookup completes the full stakeholder set.
5. **Role strategy:** CISO + Head of GRC are the structural bottlenecks (13.7% / 11.7%, flat this cycle). A dedicated sourcing pass on these two roles would unlock the largest number of fully-enriched upgrades.

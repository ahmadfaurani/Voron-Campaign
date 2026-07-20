# VoronDRQ Prospect Database Monitor — Intelligence Brief
**Run:** 2026-07-17 23:00 MYT | **Source:** prospect-database-7stakeholders.csv (repo ROOT, commit 203f95e, v5.1)
**Prev run:** 2026-07-17 15:55 MYT (commit 659f4ac, v5.0) | **Classification:** TLP:AMBER

## Headline
v5.1 enrichment landed (commit 20:59 MYT): **+14 stakeholder contacts across 8 Tier-2 Insurer/Takaful institutions**, driven by the newly-tapped **Malaysian Insurance Directory 2025/2026** (Malaysian RE Corp, conf 85–90). No new institutions, no Tier-1 changes, no new fully-enriched. Cell-fill rate +1.0pp to **39.0%**; enrichment rate holds **58.0%**. **CRO was the biggest gainer (+7)** — now tied #2 for role completion.

## 1. Database size & composition (unchanged)
- **205 real institutions** (+1 phantom junk row persists → raw 206). **0 added, 0 removed.**
- **Tier:** T1=29, T2=53, T3=49, T4=35, T5=24, T6=15
- **Segment:** Licensed Banks 29, Insurers 26, GLC-Linked 24, Cooperatives 21, E-Money 19, MSBs 17, Investment Banks 15, Fintech Sandbox 13, Takaful 12, Development FIs 11, Card Schemes 10, Payment Operators 6, Fintech Registered 2

## 2. Enrichment progress (v5.0 → v5.1)
- **119 / 205** with ≥1 contact = **58.0%** (unchanged) | **86** empty (42.0%)
- **560 / 1,435** role-cells filled = **39.0%** (+14 cells, +1.0pp from 38.0%)
- **32** fully enriched 7/7 (unchanged)
- **Role completion (high→low):** CFO 97 (47.3%) · **CRO 86 (42.0%, +7 ← biggest gainer)** · CIO 86 (42.0%, +2) · Compliance 85 (41.5%, +1) · GRC 79 (38.5%) · Internal Audit 69 (33.7%, +3) · **CISO 58 (28.3%, +1) — still lowest**

## 3. New contacts since last check (v5.1 · +14 cells / 8 institutions)
All Tier-2, Insurers/Takaful. Source: Malaysian Insurance Directory 2025/2026 (conf 85–90).

| Institution | Segment | Δ | New roles | Now |
|---|---|---|---|---|
| Tokio Marine Life Insurance MY | Insurers | +4 | CRO Andrew Ngou, Compliance Loh Chee Hoong, CIO Nicholas Tan, IA Wong Kah Keong | 1→5/7 |
| Berjaya Sompo Insurance | Insurers | +3 | CISO Mohamad Azman, CRO Samson Liew, IA Kesavan Raj | 2→5/7 |
| Chubb Insurance Malaysia | Insurers | +2 | CRO Ng Khai Yan, IA Chong Keh Bin | 3→5/7 |
| Manulife Insurance Berhad | Insurers | +1 | CRO Mohd Naim Mohd Arsad | 3→4/7 |
| MCIS Insurance Berhad | Insurers | +1 | CRO Nurliana Mat Lazim | 4→5/7 |
| Takaful IKHLAS Berhad | Takaful | +1 | CIO Lee Kok Seong | 3→4/7 |
| Family Takaful Berhad | Takaful | +1 | CRO Shizal Fisham Ramli | 5→6/7 |
| Prudential BSN Takaful Berhad | Takaful | +1 | CRO Anita Menon | 1→2/7 |

**Data-quality upgrades (3 cells, count unchanged):** Agrobank CIO → official [agrobank.com.my, conf 95]; PayNet CFO + CIO reformatted from raw scraper pipe-format → official [paynet.my, conf 95].

## 4. New institutions / Tier-1 with new contact data
- **New institutions: none** (roster stable at 205).
- **Tier-1 banks with NEW contact data this cycle: NONE.** All 14 new cells went to Tier-2 insurers/takaful. Tier-1 is unchanged from v5.0.

## 5. Tier-1 status (unchanged — for outreach readiness)
29/29 T1 banks have ≥1 contact (100%). **18 nominal / 17 true** fully enriched (7/7).
- **Ready (17 true 7/7):** Maybank, CIMB, Alliance, AmBank, RHB, Hong Leong, Bank Islam, OCBC, StanChart, Bank of China, UOB (+ Islamic subsidiaries).
- Bank Muamalat listed 7/7 but CISO = misfiled CEO Khairul Kamarudin → true 6/7.
- **Partials:** Public Bank / Public Islamic 6/7 (-CISO) · BNP 5/7 · Citibank 5/7 · HSBC 5/7 · ICBC 4/7 · Deutsche 3/7 · SMBC 3/7 · Credit Suisse / J.P.Morgan / Mizuho 1/7.
- **CISO-misfiled-CEO persists in 4 T1 CISO cells** (Bank Muamalat, ICBC, SMBC, Mizuho) — true CISO gap is wider than the 28.3% headline.

## 6. Data-integrity alerts
1. **Phantom row persists:** Sun Life CEO unescaped-quote fragment → real 205 / raw 206. Unfixed since v4.7. FIX: quote the Sun Life CISO cell.
2. **CEO-misfiled-in-CISO persists:** Bank Muamalat, ICBC, SMBC, Mizuho (T1) + Sun Life, Kurnia (T2). Inflates CISO coverage.
3. **Good cleanup this run:** PayNet CFO/CIO + Agrobank CIO reformatted to official-source attribution.

## 7. Actionable intelligence — sales outreach priority
**GREEN-LIGHT (new this cycle — T2 insurers at 5/7, strongest new insurer coverage):**
- **Tokio Marine Life Insurance** (1→5/7, +4 roles, MID conf 90) — biggest leap; approach via CRO Andrew Ngou or CIO Nicholas Tan.
- **Berjaya Sompo** (2→5/7) + **Chubb Insurance** (3→5/7) — both 5/7 with named CRO+IA(+CISO/Compliance). Ready for multi-threaded insurer outreach.
- **MCIS Insurance** (4→5/7), **Family Takaful** (5→6/7, near-full) — approaching full coverage.

**Standing (unchanged):** 17 true fully-enriched T1 banks ready; Lonpac (T2, 7/7 prior cycle); Manulife CFO/CIO (Annual Report 2024 official).

**Highest-leverage gap:** CISO still lowest at 28.3% true. T1 CISO gap-fill targets: Public Bank, BNP, Citibank, HSBC, ICBC.

**VERIFY before cold outreach:** the 14 new v5.1 contacts are sourced from an industry directory (MID 2025/2026), not institution official pages (conf 85–90) — recommend light LinkedIn/official cross-check of named individuals before send.

**REPAIR queue:** fix Sun Life phantom row; clean CEO-misfiled CISO cells (Bank Muamalat, ICBC, SMBC, Mizuho, Sun Life, Kurnia); dedup MARA.

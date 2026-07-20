# VoronDRQ Prospect Database Monitor — Intelligence Brief
**Run:** 2026-07-20 12:34 MYT | **Source:** prospect-database-7stakeholders.csv (repo ROOT, commit cfcbc96, v5.4)
**Prev run:** 2026-07-17 05:05 MYT (commit 5f6c048, v5.3 fix2) | **Classification:** TLP:AMBER
**Source note:** Task URL `prospects/...` still 404 — canonical CSV lives at repo ROOT, fetched via git (known issue).

## Headline
v5.4 enrichment landed (commit 08:39 MYT, ~4h after last check): **+35 stakeholder contact cells across 8 institutions** (5 GLC-Linked, 3 MSBs), all driven from empty (0/7). **Headline win: KWSP/EPF Investment Division — 3 sub-division rows driven to full 7/7** from the official kwsp.gov.my org chart (conf 98), the first Malaysian government institution with all 7 target roles confirmed from an official source, **including the rare CISO**. Enrichment rate **+3.9pp to 62.4%**; cell-fill **+2.5pp to 42.2%**; fully-enriched **33 to 36**. **CFO crossed 50%** (now 51.7%, biggest gainer +8). **No new institutions, no Tier-1 changes.** Phantom row persists.

## 1. Database size & composition (unchanged)
- **205 real institutions** (+1 phantom junk row persists -> raw 206). **0 added, 0 removed.**
- **Tier:** T1=29, T2=53, T3=49, T4=35, T5=24, T6=15
- **Segment:** Licensed Banks 29, Insurers 26, GLC-Linked 24, Cooperatives 21, E-Money 19, MSBs 17, Investment Banks 15, Fintech Sandbox 13, Takaful 12, Development FIs 11, Card Schemes 10, Payment Operators 6, Fintech Registered 2

## 2. Enrichment progress (v5.3 fix2 -> v5.4)
- **128 / 205** with >=1 contact = **62.4%** (+3.9pp) | **77** empty (37.6%)
- **605 / 1,435** role-cells filled = **42.2%** (+35 cells, +2.5pp from 39.7%)
- **36** fully enriched 7/7 (+3)
- **Role completion (high to low):** CFO 106 (**51.7%, +8 <- biggest gainer, crossed 50%**) · CIO 94 (45.9%, +5) · CRO 93 (45.4%, +5) · Compliance 92 (44.9%, +6) · GRC 80 (39.0%, +4) · Internal Audit 77 (37.6%, +4) · **CISO 63 (30.7%, +3 — still lowest)**

> **+35 vs +32 footnote:** The git commit msg / enrichment report cite "+32 roles". Independent monitor recount against the **verified last-check baseline (570 cells at v5.3 fix2)** yields **+35**. The 3-cell gap is the enrichment report internal "v5.3" baseline of 573 vs the verified 570; the **post-v5.4 totals (605) match exactly**. Reporting +35 as the verified cycle delta.

## 3. New contacts since last check (v5.4 · +35 cells / 8 institutions)
All 8 went from **0 (empty) -> populated**. 5 are T5/GLC-Linked, 3 are T3/MSBs.

| Institution | Tier/Seg | Delta | New roles | Now | Source / Conf |
|---|---|---|---|---|---|
| KWSP Investment Division (x3: Alt Assets, Direct Inv, Real Estate) | T5/GLC-Linked | +7 each (x3 = +21) | CISO Jasmine Goh, GRC Nora Badaruddin, CFO Ahmad Rizal Omar, CRO Rozlina Abdul Samad, Compliance Chong Yee Leng, CIO Afhzal Abdul Rahman, IA Mohammad Nasir Ismail | 0->**7/7 FULL x3** | kwsp.gov.my · conf 98 |
| Instarem Sdn Bhd (Nium Malaysia) | T3/MSBs | +4 | CFO Andre Mancl, CIO Sekhar Cidambi, CRO+Compliance Amaresh Mohan (same person) | 0->4/7 | nium.com · conf 95 |
| Permodalan BSN Berhad (PBSNB) | T5/GLC-Linked | +3 | CFO Suzylah Mohamed Noor, CRO+Compliance Wong Ching Fai (same person) | 0->3/7 | pbsn.com.my · conf 90-95 |
| Permodalan Negeri Selangor (PNSB) | T5/GLC-Linked | +3 | CFO Ahmad Zamwawi, GRC+IA Mohammed Hanafi (same person) | 0->3/7 | pnsb.com.my · conf 90-95 |
| Wise (formerly TransferWise) Malaysia | T3/MSBs | +3 | CFO Emmanuel Thomassin, CIO Harsh Sinha, Compliance Nita Patel | 0->3/7 | owners.wise.com · conf 95 |
| SenangPay Sdn Bhd | T3/MSBs | +1 | CFO Mohd Mutalib | 0->1/7 | LinkedIn · conf 70 |

**Caveat — +35 cells != 35 distinct people.** The same 7 KWSP executives are replicated across the 3 divisional sub-rows, and CRO/Compliance (and GRC/IA) are combined under one person at Instarem/PBSNB/PNSB. **Distinct new named individuals ~18** (7 KWSP + 3 Instarem + 2 PBSNB + 2 PNSB + 3 Wise + 1 SenangPay).
**Instarem & Wise contacts are GLOBAL parent execs** (Nium, Wise Plc), not Malaysia-local heads — Malaysia entities are subsidiaries.

## 4. New institutions / Tier-1 with new contact data
- **New institutions: none** (roster stable at 205; the 3 KWSP sub-rows were pre-existing empty rows, now populated).
- **Tier-1 banks with NEW contact data this cycle: NONE.** All 35 new cells went to T3 MSBs & T5 GLC-Linked. **Tier-1 is unchanged from v5.3 fix2.**

## 5. Tier-1 status (unchanged — for outreach readiness)
29/29 T1 banks have >=1 contact (100%). **18 nominal / 17 true** fully enriched (7/7).
- **Ready (17 true 7/7):** Maybank, Maybank Islamic, CIMB, CIMB Islamic, Alliance, Alliance Islamic, AmBank, AmBank Islamic, RHB, RHB Islamic, Hong Leong, Hong Leong Islamic, Bank Islam, OCBC, StanChart, Bank of China, UOB.
- Bank Muamalat listed 7/7 nominal but **CISO = misfiled CEO Khairul Kamarudin** -> true 6/7.
- **Partials:** Public Bank / Public Islamic 6/7 (-CISO) · BNP 5/7 (-CISO,CIO) · Citibank 5/7 (-CISO,Compliance) · HSBC 5/7 (-CISO,IA) · ICBC 4/7 (-GRC,CFO,CIO) · Deutsche 3/7 · SMBC 3/7 · Credit Suisse 1/7 · J.P. Morgan 1/7 · Mizuho 1/7.

## 6. Data-integrity alerts
1. **Phantom row persists:** Sun Life unescaped-quote fragment -> real 205 / raw 206. **Unfixed since v4.7.** FIX: quote the Sun Life CISO cell.
2. **CEO-misfiled-in-CISO persists:** Bank Muamalat (T1), ICBC, Mizuho, SMBC + others. Inflates CISO coverage; **true CISO completion < 30.7%**.
3. **NEW — 3 entities confirmed non-existent this cycle** (still in DB, recommend removal/flag): **PNB Capital Berhad, PNB Equity Fund Berhad, Manulife Takaful Malaysia Berhad**.
4. **KWSP modeling note:** same 7 executives across 3 Investment Division rows — **7 distinct contacts, not 21.** Pick one division to approach to avoid duplicate outreach.
5. **Instarem/Wise:** contacts are global parent (Nium/Wise Plc) execs, not Malaysia-local — subsidiary-level head still missing.
6. **Standing duplicates still open:** GX Bank/GXBank (T6), MARA (T3 Dev FIs + T5 GLC-Linked).

## 7. Actionable intelligence — sales outreach priority

**GREEN-LIGHT (new this cycle):**
- **KWSP/EPF Investment Division (T5 GLC-Linked, 0->7/7 x3 rows, kwsp.gov.my conf 98)** — strongest new coverage; first Malaysian govt institution with all 7 roles incl. rare CISO. **Approach: Head of Digital Security Jasmine Goh (CISO) or CFO Ahmad Rizal Omar.** Pick ONE division (e.g., Direct Investments) to avoid duplicate outreach. Relevant if VoronDRQ targets the EPF investment arm.
- **PBSNB (T5 GLC, 0->3/7, pbsn.com.my)** — approach CFO Suzylah Mohamed Noor or Head of Risk & Compliance Wong Ching Fai.
- **PNSB (T5 GLC, 0->3/7, pnsb.com.my)** — approach CFO Ahmad Zamwawi or Mohammed Hanafi (Integrity/Audit/Governance).

**SOFTER (global-parent contacts, not Malaysia-local):**
- **Instarem/Nium (T3 MSB, 0->4/7)** — contacts are Nium global execs (CFO Andre Mancl, CTO Sekhar Cidambi, CRO Amaresh Mohan). Subsidiary-level Malaysia head still missing.
- **Wise Malaysia (T3 MSB, 0->3/7)** — contacts are Wise Plc global execs. Same caveat.

**VERIFY before outreach:**
- **SenangPay (T3 MSB, 0->1/7)** — single CFO from LinkedIn (conf 70). Light verify before send.

**Standing (unchanged):** 17 true fully-enriched T1 banks ready for full multi-thread outreach. Lonpac (T2, 7/7), MIDF (T2), Phillip Securities (T2), MoneyMatch (T3) from prior cycles.

**Highest-leverage gap:** CISO still lowest at 30.7% (true rate lower due to CEO-misfile). **T1 CISO gap-fill targets unchanged:** Public Bank, BNP, Citibank, HSBC, ICBC.

**REPAIR queue:** fix Sun Life phantom row; clean CEO-misfiled CISO cells (Bank Muamalat, ICBC, Mizuho, SMBC); **remove/flag 3 non-existent entities** (PNB Capital, PNB Equity Fund, Manulife Takaful); dedup GX Bank/GXBank + MARA.

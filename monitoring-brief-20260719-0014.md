# VoronDRQ Prospect Database Monitor - Intelligence Brief
**Run:** 2026-07-19 08:14 MYT | **Latest source:** prospect-database-enriched-v5.9.csv (repo ROOT, commit 3d39acc, Jul 18 04:56 MYT)
**Prev analyzed baseline:** v5.6 (analysis_now_v56.json, Jul 18 19:19 MYT) | **Prev delivered brief:** v5.4 (Jul 18 11:07 MYT)
**Classification:** TLP:AMBER | **Convention:** STRICT = real named contacts (excludes NOT-FOUND audit notes); LOOSE = any non-empty (matches official reports)

## [!] Headline - two critical findings
1. **WORKFLOW DRIFT:** The canonical monitored CSV ("prospect-database-7stakeholders.csv" at repo root - the file the task URL resolves to) is **STUCK at v5.8**. The v5.9 enrichment was committed as a *separate* versioned file ("prospect-database-enriched-v5.9.csv") and was **NOT merged back** into the canonical source. Anyone monitoring the canonical file sees v5.8 and misses v5.9's +5 full-7/7 Dev FIs/GLC and the phantom-row fix. **Action: merge v5.9 into the canonical CSV.**
2. **"7/7" OVERSTATES READINESS:** Under strict (real named contacts) counting, several banks shown as 7/7 in the official reports are actually 6/7 or 5/7 - the missing cells are "NOT FOUND [reason]" audit notes, not people. CISO is the dominant false-positive gap.

**Progress headline (STRICT):** since the last analyzed baseline (v5.6), +151 real contact cells (604->755), +33 institutions gained a contact (133->166, 64.9%->81.0%), +28 reached true full 7/7 (30->58), empties cut 72->39 (-33). **CISO was the biggest gainer (+47, 44->91)** via product-brand inheritance + CISO-equivalent mapping.

## 1. Database size & composition (stable)
- **205 institutions** (roster unchanged: 0 added, 0 removed across v5.6->v5.9).
- Phantom Sun Life junk row: **FIXED in v5.9** (was 1, now 0). Long-standing data-integrity debt cleared.
- **Tier:** T1=29, T2=53, T3=49, T4=35, T5=24, T6=15
- **Segment:** Licensed Banks 29, Insurers 26, GLC-Linked 24, Cooperatives 21, E-Money 19, MSBs 17, Investment Banks 15, Fintech Sandbox 13, Takaful 12, Development FIs 11, Card Schemes 10, Payment Operators 6, Fintech Registered 2

## 2. Enrichment progress - v5.9 (latest)
| Metric | STRICT (real people) | LOOSE (official headline) |
|---|---|---|
| Cells filled | **755 / 1,435 = 52.6%** | 800 / 1,435 = 55.7% |
| >=1 contact | **166 / 205 = 81.0%** | 181 / 205 = 88.3% |
| Empty (0/7) | **39 (19.0%)** | 24 (11.7%) |
| Full 7/7 | **58 (true)** | 74 (nominal, incl. NOT-FOUND) |

**Role completion (STRICT, high->low):** CFO 135 (65.9%) - CIO 122 (59.5%) - CRO 109 (53.2%) - Compliance 109 (53.2%) - GRC 97 (47.3%) - IA 92 (44.9%) - **CISO 91 (44.4% - still lowest, but +47 since v5.6)**

## 3. Deltas
**A. Since last analyzed baseline (v5.6 -> v5.9, STRICT)** - spans v5.7+v5.8+v5.9 (3 cycles):
- Cells 604->755 (**+151**) - >=1 contact 133->166 (**+33**) - true 7/7 30->58 (**+28**) - empty 72->39 (**-33**)
- CISO 44->91 (**+47**, biggest) - CIO 101->122 (+21) - CFO 114->135 (+21) - GRC 79->97 (+18) - Compliance 93->109 (+16) - CRO 94->109 (+15) - IA 79->92 (+13)

**B. Freshest single cycle (v5.8 -> v5.9, STRICT):**
- +5 real CISO-equivalent cells; **+5 institutions to true 7/7**; phantom row fixed; +15 NOT-FOUND audit notes (inflate LOOSE, add no real people).
- Newly 7/7 (all via CISO-equivalent from official sources): **Agrobank** (Nolan Jeffrey A/L Abdul Hai, Group CIO), **BPMB** (Hairil Izwar Abd Rahman, Group CDTO), **EXIM Bank** (Hairil - inherited post May-2025 BPMB merger), **SME Bank** (Hairil - same, inherited), **Lembaga Tabung Haji** (Shamsul Kamal Hussein Kamal, CITO).
- **Note:** BPMB/EXIM/SME Bank share the SAME CISO-equivalent person (Hairil Izwar Abd Rahman) after the May 2025 BPMB Group merger - 3 institutions, 1 distinct contact. Approach via BPMB Group.

## 4. [!] Tier-1 readiness - STRICT view (for outreach)
**18 / 29 T1 banks are TRULY fully enriched** (real named contact in all 7 roles):
- Alliance, Alliance Islamic, AmBank, AmBank Islamic, Bank Islam, Bank of China, CIMB, CIMB Islamic, Hong Leong, Hong Leong Islamic, Maybank, Maybank Islamic, OCBC, RHB, RHB Islamic, StanChart, UOB, Bank Muamalat.

**Nominal 7/7 but STRICT <7 (NOT-FOUND gaps - do NOT treat as ready):**
| Bank | True | Missing (NOT-FOUND note, not a person) |
|---|---|---|
| Public Bank | 6/7 | CISO (no CISO among 25 Heads of Division) |
| Public Islamic | 6/7 | CISO (shares Public Bank leadership) |
| BNP Paribas | 5/7 | CISO + CIO |
| Citibank | 5/7 | CISO + Compliance |
| HSBC | 5/7 | CISO + IA |

**True partials (real gaps):** ICBC 4/7 (GRC,CFO,CIO) - Deutsche 3/7 - SMBC 3/7 - Credit Suisse 1/7 - J.P. Morgan 1/7 - Mizuho 1/7.

**The T1 CISO wall persists:** Public Bank, Public Islamic, BNP, Citibank, HSBC - all confirmed CISO NOT-FOUND from official sources. CISO is structurally un-listed at Malaysian banks (usually embedded under Group CIO/CDTO). Recommend approaching via the CISO-equivalent (Group CIO/CTO/CDTO) as v5.9 did for Dev FIs.

## 5. Still-empty institutions (39 STRICT-empty; 24 LOOSE-empty)
The LOOSE-empty 24 are concentrated where leadership is not publicly listed:
- **20 Cooperatives** (Koperasi Angkatan Tentera, Guru, Johor, KL, Kakitangan Kerajaan, Kedah, Kelantan, Labuan, Melaka, Negeri Sembilan, Pahang, Perak, Perlis, Polis Diraja, Pulau Pinang, Putrajaya, Sabah, Sarawak, Selangor, Tentera Malaysia, Terengganu) - co-op leadership rarely public.
- **4 China-parent e-money:** Alipay+ Malaysia (Ant Group), WeChat Pay Malaysia (Tencent) x2 rows (likely a duplicate to dedup).
- The 39 STRICT-empty adds 15 institutions whose cells are pure NOT-FOUND notes (no real person) - research-exhausted, mostly T1/T2 banks with confirmed-no-CISO.

## 6. Actionable intelligence - sales outreach priority
**GREEN-LIGHT (newly true-7/7 this cycle, v5.9, official sources):**
- **BPMB Group (Dev FI, T3)** - Hairil Izwar Abd Rahman (Group CDTO, CISO-equiv). Single point of contact also covers EXIM Bank + SME Bank post-merger. Highest-leverage new contact: one relationship opens 3 institutions.
- **Agrobank (Dev FI, T3)** - Nolan Jeffrey A/L Abdul Hai (Group CIO, CISO-equiv), agrobank.com.my official.
- **Lembaga Tabung Haji (GLC, T5)** - Shamsul Kamal Hussein Kamal (CITO, CISO-equiv).

**READY (true-7/7 T1, unchanged):** 18 T1 banks above - full multi-thread outreach ready.

**APPROACH VIA CISO-EQUIVALENT (T1 CISO wall - do not wait for named CISO):** Public Bank, Public Islamic, BNP, Citibank, HSBC - engage Group CIO / COO / Head of Technology as the de facto security owner. Same pattern that just unlocked 5 Dev FIs.

**HIGHEST-LEVERAGE GAP:** CISO still lowest at 44.4% strict. The v5.9 method (map CISO-equivalent = Group CIO/CDTO/CTO from official leadership pages) is repeatable - apply it to the remaining ~15 confirmed-NOT-FOUND CISOs.

**REPAIR QUEUE:**
1. **Merge v5.9 into canonical "prospect-database-7stakeholders.csv"** - monitored file is stale at v5.8 (headline finding #1).
2. **Dedup WeChat Pay Malaysia** (2 rows) - leftover from prior GX Bank/GXBank issue.
3. **Cooperatives (20)** - public-source-dead; consider flagging as "research-exhausted / approach via regulator (SKM)" rather than continuing web research.
4. **T1 NOT-FOUND CISO cells** - relabel as "CISO-equivalent approach required" so the 7/7 count stops overstating readiness.

## 7. Data-integrity alerts
1. **Canonical CSV drift (NEW, high):** v5.9 lives only in a versioned side-file; canonical monitored CSV is v5.8. Any pipeline pointed at the canonical file is silently one cycle behind.
2. **Counting-convention inconsistency:** official reports mix LOOSE (v5.8 headline 790/55.1% incl. NOT-FOUND) and STRICT (v5.9 per-role CISO=91 excl. NOT-FOUND). Cross-version totals are not directly comparable. This brief standardizes on STRICT for all deltas.
3. **Phantom row: FIXED** in v5.9 (was open since v4.7).
4. **BPMB-Group shared contact:** Hairil Izwar Abd Rahman spans BPMB + EXIM + SME Bank - count as 1 distinct person, not 3.
5. **Standing items still open:** CEO-misfiled-in-CISO (Bank Muamalat et al.) - verify Bank Muamalat's 7/7 is a true CISO, not a misfiled CEO; GX Bank/GXBank + MARA duplicates.

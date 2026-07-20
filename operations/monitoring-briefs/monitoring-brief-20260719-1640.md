# VoronDRQ Prospect Database Monitor — Intelligence Brief
**Run:** 2026-07-19 16:40 UTC | **Source:** prospect-database-7stakeholders.csv (repo ROOT, commit 46ec566 = v5.14, Jul 19 16:24 UTC)
**Prev baseline:** v5.13 (7c4941f, Jul 19 12:56 UTC) | **Last delivered brief:** v5.9 (Jul 19 00:14 UTC)
**CSV integrity:** Local file md5-matches GitHub raw (VERIFIED). Task URL prospects/... still 404 — canonical file is at repo root.
**Classification:** TLP:AMBER | **Two counts:** POPULATED = any non-empty cell (literal task definition); ACTIONABLE = real named contact (excludes "NOT FOUND" audit notes and CEO-misfiled) — the count that enables outreach.

---

## [!] Headline
**v5.14 was a data-quality cycle, not a growth cycle.** Net real contacts added since the v5.13 baseline: **+3** — all at a single institution (Manulife Takaful, 2/7 to 5/7). Meanwhile **+78 "NOT FOUND" audit-trail cells** were logged across the former 2/7 cluster, and **2 CEO-as-CISO misclassifications were corrected** (Zurich Life, MARA). The 2/7 cluster shrank 17 to 14 because research was **exhausted** (negative findings documented), not because people were found. **No new institutions, no T1 progress, no change in enrichment rate.** This signals diminishing returns on publicly-disclosed Malaysian financial-sector leadership — the next lever is the 1/7 cluster (32 institutions) and CISO-equivalent outreach, not more scraping.

---

## 1. Database size and composition (STABLE — 0 added/removed)
- **205 institutions** (206 raw rows; 1 phantom Sun Life junk row persists, unfixed since v4.7)
- **Tier:** T1=29, T2=53, T3=49, T4=35, T5=24, T6=15
- **Segment:** Licensed Banks 29, Insurers 26, GLC-Linked 24, Cooperatives 21, E-Money 19, MSBs 17, Investment Banks 15, Fintech Sandbox 13, Takaful 12, Development FIs 11, Card Schemes 10, Payment Operators 6, Fintech Registered 2

## 2. Enrichment progress — v5.14 (current)
| Metric | POPULATED (non-empty) | ACTIONABLE (real people) |
|---|---|---|
| Cells filled | 969 / 1,435 = **67.5%** | 750 / 1,435 = **52.3%** |
| Institutions with >=1 contact | 181 / 205 = **88.3%** | 156 / 205 = **76.1%** |
| Completely empty | 24 (11.7%) | 49 (23.9%)* |
| Full 7/7 | 120 (nominal) | **55 (true)** |

*49 with no real contact = 24 truly-empty cells + 25 institutions whose only cells are "NOT FOUND" / CEO-misfiled placeholders.

**Cluster distribution (by REAL contacts):** 0/7=49, 1/7=23, 2/7=13, 3/7=6, 4/7=13, 5/7=30, 6/7=16, **7/7=55**

**Role completion (ACTIONABLE, ranked high to low):**
| Rank | Role | Filled | % | Delta vs v5.13 |
|---|---|---|---|---|
| 1 | CFO | 136/205 | 66.3% | 0 |
| 2 | CIO | 121/205 | 59.0% | 0 |
| 3 | Compliance | 115/205 | 56.1% | +1 |
| 4 | CRO | 111/205 | 54.1% | +1 |
| 5 | GRC | 101/205 | 49.3% | 0 |
| 6 | Internal Audit | 95/205 | 46.3% | +1 |
| 7 | **CISO** | 71/205 | **34.6%** | 0 (lowest) |

> CISO is the structural wall: 73 cells are "NOT FOUND" + 21 are CEO-misfiled = **94 of 205 institutions (45.9%) have no real CISO**. CISO is the dominant blocker for Tier-1 banks.

---

## 3. Deltas since last baseline (v5.13 to v5.14, 1 commit)
**Real contacts:** 747 to 750 cells (**+3**), all at Manulife Takaful. 0 new institutions. 0 change in enrichment rate (76.1%) or true-full count (55).
**Audit trails:** "NOT FOUND" cells 117 to 195 (**+78**) — negative-findings documentation, not people.
**Nominal (inflated):** cells 890 to 969 (+79); nominal full-7/7 104 to 120 (+16, illusory from NOT FOUND fills).
**Corrections (2):** Zurich Life CISO — "Pauline Teoh" is CEO, not CISO, replaced with NOT FOUND. MARA CISO — "Datuk Zulfikri Osman" is Ketua Pengarah (CEO), not CISO, replaced with NOT FOUND.
**Data-quality flags:** CEO-as-CISO misclassification systemic (21 remaining; 3 corrected cumulatively v5.13-v5.14). **Duplicate MARA rows** (listed under both T3/Dev FIs and T5/GLC-Linked) — only the GLC row's CISO was corrected; the Dev FI row still CEO-misfiled. Phantom Sun Life row persists.

### 3 new real contacts this cycle (all Manulife Takaful, Manulife Holdings AR 2025)
| Institution | Role | Name | Conf |
|---|---|---|---|
| Manulife Takaful Malaysia Berhad | Chief Risk Officer | Mohd Naim Bin Mohd Arsad | 85 |
| Manulife Takaful Malaysia Berhad | Head of Compliance | Senthil Woon Wai Keong | 85 |
| Manulife Takaful Malaysia Berhad | Head of Internal Audit | Krishna Rajaa Ramalingam | 90 |

Manulife Takaful promoted **2/7 to 5/7** (also has CFO Ng Chun Nam, CIO Bernard Sia).

---

## 4. Tier-1 readiness (UNCHANGED this cycle — for outreach)
**17 / 29 T1 banks TRULY full 7/7 — READY for full multi-thread outreach** (unchanged since v5.8):
Alliance, Alliance Islamic, AmBank, AmBank Islamic, Bank Islam, Bank of China, CIMB, CIMB Islamic, Hong Leong, Hong Leong Islamic, Maybank, Maybank Islamic, OCBC, RHB, RHB Islamic, StanChart, UOB.

**One role from full (6/7 — CISO is the only gap, approach via Group CIO/CDTO):**
| Bank | True | Gap |
|---|---|---|
| Public Bank | 6/7 | CISO = NOT FOUND (no CISO among 25 Heads of Division) |
| Public Islamic Bank | 6/7 | CISO = NOT FOUND (shares Public Bank Group leadership) |
| Bank Muamalat | 6/7 | CISO = CEO-misfiled (Khairul Kamarudin is CEO) — needs correction |

**Further out:** HSBC 5/7 (-CISO, -IA), BNP Paribas 4/7, Citibank 4/7, Deutsche 3/7, ICBC 3/7, SMBC 3/7, Credit Suisse 1/7, J.P. Morgan 1/7, **Mizuho 0/7 real** (sole T1 with zero real contacts — only a CEO-misfiled CISO cell).

**28 / 29 T1 banks have >=1 real contact.** Mizuho is the lone exception.

---

## 5. Still-empty institutions (24 truly-empty)
Concentrated where leadership is not publicly disclosed:
- **20 Cooperatives** (Koperasi Angkatan Tentera, Guru, Johor, KL, Kakitangan Kerajaan, Kedah, Kelantan, Labuan, Melaka, Negeri Sembilan, Pahang, Perak, Perlis, Polis Diraja, Pulau Pinang, Putrajaya, Sabah, Sarawak, Selangor, Tentera Malaysia, Terengganu) — co-op leadership rarely public.
- **4 China-parent e-money:** Alipay+ Malaysia (Ant Group), WeChat Pay Malaysia (Tencent) x2 (likely duplicate to dedup).

---

## 6. Actionable intelligence — sales outreach priority
**[NEW] NEWLY ACTIONABLE THIS CYCLE:**
- **Manulife Takaful Malaysia Berhad (T2/Takaful, 5/7)** — now has CRO + Compliance + IA + CFO + CIO. Approach via **CIO Bernard Sia** or **CRO Mohd Naim Bin Mohd Arsad** (Manulife Insurance Berhad management, shared across Takaful entity).

**[READY] READY NOW (T1 true-7/7, unchanged since v5.8 — if not yet contacted, DO NOW):**
Maybank, CIMB, RHB, AmBank, Alliance, Hong Leong, Bank Islam, OCBC, StanChart, Bank of China, UOB (+ Islamic subs). These 17 have been fully enriched for ~24h+ — launch full 7-role multi-thread outreach.

**[PRIORITY] HIGHEST-ROI CISO GAP-FILL (T1, 6/7 — engage Group CIO/CTO as de facto security owner):**
Public Bank, Public Islamic Bank, Bank Muamalat. Same CISO-equivalent pattern that unlocked 5 Dev FIs in v5.9 — do not wait for a named CISO (structurally unlisted at Malaysian banks).

**[NEXT] NEXT ENRICHMENT TARGET:** the **1/7 cluster (32 institutions, ~192 roles recoverable)** — the largest remaining opportunity. The 2/7 cluster is now research-exhausted (14 remain, dominated by PayNet product brands, Allianz/Zurich/FWD insurance subs, and MARA — control-function roles systematically undisclosed).

**[HYGIENE] DATA HYGIENE (fix before next scrape):** (1) Correct Bank Muamalat and Mizuho CEO-as-CISO; (2) Dedup the two MARA rows; (3) Drop the phantom Sun Life row; (4) Resolve the WeChat Pay duplicate.

---
*Baseline checkpoint saved to memory (v5.14, 46ec566) for next-run diff. Source verified md5-identical to GitHub raw.*

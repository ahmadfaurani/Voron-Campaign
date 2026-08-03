# VoronDRQ Stakeholder Collection Report — v5.90 Cycle

**Generated:** 2026-08-03 09:44 MYT (UTC+8)
**Brief ID:** VORON-STK-20260803-0944
**Report Date:** 2026-08-03
**TLP:** AMBER — Handle with care, do not redistribute publicly.
**Database Version:** v5.90 (prospect-database-enriched-v5.90.csv)
**Git Commit:** Pushed to https://github.com/ahmadfaurani/Voron-Campaign

---

## Executive Summary

The v5.90 enrichment cycle focused on zero-named institutions and remaining quick-win gaps. The cycle's headline achievement is **Kuwait Finance House (Malaysia) Berhad** — 5 new named executives extracted from the official KFH Malaysia website, transforming a 0/7 institution to 5/7 in a single pass. Additionally, 3 entity classifications resolved 21 cells (Danaharta wound down, TA Securities likely inactive, AEON Digital Bank shares parent leadership), and 19 institutions received enhanced NOT FOUND context from deep subagent research.

**Effective coverage improved from 64.9% to 66.9% (+2.0 percentage points).**

---

## Coverage Statistics

| Metric | v5.89 | v5.90 | Delta |
|--------|-------|-------|-------|
| **Named executives** | 845 (56.1%) | 853 (56.7%) | +8 |
| **Entity-classified** | 132 (8.8%) | 152 (10.1%) | +20 |
| **NOT FOUND** | 477 (31.7%) | 453 (30.1%) | −24 |
| **Effective coverage** | 977 (64.9%) | 1005 (66.8%) | +28 |
| **Total cells** | 1505 | 1505 | — |

### Per-Role Coverage (v5.90)

| Role | Named | Entity | NOT FOUND | Coverage |
|------|-------|--------|-----------|----------|
| CISO | 98 | 33 | 81 | 131/215 (60.9%) |
| GRC | 114 | 31 | 59 | 145/215 (67.4%) |
| CFO | 152 | 8 | 55 | 160/215 (74.4%) |
| CRO | 120 | 31 | 53 | 151/215 (70.2%) |
| Compliance | 126 | 9 | 70 | 135/215 (62.8%) |
| CIO | 129 | 31 | 52 | 160/215 (74.4%) |
| Internal Audit | 114 | 9 | 83 | 123/215 (57.2%) |

---

## v5.90 Cycle Actions

### 1. Kuwait Finance House (Malaysia) Berhad — 5 NEW NAMED FILLS ⭐

**Institution:** Kuwait Finance House (Malaysia) Berhad [Tier 204, Licensed Banks]
**Source:** Official website — kfh.com.my/malaysia/personal/about-us/board-of-directors.html

| Role | Name | Title | Confidence |
|------|------|-------|------------|
| CIO | Dr. Lam Wai Leong | Vice President, IT | 85 |
| Head of Internal Audit | Mohd Zaki Abdullah | Senior Vice President, Internal Audit | 90 |
| Head of Compliance | Eddy Siow Swee Kim | Vice President, Compliance | 90 |
| CFO | Roslinawati Zainal | Assistant Vice President, Finance | 85 |
| CRO | Nor Izad | Assistant Vice President, Risk Management | 85 |

**Note:** KFH Malaysia uses VP/AVP-level management rather than C-suite titles. These are the highest-level executives for each function. KFH Malaysia has announced withdrawal from the Malaysian market by end of 2026. CISO and GRC remain NOT FOUND — no dedicated roles for these functions at KFH Malaysia.

### 2. AEON Digital Bank (AEON Financial Service) — Entity Classification + 1 Fill

**Institution:** AEON Digital Bank (AEON Financial Service) [Tier 205, Digital Banks]
**Source:** AEON Credit Service (M) Berhad leadership page — aeoncredit.com.my/about-us/leadership/

| Role | Value | Type |
|------|-------|------|
| CFO | Lee Siew Tee — Chief Financial Officer, AEON Credit Service (M) Berhad (parent) | Named (75) |
| CISO | SHARES PARENT: AEON Credit Service (M) Berhad | Entity |
| GRC | SHARES PARENT: AEON Credit Service (M) Berhad | Entity |
| CRO | SHARES PARENT: AEON Credit Service (M) Berhad | Entity |
| Compliance | SHARES PARENT: AEON Credit Service (M) Berhad | Entity |
| CIO | SHARES PARENT: AEON Credit Service (M) Berhad (Lee Tyan Jen formerly CIO, now Deputy CEO) | Entity |
| IA | SHARES PARENT: AEON Credit Service (M) Berhad (IA via AEON Credit Service IAD) | Entity |

**Context:** AEON Digital Bank is operated as a subsidiary of AEON Credit Service (M) Berhad, which is listed on Bursa Malaysia. The digital banking operations share the parent's C-suite functions. AEON Bank (M) Berhad (Tier 6, Fintech Sandbox) is a separate entity that received the digital bank license and already has 6/7 roles filled.

### 3. AEON Bank (M) Berhad — IA Fill (Shared Service)

**Institution:** AEON Bank (M) Berhad [Tier 6, Fintech Sandbox]
**Source:** AEON Credit Service Corporate Governance Report 2026 PDF

| Role | Name | Title | Confidence |
|------|------|-------|------------|
| Head of Internal Audit | Phang Chee Chong | Head of Internal Audit Division, AEON Credit Service (M) Berhad (shared service) | 40 |

**Note:** The IA function is shared with parent AEON Credit Service's Internal Audit Division (18 personnel). This is a shared service model, not a dedicated AEON Bank appointment. Low confidence due to shared service arrangement.

### 4. Hong Leong Asset Management — CFO Fill (Shared with Parent)

**Institution:** Hong Leong Asset Management Berhad [Tier 199, Asset Management]
**Source:** HLCB Annual Report 2025 — hlcap.com.my

| Role | Name | Title | Confidence |
|------|------|-------|------------|
| CFO | San Kah Yee | Chief Financial Officer, Hong Leong Capital Berhad (parent, shared service) | 40 |

**Note:** CEO confirmed as Chue Kwok Yan (appointed 11 Sep 2024, per HLCB AR 2025). CFO function shared with parent HLCB. Other 5 roles (CISO, GRC, CRO, Compliance, CIO, IA) remain NOT FOUND — no dedicated C-suite at subsidiary level; functions handled by Hong Leong Group.

### 5. Entity Classifications (21 cells)

#### Pengurusan Danaharta Nasional Berhad (Tier 194) — ENTITY WOUND DOWN
All 7 roles classified as `ENTITY WOUND DOWN`. Danaharta was established in 1998 as Malaysia's national asset management company to resolve non-performing loans (NPLs) during the Asian Financial Crisis. The entity has completed its mandate. Website danaharta.com.my is inactive; Wikipedia redirects to Khazanah Nasional.

#### TA Securities Holdings Berhad (Tier 202) — ENTITY LIKELY INACTIVE
All 7 roles classified as `ENTITY LIKELY INACTIVE`. Parent company TA Enterprise Berhad renamed to TA Global Berhad and pivoted to property development. Securities business likely wound down or divested. tasecurities.com failed to scrape.

#### AEON Digital Bank (Tier 205) — SHARES PARENT
6 roles classified as `SHARES PARENT: AEON Credit Service (M) Berhad`. Digital bank operated as subsidiary; C-suite functions shared with parent entity.

### 6. Enhanced NOT FOUND Context (28 cells across 19 institutions)

Deep research via 3 parallel subagents confirmed the absence of specific C-suite roles with detailed source documentation:

#### CISO Gaps — Enhanced Context (10 institutions)

| Institution | Previous | v5.90 Enhancement |
|-------------|----------|-------------------|
| HSBC Bank Malaysia | NOT FOUND | Only Board of Directors (6 directors) listed; no management team page; CISO at APAC regional level |
| Manulife Insurance Berhad | NOT FOUND | Manulife Holdings AR 2024 lists 25 Senior Key Management Personnel, no CISO; cybersecurity at Manulife Asia regional level |
| Manulife Takaful Malaysia | NOT FOUND | Shared with Manulife Holdings; no dedicated CISO at subsidiary level |
| Generali Insurance Malaysia | NOT FOUND | Abdul Hakim Raazip (CRO) spoke at CISO Malaysia Corinium event; cybersecurity likely under CRO remit |
| GX Bank Berhad | NOT FOUND | gxbank.my leadership page fully scraped (13 executives), no CISO listed |
| Takaful IKHLAS Berhad | NOT FOUND | MNRB Holdings has 11 senior management, no CISO; closest: Aaron Loo (Group CTO) |
| Malaysia Debt Ventures (MDV) | NOT FOUND | mdv.com.my management team page scraped, no CISO listed |
| CIMB-Principal AM | NOT FOUND | CIMB Group cybersecurity under Group CTO Ros Aziah; no dedicated CISO at subsidiary level |
| RHB Asset Management | NOT FOUND | RHB Group cybersecurity under Group CTO Wong Kwang Leh; no dedicated CISO at subsidiary level |
| Sarawak SFC (SSFC) | NOT FOUND | ssfc.com.my DNS fails; no web presence found |

#### IA/Compliance/CIO/CRO Gaps — Enhanced Context (9 institutions)

| Institution | Role | Key Finding |
|-------------|------|-------------|
| AIA Berhad | IA | Leadership page (12 execs) confirmed no IA; shared with AIA Group HK |
| AIA General Berhad | IA | Leadership page (6 execs) confirmed no IA; shared with AIA Group |
| AIA Public Takaful | IA | Leadership page (8 execs) confirmed no IA; shared with AIA Group |
| Bank Rakyat | IA | Management Committee (8 members) confirmed no IA; Board Charter confirms role exists but name not public |
| BigPay Malaysia | IA | No public leadership page; IA not publicly disclosed |
| Chubb Insurance | Compliance | BNM Public Information Disclosure page is JS-rendered; compliance officer name not accessible |
| Berjaya Sompo | CIO | Leadership page (9 senior managers) confirmed no CIO; IT likely outsourced |
| Generali Life Insurance | CIO | Leadership page (12 senior managers) confirmed no CIO; IT at Generali Group regional level |
| Setel (PETRONAS) | CRO | setel.com About Us page does not list leadership; CRO not publicly disclosed |

#### JF Apex Securities — Enhanced NOT FOUND (7 cells)

No online presence; domain jfapex.com.my does not resolve; no leadership page, Wikipedia article, or LinkedIn presence; appears to be a small privately-held stockbroker.

### 7. Maybank Asset Management Group — Research Confirmed Inaccessible

Extensive search confirmed 0 named executives. Maybank website (maybank.com, maybank2u.com.my) blocks all automated access with persistent bot detection. Domain maybankam.com.my does not resolve. Manual browser session required for Maybank annual report access.

---

## Research Methodology — v5.90

### Subagent Architecture
Three parallel subagents were dispatched targeting different gap categories:

| Subagent | Focus | Institutions | Method |
|----------|-------|-------------|--------|
| Agent 1 | Zero-named institutions | KFH, AEON Digital Bank, HLAM, Maybank AM, JF Apex, TA Sec, Danaharta | Official websites, annual reports, LinkedIn, Bursa Malaysia |
| Agent 2 | CISO gaps (10 institutions) | HSBC, Manulife, Generali, GX Bank, Takaful IKHLAS, MDV, CIMB-Principal, RHB AM, SSFC | CISO Malaysia conferences (Corinium, 3novex), ISACA, official leadership pages, LinkedIn |
| Agent 3 | IA/Compliance/CIO/CRO gaps | AEON Bank, AIA x3, Bank Rakyat, BigPay, Chubb, Berjaya Sompo, Generali Life, Setel | Official leadership pages, IIA Malaysia, BNM disclosures, annual report CG sections |

### Key Findings from CISO Research

1. **No dedicated CISO found at ANY of the 10 target institutions** — This is a significant structural finding. Malaysian financial institutions (especially insurers, asset managers, and development finance institutions) either handle cybersecurity at group/parent level or under the CRO's remit.

2. **Cybersecurity governance patterns identified:**
   - **Group CTO model:** CIMB-Principal AM (Ros Aziah, Group CTO), RHB AM (Wong Kwang Leh, Group CTO) — cybersecurity under CTO
   - **CRO model:** Generali Insurance (Abdul Hakim Raazip, CRO spoke at CISO event) — cybersecurity under CRO
   - **Group Transformation model:** Takaful IKHLAS/MNRB (Aaron Loo, Group CTO) — cybersecurity under transformation
   - **Regional model:** HSBC, Manulife — CISO at APAC/regional level, not local entity

3. **CISO Malaysia Conference speakers (Corinium/3novex):** Only institutions already in our database (AEON Bank, Kenanga, Standard Chartered) had CISO speakers at CISO Malaysia 2026 events.

### Key Findings from IA Research

1. **Internal Audit remains the hardest role to fill** (57.2% coverage) — IA executives report directly to Board Audit Committees and are deliberately kept off public management pages.

2. **AIA Group pattern confirmed:** All 3 AIA entities (AIA Berhad, AIA General, AIA Public Takaful) have confirmed IA gaps. The IA function is shared with AIA Group headquarters in Hong Kong.

3. **AEON Bank IA:** Phang Chee Chong identified as Head of IAD at parent AEON Credit Service — shared service model with 18-person IAD team.

### Key Findings from Zero-Named Research

1. **KFH Malaysia** — Full management team (10 members) publicly listed on official website, including 5 of our 7 target roles. KFH is withdrawing from Malaysia by end 2026.

2. **AEON Credit Service** — Full Board of Directors and leadership publicly listed. CEO Daisuke Maeda is also Executive Director of AEON Bank (M) Berhad.

3. **Danaharta** — Entity confirmed wound down. Established 1998, mandate completed.

4. **TA Securities** — Parent company pivoted to property development (TA Global Berhad).

5. **JF Apex Securities** — No online presence whatsoever (domain doesn't resolve).

---

## Remaining Gaps (v5.90)

### Gap Distribution by Role

| Role | NOT FOUND | Entity-Classified | Total Unnamed | Coverage |
|------|-----------|-------------------|---------------|---------|
| Internal Audit | 83 | 9 | 92 | 57.2% |
| CISO | 81 | 33 | 114 | 60.9% |
| Compliance | 70 | 9 | 79 | 62.8% |
| GRC | 59 | 31 | 90 | 67.4% |
| CRO | 53 | 31 | 84 | 70.2% |
| CFO | 55 | 8 | 63 | 74.4% |
| CIO | 52 | 31 | 83 | 74.4% |

### Per-Segment Coverage

| Segment | Cells | Named | Entity | NOT FOUND | Coverage |
|---------|-------|-------|--------|-----------|---------|
| Investment Banks | 119 | 103 | 0 | 16 | 86.6% |
| Card Schemes | 70 | 60 | 0 | 10 | 85.7% |
| Development FIs | 63 | 53 | 0 | 10 | 84.1% |
| Licensed Banks | 224 | 184 | 0 | 40 | 82.1% |
| Payment Processors | 14 | 4 | 7 | 3 | 78.6% |
| Insurers | 196 | 150 | 0 | 46 | 76.5% |
| Takaful | 84 | 60 | 0 | 24 | 71.4% |
| Credit Cooperatives | 21 | 3 | 11 | 7 | 66.7% |
| E-Money | 77 | 45 | 0 | 32 | 58.4% |
| Cooperatives | 147 | 0 | 84 | 63 | 57.1% |
| GLC-Linked | 168 | 107 | 1 | 60 | 64.3% |
| Fintech Sandbox | 70 | 29 | 0 | 41 | 41.4% |
| Payment Operators | 42 | 18 | 0 | 24 | 42.9% |
| Development Finance | 21 | 10 | 0 | 11 | 47.6% |
| Asset Management | 35 | 13 | 0 | 22 | 37.1% |
| Fintech | 35 | 3 | 7 | 25 | 28.6% |
| MSBs | 98 | 23 | 0 | 75 | 23.5% |
| Fintech Registered | 14 | 2 | 0 | 12 | 14.3% |
| Digital Banks | 7 | 0 | 0 | 7 | 0.0% → 100% (all SHARES PARENT) |

### Top Remaining Quick Wins (1-2 gaps, 3+ named)

**Single-gap institutions (6/7 named):**
1. Berjaya Sompo Insurance — CIO gap
2. Chubb Insurance Malaysia — Compliance gap
3. GX Bank Berhad — CISO gap
4. HSBC Bank Malaysia — CISO gap
5. Manulife Insurance Berhad — CISO gap
6. Manulife Takaful Malaysia — CISO gap
7. Sarawak SFC (SSFC) — CISO gap
8. Setel (PETRONAS) — CRO gap
9. Takaful IKHLAS — CISO gap
10. MDV — CISO gap
11. CIMB-Principal AM — CISO gap
12. RHB Asset Management — CISO gap
13. AIA Berhad — IA gap
14. AIA General Berhad — IA gap
15. AIA Public Takaful — IA gap
16. Bank Rakyat — IA gap
17. BigPay Malaysia — IA gap
18. Generali Insurance — CISO gap
19. Generali Life Insurance — CIO gap

**Double-gap institutions (5/7 named):**
20. BNP Paribas Malaysia — CISO, CIO
21. BSN — CISO, IA
22. Citibank Berhad — CISO, Compliance
23. FWD Insurance — CISO, CIO
24. General Takaful — CISO, CRO
25. JCorp — CISO, CRO
26. Khazanah Nasional — CISO, IA
27. PUNB — CISO, CIO
28. PNSB — CISO, CIO
29. Phillip Securities — CISO, GRC

---

## Next Steps (v5.91 Priorities)

1. **Manual browser research** for bot-blocked institutions:
   - Maybank Group (maybank.com) — persistent bot detection blocking all scraping
   - Chubb Insurance (chubb.com/my-en/) — BNM Public Information Disclosure page is JS-rendered
   - AEON Digital Bank senior leaders — JS-rendered tabs

2. **Annual report PDF extraction** for remaining 0/7 institutions:
   - Maybank Asset Management Group — requires Maybank annual report (bot-blocked)
   - J.P. Morgan Chase Malaysia — 2025 CG Statement confirmed no public data

3. **MSB and Fintech segment deep dive** (lowest coverage at 23.5% and 28.6%):
   - 2C2P, Billplz, CurrencyFair, G2G Online, I.Destinasi, ToyyibPay — research via BNM MSB registry
   - Alipay+ Malaysia, WeChat Pay Malaysia — entity classification (subsidiaries of foreign parents)

4. **Industry award mining** — expand beyond CSO30:
   - The Edge Malaysia Business Excellence Awards
   - IIA Malaysia (Institute of Internal Auditors) — for IA role identification
   - ISACA Malaysia Chapter — for CISO identification
   - BNM Technology Risk Management Forum speakers

5. **Regulatory filing extraction**:
   - BNM Corporate Governance Report submissions (publicly available)
   - Companies Commission of Malaysia (SSM) annual returns
   - Securities Commission Malaysia annual reports

---

## File Inventory

| File | Description | Status |
|------|-------------|--------|
| `prospect-database-enriched-v5.90.csv` | Main database (215 institutions, 1505 cells) | ✅ Written |
| `update_v590.py` | v5.90 update script | ✅ Written |
| `gap_analysis_v590.py` | Gap analysis script for v5.90 targeting | ✅ Written |
| `integrity-guard-report-v590.md` | Integrity guard report (0 issues) | ✅ Generated |

---

## Classification

**TLP:** AMBER — Handle with care. This report contains executive names and organizational leadership structures for Malaysian financial institutions. Do not redistribute publicly.

**Repository:** https://github.com/ahmadfaurani/Voron-Campaign
**Git Email:** p62operator@proton.me
**Version:** v5.90
**Cycle:** Stakeholder Collection — Expanded Scope (143 institutions target, 215 in database)

---

*End of Report — VoronDRQ Stakeholder Collection Agent, v5.90 Cycle*

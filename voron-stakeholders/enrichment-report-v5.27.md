# VoronDRQ Stakeholder Enrichment Report — v5.27

**Generated:** 2026-07-22 04:00 MYT (UTC+8)
**Database:** prospect-database-enriched-v5.27.csv
**Previous:** v5.26 (835/1435 filled, 58.2%)
**Current:** v5.27 (836/1435 filled, 58.3%)
**Delta:** +1 new fill, +1 correction, +8 source evidence upgrades

---

## Executive Summary

Cycle v5.27 focused on annual report extraction and source evidence strengthening for high-value institutions. The primary breakthrough was extracting the **Manulife Holdings Berhad Annual Report 2023** PDF, which revealed the complete senior management team across 3 subsidiaries — yielding a new Head of Internal Audit fill and upgrading multiple confidence levels. Additionally, the **HL Capital AR 2025** was extracted to correct the HLIB CFO entry from group-level to entity-specific. Five NOT FOUND CISO entries were strengthened with official source evidence, raising confidence from 25-35% to 90-95%.

---

## Metrics

| Metric | v5.26 | v5.27 | Delta |
|--------|-------|-------|-------|
| Total Institutions | 205 | 205 | 0 |
| Total Cells | 1,435 | 1,435 | 0 |
| Filled | 835 (58.2%) | 836 (58.3%) | +1 |
| NOT FOUND | 600 (41.8%) | 599 (41.7%) | -1 |
| Avg Confidence (filled) | — | Improved | ↑ |

---

## Changes Applied (10 total, 5 institutions)

### 1. NEW FILL — Manulife Insurance Berhad, Head of Internal Audit
- **Name:** Krishna Rajaa Ramalingam
- **Title:** Head of Internal Audit (Audit Services – Malaysia)
- **Source:** Manulife Holdings Berhad AR 2023 (official PDF, manulife.com.my)
- **Confidence:** 90%
- **Previous:** NOT FOUND
- **Impact:** +1 fill, -1 NOT FOUND

### 2. CORRECTION — Hong Leong Investment Bank Berhad, CFO
- **Old:** Malkit Singh (CFO) [Group-level: Hong Leong Bank]
- **New:** San Kah Yee (Chief Financial Officer, HLIB)
- **Source:** HL Capital AR 2025 Key Senior Management (7 members listed)
- **Confidence:** 95% (official annual report, entity-specific)
- **Rationale:** AR 2025 confirms San Kah Yee as HLIB-specific CFO. Malkit Singh is the HL Bank Group CFO, not HLIB-specific.

### 3. SOURCE UPDATE — HLIB, CISO
- **Previous:** NOT FOUND [AR 2024, 8 people] conf 25
- **Updated:** NOT FOUND [AR 2025 Key Senior Management: 7 members (Lee Jim Leng CEO, San Kah Yee CFO, Chong Poh Choon, Ling Yuen Cheng, Phang Siew Loong, Tan Jie Khien, Chue Kwok Yan). No CISO.] conf 95
- **Source:** hlib.com.my/Files/AnnualReports/HL_Capital_AR2025.pdf

### 4. SOURCE UPDATE — MIDF Amanah, CISO
- **Previous:** NOT FOUND [key-management page, CEO only named] conf 35
- **Updated:** NOT FOUND [6 Management Committee members listed: Azizi Mustafa (CEO), Meor Ibrahim Othman (Compliance), Zanariah Daud (Control Assurance), Sheikh Shahruddin (Bank Ops), Vasuthevan Gopalakrishnan (HR), Nor Azita Sarip (Legal). No CISO.] conf 95
- **Source:** midf.com.my/key-management

### 5. SOURCE UPDATE — Generali Insurance Malaysia, CISO
- **Previous:** NOT FOUND [no leadership page, JS SPA, LinkedIn requires login] conf 25
- **Updated:** NOT FOUND [10 General Insurance SMT members listed on official leadership page + AR 2024 control function hierarchy lists 12 roles (CEO, CTO, CIO=Chief Insurance Officer, CPO, COS, CMO, GC, Head of Control Function, CIA, CCO, CRO, AA) — no CISO in either] conf 95
- **Sources:** generali.com.my/about-generali/leadership + Generali AR 2024 (Note 18b, p.91)

### 6. SOURCE UPDATE — Generali Life Insurance, CISO
- **Previous:** NOT FOUND [no CISO listed] conf 25
- **Updated:** NOT FOUND [12 Life Insurance SMT members listed: Tony Lin CFO, May Chan COO, Steven Tong, Irene Gan, Vincent Fong CRO, Grace Yew, Alex Chin (Chief Investment Officer), Lee Jo Wen, Teoh Seng Hong, Aw Teck Yee (Compliance), George Tan (IA), Tan Jian Wei. No CISO.] conf 90
- **Source:** generali.com.my/about-generali/leadership

### 7. SOURCE UPDATE — Generali Life Insurance, CIO
- **Previous:** NOT FOUND [no CIO/CTO listed] conf 25
- **Updated:** NOT FOUND [12 Life Insurance SMT members. Alex Chin is "Chief Investment Officer" (investment role, not IT). No Chief Information Officer or CTO listed.] conf 90
- **Source:** generali.com.my/about-generali/leadership

### 8. SOURCE UPDATE — Manulife Insurance Berhad, CISO
- **Previous:** NOT FOUND [board page only, no senior management] conf 25
- **Updated:** NOT FOUND [AR 2023 lists 11 MIB senior managers: Vibha Hamsi Coburn (CEO), Ng Chun Nam (CFO), Alex Tan (CAO), Marilyn Wang (CMO), Lee Tat Fatt (COO), Bernard Sia (CIO), Ricky Lim (CPO), Jonathan Yen (CCO), Senthil Woon (Compliance), Siti Nur Rasyida Rosely (CRM), Alston Go (Actuary). No CISO.] conf 95
- **Source:** manulife.com.my AR 2023 PDF

### 9. SOURCE UPDATE — Manulife Insurance Berhad, GRC
- **Previous:** NOT FOUND [corporate governance page, no GRC role] conf 25
- **Updated:** NOT FOUND [AR 2023 lists 11 MIB senior managers. Risk function headed by Siti Nur Rasyida Rosely (Chief Risk Management); Compliance by Senthil Woon. No dedicated GRC role.] conf 90
- **Source:** manulife.com.my AR 2023 PDF

### 10. CONFIDENCE UPGRADE — Manulife Insurance Berhad, Compliance
- **Previous:** Senthil Woon (Chief Compliance Officer) [RocketReach, conf 50]
- **Updated:** Senthil Woon Wai Keong (Chief Compliance Officer) [Official: Manulife AR 2023, conf 90]
- **Change:** Full name confirmed + confidence upgraded from 50 to 90 via official AR 2023

---

## Key Discoveries

### Manulife Holdings Berhad AR 2023 — Full Senior Management Extracted
The AR 2023 PDF (30 pages parsed) revealed complete senior management for 3 subsidiaries:

**Manulife Insurance Berhad (11 senior managers):**
- Vibha Hamsi Coburn — Group CEO/Executive Director
- Ng Chun Nam — Chief Financial Officer
- Alex Tan Cheng Leong — Chief Agency Officer
- Marilyn Wang — Chief Marketing Officer
- Lee Tat Fatt — Chief Operations Officer
- Bernard Sia — Chief Information Officer
- Ricky Lim Soon Joo — Chief Product Officer
- Jonathan Yen — Chief Commercial Officer
- Senthil Woon Wai Keong — Chief Compliance Officer
- Siti Nur Rasyida Rosely — Chief Risk Management
- Alston Go Xue Ji — Appointed Actuary

**Manulife Investment Management (M) Berhad (12 senior managers):**
- Jason Chong Soon Min — CEO & Executive Director
- Kenneth Kwong Chor Wah — Head of Finance
- + 10 other heads of functions

**Head of Internal Audit (group-level):**
- Krishna Rajaa Ramalingam — Head of Internal Audit (Audit Services – Malaysia)

**Note:** AR 2024 PDF not yet available on manulife.com.my (49th AGM 2025 URL returned 404). AR 2023 is the latest available.

### HL Capital AR 2025 — HLIB CFO Correction
The AR 2025 Key Senior Management confirms 7 members, including San Kah Yee as CFO (entity-specific for HLIB, not group-level Malkit Singh).

### Generali AR 2024 — Control Function Hierarchy
The AR 2024 (Note 18b, p.91) lists the full control function hierarchy: CEO, CTO (Chief Transformation Officer), CIO (Chief Insurance Officer), CPO, COS, CMO, GC, Head of Control Function, CIA, CCO, CRO, AA. **No CISO** in the control function list — confirming CISO is not a designated control function role at Generali Malaysia.

---

## Segment Coverage (v5.27)

| Segment | Institutions | NOT FOUND | Fill Rate |
|---------|-------------|-----------|-----------|
| Investment Banks | 15 | 7/105 (7%) | 93% |
| Card Schemes | 10 | 10/70 (14%) | 86% |
| Licensed Banks | 29 | 33/203 (16%) | 84% |
| Development FIs | 11 | 20/77 (26%) | 74% |
| Insurers | 26 | 48/182 (26%) | 74% |
| Takaful | 12 | 30/84 (36%) | 64% |
| GLC-Linked | 24 | 64/168 (38%) | 62% |
| E-Money | 19 | 63/133 (47%) | 53% |
| Payment Operators | 6 | 24/42 (57%) | 43% |
| Fintech Sandbox | 13 | 52/91 (57%) | 43% |
| MSBs | 17 | 89/119 (75%) | 25% |
| Fintech Registered | 2 | 13/14 (93%) | 7% |
| Cooperatives | 21 | 147/147 (100%) | 0% |

---

## Search Engine Notes

- **Firecrawl search** continues to return irrelevant results for Malaysian financial institution CISO queries (IoT articles, dictionary definitions, WhatsApp)
- **web_search** also returned irrelevant results (WhatsApp, unrelated sites)
- **Direct URL extraction** remains the most reliable method — annual report PDFs and official leadership pages
- **BSN website** (bsn.com.my) has changed URL structure; old /EN/AboutUs/Pages/ URLs return 404; site map returned no links (JS SPA)
- **Manulife AR 2024** not yet published on website (URL pattern returned 404)

---

## Next Steps

1. **Locate Manulife AR 2024** — check Bursa Malaysia filings for the latest annual report
2. **BSN leadership page** — try browser-based extraction (JS SPA) or BSN annual report PDF
3. **Continue single-gap institutions** — focus on remaining CISO gaps at: Citibank Berhad, AIA Berhad, Great Eastern, Maybank IB, BSN
4. **Manulife Investment Management** — the AR 2023 data for MIMMB (12 senior managers) could fill additional gaps if MIMMB is in the database
5. **Remaining 599 NOT FOUND** — prioritize by segment fill rate (Cooperatives 100%, Fintech Registered 93%, MSBs 75%)

---

## File Inventory

| File | Status |
|------|--------|
| prospect-database-enriched-v5.27.csv | ✅ Created (224KB, 206 lines) |
| prospect-database-enriched-v5.26.csv | Previous version (preserved) |
| enrichment-report-v5.27.md | ✅ This file |

---

*TLP:AMBER — Handle with care, do not redistribute publicly.*
*Classification: VoronDRQ Campaign Intelligence*
*GitHub: https://github.com/ahmadfaurani/Voron-Campaign*

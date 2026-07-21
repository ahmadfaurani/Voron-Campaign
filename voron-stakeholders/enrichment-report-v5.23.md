# VoronDRQ Stakeholder Collection — Enrichment Report v5.23

**Generated:** 2026-07-21 12:00 +08  
**Report Date:** 2026-07-21  
**Brief ID:** VORON-ENRICH-V5.23-20260721-1200  
**TLP:AMBER** — Handle with care, do not redistribute publicly.  
**Database:** prospect-database-enriched-v5.23.csv  
**Previous Version:** v5.22  

---

## Executive Summary

This enrichment cycle (v5.23) focused on extracting executive leadership data from secondary sources (TheOrg crowd-sourced org charts, RocketReach) for fintech and e-money institutions with significant role gaps. The primary achievement was filling **6 new cells** across both BigPay database entries, bringing BigPay from 1/7 to 4/7 roles filled.

**Key achievements this cycle:**
- Filled **3 new executive roles** for **BigPay (Capital A)** (T4, E-Money): CISO, CIO, Compliance
- Filled **3 new executive roles** for **BigPay Malaysia Sdn Bhd** (T3, MSBs): CISO, CIO, Compliance
- Updated **2 CFO entries** from parent-level (Capital A CFO Mun Hui Teh) to BigPay-specific CFO (Nicholas Chua)
- Enhanced **6 NOT FOUND notes** (CRO, IA, GRC × 2 BigPay entries) with TheOrg research findings
- Confirmed **iPay88 CISO** (Alex Wah, already in database from v5.22) via RocketReach verification
- Researched but confirmed NOT FOUND: HSBC Amanah Takaful (board-only disclosure), Billplz (no C-suite beyond CEO), PayNet (anti-bot blocked), Allianz Malaysia (URL 404)
- **0 new NOT FOUND** entries — all researched institutions documented

---

## Database Statistics

### Overall Coverage

| Metric | Value |
|--------|-------|
| Total Institutions | 205 |
| Total Stakeholder Cells | 1,435 (205 × 7 roles) |
| Filled (Named Executives) | 832 (58.0%) |
| NOT FOUND (Researched, Not Disclosed) | 603 (42.0%) |
| Empty (Not Yet Researched) | 0 (0.0%) |
| Research Coverage | 100.0% |

### Coverage Trend

| Version | Date | Filled | NOT FOUND | Coverage |
|---------|------|--------|-----------|----------|
| v5.21 | 2026-07-20 | 824 | 611 | 57.4% |
| v5.22 | 2026-07-21 | 826 | 609 | 57.6% |
| **v5.23** | **2026-07-21** | **832** | **603** | **58.0%** |

**Net change:** +6 filled, -6 NOT FOUND

---

## Updates Applied in v5.23

### 1. BigPay (Capital A) — 3 New Fills + CFO Update ✅

**Tier:** T4 | **Segment:** E-Money | **Parent:** Capital A Berhad (formerly AirAsia)

**Source:** TheOrg crowd-sourced org chart — https://theorg.com/org/bigpay/teams/leadership-team  
**Confidence:** 65 (secondary source, TheOrg "Unverified" tag)

#### New Roles Filled:

| Role | Name | Title | Conf | Source |
|------|------|-------|------|--------|
| **CISO** | Angus Thorn | Group Chief Information Security Officer | 65 | TheOrg Leadership Team |
| **CIO** | Siddharth (Sid) R. | Group Chief Technology Officer | 65 | TheOrg Leadership Team |
| **Compliance** | Divya Das | Head Of Compliance (CAMS, ICA RC Dip) | 65 | TheOrg Finance & Compliance Team |

#### CFO Updated:

| Role | Previous | New |
|------|----------|-----|
| **CFO** | Mun Hui Teh (Capital A parent CFO, conf 80) | Nicholas Chua (BigPay-specific CFO, conf 65, TheOrg) |

**Note:** The previous CFO entry was inherited from Capital A parent (Mun Hui Teh, capitala.com). TheOrg confirms BigPay has its own dedicated CFO (Nicholas Chua), which is more precise for the institution-level target.

#### Remaining NOT FOUND (Enhanced Notes):

| Role | Status | Research Finding |
|------|--------|-----------------|
| **CRO** | NOT FOUND | TheOrg lists Ryan Vinoth as "Head of Credit Risk" — credit risk subset, not enterprise CRO. Capital A parent-level risk function may apply. |
| **IA** | NOT FOUND | TheOrg org chart (6 teams, 49 people) lists no IA function. IA may be handled at Capital A group level. |
| **GRC** | NOT FOUND | GRC function likely split between Compliance (Divya Das) and Risk at Capital A group level. |

**Impact:** BigPay (Capital A) now has 4 of 7 roles filled (CISO, CFO, CIO, Compliance). 3 remain NOT FOUND.

---

### 2. BigPay Malaysia Sdn Bhd — 3 New Fills + CFO Update ✅

**Tier:** T3 | **Segment:** MSBs | **Note:** Same entity as BigPay (Capital A) — duplicate database entry for the BNM-licensed MSB entity.

Same updates applied as BigPay (Capital A):
- CISO: Angus Thorn (Group CISO, conf 65)
- CFO: Nicholas Chua (BigPay CFO, conf 65) — replacing parent CFO Mun Hui Teh
- CIO: Siddharth (Sid) R. (Group CTO, conf 65)
- Compliance: Divya Das (Head of Compliance, conf 65)

**Impact:** BigPay Malaysia Sdn Bhd now has 4 of 7 roles filled. 3 remain NOT FOUND (CRO, IA, GRC).

---

## Institutions Researched (No New Fills — Confirmed NOT FOUND)

### HSBC Amanah Takaful (Malaysia) Berhad

**Source:** https://www.hsbcamanah.com.my/amanah-and-you/board-of-directors/  
**Status:** Official website lists only Board of Directors (5 members). No executive C-suite (CISO, CIO, IA) publicly disclosed.

**Confirmed Board of Directors (5 members):**
- Chairperson: Datin Che Teh Ija Binti Mohd Jalil (Independent Non-Executive, appointed 1 Jan 2022)
- Executive Director: Dato' Omar Siddiq Bin Amin Noer Rashid (also CEO/Head of Banking, HSBC Bank Malaysia Berhad)
- Senior Independent Director: Lim Tiang Siew (Chairman of Risk Committee; former Group Chief Internal Auditor of CIMB Group, retired March 2018)
- Independent Director: Datuk Md Arif Bin Mahmood (Chairman of Nominations & Remuneration; former EVP & CEO Downstream, PETRONAS)
- Independent Director: Ng Ing Peng (Chairperson of Audit Committee)

**Conclusion:** HSBC Amanah Takaful's 5 target roles (CISO, GRC, CRO, CIO, IA) remain NOT FOUND. The company does not publicly disclose executive management — only board-level governance. Lim Tiang Siew (board director) has IA background but serves as director, not executive Chief Audit Executive. TheOfficialBoard.com lists 8 executives including "Raja Amir Azwa" but this data is paywalled and unverified.

---

### Billplz Sdn Bhd

**Source:** TheOrg — https://theorg.com/org/billplz  
**Status:** TheOrg lists 14 people at Billplz HQ (Shah Alam). Only CEO (Nazroof Hakim) and Compliance Manager (Vinod Varma) are listed. No CFO, CISO, CRO, CIO, IA, or GRC roles publicly disclosed.

**Confirmed Billplz personnel (TheOrg):**
- CEO: Nazroof Hakim
- Compliance Manager: Vinod Varma (too junior for "Head of Compliance" — manager level, not head)
- Accounting AVP: Nimalajothy Tamby (finance, not CFO)
- Technology Advisor: Arzumy MD
- Independent Non-Executive Director: Azril Azmi

**Conclusion:** Billplz's 7 target roles remain NOT FOUND. As an 11-50 employee startup, C-suite roles beyond CEO are not publicly disclosed. Compliance function exists at manager level (Vinod Varma) but not at Head/Chief level.

---

### PayNet (Payments Network Malaysia Sdn Bhd)

**Source:** https://www.paynet.my/about-us.html  
**Status:** PayNet website blocked automated scraping (anti-bot protection). The about-us page contains only company history/timeline, no leadership section. DuitNow, FPX, and JomPAY (PayNet subsidiaries) all inherit this limitation.

**Conclusion:** PayNet's 4 target roles (GRC, CRO, Compliance, IA) for DuitNow, FPX, and JomPAY remain NOT FOUND. The national payments network operator does not publicly disclose executive management on its website.

---

### Allianz Malaysia (3 Entities)

**Source:** Attempted https://www.allianz.com.my/en/about-allianz/management-team.html (404)  
**Status:** Allianz Malaysia website returned 404 for management team page. Site map returned no leadership/management URLs. Allianz General, Allianz Life, and Allianz Takaful entities all at 4 NOT FOUND roles each (CISO, GRC, CRO, Compliance).

**Conclusion:** Allianz Malaysia's 12 target roles (4 × 3 entities) remain NOT FOUND. Previous research (IAR 2024) confirmed CISO not in 16-member Senior Management Team. Allianz Group may centralize cybersecurity at regional level.

---

## Sources Used This Cycle

### Primary Sources (New Fills)

1. **TheOrg** (crowd-sourced org charts):
   - https://theorg.com/org/bigpay/teams/leadership-team (4 people: CISO, CFO, CTO, CGCO)
   - https://theorg.com/org/bigpay/teams/finance-and-compliance-team (13 people: Head of Compliance, Head of Credit Risk, finance team)
   - https://theorg.com/org/bigpay/teams/engineering-and-development-team (10 people: Cyber Security Engineer, Head of Mobile Engineering)
   - https://theorg.com/org/bigpay/teams/operations-team (6 people)
   - https://theorg.com/org/billplz (14 people at HQ)
   - https://theorg.com/org/billplz/offices/hq

2. **RocketReach** (executive database):
   - https://rocketreach.co/ipay88-management_b5e52ecdf42e67ac (iPay88 management team — confirmed Alex Wah as Head of IT Cum CISO)
   - https://rocketreach.co/alex-wah-email_52486791 (Alex Wah profile — Cyberjaya, MY, MBA Universiti Utara Malaysia)

### Secondary Sources (Research Only, No Fills)

3. **Official corporate websites**:
   - https://www.hsbcamanah.com.my/amanah-and-you/board-of-directors/ (HSBC Amanah board — 5 directors)
   - https://www.paynet.my/about-us.html (PayNet — company story only, no leadership)
   - https://www.allianz.com.my/en/about-allianz/management-team.html (404)

4. **TheOfficialBoard** (paywalled):
   - https://www.theofficialboard.com/org-chart/hsbc-amanah-malaysia-2 (8 executives listed but details paywalled)

5. **CB Insights** (paywalled):
   - https://www.cbinsights.com/company/ipay88/people (9 executives, 8 paywalled)

---

## Confidence Scoring

| Score | Meaning | Example |
|-------|---------|---------|
| 95 | Official source, current, directly named on leadership page | Generali Malaysia (official website) |
| 90 | Official source, slightly indirect (annual report, CG statement) | Maybank (annual report) |
| 85 | Official source with minor inference (combined role, acting position) | Boost Bank CISO (LinkedIn + official) |
| 80 | Official source, parent-level (inherited to subsidiary) | BigPay CFO previous (Capital A parent) |
| 70 | LinkedIn/secondary source, well-corroborated | iPay88 CISO (RocketReach) |
| 65 | TheOrg crowd-sourced org chart, "Unverified" tag | BigPay CISO/CFO/CIO/Compliance (this cycle) |
| 60 | LinkedIn only, single source | — |
| 35-40 | Researched, NOT FOUND — institution does not publicly disclose | All NOT FOUND entries |
| 0 | Not yet researched | — |

---

## Priority Institutions for Next Cycle

### High-Priority Gaps (6 missing roles, Tier 1-2 institutions)

| Institution | Tier | Segment | Missing | Challenge |
|-------------|------|---------|---------|-----------|
| J.P. Morgan Chase Bank Malaysia | T1 | Licensed Banks | 6 | Non-disclosure policy |
| ICBC (Malaysia) Berhad | T1 | Licensed Banks | 6 | Only board directors disclosed |
| Mizuho Bank (Malaysia) Berhad | T1 | Licensed Banks | 6 | Only board directors disclosed |
| Zurich Life Insurance Malaysia | T2 | Insurers | 6 | Only CEOs/board disclosed |
| Zurich Takaful Malaysia | T2 | Takaful | 6 | Only CEOs/board disclosed |
| Prudential BSN Takaful | T2 | Takaful | 6 | CRO/Compliance name undisclosed |
| KAF Digital Bank | T6 | Fintech Sandbox | 6 | Leadership transition |

### Medium-Priority Gaps (5-6 missing roles, now reduced)

| Institution | Tier | Segment | Missing | Note |
|-------------|------|---------|---------|------|
| ~~BigPay (Capital A)~~ | T4 | E-Money | ~~6~~ → **3** | **Improved this cycle: 4/7 filled** |
| ~~BigPay Malaysia Sdn Bhd~~ | T3 | MSBs | ~~6~~ → **3** | **Improved this cycle: 4/7 filled** |
| HSBC Amanah Takaful Malaysia | T2 | Takaful | 5 | Board-only disclosure |
| iPay88 (M) Sdn Bhd | T6 | Fintech Registered | 6 | CISO filled, rest not disclosed |
| iPay88 (Malaysia) Sdn Bhd | T3 | MSBs | 6 | Same entity, CISO filled |
| Billplz Sdn Bhd | T3 | MSBs | 7 | Startup, no C-suite public |
| ToyyibPay Sdn Bhd | T3 | MSBs | 7 | No public leadership data |
| SenangPay Sdn Bhd | T3 | MSBs | 6 | No public leadership data |
| Money Match Sdn Bhd | T3 | MSBs | 6 | No public leadership data |
| Wallex Sdn Bhd | T3 | MSBs | 6 | No public leadership data |
| Xendit Technologies Malaysia | T3 | MSBs | 6 | No public leadership data |
| GrabPay (Grab Malaysia) | T4 | E-Money | 5 | Grab HQ Singapore, no MY execs |
| ShopeePay Malaysia | T4 | E-Money | 5 | Sea Group, no MY-specific execs |
| Razer Pay Malaysia | T4 | E-Money | 6/7 | No public leadership data |

---

## Next Steps

1. **TheOrg expansion pass** — Search TheOrg for more Malaysian fintech/MSB institutions (ToyyibPay, Money Match, SenangPay, Wallex, Xendit, GrabPay, ShopeePay). TheOrg crowd-sourced org charts yielded 6 fills for BigPay this cycle — replicable for other fintechs.
2. **LinkedIn enrichment pass** — Search for named executives at Tier 1-2 institutions with NOT FOUND status (Zurich, PruBSN, ICBC, Mizuho, JPM, HSBC Amanah Takaful). Focus on CISO and CRO roles.
3. **Annual report deep-dive** — Extract executive names from FY2025 annual reports for insurers and takaful operators (Allianz, Zurich, PruBSN, HSBC Amanah Takaful).
4. **PayNet deep-dive** — Try alternative approaches for PayNet leadership (BNM annual report, industry directories, LinkedIn company page).
5. **MSB segment push** — 17 MSBs at 23% coverage; target ToyyibPay, SenangPay, Wallex, Xendit, Money Match via TheOrg and LinkedIn.
6. **Cooperative segment** — 21 cooperatives at 0% coverage; assess feasibility (most are small, unlisted entities with no public leadership data).
7. **KAF Digital Bank monitoring** — Track new CEO appointment announcement.
8. **iPay88 deep-dive** — Try LinkedIn company page and industry directories for CFO, CRO, Compliance, CIO, IA, GRC roles beyond the confirmed CISO (Alex Wah).

---

## File Inventory

| File | Description | Size |
|------|-------------|------|
| prospect-database-enriched-v5.23.csv | Master enriched database (205 institutions × 7 roles) | ~218 KB |
| enrichment-report-v5.23.md | This report | ~10 KB |
| update_v523.py | Update script for this cycle | ~6 KB |
| prospect-database-enriched-v5.22.csv | Previous version (backup) | ~218 KB |

---

## Methodology Notes

### TheOrg as a Source

TheOrg (theorg.com) is a crowd-sourced organizational chart platform that lists company employees with their titles. Data is marked "Unverified" and should be treated as MEDIUM confidence (score 65). However, TheOrg proved valuable for this cycle because:

1. **Fintech coverage**: TheOrg has good coverage of Southeast Asian fintech startups (BigPay, Billplz) that traditional corporate websites do not.
2. **Specific titles**: TheOrg lists exact job titles (e.g., "Group Chief Information Security Officer", "Head Of Compliance") that match our 7 target roles.
3. **Named individuals**: Each entry has a real person's name, enabling cross-referencing with LinkedIn.

**Limitations:**
- Data is "Unverified" (crowd-sourced, not officially confirmed)
- May be outdated (employees may have left)
- No source URLs or dates for individual entries
- Some companies have no TheOrg page (iPay88, Money Match, SenangPay returned 404)

### BigPay Entity Mapping

BigPay appears as two entries in the database:
1. **BigPay (Capital A)** — T4, E-Money — the e-money product/service
2. **BigPay Malaysia Sdn Bhd** — T3, MSBs — the BNM-licensed MSB entity

Both represent the same operating company (BigPay, a Capital A / formerly AirAsia fintech subsidiary). The same executive team applies to both entries. Previous research noted CFO Mun Hui Teh from Capital A parent (conf 80); this cycle replaced with BigPay-specific CFO Nicholas Chua (conf 65, TheOrg).

---

**Report prepared by:** VoronDRQ Stakeholder Collection Agent  
**Git Repository:** https://github.com/ahmadfaurani/Voron-Campaign  
**Git Email:** p62operator@proton.me  
**Classification:** TLP:AMBER  
**Next scheduled run:** Automated cron — next cycle  

# Voron Stakeholder Enrichment Report v5.26

**Generated:** 2026-07-22 00:17 +08 (MYT)
**Database:** prospect-database-enriched-v5.26.csv
**Previous Version:** v5.25 (2026-07-21)
**Classification:** TLP:AMBER — Handle with care, do not redistribute publicly

---

## Executive Summary

This cycle focused on verifying and enriching leadership data for Malaysian insurers and takaful operators, with emphasis on confirming NOT FOUND entries using official annual reports and corporate leadership pages.

**1 new stakeholder fill** was applied (Tokio Marine Life CISO), and **14 NOT FOUND entries** were updated with strengthened source attribution from official documents.

### Key Metrics

| Metric | v5.25 | v5.26 | Change |
|--------|-------|-------|--------|
| Total Institutions | 205 | 205 | 0 |
| Named Cells | 834 (58.1%) | 835 (58.2%) | +1 |
| NOT FOUND | 601 (41.9%) | 600 (41.8%) | -1 |
| Empty (unresearched) | 0 | 0 | 0 |
| Total Cells | 1,435 | 1,435 | 0 |

---

## New Fill: Tokio Marine Life Insurance Malaysia Bhd

### CISO — Irfan Ismail

| Field | Value |
|-------|-------|
| **Name** | Irfan Ismail |
| **Title** | CISO & Head of Technology Risk |
| **Institution** | Tokio Marine Life Insurance Malaysia Bhd |
| **Source** | RocketReach/LinkedIn (rocketreach.co/irfan-ismail-email_229003941) |
| **Confidence** | 55 (LinkedIn-cited via RocketReach; not on official management team page) |
| **Verification** | Tokio Marine Life management team page (9 senior managers listed) does not include CISO role — Irfan Ismail identified through RocketReach LinkedIn aggregation |
| **Notes** | Tokio Marine Life previously had CISO = NOT FOUND. This fill brings Tokio Marine Life to 6/7 roles filled (only GRC remains NOT FOUND) |

---

## Source Evidence Updates (14 entries)

### MSIG Insurance (Malaysia) Bhd — 4 NOT FOUND entries strengthened

**Source:** MSIG Annual Report 2024 (msig.com.my/media/c53di1r0/msig_annual_report_2024.pdf), p.107-108

The AR 2024 lists a 13-member Senior Management Team. None of the 13 members hold a CISO, GRC head, Compliance head, or Internal Audit head title. This confirms the existing NOT FOUND status with high confidence (95%).

| Role | Status | Source Evidence |
|------|--------|----------------|
| CISO | NOT FOUND | AR 2024 p.107-108: 13-member SMT listed; no CISO. IT headed by Chin Jee Gwan (EVP IT, Digital, Bancassurance & Branding), no dedicated cybersecurity role |
| GRC | NOT FOUND | AR 2024: No "Head of GRC" in 13-member SMT. Risk covered by Kelvin Hii (SVP ERM) |
| Compliance | NOT FOUND | AR 2024 references "Chief Compliance Officer" in CG disclosure but does not name the CCO |
| Internal Audit | NOT FOUND | AR 2024 references "Chief Internal Auditor" in Internal Audit disclosure but does not name the CIA |

**Already filled (verified this cycle):**
- CFO: Soh Lai Sim (COO, also Officer primarily responsible for financial management per AR 2024 statutory declaration) ✓
- CRO: Kelvin Hii Chee Yun (SVP, Enterprise Risk Management) ✓
- CIO: Chin Jee Gwan (EVP IT, Digital, Bancassurance & Branding) ✓

### Kurnia Insurans / Zurich General Insurance Malaysia Berhad — 3 NOT FOUND entries strengthened

**Source:** Zurich Malaysia leadership page (zurich.com.my/about-zurich/the-zurich-story/our-leaders)

The Zurich Malaysia leadership page lists only 4 CEOs as "Senior Management" — no CISO, CFO, CRO, CIO, Compliance, IA, or GRC roles are publicly disclosed at entity or country level.

| Role | Status | Source Evidence |
|------|--------|----------------|
| CISO | NOT FOUND | Zurich Malaysia leadership page lists only 4 CEOs as Senior Management; no CISO disclosed |
| CFO | NOT FOUND | Zurich Malaysia leadership page lists only 4 CEOs as Senior Management; no CFO disclosed |
| CRO | NOT FOUND | Zurich Malaysia leadership page lists only 4 CEOs as Senior Management; no CRO disclosed |

**Zurich Malaysia Senior Management (confirmed):**
- Junior Cho — Country CEO, Zurich Malaysia + CEO, Zurich General Insurance Malaysia Berhad
- Pauline Teoh — CEO, Zurich Life Insurance Malaysia Berhad
- Nur Fatihah Mustafa — CEO, Zurich Takaful Malaysia Berhad
- Shamsul Azman — CEO, Zurich General Takaful Malaysia Berhad

### Zurich Life Insurance Malaysia Berhad — 3 NOT FOUND entries strengthened

**Source:** Zurich Malaysia leadership page + AR 2025 financial statements (signed by directors only, no CFO named)

| Role | Status | Source Evidence |
|------|--------|----------------|
| CISO | NOT FOUND | Zurich Malaysia leadership page lists only 4 CEOs; no CISO disclosed. AR 2025 FS signed by directors only |
| CFO | NOT FOUND | Zurich Malaysia leadership page lists only 4 CEOs; no CFO disclosed. AR 2025 FS signed by directors only |
| CRO | NOT FOUND | Zurich Malaysia leadership page lists only 4 CEOs; no CRO disclosed. Board Risk Committee chaired by Donald Joshua Jaganathan (board-level) |

### Zurich Takaful Malaysia Berhad — 3 NOT FOUND entries strengthened

**Source:** Zurich Malaysia leadership page + AR 2025 financial statements (signed by directors only, no CFO named)

| Role | Status | Source Evidence |
|------|--------|----------------|
| CISO | NOT FOUND | Zurich Malaysia leadership page lists only 4 CEOs; no CISO disclosed. AR 2025 FS signed by directors only |
| CFO | NOT FOUND | Zurich Malaysia leadership page lists only 4 CEOs; no CFO disclosed. AR 2025 FS signed by directors only |
| CRO | NOT FOUND | Zurich Malaysia leadership page lists only 4 CEOs; no CRO disclosed. Board Risk Committee chaired by Datuk Dr. Hafsah binti Hashim (board-level) |

---

## Verification Activities This Cycle

### Sources Consulted

1. **MSIG Annual Report 2024** (PDF, msig.com.my) — Scraped via Firecrawl. Confirmed 13-member Senior Management Team. No CISO/GRC/Compliance/IA in SMT.
2. **Zurich Malaysia Leadership Page** (zurich.com.my/about-zurich/the-zurich-story/our-leaders) — Extracted via web_extract. Confirmed only 4 CEOs listed as Senior Management.
3. **Sun Life Malaysia Management Team Page** (sunlifemalaysia.com/about-us/leadership/management-team/) — Scraped via Firecrawl. Page is photo-heavy with alt-text containing names only; no job titles visible in text extraction. Cannot determine role assignments from this source.
4. **Tokio Marine Life Management Team Page** (tokiomarine.com/my/en/life/about-us/our-board-of-directors-and-management-team.html) — Extracted via web_extract. 9 senior managers listed; CISO not among them.
5. **Manulife Insurance Board of Directors Page** (manulife.com.my/en/individual/about-us/about-manulife-malaysia/manulife-insurance-berhad-board-of-directors.html) — Scraped via Firecrawl (25,945 chars). Board members listed but management team / CISO not on this page.
6. **Chubb Malaysia Corporate Governance Page** (chubb.com/my-en/about-chubb/corporate-governance.html) — Extracted. Board structure and committees described but individual C-suite executives (CISO, Compliance) not named.
7. **RocketReach** (rocketreach.co/irfan-ismail-email_229003941) — LinkedIn aggregation. Confirmed Irfan Ismail as CISO & Head of Technology Risk at Tokio Marine Life Insurance Malaysia. Direct page extraction failed (blocked), but search result snippet provided the confirmation.

### Institutions Verified (no changes needed)

- **Affin Investment Bank Berhad** — All 7 roles already filled (Group CISO: Teng Wei Lim, Group CFO: Joanne Rodrigues, Group CRO: Cheong Dang, etc.)
- **Bank Muamalat Malaysia Berhad** — All 7 roles already filled (CISO: Ts. Dr. Ismamuradi Abdul Kadir, CFO: Amirul Nasir Abdul Rahim, CRO: Hamidi A Razak, etc.)
- **MSIG Insurance** — CFO, CRO, CIO already filled and verified against AR 2024 SMT
- **Manulife Insurance Berhad** — CFO (Ng Chun Nam), CRO (Mohd Naim Mohd Arsad), CIO (Bernard Sia), Compliance (Senthil Woon) already filled. CISO and IA remain NOT FOUND.

---

## Remaining Gaps by Segment (High Priority)

### Insurers (49 NOT FOUND → 48 NOT FOUND after this cycle)

Key remaining insurer gaps:
- **Allianz General/Life**: CISO, GRC, CRO, Compliance NOT FOUND (AR 2024 checked, 16-member SMT)
- **AmMetLife Insurance**: CISO, GRC, Compliance, IA NOT FOUND
- **Chubb Insurance**: CISO, Compliance NOT FOUND
- **FWD Insurance**: CISO, CIO NOT FOUND
- **Great Eastern General Insurance**: CISO NOT FOUND
- **Manulife Insurance**: CISO, IA NOT FOUND
- **MSIG Insurance**: CISO, GRC, Compliance, IA NOT FOUND (AR 2024 confirmed)
- **Sun Life Malaysia Assurance**: Management page photos only, no titles extractable

### Takaful (30 NOT FOUND)

Key remaining takaful gaps:
- **AIA Public Takaful**: IA NOT FOUND
- **General Takaful**: CISO, CRO NOT FOUND
- **HSBC Amanah Takaful**: CISO, GRC, CRO, CIO, IA NOT FOUND (official team page has only 6 executives)
- **Manulife Takaful**: CISO, GRC NOT FOUND
- **Zurich Takaful**: CISO, CFO, CRO NOT FOUND (Zurich leadership page confirmed)

### Development FIs (20 NOT FOUND)

Key remaining DevFI gaps:
- **BSN**: CISO, IA NOT FOUND
- **Bank Rakyat**: IA NOT FOUND
- **PUNB**: CISO, CIO NOT FOUND

### Licensed Banks (33 NOT FOUND)

Key remaining bank gaps:
- **Mizuho Bank Malaysia**: CFO, CRO, CISO, CIO, Compliance, GRC NOT FOUND (audited FS FYE Mar 2025 references roles but doesn't name holders)
- **SMBC Malaysia**: Leadership data not found in public sources

---

## Search Engine Issues

Both `web_search` and `firecrawl_search` returned extremely poor results throughout this cycle:
- Malaysian financial institution queries returned Chinese forum posts, Taiwanese government websites, Swiss tourism pages, and dictionary definitions
- LinkedIn site: searches returned empty results
- Domain-restricted Firecrawl searches returned 0 results

This significantly limited the ability to find new CISO and leadership data via web search this cycle. Direct URL extraction (web_extract, Firecrawl scrape) remained reliable for known URLs.

---

## Next Steps (v5.27 Targets)

1. **Manulife Insurance Berhad**: Search for CISO and Head of Internal Audit via Manulife Holdings Berhad Annual Report (Bursa Malaysia filing)
2. **Sun Life Malaysia Assurance**: Try browser-based extraction of management team page to capture titles from image alt-text or hover text
3. **BSN**: Search for CISO and IA via BSN Annual Report or Bursa Malaysia filings
4. **Bank Rakyat**: Search for IA via Bank Rakyat Annual Report
5. **Great Eastern General Insurance**: Try more targeted LinkedIn searches for CISO
6. **Allianz General/Life**: Try Allianz Malaysia IAR 2024 for CRO and Compliance heads
7. **HSBC Amanah Takaful**: Try HSBC Malaysia annual report for C-suite roles
8. **Chubb Insurance**: Try Chubb Malaysia annual report for CISO and Compliance
9. **Mizuho/SMBC Malaysia**: Try BNM PI publication or annual report PDFs
10. **Investment Banks**: Kenanga, TA Securities, JF Apex leadership pages

---

## Audit Trail

| # | Institution | Role | Change Type | Source |
|---|-------------|------|-------------|--------|
| 1 | Tokio Marine Life Insurance Malaysia Bhd | CISO | **NEW FILL** | RocketReach/LinkedIn (conf 55) |
| 2 | MSIG Insurance (Malaysia) Bhd | CISO | Source Update | AR 2024 p.107-108 |
| 3 | MSIG Insurance (Malaysia) Bhd | GRC | Source Update | AR 2024 SMT |
| 4 | MSIG Insurance (Malaysia) Bhd | Compliance | Source Update | AR 2024 CG disclosure |
| 5 | MSIG Insurance (Malaysia) Bhd | IA | Source Update | AR 2024 IA disclosure |
| 6 | Kurnia Insurans / Zurich General | CISO | Source Update | Zurich Malaysia leadership page |
| 7 | Kurnia Insurans / Zurich General | CFO | Source Update | Zurich Malaysia leadership page |
| 8 | Kurnia Insurans / Zurich General | CRO | Source Update | Zurich Malaysia leadership page |
| 9 | Zurich Life Insurance Malaysia | CISO | Source Update | Zurich Malaysia leadership page |
| 10 | Zurich Life Insurance Malaysia | CFO | Source Update | Zurich Malaysia leadership page |
| 11 | Zurich Life Insurance Malaysia | CRO | Source Update | Zurich Malaysia leadership page |
| 12 | Zurich Takaful Malaysia | CISO | Source Update | Zurich Malaysia leadership page |
| 13 | Zurich Takaful Malaysia | CFO | Source Update | Zurich Malaysia leadership page |
| 14 | Zurich Takaful Malaysia | CRO | Source Update | Zurich Malaysia leadership page |

---

## Methodology Notes

- **Confidence scoring**: HIGH (90-95) = official source + Malaysia-specific; MEDIUM (55-75) = LinkedIn/ RocketReach/ secondary source; LOW (25-40) = inference or stale data
- **Source hierarchy**: Official annual reports > Official leadership pages > Malaysian Insurance Directory > TheOfficialBoard > RocketReach/LinkedIn > The Org > SimplyWall.st
- **NOT FOUND vs Empty**: NOT FOUND = actively researched but no public data found; Empty = not yet researched
- **Source evidence updates**: NOT FOUND entries are updated with specific source references to document what was checked and why the role was not found. This improves audit trail and prevents duplicate research in future cycles.

---

*Report generated by VoronDRQ Stakeholder Collection Agent*
*GitHub: https://github.com/ahmadfaurani/Voron-Campaign*
*TLP:AMBER — Handle with care*

# Enrichment Report v5.40

**Generated:** 2026-07-25 04:17 +08 (MYT)
**Classification:** TLP:AMBER
**Database:** prospect-database-enriched-v5.40.csv
**Previous Version:** v5.39

---

## Executive Summary

This report documents the v5.40 enrichment cycle of the VoronDRQ 7-stakeholder prospect database covering 207 Malaysian financial institutions across 8 segments.

**Coverage remains at 58.5%** (848/1,449 role cells filled). The v5.40 cycle focused on verifying and enriching notes for quick-win institutions (1 missing role) via direct URL extraction from official leadership pages. While no new personnel names were confirmed in this cycle, three institutions received updated, higher-confidence NOT FOUND notes based on newly extracted official sources.

---

## Coverage Statistics

### Overall
| Metric | Count | % |
|--------|-------|---|
| Total institutions | 207 | — |
| Total role cells | 1,449 | — |
| Filled (with name) | 848 | 58.5% |
| NOT FOUND | 581 | 40.1% |
| ENTITY NON-EXISTENT | 20 | 1.4% |

### By Role
| Role | Filled | NOT FOUND | Entity Non-Existent |
|------|--------|-----------|---------------------|
| CISO | 95 | 110 | 2 |
| Head of GRC | 111 | 93 | 3 |
| CFO | 148 | 56 | 3 |
| CRO | 121 | 83 | 3 |
| Head of Compliance | 127 | 77 | 3 |
| CIO | 131 | 73 | 3 |
| Head of Internal Audit | 115 | 89 | 3 |

### Institutions by Missing Role Count
| Missing Roles | Institutions |
|---------------|-------------|
| 0 (complete) | 77 |
| 1 | 14 |
| 2 | 22 |
| 3 | 13 |
| 4 | 17 |
| 5 | 9 |
| 6 | 14 |
| 7 (all missing) | 41 |

---

## v5.40 Updates (3 note enrichments)

### 1. Bank Rakyat Malaysia → Head of Internal Audit
- **Source:** Official management committee page — `bankrakyat.com.my/portal-main/leaders/management-committee`
- **Finding:** Page lists 8 management committee members: Group CEO (Ahmad Shahril Mohd Shariff), CFO (Nor Haimee Zakaria), Chief Retail Banking Officer (Khairudin Abdul Rahman), COO (Amren Faisal Fadzil), Chief Strategy & Sustainability Officer (Mohamad Taufik Mahamad Zakaria), Group CRO (Azni Azaddin), Chief People Officer (Elina Ahmad), Group Chief Compliance Officer (Jufree Soaidin)
- **Status:** Head of Internal Audit NOT listed on management committee page or BOD page
- **Confidence:** 85 (up from prior)
- **Note:** Also confirmed BOD page (7 directors) does not name an audit executive. 2024 + 2025 Audited Financial Statements reference the Internal Audit function but do not name the role holder.

### 2. HSBC Bank Malaysia Berhad → CISO
- **Source:** Official Board of Directors page — `about.hsbc.com.my/hsbc-in-malaysia/board-of-directors`
- **Finding:** Board page lists 5+ directors including CEO Dato' Omar Siddiq. Management team page returned 404 (not found). No CISO disclosed.
- **Status:** NOT FOUND — country CISO role not publicly disclosed
- **Confidence:** 85 (up from prior)
- **Note:** HSBC's about site structure does not include a management/executive team page. Only Board of Directors is publicly listed.

### 3. Bank Rakyat Investment Bank Berhad → CISO
- **Source:** Bank Rakyat parent Management Committee page (cross-reference)
- **Finding:** Parent Bank Rakyat group management committee (8 members) does not include a CISO. The investment bank subsidiary's own leadership page (rmanagement.com.my) also lacks a CISO.
- **Status:** NOT FOUND — CISO role not listed at subsidiary or group level
- **Confidence:** 40 (unchanged)
- **Note:** Closest IT-related role is Ismat Nazarul Mat Isa (Senior Manager Finance & IT).

---

## Sources Checked This Cycle

| Source | URL | Result |
|--------|-----|--------|
| Bank Rakyat Management Committee | bankrakyat.com.my/portal-main/leaders/management-committee | ✅ Extracted (8 members listed) |
| Bank Rakyat Board of Directors | bankrakyat.com.my/portal-main/leaders/BOD | ✅ Extracted (7 directors listed) |
| Bank Rakyat Site Map | firecrawl_map | ✅ 275 URLs discovered |
| HSBC Board of Directors | about.hsbc.com.my/hsbc-in-malaysia/board-of-directors | ✅ Extracted (5+ directors) |
| HSBC Management Team | about.hsbc.com.my/hsbc-in-malaysia/management-team | ❌ 404 Not Found |
| HSBC Who We Are | about.hsbc.com.my/who-we-are | ❌ 404 Not Found |
| HSBC Our Leadership | about.hsbc.com.my/our-leadership | ❌ 404 Not Found |
| Boost Bank | boostbank.com | ⚠️ Wrong entity (affiliate marketing site, not Malaysian digital bank) |
| GX Bank | gxbank.com.my | ❌ DNS resolution failed |
| ASNB | asnb.com.my | ❌ firecrawl_map returned empty |

---

## Key Findings & Observations

1. **CISO is the hardest role to fill** (110 NOT FOUND out of 207 institutions, 53%). Most Malaysian financial institutions do not publicly disclose their CISO on official websites or leadership pages. This is consistent with global banking sector norms where CISOs are often not publicly listed for security reasons.

2. **CFO has the best coverage** (148 filled, 72%). CFOs are commonly listed in annual reports, press releases, and leadership pages.

3. **41 institutions have all 7 roles missing** — these are primarily smaller Tier 2/3 institutions, fintech startups, and credit cooperatives with minimal public leadership disclosure.

4. **77 institutions (37%) have complete 7-role coverage** — primarily Tier 1 banks and larger insurance/takaful companies.

5. **Firecrawl agent and web search tools continue to return irrelevant results** for Malaysian financial sector executive queries. Direct URL extraction (web_extract, firecrawl_scrape) from official institution websites remains the most productive method.

6. **Bank Rakyat's website structure** uses a portal-main path structure with separate BOD and Management Committee pages. The management committee page is the primary source for senior management roles.

7. **HSBC Malaysia's about site** does not expose a management/executive team page — only Board of Directors. This limits public access to C-suite executives beyond the CEO.

---

## Next Steps

### Priority 1: 14 institutions with 1 missing role
- 10 are missing CISO (hard to find publicly)
- 1 missing Head of Internal Audit (Bank Rakyat — confirmed not listed on official pages)
- 1 missing CIO (Berjaya Sompo — confirmed not listed)
- 1 missing Head of GRC (Boost Bank — confirmed split between CRO/CCO)
- 1 missing Head of GRC (Tokio Marine — confirmed not a combined role)

### Priority 2: 22 institutions with 2 missing roles
- Most are missing CISO + one other role
- Target via annual reports, regulatory disclosures, and LinkedIn enrichment

### Priority 3: 13 institutions with 3 missing roles
- Target via annual reports and BNM regulatory filings

### Priority 4: 41 institutions with all 7 roles missing
- These are the hardest to enrich — primarily small institutions with no public leadership data
- Consider alternative approaches: regulatory filings, company registry, industry directories

---

## Methodology Notes

- **Primary method:** Direct URL extraction from official institution leadership/management pages
- **Secondary method:** Firecrawl scrape with JavaScript rendering for SPA-heavy sites
- **Tertiary method:** Firecrawl map for URL discovery when direct page URLs are unknown
- **Failed methods:** Web search and firecrawl search consistently return irrelevant results for Malaysian financial sector queries
- **Confidence scoring:** 80-95 for official source + Malaysia, 40-60 for LinkedIn only, 20-40 for unverified

---

*Report generated by VoronDRQ Stakeholder Collection Agent*
*GitHub: https://github.com/ahmadfaurani/Voron-Campaign*
*Git Email: p62operator@proton.me*
*TLP:AMBER — Handle with care, do not redistribute publicly.*

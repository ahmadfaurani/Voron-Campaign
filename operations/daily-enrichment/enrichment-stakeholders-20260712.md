# VoronDRQ Stakeholder Enrichment Summary
## Date: 2026-07-12 (Batch 2 - Leadership Pages)
**TLP:AMBER** - Commercial Intelligence

---

## Execution Summary

| Metric | Value |
|--------|-------|
| **Institutions Processed** | 6 |
| **Institutions Enriched** | 3 |
| **New Stakeholders Added** | 7 |
| **Existing Records Updated** | 1 |
| **HIGH Confidence (80-100)** | 7 |
| **MEDIUM Confidence (60-79)** | 0 |
| **Not Found** | 0 (for enriched institutions) |

---

## Enrichment Details

### 1. Maybank Investment Bank Berhad (Segment: Investment Banks)
**Source:** Official leadership page (maybank2u.com.my)
**Coverage:** 3/7 roles (43%)

| # | Role | Name | Confidence | Source |
|---|------|------|------------|--------|
| 1 | CFO | Ezrina Mahadzir | 95 (HIGH) | Official: maybank2u.com.my |
| 2 | CRO | Cheryl Cheng Siew Ying | 95 (HIGH) | Official: maybank2u.com.my |
| 3 | CIO | Adrian Tan Kai Thern | 85 (HIGH) | Official: maybank2u.com.my (Head of IT) |

**Not Found:** CISO, Head of GRC, Head of Compliance, Head of Internal Audit

### 2. Affin Investment Bank Berhad (Segment: Investment Banks)
**Source:** Simply Wall St (financial data platform)
**Coverage:** 4/7 roles (57%)

| # | Role | Name | Confidence | Source |
|---|------|------|------------|--------|
| 1 | CFO | Joanne Rodrigues | 80 (HIGH) | SimplyWall.st (Group CFO, 6.1yrs) |
| 2 | CRO | Cheong Dang | 80 (HIGH) | SimplyWall.st (Group CRO, 4.3yrs) |
| 3 | Compliance | Adzamimah Adzmi | 80 (HIGH) | SimplyWall.st (Group CCO, 8yrs) |
| 4 | Internal Audit | Wahdania Binti Mohd Khir | 80 (HIGH) | SimplyWall.st (Group CIA, 6.2yrs) |

**Not Found:** CISO, Head of GRC, CIO/CTO

### 3. Great Eastern Life Assurance (Malaysia) Berhad (Segment: Insurers)
**Source:** Official key executives page (greateasternlife.com)
**Coverage:** 5/7 roles (71%) — IMPROVED from prior run

| # | Role | Name | Confidence | Source | Change |
|---|------|------|------------|--------|--------|
| 1 | CFO | Loke Chang Yueh | 95 (HIGH) | Official: greateasternlife.com | Updated with full details |
| 2 | CRO | Teo Chun Seng | 90 (HIGH) | Official: greateasternlife.com | Updated with appointment date |
| 3 | Compliance | Helen Quat Li Huang | 95 (HIGH) | Official: greateasternlife.com | NEW — replaced Liza Hanim (Legal) |
| 4 | CIO | Vincent Chin | 90 (HIGH) | Official: greateasternlife.com | Updated with join date |
| 5 | Internal Audit | Audra Chung Kit Li | 95 (HIGH) | Official: greateasternlife.com | Updated with details |

**Not Found:** CISO, Head of GRC

---

## Institutions Not Enriched (This Batch)

| Institution | Reason | Next Step |
|-------------|--------|-----------|
| Citibank Berhad | No leadership data found via search/scrape | Try LinkedIn enrichment, annual report |
| Prudential Assurance Malaysia Berhad | Board page only (no C-suite); CEO appointment found | Search for management team page |
| Manulife Insurance Berhad | Board page scraped; CEO only found | Search for management team / annual report |

---

## Source URLs

| Institution | Source URL | Type |
|------------|-----------|------|
| Maybank IB | https://www.maybank2u.com.my/Investment-bank/en/about-us/our-leadership/senior-management.page | Official |
| Affin Bank | https://simplywall.st/stocks/my/banks/klse-affin/affin-bank-berhad-shares/management | Financial Data |
| Great Eastern Life | https://www.greateasternlife.com/my/en/about-us/company-profile/our-leaders/key-executive.html | Official |
| Great Eastern Board | https://www.greateasternlife.com/my/en/about-us/company-profile/our-leaders/board-of-directors.html | Official |
| Prudential Board | https://www.prudential.com.my/en/about-us/our-company/leadership | Official (board only) |

---

## CSV Updates

### Master CSV (column-per-role schema)
**File:** `prospects/prospect-database-7stakeholders.csv`

| Row | Institution | Roles Added/Updated |
|-----|-------------|-------------------|
| 9 | Affin Investment Bank Berhad | 4 roles (CFO, CRO, Compliance, Internal Audit) |
| 69 | Great Eastern Life Assurance (Malaysia) Berhad | 5 roles updated (CFO, CRO, Compliance, CIO, Internal Audit) |
| 134 | Maybank Investment Bank Berhad | 3 roles (CFO, CRO, CIO) |

### Enriched CSV v1.9
**File:** `prospects/prospect-database-enriched-v1.9.csv`
Same updates as master CSV.

---

## Next Steps

1. [ ] LinkedIn enrichment for Citibank Berhad (no official leadership data found)
2. [ ] Search for Prudential Malaysia management team page (board page found, need C-suite)
3. [ ] Search for Manulife Malaysia management team (board page found, need C-suite)
4. [ ] Continue to next batch: Bank Islam, Bank Rakyat, BSN (Development Finance)
5. [ ] Cross-reference with annual reports for MEDIUM confidence contacts
6. [ ] GitHub push pending

---

**Classification:** TLP:AMBER
**Agent:** VoronDRQ Stakeholder Collection Agent
**Run:** 2026-07-12 Batch 2

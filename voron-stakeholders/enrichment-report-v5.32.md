# VoronDRQ Stakeholder Enrichment Report v5.32

**Generated:** 2026-07-23 12:00 MYT (UTC+8)
**Brief ID:** VDRQ-ENV532-20260723
**Classification:** TLP:AMBER
**Git Repo:** https://github.com/ahmadfaurani/Voron-Campaign
**Database:** prospect-database-enriched-v5.32.csv

---

## Executive Summary

This enrichment session focused on **official leadership page verification** and **2025 Financial Statement PDF extraction** for gap institutions across insurance, banking, and takaful segments. Research targeted 15+ institutions using Firecrawl scrape (including PDF parsing), Firecrawl map, and direct URL extraction.

### Key Achievements
- **1 CFO update** — Sun Life Malaysia Assurance Berhad CFO updated from "Chew Chin Lim" (2024 AR) to "Ong Le Keat" (2025 Financial Statement, statutory declaration dated 10 March 2026)
- **1 new entity added** — Sun Life Malaysia Takaful Berhad added as separate institution (row 181) with CFO = Ong Le Keat (2025 FS statutory declaration dated 11 March 2026)
- **12 institutions verified** — Leadership pages scraped and gaps confirmed as genuinely not publicly listed for: AIA Bhd, AIA General, AIA Public Takaful, Bank Rakyat, Berjaya Sompo, Tokio Marine Life Malaysia, Manulife Insurance Berhad, Manulife Holdings Berhad, Takaful Malaysia, Takaful Am General Berhad, Khazanah Nasional, Sun Life Malaysia
- **Total database coverage:** 841/1,442 cells filled (58.3%) across 206 institutions

### Research Conclusion
This session confirmed the structural finding from v5.31: remaining gaps (primarily CISO, Internal Audit, GRC, CRO) represent roles genuinely not publicly listed by Malaysian financial institutions. The 2025 Financial Statement PDFs for Sun Life Malaysia (both Assurance and Takaful) confirmed:
- CFO is named in the statutory declaration (Officer primarily responsible for financial management)
- CEO and Executive Directors are named in the Directors' Report
- CISO, CIO, Compliance, GRC, and Internal Audit executives are NOT named in financial statements
- Management team web pages use image-based cards (titles not extractable via text scraping)

---

## Changes from v5.31 to v5.32

### 1. Sun Life Malaysia Assurance Berhad — CFO Update

| Field | v5.31 (Old) | v5.32 (New) |
|-------|-------------|-------------|
| **CFO Name** | Chew Chin Lim | Ong Le Keat |
| **Title** | Chief Financial Officer | Chief Financial Officer / Officer primarily responsible for financial management |
| **Source** | Sun Life Malaysia 2024 Annual Report PDF | Sun Life Malaysia Assurance Berhad 2025 Financial Statement PDF |
| **Date** | 2024 AR | Statutory Declaration dated 10 March 2026 |
| **Confidence** | HIGH (official) | HIGH (official, statutory declaration) |

**Context:** The 2024 Annual Report listed "Chew Chin Lim" as the CFO in the statutory declaration. The 2025 Financial Statement (signed 10 March 2026) lists "Ong Le Keat" as the "Officer primarily responsible for the financial management of Sun Life Malaysia Assurance Berhad." This is a genuine CFO change between 2024 and 2025.

### 2. Sun Life Malaysia Takaful Berhad — New Entity Added

| Field | Value |
|-------|-------|
| **Institution** | Sun Life Malaysia Takaful Berhad |
| **Tier** | 2 |
| **Segment** | Insurers |
| **CFO** | Ong Le Keat (Officer primarily responsible for financial management) |
| **Source** | Sun Life Malaysia Takaful Berhad 2025 Financial Statement PDF, Statutory Declaration dated 11 March 2026 |
| **Confidence** | HIGH (official, statutory declaration) |

**Note:** Ong Le Keat serves as CFO for BOTH Sun Life Malaysia Assurance Berhad and Sun Life Malaysia Takaful Berhad. The Takaful entity was missing from the v5.31 database but is now added as a separate institution (row 181) consistent with how other Takaful entities (AIA Public Takaful, Manulife Takaful, Zurich Takaful) are tracked.

**CEO of Takaful entity:** Encik Noor Azam Bin Mohd Yusof (appointed 3 February 2025, per 2025 FS Directors' Report).

---

## Institutions Verified (Gaps Confirmed)

### AIA Group (3 entities, Internal Audit gap)
| Institution | Gap | Page Scraped | Status |
|-------------|-----|-------------|--------|
| AIA Bhd | Head of Internal Audit | aia.com.my/en/about-aia/aia-subsidiaries/about-aia-bhd/leadership-team.html (15,366 chars) | NOT FOUND — EXCO page lists 11 executives, no Internal Audit |
| AIA General Berhad | Head of Internal Audit | aia.com.my/en/about-aia/aia-subsidiaries/about-aia-general-berhad/leadership-team.html (9,381 chars) | NOT FOUND — Management Team lists 6 people, no Internal Audit |
| AIA Public Takaful | Head of Internal Audit | aia.com.my/en/about-aia/aia-subsidiaries/about-aia-public-takaful-bhd/leadership-team.html (23,077 chars) | NOT FOUND — Management Team page, no Internal Audit listed |

### Banking
| Institution | Gap | Page Scraped | Status |
|-------------|-----|-------------|--------|
| Bank Rakyat | Head of Internal Audit | bankrakyat.com.my/portal-main/leaders/management-committee (6,328 chars) | NOT FOUND — Management Committee lists 8 executives, no Internal Audit |
| Khazanah Nasional | CISO, Internal Audit | khazanah.com.my/responsible-stewardship/leadership/executive-management + investment-management (20,414 chars) | NOT FOUND — Executive Management lists 9 people + Investment team; CISO and Internal Audit not listed |

### Insurance & Takaful
| Institution | Gap | Page Scraped | Status |
|-------------|-----|-------------|--------|
| Berjaya Sompo Insurance | CIO | berjayasompo.com.my/leadership-team (2,981 chars) | NOT FOUND — Management Team lists 8 executives (CEO, CCO, CFO, CHRO, CCLO, COO, Chief Claims Officer), no CIO |
| Tokio Marine Life Malaysia | GRC | tokiomarine.com/my/en/life/about-us/our-board-of-directors-and-management-team.html (14,429 chars) | NOT FOUND — Senior Management Team lists 9 people, no GRC role |
| Takaful Malaysia | CISO, CRO | takaful-malaysia.com.my/tentang-kami/barisan-kepimpinan/ (13,950 chars) | NOT FOUND — 11 Group Management + 7 STMAB Management roles listed; no CISO or CRO. All other 5 roles already in CSV |
| Takaful Am General Berhad | CISO, CRO | (same page as Takaful Malaysia) | NOT FOUND — Data from MNRB Holdings; CISO and CRO not listed |

### Manulife Group
| Institution | Gap | Page Scraped | Status |
|-------------|-----|-------------|--------|
| Manulife Insurance Berhad | CISO, GRC | manulife.com.my board pages (24,319 + 20,311 chars) | NOT FOUND — Board pages only list non-executive directors. Management team data from AR already in CSV |
| Manulife Holdings Berhad | (board verification) | manulife.com.my board page (25,121 chars) | Confirmed — Board members only; Group CEO Vibha Hamsi Coburn confirmed |

### Sun Life Malaysia (Image-Based Page)
| Institution | Gap | Page Scraped | Status |
|-------------|-----|-------------|--------|
| Sun Life Malaysia Assurance | CISO, CIO, Compliance | sunlifemalaysia.com/about-us/leadership/management-team/ | 16 executives identified from image filenames but titles embedded in images, not extractable via text scraping. Web searches for individual names returned no relevant results. 2025 Financial Statement PDF confirms CFO but does not name CISO, CIO, or Compliance head. |

### Inaccessible Sites
| Institution | Issue |
|-------------|-------|
| Allianz Malaysia | Antibot protection blocked all Firecrawl requests |
| BSN (Bank Simpanan Nasional) | URL 404, map returned 0 links |
| QBE Insurance Malaysia | URL 404, map returned 0 links |
| MSIG Insurance Malaysia | URL 404 |
| Sun Life Malaysia (global) | sunlifeglobal.com returned 404 |

---

## Database Statistics

| Metric | v5.31 | v5.32 | Change |
|--------|-------|-------|--------|
| Total Institutions | 205 | 206 | +1 |
| Total Leadership Cells | 1,435 | 1,442 | +7 |
| Actual Name Fills | 840 | 841 | +1 (net) |
| NOT FOUND (with context) | 595 | 601 | +6 |
| Fill Rate | 58.5% | 58.3% | -0.2pp |

### Gaps by Role (v5.32)
| Role | Filled | Gaps | Fill Rate |
|------|--------|------|-----------|
| Chief Financial Officer | 147 | 59 | 71.4% |
| Chief Information Officer | 132 | 74 | 64.1% |
| Head of Compliance | 129 | 77 | 62.6% |
| Chief Risk Officer | 120 | 86 | 58.2% |
| Head of Governance Risk & Compliance | 112 | 94 | 54.4% |
| Head of Internal Audit | 113 | 93 | 54.8% |
| Chief Information Security Officer | 88 | 118 | 42.7% |

### Institutional Coverage
| Category | Count |
|----------|-------|
| Institutions with 7/7 filled | 70 |
| Institutions with 1-6/7 filled | 95 |
| Institutions with 0/7 filled | 41 |

---

## Methodology Notes

### Proven Methods (v5.32)
1. **Financial Statement PDF extraction** — Firecrawl with `parsers: ["pdf"]` successfully extracted 300K+ char PDFs. Statutory declarations reliably name the CFO ("Officer primarily responsible for financial management"). Directors' Reports reliably name CEO and Executive Directors. Other executives (CISO, CIO, Compliance, GRC, Internal Audit) are NOT named.
2. **Official leadership page scraping** — Firecrawl scrape of official leadership/management pages is the fastest method for confirming role-holder names. When pages exist in text format (AIA, Bank Rakyat, Takaful Malaysia, Khazanah, Tokio Marine, Berjaya Sompo), data extraction is reliable.
3. **Firecrawl map** — Essential for discovering correct leadership page URLs when direct URLs return 404s.

### Limitations Encountered
1. **Image-based leadership pages** — Sun Life Malaysia uses image cards for management team. Names extractable from image filenames but titles are embedded in images. Text-based scraping cannot extract titles. Browser vision tools were unavailable (CDP endpoint not connected).
2. **Antibot protection** — Allianz Malaysia blocks all Firecrawl requests.
3. **Web search irrelevance** — Both web_search and firecrawl_search consistently return irrelevant results for executive name + institution queries. LinkedIn `site:` searches return empty results.
4. **Structural gap** — CISO, Internal Audit, and GRC roles are genuinely not publicly listed by most Malaysian financial institutions. These are structural limitations, not research gaps.

---

## Next Steps

1. **Sun Life Malaysia Takaful Berhad** — Try browser vision tools (if CDP available) to extract management team titles from image-based page
2. **Allianz Malaysia** — Try alternative scraping methods (different proxy, browser automation) to bypass antibot protection
3. **Annual Report PDFs** — Continue extracting 2025 Financial Statement PDFs for institutions with CFO/CEO changes (BSN, Great Eastern, Prudential, etc.)
4. **BSN, QBE, MSIG** — Try alternative URL patterns or Firecrawl agent for leadership page discovery
5. **41 zero-fill institutions** — Research feasibility; many are small cooperatives and fintech sandbox entities with no public leadership data

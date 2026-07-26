# VoronDRQ Stakeholder Enrichment Report — v5.52

**Generated:** 2026-07-27 00:14 MYT  
**Database Version:** v5.52  
**Previous Version:** v5.51 (2026-07-26)  
**Classification:** TLP:AMBER  

---

## Executive Summary

This enrichment cycle focused on two objectives: (1) data-quality fixes identified during the v5.51 review, and (2) mining the ET CIO SEA "CIO Movements" article series for Malaysian financial-sector leadership appointments. Four updates were applied across three institutions, including one material data-integrity correction (Khazanah CIO/CTO misclassification).

### Key Metrics

| Metric | v5.51 | v5.52 | Delta |
|--------|-------|-------|-------|
| Institutions | 191 | 191 | 0 |
| Named stakeholders | ~794 | ~798 | +4 |
| Data-integrity fixes | — | 1 | +1 |
| New appointments logged | — | 3 | +3 |

---

## Updates Applied

### 1. Khazanah Nasional Berhad — CIO/CTO Data-Integrity Fix (MATERIAL)

**Issue:** The CIO/CTO column listed "Datuk Hisham Hamdan (Chief Investment Officer)" — this is a **finance/investment** role, NOT an IT role. "Chief Investment Officer" ≠ "Chief Information Officer."

**Fix:** Replaced with **Dr Farid Mohamed Sani (Head, Digitalisation)**, the actual digital/IT leader on Khazanah's Executive Management team, sourced from the official leadership page (khazanah.com.my/who-we-are/leadership).

**Source:** Official: khazanah.com.my/who-we-are/leadership, extracted 2026-07-27  
**Confidence:** 90

**Also updated:** Internal Audit NOT FOUND note — revised executive count from "8 executives" to "9 execs listed" and updated source URL to current page.

---

### 2. Johor Corporation (JCorp) — Deputy Chief Digital Officer Added

**Update:** Added **Budiman Bujang (Deputy Chief Digital Officer)**, appointed January 2025, as deputy to Ahmad Yusri Mohamed (Chief Digital Officer).

**Source:** ET CIO SEA — ciosea.economictimes.indiatimes.com/news/corporate/budiman-bujang-becomes-deputy-chief-digital-officer-at-johor-corporation/116869210  
**Confidence:** 85  
**Notes:** 20 years experience, 16 in leadership. Enterprise strategy, digital, finance, operations background.

---

### 3. Great Eastern Life Assurance (Malaysia) Berhad — Group IT MD Added

**Update:** Added **Gary Goh (MD for Group IT)**, appointed January 2025 at the group level (Singapore-based). Vincent Chin remains as Malaysia entity Head of IT.

**Source:** ET CIO SEA — ciosea.economictimes.indiatimes.com/news/corporate/great-eastern-life-appoints-gary-goh-as-its-md-for-group-it/117069702  
**Confidence:** 85  
**Notes:** Former CTO & Operations Officer at AIA Malaysia (6 years), MetLife (14 years), started career at Accenture (1996). Group-level appointment above Malaysia entity.

---

### 4. Syarikat Takaful Malaysia Berhad — CTO Historical Note Added

**Update:** Added audit-trail note that ET CIO SEA reported **Ts. Tengku Intan** joining as CTO in January 2025. Current official website (confirmed 2026-07-26) lists **Nazaruddin Adha bin Md Noor** as CTO, suggesting Tengku Intan has since departed or changed roles.

**Source:** ET CIO SEA — ciosea.economictimes.indiatimes.com/news/corporate/ts-tengku-intan-joins-syarikat-takaful-malaysia-as-chief-technology-officer/116882054  
**Confidence:** 75 (historical note; current official source takes precedence)  
**Notes:** Tengku Intan was formerly Head of Technology Strategy at DRB-HICOM, and CDIO at SIRIM Berhad (~4 years).

---

## Research Methodology

### ET CIO SEA "CIO Movements" Mining

This cycle successfully mined the ET CIO SEA "CIO Movements" monthly roundup articles for Malaysian financial-sector appointments:

1. **January 2025 roundup** (published Feb 4, 2025) — 17 appointments reviewed, 3 Malaysian identified
2. **February 2025 roundup** (published Mar 5, 2025) — 10 appointments reviewed, 0 Malaysian identified

**Access method:** Firecrawl `scrape(links)` on the `cio+movements` tag page to discover article URLs, then `web_extract` for content. Search backends (web_search, firecrawl_search) continue to return irrelevant global results for Malaysia-specific leadership queries.

### Sources Checked with No New Findings

- MNRB Holdings leadership page (mnrb.com.my/about-us/our-leadership) — Takaful IKHLAS parent; no CISO listed; SMT section uses placeholder text
- Takaful IKHLAS leadership page (takaful-ikhlas.com.my/corporate/our-leadership) — SMT section uses Lorem Ipsum placeholder
- Manulife Malaysia site map — no leadership page found
- FWD Malaysia site map — no leadership page found
- SeaBank Malaysia (seabank.com.my) — domain does not resolve; entity may operate under different URL

---

## Coverage Status

### Role Coverage (unchanged from v5.51)
- **CISO:** 46.6% — remains the worst-covered role; no new CISO appointments found in Jan/Feb 2025 CIO Movements
- **CFO:** ~85% — stable
- **CRO:** ~65% — stable
- **CIO/CTO:** ~70% — improved with Khazanah fix + JCorp deputy + GE Life group appointment
- **Compliance:** ~75% — stable
- **Internal Audit:** ~65% — stable
- **GRC:** ~55% — stable

### Segment Coverage (unchanged)
- **Tier 1 Banks:** ~85% — stable
- **Development Finance:** ~70% — stable
- **Insurance & Takaful:** ~65% — stable
- **Investment & Asset Management:** ~60% — stable
- **Tier 2 & 3 Banks:** ~55% — stable
- **Fintech & Digital Banks:** ~40% — stable
- **Payment Processors:** ~65% — stable
- **Credit Cooperatives:** 0% — structurally unfillable (no C-suite model)

---

## Known Limitations

1. **Search backend degradation:** Both `web_search` and `firecrawl_search` continue to return irrelevant global results for Malaysia-specific leadership queries. Workaround: direct URL extraction + Firecrawl `scrape(links)` for URL discovery.
2. **SeaBank Malaysia:** Domain (seabank.com.my) does not resolve. Entity may operate under a different URL or be a digital-only bank without a public corporate website. All 7 roles remain NOT FOUND.
3. **Cooperatives:** 0% coverage is structural — credit cooperatives (koperasi) do not publish C-suite leadership data. No further research effort warranted.
4. **Foreign bank CISOs:** BNP Paribas, Citibank, Deutsche Bank, ICBC, J.P. Morgan, Mizuho, Bank of America — CISO functions managed at APAC/group level, not published for local Malaysian entities. No new findings this cycle.
5. **Takaful IKHLAS:** Leadership page SMT section uses Lorem Ipsum placeholder text — website is under construction.

---

## Next Steps

1. **Continue ET CIO SEA mining:** Extract March–December 2025 CIO Movements roundups for additional Malaysian appointments
2. **SeaBank:** Try alternative domain discovery (Companies Commission of Malaysia/SSM search, LinkedIn company page)
3. **Annual reports:** Target FY2025 annual reports for insurance/takaful companies with image-based leadership pages (Sun Life Malaysia, Manulife)
4. **CISO-specific:** Monitor ET CIO SEA "Know Your CISO" series for additional Malaysian financial-sector CISO profiles
5. **Version v5.53:** Next cycle targeting remaining CISO gaps and Q3 2025 appointment roundups

---

## Files Modified

| File | Action |
|------|--------|
| `prospect-database-enriched-v5.52.csv` | Created from v5.51; 4 updates applied |
| `enrichment-report-v5.52.md` | New report (this file) |

## Git Commit

```
git add prospect-database-enriched-v5.52.csv enrichment-report-v5.52.md
git commit -m "v5.52: Khazanah CIO/CTO data-integrity fix + 3 ET CIO SEA appointments (JCorp, GE Life, Takaful Malaysia)"
```

---

*Classification: TLP:AMBER — Handle with care, do not redistribute publicly.*

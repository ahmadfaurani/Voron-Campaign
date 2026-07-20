# VoronDRQ 7 Stakeholder Target List - Tier 1 Banks (Malaysia)

**Target Roles (7 stakeholders):**
1. Chief Information Security Officer (CISO)
2. Chief Financial Officer (CFO)
3. Chief Risk Officer (CRO)
4. Chief Information Officer (CIO)
5. Head of Compliance
6. Head of Internal Audit
7. Head of Governance, Risk & Compliance (GRC)

---

## Tier 1 Banks - Priority Targets (28 institutions)

### Major Local Banks (Top 8)

| # | Bank | Leadership URL | Annual Report URL | Priority |
|---|------|----------------|-------------------|----------|
| 1 | Maybank Berhad | https://www.maybank.com.my/about-us/our-leaders | https://www.maybank.com.my/investor-relations/financial-reports | HIGH |
| 2 | CIMB Bank Berhad | https://www.cimb.com/en/about-cimb/leadership.html | https://www.cimb.com/en/research-and-insights/financial-reports.html | HIGH |
| 3 | Public Bank Berhad | https://www.publicbank.com.my/en-my/about-us/board-of-directors | https://www.publicbank.com.my/en-my/investor-relations/financial-reports | HIGH |
| 4 | RHB Bank Berhad | https://www.rhbgroup.com/en/about-us/our-people | https://www.rhbgroup.com/en/investor-relations/financial-reports | HIGH |
| 5 | Hong Leong Bank Berhad | https://www.hlb.com.my/en/about-hlb/our-board-and-senior-management.html | https://www.hlb.com.my/en/investor-relations/financial-reports.html | HIGH |
| 6 | AmBank Berhad | https://www.ambankgroup.com/about-us/our-leadership/ | https://www.ambankgroup.com/investor-relations/financial-reports/ | HIGH |
| 7 | Bank Islam Malaysia Berhad | https://www.bankislam.com.my/about-us/board-of-directors/ | https://www.bankislam.com.my/investor-relations/financial-reports/ | HIGH |
| 8 | Bank Rakyat | https://www.bankrakyat.com.my/about-us/corporate-governance/board-of-directors | https://www.bankrakyat.com.my/investor-relations/financial-reports | HIGH |

### Foreign Banks with Local Operations (Top 10)

| # | Bank | Leadership URL | Priority |
|---|------|----------------|----------|
| 9 | OCBC Bank (Malaysia) Berhad | https://www.ocbc.com.my/personal-banking/about-ocbc/our-leadership | HIGH |
| 10 | UOB Malaysia Berhad | https://www.uob.com.my/personal/about-uob/our-leadership.page | HIGH |
| 11 | HSBC Bank Malaysia Berhad | https://www.hsbc.com.my/about-hsbc/who-we-are/ | HIGH |
| 12 | Standard Chartered Bank Malaysia Berhad | https://www.sc.com/my/about-us/ | HIGH |
| 13 | Citibank Berhad | https://www.citi.com.my/personal-banking/about-citi | MEDIUM |
| 14 | Bank of China (Malaysia) Berhad | https://www.bocmy.com/bocmy/en/home/about-us/leadership.html | MEDIUM |
| 15 | Industrial and Commercial Bank of China (Malaysia) Berhad | https://www.icbc.com.my/icbcmy/en/home/about-us.html | MEDIUM |
| 16 | Sumitomo Mitsui Banking Corporation Malaysia Berhad | https://www.smbc.co.id/en/about-us/our-organization | MEDIUM |
| 17 | Mizuho Bank Berhad | https://www.mizuho-fg.com/our-company/organization/index.html | LOW |
| 18 | MUFG Bank Malaysia Berhad | https://www.mufg.jp/english/corporate/profile/ | LOW |

### Investment Banks (Top 10)

| # | Bank | Leadership URL | Priority |
|---|------|----------------|----------|
| 19 | Maybank Investment Bank | https://www.maybank-ib.com/about-us/leadership.html | HIGH |
| 20 | CIMB Investment Bank | https://www.cimb.com/en/about-cimb/leadership.html | HIGH |
| 21 | RHB Investment Bank | https://www.rhbib.com.my/about-us/our-people.html | MEDIUM |
| 22 | Hong Leong Investment Bank | https://www.hlib.com/about-us/board-and-management/ | MEDIUM |
| 23 | Public Investment Bank | https://www.publicinvest.com.my/about-us/board-of-directors/ | MEDIUM |
| 24 | AmInvestment Bank | https://www.aminvestmentbank.com.my/about-us/our-leadership/ | MEDIUM |
| 25 | Kenanga Investment Bank | https://www.kenangaresearch.com.my/about-us/board-of-directors/ | MEDIUM |
| 26 | Affin Investment Bank | https://www.affinib.com/about-us/our-leadership/ | LOW |
| 27 | Alliance Investment Bank | https://www.allianceib.com.my/about-us/board-of-directors/ | LOW |
| 28 | TA Investment Bank | https://www.tainvestment.com.my/about-us/board-of-directors/ | LOW |

---

## Collection Strategy

### Phase 1: Top 8 Local Banks (Days 1-3)
- Scrape leadership pages with Firecrawl
- Extract C-suite and department heads
- Cross-reference with annual reports
- Target: 60-70% enrichment rate

### Phase 2: Foreign Banks (Days 4-7)
- Scrape regional leadership pages
- Focus on Malaysia-specific roles
- Target: 40-50% enrichment rate

### Phase 3: Investment Banks (Days 8-10)
- Scrape investment banking leadership
- Often separate from commercial banking
- Target: 50-60% enrichment rate

---

## Data Quality Standards

**Confidence Scoring:**
- **HIGH (80-100):** Exact role match + company match + Malaysia location + official source URL
- **MEDIUM (60-79):** Related role OR subsidiary company OR regional scope
- **LOW (0-59):** Role mismatch OR unclear affiliation OR outdated information

**Validation Requirements:**
- ✅ Source URL tracked for every contact
- ✅ Role title normalized to standard 7 stakeholder roles
- ✅ Company name normalized to legal entity name
- ✅ No fabrication or guessing of missing data

---

## Output Format

**Database Schema:**
```csv
institution_name,role,full_name,official_title,source_url,confidence_score,extraction_date,notes
Maybank Berhad,CISO,[Name],[Official Title],https://...,95,2026-07-09,Verified from leadership page
```

**GitHub Location:**
- Local: `/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v{version}.csv`
- Remote: `https://github.com/ahmadfaurani/Voron-Campaign/prospects/prospect-database-7stakeholders.csv`

---

**Classification:** TLP:AMBER  
**Last Updated:** 2026-07-09  
**Workspace:** `/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/`

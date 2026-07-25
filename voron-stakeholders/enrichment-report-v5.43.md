# Enrichment Report v5.43

**Generated:** 2026-07-25 08:05 MYT
**Previous version:** v5.42
**Database:** prospect-database-enriched-v5.43.csv
**Total institutions:** 207
**Total cells:** 1,449 (7 roles × 207 institutions)

---

## Coverage Summary

| Role | Filled | NOT FOUND | Coverage % |
|------|--------|-----------|------------|
| CISO | 100 | 107 | 48.3% |
| GRC  | 114 | 93  | 55.1% |
| CFO  | 150 | 57  | 72.5% |
| CRO  | 124 | 83  | 59.9% |
| Comp | 130 | 77  | 62.8% |
| CIO  | 134 | 73  | 64.7% |
| IA   | 118 | 89  | 57.0% |
| **OVERALL** | **870** | **579** | **60.0%** |

**Institutions with 7/7 filled:** 79
**Institutions with 6/7 filled:** 13
**Institutions with 5/7 filled:** 21
**Institutions with ≤4/7 filled:** 94

---

## Changes from v5.42 → v5.43 (3 new fills)

### 1. ASNB (Amanah Saham Nasional Berhad) — CISO ✅ NEW
- **Name:** Aishah Farha Mohd Raih
- **Role:** Chief Information Security Officer (CISO)
- **Source:** ET CIO SEA "Know Your CISO" series
- **URL:** https://ciosea.economictimes.indiatimes.com/news/security/know-your-ciso-aishah-farha-mohd-raih-permodalan-nasional-berhad/112514205
- **Confidence:** HIGH (90) — official CISO interview series, confirmed at Permodalan Nasional Berhad (PNB), parent of ASNB

### 2. Maybank Investment Bank Berhad — CISO ✅ NEW (Group Inheritance)
- **Name:** Devinder Singh
- **Role:** Group Chief Information Security Officer (Group CISO)
- **Source:** Maybank Group leadership page + LinkedIn/The Org
- **Confidence:** HIGH (85) — CISO function shared with Maybank group per SORMIC FY2023; consistent with established inheritance pattern for Maybank subsidiaries (Maybank Islamic, product brands already inherit this role)
- **Rationale:** Maybank IB's SORMIC FY2023 discusses Cyber and Technology Risk Management Framework but does not name a dedicated CISO; group-level CISO applies

### 3. Hong Leong Investment Bank Berhad — CISO ✅ NEW (Group Inheritance)
- **Name:** Dr. Simon Hoh
- **Role:** Group Chief Information Security Officer (Group CISO)
- **Source:** TheOrg (theorg.com/org/hong-leong-bank/org-chart/dr-simon-hoh)
- **Confidence:** MEDIUM (60) — HL Capital AR 2025 Key Senior Management lists 7 members, none with CISO title; inherited from Hong Leong Bank Berhad group, consistent with Hong Leong Islamic Bank inheritance pattern

---

## Confirmed Absences (Official Page Verification)

### GXBank — CISO: Not publicly listed
- **Finding:** Official leadership page (gxbank.my/our-leadership) lists 13 management team members; no CISO/head of information security role among them
- **Management team includes:** CEO (Kaushik Chowdhury), Deputy CEO/COO (Hildah Hamzah), CTO (Nishant Sharma), CRO (Kiyoka Thaam), CFO (Kenneth Leong), Head of Data, Head of Compliance (Nadia Farhan Noordin), Head of Internal Audit (Karina Sivam), Head of Product, Head of Partnerships, Head of Marketing, Head of CX, Head of People
- **Conclusion:** CISO function likely exists but is not publicly disclosed at the leadership team level

### Berjaya Sompo Insurance — CIO/CTO: Not publicly listed
- **Finding:** Official leadership team page (berjayasompo.com.my/leadership-team) lists 8 management team members; no CIO/CTO role among them
- **Management team includes:** CEO (Soo Wai Har), CCO (Vanessa Ngew), Chief Consumer & SME Officer, CFO (Rina Aprila Afianty), CHRO (Jun Ishak), Chief Compliance and Legal Officer (Tricia Mallika Appaduray), COO (Eng Chun Mun), Chief Claims Officer
- **Conclusion:** IT/CIO function likely embedded under COO; no dedicated CIO at leadership level

### Boost Bank — GRC: No standalone role
- **Finding:** GRC function split between CRO (Puteri Syurga) and CCO (Dr Mohanamerry Vedamanikam); board-level "Board Risk and Compliance Committee" exists at governance level
- **Conclusion:** GRC is not a standalone role; it's a combined function handled by CRO + CCO

### MBSB Bank Group — CISO: Not publicly listed
- **Finding:** MBSB Bank Group Management Committee (mbsb.com/corporate_about_team.html) lists 16 executives; no CISO among them
- **Committee includes:** Group CEO (Rafe Haneef), Group CFO (Shahnaz Jammal), Group CRO (Laurence Ong Wooi Keat), Group CCO (Tengku Khalizul Tengku Khalid), Group Chief Internal Auditor (Aniza Zakaria), Group CTO (Noor Azman Bin Abdul Karim), and 10 others
- **Conclusion:** MBSB Bank group does not publicly disclose a CISO; MIDF Amanah Investment Bank's CISO cannot be filled via group inheritance

### Manulife Insurance Berhad & Manulife Takaful — CISO: Not publicly listed
- **Finding:** Manulife Malaysia website only publishes Board of Directors pages, not management team pages; Manulife Holdings Berhad AR 2023 lists 11 MIB senior managers, no CISO
- **Board of Directors includes:** Chairman (Renzo Christopher Viegas / Mary Bernadette James), CEO (Vibha Hamsi Coburn), various INEDs
- **Conclusion:** CISO not publicly disclosed at Manulife Malaysia level

---

## Additional Findings from MBSB Bank Group Page

- **Group Chief Compliance Officer:** Tengku Khalizul Tengku Khalid (MBSB Bank group level)
- **Group Chief Internal Auditor:** Aniza Zakaria (MBSB Bank group level)
- These are group-level roles; MIDF-specific roles (Meor Ibrahim Othman for Compliance, Zanariah Daud for IA) remain valid as subsidiary-level appointments

---

## Search Issues Encountered

- **web_search backend:** Returned completely irrelevant results for institution-specific CISO queries (dictionary definitions, Reddit, unrelated news) — appears degraded
- **firecrawl_search:** Continued to return irrelevant results (Microsoft Excel pages, unrelated domains) for specific Malaysian FI CISO queries
- **Workaround:** Direct `web_extract` on known leadership page URLs and `firecrawl_scrape` for full-page content extraction proved most reliable
- **Blocked:** Citibank Malaysia leadership page returned "private/internal network" error

---

## Methodology

1. **Direct URL extraction** — Primary method: extracted official leadership/management pages from institution websites using `web_extract` and `firecrawl_scrape`
2. **Group inheritance** — Applied where a subsidiary's parent group has a confirmed CISO and the subsidiary itself does not list a dedicated CISO (consistent with established database patterns)
3. **"Know Your CISO" series** — ET CIO SEA publishes CISO interview articles; confirmed Aishah Farha Mohd Raih at PNB via this series
4. **Confirmation of absence** — Where official leadership pages list full management teams without a CISO/CIO/GRC role, documented as confirmed absence rather than NOT FOUND

---

## Next Steps

1. Continue CISO search for remaining 107 NOT FOUND institutions — prioritize Tier 2-3 banks and insurance/takaful segment
2. Search for GRC heads at remaining 93 NOT FOUND institutions
3. Explore LinkedIn-direct queries for institutions where official pages don't list CISOs
4. Consider expanding to annual report PDF extraction for deeper CISO identification
5. Investigate whether some institutions genuinely don't have a standalone CISO (embedded under CIO/CTO or COO)

---

*TLP:AMBER — Handle with care, do not redistribute publicly.*

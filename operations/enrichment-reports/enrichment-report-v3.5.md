# VoronDRQ Enrichment Report v3.5
**Classification:** TLP:AMBER
**Date:** 2026-07-14
**Version:** v3.5 (from v3.4)

## Summary

This enrichment cycle focused on extracting executive leadership data from official corporate websites for previously empty institutions. The primary achievement was a complete executive team extraction from QBE Insurance Malaysia's official website, yielding 3 of 7 target roles with HIGH confidence. A data quality correction was also applied to Manulife Insurance Berhad's CISO field.

## Updates This Cycle

### 1. QBE Insurance (Malaysia) Sdn Bhd — 0/7 → 3/7 ✅ NEW
**Source:** https://www.qbe.com/my/about-qbe/executive-team (OFFICIAL)

| Role | Name | Title | Confidence | Source |
|------|------|-------|------------|--------|
| CFO | Vivien Wong | Head of Finance (joined May 2026, 25+ yrs, CPA Australia & MIA) | HIGH (95) | qbe.com/my |
| CRO | Mohd Farid Bin Othman | Head of Risk (joined Dec 2018, 20+ yrs audit/risk, MIA member) | HIGH (95) | qbe.com/my |
| Head of Compliance | Jaysree Kaliappan | Head of Compliance (joined Jul 2025, 14+ yrs, ICA Dipl. GRC) | HIGH (95) | qbe.com/my |
| CEO (bonus) | Jef Tio | CEO (joined Sep 2025, 23 yrs insurance) | HIGH (95) | qbe.com/my |

**Not found:** CISO, CIO/CTO, Head of Internal Audit, Head of GRC

### 2. Manulife Insurance Berhad — Data Quality Fix
- **CISO field:** Cleared incorrect entry (was "Group CEO: Vibha Hamsi Coburn" — CEO is not CISO)
- **Net change:** 3/7 → 2/7 (GRC: Jasbender Kaur, Compliance: Senthil Woon remain)

### 3. Institutions Investigated But No Target Role Data Found

| Institution | Segment | Source Attempted | Finding |
|-------------|---------|-------------------|---------|
| Zurich Life Insurance Malaysia | Insurers | zurich.com.my/our-leaders | CEO (Pauline Teoh) found but no 7-target-role data |
| Zurich Takaful Malaysia | Takaful | zurich.com.my/our-leaders | CEO (Nur Fatihah Mustafa) found but no 7-target-role data |
| HSBC Amanah Takaful | Takaful | hsbcamanah.com.my | Board of Directors found; executive management page 404 |
| Manulife Takaful Malaysia | Takaful | manulife.com.my | Board pages exist; no executive management data |
| Kurnia Insurans Malaysia | Insurers | kurnia.com | Only contact page, no leadership page |
| MARA | Development FIs | mara.gov.my | Management team page has 28+ names but NO titles |
| PUNB | Development FIs | punb.com.my | Board of Directors found (Chairman: Tan Sri Rastam Mohd Isa); no C-suite |
| Tekun Nasional | Development FIs | web search | No leadership data found |
| LPPSA | Development FIs | web search | No leadership data found |
| Mizuho Bank Malaysia | Licensed Banks | mizuhogroup.com | Limited Malaysia-specific data; no executive names |
| SMBC Malaysia | Licensed Banks | web search | No leadership page found |
| Credit Suisse Malaysia | Licensed Banks | web search | Merged with UBS; may not exist as separate entity |
| Public Bank Berhad | Licensed Banks | web search | CISO not found (5/7 coverage maintained) |

## Overall Database Statistics

### Coverage by Tier
| Tier | Filled/Total | Coverage % |
|------|-------------|-----------|
| T1 (Licensed Banks) | 145/203 | 71.4% |
| T2 (Investment Banks, Insurers, Takaful) | 181/371 | 48.8% |
| T3 (Development FIs, MSBs) | 34/343 | 9.9% |
| T4 (Payment Operators, Card Schemes) | 1/245 | 0.4% |
| T5 (GLC-Linked) | 23/168 | 13.7% |
| T6 (Fintech, E-Money, Cooperatives) | 14/105 | 13.3% |
| **TOTAL** | **398/1435** | **27.7%** |

### Coverage by Segment
| Segment | Filled/Total | Coverage % | Institutions |
|---------|-------------|-----------|-------------|
| Licensed Banks | 145/203 | 71.4% | 29 |
| Investment Banks | 69/105 | 65.7% | 15 |
| Insurers | 91/182 | 50.0% | 26 |
| Development FIs | 34/77 | 44.2% | 11 |
| Takaful | 21/84 | 25.0% | 12 |
| Fintech Sandbox | 14/91 | 15.4% | 13 |
| GLC-Linked | 23/168 | 13.7% | 24 |
| Card Schemes | 1/70 | 1.4% | 10 |
| Payment Operators | 0/42 | 0.0% | 6 |
| MSBs | 0/119 | 0.0% | 17 |
| E-Money | 0/133 | 0.0% | 19 |
| Cooperatives | 0/147 | 0.0% | 21 |
| Fintech Registered | 0/14 | 0.0% | 2 |

### Role Coverage (Across 205 Institutions)
| Role | Filled | Coverage % |
|------|--------|-----------|
| Chief Financial Officer (CFO) | 73/205 | 35.6% |
| Head of Compliance | 64/205 | 31.2% |
| Chief Risk Officer (CRO) | 61/205 | 29.8% |
| Head of GRC | 59/205 | 28.8% |
| Chief Information Officer (CIO) | 59/205 | 28.8% |
| Head of Internal Audit | 51/205 | 24.9% |
| Chief Information Security Officer (CISO) | 31/205 | 15.1% |

### Institutions at 7/7 Coverage: 15
- Affin Investment Bank, Alliance Bank, Alliance Investment Bank, Alliance Islamic Bank
- AmBank, AmBank Islamic, AmInvestment Bank, BIMB Investment Bank
- Bank Islam Malaysia, Bank Muamalat Malaysia, CIMB (Khazanah-linked)
- CIMB Bank, CIMB Investment Bank, CIMB Islamic Bank, Etiqa General Insurance

### Empty Institutions (0/7): 122

## Key Observations

1. **CISO remains the hardest role to fill** (15.1%) — most institutions don't publicly list CISO on their websites
2. **CFO is the best-covered role** (35.6%) — often listed in annual reports and leadership pages
3. **T1 Licensed Banks have strong coverage** (71.4%) — most have official leadership pages
4. **T3/T4 segments need major effort** — Development FIs, MSBs, Payment Operators, E-Money, Cooperatives are largely empty
5. **122 institutions at 0/7** — primarily fintech, e-money, payment processors, and cooperatives
6. **QBE Malaysia extraction was highly productive** — their executive team page had detailed bios for all functional heads
7. **Government agencies (MARA, PUNB, Tekun, LPPSA)** have management pages but lack standard C-suite titles

## Next Priority Targets

1. **Takaful operators** (25% coverage) — HSBC Amanah, Manulife Takaful, Zurich Takaful need executive team pages
2. **Development FIs** (44.2% coverage) — MARA, Tekun, LPPSA need alternative data sources (annual reports, BNM filings)
3. **Insurers** (50% coverage) — Kurnia (likely merged), Zurich Life/General need LinkedIn enrichment
4. **CISO gap-filling** for T1 banks with 5-6/7 coverage (Public Bank, HSBC, Standard Chartered)
5. **T2/T3 Investment banks and Development FIs** — extract from annual reports and BNM disclosure

## Files Updated
- `prospect-database-enriched-v3.5.csv` — 205 institutions, 398/1435 roles filled (27.7%)

---
**Classification:** TLP:AMBER — Handle with care, do not redistribute publicly.

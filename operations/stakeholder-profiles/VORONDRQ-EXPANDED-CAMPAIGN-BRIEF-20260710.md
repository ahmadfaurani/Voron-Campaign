# VORONDRQ EXPANDED SCOPE - CAMPAIGN BRIEF
**Classification:** TLP:AMBER  
**Date:** 2026-07-10  
**Time:** 17:30 MYT  
**Operator:** DAF

---

## EXECUTIVE SUMMARY

**VoronDRQ Stakeholder Mapping has been EXPANDED from 28 Tier 1 banks to ALL Malaysian financial institutions.**

**New Scope:**
- **143 institutions** (up from 28)
- **1,001 stakeholders** (up from 196)
- **8 segments** covering entire Malaysian financial sector
- **28-day timeline** to complete full collection

---

## EXPANDED SCOPE BREAKDOWN

| Segment | Institutions | Stakeholders | Priority | Status | Timeline |
|---------|--------------|--------------|----------|--------|----------|
| **A: Tier 1 Banks** | 28 | 196 | HIGH | 🟡 10/28 (35.7%) | 2026-07-10 to 2026-07-15 |
| **B: Development Finance** | 12 | 84 | HIGH | ⏳ Pending | 2026-07-15 to 2026-07-18 |
| **C: Insurance & Takaful** | 25 | 175 | MEDIUM-HIGH | ⏳ Pending | 2026-07-18 to 2026-07-22 |
| **D: Investment & Asset Mgmt** | 30 | 210 | MEDIUM | ⏳ Pending | 2026-07-22 to 2026-07-26 |
| **E: Tier 2 & 3 Banks** | 15 | 105 | MEDIUM | ⏳ Pending | 2026-07-26 to 2026-07-29 |
| **F: Fintech & Digital Banks** | 15 | 105 | MEDIUM | ⏳ Pending | 2026-07-29 to 2026-08-02 |
| **G: Payment Processors** | 10 | 70 | MEDIUM-HIGH | ⏳ Pending | 2026-08-02 to 2026-08-05 |
| **H: Credit Cooperatives** | 8 | 56 | LOW | ⏳ Pending | 2026-08-05 to 2026-08-07 |
| **TOTAL** | **143** | **1,001** | - | - | **28 days** |

---

## CURRENT PROGRESS (Segment A: Tier 1 Banks)

### ✅ COMPLETED INSTITUTIONS (10/28)

| Bank | Coverage | Stakeholders | Status |
|------|----------|--------------|--------|
| CIMB Bank | 7/7 (100%) ✅ | 7 | Complete |
| Maybank | 3/7 (42.9%) | 3 | In Progress |
| Hong Leong Bank | 2/7 (28.6%) | 2 | In Progress |
| RHB Bank | 2/7 (28.6%) | 2 | In Progress |
| AmBank | 2/7 (28.6%) | 2 | In Progress |
| Bank Rakyat | 2/7 (28.6%) | 2 | In Progress |
| Bank Islam | 2/7 + Shariah | 3 | In Progress |
| HSBC Malaysia | 1/7 (14.3%) | 1 | In Progress |
| OCBC/UOB | 0/7 | 0 | ⚠️ 404 errors |
| **Subtotal** | **21/70** (30%) | **22** | **35.7% banks processed** |

### ⏳ REMAINING INSTITUTIONS (18)

**Priority Order:**
1. Public Bank Berhad
2. Standard Chartered Bank Malaysia
3. Citibank Berhad
4. Bank of China (Malaysia)
5. ICBC (Malaysia)
6. Sumitomo Mitsui Banking Corp
7. Mizuho Bank Berhad
8. MUFG Bank Malaysia
9. Maybank Investment Bank
10. CIMB Investment Bank
11. RHB Investment Bank
12. Hong Leong Investment Bank
13. AmInvestment Bank
14. Affin Investment Bank
15. Kenanga Investment Bank
16. MIDF Amanah Investment Bank
17. JF Apex Securities
18. TA Securities Holdings

---

## COLLECTION METHODOLOGY

### Proven Pattern (CIMB 100% Coverage)

**Step 1: Direct URL Extraction (15 min)**
```
- Use known leadership page URL patterns
- web_extract leadership page → convert to markdown
- Extract all 7 roles with names + titles
- Confidence: HIGH (official source + Malaysia)
```

**Step 2: Web Search (Supplementary, 10 min)**
```
- Search: "{Bank} CFO" OR "CRO" OR "CISO" appointment
- Target: The Edge, NST, FMT, Bernama, official press releases
- Extract from news articles about executive appointments
- Confidence: HIGH (named + titled + dated + official source)
```

**Step 3: LinkedIn Enrichment (10 min)**
```
- Search: site:linkedin.com/in "{Bank}" "{Role}"
- Validate: Role + company + Malaysia location
- Confidence: MEDIUM (LinkedIn only), HIGH if cross-referenced
- Use user's 10k+ network for passive enrichment (pending decision)
```

**Step 4: Database Integration (5 min)**
```
- Update enriched CSV (row-per-contact schema)
- Update master CSV (role-column schema)
- Version control: prospect-database-enriched-v{version}.csv
- Push to GitHub: Voron-Campaign repo
- Telegram alert with commit hash
```

**Total Time per Institution:** 40 minutes  
**Daily Capacity:** 12-15 institutions (84-105 stakeholders)

---

## CRONJOB CONFIGURATION

### Active Jobs

**Job 1: VoronDRQ Stakeholder Collection**
- **Job ID:** 7d5ddfa5bd0b
- **Schedule:** Every 4 hours (0 */4 * * *)
- **Delivery:** Telegram
- **Scope:** All 8 segments (expanded)
- **Status:** ✅ Active, updated with expanded scope prompt

**Job 2: Voron LinkedIn Enrichment Monitor**
- **Job ID:** 434ad2e407cb
- **Schedule:** Every 240 minutes
- **Delivery:** Telegram
- **Scope:** Process LinkedIn exports when available
- **Status:** ✅ Active

**Job 3: Voron Prospect DB Monitor**
- **Job ID:** 9050e5e3fafd
- **Schedule:** Every 360 minutes
- **Delivery:** Telegram
- **Scope:** Monitor database changes
- **Status:** ✅ Active

### Cronjob Updates Applied

**Updated Prompt (7d5ddfa5bd0b):**
- ✅ Expanded target list from 28 to 143 institutions
- ✅ Added all 8 segments with priority order
- ✅ Included proven collection methodology (direct URL extraction)
- ✅ Updated output format with segment tracking
- ✅ Maintained TLP:AMBER classification
- ✅ GitHub auto-push integration preserved

---

## GITHUB REPO STRUCTURE

```
Voron-Campaign/
├── prospects/
│   ├── prospect-database-7stakeholders.csv  # Master (all segments)
│   ├── segment-tier1-banks.csv              # Tier 1 only
│   ├── segment-development-finance.csv      # DFIs
│   ├── segment-insurance-takaful.csv        # Insurance
│   └── segment-investment-asset-mgmt.csv    # Investment firms
├── enriched/
│   ├── prospect-database-enriched-v1.2.csv  # Current (22 stakeholders)
│   ├── prospect-database-enriched-v1.3.csv  # After Tier 1 completion
│   └── ...                                  # Versioned snapshots
├── reports/
│   ├── tier1-banks-summary.md
│   ├── development-finance-summary.md
│   ├── insurance-takaful-summary.md
│   └── ...                                  # Per-segment reports
└── scripts/
    ├── process_linkedin_export.py
    ├── integrate_stakeholders_to_master.py
    └── push-to-github.sh
```

---

## TELEGRAM ALERT FORMAT (Updated)

```
✅ VoronDRQ Enrichment Update - Segment: Tier 1 Banks

📊 Institutions Processed: 10/28 (35.7%)
👥 Stakeholders Collected: 22 (HIGH: 20, MEDIUM: 2)
📈 Coverage Rate: 30% (21/70 roles)

Top Institutions:
- CIMB Bank: 7/7 roles (100%) ✅
- Maybank: 3/7 roles (42.9%)
- Hong Leong Bank: 2/7 roles (28.6%)

📝 Commit: {hash}
🔗 GitHub: {commit_url}
📄 Raw CSV: {raw_url}

Next: Public Bank, Standard Chartered, Citibank
```

---

## LINKEDIN NETWORK INTEGRATION (Pending)

**User Asset:** 10,000+ LinkedIn connections

**Proposed Approach:** Passive crawl (non-intrusive, no credential sharing)

**Options:**
1. **CSV Export** - User exports connections, upload for parsing
   - Setup: 5 minutes
   - Coverage: Names, titles, companies
   - Confidence: MEDIUM-HIGH (requires validation)

2. **Browser Automation** - User logged in, agent extracts visible data
   - Setup: 10 minutes
   - Coverage: + profile details, activity
   - Confidence: HIGH (real-time validation)

3. **Hybrid** - Export for bulk + browser for enrichment
   - Setup: 15 minutes
   - Coverage: Full enrichment
   - Confidence: HIGH

**Potential Value for Expanded Scope:**
- Political operatives in financial sector
- Journalists covering finance/insurance
- Government officials (BSN, PNB, MARA, SME Bank)
- Party members working in finance
- Campaign consultants
- PDRM personnel (financial crime units)
- Cross-sector stakeholders (banks → insurance → fintech)

**Decision Required:** User to choose method and priority

---

## SUCCESS METRICS

### Phase 1: Tier 1 Banks (Current)
- **Target:** 28 institutions, 196 stakeholders
- **Timeline:** 5 days (by 2026-07-15)
- **Expected Coverage:** 40-50% from public sources, 60-70% with LinkedIn
- **Current:** 22 stakeholders (10/28 banks, 35.7%)

### Full Scope (All 8 Segments)
- **Target:** 143 institutions, 1,001 stakeholders
- **Timeline:** 28 days (by 2026-08-07)
- **Expected Coverage:** 50-60% average (varies by segment)
- **Projected Database:** 500-600 HIGH confidence contacts

### Segment-Specific Targets

| Segment | Expected Coverage | Timeline | Priority |
|---------|-------------------|----------|----------|
| Tier 1 Banks | 60-70% | 5 days | HIGH |
| Development Finance | 70-80% | 3 days | HIGH (gov-linked) |
| Insurance & Takaful | 50-60% | 4 days | MEDIUM-HIGH |
| Investment & Asset Mgmt | 40-50% | 4 days | MEDIUM |
| Tier 2 & 3 Banks | 40-50% | 3 days | MEDIUM |
| Fintech & Digital Banks | 30-40% | 4 days | MEDIUM (newer, less public) |
| Payment Processors | 50-60% | 3 days | MEDIUM-HIGH |
| Credit Cooperatives | 30-40% | 2 days | LOW |

---

## RISK ALERTS

| Risk | Severity | Mitigation |
|------|----------|------------|
| **Tier 1 coverage gap** | 🟡 MEDIUM | LinkedIn export + annual reports |
| **Search loop on SEO-heavy sites** | 🟡 MEDIUM | Switch to direct URLs after 2-3 failed searches |
| **JavaScript-heavy leadership pages** | 🟡 MEDIUM | Use browser_vision for screenshot analysis |
| **Cronjob reliability** | 🟢 LOW | Monitor first few runs, adjust if needed |
| **TLP compliance** | 🟢 LOW | All files marked AMBER, access controlled |
| **GitHub rate limits** | 🟢 LOW | Batch commits per segment, not per institution |
| **LinkedIn ToS compliance** | 🟡 MEDIUM | Passive crawl only, no automated login/scraping |

---

## NEXT 24 HOURS

### Immediate (Next 6 hours)
1. ⏳ Cronjob run: Continue Tier 1 bank collection (18 remaining)
2. ⏳ Receive Telegram alert with new stakeholders
3. ⏳ Verify GitHub commit successful
4. ⏳ User decision on LinkedIn network method

### Short-Term (24-48 hours)
1. Complete Tier 1 banks (target: 28/28, 196 stakeholders)
2. Start Development Finance Institutions (12 institutions)
3. Verify PDRM first daily brief quality
4. Monitor PRN Johor polling day (D-2)

### Medium-Term (Week of 11-17 Jul)
1. PRN Johor post-election analysis (within 24hrs of 11 Jul polling)
2. Complete Segments A+B (Tier 1 + Development Finance)
3. Start Segment C (Insurance & Takaful)
4. LinkedIn network integration (if approved)

---

## FILES CREATED/UPDATED

**New Files:**
- `VORONDRQ-EXPANDED-SCOPE-ALL-SEGMENTS.md` (13.7KB) - Full scope documentation
- `VORONDRQ-EXPANDED-CAMPAIGN-BRIEF-20260710.md` (this file)

**Updated Files:**
- Cronjob 7d5ddfa5bd0b prompt (expanded scope)
- `prospect-database-enriched-v1.2.csv` (22 stakeholders)
- `CAMPAIGN-STATUS-MULTI-STREAM-20260710.md` (multi-stream overview)

**Existing Files (Preserved):**
- 7 individual bank reports (CIMB, Maybank, Hong Leong, RHB, AmBank, Bank Rakyat, Bank Islam)
- `target-banks.md` (28 Tier 1 banks - now Segment A)
- `stakeholder-enrichment` skill (methodology preserved)

---

## ACTION REQUIRED

**User Decisions Needed:**

1. ✅ **VoronDRQ Expanded Scope** - CONFIRMED (cronjob updated, collection running)
2. ⏳ **LinkedIn Network Method** - Choose one:
   - A) CSV Export (fastest, safest)
   - B) Browser Automation (more details)
   - C) Hybrid (comprehensive)
   - D) Skip LinkedIn, focus on public sources only

3. ⏳ **Priority After Tier 1** - Which segment next?
   - A) Development Finance (government-linked, strategic)
   - B) Insurance & Takaful (large market, high AUM)
   - C) Investment & Asset Management (high-value targets)
   - D) Continue current priority order (B → C → D → E → F → G → H)

**Reply with:**
- "LinkedIn: [A/B/C/D]"
- "Next Priority: [A/B/C/D]"

---

**Classification:** TLP:AMBER  
**Owner:** DAF  
**Created:** 2026-07-10 17:30 MYT  
**Status:** Expanded scope deployed, collection active

---

## APPENDIX: INSTITUTION LIST BY SEGMENT

### Segment A: Tier 1 Banks (28)
Maybank, CIMB, Public Bank, RHB, Hong Leong, AmBank, Bank Islam, Bank Rakyat, OCBC, UOB, HSBC, Standard Chartered, Citibank, Bank of China, ICBC, Sumitomo Mitsui, Mizuho, MUFG, Maybank IB, CIMB IB, RHB IB, Hong Leong IB, AmInvestment, Affin IB, Kenanga, MIDF Amanah, JF Apex, TA Securities

### Segment B: Development Finance (12)
BSN, Agrobank, SME Bank, EXIM Bank, BPMB, PNB, MARA, CGC, MDV, Danaharta, SJPP, Tekun

### Segment C: Insurance & Takaful (25)
Great Eastern, Prudential, AIA, Allianz, AXA Affin, CIMB Principal, Etiqa, Hong Leong Assurance, Income, Kurnia Asia, Liberty, Manulife, MSIG, Pacific & East, Public Mutual, Takaful IKHLAS, Takaful Malaysia, Zurich Takaful, AmGeneral, Bank Islam Takaful, FWD Takaful, Great Eastern Takaful, Prudential BSN Takaful, RHB Takaful, Takaful Malaysia Keluarga

### Segment D: Investment & Asset Management (30)
ASNB, CIMB-Principal, Public Mutual, RHB AM, Hong Leong AM, Maybank AM, Affin Hwang AM, AmInvestment, Axis REIT, BSN AM, Commerce Asset-Holders, Eastspring, Franklin Templeton, HSBC AM, IMU AM, Inter-Pacific, Kenanga Investors, KAF Investment, Manulife AM, Principal AM, Rakuten AM, Schroders, UOB AM, Value Partners, Versa AM, Kenanga IB, M+ Securities, MIDF Amanah IB, JF Apex, TA Securities

### Segment E: Tier 2 & 3 Banks (15)
Alliance Bank, AmInvestment Bank, Bank Muamalat, Bank of Tokyo-Mitsubishi UFJ, CIMB Islamic, Hong Leong Islamic, Maybank Islamic, RHB Islamic, Affin Bank, Agrobank, Bank Kerjasama Rakyat, EON Capital (merged), Kuwait Finance House, OCBC Al-Amin, Standard Chartered Saadiq

### Segment F: Fintech & Digital Banks (15)
AEON Digital Bank, Boost-RHB Digital Bank, Grab-Singtel Digital Bank, SeaBank Malaysia, TnG Digital Bank, Billplz, Curlec, Eazycall, Favepay, Fundazti, HelloGold, iPay88, Jirnexu (CompareHero, RinggitPlus), Soft Space, Wallets (Boost)

### Segment G: Payment Processors (10)
Alipay Malaysia, Boost, GrabPay, KiplePay, Maybank QRPay, CIMB Clicks Pay, Touch 'n Go eWallet, BigPay, Rakuten Pay, ShopeePay

### Segment H: Credit Cooperatives (8)
Bank Kerjasama Rakyat, Koperasi Tentera Udara, Koperasi ATM, Koperasi PDRM, Koperasi Kerajaan, MBSM, Koperasi Pelaburan Malaysia, Koperasi ASNB

---

**END OF BRIEF**

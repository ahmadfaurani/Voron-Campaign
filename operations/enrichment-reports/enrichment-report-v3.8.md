# VoronDRQ Enrichment Report v3.8
**Classification:** TLP:AMBER
**Date:** 2026-07-14
**Agent:** VoronDRQ Stakeholder Collection Agent
**Session:** CISO Gap-Fill + Foreign Bank Crack

## Executive Summary

This session focused on gap-filling CISO and other missing stakeholder roles for Tier 1 Malaysian banks. Six updates were made across 6 institutions, bringing the enriched database to v3.8 (205 institutions, 42,590 chars).

## Updates Made

### 1. Hong Leong Bank Berhad — CISO Gap-Filled ✅
- **Role:** Chief Information Security Officer (CISO)
- **Name:** Dr. Simon Hoh
- **Source:** TheOrg (theorg.com/org/hong-leong-bank/org-chart/dr-simon-hoh)
- **Confidence:** MEDIUM (65) — TheOrg listing, corroborated by web search
- **Background:** PhD Computer Science (University of Nottingham); prev: AmMetLife, Tokio Marine, BT, ACE Digital/RGE Group
- **Coverage Impact:** 6/7 → 7/7 (100%)

### 2. Hong Leong Islamic Bank Berhad — CISO Gap-Filled ✅
- **Role:** Chief Information Security Officer (CISO)
- **Name:** Dr. Simon Hoh (Group-level)
- **Source:** TheOrg (group-level appointment, Hong Leong Bank)
- **Confidence:** MEDIUM (60) — Group-level inference
- **Coverage Impact:** 6/7 → 7/7 (100%)

### 3. Mizuho Bank (Malaysia) Berhad — CEO Identified (Context) 📋
- **Role:** Executive Director / CEO
- **Name:** Daisuke Ihara
- **Source:** Official — Mizuho Bank (Malaysia) Berhad Profile of Directors PDF (mizuhogroup.com)
- **Confidence:** HIGH (95) — Official corporate filing
- **Details:** Appointed 1 July 2026; Bachelor of Commerce (Doshisha University); Certified AML Specialist
- **Chairman:** Dato' Dr. Zaha Rina binti Zahari (Independent Non-Executive Director, appointed 7 Feb 2022)
- **Note:** CEO is not one of the 7 target roles but provides critical context for future outreach
- **Coverage Impact:** 0/7 → 0/7 (CEO context added, target roles still unfilled)

### 4. HSBC Bank Malaysia Berhad — CEO Confirmed 📋
- **Role:** CEO and Head of Banking
- **Name:** Dato' Omar Siddiq
- **Source:** Official — hsbc.com.my/about-hsbc/leadership/
- **Confidence:** HIGH (95) — Official bank website
- **Note:** CEO confirmed; added to GRC field as context. HSBC still at 5/7 (missing CISO + Internal Audit)
- **Coverage Impact:** 5/7 → 5/7 (context enrichment)

### 5. Citibank Berhad — CEO Confirmed 📋
- **Role:** CEO Citi Malaysia
- **Name:** Vikram Singh
- **Source:** theasianbanker.com (conf 90)
- **Details:** Effective 1 May 2023; Country Lead: Divya Nair; Head of Commercial Bank: Shawn Khong
- **Note:** Added to GRC field as context. Citibank still at 2/7
- **Coverage Impact:** 2/7 → 2/7 (context enrichment)

### 6. Credit Suisse (Malaysia) Berhad — Entity Status Note ⚠️
- **Status:** Credit Suisse acquired by UBS; parent banks merged 31 May 2024
- **Source:** ubs.com press release (30 May 2024)
- **Confidence:** HIGH (85) — Official UBS press release
- **Impact:** Entity likely absorbed/restructured. May need reclassification as UBS Malaysia.
- **Coverage Impact:** 0/7 → 0/7 (status clarified)

## T1 Bank Coverage Summary

| Tier | Coverage | Institutions at 7/7 |
|------|----------|-------------------|
| T1 Local Banks | 85% | Maybank, CIMB, Public Bank (6/7), RHB, Hong Leong, AmBank, Bank Islam |
| T1 Foreign Banks | 43% | OCBC (7/7), UOB (6/7), HSBC (5/7), Stanchart (6/7), Citibank (2/7), BOC (6/7), ICBC (2/7), Credit Suisse (0/7), Mizuho (0/7) |
| T1 Investment Banks | 71% | CIMB IB (7/7), RHB IB (7/7), Maybank IB (3/7), HLIB (6/7), Public IB (6/7) |
| T1 Islamic Banks | 96% | Maybank Islamic, CIMB Islamic, RHB Islamic, AmBank Islamic, HLB Islamic (all 7/7), Public Islamic (6/7) |

**Overall T1 Coverage:** 167/224 (75%)

## Key Findings

1. **CISO is the hardest role to find** — Most banks don't publicly list their CISO. Only Hong Leong Bank's CISO (Dr. Simon Hoh) was confirmed via TheOrg.
2. **Foreign bank local subsidiaries** often don't have dedicated Malaysia CISOs — security is managed at group level (e.g., Standard Chartered's Alvaro Garrido is Singapore-based group CISO).
3. **Credit Suisse Malaysia** is effectively defunct post-UBS merger (31 May 2024). Should be reclassified.
4. **Mizuho Bank Malaysia** has a comprehensive Profile of Directors PDF on their website — confirms CEO Daisuke Ihara but doesn't list the 7 target C-suite roles (only board directors).
5. **HSBC Malaysia** leadership page only shows CEO (Dato' Omar Siddiq). Board of Directors page returns 404.

## Blocked Sources

| Source | Issue |
|--------|-------|
| Firecrawl Agent | Non-functional (generic error) |
| ICBC Malaysia website | Domain www.icbc.com.my doesn't resolve (DNS failure) |
| SimplyWall.st team pages | All return 404 |
| Standard Chartered Malaysia (sc.com.my) | Leadership page under maintenance/404 |
| UOB Malaysia (uob.com.my) | Leadership page inaccessible |
| Citibank Malaysia (citibank.com.my) | DNS resolution failed |
| TheOfficialBoard | Citibank Malaysia page anti-bot blocked |

## Next Steps

- [ ] Continue CISO gap-fill for: Public Bank, UOB, Standard Chartered, Bank of China (all at 6/7)
- [ ] HSBC Malaysia: Find CISO + Head of Internal Audit (5/7 → 7/7)
- [ ] Citibank (2/7) and ICBC (2/7): Major gap-fill needed
- [ ] Mizuho Bank Malaysia: Find 7 target C-suite roles (currently 0/7)
- [ ] Credit Suisse: Reclassify as UBS Malaysia or mark as defunct
- [ ] LinkedIn enrichment for MEDIUM confidence contacts
- [ ] Annual report cross-reference for remaining gaps
- [ ] Begin Segment B (Development Finance) after T1 completion

## File Inventory

| File | Size | Description |
|------|------|-------------|
| prospect-database-enriched-v3.8.csv | 42,590 chars | Latest enriched database (205 institutions) |
| prospect-database-7stakeholders.csv | 6,345 chars | Master CSV (25 institutions, partial) |

---
**Classification:** TLP:AMBER

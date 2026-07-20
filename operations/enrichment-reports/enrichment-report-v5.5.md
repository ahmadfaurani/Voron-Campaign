# VoronDRQ Enrichment Report - v5.5
**Classification:** TLP:AMBER
**Update Date:** 2026-07-18
**Agent:** VoronDRQ Stakeholder Collection Agent (Cron Run)
**Database Version:** v5.5 (enriched)

## Summary

### Coverage Statistics
| Metric | v5.4 | v5.5 | Delta |
|--------|------|------|-------|
| Total Institutions | 205 | 205 | 0 |
| Total Roles Possible | 1,435 | 1,435 | 0 |
| Total Roles Found | 604 | 621 | +17 |
| Overall Coverage | 42.1% | 43.3% | +1.2% |
| Full Coverage (7/7) | 36 | 36 | 0 |
| 6/7 Coverage | 20 | 20 | 0 |
| 5/7 Coverage | 25 | 26 | +1 |
| 4/7 Coverage | 11 | 11 | 0 |
| 3/7 Coverage | 9 | 9 | 0 |
| 2/7 Coverage | 10 | 16 | +6 |
| 1/7 Coverage | 16 | 16 | 0 |
| 0/7 Coverage | 78 | 71 | -7 |

### This Run's Achievements

**+17 new stakeholder roles** across **7 institutions**, plus **2 duplicates flagged**, **3 non-existent entities flagged**, **2 Khazanah gaps confirmed not publicly disclosed**, and **11 institutions researched with 0 target roles** (audit notes added).

**Research Method:** 3 parallel subagents researched 25 institutions across 3 workstreams:
1. **State Dev Corps & GLC-Linked Workstream** (7 institutions): Penang Development Corporation (PDC), Sabah State Financial Corporation, Sarawak State Financial Corporation (SEDC), PNB Income Fund Berhad, Iskandar Waterfront City, Maybank (Khazanah-linked), Khazanah Nasional Berhad
2. **MSBs & Fintech Workstream** (10 institutions): 2C2P, CurrencyFair, G2G Online, I.Destinasi, Money Match, Stripe Malaysia, Jirnexu, KDI Save, Soft Space, JCL Corporation
3. **PayNet & Investment Banks Workstream** (8 institutions): PayNet parent + 6 PayNet products (DuitNow, FPX, JomPAY, Me2U, PayDirect, PayNet Card) + 2 investment banks (Malaysia International Islamic Bank IB, JCL Corporation)

### New Contacts Added (17 roles)

#### 1. Sarawak Economic Development Corporation (SEDC) — 5 NEW roles (0/7 → 5/7)

**Major Discovery:** The DB entry "Sarawak State Financial Corporation (SSFC)" maps to the **Sarawak Economic Development Corporation (SEDC)** — the official entity at sedc.com.my. (The URL sfc.sarawak.gov.my is actually Sarawak Forestry Corporation, a wrong entity.) SEDC publishes a full leadership team and management team page with 18 named executives.

| Role | Name | Title | Source | Conf |
|------|------|-------|--------|------|
| CFO | Encik Leo Lanaiwong | Group Chief Financial Officer | sedc.com.my/leadership-team/ | 95 |
| CRO | Cik Khartini Johari | Head, Group Integrity and Risk Management | sedc.com.my/management-team/ | 95 |
| GRC | Cik Khartini Johari | Head, Group Integrity and Risk Management | sedc.com.my/management-team/ | 95 |
| Internal Audit | Encik Yap Yien Chiang | Head, Group Internal Audit | sedc.com.my/management-team/ | 95 |
| CIO/CTO | Tuan Haji Nor Azlan Husaini | Acting Head, Group Digital & Technology | sedc.com.my/management-team/ | 95 |

**Note:** CRO and GRC functions are combined under one role (Cik Khartini Johari). CISO and a separate Head of Compliance are NOT found as distinct positions at SEDC.

#### 2. PayNet Products — 12 NEW roles (6 institutions × 2 roles each, all 0/7 → 2/7)

**Methodology:** PayNet (Payments Network Malaysia Sdn Bhd) is the parent of 6 product entries in the DB. PayNet's official leadership page (paynet.my/about-us/corporate-profile/leadership.html) lists 8 executives, of which 2 match target roles: CFO Tan Wei Tze and CTO Teh Lip Guan. These 2 are inherited by each PayNet product with confidence 85 (one step below direct official source, since it's an inference from parent to product).

| Product | CFO | CIO/CTO | Conf |
|---------|-----|---------|------|
| DuitNow (by PayNet) | Tan Wei Tze | Teh Lip Guan | 85 |
| FPX (by PayNet) | Tan Wei Tze | Teh Lip Guan | 85 |
| JomPAY (by PayNet) | Tan Wei Tze | Teh Lip Guan | 85 |
| Me2U (by PayNet) | Tan Wei Tze | Teh Lip Guan | 80 (caveat) |
| PayDirect (by PayNet) | Tan Wei Tze | Teh Lip Guan | 85 |
| PayNet Card (by PayNet) | Tan Wei Tze | Teh Lip Guan | 85 |

**Me2U Caveat:** Me2U is NOT listed among PayNet's 10 official named services (IBG, JomPAY, MyDebit, FPX, DirectDebit, DuitNow, DuitNow QR, Shared ATM, Cross-Border Cash Withdrawal, Smart Card). Me2U is more commonly associated with Maybank2u's transfer feature. PayNet leadership is inherited with reduced confidence (80) and an explicit caveat.

### Entities Flagged (Not Enriched — Audit Notes Added)

#### Duplicates (2)

| Institution | Duplicate Of | Reason |
|-------------|--------------|--------|
| Maybank (Khazanah-linked) | Maybank Berhad (7/7 in DB) | Same entity — Khazanah holds ~11.5% of Maybank. Recommend removing row or marking as duplicate. |
| Money Match Sdn Bhd | MoneyMatch Sdn Bhd (4/7 in DB) | Same entity, different spelling. Correct spelling is "MoneyMatch". Recommend removing row or marking as duplicate. |

#### Non-Existent (3)

| Institution | Reason | Verification |
|-------------|--------|--------------|
| PNB Income Fund Berhad | No evidence on pnb.com.my or ASNB fund listing (18 unit trust funds, none named "PNB Income Fund"). PNB Capital and PNB Equity Fund previously confirmed non-existent. | 2 Firecrawl agents + official PNB/ASNB pages |
| Malaysia International Islamic Bank IB | No match on BNM licensed Islamic banks list (12 known entities). No BNM/Bursa/SSM record. Likely mislabel or placeholder. | BNM licensed banks list + Wikipedia "List of banks in Malaysia" |
| JCL Corporation Sdn Bhd | No match on BNM licensed investment banks list (10 known entities). No Bursa/SSM record. Likely mislabel or placeholder. | BNM licensed investment banks list + targeted searches |

### Khazanah Nasional Berhad — 2 Missing Roles Confirmed Not Publicly Disclosed

Khazanah was already at 5/7. The 2 missing roles (CISO and Head of Internal Audit) were researched extensively:
- **CISO:** NOT FOUND. Khazanah's official website lists 22+ executives across Executive Management and Investment Management pages. No CISO or Head of Information Security is listed. The governance page mentions ERM, ORM, BCM frameworks but does not name a CISO. Likely an internal position not publicly disclosed.
- **Head of Internal Audit:** NOT FOUND. The ARC (Audit & Risk Committee) at board level is documented (Chairman: Wong Kang Hwee; Members: Goh Ching Yin, Dr Nungsari Ahmad Radhi) but the Head of Internal Audit is not publicly named. Likely an internal position.

### Researched but 0 Target Roles Found (11 institutions — audit notes added)

These institutions were researched but have 0 of the 7 target roles publicly available. Notes added to CISO cell for audit trail.

| Institution | Key Finding | Source |
|-------------|-------------|--------|
| Penang Development Corporation (PDC) | Entity correction: correct name is PDC (pdc.gov.my). CEO Dato' Abdul Latiff bin Abd Aziz confirmed. Org chart is JPEG image. | pdc.gov.my |
| Sabah State Financial Corporation (SSFC) | Likely Sabah Credit Corporation (SCC). Both ykn.sabah.gov.my and scc.sabah.gov.my DNS-fail. Chairman/CEO from news. | sabahbarunews.com |
| Iskandar Waterfront City (IWCity) | Small Bursa-listed property developer. Full management team confirmed but no target C-suite roles. | iwcity.com.my |
| 2C2P (Malaysia) Sdn Bhd | Parent: Ant Group. Founder Aung Kyaw Moe (non-target). No leadership section on 2c2p.com. | Wikipedia |
| CurrencyFair (Malaysia) Sdn Bhd | Parent: CurrencyFair (Irish). CEO Brett Meyers (non-target). No Malaysia office listed. | currencyfair.com |
| G2G Online (Malaysia) Sdn Bhd | Malaysian MSB licensee. No public leadership information. | — |
| I.Destinasi Sdn Bhd (IDSB) | Malaysian MSB licensee. No public leadership information. | — |
| Jirnexu (M) Sdn Bhd | Operates RinggitPlus/CompareHero. ringgitplus.com DNS-fails. Founders unverified. | LinkedIn |
| KDI Save Sdn Bhd | Fintech under KDI Group. No public leadership information. | — |
| Soft Space Sdn Bhd | CSO & co-founder Chris Leong (non-target). CEO Justin Chew reported but unverified. | softspace.com.my |
| Stripe Payments Malaysia Sdn Bhd | Parent: Stripe Inc. Global CEO Patrick Collison (non-target). No Malaysia-specific leadership. | stripe.com |

### Per-Role Completion (Post v5.5)
| Role | Filled | Total | % | Delta |
|------|--------|-------|---|-------|
| CISO | 62 | 205 | 30.2% | 0 |
| GRC | 81 | 205 | 39.5% | +1 |
| CFO | 113 | 205 | 55.1% | +7 |
| CRO | 94 | 205 | 45.9% | +1 |
| Compliance | 92 | 205 | 44.9% | 0 |
| CIO | 101 | 205 | 49.3% | +7 |
| Internal Audit | 78 | 205 | 38.0% | +1 |

### Coverage Distribution
| Coverage | Count | Change from v5.4 |
|----------|-------|-------------------|
| 0/7 | 71 | -7 |
| 1/7 | 16 | 0 |
| 2/7 | 16 | +6 |
| 3/7 | 9 | 0 |
| 4/7 | 11 | 0 |
| 5/7 | 26 | +1 |
| 6/7 | 20 | 0 |
| 7/7 | 36 | 0 |

### PayNet Leadership Context (Corrected)

The task brief stated PayNet's current group CEO is "Suhaila Kamaruddin (or predecessor Shahdja Farouk)". This is **INCORRECT** per the official PayNet leadership page (paynet.my/about-us/corporate-profile/leadership.html, scraped 2026-07-18):

| Role | Name (Official) | Title |
|------|-----------------|-------|
| CEO | Praveen Rajan | Chief Executive Officer |
| CFO | Tan Wei Tze | Chief Financial Officer |
| CTO | Teh Lip Guan | Chief Technology Officer |
| CCO | Azrul Fakhzan B. Mainor | Chief Commercial Officer |
| CPO | Shafenaz Farouk | Chief People Officer |
| Senior Director | Firdaus Ghani | Senior Director |
| Senior Director | Ken Yon Kian Guan | Senior Director |
| Senior Director | Boey Teck Mein | Senior Director |

**PayNet CISO/CRO/Compliance/Internal Audit/GRC functions EXIST** (per the official Committees page at paynet.my/about-us/corporate-profile/committees.html, which references "CISO Office", "Integrity Unit under Compliance Department", "internal auditors", and "personnel in charge of risk management") but the named role-holders are NOT publicly disclosed at the executive leadership tier. "Head of GRC" is not a distinct PayNet executive title — "GRC" at PayNet refers to the **Group Risk Committee**, a Board-level governance committee.

### Key Sources Used This Run
1. **sedc.com.my/leadership-team/** — Official SEDC Sarawak leadership team (5 C-suite executives)
2. **sedc.com.my/management-team/** — Official SEDC Sarawak management team (13 heads of division)
3. **paynet.my/about-us/corporate-profile/leadership.html** — Official PayNet executive leadership (8 named executives)
4. **paynet.my/about-us/corporate-profile/committees.html** — PayNet governance committees (confirms CISO/Compliance/IA functions exist)
5. **pdc.gov.my** — Penang Development Corporation official site (CEO confirmed; org chart is image-only)
6. **iwcity.com.my** — Iskandar Waterfront City official site (full management team + board)
7. **khazanah.com.my** — Khazanah official leadership (22+ executives; CISO and Head of IA not listed)
8. **pnb.com.my** — PNB/ASNB fund listing (18 funds; none named "PNB Income Fund")
9. **moneymatch.co/about-us** — MoneyMatch official (confirmed duplicate; founders Adrian Tan, Nikki Yeo)
10. **en.wikipedia.org/wiki/Payments_Network_Malaysia** — PayNet context (NOTE: Wikipedia infobox incorrectly lists "Anwar Ibrahim (CEO)" — this is the PM, not PayNet's CEO)

### Verified Gaps (Confirmed Not Publicly Available)

**Institutions with inaccessible/unavailable leadership:**
- PDC Penang: Org chart is JPEG image (not text-extractable); iDirectory uses iframe
- Sabah SCC: Both ykn.sabah.gov.my and scc.sabah.gov.my DNS-fail
- Jirnexu: ringgitplus.com DNS-fails (Cloudflare 1016 error)
- PayNet: CISO/CRO/Compliance/IA names not on official leadership page (functions exist per Committees page)
- Khazanah: CISO and Head of Internal Audit not publicly disclosed (22+ executives listed, but not these 2)

**CISO role rarely publicly listed:**
- SEDC Sarawak (5/7) does NOT have a publicly named CISO — the closest is the Acting Head of Group Digital & Technology
- PayNet (2/7) has a "CISO Office" per the Committees page but does not name the CISO
- Khazanah (5/7) does not publicly name a CISO
- This reinforces the v5.4 finding: CISO is the rarest publicly-listed role (30.2% fill rate)

### Entities Recommended for Removal/Flagging (5 total)

| Institution | Recommendation |
|-------------|----------------|
| PNB Capital Berhad | Non-existent (confirmed v5.4) — remove or flag |
| PNB Equity Fund Berhad | Non-existent (confirmed v5.4) — remove or flag |
| PNB Income Fund Berhad | Non-existent (confirmed v5.5) — remove or flag |
| Malaysia International Islamic Bank IB | Non-existent (confirmed v5.5) — remove or flag |
| JCL Corporation Sdn Bhd | Non-existent (confirmed v5.5) — remove or flag |

### Duplicates Recommended for Removal/Flagging (2 total)

| Institution | Duplicate Of |
|-------------|--------------|
| Maybank (Khazanah-linked) | Maybank Berhad (7/7) |
| Money Match Sdn Bhd | MoneyMatch Sdn Bhd (4/7) |

### Next Steps
- [ ] GitHub push pending
- [ ] Remove or flag 5 non-existent entities from master CSV (clean-up pass)
- [ ] Remove or flag 2 duplicate entities from master CSV (clean-up pass)
- [ ] Continue enrichment of 0/7 institutions (71 remaining — mostly cooperatives and e-money/card products)
- [ ] OCR PDC Penang org chart image for management team names
- [ ] Verify Sabah SCC correct entity name and website domain
- [ ] Annual report cross-reference for institutions with no public leadership pages
- [ ] LinkedIn verification for MEDIUM confidence contacts

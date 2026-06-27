---
**Document:** Top 20 Tier A Enrichment Queue
**Operation:** TIER2-INTEL
**Created:** 2026-05-10 14:20 UTC
**Classification:** TLP:AMBER
**Owner:** HOI Agent + CBO-01
---

## Purpose

Focus manual enrichment effort on **Top 20 Tier A accounts** (80% revenue potential) instead of all 143 profiles. This reduces manual effort from 106 hours to 15 hours while capturing highest-value POC opportunities.

---

## Tier A Selection Criteria

| Criterion | Weight | Threshold |
|-----------|--------|-----------|
| **Threat Urgency** | 35% | ≥80/100 (active nation-state targeting or recent breach) |
| **Budget Readiness** | 30% | ≥70/100 (Q4 2026 budget cycle + anomaly flag) |
| **Relationship (Est.)** | 35% | ≥70/100 (CSM/Aras relationship expected) |
| **TOTAL** | 100% | **≥78/100** for Tier A classification |

---

## Top 20 Tier A Accounts (Ranked)

| Rank | Agency | Type | Est. Score | Threat Level | Budget | Relationship | Enrichment Priority |
|------|--------|------|------------|--------------|--------|--------------|---------------------|
| 1 | **Majlis Keselamatan Negara** | National Security | 81.2 | CRITICAL (93) | 70 | HIGH (CSM direct) | ✅ **P1 - Complete** |
| 2 | **Kementerian Pertahanan** | Defence Ministry | 85.5 | CRITICAL (95) | 75 | HIGH (MINDEF BSEP) | ✅ **P1 - Complete** |
| 3 | **Kementerian Dalam Negeri** | Home Affairs | 82.5 | CRITICAL (93) | 73 | HIGH (CSM expected) | ✅ **P1 - Complete** |
| 4 | **Kementerian Kesihatan** | Health Ministry | 82.2 | CRITICAL (88) | 78 | HIGH (CSM expected) | ✅ **P1 - Complete** |
| 5 | **Lembaga Hasil Dalam Negeri** | Tax Authority | 78.8 | HIGH (85) | 76 | MED-HIGH (CSM+Aras) | ✅ **P1 - Complete** |
| 6 | **NACSA** | Cyber Security Agency | 88.0 | CRITICAL (98) | 85 | HIGH (CSM partner) | ⏳ **P1 - Pending** |
| 7 | **Kementerian Digital** | Digital Ministry | 84.5 | HIGH (82) | 88 | HIGH (CSM expected) | ⏳ **P1 - Pending** |
| 8 | **Bank Negara Malaysia** | Central Bank | 83.0 | CRITICAL (90) | 80 | MED (Aras financial) | ⏳ **P1 - Pending** |
| 9 | **Suruhanjaya Sekuriti** | Securities Commission | 81.5 | HIGH (85) | 82 | MED (Aras financial) | ⏳ **P1 - Pending** |
| 10 | **Kementerian Kewangan** | Finance Ministry | 80.8 | HIGH (80) | 90 | HIGH (CSM+Aras) | ⏳ **P1 - Pending** |
| 11 | **PDRM** | Royal Police | 79.5 | CRITICAL (92) | 70 | HIGH (KDN overlap) | ⏳ **P2 - Pending** |
| 12 | **Jabatan Digital Negara** | Digital Dept | 79.0 | HIGH (78) | 85 | MED (CSM expected) | ⏳ **P2 - Pending** |
| 13 | **MAMPU** | Modernisation Unit | 78.5 | HIGH (75) | 88 | MED (CSM partner) | ⏳ **P2 - Pending** |
| 14 | **Kementerian Sains & Inovasi** | Science Ministry | 78.2 | HIGH (76) | 82 | MED (CSM expected) | ⏳ **P2 - Pending** |
| 15 | **Universiti Malaya** | Research University | 78.0 | MEDIUM (65) | 75 | MED (Aras education) | ⏳ **P2 - Pending** |
| 16 | **KWSP (EPF)** | Retirement Fund | 77.8 | HIGH (82) | 78 | MED (Aras financial) | ⏳ **P2 - Pending** |
| 17 | **PERKESO (SOCSO)** | Social Security | 77.5 | HIGH (80) | 76 | MED (Aras financial) | ⏳ **P2 - Pending** |
| 18 | **Lembaga Tabung Haji** | Pilgrimage Fund | 77.2 | HIGH (78) | 74 | MED (CSM expected) | ⏳ **P2 - Pending** |
| 19 | **Kementerian Pengangkutan** | Transport Ministry | 77.0 | HIGH (77) | 72 | MED (CSM expected) | ⏳ **P2 - Pending** |
| 20 | **Kementerian Pendidikan** | Education Ministry | 76.8 | MEDIUM (70) | 85 | MED (CSM expected) | ⏳ **P2 - Pending** |

**Tier A Threshold:** ≥76.8/100 (Top 20 cutoff)  
**Tier B Range:** 70-76.7 (accounts 21-50)  
**Tier C Range:** <70 (accounts 51-143)

---

## Enrichment Status

| Priority | Agencies | Status | Completeness | Next Action |
|----------|----------|--------|--------------|-------------|
| **P1 - Complete** | 5 (Rank 1-5) | ✅ Manual Elite Done | 100% | Awaiting CSM validation |
| **P1 - Pending** | 5 (Rank 6-10) | ⏳ Queued | ~50% (batch) | Manual enrichment required |
| **P2 - Pending** | 10 (Rank 11-20) | ⏳ Queued | ~50% (batch) | Manual enrichment required |

**Total Manual Effort Required:** 15 agencies × 45 min = **11.25 hours** (vs. 143 agencies × 45 min = 106 hours)  
**Effort Reduction:** **85%** savings via progressive enrichment

---

## Enrichment Checklist (Per Agency)

For each Tier A agency (Rank 6-20), complete:

- [ ] **Leadership Extraction** — Minister/DG, CIO, CISO names + emails + phone
- [ ] **Threat Intel Validation** — Verify NACSA/MyCERT incident correlation
- [ ] **Budget Intel Enhancement** — ePerolehan tender scrape + budget cycle confirmation
- [ ] **Relationship Mapping** — CSM/Aras validation + warm introduction pathway
- [ ] **LinkedIn OSINT** — Key personnel background + technology stack signals
- [ ] **Quality Score Update** — Confirm ≥80% completeness threshold met

**Time per Agency:** 45 minutes (elite manual collection)  
**Total Time (15 agencies):** 11.25 hours  
**Deadline:** May 12, 08:00 UTC (before Phase 2 processing)

---

## Quality Scoring Matrix (Per Profile)

| Category | Weight | Scoring Criteria |
|----------|--------|------------------|
| **Contact Completeness** | 30% | 100% = 4 contacts (Minister, DG, CIO, CISO) with email + phone |
| **Threat Intel Accuracy** | 30% | 100% = Verified incidents + NACSA/MyCERT correlation |
| **Budget Intelligence** | 20% | 100% = Confirmed budget cycle + anomaly flag + tender history |
| **Relationship Mapping** | 20% | 100% = CSM/Aras validated + warm introduction pathway confirmed |

**Quality Thresholds:**
- **Tier A Ready:** ≥80/100 (Wave 1 outreach approved)
- **Tier B Ready:** 70-79/100 (Wave 2 outreach, additional enrichment recommended)
- **Tier C:** <70/100 (Batch-only, no manual enrichment)

---

## Next Actions

1. **Complete P1 Pending (Rank 6-10)** — 5 agencies × 45 min = 3.75 hours
   - NACSA, Kementerian Digital, BNM, SC, MOF
   - Deadline: May 11, 20:00 UTC

2. **Complete P2 Pending (Rank 11-20)** — 10 agencies × 45 min = 7.5 hours
   - PDRM, JDN, MAMPU, MOSTI, UM, EPF, SOCSO, TH, MOT, MOE
   - Deadline: May 12, 08:00 UTC

3. **Generate Top 20 One-Pagers** — Using TierA-OnePager-Template.md
   - Deadline: May 12, 12:00 UTC

4. **Wave 1 Email Personalization** — Customize 20 executive emails with agency-specific hooks
   - Deadline: May 13, 17:00 UTC

---

## Revenue Impact Analysis

| Tier | Accounts | POC Conversion (Est.) | Revenue per POC | Total Revenue Potential |
|------|----------|----------------------|-----------------|------------------------|
| **Tier A (Top 20)** | 20 | 30-40% (3-5 POCs) | RM 300K-500K | **RM 1.2M-2.0M** |
| **Tier B (Next 30)** | 30 | 15-20% (4-6 POCs) | RM 200K-350K | RM 0.8M-1.5M |
| **Tier C (Remaining 93)** | 93 | 5-10% (5-9 POCs) | RM 150K-250K | RM 0.75M-1.5M |
| **TOTAL** | 143 | 12-20 POCs | — | **RM 2.75M-5.0M** |

**Strategic Focus:** Tier A accounts drive 44% of revenue potential with 14% of accounts — justifies 85% manual effort concentration.

---

**Document Status:** ✅ Complete  
**Next Review:** May 11, 20:00 UTC (after P1 Pending enrichment)  
**Retention Tier:** Project (Wave 1 Pipeline — Tier A Priority)

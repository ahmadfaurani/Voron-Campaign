---
**Agency:** [Agency Name]
**Profile ID:** TIER2-[XXX]-[YYYYMMDD]
**Type:** Federal / State / Statutory Body
**Collection Date:** [YYYY-MM-DD HH:MM UTC]
**Collector:** HOI Agent (Automated OSINT)
**Confidence:** High / Medium / Low
**Classification:** TLP:AMBER
**Operation:** TIER2-INTEL
---

## 1. Agency Profile

| Field | Value | Confidence |
|-------|-------|------------|
| **Full Name** | [Official agency name] | High |
| **Short Name** | [Common abbreviation] | High |
| **Type** | Federal Department / State Agency / Statutory Body | High |
| **Parent Ministry** | [Ministry name, if applicable] | Medium |
| **Mandate** | [1-2 sentence description of core function] | High |
| **Website** | [Official URL] | High |
| **HQ Address** | [Physical address] | Medium |
| **Employee Count** | [Approximate range] | Low |
| **Established** | [Year founded] | Low |

---

## 2. Leadership + Contact Intelligence

| Role | Name | Title | Email | Phone | Confidence |
|------|------|-------|-------|-------|------------|
| **Director-General** | [Name] | [Title] | [Email] | [Phone] | High/Med/Low |
| **CIO / IT Director** | [Name] | [Title] | [Email] | [Phone] | High/Med/Low |
| **CISO / Security Head** | [Name] | [Title] | [Email] | [Phone] | High/Med/Low |
| **Procurement Head** | [Name] | [Title] | [Email] | [Phone] | Low |

**Email Pattern:** `[firstname].[lastname]@[domain].gov.my` (inferred)  
**Phone Pattern:** `+603-XXXX-XXXX` (HQ) / `+60X-XXX-XXXX` (state)

**Source Notes:**
- [ ] LinkedIn company page verified
- [ ] Official portal "About Us" page scraped
- [ ] Government directory confirmed
- [ ] Social media cross-validated

---

## 3. Threat Intelligence Profile

| Indicator | Status | Details | Confidence |
|-----------|--------|---------|------------|
| **Recent Breach (12 months)** | Yes / No | [Date, type, impact if known] | High/Med/Low |
| **Nation-State Targeting** | High / Medium / Low | [APT group name if known] | Medium |
| **Sector Threat Level** | High / Medium / Low | [Industry-specific risks] | High |
| **MyCERT Incidents** | [Count] reported | [Types: data breach, ransomware, etc.] | High |
| **NACSA Investigation** | Yes / No / Unknown | [Case reference if known] | Medium |
| **Compliance Deadlines** | [PDPA/NACSA Act dates] | [Specific requirements] | High |
| **Digital Transformation Projects** | [Project names] | [RPSA 2026-2030 initiatives] | Medium |

**Threat Score:** XX/100  
**Calculation:** (Breach History × 0.30) + (Targeting Level × 0.35) + (Compliance Urgency × 0.35)

**Threat Hooks for POC:**
1. [Specific threat intel to reference in outreach]
2. [Compliance deadline pressure point]
3. [Sector-specific risk narrative]

---

## 4. Budget + Vendor Intelligence

| Indicator | Status | Details | Confidence |
|-----------|--------|---------|------------|
| **Current Security Vendor** | [Vendor name / Unknown] | [Contract type] | Low/Med |
| **Contract Expiry** | Q[1-4] YYYY / Unknown | [Service category] | Low |
| **Budget Cycle** | Q1 / Q2 / Q3 / Q4 2026 | [Fiscal year pattern] | Medium |
| **Budget Anomaly Flag** | Yes / No | [Emergency funding detected] | Medium |
| **Recent Tenders (Security)** | [Count] in last 12 months | [ePerolehan references] | High |
| **Vendor Lock-in Level** | High / Medium / Low | [Proprietary systems, integration depth] | Low |

**Budget Score:** XX/100  
**Calculation:** (Cycle Timing × 0.40) + (Anomaly Flag × 0.30) + (Vendor Expiry × 0.30)

**Budget Hooks for POC:**
1. [Budget cycle timing for outreach]
2. [Contract expiry opportunity]
3. [Emergency funding angle if applicable]

---

## 5. Relationship Intelligence (CSM/Aras Input)

| Source | Relationship Level | Last Engagement | Contact Warmth | Notes |
|--------|-------------------|-----------------|----------------|-------|
| **CSM** | High / Medium / Low / Unknown | [Date] | Warm / Cold / Unknown | [Engagement type] |
| **Aras** | Pipeline / Past POC / Active / Cold | [Date] | Warm / Cold / Unknown | [Pipeline status] |
| **MINDEF Network** | Yes / No / Unknown | [Date] | Warm Introduction Available | [Contact name] |

**Relationship Score:** XX/100  
**Calculation:** (CSM Level × 0.50) + (Aras Status × 0.30) + (MINDEF Intro × 0.20)

**Warm Introduction Pathway:**
- [ ] CSM direct introduction available
- [ ] Aras existing relationship
- [ ] MINDEF BSEP network contact
- [ ] Cold outreach only

---

## 6. Scoring Summary (100-Point Matrix)

| Criterion | Weight | Score (0-100) | Weighted Score |
|-----------|--------|---------------|----------------|
| **Relationship Warmth** | 35% | XX | XX.X |
| **Threat Urgency** | 35% | XX | XX.X |
| **Budget Readiness** | 30% | XX | XX.X |
| **TOTAL** | 100% | — | **XX.X / 100** |

**Tier Classification:**
- **Tier A (Top 20):** Score ≥ 75
- **Tier B (Next 40):** Score 50-74
- **Tier C (Remaining 40):** Score < 50

**Priority Rank:** #XX of 100

---

## 7. Sources

| Source | URL | Access Date | Data Type | Confidence |
|--------|-----|-------------|-----------|------------|
| [Source 1] | [URL] | [Date] | Leadership, Contact | High |
| [Source 2] | [URL] | [Date] | Threat Intel | High |
| [Source 3] | [URL] | [Date] | Budget, Vendor | Medium |
| [CSM Validation] | [Internal] | [Pending/Date] | Relationship | [Pending/High] |

---

## 8. Evidence Chain

| Action | Timestamp | Collector | Status |
|--------|-----------|-----------|--------|
| **Profile Created** | [YYYY-MM-DD HH:MM UTC] | HOI-Agent | Complete |
| **Leadership Extracted** | [YYYY-MM-DD HH:MM UTC] | HOI-Agent | Complete |
| **Threat Intel Correlated** | [YYYY-MM-DD HH:MM UTC] | HOI-Agent | Complete |
| **Budget Analysis** | [YYYY-MM-DD HH:MM UTC] | HOI-Agent | Complete |
| **CSM Validation** | [Pending / YYYY-MM-DD HH:MM UTC] | Zaharudin | Pending / Complete |
| **Final Review** | [YYYY-MM-DD HH:MM UTC] | HOI-Agent | Pending |

**Storage Path:** `/home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/evidence/Agency-Profiles/[XXX]-[AgencyName]-Profile.md`  
**Evidence ID:** TIER2-AGY-[XXX]  
**Retention Tier:** Project (Wave 1 Pipeline)

---

## 9. Outreach Readiness

| Check | Status | Notes |
|-------|--------|-------|
| **Contact Info Complete (≥80%)** | ✅ Yes / ❌ No | [Missing fields if any] |
| **Threat Intel Validated** | ✅ Yes / ❌ No | [CSM confirmation if needed] |
| **Budget Intel Sufficient** | ✅ Yes / ❌ No | [Gaps if any] |
| **Relationship Pathway Clear** | ✅ Yes / ❌ No | [Warm intro available] |
| **Ready for Wave 1** | ✅ Yes / ❌ No | [Blockers if any] |

**Recommended Outreach Track:** Executive / Technical / Hybrid  
**Recommended Timing:** Week 1 / Week 2 / Week 3 (Wave 1 cycle)  
**Recommended Hook:** [Threat intel / Compliance / Budget / Reference]

---

**Profile Status:** ⏳ In Progress / ✅ Complete / ⚠️ Incomplete (Awaiting CSM)  
**Last Updated:** [YYYY-MM-DD HH:MM UTC]  
**Next Review:** [YYYY-MM-DD HH:MM UTC]

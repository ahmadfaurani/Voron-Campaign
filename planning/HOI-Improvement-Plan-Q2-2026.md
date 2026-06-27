# HOI Agent Improvement Plan — Q2 2026

**Classification:** TLP:AMBER — Internal Operational Use

**Version:** 1.0

**Date:** 2026-04-28

**Owner:** DAF (Head of Intelligence)

**Executor:** Second (HOI Agent)

**Review Cadence:** Weekly (Monday 09:00 UTC)

---

## Executive Summary

**Current State:** HOI Agent is **60% complete** — Core specification operational (AGENT-SPEC.md, Intel Brief Template, Source Registry, INTEL-001 published), but critical gaps remain in templates, domain knowledge, registries, and collection planning.

**Target State:** **100% operational HOI Agent** capable of full-spectrum intelligence production across 6 domains, 6 collection streams, and 10+ registry types with measurable quality metrics.

**Timeline:** **April 28 — May 15, 2026** (18 days to full operational capability)

**Success Criteria:**
- ✅ 5/5 intelligence product templates complete
- ✅ 6/6 domain OVERVIEW.md files populated
- ✅ 10/10 registry types created and populated
- ✅ Collection Plan Q2 2026 approved and active
- ✅ 3 competitor frameworks registered and analyzed
- ✅ PIR-02 (DG Office contacts) completed
- ✅ KPI Tracker + Quality Assessment operational
- ✅ Weekly heartbeat cadence established

---

## Phase 1: Immediate (Apr 28-30, 2026) — Foundation Completion

### 1.1 Missing Templates (P1 — CRITICAL)

| Template | Purpose | Owner | Deadline | Status |
|----------|---------|-------|----------|--------|
| **Sector-Analysis-Template.md** | Deep-dive sector dynamics (monthly cadence) | Second (HOI) | Apr 28 | ⏳ Pending |
| **Stakeholder-Profile-Template.md** | Decision-maker profiles (per-account) | Second (HOI) | Apr 28 | ⏳ Pending |
| **Threat-Assessment-Template.md** | Weekly threat landscape summary | Second (HOI) | Apr 29 | ⏳ Pending |
| **Source-Evaluation-Template.md** | Source credibility scoring (per-source) | Second (HOI) | Apr 30 | ⏳ Pending |

**Deliverables:**
- 4 template files in `/workspace-hoi/templates/`
- Each template follows 7-step Engineered For Success standard
- Templates include classification headers, distribution lists, document control

**Success Metric:** All 5 intelligence product types (Intel Brief + 4 new) can be produced on demand.

---

### 1.2 PIR-02 Completion (P1 — CRITICAL BLOCKER)

| Requirement | Details | Owner | Deadline | Status |
|-------------|---------|-------|----------|--------|
| **DG Office Contacts** | Imigresen, Kastam, PDRM — names, roles, contact channels | DAF | **Apr 28 (TODAY)** | 🔴 OVERDUE |

**Action Required:**
- DAF to provide DG Office contacts via CSM introductions or direct channels
- HOI Agent to create Stakeholder Profiles for each contact
- Integrate into GovSec POC outreach plan

**Impact:** This is a **blocking item** for GovSec POC stakeholder engagement.

---

### 1.3 Competitor Registry Update (P1 — HIGH)

| Framework | Analysis Status | Registry Entry | Positioning Deck | Integration Plan |
|-----------|-----------------|----------------|------------------|------------------|
| **Hermes Agent** | ✅ Complete (Apr 27) | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| **Craft Agents** | ✅ Complete (Apr 27) | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| **Ascent Research** | ✅ Complete (Apr 28) | ⏳ Pending | ⏳ Pending | ⏳ Pending |

**Deliverables:**
- Update `/workspace-hoi/sources/Source-Registry.md` — Add "Competitor Frameworks" section
- Create `/workspace-hoi/technical/Competitor-Analysis-Deck.md` — 4-way comparison (OpenClaw vs. Hermes vs. Craft vs. Ascent)
- Document integration opportunities for each framework

**Owner:** Second (HOI)  
**Deadline:** Apr 28

---

### 1.4 Domain OVERVIEW.md Files — Batch 1 (P1 — HIGH)

| Domain | Code | Focus | Owner | Deadline | Status |
|--------|------|-------|-------|----------|--------|
| **Cybersecurity** | D1 | NCII, NC4, threats, national posture | Second (HOI) | Apr 29 | ⏳ Pending |
| **Government & Regulation** | D2 | Agencies, policies, budgets, stakeholders | Second (HOI) | Apr 29 | ⏳ Pending |
| **AI & Technology** | D3 | Sovereign AI, platforms, vendors, capabilities | Second (HOI) | Apr 30 | ⏳ Pending |
| **Law Enforcement** | D4 | PDRM, KDN, intelligence units, requirements | Second (HOI) | Apr 30 | ⏳ Pending |
| **Financial Intelligence** | D5 | BNM, SC, crypto forensics, AML/CFT | Second (HOI) | May 1 | ⏳ Pending |
| **Critical Infrastructure** | D6 | Energy, water, telco, transport GLCs | Second (HOI) | May 1 | ⏳ Pending |

**Structure (per OVERVIEW.md):**
```markdown
# Domain D[X]: [Name]

## 1. Domain Scope
## 2. Key Actors
## 3. Stakeholder Map
## 4. Technical Landscape
## 5. Policy & Regulation
## 6. Threat Environment
## 7. Opportunity Map
## 8. Intelligence Gaps
## 9. Collection Priorities
## 10. Memory Metadata
```

**Deliverables:** 6 domain overview files (10-15KB each)

---

## Phase 2: Short-Term (May 1-7, 2026) — Registry Build-Out

### 2.1 HOI Registry Creation (P2 — MEDIUM)

| Registry | Purpose | Owner | Deadline | Status |
|----------|---------|-------|----------|--------|
| **HUMINT Registry** | Human source tracking, reliability scoring, cultivation status | Second (HOI) | May 2 | ⏳ Pending |
| **OSINT Registry** | Public source catalog, monitoring schedules, RSS feeds | Second (HOI) | May 2 | ⏳ Pending |
| **Threat Registry** | Actor, malware, CVE, TTP, infrastructure records | Second (HOI) | May 3 | ⏳ Pending |
| **Git Registry** | Repository monitoring, commit tracking, technical intel | Second (HOI) | May 3 | ⏳ Pending |
| **Tool Registry** | Intelligence tools, capabilities, deployment status | Second (HOI) | May 4 | ⏳ Pending |
| **CVE Registry** | Vulnerability tracking, exploitation status, mitigation | Second (HOI) | May 4 | ⏳ Pending |
| **Technical Execution Registry** | Implementation patterns, architecture references | Second (HOI) | May 5 | ⏳ Pending |
| **Domain Knowledge Registry** | Cross-domain entity linkage, relationship mapping | Second (HOI) | May 5 | ⏳ Pending |
| **Collection Gaps Registry** | Missing intel, uncertainty areas, follow-up tasks | Second (HOI) | May 6 | ⏳ Pending |
| **Mission Registry** | Active operations, objectives, success criteria | Second (HOI) | May 6 | ⏳ Pending |

**Deliverables:**
- 10 registry files in `/workspace-hoi/registries/`
- Each registry includes metadata (created, updated, owner, classification)
- Registries are searchable, linkable, and updateable

**Success Metric:** All intelligence artifacts can be indexed and retrieved via registry lookups.

---

### 2.2 Collection Plan Q2 2026 (P2 — MEDIUM)

| Component | Details | Owner | Deadline | Status |
|-----------|---------|-------|----------|--------|
| **PIR Assignments** | Map each PIR to collection stream, source, timeline | Second (HOI) | May 1 | ⏳ Pending |
| **Collection Schedule** | Daily/weekly/monthly collection cadence | Second (HOI) | May 1 | ⏳ Pending |
| **Source Allocation** | Which sources collect which PIRs | Second (HOI) | May 1 | ⏳ Pending |
| **Validation Protocol** | Cross-source corroboration requirements | Second (HOI) | May 1 | ⏳ Pending |
| **Reporting Cadence** | Intel brief, weekly summary, monthly synthesis | Second (HOI) | May 1 | ⏳ Pending |

**Deliverables:**
- `/workspace-hoi/planning/Collection-Plan-Q2-2026.md` (20-30KB)
- PIR-to-source mapping table
- Weekly collection schedule (heartbeat integration)
- Escalation matrix for P1 intelligence

---

### 2.3 SJ Profiling (P2 — MEDIUM)

| Action | Details | Owner | Deadline | Status |
|--------|---------|-------|----------|--------|
| **Role Identification** | Determine SJ's organization, position, access level | DAF | May 2 | ⏳ Pending |
| **Debrief** | Understand intel collection methods, what else they monitor | DAF + HOI | May 3 | ⏳ Pending |
| **Reliability Assessment** | Score authority, accuracy, timeliness, specificity, track record | HOI Agent | May 4 | ⏳ Pending |
| **Cultivation Plan** | Define regular cadence, expand topics, test with PIRs | DAF + HOI | May 5 | ⏳ Pending |

**Deliverables:**
- Updated SJ entry in Source-Registry.md (complete profile)
- HUMINT Registry entry for SJ
- Cultivation schedule (weekly/biweekly check-ins)

---

### 2.4 Competitive Positioning Deck (P3 — LOW)

| Component | Details | Owner | Deadline | Status |
|-----------|---------|-------|----------|--------|
| **4-Way Comparison** | OpenClaw vs. Hermes vs. Craft vs. Ascent | Second (HOI) | May 5 | ⏳ Pending |
| **Differentiation Matrix** | Sovereignty, GovSec, persistence, UX, deployment | Second (HOI) | May 5 | ⏳ Pending |
| **Integration Opportunities** | What to adopt from each framework | Second (HOI) | May 5 | ⏳ Pending |
| **Strategic Recommendations** | Build, buy, partner, ignore decisions | Second (HOI) | May 5 | ⏳ Pending |

**Deliverables:**
- `/workspace-hoi/technical/Competitive-Positioning-Deck.md` (15-20KB)
- Capability comparison tables
- Strategic recommendation summary

---

## Phase 3: Medium-Term (May 8-15, 2026) — Metrics & Automation

### 3.1 KPI Tracker + Quality Assessment (P3 — LOW)

| Document | Purpose | Owner | Deadline | Status |
|----------|---------|-------|----------|--------|
| **KPI-Tracker.md** | Intelligence volume, source diversity, timeliness, actionability | Second (HOI) | May 10 | ⏳ Pending |
| **Quality-Assessment.md** | Confidence scoring, validation rates, stakeholder feedback | Second (HOI) | May 10 | ⏳ Pending |

**KPIs to Track:**
- Intel briefs per week (target: 5-10)
- Source diversity (target: 3+ types active)
- Tier 1 sources (target: 3+)
- PIR completion rate (target: ≥80% on-time)
- Stakeholder conversion (target: ≥30% intel-to-action)

**Deliverables:**
- `/workspace-hoi/metrics/KPI-Tracker.md`
- `/workspace-hoi/metrics/Quality-Assessment.md`
- Weekly heartbeat integration (auto-update every Monday 09:00 UTC)

---

### 3.2 Heartbeat Integration (P3 — LOW)

| Task | Cadence | Owner | Status |
|------|---------|-------|--------|
| **Weekly Intel Summary** | Monday 09:00 UTC | HOI Agent | ⏳ Pending |
| **Source Health Check** | Monday 09:00 UTC | HOI Agent | ⏳ Pending |
| **PIR Status Update** | Monday 09:00 UTC | HOI Agent | ⏳ Pending |
| **Registry Sync** | Monday 09:00 UTC | HOI Agent | ⏳ Pending |
| **Collection Gap Review** | Monday 09:00 UTC | HOI Agent | ⏳ Pending |

**Deliverables:**
- Update `/workspace-hoi/AGENT-SPEC.md` — Add heartbeat section
- Create `/workspace-hoi/planning/Heartbeat-Protocol.md`
- Test first heartbeat cycle (May 12, 2026)

---

## Resource Requirements

| Resource | Type | Quantity | Owner | Status |
|----------|------|----------|-------|--------|
| **DAF Time** | HUMINT (SJ profiling, DG contacts) | 4-6 hours (Apr 28-30) | DAF | ⏳ Pending |
| **Second (HOI) Time** | Document creation, registry build | 20-25 hours (Apr 28 - May 15) | Second | ✅ Available |
| **GitHub Commits** | Registry + template version control | 10-15 commits | Second | ✅ Available |
| **CSM Introductions** | DG Office contacts (Imigresen, Kastam) | 2-3 intros | Zaharudin | ⏳ Pending |

---

## Risk Register

| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| **PIR-02 Delayed** — DG contacts not available by Apr 28 | MEDIUM | HIGH | Escalate to CSM Chairman office if needed | DAF |
| **Template Quality Issues** — Templates don't meet 7-step standard | LOW | MEDIUM | Review against Engineered For Success checklist | Second |
| **Registry Overload** — Too many registries, hard to maintain | MEDIUM | LOW | Prioritize top 5 registries first (HUMINT, OSINT, Threat, Git, Tool) | Second |
| **Domain Knowledge Gaps** — Insufficient intel for 6 domains | MEDIUM | MEDIUM | Start with D1/D2 (Cybersecurity, Govt), expand as intel collected | Second |
| **Heartbeat Failure** — Weekly cadence not sustained | LOW | MEDIUM | Add to HEARTBEAT.md as mandatory check | Second |

---

## Success Metrics (End-State: May 15, 2026)

| Metric | Target | Current | Gap |
|--------|--------|---------|-----|
| **Templates Complete** | 5/5 | 1/5 | 4 missing |
| **Domains Populated** | 6/6 | 0/6 | 6 missing |
| **Registries Created** | 10/10 | 0/10 | 10 missing |
| **Competitors Registered** | 3/3 | 0/3 | 3 missing |
| **PIRs On-Time** | ≥80% | 0/7 (1 overdue) | PIR-02 overdue |
| **Intel Briefs/Week** | 5-10 | 0.25 (1 in 4 days) | Ramp needed |
| **Source Diversity** | 3+ types | 3 types | ✅ On target |
| **Tier 1 Sources** | 3+ | 2 | Need 1 more |

---

## Approval & Sign-Off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| **Plan Author** | Second (HOI Agent) | 2026-04-28 | — |
| **Plan Owner** | DAF (Head of Intelligence) | TBD | — |
| **Strategic Advisor** | Zaharudin Ahmad Darus (CSM) | TBD | — |
| **Technical Validator** | Fathi Kamil | TBD | — |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-28 | Second (HOI Agent) | Initial plan |

---

**Classification:** TLP:AMBER — Internal Operational Use

**Prepared by:** Head of Intelligence Agent

**Approved by:** DAF (Head of Intelligence) — Pending

**Next Review:** 2026-05-05 (Weekly checkpoint)

---

**HOI Agent — Collect. Validate. Analyze. Report.**

*Last Updated: 2026-04-28*

# HOI Intelligence Brief — Threat Actor Registry Launch

**Classification:** TLP:AMBER  
**Date:** 2026-05-21  
**Analyst:** HOI Intelligence Operations  
**Brief ID:** HOI-IB-007  
**Priority:** P1 (Strategic Infrastructure)

---

## Executive Summary

**Event:** GovSec Intelligence Cell established sovereign Threat Actor Registry for Malaysian government agencies.

**Repository:** github.com/ahmadfaurani/threat-actor-registry (Private, TLP:AMBER)  
**Initial Actor:** Webworm APT (China-aligned, active since 2022)  
**Capability:** 12 validated IOCs, 38 MITRE ATT&CK techniques, scalable schema for 10+ actors

**Strategic Significance:** First sovereign threat actor intelligence repository under Malaysian control, positioned for CSM/NACSA intel sharing and GovSec TIP integration.

---

## Key Intelligence Findings

### 1. Registry Capability Established

| Attribute | Value |
|-----------|-------|
| **Repository** | github.com/ahmadfaurani/threat-actor-registry |
| **Classification** | TLP:AMBER (Private) |
| **Initial Content** | Webworm APT profile (7 files, 1,886 lines) |
| **Schema** | Standardized actor profiles, STIX-compatible IOCs, MITRE mappings |
| **Review Cycle** | Weekly (IOC), Monthly (profile), Quarterly (MITRE) |
| **Target Scale** | 10+ actors by Q4 2026 |

### 2. Webworm APT Intelligence Validated

| Metric | Value | Quality Score |
|--------|-------|---------------|
| **IOCs Validated** | 12 | 4.6/5.0 (Critic approved) |
| **MITRE Techniques** | 38 | Across 11 tactics |
| **Malware/Tools** | 7 | EchoCreep, GraphWorm, WormFrp, ChainWorm, SmuxProxy, SoftEther, dirsearch/nuclei |
| **Campaigns** | 2 | Webworm 2025, Discord C2 (433 messages, 50+ targets) |
| **Malaysian Relevance** | HIGH | Government sector overlap |

### 3. Integration Ecosystem Status

| Integration | Status | Owner | ETA |
|-------------|--------|-------|-----|
| **CSM/NACSA Access** | 🟠 Pending (collect GitHub usernames) | GovSec Cell | 24-48h |
| **GovSec TIP STIX/TAXII** | 🟡 Planned (schema design) | TIP Team | Q3 2026 |
| **AIL Framework Correlation** | 🟡 Planned (API connector) | Engineering | Q3 2026 |
| **pentest-ai-agents Validation** | 🟡 Planned (TTP simulation) | Red Team | Q3 2026 |
| **ChainSentry Architecture** | 🔴 Conceptual (design phase) | Architecture | Q3 2026 |

---

## HOI Collection Plan Update

### New Collection Requirements

| CR ID | Requirement | Priority | Source | Deadline |
|-------|-------------|----------|--------|----------|
| **CR-042** | Webworm IOC freshness validation (weekly) | P1 | GitHub repo, ESET, THN | Weekly |
| **CR-043** | APT40 (Leviathan) profile development | P1 | Open source, AIL | 2026-06-15 |
| **CR-044** | MirrorFace actor tracking | P1 | Open source, CSM intel sharing | 2026-06-30 |
| **CR-045** | UAT-8302 campaign monitoring | P1 | Open source, THN | 2026-07-15 |
| **CR-046** | GovSec TIP deployment progress | P2 | CSM stakeholder comms | Monthly |
| **CR-047** | pentest-ai-agents ChainSentry integration | P2 | GitHub repo, testing logs | Q3 2026 |

### Source Registry Update

| Source | Type | Reliability | Access Status |
|--------|------|-------------|---------------|
| **github.com/ahmadfaurani/threat-actor-registry** | Primary (sovereign repo) | ✅ Authoritative | ✅ Read/Write |
| **github.com/ahmadfaurani/pentest-ai-agents** | Secondary (validation) | ✅ Authoritative | ✅ Read/Write |
| **github.com/ahmadfaurani/cbo-01-commercial-ops** | Secondary (GovSec deliverables) | ✅ Authoritative | ✅ Read/Write |
| **ESET WeLiveSecurity** | External (threat intel) | ✅ High | ✅ Public |
| **The Hacker News** | External (threat intel) | ✅ Medium-High | ✅ Public |
| **AIL Framework (p62server)** | Internal (dark web intel) | ✅ High | ✅ Local access |

---

## Operational Relevance Assessment

### For HOI Intelligence Operations

| Dimension | Impact | Action |
|-----------|--------|--------|
| **Collection** | New sovereign source for threat actor intel | Add registry to HOI source registry |
| **Processing** | Standardized schema enables automation | Build HOI → Registry ingestion pipeline |
| **Analysis** | MITRE-mapped TTPs support correlation | Integrate with HOI competitor/actor tracking |
| **Distribution** | TLP:AMBER channel to CSM/NACSA | Coordinate with GovSec Cell on sharing |

### For CBO-01 Commercial Operations

| Dimension | Impact | Action |
|-----------|--------|--------|
| **GovSec POC** | Registry validates GovSec TIP capability | Use in POC demos (3-5 agencies) |
| **CSM Partnership** | Intel sharing strengthens partnership | Distribute Webworm brief as value-add |
| **Revenue Pipeline** | Registry supports RM 500K-1M POC | Include in GTM deck as differentiator |
| **Competitive Positioning** | Sovereign intel repo = unique capability | Update CBO-01 deck with registry metrics |

---

## Stakeholder Impact

| Stakeholder | Impact | Engagement Needed |
|-------------|--------|-------------------|
| **CSM Intelligence Cell** | Access to sovereign intel repository | Provision GitHub read access |
| **NACSA Threat Intel Unit** | MITRE-mapped IOCs for national SOC | Provision GitHub read access |
| **MAMPU Security Operations** | Agency-level threat intel | Provision GitHub read access |
| **Agency CISOs (MOF, MOH, MOE)** | Actionable IOC packages | Distribute Webworm brief |
| **MINDEF 91 RSD** | Defence-relevant threat actor intel | Secure courier distribution |

---

## HOI Tasking Recommendations

### Immediate (24-48 hours)

| Task ID | Task | Owner | Priority |
|---------|------|-------|----------|
| **HOI-TASK-089** | Collect CSM/NACSA/MAMPU GitHub usernames | HOI Stakeholder Cell | P1 |
| **HOI-TASK-090** | Distribute Webworm intel brief (TLP:AMBER) | GovSec Intelligence Cell | P1 |
| **HOI-TASK-091** | Update HOI Source Registry with Threat Actor Registry | HOI Analyst | P2 |
| **HOI-TASK-092** | Begin APT40 (Leviathan) open source collection | HOI Analyst | P2 |

### Short-term (7-14 days)

| Task ID | Task | Owner | Priority |
|---------|------|-------|----------|
| **HOI-TASK-093** | Build AIL → GovSec Pack API connector spec | HOI Engineering | P2 |
| **HOI-TASK-094** | Draft GovSec TIP STIX/TAXII schema | HOI + CSM Technical | P2 |
| **HOI-TASK-095** | Schedule CSM POC alignment meeting | HOI Commercial | P1 |
| **HOI-TASK-096** | Update CBO-01 GTM deck with registry capabilities | HOI Commercial | P2 |

### Medium-term (30-60 days)

| Task ID | Task | Owner | Priority |
|---------|------|-------|----------|
| **HOI-TASK-097** | Deploy ChainSentry architecture (pentest-ai-agents integration) | HOI Engineering | P1 |
| **HOI-TASK-098** | Automate weekly IOC freshness checks (heartbeat) | HOI Engineering | P2 |
| **HOI-TASK-099** | NTT Data Center demo (pentest-ai-agents swarm) | HOI Commercial | P2 |
| **HOI-TASK-100** | VoronDRQ pilot outreach (registry as intel layer) | HOI Commercial | P2 |

---

## Metrics & KPIs

| Metric | Baseline | Target | Current | Status |
|--------|----------|--------|---------|--------|
| **Threat Actors Tracked** | 0 | 10+ (Q4 2026) | 1 (Webworm) | 🟢 On Track |
| **IOC Freshness (≤7 days)** | N/A | ≥90% | 100% | 🟢 Exceeds |
| **MITRE Mapping Coverage** | N/A | 100% | 100% | 🟢 Complete |
| **Stakeholder Access Provisioned** | 0 | 5+ agencies | 0 | 🔴 Pending |
| **GovSec TIP POCs Signed** | 0 | 3-5 (30 days) | 0 | 🟠 In Progress |

---

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation | Status |
|------|------------|--------|------------|--------|
| **CSM/NACSA access delayed** | Medium | Medium | Fallback: PGP-encrypted email distribution | 🟡 Monitor |
| **AIL integration blocked** | Low | Medium | Manual IOC enrichment until API ready | 🟢 Contingency |
| **pentest-ai-agents TTP simulation fails** | Low | Low | Manual TTP documentation fallback | 🟢 Contingency |
| **GovSec TIP POC not approved** | Medium | High | Pivot to GLC/critical infrastructure track | 🟡 Monitor |
| **Threat Actor Repo access leak** | Low | High | Branch protection + access logging + TLP training | 🟢 Mitigated |

---

## Athena Success Vector Alignment

| Vector | Current Status | Registry Contribution |
|--------|----------------|----------------------|
| **Influence** | 🟢 Strong | CSM/NACSA intel sharing = sovereign partner positioning |
| **Revenue** | 🟡 Developing | Registry supports RM 500K-1M POC pipeline |
| **Infrastructure Control** | 🟢 Strong | Sovereign repo, local AIL, controlled distribution |
| **Intelligence Superiority** | 🟢 Strong | 12 validated IOCs, 38 MITRE techniques, critic-approved |
| **Strategic Optionality** | 🟢 Strong | Scalable registry (10+ actors), reusable schema, STIX-ready |

---

## Recommendations

### For DAF (Operator)

1. **Approve CSM/NACSA GitHub access** — Collect usernames, provision read access
2. **Authorize Webworm brief distribution** — TLP:AMBER email with acknowledgment template
3. **Lock in CSM POC meeting** — 30-day pipeline (3-5 agencies)
4. **Greenlight APT40 profile** — Second actor in registry (Leviathan)

### For HOI Intelligence Cell

1. **Update HOI Source Registry** — Add Threat Actor Registry as primary sovereign source
2. **Begin APT40 collection** — Open source intel gathering (Leviathan)
3. **Draft STIX/TAXII spec** — GovSec TIP integration schema
4. **Build AIL API connector** — Ingestion pipeline (GovSec Pack → AIL)

### For CBO-01 Commercial Ops

1. **Update GTM deck** — Include Threat Actor Registry as differentiator
2. **Schedule NTT demo** — pentest-ai-agents swarm (reschedule May 10-15)
3. **VoronDRQ outreach** — Registry as intel layer for DRQ platform
4. **CSM SOW draft** — POC terms (60/40 split, 30-day pipeline)

---

## Appendix: Webworm IOC Summary

| Type | Indicator | Confidence | Source |
|------|-----------|------------|--------|
| **GitHub Repo** | `github[.]com/anjsdgasdf/WordPress` | High | ESET |
| **Discord C2** | Discord API endpoints (433 messages) | High | ESET |
| **MS Graph C2** | Microsoft Graph API calls | High | ESET |
| **S3 Exfil** | Compromised Amazon S3 buckets | Medium | ESET |
| **Proxy Tools** | WormFrp, ChainWorm, SmuxProxy | Medium | ESET |
| **VPN Tunneling** | SoftEther VPN | High | ESET |

**Full IOC List:** `github.com/ahmadfaurani/threat-actor-registry/tree/master/iocs/webworm-iocs.json`

---

## Appendix: MITRE ATT&CK Mapping (Top 10 Techniques)

| Tactic | Technique ID | Name | Webworm Procedure |
|--------|--------------|------|-------------------|
| **Initial Access** | T1190 | Exploit Public-Facing Application | dirsearch + nuclei web vuln scanning |
| **Execution** | T1059.003 | Windows CMD Shell | cmd.exe via EchoCreep/GraphWorm |
| **Defense Evasion** | T1572 | Protocol Tunneling | SoftEther VPN + proxy chain |
| **Defense Evasion** | T1071.004 | Application Layer Protocol: DNS | Discord C2 traffic |
| **Defense Evasion** | T1071.001 | Application Layer Protocol: Web Protocols | MS Graph API C2 |
| **Command and Control** | T1102 | Web Service: Cloud Services | Discord, GitHub, OneDrive |
| **Exfiltration** | T1567.002 | Exfiltration to Cloud Storage | Amazon S3 buckets |
| **Persistence** | T1547.001 | Registry Run Keys | Assessed (standard persistence) |
| **Credential Access** | T1003 | OS Credential Dumping | Assessed (RAT capability) |
| **Discovery** | T1082 | System Information Discovery | Assessed (recon phase) |

**Full Mapping:** `github.com/ahmadfaurani/threat-actor-registry/tree/master/mitre-mappings/webworm-mapping.json`

---

**Classification:** TLP:AMBER  
**Distribution:** CSM, NACSA, MAMPU, Agency CISOs, MINDEF 91 RSD  
**Analyst:** HOI Intelligence Operations  
**Next Review:** 2026-05-28 (weekly IOC freshness)

---

*This brief is part of the HOI Intelligence Operations collection. For access requests or tasking, contact HOI Analyst.*

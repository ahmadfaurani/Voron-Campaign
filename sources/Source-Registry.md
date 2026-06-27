# HOI Source Registry

**Classification:** TLP:GREEN  
**Last Updated:** 2026-05-21  
**Total Sources:** 24  
**Owner:** HOI Intelligence Operations

---

## Source Categories

| Category | Count | Sources |
|----------|-------|---------|
| **Sovereign Intelligence** | 3 | Threat Actor Registry, cbo-01-commercial-ops, hoi-intelligence-ops |
| **Threat Intelligence** | 5 | ESET, THN, Symantec, MITRE ATT&CK, CISA |
| **Vulnerability Data** | 4 | NVD, CVE.org, GHSA, CISA KEV |
| **Dark Web (AIL)** | 1 | AIL Framework (p62server) |
| **Academic/Research** | 4 | arXiv, Google Scholar, IEEE Xplore, ACM DL |
| **Commercial/Industry** | 4 | Gartner, Forrester, IDC, CB Insights |
| **Government/Regulatory** | 3 | CSM, NACSA, MAMPU |

---

## Sovereign Intelligence Sources (Priority 1)

| Source ID | Name | URL | Type | Reliability | Access | Last Validated |
|-----------|------|-----|------|-------------|--------|----------------|
| **SRC-001** | **Threat Actor Registry** | github.com/ahmadfaurani/threat-actor-registry | Primary Intel | ✅ Authoritative | ✅ Read/Write | 2026-05-21 |
| **SRC-002** | **cbo-01-commercial-ops** | github.com/ahmadfaurani/cbo-01-commercial-ops | Commercial Intel | ✅ Authoritative | ✅ Read/Write | 2026-05-21 |
| **SRC-003** | **hoi-intelligence-ops** | github.com/ahmadfaurani/hoi-intelligence-ops | HOI Operations | ✅ Authoritative | ✅ Read/Write | 2026-05-21 |

### SRC-001: Threat Actor Registry (NEW - 2026-05-21)

**Purpose:** Sovereign threat actor intelligence repository for Malaysian GovSec

**Content:**
- Threat actor profiles (standardized schema)
- Validated IOCs (STIX-compatible JSON)
- MITRE ATT&CK mappings
- Campaign tracking
- TLP-governed distribution

**Initial Actor:** Webworm APT (China-aligned)
- 12 validated IOCs
- 38 MITRE ATT&CK techniques
- Quality score: 4.6/5.0 (Critic approved)
- Malaysian relevance: HIGH

**Collection Requirements:**
- **CR-042:** Weekly IOC freshness validation
- **CR-043:** APT40 (Leviathan) profile by 2026-06-15
- **CR-044:** MirrorFace profile by 2026-06-30
- **CR-045:** UAT-8302 profile by 2026-07-15

**Integration Points:**
- GovSec TIP (STIX/TAXII ingestion)
- AIL Framework (IOC correlation)
- pentest-ai-agents (TTP validation)
- CSM/NACSA (intel sharing)

**Access:** Private GitHub repository (TLP:AMBER)  
**Provisioned Access:** CSM, NACSA, MAMPU (pending usernames)

---

## Threat Intelligence Sources

| Source ID | Name | URL | Type | Reliability | Access | Last Validated |
|-----------|------|-----|------|-------------|--------|----------------|
| **SRC-004** | ESET WeLiveSecurity | welivesecurity.com | Vendor Research | ✅ High | ✅ Public | 2026-05-21 |
| **SRC-005** | The Hacker News | thehackernews.com | News Coverage | ✅ Medium-High | ✅ Public | 2026-05-21 |
| **SRC-006** | Symantec (Broadcom) | symantec-enterprise-blogs.security.com | Vendor Research | ✅ High | ✅ Public | 2026-05-21 |
| **SRC-007** | MITRE ATT&CK | attack.mitre.org | Framework | ✅ Authoritative | ✅ Public | 2026-05-21 |
| **SRC-008** | CISA | cisa.gov | Government Advisory | ✅ Authoritative | ✅ Public | 2026-05-01 |

---

## Vulnerability Data Sources

| Source ID | Name | URL | Type | Reliability | Access | Last Validated |
|-----------|------|-----|------|-------------|--------|----------------|
| **SRC-009** | NVD | nvd.nist.gov | Official CVE Database | ✅ Authoritative | ✅ Public | 2026-05-01 |
| **SRC-010** | CVE.org | cve.org | Authoritative CVE List | ✅ Authoritative | ✅ Public | 2026-05-01 |
| **SRC-011** | GitHub Security Advisories | github.com/advisories | Open Source Vulnerabilities | ✅ High | ✅ Public | 2026-05-01 |
| **SRC-012** | CISA KEV Catalog | cisa.gov/known-exploited-vulnerabilities | Known Exploited | ✅ Authoritative | ✅ Public | 2026-05-01 |

---

## Dark Web Intelligence

| Source ID | Name | URL | Type | Reliability | Access | Last Validated |
|-----------|------|-----|------|-------------|--------|----------------|
| **SRC-013** | **AIL Framework** | https://192.168.1.102:7000 (local) | Dark Web Intel | ✅ High | ✅ Local (p62server) | 2026-05-10 |

**Deployment:** `/home/p62operator/.openclaw/deployments/ail-framework/`  
**Version:** v6.7  
**Status:** Operational  
**Integration:** HOI → AIL crawl pipeline (automated)

---

## Academic/Research Sources

| Source ID | Name | URL | Type | Reliability | Access | Last Validated |
|-----------|------|-----|------|-------------|--------|----------------|
| **SRC-014** | arXiv | arxiv.org | Preprint Server | ✅ High | ✅ Public | 2026-05-05 |
| **SRC-015** | Google Scholar | scholar.google.com | Academic Search | ✅ High | ✅ Public | 2026-04-27 |
| **SRC-016** | IEEE Xplore | ieee.org | Academic Database | ✅ High | ⚠️ Subscription | 2026-04-01 |
| **SRC-017** | ACM Digital Library | dl.acm.org | Academic Database | ✅ High | ⚠️ Subscription | 2026-04-01 |

---

## Commercial/Industry Sources

| Source ID | Name | URL | Type | Reliability | Access | Last Validated |
|-----------|------|-----|------|-------------|--------|----------------|
| **SRC-018** | Gartner | gartner.com | Industry Analyst | ✅ High | ⚠️ Subscription | 2026-04-01 |
| **SRC-019** | Forrester | forrester.com | Industry Analyst | ✅ High | ⚠️ Subscription | 2026-04-01 |
| **SRC-020** | IDC | idc.com | Market Research | ✅ High | ⚠️ Subscription | 2026-04-01 |
| **SRC-021** | CB Insights | cbinsights.com | Startup/VC Intel | ✅ Medium-High | ⚠️ Subscription | 2026-04-01 |

---

## Government/Regulatory Sources

| Source ID | Name | URL | Type | Reliability | Access | Last Validated |
|-----------|------|-----|------|-------------|--------|----------------|
| **SRC-022** | CyberSecurity Malaysia (CSM) | cybersecurity.my | National CERT | ✅ Authoritative | ⚠️ Partner Access | 2026-04-24 |
| **SRC-023** | NACSA | nacsa.gov.my | National Cyber Security Agency | ✅ Authoritative | ⚠️ Partner Access | 2026-04-24 |
| **SRC-024** | MAMPU | mampu.gov.my | Government IT Office | ✅ Authoritative | ⚠️ Partner Access | 2026-04-24 |

---

## Collection Plan Integration

### Active Collection Requirements (Q2 2026)

| CR ID | Requirement | Source(s) | Priority | Status |
|-------|-------------|-----------|----------|--------|
| **CR-042** | Webworm IOC freshness validation (weekly) | SRC-001, SRC-004, SRC-005 | P1 | 🟢 Active |
| **CR-043** | APT40 (Leviathan) profile development | SRC-001, SRC-004, SRC-005, SRC-006 | P1 | 🟡 Pending |
| **CR-044** | MirrorFace actor tracking | SRC-001, SRC-004, SRC-005 | P1 | 🟡 Pending |
| **CR-045** | UAT-8302 campaign monitoring | SRC-001, SRC-005 | P1 | 🟡 Pending |
| **CR-046** | GovSec TIP deployment progress | SRC-022, SRC-023 | P2 | 🟡 Pending |
| **CR-047** | pentest-ai-agents ChainSentry integration | SRC-002, GitHub | P2 | 🟡 Pending |

---

## Source Validation Matrix

| Source | Validation Method | Frequency | Last Validation | Next Validation |
|--------|-------------------|-----------|-----------------|-----------------|
| **SRC-001 (Threat Actor Registry)** | GitHub commit hash + content review | Weekly | 2026-05-21 | 2026-05-28 |
| **SRC-004 (ESET)** | Cross-reference with other vendors | Monthly | 2026-05-21 | 2026-06-21 |
| **SRC-005 (THN)** | Cross-reference with primary sources | Monthly | 2026-05-21 | 2026-06-21 |
| **SRC-013 (AIL Framework)** | Crawl quality score (75-80 target) | Per crawl | 2026-05-10 | Next crawl |

---

## Source Reliability Scoring

| Score | Meaning | Sources |
|-------|---------|---------|
| **✅ Authoritative** | Primary source, official/owner content | SRC-001, SRC-002, SRC-003, SRC-007, SRC-009, SRC-010, SRC-012, SRC-022, SRC-023, SRC-024 |
| **✅ High** | Reputable vendor/research institution | SRC-004, SRC-006, SRC-011, SRC-014, SRC-015, SRC-016, SRC-017, SRC-018, SRC-019, SRC-020 |
| **✅ Medium-High** | Industry news, market intel | SRC-005, SRC-021 |

---

## Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-05-21 | Added SRC-001 (Threat Actor Registry) + CR-042 to CR-047 | HOI Analyst |
| 2026-05-10 | Updated AIL Framework crawl status | HOI Analyst |
| 2026-05-05 | Added arXiv (FAMA, SSL papers) | HOI Analyst |
| 2026-05-01 | Added ml-intern (Hugging Face) to competitor tracking | HOI Analyst |
| 2026-04-27 | Initial source registry creation | HOI Analyst |

---

**Classification:** TLP:GREEN  
**Owner:** HOI Intelligence Operations  
**Contact:** HOI Analyst  
**Next Review:** 2026-06-21 (quarterly)

---

*This registry is part of the HOI Intelligence Operations source management framework. For source additions or validation, contact HOI Analyst.*

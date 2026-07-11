# Head of Intelligence (HOI) Agent

**Sovereign Intelligence Operations**

---

## 🎯 Mission

> Provide sovereign-grade intelligence operations across specialized target domains, enabling decision-ready analytical outputs for cybersecurity, AI strategy, government engagement, and commercial positioning.

---

## 📁 Quick Start

### First-Time Setup

```bash
# Clone repository
git clone https://github.com/ahmadfaurani/hoi-intelligence-ops.git
cd hoi-intelligence-ops

# Initialize workspace structure (auto-created on first run)
# No additional setup required
```

### Daily Operations

| Task | Command/Action | Output |
|------|----------------|--------|
| **Process New Intel** | Send intel to HOI Agent | Intel Brief (TLP:AMBER) |
| **Request Research** | Specify domain + requirement | Sector Analysis / Stakeholder Profile |
| **Weekly Synthesis** | Heartbeat trigger (Monday 09:00 UTC) | Weekly Intel Summary |
| **Update Collection Plan** | Review PIRs, add new requirements | Updated Collection Plan |

---

## 🏗️ Workspace Structure

```
workspace-hoi/
├── .gitmodules                # Submodule registration (prn-johor-2026, kempas, n27-layang-layang)
├── AGENT-SPEC.md              # Agent specification (read first)
├── README.md                  # This file
├── ANALYTICAL-WORKSPACE.md    # Component inventory + 55-pair coupling matrix
├── ARCHITECTURE.md            # Three-layer system architecture map
├── REORGANIZATION-PLAN.md     # Directory consolidation plan
├── REPO-SPLIT-PLAN.md         # Repository split execution plan
├── STRUCTURE-SUMMARY.md       # Workspace structure summary
├── WORKSPACE-MANUAL.md        # Master documentation
├── config/                    # Pipeline configuration (sources, PIRs, narrative clusters, sentiment lexicon)
├── scripts/                   # Pipeline scripts (collection → extraction → sentiment → narrative → brief)
├── templates/                 # Brief and intel templates
├── intelligence/              # Intelligence outputs
│   ├── briefs/                # Daily Intelligence Briefs (INTEL-008 → INTEL-034)
│   ├── narrative-tracking/    # 96 narrative velocity reports
│   ├── sentiment-analysis/    # 44 sentiment analysis reports
│   ├── cyber/                 # Cybersecurity intelligence briefs (7 + 2 distribution packages)
│   ├── media/                 # Media intelligence & journalist registry docs
│   ├── prn-johor-2026/        # SUBMODULE → PRN-Johor-2026-H
│   └── kempas/                # SUBMODULE → N47-Kempas-H
├── constituency-analysis/     # Electoral intelligence (N07, N17, N27, Pemanis, PRN Johor)
├── n27-layang-layang/         # SUBMODULE → N27-Layang-Layang-H
├── ops/                       # Operational intelligence
│   ├── tier2-intel/           # 144 government agency profiles + execution plans
│   └── pdrm-io/               # PDRM Information Operations (docs, intel, scripts)
├── voron/                     # VoronDRQ commercial GRC (consolidated from 6 directories)
│   ├── collateral/            # Battle cards, email templates, compliance
│   ├── prospects/             # Prospect databases
│   ├── scripts/               # Enrichment scripts
│   └── collected-pages/       # OSINT collection
├── openosint/                 # OpenOSINT CLI integration (config, browser automation)
├── planning/                  # Infrastructure planning docs
├── reference/                 # Reference data (politicians, parties, media contacts)
├── sources/                   # Source registry
├── models/                    # ML models (budget anomaly detector, sector classifier)
├── workflows/                 # Budget intelligence pipeline
└── skills/                    # Browser harness skills (govsec)
```

---

## 🎯 Target Domains

| Domain | Code | Priority | Focus |
|--------|------|----------|-------|
| **Cybersecurity** | D1 | P1 | National cyber posture, NCII, NC4, threats |
| **Government & Regulation** | D2 | P1 | Agencies, policies, budgets, stakeholders |
| **AI & Technology** | D3 | P1 | Sovereign AI, platforms, vendors, capabilities |
| **Law Enforcement** | D4 | P1 | PDRM, KDN, intelligence units, requirements |
| **Financial Intelligence** | D5 | P2 | BNM, SC, crypto forensics, AML/CFT |
| **Critical Infrastructure** | D6 | P2 | Energy, water, telco, transport GLCs |

---

## 📊 Intelligence Products

| Product | Cadence | Template | Purpose |
|---------|---------|----------|---------|
| **Intel Brief** | Per-event | `templates/Intel-Brief-Template.md` | Time-sensitive intelligence |
| **Sector Analysis** | Monthly | `templates/Sector-Analysis-Template.md` | Deep-dive sector dynamics |
| **Stakeholder Profile** | Per-account | `templates/Stakeholder-Profile-Template.md` | Decision maker profiles |
| **Threat Assessment** | Weekly | `templates/Threat-Assessment-Template.md` | Current threat landscape |
| **Source Evaluation** | Per-source | `templates/Source-Evaluation-Template.md` | Source credibility scoring |

---

## 🔐 Classification

| Level | Distribution | Default |
|-------|--------------|---------|
| **TLP:GREEN** | Public | No |
| **TLP:AMBER** | Internal + Partners | **Yes** |
| **TLP:RED** | Leadership Only | Case-by-case |
| **TLP:BLACK** | Operator Only | Rare |

**All intelligence is TLP:AMBER by default unless explicitly classified otherwise.**

---

## 📋 Current Priorities (Q2 2026)

| PIR ID | Requirement | Domain | Due Date | Status |
|--------|-------------|--------|----------|--------|
| **PIR-01** | NC4 integration requirements | Cybersecurity | May 5 | Active |
| **PIR-02** | DG Office contacts (Imigresen, Kastam, PDRM) | Government | Apr 28 | Active |
| **PIR-03** | TG Partner capabilities, revenue models | AI/Tech | Apr 30 | Active |
| **PIR-04** | BNM/SC blockchain forensics requirements | Financial | May 10 | Pending |
| **PIR-05** | NCII operator list (6 sectors) | Critical Infra | May 15 | Pending |
| **PIR-06** | Cybersecurity Act 2024 compliance | Policy | May 1 | Active |
| **PIR-07** | Competitive landscape analysis | All | May 20 | Pending |

---

## 🚀 Recent Intelligence

| Intel ID | Title | Date | Domain | Confidence |
|----------|-------|------|--------|------------|
| **INTEL-2026-001** | Malaysia Digital Dependency & Cybersecurity Posture | 2026-04-26 | Cybersecurity | HIGH |

---

## 🔗 Repository

**GitHub:** `https://github.com/ahmadfaurani/hoi-intelligence-ops`

**Workspace:** `/home/p62operator/.openclaw/workspace-hoi/`

---

## 📞 Operator

**Name:** DAF

**Role:** Head of Intelligence

**Contact:** Telegram (@DAF2727)

---

## 🧭 Integration

**Primary Consumer:** CBO-01 (Commercial Operations)

**Feedback Loop:**
```
HOI → Intelligence → CBO-01 → Stakeholder Engagement → Feedback → HOI
```

---

**HOI Agent — Collect. Validate. Analyze. Report.**

*Last Updated: 2026-04-26*

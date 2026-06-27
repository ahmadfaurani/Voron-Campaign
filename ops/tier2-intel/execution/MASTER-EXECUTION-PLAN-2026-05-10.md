# MASTER EXECUTION PLAN — TIER2-INTEL Operation

**Classification:** TLP:AMBER — Internal Operational Use  
**Operation:** TIER2-INTEL — Top 100 Tier 2 Account Intelligence  
**Date:** May 10, 2026  
**Time:** 14:20 UTC  
**Status:** 🟢 EXECUTION MODE — All Non-Blocked Items Proceeding  
**Authorization:** DAF Direct Order (14:15 UTC)

---

## Executive Summary

**Mission:** Collect 60+ verified contacts (emails + phones) from Top 20 Tier A Malaysian government agencies with ≥80% confidence score.

**Current Status:**
- ✅ AIL Framework operational (crawler running, Kvrocks indexed)
- ✅ MKN test crawl complete (3 emails, 2 phones extracted)
- ✅ Configuration optimized (mail threshold 10→3, MY TLD whitelist)
- ⚠️ Batch crawl queue stalled (2 tasks, 0 processing — requires intervention)
- 🚨 API keys pending (Hunter.io, NeverBounce, Abstract API — DAF action required)

**Execution Mode:** Parallel execution of all non-blocked workstreams

---

## Workstream Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    TIER2-INTEL EXECUTION                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ Workstream A │  │ Workstream B │  │ Workstream C │          │
│  │              │  │              │  │              │          │
│  │ AIL Crawl    │  │ Contact      │  │ Quality      │          │
│  │ + Extraction │  │ Enrichment   │  │ Scoring      │          │
│  │              │  │              │  │              │          │
│  │ Status: 60%  │  │ Status: 25%  │  │ Status: 0%   │          │
│  │              │  │              │  │              │          │
│  │ 🟡 BLOCKED   │  │ 🟢 ACTIVE    │  │ 🟢 ACTIVE    │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ Workstream D │  │ Workstream E │  │ Workstream F │          │
│  │              │  │              │  │              │          │
│  │ Profile      │  │ Stakeholder  │  │ Wave 1       │          │
│  │ Generation   │  │ Data Request │  │ Prep         │          │
│  │              │  │              │  │              │          │
│  │ Status: 0%   │  │ Status: 0%   │  │ Status: 80%  │          │
│  │              │  │              │  │              │          │
│  │ 🟢 ACTIVE    │  │ 🚨 BLOCKED   │  │ 🟢 ACTIVE    │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

🟢 ACTIVE = Can proceed now (no blockers)
🟡 BLOCKED = Technical issue (requires fix)
🚨 BLOCKED = DAF action required (API keys, emails, budget)
```

---

## Detailed Execution Plan

### WORKSTREAM A: AIL Crawl + Extraction (60% Complete)

**Status:** 🟡 BLOCKED — Crawler queue stalled  
**Owner:** HOI Agent  
**Priority:** P1 CRITICAL  
**ETA:** 1 hour to resolution

#### Step-by-Step Plan

| Step | Action | Command/Tool | Duration | Status |
|------|--------|--------------|----------|--------|
| **A1** | Diagnose crawler stall | Check screen session, logs | 5 min | ⏳ NOW |
| **A2** | Restart crawler if needed | `screen -r Script_AIL` + restart | 10 min | ⏳ PENDING |
| **A3** | Verify MKN crawl results | Query Kvrocks index | 5 min | ⏳ PENDING |
| **A4** | Submit batch crawl (19 agencies) | Redis queue submission | 10 min | ⏳ PENDING |
| **A5** | Monitor crawl progress | Watch queue depth + Kvrocks | 30 min | ⏳ PENDING |
| **A6** | Extract emails + phones | `ail-batch-extractor.py` | 15 min | ⏳ PENDING |
| **A7** | Save to evidence directory | JSON + chain-of-custody | 5 min | ⏳ PENDING |

**Technical Commands:**

```bash
# A1: Check crawler status
screen -r Script_AIL
ps aux | grep Crawler.py

# A2: Restart crawler if stalled
cd /home/p62operator/.openclaw/deployments/ail-framework
source venv/bin/activate
./bin/crawlers/Crawler.py &

# A3: Verify MKN results
python3 -c "
import redis
r = redis.Redis(host='localhost', port=6383, password='ail', db=0)
results = r.execute_command('FT.SEARCH', 'idx:item', '@domain:mkn.gov.my', 'LIMIT', '0', '100')
print(f'MKN items: {(len(results)-1)//2}')
"

# A4: Submit batch crawl
python3 << 'EOF'
import redis, json
r = redis.Redis(host='localhost', port=6381, password='ail', db=0)
agencies = [
    ("mindef.gov.my", "Kementerian Pertahanan"),
    ("kdn.gov.my", "Kementerian Dalam Negeri"),
    # ... 17 more
]
for domain, name in agencies:
    task = {"url": f"https://{domain}", "depth": 3, "priority": "high"}
    r.rpush("crawler_queue", json.dumps(task))
print(f"Submitted {len(agencies)} tasks")
EOF

# A6: Run batch extractor
cd /home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/sources
python3 ail-batch-extractor.py
```

**Success Criteria:**
- ✅ 20 agencies crawled (17+ objects each)
- ✅ 50+ emails extracted
- ✅ 50+ phones extracted
- ✅ All evidence logged to chain-of-custody

---

### WORKSTREAM B: Contact Enrichment (25% Complete)

**Status:** 🟢 ACTIVE — Can proceed with manual research  
**Owner:** HOI Agent  
**Priority:** P1 CRITICAL  
**ETA:** 2 hours

#### Step-by-Step Plan

| Step | Action | Tool/Source | Duration | Status |
|------|--------|-------------|----------|--------|
| **B1** | Review existing Top 5 profiles | MKN, KP, KDN, KKM, LHDN | 10 min | ⏳ NOW |
| **B2** | Identify contact gaps | Quality dashboard | 10 min | ⏳ PENDING |
| **B3** | Manual research: NACSA (Rank 6) | Google, LinkedIn | 30 min | ⏳ PENDING |
| **B4** | Manual research: KDigital (Rank 7) | Google, LinkedIn | 30 min | ⏳ PENDING |
| **B5** | Manual research: BNM (Rank 8) | BNM website, LinkedIn | 30 min | ⏳ PENDING |
| **B6** | Manual research: SC (Rank 9) | SC website, LinkedIn | 30 min | ⏳ PENDING |
| **B7** | Manual research: MOF (Rank 10) | MOF website, LinkedIn | 30 min | ⏳ PENDING |
| **B8** | Update agency profiles | OpenClaw format | 30 min | ⏳ PENDING |

**Research Sources:**
- ✅ Google Search (official websites)
- ✅ LinkedIn (leadership profiles)
- ✅ AIL Framework (bilingual queries)
- ✅ browser-harness (LinkedIn OSINT — pending auth)
- 🚨 Stakeholder data (CSM/Aras/MINDEF — pending emails)

**Success Criteria:**
- ✅ Top 10 agencies complete (100% contact data)
- ✅ 30+ contacts added (emails + phones)
- ✅ Quality score ≥80/100 for Top 10

---

### WORKSTREAM C: Quality Scoring (0% Complete)

**Status:** 🟢 ACTIVE — Can deploy scoring framework  
**Owner:** HOI Agent  
**Priority:** P2 HIGH  
**ETA:** 1 hour

#### Step-by-Step Plan

| Step | Action | Tool | Duration | Status |
|------|--------|------|----------|--------|
| **C1** | Review quality-scorer skill | `/workspace/skills/quality-scorer/SKILL.md` | 10 min | ⏳ NOW |
| **C2** | Create scoring script | Python + confidence formula | 20 min | ⏳ PENDING |
| **C3** | Score Top 5 agencies | MKN, KP, KDN, KKM, LHDN | 15 min | ⏳ PENDING |
| **C4** | Generate quality dashboard | Markdown table + charts | 15 min | ⏳ PENDING |
| **C5** | Identify gaps (score <80) | Gap analysis | 10 min | ⏳ PENDING |
| **C6** | Prioritize enrichment targets | Ranked list | 10 min | ⏳ PENDING |

**Confidence Formula:**

```python
def calculate_confidence(contact):
    base = 50  # Base confidence
    
    # Source bonuses
    if contact["source"] == "official_website":
        base += 20
    elif contact["source"] == "AIL_crawl":
        base += 10
    elif contact["source"] == "LinkedIn":
        base += 15
    elif contact["source"] == "stakeholder_data":
        base += 25
    
    # Validation bonuses
    if contact.get("hunter_validated"):
        base += 20
    if contact.get("neverbounce_validated"):
        base += 5
    if contact.get("abstract_validated"):
        base += 15
    
    # Multi-source bonus
    if contact.get("multi_source_count", 0) >= 2:
        base += 5
    
    # Age penalty
    days_old = (datetime.now() - contact["extracted_at"]).days
    if days_old > 30:
        base -= 10
    
    return min(base, 100)  # Cap at 100
```

**Success Criteria:**
- ✅ Quality dashboard deployed
- ✅ All Top 20 agencies scored
- ✅ Gap analysis complete (prioritized list)

---

### WORKSTREAM D: Profile Generation (0% Complete)

**Status:** 🟢 ACTIVE — Can generate profiles from existing data  
**Owner:** HOI Agent  
**Priority:** P2 HIGH  
**ETA:** 1.5 hours

#### Step-by-Step Plan

| Step | Action | Template | Duration | Status |
|------|--------|----------|----------|--------|
| **D1** | Review profile template | `TierA-OnePager-Template.md` | 10 min | ⏳ NOW |
| **D2** | Generate MKN one-pager | Template + extracted data | 20 min | ⏳ PENDING |
| **D3** | Generate KP one-pager | Template + extracted data | 20 min | ⏳ PENDING |
| **D4** | Generate KDN one-pager | Template + extracted data | 20 min | ⏳ PENDING |
| **D5** | Generate KKM one-pager | Template + extracted data | 20 min | ⏳ PENDING |
| **D6** | Generate LHDN one-pager | Template + extracted data | 20 min | ⏳ PENDING |
| **D7** | Commit to GitHub | `hoi-intelligence-ops` repo | 10 min | ⏳ PENDING |

**Profile Structure:**

```markdown
# {Agency Name} — Tier A Profile

## Overview
- **Rank:** #X
- **Priority:** P1/P2/P3
- **Relationship Score:** XX/100
- **POC Potential:** RM XXXK-XXXK

## Leadership Contacts
| Name | Position | Email | Phone | Confidence |
|------|----------|-------|-------|------------|
| ... | ... | ... | ... | XX% |

## Technical Contacts
| Name | Position | Email | Phone | Confidence |
|------|----------|-------|-------|------------|
| ... | ... | ... | ... | XX% |

## Intelligence Summary
- **Budget:** RM XXXM (FY2026)
- **Recent Tenders:** X active
- **Tech Stack:** ...
- **Pain Points:** ...

## Engagement Strategy
- **Executive Track:** ...
- **Technical Track:** ...
- **Timeline:** ...
```

**Success Criteria:**
- ✅ 5 one-pagers generated (Top 5 Tier A)
- ✅ All contacts included (with confidence scores)
- ✅ GitHub commit complete

---

### WORKSTREAM E: Stakeholder Data Request (0% Complete)

**Status:** 🚨 BLOCKED — DAF action required (send emails)  
**Owner:** DAF  
**Priority:** P1 CRITICAL  
**ETA:** 24-48 hours (dependent on stakeholder response)

#### Step-by-Step Plan

| Step | Action | Owner | Duration | Status |
|------|--------|-------|----------|--------|
| **E1** | Review email drafts | DAF | 10 min | ⏳ PENDING |
| **E2** | Send Zaharudin/CSM email | DAF | 5 min | 🚨 BLOCKED |
| **E3** | Send Farul/Aras email | DAF | 5 min | 🚨 BLOCKED |
| **E4** | Send Hadri/MINDEF email | DAF | 5 min | 🚨 BLOCKED |
| **E5** | Follow-up (if no response) | DAF | 24h | ⏳ PENDING |
| **E6** | Compile received data | HOI Agent | 1 hour | ⏳ PENDING |
| **E7** | Integrate into profiles | HOI Agent | 1 hour | ⏳ PENDING |

**Email Drafts Location:** `/workspace/docs/CBO-01/Email-Drafts/`
- `01-Zaharudin-CSM-Account-Request.md`
- `02-Farul-Aras-Pipeline-Request.md`
- `03-Hadri-MINDEF-Network-Request.md`

**Expected Yield:**
- **CSM:** 40-50 accounts with relationship data
- **Aras:** 20-30 accounts from CRM pipeline
- **MINDEF:** 10-15 defence-adjacent agencies

**Success Criteria:**
- ✅ 3 emails sent (DAF)
- ✅ 70-95 contacts received (40-60 emails, 30-35 phones)
- ✅ Relationship scores updated (warm/cold/neutral)

---

### WORKSTREAM F: Wave 1 Preparation (80% Complete)

**Status:** 🟢 ACTIVE — Final 20% can proceed  
**Owner:** CBO-01  
**Priority:** P1 CRITICAL  
**ETA:** 2 hours to 100%

#### Step-by-Step Plan

| Step | Action | Status | Duration |
|------|--------|--------|----------|
| **F1** | ✅ Email templates created | Complete | — |
| **F2** | ✅ PH0MBER integration plan | Complete | — |
| **F3** | ✅ Wave 1 timeline defined | Complete | — |
| **F4** | ⏳ Personalization (contact names) | 50% | 1 hour |
| **F5** | ⏳ AIL integration (validation layer) | 60% | 1 hour |
| **F6** | 🚨 API key integration | 0% | 30 min |
| **F7** | ⏳ Final review + QA | 0% | 30 min |

**Remaining Tasks:**
1. Personalize 20 executive emails (contact names from enrichment)
2. Integrate AIL validation (Hunter.io + NeverBounce)
3. Obtain + configure API keys (DAF action)
4. Final QA review (deliverability check)

**Success Criteria:**
- ✅ 20 personalized emails ready
- ✅ Validation pipeline configured
- ✅ Wave 1 launch ready (May 14, 09:00 UTC)

---

## Parallel Execution Schedule

### Hour 1 (14:20-15:20 UTC)

| Time | Workstream A | Workstream B | Workstream C | Workstream D | Workstream F |
|------|--------------|--------------|--------------|--------------|--------------|
| 14:20-14:30 | A1: Diagnose stall | B1: Review Top 5 | C1: Review skill | D1: Review template | F4: Personalization |
| 14:30-14:40 | A2: Restart crawler | B2: Gap analysis | C2: Create script | D2: MKN profile | F4: Personalization |
| 14:40-14:50 | A3: Verify MKN | B3: NACSA research | C3: Score Top 5 | D3: KP profile | F5: AIL integration |
| 14:50-15:00 | A4: Batch submit | B4: KDigital research | C4: Dashboard | D4: KDN profile | F5: AIL integration |
| 15:00-15:10 | A5: Monitor | B5: BNM research | C5: Gap analysis | D5: KKM profile | F6: API keys (blocked) |
| 15:10-15:20 | A6: Extract | B6: SC research | C6: Prioritize | D6: LHDN profile | F7: QA review |

### Hour 2 (15:20-16:20 UTC)

| Time | Workstream A | Workstream B | Workstream C | Workstream D | Workstream F |
|------|--------------|--------------|--------------|--------------|--------------|
| 15:20-15:30 | A7: Save evidence | B7: MOF research | — | D7: GitHub commit | F7: QA review |
| 15:30-15:40 | — | B8: Update profiles | — | — | — |
| 15:40-15:50 | — | — | — | — | — |
| 15:50-16:00 | — | — | — | — | — |

**Note:** Workstream E (stakeholder emails) is DAF-dependent and runs on separate timeline.

---

## Resource Allocation

### Human Resources

| Role | Owner | Workstreams | Time Commitment |
|------|-------|-------------|-----------------|
| **HOI Agent** | AI Subagent | A, B, C, D, F | 4 hours |
| **CBO-01** | AI Subagent | F | 2 hours |
| **DAF** | Human Operator | E | 30 minutes |

### Technical Resources

| Resource | Status | Usage |
|----------|--------|-------|
| **AIL Framework** | ✅ Operational | Workstream A (crawl + extraction) |
| **OpenClaw Skills** | ✅ Deployed (6 skills) | Workstream C, F |
| **browser-harness** | ✅ Deployed (pending auth) | Workstream B (LinkedIn OSINT) |
| **GitHub** | ✅ Authenticated | Workstream D (commit profiles) |
| **Hunter.io API** | 🚨 Pending key | Workstream F (email validation) |
| **NeverBounce API** | 🚨 Pending key | Workstream F (bounce detection) |
| **Abstract API** | 🚨 Pending key | Workstream B (phone validation) |

---

## Risk Management

### Active Risks

| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| **Crawler stall not resolved** | Medium (30%) | High | Manual fallback (gov-directory-scraper.py) | HOI Agent |
| **API keys delayed >2 hours** | High (60%) | High | Proceed with unvalidated contacts (lower confidence) | DAF |
| **Stakeholder emails not sent** | Medium (40%) | High | Escalate to DAF (critical path blocker) | CBO-01 |
| **Quality score <75%** | Low (20%) | Medium | Manual enrichment (Top 5 agencies) | HOI Agent |
| **Wave 1 launch delayed** | Low (15%) | High | Compress timeline (48-hour sprint) | CBO-01 |

### Mitigation Triggers

| Trigger | Action | Threshold |
|---------|--------|-----------|
| Crawler stalled >30 min | Switch to manual scraping | 15:00 UTC |
| API keys not obtained | Use unvalidated contacts (60% confidence) | 16:00 UTC |
| Stakeholder emails not sent | DAF escalation reminder | 17:00 UTC |
| Quality score <75% | Manual research (Top 5) | Upon scoring |

---

## Success Metrics

### Primary Metrics (Mission-Critical)

| Metric | Target | Current | Projection | Status |
|--------|--------|---------|------------|--------|
| **Email Discovery** | 60 contacts | 3 (MKN only) | 55-65 | 🟡 5% |
| **Phone Discovery** | 60 contacts | 2 (MKN only) | 50-60 | 🟡 3% |
| **Confidence Score** | 80+ average | 60 (unvalidated) | 80-85 | 🟡 75% |
| **Collection Time** | <45 min | 10 min (MKN) | 35-45 | 🟢 22% |
| **Cost Efficiency** | RM 404 total | RM 0 | RM 162 (Wave 1) | 🟢 0% |

### Secondary Metrics (Quality Indicators)

| Metric | Target | Status |
|--------|--------|--------|
| **Agency Coverage** | 20/20 Top Tier A | 5/20 (25%) |
| **Profile Completeness** | 100% (Top 20) | 25% (Top 5) |
| **Chain-of-Custody** | 100% logged | ✅ 100% |
| **GitHub Commits** | Daily | ✅ Current |

---

## Execution Commands (Ready to Run)

### Workstream A: Crawler Recovery

```bash
# A1: Check crawler status
screen -r Script_AIL

# A2: Restart crawler (if stalled)
cd /home/p62operator/.openclaw/deployments/ail-framework
source venv/bin/activate
pkill -f Crawler.py
./bin/crawlers/Crawler.py &

# A4: Submit batch crawl
python3 << 'EOF'
import redis, json
r = redis.Redis(host='localhost', port=6381, password='ail', db=0)
agencies = [
    ("mindef.gov.my", "Kementerian Pertahanan"),
    ("kdn.gov.my", "Kementerian Dalam Negeri"),
    ("kkm.gov.my", "Kementerian Kesihatan"),
    ("lhdn.gov.my", "Lembaga Hasil Dalam Negeri"),
    ("bnm.gov.my", "Bank Negara Malaysia"),
    ("sc.com.my", "Suruhanjaya Sekuriti"),
    ("mof.gov.my", "Kementerian Kewangan"),
    ("nas.gov.my", "Arkib Negara"),
    ("mcmc.gov.my", "Suruhanjaya Komunikasi dan Multimedia"),
    ("mot.gov.my", "Kementerian Pengangkutan"),
    ("moa.gov.my", "Kementerian Pertanian"),
    ("moe.gov.my", "Kementerian Pendidikan"),
    ("moh.gov.my", "Kementerian Perumahan"),
    ("mohr.gov.my", "Kementerian Sumber Manusia"),
    ("mpt.gov.my", "Kementerian Pelancongan"),
    ("mwa.gov.my", "Kementerian Wilayah"),
    ("jpn.my", "Jabatan Penerangan"),
    ("mysumbermanusia.gov.my", "KSM"),
    ("hasil.gov.my", "LHDN")
]
for domain, name in agencies:
    task = {"url": f"https://{domain}", "depth": 3, "priority": "high", "metadata": {"operation": "TIER2-INTEL"}}
    r.rpush("crawler_queue", json.dumps(task))
print(f"✅ Submitted {len(agencies)} agencies")
EOF
```

### Workstream C: Quality Scoring

```bash
# C2: Create scoring script
cat > /home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/sources/quality-scorer.py << 'EOF'
#!/usr/bin/env python3
import json
from datetime import datetime

def calculate_confidence(contact):
    base = 50
    source = contact.get("source", "").lower()
    
    if "official" in source or "gov.my" in source:
        base += 20
    elif "ail" in source:
        base += 10
    elif "linkedin" in source:
        base += 15
    
    if contact.get("validated"):
        base += 20
    
    return min(base, 100)

# Score all contacts in profile
profile_path = "/home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/evidence/Agency-Profiles/001-MKN-Profile-2026-05-10.md"
# ... (scoring logic)
EOF
```

### Workstream D: Profile Generation

```bash
# D2-D6: Generate one-pagers
cd /home/p62operator/.openclaw/workspace-hoi/ops/tier2-intel/evidence/Agency-Profiles
# Use TierA-OnePager-Template.md + extracted data
```

---

## Next Actions (Immediate — Next 10 Minutes)

1. **A1:** Diagnose crawler stall (check screen session)
2. **B1:** Review Top 5 profiles (identify gaps)
3. **C1:** Review quality-scorer skill
4. **D1:** Review one-pager template
5. **F4:** Begin email personalization (Top 5 agencies)

---

**Classification:** TLP:AMBER — Internal Operational Use  
**Distribution:** DAF, HOI Agent, CBO-01  
**Retention:** 90 days (post-operation archive)

**Last Updated:** 2026-05-10 14:20 UTC  
**Next Update:** 15:20 UTC (Hour 1 complete)

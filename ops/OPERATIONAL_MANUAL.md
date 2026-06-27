# Tech Stack Operational Manual & Workflow Guide
## Political Intelligence Operations — Standard Operating Procedures

**Report Date:** June 18, 2026  
**Classification:** TLP:AMBER (Internal + Partners)  
**Operator:** p62operator  
**Version:** 1.0  
**Supplements:** `/home/p62operator/TECH_STACK_ANALYTICAL_REPORT_2026-06-18.md`

---

## Table of Contents

1. [Daily Operations Rhythm](#1-daily-operations-rhythm)
2. [Intelligence Collection Workflows](#2-intelligence-collection-workflows)
3. [Agent Orchestration Procedures](#3-agent-orchestration-procedures)
4. [Browser Automation Playbooks](#4-browser-automation-playbooks)
5. [Memory Management Operations](#5-memory-management-operations)
6. [Incident Response Runbooks](#6-incident-response-runbooks)
7. [Maintenance & Health Checks](#7-maintenance--health-checks)
8. [Quality Control Procedures](#8-quality-control-procedures)
9. [Data Flow & Integration Maps](#9-data-flow--integration-maps)
10. [Escalation & Decision Matrices](#10-escalation--decision-matrices)

---

## 1. Daily Operations Rhythm

### 1.1 Morning Check (08:00-09:00 UTC)

| Time | Task | Command/Action | Expected Output | Owner |
|------|------|----------------|-----------------|-------|
| **08:00** | Infrastructure Health Check | `./scripts/health-check.sh` | All services green | Operator |
| **08:15** | Overnight Intel Review | Check `/home/p62operator/.openclaw/workspace-hoi/intelligence/` | New briefs flagged | HOI Agent |
| **08:30** | PIR Status Update | Review collection plan | Updated priorities | Operator |
| **08:45** | Source Monitoring | SearXNG alerts for priority keywords | Alert digest | Automated |
| **09:00** | Daily Standup Sync | Review Honcho conclusions | Peer updates | Operator + Agent |

### 1.2 Health Check Script

```bash
#!/bin/bash
# /home/p62operator/scripts/health-check.sh

echo "=== INFRASTRUCTURE HEALTH CHECK ==="
echo "Timestamp: $(date -u '+%Y-%m-%d %H:%M UTC')"
echo ""

# Service Health Checks
echo "[1/6] Honcho API..."
curl -s http://localhost:8000/health | jq -r '.status' || echo "❌ FAILED"

echo "[2/6] DeerFlow Gateway..."
curl -s http://localhost:2026/api/health 2>/dev/null && echo "✅ OK" || echo "⚠️  Auth Required (Normal)"

echo "[3/6] Firecrawl API..."
curl -s -o /dev/null -w "%{http_code}" http://localhost:3002 | grep -q "200\|404" && echo "✅ OK" || echo "❌ FAILED"

echo "[4/6] SearXNG..."
curl -s -o /dev/null -w "%{http_code}" http://localhost:8080 | grep -q "200" && echo "✅ OK" || echo "❌ FAILED"

echo "[5/6] Docker Containers..."
docker ps --format "table {{.Names}}\t{{.Status}}" | grep -c "Up" | xargs -I {} echo "{} containers running"

echo "[6/6] Disk Usage..."
df -h /home | tail -1 | awk '{print $5 " used"}'

echo ""
echo "=== HEALTH CHECK COMPLETE ==="
```

### 1.3 Evening Synthesis (17:00-18:00 UTC)

| Time | Task | Action | Output |
|------|------|--------|--------|
| **17:00** | Collection Review | Audit new intel gathered | Collection efficiency metric |
| **17:15** | Source Validation | Verify new source credibility | Source evaluation records |
| **17:30** | Memory Consolidation | Review Honcho conclusions | Fact validation |
| **17:45** | Queue Processing | Clear pending Firecrawl jobs | Empty extraction queue |
| **18:00** | Daily Log | Update operations log | `/home/p62operator/.openclaw/workspace-hoi/ops/daily-log.md` |

---

## 2. Intelligence Collection Workflows

### 2.1 Breaking News Response Workflow

**Trigger:** High-priority political event detected (e.g., cabinet reshuffle, coalition change)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    BREAKING NEWS RESPONSE FLOW                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  [1] DETECTION                                                          │
│      │                                                                  │
│      ├── SearXNG Alert (keyword match)                                  │
│      ├── RSS Feed Monitor                                               │
│      └── Manual Tip                                                     │
│                                                                         │
│      ▼                                                                  │
│  [2] TRIAGE (TLP Classification)                                        │
│      │                                                                  │
│      ├── TLP:GREEN → Public monitoring                                  │
│      ├── TLP:AMBER → Internal analysis (DEFAULT)                        │
│      ├── TLP:RED → Leadership briefing only                             │
│      └── TLP:BLACK → Operator eyes only                                 │
│                                                                         │
│      ▼                                                                  │
│  [3] COLLECTION PLAN ACTIVATION                                         │
│      │                                                                  │
│      ├── Identify relevant PIRs                                         │
│      ├── Select target sources (5-10 outlets)                           │
│      ├── Deploy Firecrawl extraction jobs                               │
│      └── Activate browser automation for JS sites                       │
│                                                                         │
│      ▼                                                                  │
│  [4] ANALYSIS                                                           │
│      │                                                                  │
│      ├── DeerFlow agent synthesizes collection                          │
│      ├── Cross-reference with existing intel                            │
│      ├── Identify stakeholder impacts                                   │
│      └── Draft initial assessment                                       │
│                                                                         │
│      ▼                                                                  │
│  [5] PRODUCT GENERATION                                                 │
│      │                                                                  │
│      ├── Intel Brief (within 2 hours)                                   │
│      ├── Stakeholder Impact Matrix                                      │
│      └── Follow-up Collection Requirements                              │
│                                                                         │
│      ▼                                                                  │
│  [6] DISTRIBUTION                                                       │
│      │                                                                  │
│      └── TLP-based routing via send_message tool                        │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Collection Execution Commands

```bash
# Step 1: Create collection task directory
mkdir -p /home/p62operator/.openclaw/workspace-hoi/intelligence/collections/$(date +%Y%m%d-%H%M)

# Step 2: Firecrawl extraction (single URL)
curl -X POST http://localhost:3002/v1/scrape \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://www.thestar.com.my/news/nation/2026/06/18/cabinet-reshuffle",
    "formats": ["markdown", "links"],
    "onlyMainContent": true,
    "waitFor": 3000
  }'

# Step 3: Firecrawl batch extraction (multiple URLs)
curl -X POST http://localhost:3002/v1/crawl \
  -H "Content-Type: application/json" \
  -d '{
    "urls": [
      "https://www.thestar.com.my/news/nation/...",
      "https://www.malaysiakini.com/news/...",
      "https://www.freemalaysiatoday.com/category/nation/..."
    ],
    "formats": ["markdown"],
    "limit": 50
  }'

# Step 4: Patchright for JavaScript-heavy sites
cd /home/p62operator/browser-automation
node test-patchright.js

# Step 5: DeerFlow agent synthesis
# Via Hermes Agent prompt:
# "Analyze the collected intelligence from [directory] and produce an Intel Brief"
```

### 2.3 Malaysia Journalist Registry Collection Pipeline

**Target:** 600+ journalists across 27 outlets  
**Method:** Byline extraction → Contact verification → Registry entry

#### Phase 1: Outlet Prioritization

| Tier | Outlets | Method | Timeline |
|------|---------|--------|----------|
| **Tier 1** | FMT, The Star, Malaysiakini, MalaysiaNow | Patchright + RSS | Week 1-2 |
| **Tier 2** | BH, Utusan, NST, The Edge | Browser automation | Week 3-4 |
| **Tier 3** | Regional (TVS, Sabah outlets) | Mixed methods | Week 5-6 |
| **Tier 4** | Digital-native, niche outlets | Manual + scripts | Week 7-8 |

#### Phase 2: Extraction Workflow

```bash
# For each outlet in priority list:

# 1. Create outlet working directory
mkdir -p /home/p62operator/.openclaw/workspace-hoi/sources/journalist-registry/[outlet-code]

# 2. Extract bylines via Firecrawl
curl -X POST http://localhost:3002/v1/extract \
  -H "Content-Type: application/json" \
  -d '{
    "urls": ["https://www.freemalaysiatoday.com/"],
    "prompt": "Extract all journalist bylines with article URLs from the homepage",
    "schema": {
      "type": "object",
      "properties": {
        "journalists": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {"type": "string"},
              "article_url": {"type": "string"},
              "article_title": {"type": "string"}
            }
          }
        }
      }
    }
  }'

# 3. For JavaScript-rendered sites, use Patchright
cd /home/p62operator/browser-automation
node -e "
const { chromium } = require('patchright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('https://www.freemalaysiatoday.com/');
  await page.waitForSelector('article');
  const bylines = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('.byline')).map(el => el.textContent);
  });
  console.log(JSON.stringify({bylines}, null, 2));
  await browser.close();
})();
"

# 4. Validate and enrich contacts
# - Search for verified public emails (official masthead, LinkedIn, Twitter)
# - NEVER activate pattern-inferred emails
# - Record source URL for every contact

# 5. Add to Honcho memory
curl -X POST http://localhost:8000/api/v3/peers/[peer-id]/messages \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Journalist contact: [Name], [Outlet], [Verified Email]",
    "metadata": {
      "source_url": "https://...",
      "confidence": "verified",
      "collection_date": "2026-06-18"
    }
  }'
```

#### Phase 3: Quality Gates

| Gate | Criteria | Action if Failed |
|------|----------|------------------|
| **G1: Source URL** | Every record has source URL | Reject record |
| **G2: Contact Confidence** | Only verified public emails | Mark as "unverified" if inferred |
| **G3: Deduplication** | No duplicate entries | Merge records |
| **G4: Outlet Classification** | Correct tier assignment | Reclassify |
| **G5: TLP Marking** | All records marked TLP:AMBER | Add classification |

---

## 3. Agent Orchestration Procedures

### 3.1 DeerFlow Agent Deployment

**Use Case:** Complex multi-step intelligence analysis tasks

#### Step-by-Step Deployment

```bash
# 1. Navigate to workspace
cd /home/p62operator/.openclaw/workspace-hoi

# 2. Create agent task specification
cat > /tmp/agent-task.md << 'EOF'
# Task: Weekly Political Intelligence Synthesis

## Objective
Produce weekly intelligence summary covering all 6 priority domains.

## Collection Sources
- SearXNG: Keywords ["Kabinet", "Parlimen", "PKR", "Johor politics"]
- Firecrawl: Top 10 Malaysian news outlets
- Honcho: Review conclusions from past 7 days

## Analysis Requirements
1. Identify emerging trends per domain
2. Cross-reference with historical patterns
3. Flag anomalies requiring follow-up
4. Assess stakeholder impacts

## Output Format
- Executive Summary (200 words)
- Domain-by-Domain Analysis
- Priority Intelligence Requirements Update
- Recommended Collection Adjustments

## Classification
TLP:AMBER
EOF

# 3. Submit task to DeerFlow via API
curl -X POST http://localhost:2026/api/v1/tasks \
  -H "Authorization: Bearer [TOKEN]" \
  -H "Content-Type: application/json" \
  -d '{
    "task_spec": "/tmp/agent-task.md",
    "workspace": "workspace-hoi",
    "priority": "high",
    "deadline": "2026-06-19T09:00:00Z"
  }'

# 4. Monitor task progress
curl -X GET http://localhost:2026/api/v1/tasks/[TASK-ID]/status \
  -H "Authorization: Bearer [TOKEN]"

# 5. Retrieve completed product
curl -X GET http://localhost:2026/api/v1/tasks/[TASK-ID]/output \
  -H "Authorization: Bearer [TOKEN]" \
  -o /home/p62operator/.openclaw/workspace-hoi/intelligence/weekly-summary-$(date +%Y%m%d).md
```

### 3.2 Subagent Delegation Patterns

| Pattern | Use Case | Configuration |
|---------|----------|---------------|
| **Parallel Research** | Multiple domains simultaneously | `max_concurrent_children: 3` |
| **Sequential Pipeline** | Collection → Analysis → Product | Chain via `context_from` |
| **Specialist Agents** | Domain-specific expertise | Assign by skill match |
| **Quality Review** | Independent verification | Separate agent, same data |

### 3.3 Hermes Agent Delegation Workflow

```python
# Example: Parallel domain research via delegate_task

from hermes_tools import delegate_task

# Research 3 domains in parallel
results = delegate_task(tasks=[
    {
        "goal": "Research cybersecurity developments in Malaysia (past 7 days)",
        "context": "Focus on NCII, NC4, critical infrastructure protection. Use SearXNG and Firecrawl.",
        "toolsets": ["web", "terminal"]
    },
    {
        "goal": "Research government & regulation developments (past 7 days)",
        "context": "Focus on KDN, agency restructuring, policy changes. Check official gazettes.",
        "toolsets": ["web", "terminal"]
    },
    {
        "goal": "Research AI & technology developments (past 7 days)",
        "context": "Focus on sovereign AI initiatives, vendor contracts, capability announcements.",
        "toolsets": ["web", "terminal"]
    }
])

# Synthesize results
# [Results returned as array of subagent summaries]
```

---

## 4. Browser Automation Playbooks

### 4.1 Playwright vs. Patchright Decision Matrix

| Scenario | Recommended Tool | Rationale |
|----------|------------------|-----------|
| **Internal testing** | Playwright | Faster, no stealth overhead |
| **Malaysian news sites (general)** | Patchright | Better anti-bot bypass |
| **Cloudflare-protected sites** | Patchright | 90-100% bypass rate |
| **AI agent control via MCP** | Playwright MCP | Native integration |
| **High-volume scraping** | Playwright | Lower resource usage |
| **JavaScript-heavy outlets (BH, Edge)** | Patchright | Full JS rendering + stealth |

### 4.2 Standard Extraction Script Template

```javascript
// /home/p62operator/browser-automation/templates/extract-bylines.js

const { chromium } = require('patchright');

async function extractBylines(outletConfig) {
  const browser = await chromium.launch({
    headless: true,
    args: [
      '--disable-blink-features=AutomationControlled',
      '--disable-dev-shm-usage',
      '--no-sandbox'
    ]
  });

  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 },
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    locale: 'en-MY',
    timezoneId: 'Asia/Kuala_Lumpur'
  });

  const page = await context.newPage();

  // Additional stealth
  await page.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3] });
  });

  try {
    console.log(`Navigating to ${outletConfig.url}...`);
    await page.goto(outletConfig.url, {
      waitUntil: 'networkidle',
      timeout: 60000
    });

    // Wait for content
    await page.waitForSelector(outletConfig.selectors.article, { timeout: 30000 });

    // Extract bylines
    const bylines = await page.evaluate((selectors) => {
      const results = [];
      const articles = document.querySelectorAll(selectors.article);
      articles.forEach(article => {
        const bylineEl = article.querySelector(selectors.byline);
        const titleEl = article.querySelector(selectors.title);
        const urlEl = article.querySelector(selectors.url);
        if (bylineEl) {
          results.push({
            name: bylineEl.textContent.trim(),
            article_title: titleEl ? titleEl.textContent.trim() : '',
            article_url: urlEl ? urlEl.href : ''
          });
        }
      });
      return results;
    }, outletConfig.selectors);

    console.log(`Extracted ${bylines.length} bylines`);
    return bylines;

  } catch (error) {
    console.error(`Extraction failed: ${error.message}`);
    await page.screenshot({ path: `error-${outletConfig.code}.png` });
    throw error;
  } finally {
    await browser.close();
  }
}

// Outlet configurations
const outlets = {
  'fmt': {
    url: 'https://www.freemalaysiatoday.com/',
    code: 'fmt',
    selectors: {
      article: 'article.post',
      byline: '.author-name',
      title: '.post-title',
      url: 'a.post-link'
    }
  },
  'thestar': {
    url: 'https://www.thestar.com.my/',
    code: 'thestar',
    selectors: {
      article: 'div.story-block',
      byline: '.author-name',
      title: 'h3.story-headline',
      url: 'a.story-link'
    }
  },
  // Add more outlets...
};

// Run extraction
(async () => {
  const outlet = process.argv[2] || 'fmt';
  const config = outlets[outlet];
  if (!config) {
    console.error(`Unknown outlet: ${outlet}`);
    process.exit(1);
  }

  const bylines = await extractBylines(config);
  console.log(JSON.stringify({outlet, bylines, extracted_at: new Date().toISOString()}, null, 2));
})();
```

### 4.3 Cloudflare Bypass Escalation

```
┌─────────────────────────────────────────────────────────────────────────┐
│                 CLOUDFLARE BYPASS ESCALATION LADDER                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Level 1: Standard Patchright                                           │
│  ─────────────────────────────                                          │
│  - Stealth patches enabled                                              │
│  - Realistic user agent                                                 │
│  - Success Rate: ~70%                                                   │
│                                                                         │
│  Level 2: Enhanced Stealth                                              │
│  ─────────────────────────────                                          │
│  - Add realistic mouse movements                                        │
│  - Randomize viewport dimensions                                        │
│  - Add human-like delays                                                │
│  - Success Rate: ~85%                                                   │
│                                                                         │
│  Level 3: Residential Proxy                                             │
│  ─────────────────────────────                                          │
│  - Route through residential IP                                         │
│  - Match geolocation to outlet                                          │
│  - Success Rate: ~95%                                                   │
│                                                                         │
│  Level 4: Managed Service                                               │
│  ─────────────────────────────                                          │
│  - Bright Data / Browserbase                                            │
│  - Last resort for critical targets                                     │
│  - Success Rate: ~99%                                                   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 4.4 Extraction Quality Verification

```bash
# Verify extraction results
cd /home/p62operator/browser-automation

# Check for expected output structure
node -e "
const data = require('./extraction-results.json');
const checks = {
  has_outlet: !!data.outlet,
  has_bylines: Array.isArray(data.bylines),
  byline_count: data.bylines.length > 0,
  has_names: data.bylines.every(b => b.name),
  has_urls: data.bylines.every(b => b.article_url),
  no_duplicates: new Set(data.bylines.map(b => b.name)).size === data.bylines.length
};

console.log('Quality Checks:');
Object.entries(checks).forEach(([check, passed]) => {
  console.log(\`  [\${passed ? '✅' : '❌'}] \${check}\`);
});

const allPassed = Object.values(checks).every(v => v);
process.exit(allPassed ? 0 : 1);
"
```

---

## 5. Memory Management Operations

### 5.1 Honcho Memory Lifecycle

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    HONCHO MEMORY LIFECYCLE                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  [CREATE] Message Ingestion                                             │
│      │                                                                  │
│      ├── POST /api/v3/peers/{peer_id}/messages                          │
│      ├── Batch up to 100 messages                                       │
│      └── Enqueue for background processing                              │
│                                                                         │
│      ▼                                                                  │
│  [PROCESS] Deriver Worker                                               │
│      │                                                                  │
│      ├── Extract conclusions (facts)                                    │
│      ├── Update peer representation                                     │
│      └── Store in vector DB (pgvector)                                  │
│                                                                         │
│      ▼                                                                  │
│  [CONSOLIDATE] Reconciler (Periodic)                                    │
│      │                                                                  │
│      ├── Generate embeddings for new messages                           │
│      ├── Clean up stale queue items                                     │
│      └── Optimize vector indices                                        │
│                                                                         │
│      ▼                                                                  │
│  [RETRIEVE] Dialectic Query                                             │
│      │                                                                  │
│      ├── POST /api/v3/peers/{peer_id}/chat                              │
│      ├── Semantic search conclusions                                    │
│      └── Inject context into response                                   │
│                                                                         │
│      ▼                                                                  │
│  [PRUNE] Memory Hygiene (Weekly)                                        │
│      │                                                                  │
│      ├── Review low-confidence conclusions                              │
│      ├── Delete PII if requested                                        │
│      └── Archive old sessions                                           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Memory Operations Commands

```bash
# List all workspaces
curl -s http://localhost:8000/api/v3/workspaces/list \
  | jq '.workspaces[] | {id: .id, name: .name, created: .created_at}'

# List peers in workspace
curl -s http://localhost:8000/api/v3/workspaces/political-intelligence/peers/list \
  | jq '.peers[] | {id: .id, metadata: .metadata}'

# Query peer conclusions (semantic search)
curl -s -X POST http://localhost:8000/api/v3/peers/[PEER-ID]/conclusions/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "PKR leadership stability",
    "max_results": 10,
    "min_score": 0.7
  }' | jq '.conclusions[] | {text: .text, created: .created_at}'

# Add new conclusion
curl -s -X POST http://localhost:8000/api/v3/peers/[PEER-ID]/conclusions \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Rafizi Ramli announced new PKR youth initiative on 2026-06-15",
    "metadata": {
      "source": "The Star",
      "confidence": "high",
      "domain": "cybersecurity"
    }
  }'

# Delete conclusion (PII removal)
curl -s -X DELETE http://localhost:8000/api/v3/peers/[PEER-ID]/conclusions/[CONCLUSION-ID]

# Get peer representation (psychological model)
curl -s http://localhost:8000/api/v3/peers/[PEER-ID]/representation \
  | jq '.representation'
```

### 5.3 Memory Quality Assurance

| Check | Frequency | Command | Threshold |
|-------|-----------|---------|-----------|
| **Duplicate Conclusions** | Weekly | Semantic similarity > 0.95 | Merge |
| **Low-Confidence Facts** | Weekly | Query score < 0.5 | Review |
| **Orphan Messages** | Daily | Unprocessed > 24h | Investigate |
| **Queue Backlog** | Daily | Deriver queue depth | Alert if > 1000 |
| **Vector DB Size** | Monthly | pgvector table size | Plan if > 10GB |

---

## 6. Incident Response Runbooks

### 6.1 Service Failure Response

#### DeerFlow Gateway Down

```bash
# SYMPTOM: curl http://localhost:2026 returns connection refused

# Step 1: Check container status
docker ps -a | grep deer-flow

# Step 2: Check container logs
docker logs deer-flow-gateway --tail 100

# Step 3: Restart container
docker restart deer-flow-gateway

# Step 4: Verify recovery
curl -s http://localhost:2026

# Step 5: If still failing, check nginx
docker logs deer-flow-nginx --tail 50

# Step 6: Full stack restart (last resort)
cd /opt/deer-flow
docker compose restart
```

#### Firecrawl Extraction Failures

```bash
# SYMPTOM: Firecrawl API returns 500 errors or timeouts

# Step 1: Check API container
docker logs firecrawl-api-1 --tail 100

# Step 2: Check Playwright service
docker logs firecrawl-playwright-service-1 --tail 100

# Step 3: Check RabbitMQ queue depth
docker exec firecrawl-rabbitmq-1 rabbitmqctl list_queues

# Step 4: Clear stuck jobs (if queue > 1000)
docker exec firecrawl-rabbitmq-1 rabbitmqctl purge_queue [QUEUE-NAME]

# Step 5: Restart affected containers
docker restart firecrawl-api-1 firecrawl-playwright-service-1

# Step 6: Verify recovery
curl -X POST http://localhost:3002/v1/scrape \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

#### Honcho Memory Corruption

```bash
# SYMPTOM: Conclusions returning garbled or duplicate data

# Step 1: Check API health
curl -s http://localhost:8000/health

# Step 2: Check database connectivity
docker exec honcho-database-1 psql -U postgres -c "SELECT count(*) FROM conclusions;"

# Step 3: Check for database locks
docker exec honcho-database-1 psql -U postgres -c "SELECT * FROM pg_locks WHERE granted = false;"

# Step 4: If locks detected, identify blocking queries
docker exec honcho-database-1 psql -U postgres -c "SELECT pid, query, state FROM pg_stat_activity WHERE state != 'idle';"

# Step 5: Kill blocking queries (if safe)
docker exec honcho-database-1 psql -U postgres -c "SELECT pg_terminate_backend([PID]);"

# Step 6: Restart API (clears in-memory state)
docker restart honcho-api-1

# Step 7: Verify recovery
curl -s http://localhost:8000/api/v3/peers/[PEER-ID]/conclusions/query \
  -d '{"query": "test", "max_results": 1}'
```

### 6.2 Security Incident Response

#### Unauthorized Access Detected

```bash
# SYMPTOM: Unknown IPs in access logs, unexpected API calls

# Step 1: Isolate affected services
docker network disconnect openclaw_default [CONTAINER-NAME]

# Step 2: Capture evidence
docker logs [CONTAINER-NAME] > /home/p62operator/.openclaw/incident-logs/$(date +%Y%m%d-%H%M).log

# Step 3: Review access logs
grep -E "POST|GET" /home/p62operator/.openclaw/logs/access.log | tail 100

# Step 4: Rotate credentials
# - OpenClaw gateway token
# - Honcho API key (if enabled)
# - Database passwords

# Step 5: Audit firewall rules
ufw status verbose
iptables -L -n

# Step 6: Document incident
# Create incident report in /home/p62operator/.openclaw/incident-logs/
```

### 6.3 Data Loss Recovery

```bash
# SYMPTOM: Missing intelligence products, corrupted database

# Step 1: Identify scope of loss
ls -la /home/p62operator/.openclaw/workspace-hoi/intelligence/
# Compare with expected output

# Step 2: Check database integrity
docker exec honcho-database-1 pg_isready
docker exec honcho-database-1 psql -U postgres -c "SELECT pg_database_size('honcho');"

# Step 3: Restore from backup (if available)
# Backups stored in /home/p62operator/backups/honcho/
docker cp /home/p62operator/backups/honcho/[BACKUP-FILE].sql honcho-database-1:/tmp/restore.sql
docker exec honcho-database-1 psql -U postgres -f /tmp/restore.sql

# Step 4: Restore file-based data
# From /home/p62operator/backups/workspace-hoi/
rsync -av /home/p62operator/backups/workspace-hoi/ /home/p62operator/.openclaw/workspace-hoi/

# Step 5: Verify restoration
# Run health checks and spot-check data integrity

# Step 6: Document recovery
# Record what was lost, what was recovered, gaps identified
```

---

## 7. Maintenance & Health Checks

### 7.1 Scheduled Maintenance Calendar

| Frequency | Task | Duration | Impact | Owner |
|-----------|------|----------|--------|-------|
| **Daily** | Health check script | 2 min | None | Automated |
| **Daily** | Queue depth review | 5 min | None | Operator |
| **Weekly** | Database backup | 30 min | None | Automated |
| **Weekly** | Log rotation | 10 min | None | Automated |
| **Weekly** | Memory QA review | 60 min | None | Operator |
| **Monthly** | Container updates | 60 min | Brief downtime | Operator |
| **Monthly** | Disk cleanup | 30 min | None | Operator |
| **Quarterly** | Full stack backup | 4 hours | Planned downtime | Operator |
| **Quarterly** | Security audit | 8 hours | None | External |

### 7.2 Backup Procedures

```bash
#!/bin/bash
# /home/p62operator/scripts/backup-weekly.sh

BACKUP_DIR="/home/p62operator/backups/$(date +%Y%m%d)"
mkdir -p $BACKUP_DIR/{honcho,workspace-hoi,browser-automation,configs}

echo "=== WEEKLY BACKUP ==="
echo "Timestamp: $(date -u '+%Y-%m-%d %H:%M UTC')"
echo "Backup Directory: $BACKUP_DIR"
echo ""

# Honcho Database Backup
echo "[1/5] Backing up Honcho PostgreSQL..."
docker exec honcho-database-1 pg_dump -U postgres honcho | gzip > $BACKUP_DIR/honcho/database-$(date +%Y%m%d).sql.gz

# Honcho Redis Backup (if persistence enabled)
echo "[2/5] Backing up Honcho Redis..."
docker exec honcho-redis-1 redis-cli SAVE 2>/dev/null || echo "Redis persistence not enabled"

# Workspace Files Backup
echo "[3/5] Backing up HOI workspace..."
rsync -av --exclude='*.tmp' /home/p62operator/.openclaw/workspace-hoi/ $BACKUP_DIR/workspace-hoi/

# Browser Automation Backup
echo "[4/5] Backing up browser automation..."
rsync -av /home/p62operator/browser-automation/ $BACKUP_DIR/browser-automation/

# Configuration Backup
echo "[5/5] Backing up configurations..."
cp /home/p62operator/.hermes/config.yaml $BACKUP_DIR/configs/
cp /home/p62operator/.openclaw/openclaw.json $BACKUP_DIR/configs/
cp /home/p62operator/.mcp.json $BACKUP_DIR/configs/

# Compress backup
echo ""
echo "Compressing backup..."
tar -czf $BACKUP_DIR.tar.gz -C $(dirname $BACKUP_DIR) $(basename $BACKUP_DIR)
rm -rf $BACKUP_DIR

# Verify backup
echo "Verifying backup..."
tar -tzf $BACKUP_DIR.tar.gz > /dev/null && echo "✅ Backup verified" || echo "❌ Backup verification failed"

# Cleanup old backups (keep 4 weeks)
echo ""
echo "Cleaning up old backups..."
find /home/p62operator/backups/ -name "*.tar.gz" -mtime +28 -delete

echo ""
echo "=== BACKUP COMPLETE ==="
echo "Backup Location: $BACKUP_DIR.tar.gz"
echo "Backup Size: $(du -h $BACKUP_DIR.tar.gz | cut -f1)"
```

### 7.3 Health Check Dashboard

```bash
#!/bin/bash
# /home/p62operator/scripts/health-dashboard.sh

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║         POLITICAL INTELLIGENCE STACK - HEALTH DASHBOARD       ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "Timestamp: $(date -u '+%Y-%m-%d %H:%M UTC')"
echo ""

# Container Status
echo "┌───────────────────────────────────────────────────────────────┐"
echo "│ CONTAINER STATUS                                              │"
echo "├───────────────────────────────────────────────────────────────┤"
docker ps --format "│ %-30s │ %-25s │" "{{.Names}}" "{{.Status}}"
echo "└───────────────────────────────────────────────────────────────┘"
echo ""

# Service Health
echo "┌───────────────────────────────────────────────────────────────┐"
echo "│ SERVICE HEALTH                                                │"
echo "├───────────────────────────────────────────────────────────────┤"

# Honcho
HONCHO_STATUS=$(curl -s http://localhost:8000/health | jq -r '.status' 2>/dev/null || echo "DOWN")
printf "│ %-30s │ %-25s │\n" "Honcho API" "$HONCHO_STATUS"

# DeerFlow
DEERFLOW_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:2026 2>/dev/null)
if [ "$DEERFLOW_STATUS" = "200" ] || [ "$DEERFLOW_STATUS" = "401" ]; then
  DEERFLOW_STATUS="OK ($DEERFLOW_STATUS)"
else
  DEERFLOW_STATUS="DOWN ($DEERFLOW_STATUS)"
fi
printf "│ %-30s │ %-25s │\n" "DeerFlow Gateway" "$DEERFLOW_STATUS"

# Firecrawl
FIRECRAWL_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3002 2>/dev/null)
if [ "$FIRECRAWL_STATUS" = "200" ] || [ "$FIRECRAWL_STATUS" = "404" ]; then
  FIRECRAWL_STATUS="OK ($FIRECRAWL_STATUS)"
else
  FIRECRAWL_STATUS="DOWN ($FIRECRAWL_STATUS)"
fi
printf "│ %-30s │ %-25s │\n" "Firecrawl API" "$FIRECRAWL_STATUS"

# SearXNG
SEARXNG_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8080 2>/dev/null)
if [ "$SEARXNG_STATUS" = "200" ]; then
  SEARXNG_STATUS="OK"
else
  SEARXNG_STATUS="DOWN ($SEARXNG_STATUS)"
fi
printf "│ %-30s │ %-25s │\n" "SearXNG" "$SEARXNG_STATUS"

echo "└───────────────────────────────────────────────────────────────┘"
echo ""

# Resource Usage
echo "┌───────────────────────────────────────────────────────────────┐"
echo "│ RESOURCE USAGE                                                │"
echo "├───────────────────────────────────────────────────────────────┤"
printf "│ %-30s │ %-25s │\n" "Disk Usage" "$(df -h /home | tail -1 | awk '{print $5}')"
printf "│ %-30s │ %-25s │\n" "Memory Usage" "$(free -h | grep Mem | awk '{print $3 "/" $2}')"
printf "│ %-30s │ %-25s │\n" "Running Containers" "$(docker ps -q | wc -l)"
echo "└───────────────────────────────────────────────────────────────┘"
echo ""

# Queue Depths
echo "┌───────────────────────────────────────────────────────────────┐"
echo "│ QUEUE DEPTHS                                                  │"
echo "├───────────────────────────────────────────────────────────────┤"
FIRECRAWL_QUEUE=$(docker exec firecrawl-rabbitmq-1 rabbitmqctl list_queues name messages 2>/dev/null | tail -1 | awk '{print $2}')
printf "│ %-30s │ %-25s │\n" "Firecrawl Queue" "${FIRECRAWL_QUEUE:-N/A}"
echo "└───────────────────────────────────────────────────────────────┘"
```

---

## 8. Quality Control Procedures

### 8.1 Intelligence Product Quality Gates

| Gate | Criteria | Verification Method | Pass Threshold |
|------|----------|---------------------|----------------|
| **G1: Source Attribution** | Every claim has source URL | Manual review | 100% |
| **G2: TLP Classification** | All products marked | Template check | 100% |
| **G3: Timestamp** | Collection date recorded | Metadata check | 100% |
| **G4: Confidence Scoring** | Sources rated | Adherence scale | 100% |
| **G5: Cross-Reference** | Claims verified across 2+ sources | Analyst review | 80% |
| **G6: Analytical Rigor** | Alternative hypotheses considered | Structured analysis | 80% |
| **G7: Actionability** | Recommendations specific | SME review | 80% |

### 8.2 Source Credibility Assessment

```
┌─────────────────────────────────────────────────────────────────────────┐
│                 SOURCE CREDIBILITY ASSESSMENT MATRIX                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  RELIABILITY (Source Track Record)                                      │
│  ─────────────────────────────────                                      │
│  A - Completely Reliable (no history of error)                          │
│  B - Usually Reliable (minor errors, corrected)                         │
│  C - Fairly Reliable (occasional errors)                                │
│  D - Not Usually Reliable (frequent errors)                             │
│  E - Unreliable (known fabrications)                                    │
│  F - Reliability Cannot Be Judged (new source)                          │
│                                                                         │
│  CREDIBILITY (Information Quality)                                      │
│  ─────────────────────────────────                                      │
│  1 - Confirmed by independent sources                                   │
│  2 - Probably true (consistent with known facts)                        │
│  3 - Possibly true (no contradictions)                                  │
│  4 - Doubtful (contradicts known facts)                                 │
│  5 - Improbable (highly unlikely)                                       │
│  6 - Truth Cannot Be Judged (insufficient data)                         │
│                                                                         │
│  COMBINED RATING EXAMPLE: "B2" = Usually Reliable, Probably True        │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 8.3 Analyst Review Checklist

```markdown
## Pre-Release Review Checklist

### Content Verification
- [ ] All factual claims have source citations
- [ ] Sources span multiple outlets (no single-source dependency)
- [ ] Dates and times are accurate and timezone-specified
- [ ] Names and titles are correctly spelled
- [ ] Numerical data verified against original sources

### Analytical Quality
- [ ] Alternative explanations considered
- [ ] Assumptions explicitly stated
- [ ] Confidence levels assigned to key judgments
- [ ] Dissenting views noted (if applicable)
- [ ] Logical fallacies avoided

### Classification & Handling
- [ ] TLP marking applied correctly
- [ ] Distribution list appropriate for classification
- [ ] Sensitive information properly redacted
- [ ] Retention period specified

### Formatting & Presentation
- [ ] Template followed correctly
- [ ] Executive summary present (for long reports)
- [ ] Visual aids (charts, maps) accurate and labeled
- [ ] Hyperlinks functional
- [ ] Document version controlled
```

---

## 9. Data Flow & Integration Maps

### 9.1 End-to-End Intelligence Pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│              END-TO-END INTELLIGENCE PIPELINE                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  COLLECTION LAYER                                                       │
│  ────────────────                                                       │
│                                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐   │
│  │  SearXNG    │  │  Firecrawl  │  │  Patchright │  │  RSS/ATOM   │   │
│  │  (Search)   │  │  (Scrape)   │  │  (Browser)  │  │  (Feeds)    │   │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘   │
│         │                │                │                │           │
│         └────────────────┴────────────────┴────────────────┘           │
│                                  │                                      │
│                                  ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │              Raw Collection Storage                              │   │
│  │         /home/p62operator/.openclaw/workspace-hoi/               │   │
│  │                    sources/raw/                                  │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  PROCESSING LAYER                                                       │
│  ───────────────                                                        │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │              DeerFlow Agent Orchestration                        │   │
│  │                                                                  │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │   │
│  │  │  Extraction  │  │  Analysis    │  │  Synthesis   │          │   │
│  │  │  Subagent    │  │  Subagent    │  │  Subagent    │          │   │
│  │  └──────────────┘  └──────────────┘  └──────────────┘          │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                  │                                      │
│                                  ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │              Honcho Memory Layer                                 │   │
│  │         (Conclusions, Representations, Context)                  │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  PRODUCT LAYER                                                          │
│  ─────────────                                                          │
│                                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐   │
│  │ Intel Brief │  │  Sector     │  │ Stakeholder │  │  Threat     │   │
│  │  (TLP:AMBER)│  │  Analysis   │  │  Profile    │  │  Assessment │   │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘   │
│                                                                         │
│  DISTRIBUTION LAYER                                                     │
│  ──────────────────                                                     │
│                                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                     │
│  │  Telegram   │  │   Email     │  │    API      │                     │
│  │  (Home)     │  │  (Himalaya) │  │  (REST)     │                     │
│  └─────────────┘  └─────────────┘  └─────────────┘                     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 9.2 API Integration Reference

| Integration | Endpoint | Method | Auth | Purpose |
|-------------|----------|--------|------|---------|
| **Honcho Messages** | `/api/v3/peers/{id}/messages` | POST | None (local) | Ingest intelligence |
| **Honcho Conclusions** | `/api/v3/peers/{id}/conclusions/query` | POST | None (local) | Semantic search |
| **Firecrawl Scrape** | `/v1/scrape` | POST | None (local) | Single URL extraction |
| **Firecrawl Crawl** | `/v1/crawl` | POST | None (local) | Multi-URL extraction |
| **Firecrawl Extract** | `/v1/extract` | POST | None (local) | Schema-based extraction |
| **DeerFlow Tasks** | `/api/v1/tasks` | POST | Bearer Token | Submit agent tasks |
| **SearXNG Search** | `/search` | GET/POST | None | Metasearch queries |

---

## 10. Escalation & Decision Matrices

### 10.1 Intelligence Escalation Matrix

| Scenario | Classification | Distribution | Timeline | Approver |
|----------|----------------|--------------|----------|----------|
| **Routine Intel** | TLP:AMBER | Internal team | 24-48 hours | HOI Agent |
| **Time-Sensitive** | TLP:AMBER | Internal + Partners | 2-4 hours | Operator |
| **Critical Development** | TLP:RED | Leadership only | Immediate | Operator + Review |
| **Source Compromise** | TLP:BLACK | Operator only | Immediate | Operator |
| **Public Information** | TLP:GREEN | Wide distribution | Standard | HOI Agent |

### 10.2 Technical Escalation Matrix

| Severity | Symptom | Response Time | Escalation Path |
|----------|---------|---------------|-----------------|
| **P1 - Critical** | Complete service outage | 15 min | Operator → Infrastructure Lead |
| **P2 - High** | Degraded performance | 1 hour | Operator → Self-remediate |
| **P3 - Medium** | Non-critical feature broken | 24 hours | Operator → Scheduled fix |
| **P4 - Low** | Cosmetic issues | Next maintenance | Operator → Backlog |

### 10.3 Decision Authority Matrix

| Decision Type | Operator | HOI Agent | Infrastructure Lead | External |
|---------------|----------|-----------|---------------------|----------|
| **Collection Priority** | ✅ | Advisory | — | — |
| **TLP Classification** | ✅ | ✅ | — | — |
| **Source Activation** | ✅ | Advisory | — | — |
| **Infrastructure Change** | Advisory | — | ✅ | — |
| **Budget Approval** | — | — | ✅ | ✅ |
| **Partner Sharing** | ✅ | ✅ | Advisory | ✅ |
| **Emergency Response** | ✅ | Advisory | Notify | — |

---

## Appendix A: Command Quick Reference

```bash
# === SERVICE MANAGEMENT ===
docker ps --format "table {{.Names}}\t{{.Status}}"     # List containers
docker restart [container]                              # Restart service
docker logs -f [container] --tail 100                   # Follow logs

# === HEALTH CHECKS ===
curl http://localhost:8000/health                       # Honcho
curl http://localhost:2026                              # DeerFlow
curl http://localhost:3002                              # Firecrawl
curl http://localhost:8080                              # SearXNG

# === BACKUP ===
/home/p62operator/scripts/backup-weekly.sh              # Weekly backup
/home/p62operator/scripts/health-check.sh               # Daily health
/home/p62operator/scripts/health-dashboard.sh           # Dashboard view

# === BROWSER AUTOMATION ===
cd /home/p62operator/browser-automation
node test-playwright.js                                 # Standard test
node test-patchright.js                                 # Anti-bot test

# === HONCHO MEMORY ===
curl http://localhost:8000/api/v3/workspaces/list       # List workspaces
curl http://localhost:8000/api/v3/peers/list            # List peers
curl -X POST http://localhost:8000/api/v3/peers/[ID]/conclusions/query  # Search

# === FIRECRAWL ===
curl -X POST http://localhost:3002/v1/scrape -d '{"url":"https://..."}'  # Scrape
curl -X POST http://localhost:3002/v1/crawl -d '{"urls":[...]}'          # Crawl
curl -X POST http://localhost:3002/v1/extract -d '{"url":"..."}'         # Extract
```

---

## Appendix B: Contact & Escalation

| Role | Contact | Availability | Escalation To |
|------|---------|--------------|---------------|
| **Operator** | p62operator | Business hours | Infrastructure Lead |
| **HOI Agent** | agent-rook (Honcho peer) | 24/7 automated | Operator |
| **Infrastructure** | [TBD] | Business hours | External vendor |
| **Emergency** | [TBD] | 24/7 | — |

---

**Document Control:**
- **Version:** 1.0
- **Created:** June 18, 2026
- **Review Date:** July 18, 2026
- **Classification:** TLP:AMBER
- **Location:** `/home/p62operator/.openclaw/workspace-hoi/ops/OPERATIONAL_MANUAL.md`

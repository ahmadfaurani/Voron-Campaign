# OSINT Process Optimization Plan

**Classification:** TLP:AMBER  
**Operation:** TIER2-INTEL  
**Date:** 2026-05-10 12:25 UTC  
**Author:** HOI Agent (Research Bot #2)  
**Mission Owner:** DAF  

---

## Executive Summary

**Current State:** 143 agency profiles created (Phase 1 complete), but **0% contact completeness** (0/60 required contacts) and **quality gap** (Top 20 Tier A average 74.2/100 vs. target 80+/100).

**Root Cause:** Batch processor creates skeleton profiles with `[Pending OSINT]` placeholders. No automated contact enrichment, no parallelization, no real-time quality validation.

**Target:** Reduce manual effort from **11.25 hours to <5 hours** while improving quality to **85+/100** and achieving **85-95% contact completeness**.

---

## Current State Assessment

| Metric | Current | Target | Gap |
|--------|---------|--------|-----|
| Contact Completeness | 0% (0/60 contacts) | 100% | -100% |
| Quality Score (Top 20 Tier A) | 74.2/100 | 80+/100 | -5.8 pts |
| Collection Velocity | 143 agencies / ~3 hours | Baseline | — |
| Manual Effort (Planned) | 11.25 hours | <5 hours | -55% |
| Automation Level | ~20% (batch profile gen) | ~80% | +60% |
| Parallel Workers | 1 (sequential) | 4-8 | +300-700% |

---

## Bottleneck Analysis

| Bottleneck | Impact | Root Cause | Solution |
|------------|--------|------------|----------|
| **Sequential Processing** | HIGH | `batch-processor.py` runs single-threaded | Implement multiprocessing with 4-8 workers |
| **No Contact Enrichment** | CRITICAL | Profiles have `[Pending]` for all contacts | Integrate Hunter.io API + email inference + domain scraping |
| **Post-Collection QA** | HIGH | Quality checked after collection (not during) | Real-time confidence scoring + auto-flag low-quality records |
| **Manual LinkedIn Scraping** | HIGH | 20 agencies × ~15 min each = 5 hours | Selenium/Playwright automation with rate-limit handling |
| **No Retry Logic** | MEDIUM | Failed scrapes require manual restart | Exponential backoff + failure logging + retry queue |
| **Static Templates** | MEDIUM | All profiles use same threat/budget scores | Dynamic scoring based on actual OSINT data |
| **No Rate Limit Handling** | HIGH | 429 responses break collection | Request throttling + rotating user agents + proxy support |

---

## Automation Roadmap

### Immediate (24 hours) — Quick Wins

| Automation | Effort | Impact | Priority |
|------------|--------|--------|----------|
| **Email Pattern Inference** | Low (2 hours) | HIGH — Auto-generate emails from domain | P0 |
| **Domain Scraping** | Medium (4 hours) | HIGH — Extract contacts from agency websites | P0 |
| **Confidence Scoring** | Low (1 hour) | MEDIUM — Flag low-quality records for review | P1 |
| **Parallel Worker Pool** | Medium (6 hours) | HIGH — 4x throughput increase | P0 |
| **Retry Logic + Backoff** | Low (2 hours) | MEDIUM — Handle transient failures | P1 |

**Total Effort:** ~15 hours  
**Expected Impact:** Contact completeness 0% → 60%, Manual effort 11.25h → 7h

### Short-Term (48-72 hours) — Medium Effort

| Automation | Effort | Impact | Priority |
|------------|--------|--------|----------|
| **Hunter.io API Integration** | Medium (4 hours) | HIGH — Verified B2B email database | P0 |
| **LinkedIn Company Page Scraper** | High (8 hours) | HIGH — Leadership extraction (ToS-compliant) | P1 |
| **Phone Validation API** | Low (2 hours) | MEDIUM — Validate Malaysian phone formats | P2 |
| **CAPTCHA Handling** | High (6 hours) | MEDIUM — 2Captcha integration for blocked requests | P2 |
| **Progress Dashboard (Real-Time)** | Medium (4 hours) | LOW — Live metrics + completion tracking | P3 |

**Total Effort:** ~24 hours  
**Expected Impact:** Contact completeness 60% → 85%, Quality score 74 → 82

### Long-Term (Post-Wave 1) — Strategic

| Automation | Effort | Impact | Priority |
|------------|--------|--------|----------|
| **Multi-Proxy Rotation** | High (8 hours) | MEDIUM — Avoid IP bans | P2 |
| **Browser Fingerprint Rotation** | High (10 hours) | MEDIUM — Evade bot detection | P2 |
| **ML-Based Contact Prediction** | High (16 hours) | LOW — Predict likely contacts from patterns | P3 |
| **Automated LinkedIn Login Flow** | Very High (20 hours) | HIGH — Authenticated scraping (risky) | P1 |
| **Commercial API Aggregation** | Medium (6 hours) | HIGH — Snov.io, Clearbit, NeverBounce integration | P1 |

**Total Effort:** ~60 hours  
**Expected Impact:** Contact completeness 85% → 95%, Manual review 30% → 10%

---

## Parallel Execution Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    MASTER COORDINATOR                        │
│  - Queue management (20 agencies / 4 workers = 5 each)      │
│  - Result aggregation + conflict resolution                 │
│  - Progress tracking + failure recovery                     │
└─────────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│   Worker 1    │ │   Worker 2    │ │   Worker 3    │ │   Worker 4    │
│ Agencies 1-5  │ │ Agencies 6-10 │ │ Agencies 11-15│ │ Agencies 16-20│
│               │ │               │ │               │ │               │
│ - Domain scan │ │ - Domain scan │ │ - Domain scan │ │ - Domain scan │
│ - Email find  │ │ - Email find  │ │ - Email find  │ │ - Email find  │
│ - LinkedIn    │ │ - LinkedIn    │ │ - LinkedIn    │ │ - LinkedIn    │
│ - Validation  │ │ - Validation  │ │ - Validation  │ │ - Validation  │
└───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘
        │                 │                 │                 │
        └─────────────────┴─────────────────┴─────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │   MERGED OUTPUT       │
              │   - Deduplicated      │
              │   - Confidence scored │
              │   - Flagged for QA    │
              └───────────────────────┘
```

| Worker | Scope | Expected Output | Duration |
|--------|-------|-----------------|----------|
| Worker 1 | Agencies 1-5 (Tier A) | 15 contacts (3 per agency) | 2 hours |
| Worker 2 | Agencies 6-10 (Tier A) | 15 contacts | 2 hours |
| Worker 3 | Agencies 11-15 (Tier A/B) | 15 contacts | 2 hours |
| Worker 4 | Agencies 16-20 (Tier A/B) | 15 contacts | 2 hours |

**Total Throughput:** 60 contacts in 2 hours (vs. 11.25 hours manual = **5.6x speedup**)

---

## Tool Stack Recommendations

| Tool | Purpose | Cost | Setup | Integration |
|------|---------|------|-------|-------------|
| **Hunter.io API** | Email discovery + verification | $49/mo (2K credits) | 1 hour | Python `hunter` library |
| **BeautifulSoup4** | HTML parsing (government portals) | Free | Built-in | Existing in `gov-directory-scraper.py` |
| **Selenium/Playwright** | JavaScript-rendered pages (LinkedIn) | Free | 2 hours | Headless Chrome + stealth plugins |
| **NeverBounce/ZeroBounce** | Email validation | $0.008/email | 30 min | REST API |
| **Numverify/Abstract API** | Phone number validation | Free tier | 30 min | REST API |
| **Snov.io API** | Alternative email finder | $39/mo | 1 hour | REST API (backup to Hunter) |
| **Clearbit API** | Company enrichment | $99/mo | 2 hours | REST API (firmographic data) |
| **2Captcha** | CAPTCHA solving | $1-3 per 1000 | 1 hour | API integration |
| **rotating-proxies** | IP rotation (avoid bans) | $15/mo (Bright Data) | 2 hours | HTTP proxy config |
| **python-dotenv** | API key management | Free | 15 min | Environment variables |

**Recommended Stack (Phase 1):**
1. Hunter.io API (primary email source)
2. BeautifulSoup4 (existing, extend)
3. NeverBounce (email validation)
4. Numverify (phone validation, free tier)

**Total Cost:** ~$60-100/month (justified by 6+ hours manual time saved)

---

## Quality Control Pipeline

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  COLLECTION  │───▶│  VALIDATION  │───▶│   SCORING    │───▶│    OUTPUT    │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
       │                   │                   │                   │
       │                   │                   │                   │
       ▼                   ▼                   ▼                   ▼
 - Domain scrape     - Email format     - Confidence       - JSON + Markdown
 - API lookup          validation         score (0-100)      profiles
 - LinkedIn extract  - Phone format     - Flag <70 for     - QA dashboard
 - Inference rules   - Domain match       manual review    - GitHub commit
```

| Checkpoint | Validation Rule | Action on Failure |
|------------|-----------------|-------------------|
| **Email Format** | Regex: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` | Reject + log as "invalid_format" |
| **Domain Match** | Email domain must match agency domain | Flag as "low_confidence" (score -20) |
| **Phone Format** | Malaysian: `+60X-XXX-XXXX` or `0X-XXX-XXXX` | Reject + log as "invalid_phone" |
| **Role Completeness** | Must have ≥1 of: DG, CIO, CISO | Flag for "manual_followup" |
| **Source Attribution** | Every contact must have source URL | Reject if missing (chain-of-custody) |
| **Confidence Threshold** | Overall score ≥70/100 | Auto-flag <70 for manual review |
| **Duplicate Detection** | Same email/phone across agencies | Merge + flag as "shared_contact" |

---

## Expected Outcomes (Post-Optimization)

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Collection Time (20 agencies) | 11.25 hours | 4-5 hours | **-60%** |
| Contact Completeness | 0% | 85-95% | **+85-95%** |
| Quality Score (Top 20) | 74.2/100 | 85+/100 | **+10.8 pts** |
| Manual Review Required | 100% | 20-30% | **-70-80%** |
| Contacts per Hour | ~5 | ~12-15 | **+140-200%** |
| Failure Rate | Unknown (no logging) | <5% (with retry) | **N/A** |

---

## Implementation Timeline

| Task | Owner | Start | End | Dependencies |
|------|-------|-------|-----|--------------|
| **Email Pattern Inference Module** | HOI Agent | May 10, 14:00 UTC | May 10, 16:00 UTC | None |
| **Parallel Worker Framework** | HOI Agent | May 10, 16:00 UTC | May 10, 22:00 UTC | Email module |
| **Hunter.io API Integration** | HOI Agent | May 11, 08:00 UTC | May 11, 12:00 UTC | API key from DAF |
| **Confidence Scoring System** | HOI Agent | May 11, 12:00 UTC | May 11, 14:00 UTC | None |
| **Domain Scraper Enhancement** | HOI Agent | May 11, 14:00 UTC | May 11, 18:00 UTC | BeautifulSoup4 |
| **Retry Logic + Backoff** | HOI Agent | May 11, 18:00 UTC | May 11, 20:00 UTC | None |
| **QA Dashboard (Live)** | HOI Agent | May 12, 08:00 UTC | May 12, 12:00 UTC | All above |
| **Test Run (5 agencies)** | HOI Agent | May 12, 14:00 UTC | May 12, 16:00 UTC | All modules |
| **Full Deployment (20 agencies)** | HOI Agent | May 12, 16:00 UTC | May 12, 20:00 UTC | Test run pass |

**Critical Path:** Hunter.io API key (DAF must procure by May 11, 08:00 UTC)

---

## Risk Register

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **Hunter.io Rate Limits** | Medium | HIGH — Collection stalls | Implement request throttling (1 req/sec), use credit pool monitoring |
| **LinkedIn IP Ban** | High | HIGH — Leadership data lost | Use rotating proxies + stealth browser + rate limiting (max 20 req/min) |
| **Government Portal Downtime** | Low | MEDIUM — Delays collection | Queue failed agencies, retry after 1 hour, fallback to cached data |
| **API Key Exhaustion** | Medium | HIGH — Collection incomplete | Monitor credit usage, implement pause/resume, procure backup API (Snov.io) |
| **CAPTCHA Blocks** | Medium | MEDIUM — Manual intervention needed | Integrate 2Captcha API ($1-3/1000), flag for manual review if budget constrained |
| **False Positive Contacts** | High | MEDIUM — Outreach failures | NeverBounce validation, confidence scoring, manual review for <70 score |
| **Data Merge Conflicts** | Low | LOW — Duplicate profiles | Implement deduplication by email/phone, master-record precedence rules |
| **ToS Violation (LinkedIn)** | Medium | CRITICAL — Legal risk | Use only public pages, no authenticated scraping, respect robots.txt, rate limit |
| **Proxy Service Downtime** | Low | MEDIUM — Collection pauses | Have fallback to direct requests (slower but functional) |

---

## Legal + ToS Compliance Notes

| Platform | ToS Status | Recommended Approach |
|----------|------------|---------------------|
| **LinkedIn** | ⚠️ Scraping prohibited (ToS §8.2) | Use only public company pages, no login, rate limit to 20 req/min, consider LinkedIn API (paid) |
| **Government Portals** | ✅ Generally permitted (public data) | Respect robots.txt, rate limit to 1 req/sec, identify bot in User-Agent |
| **Hunter.io API** | ✅ Commercial use allowed | Adhere to credit limits, no resale of data, comply with GDPR/PDPA |
| **NeverBounce API** | ✅ Commercial use allowed | Validate only business emails, no personal email verification without consent |

**Recommendation:** For Wave 1 (20 Tier A agencies), use **manual LinkedIn review** (compliant) + **automated domain scraping** (compliant) + **Hunter.io API** (compliant). Defer automated LinkedIn scraping until legal review complete.

---

## Next Steps (Immediate)

1. **DAF:** Procure Hunter.io API key ($49/mo plan, 2K credits) — Deadline: May 11, 08:00 UTC
2. **HOI Agent:** Implement email pattern inference module — Start: May 10, 14:00 UTC
3. **HOI Agent:** Build parallel worker framework (4 workers) — Start: May 10, 16:00 UTC
4. **DAF:** Review + approve ToS compliance approach (LinkedIn manual vs. automated) — Deadline: May 11, 12:00 UTC
5. **HOI Agent:** Test run on 5 agencies (not Tier A) — May 12, 14:00 UTC
6. **HOI Agent:** Full deployment on 20 Tier A agencies — May 12, 16:00 UTC

---

**Classification:** TLP:AMBER  
**Distribution:** DAF, CBO-01, HOI Agent  
**Retention:** Project (Wave 1 Pipeline)  

---

*Generated by HOI Agent Research Bot #2 — OSINT Process Optimization*  
*2026-05-10 12:25 UTC*

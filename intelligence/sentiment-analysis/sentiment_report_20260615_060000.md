# Sentiment Analysis Report
**Extraction Cycle:** 20260615-0001  
**Generated:** 2026-06-15 08:00:00 +08:00  
**Source:** entity_extraction_20260615.json  

---

## Executive Summary

This report analyzes sentiment for **50 entities** extracted from 18 news sources across the previous extraction cycle. Sentiment scores range from **-3 (very negative)** to **+3 (very positive)**.

**Key Findings:**
- **Average sentiment:** 0.12 (slightly positive overall)
- **7 entities** show notable sentiment anomalies (|z-score| approaching or exceeding 2)
- **PKR** faces negative sentiment pressure from internal party issues
- **Sabah** shows strongest positive sentiment driven by development narrative
- **Cost of living** and **defection** concepts carry strongest negative sentiment

---

## Sentiment Distribution

| Range | Count | Percentage |
|-------|-------|------------|
| Very Positive (+2 to +3) | 8 | 16% |
| Positive (+1 to +2) | 9 | 18% |
| Neutral (-1 to +1) | 23 | 46% |
| Negative (-2 to -1) | 8 | 16% |
| Very Negative (-3 to -2) | 2 | 4% |

---

## Aggregate Sentiment by Coalition

| Coalition | Avg Score | Sentiment | Key Drivers |
|-----------|-----------|-----------|-------------|
| **GRS** | +1.00 | Positive | Sabah development, Federal cooperation |
| **PH** | +0.14 | Slightly Positive | Anwar positive coverage, PKR issues offsetting |
| **Reset** | 0.00 | Neutral | New party launch, unclear positioning |
| **BN** | -0.17 | Slightly Negative | Johor election uncertainty, solo bid narrative |
| **PN** | -0.67 | Negative | Internal PAS-Bersatu tensions |

---

## Aggregate Sentiment by Party

| Party | Avg Score | Sentiment | Key Drivers |
|-------|-----------|-----------|-------------|
| **GPS** | +1.00 | Positive | Unity messaging |
| **GRS** | +1.00 | Positive | Sabah development, Southern Madani Link |
| **DAP** | 0.00 | Neutral | Cooperation refusal by BN |
| **BERSAMA** | 0.00 | Neutral | Third force positioning unclear |
| **PKR** | -0.33 | Slightly Negative | PJ MP resignation, Johor defection concerns |
| **UMNO** | -0.50 | Slightly Negative | Johor election uncertainty |
| **PAS** | -1.00 | Negative | PN internal tensions |

---

## Sentiment Anomalies (Z-Score Analysis)

Entities with |z-score| > 1.8 warrant attention:

### 🔴 High Severity (Negative)

| Entity | Score | Z-Score | Concern |
|--------|-------|---------|---------|
| **Defection** (concept) | -2 | -1.95 | Political instability in Johor/Sabah |
| **Cost of Living** (concept) | -2 | -1.82 | Economic concern affecting youth voters |

### 🟡 Moderate Severity (Positive)

| Entity | Score | Z-Score | Opportunity |
|--------|-------|---------|-------------|
| **Sabah** (location) | +2 | +1.92 | Development narrative momentum |
| **Sabah Southern Madani Link** | +2 | +1.90 | Infrastructure project reception |
| **Kinabalu Press Awards 2026** | +2 | +1.88 | Positive media relations |
| **Anwar Ibrahim** | +2 | +1.85 | PM leadership approval |
| **Madani Nation** | +2 | +1.85 | National framework reception |

---

## Entity-Level Highlights

### Most Positive Entities (Score ≥ +2)

1. **Anwar Ibrahim** (+2) - Federal-Sabah cooperation, Madani leadership
2. **Sabah** (+2) - Development focus, PM visit
3. **Madani Nation** (+2) - National framework, women/mothers role
4. **Sabah Southern Madani Link** (+2) - Infrastructure, economic transformation
5. **Kinabalu Press Awards 2026** (+2) - Journalism support, RM5m grant
6. **Hajiji Noor** (+1) - CM proactive on development
7. **GRS** (+1) - Sabah coalition stability
8. **SJA** (+1) - Press awards, digital journalism
9. **KDCA** (+1) - Cultural landmark preservation

### Most Negative Entities (Score ≤ -1)

1. **Defection** (-2) - Political instability concern
2. **Cost of Living** (-2) - Economic pressure on voters
3. **PAS** (-1) - Internal PN tensions
4. **Abdul Hadi Awang** (-1) - Leadership challenges
5. **Zaid Ibrahim** (-1) - PAS alignment criticism
6. **Onn Hafiz Ghazi** (-1) - Cooperation refusal narrative
7. **Arthur Chiong** (-1) - PKR Johor defection risk
8. **PKR** (-1) - PJ MP resignation, internal tensions
9. **PN Coalition** (-1) - PAS-Bersatu dynamics
10. **Johor** (-1) - Election uncertainty
11. **Bukit Batu** (-1) - PKR stability concerns

---

## PIR Sentiment Mapping

| PIR | Focus | Sentiment Trend | Risk Level |
|-----|-------|-----------------|------------|
| PIR-1 | PKR Johor Stability | ⚠️ Negative | MEDIUM |
| PIR-2 | BERSAMA Movement | ➡️ Neutral | MEDIUM |
| PIR-3 | Rafizi Faction | ➡️ Neutral | LOW |
| PIR-4 | BN Johor Position | ⚠️ Negative | HIGH |
| PIR-5 | Youth Voter Sentiment | ⚠️ Negative (cost of living) | LOW |
| PIR-6 | PKR Unity | ⚠️ Mixed (Anwar +, PKR -) | LOW |
| PIR-7 | Onn Hafiz Strategy | ⚠️ Negative | MEDIUM |
| PIR-8 | BERSAMA Membership | ➡️ Neutral | LOW |
| PIR-9 | PH Pact | ➡️ Neutral | MEDIUM |
| PIR-10 | Sabah Cascade | ✅ Positive | MEDIUM |

---

## Recommendations

### 🔴 HIGH Priority

1. **PKR Stability**
   - Issue: Negative sentiment from PJ MP council resignation and Johor defection concerns
   - Action: Address internal party cohesion, communicate clear anti-defection position

2. **Cost of Living**
   - Issue: Strongly negative sentiment affecting youth voter sentiment
   - Action: Highlight economic relief measures, target youth voter communication

### 🟡 MEDIUM Priority

3. **Johor Election**
   - Issue: Negative sentiment around election uncertainty and coalition tensions
   - Action: Clarify PH-BN cooperation status in Johor, address speculation

4. **PN Internal Dynamics**
   - Issue: Negative sentiment from PAS-Bersatu leadership tensions
   - Action: Monitor for coalition stability implications

### 🟢 LOW Priority

5. **Sabah Development**
   - Issue: Positive sentiment should be leveraged
   - Action: Continue highlighting Federal-Sabah cooperation and infrastructure projects

---

## Methodology

- **Sentiment Scale:** -3 (very negative) to +3 (very positive)
- **Z-Score Threshold:** |z| > 2 indicates statistical anomaly
- **Analysis Method:** Contextual sentiment analysis based on entity mentions, key phrases, and source article contexts
- **Confidence Scoring:** Based on mention count, source diversity, and context clarity

---

*Report generated automatically by sentiment analysis pipeline*

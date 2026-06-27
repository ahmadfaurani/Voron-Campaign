# SENTIMENT ANALYSIS REPORT
**Classification:** TLP:AMBER
**Report ID:** SENTIMENT-20260619_080124
**Generated:** 2026-06-19T08:01:24.578206Z
**Source Data:** 2026-06-19T000422Z_political_collection.json
**Entities Analyzed:** 118

---

## Executive Summary

**Overall Sentiment Landscape:**
- Mean Sentiment Score: 0.02 (Neutral)
- Positive Entities: 29 (24.6%)
- Negative Entities: 23 (19.5%)
- Neutral Entities: 66 (55.9%)

**Key Findings:**
- Anomalies Detected: 8 entities with z-score > 2.0
- Most Positive: Anti-Bullying Act (score: +1.5)
- Most Negative: cross-border crime (score: -1.5)

---

## Aggregate Sentiment by Coalition

| Coalition | Score | Label | Confidence | Entities |
|-----------|-------|-------|------------|----------|
| PH | +0.23 | Neutral | 0.8 | DAP, Amanah, PH |
| BN | -0.17 | Neutral | 0.8 | UMNO, Umno, BN |
| PN | -0.28 | Neutral | 0.8 | PAS, Bersatu, Perikatan Nasional, BERSATU, PN |

---

## Aggregate Sentiment by Entity Type

### PERSON
- **Mean Score:** -0.09 (Neutral)
- **Std Dev:** 0.25
- **Count:** 34
- **Range:** [-0.80, +0.20]

### ORGANIZATION
- **Mean Score:** -0.05 (Neutral)
- **Std Dev:** 0.18
- **Count:** 32
- **Range:** [-0.50, +0.30]

### LOCATION
- **Mean Score:** +0.00 (Neutral)
- **Std Dev:** 0.00
- **Count:** 32
- **Range:** [+0.00, +0.00]

### EVENT
- **Mean Score:** +0.26 (Neutral)
- **Std Dev:** 0.35
- **Count:** 9
- **Range:** [+0.00, +1.00]

### CONCEPT
- **Mean Score:** +0.36 (Neutral)
- **Std Dev:** 0.90
- **Count:** 11
- **Range:** [-1.50, +1.50]

---

## Sentiment Anomalies (Z-Score > 2.0)

| Entity | Type | Score | Z-Score | Severity | Direction |
|--------|------|-------|---------|----------|----------|
| cross-border crime | CONCEPT | -1.50 | -4.34 | HIGH | negative |
| Anti-Bullying Act | CONCEPT | +1.50 | +4.24 | HIGH | positive |
| domestic dispute | CONCEPT | -1.00 | -2.91 | MEDIUM | negative |
| World Cup | EVENT | +1.00 | +2.81 | MEDIUM | positive |
| green jobs | CONCEPT | +1.00 | +2.81 | MEDIUM | positive |
| strategic partnership | CONCEPT | +1.00 | +2.81 | MEDIUM | positive |
| unity | CONCEPT | +1.00 | +2.81 | MEDIUM | positive |
| Najib | PERSON | -0.80 | -2.33 | MEDIUM | negative |

---

## Most Positive Entities

| Entity | Type | Score | Confidence | Context |
|--------|------|-------|------------|---------|
| Anti-Bullying Act | CONCEPT | +1.50 | 0.6 | N/A |
| World Cup | EVENT | +1.00 | 0.6 | N/A |
| green jobs | CONCEPT | +1.00 | 0.6 | N/A |
| strategic partnership | CONCEPT | +1.00 | 0.6 | N/A |
| unity | CONCEPT | +1.00 | 0.6 | N/A |
| Official Visit | EVENT | +0.50 | 0.6 | N/A |
| QS World University Rankings | EVENT | +0.50 | 0.6 | N/A |
| direct flights | CONCEPT | +0.50 | 0.6 | N/A |
| energy security | CONCEPT | +0.50 | 0.6 | N/A |
| mental health | CONCEPT | +0.50 | 0.6 | N/A |

---

## Most Negative Entities

| Entity | Type | Score | Confidence | Context |
|--------|------|-------|------------|---------|
| cross-border crime | CONCEPT | -1.50 | 0.6 | N/A |
| domestic dispute | CONCEPT | -1.00 | 0.6 | N/A |
| Najib | PERSON | -0.80 | 0.6 | N/A |
| Donald Trump | PERSON | -0.50 | 0.6 | Former US President |
| Trump | PERSON | -0.50 | 0.6 | Former US President |
| MACC | ORGANIZATION | -0.50 | 0.6 | Government agency |
| Putin | PERSON | -0.40 | 0.6 | Russian President |
| Sanusi | PERSON | -0.40 | 0.6 | Opposition figure |
| PAS | ORGANIZATION | -0.40 | 0.6 | Opposition/Political party |
| Ahmad Zahid | PERSON | -0.30 | 0.5 | Deputy Prime Minister |

---

## Detailed Entity Sentiment Breakdown

### PERSON

| Entity | Score | Confidence | Emotion | Frame | PIR Relevance |
|--------|-------|------------|---------|-------|---------------|
| Anwar | +0.20 | 0.5 | neutral | neutral | - |
| Anwar Ibrahim | +0.20 | 0.5 | neutral | neutral | - |
| PM Anwar | +0.20 | 0.5 | neutral | neutral | - |
| Seri Anwar Ibrahim | +0.20 | 0.5 | neutral | neutral | - |
| Seri Dr Wan Azizah Wan Ismail | +0.20 | 0.5 | neutral | neutral | - |
| Dzulkefly Ahmad | +0.10 | 0.5 | neutral | neutral | - |
| Fahmi | +0.10 | 0.5 | neutral | neutral | - |
| Loke | +0.10 | 0.5 | neutral | neutral | - |
| Nancy | +0.10 | 0.5 | neutral | neutral | - |
| Nancy Shukri | +0.10 | 0.5 | neutral | neutral | - |
| Andrew Sheng | 0.00 | 0.5 | neutral | neutral | - |
| Anwar 
      Malaysia | 0.00 | 0.5 | neutral | neutral | - |
| Anwar 
      Russia | 0.00 | 0.5 | neutral | neutral | - |
| Anwar Arrives In Turkmenistan For Two | 0.00 | 0.5 | neutral | neutral | - |
| Fazzrudin Abdul Rahman | 0.00 | 0.5 | neutral | neutral | - |
| Fuad | 0.00 | 0.5 | neutral | neutral | - |
| Mashitah Hamidi | 0.00 | 0.5 | neutral | neutral | - |
| Mohd Tajuddin Mohd Rasdi | 0.00 | 0.5 | neutral | neutral | - |
| Nizam Abu Bakar Titingan | 0.00 | 0.5 | neutral | neutral | - |
| Onn Hafiz | 0.00 | 0.5 | neutral | neutral | PIR-7 |
| Roger | 0.00 | 0.5 | neutral | neutral | - |
| Tengku Zafrul | 0.00 | 0.5 | neutral | neutral | - |
| Zafrul | 0.00 | 0.5 | neutral | neutral | - |
| Ahmad Zahid | -0.30 | 0.5 | neutral | neutral | - |
| Azmin | -0.30 | 0.5 | neutral | neutral | - |
| Azmin Ali | -0.30 | 0.5 | neutral | neutral | - |
| Hamzah | -0.30 | 0.5 | neutral | neutral | - |
| Muhyiddin | -0.30 | 0.5 | neutral | neutral | - |
| Zahid | -0.30 | 0.5 | neutral | neutral | - |
| Putin | -0.40 | 0.6 | neutral | responsibility | - |
| Sanusi | -0.40 | 0.6 | neutral | responsibility | - |
| Donald Trump | -0.50 | 0.6 | neutral | responsibility | - |
| Trump | -0.50 | 0.6 | neutral | responsibility | - |
| Najib | -0.80 | 0.6 | surprise | responsibility | - |

### ORGANIZATION

| Entity | Score | Confidence | Emotion | Frame | PIR Relevance |
|--------|-------|------------|---------|-------|---------------|
| PH | +0.30 | 0.5 | neutral | responsibility | - |
| ASEAN | +0.20 | 0.5 | neutral | responsibility | - |
| Amanah | +0.20 | 0.5 | neutral | responsibility | - |
| DAP | +0.20 | 0.5 | neutral | responsibility | - |
| Petronas | +0.10 | 0.5 | neutral | responsibility | - |
| SCO | +0.10 | 0.5 | neutral | responsibility | - |
| ACEM | 0.00 | 0.5 | neutral | responsibility | - |
| BERSAMA | 0.00 | 0.5 | neutral | responsibility | PIR-2 |
| Bernama | 0.00 | 0.5 | neutral | responsibility | - |
| CIMB | 0.00 | 0.5 | neutral | responsibility | - |
| Daily Express | 0.00 | 0.5 | neutral | responsibility | - |
| GRS | 0.00 | 0.5 | neutral | responsibility | - |
| Malaysiakini | 0.00 | 0.5 | neutral | responsibility | - |
| NST | 0.00 | 0.5 | neutral | responsibility | - |
| PBS | 0.00 | 0.5 | neutral | responsibility | - |
| PERKESO | 0.00 | 0.5 | neutral | responsibility | - |
| PPj | 0.00 | 0.5 | neutral | responsibility | - |
| Putrajaya Corporation | 0.00 | 0.5 | neutral | responsibility | - |
| SUPP | 0.00 | 0.5 | neutral | responsibility | - |
| Socso | 0.00 | 0.5 | neutral | responsibility | - |
| Upko | 0.00 | 0.5 | neutral | responsibility | - |
| Warisan | 0.00 | 0.5 | neutral | responsibility | - |
| BN | -0.10 | 0.5 | neutral | responsibility | PIR-4 |
| MCMC | -0.20 | 0.5 | neutral | responsibility | - |
| PN | -0.20 | 0.5 | neutral | responsibility | - |
| Perikatan Nasional | -0.20 | 0.5 | neutral | responsibility | - |
| UMNO | -0.20 | 0.5 | neutral | responsibility | PIR-4, PIR-7 |
| Umno | -0.20 | 0.5 | neutral | responsibility | PIR-4, PIR-7 |
| BERSATU | -0.30 | 0.5 | neutral | responsibility | PIR-2 |
| Bersatu | -0.30 | 0.5 | neutral | responsibility | PIR-2 |
| PAS | -0.40 | 0.6 | neutral | responsibility | - |
| MACC | -0.50 | 0.6 | neutral | responsibility | - |

### LOCATION

| Entity | Score | Confidence | Emotion | Frame | PIR Relevance |
|--------|-------|------------|---------|-------|---------------|
| Bintulu | 0.00 | 0.5 | neutral | neutral | - |
| Borneo | 0.00 | 0.5 | neutral | neutral | - |
| Brazil | 0.00 | 0.5 | neutral | neutral | - |
| Brunei | 0.00 | 0.5 | neutral | neutral | - |
| Bukit Bintang | 0.00 | 0.5 | neutral | neutral | - |
| Carey Island | 0.00 | 0.5 | neutral | neutral | - |
| Cheras | 0.00 | 0.5 | neutral | neutral | - |
| China | 0.00 | 0.5 | neutral | neutral | - |
| East Coast | 0.00 | 0.5 | neutral | neutral | - |
| Germany | 0.00 | 0.5 | neutral | neutral | - |
| Johor | 0.00 | 0.5 | neutral | neutral | - |
| KK | 0.00 | 0.5 | neutral | neutral | - |
| Kazan | 0.00 | 0.5 | neutral | neutral | - |
| Kedah | 0.00 | 0.5 | neutral | neutral | - |
| Kota Kinabalu | 0.00 | 0.5 | neutral | neutral | - |
| Kpg Sagah | 0.00 | 0.5 | neutral | neutral | - |
| Kuala Lumpur | 0.00 | 0.5 | neutral | neutral | - |
| Malaysia | 0.00 | 0.5 | neutral | neutral | - |
| Miri | 0.00 | 0.5 | neutral | neutral | - |
| N Sembilan | 0.00 | 0.5 | neutral | neutral | - |
| Penang | 0.00 | 0.5 | neutral | neutral | - |
| Petaling Jaya | 0.00 | 0.5 | neutral | neutral | - |
| Pudu | 0.00 | 0.5 | neutral | neutral | - |
| Putrajaya | 0.00 | 0.5 | neutral | neutral | - |
| Russia | 0.00 | 0.5 | neutral | neutral | - |
| Sabah | 0.00 | 0.5 | neutral | neutral | - |
| Sarawak | 0.00 | 0.5 | neutral | neutral | - |
| Selangor | 0.00 | 0.5 | neutral | neutral | - |
| Senai | 0.00 | 0.5 | neutral | neutral | - |
| Sibu | 0.00 | 0.5 | neutral | neutral | - |
| Tupong | 0.00 | 0.5 | neutral | neutral | - |
| Turkmenistan | 0.00 | 0.5 | neutral | neutral | - |

### EVENT

| Entity | Score | Confidence | Emotion | Frame | PIR Relevance |
|--------|-------|------------|---------|-------|---------------|
| World Cup | +1.00 | 0.6 | anticipation | neutral | - |
| Official Visit | +0.50 | 0.6 | neutral | neutral | - |
| QS World University Rankings | +0.50 | 0.6 | neutral | neutral | - |
| ASEAN | +0.20 | 0.5 | neutral | neutral | - |
| SCO | +0.10 | 0.5 | neutral | neutral | - |
| GE16 | 0.00 | 0.5 | neutral | neutral | - |
| Johor Polls | 0.00 | 0.5 | neutral | neutral | - |
| STPM 2025 | 0.00 | 0.5 | neutral | neutral | - |
| State Polls 2026 | 0.00 | 0.5 | neutral | neutral | - |

### CONCEPT

| Entity | Score | Confidence | Emotion | Frame | PIR Relevance |
|--------|-------|------------|---------|-------|---------------|
| Anti-Bullying Act | +1.50 | 0.6 | anticipation | neutral | - |
| green jobs | +1.00 | 0.6 | anticipation | neutral | - |
| strategic partnership | +1.00 | 0.6 | anticipation | neutral | - |
| unity | +1.00 | 0.6 | anticipation | neutral | - |
| direct flights | +0.50 | 0.6 | neutral | neutral | - |
| energy security | +0.50 | 0.6 | neutral | neutral | - |
| mental health | +0.50 | 0.6 | neutral | neutral | - |
| visa-free travel | +0.50 | 0.6 | neutral | neutral | - |
| membership | 0.00 | 0.5 | neutral | neutral | - |
| domestic dispute | -1.00 | 0.6 | surprise | neutral | - |
| cross-border crime | -1.50 | 0.6 | surprise | neutral | - |

---

## Methodology Notes

- **Sentiment Scale:** 7-point Likert scale (-3 to +3)
- **Anomaly Detection:** Z-score threshold > 2.0 (Medium), > 3.0 (High)
- **Confidence Scoring:** Based on baseline strength and context keyword matching
- **Emotion Detection:** Primary emotion derived from sentiment intensity and context
- **Framing Detection:** News frame classification based on entity type and context
- **Coalition Aggregation:** Weighted average of member party sentiments

---

*Report generated by HOI Agent Political Monitoring Workstream*
*Classification: TLP:AMBER - Internal Operational Use*
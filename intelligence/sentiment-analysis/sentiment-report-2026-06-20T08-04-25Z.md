# Sentiment Analysis Report

**Generated:** 2026-06-20T08-04-25Z  
**Source File:** /home/p62operator/.openclaw/workspace-hoi/intelligence/entities/entities-2026-06-20T00-00-50Z.json  
**Analysis Scope:** All entities from previous extraction cycle

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Entities Analyzed | 96 |
| Average Sentiment | -0.03 |
| Anomalies Detected | 9 |
| Sentiment Range | -3 (Very Negative) to +3 (Very Positive) |

---

## Aggregate Sentiment by Coalition/Party

### 🔴 Pakatan Harapan (PH)

- **Average Sentiment:** -0.25
- **Entities Analyzed:** 4
- **Distribution:** 
  - Positive: 0
  - Neutral: 3
  - Negative: 1

**Entities:**
- 🟡 PKR (ORGANIZATION): Score 0
- 🔴 PKR Unity (CONCEPT): Score -1
- 🟡 DAP (ORGANIZATION): Score 0
- 🟡 Amanah (ORGANIZATION): Score 0

### 🔴 Perikatan Nasional (PN)

- **Average Sentiment:** -0.33
- **Entities Analyzed:** 3
- **Distribution:** 
  - Positive: 0
  - Neutral: 2
  - Negative: 1

**Entities:**
- 🔴 PAS (ORGANIZATION): Score -1
- 🟡 Bersatu (ORGANIZATION): Score 0
- 🟡 Bersatu (ORGANIZATION): Score 0

### 🔴 Barisan Nasional (BN)

- **Average Sentiment:** -1.0
- **Entities Analyzed:** 1
- **Distribution:** 
  - Positive: 0
  - Neutral: 0
  - Negative: 1

**Entities:**
- 🔴 UMNO (ORGANIZATION): Score -1

### 🟢 Gabungan Rakyat Sabah (GRS)

- **Average Sentiment:** 1.17
- **Entities Analyzed:** 6
- **Distribution:** 
  - Positive: 5
  - Neutral: 1
  - Negative: 0

**Entities:**
- 🟢 Upko (ORGANIZATION): Score 1
- 🟢 Upko Joins GRS (EVENT): Score 1
- 🟡 Warisan (ORGANIZATION): Score 0
- 🟢 Gabungan Rakyat Sabah (GRS) (ORGANIZATION): Score 2
- 🟢 Upko Joins GRS (EVENT): Score 1
- 🟢 GRS (Gabungan Rakyat Sabah) (CONCEPT): Score 2

### 🟡 Third Force

- **Average Sentiment:** 0.0
- **Entities Analyzed:** 3
- **Distribution:** 
  - Positive: 0
  - Neutral: 3
  - Negative: 0

**Entities:**
- 🟡 BERSAMA (ORGANIZATION): Score 0
- 🟡 BERSAMA Political Venture Launch (EVENT): Score 0
- 🟡 Wawasan Negara (ORGANIZATION): Score 0

---

## Sentiment Anomalies (Z-Score > 2)

| Entity | Type | Score | Z-Score | Direction |
|--------|------|-------|---------|----------|
| Mojuntin | PERSON | 2 | 2.27 | positive |
| Gabungan Rakyat Sabah (GRS) | ORGANIZATION | 2 | 2.27 | positive |
| MCMC | ORGANIZATION | -2 | -2.2 | negative |
| FMT | ORGANIZATION | -2 | -2.2 | negative |
| Petaling Jaya | LOCATION | -2 | -2.2 | negative |
| PN Leadership Tussle | EVENT | -2 | -2.2 | negative |
| Defection | CONCEPT | -3 | -3.32 | negative |
| GRS (Gabungan Rakyat Sabah) | CONCEPT | 2 | 2.27 | positive |
| Bullying | CONCEPT | -3 | -3.32 | negative |

---

## Detailed Entity Sentiments

### By Entity Type

#### PERSON

| Name | Score | Reasoning | Sources |
|------|-------|-----------|--------|
| 🟢 Mojuntin | 2 | positive context indicators; unity/consolidation theme | daily-express |
| 🟢 Mat Sabu | 1 | positive context indicators | fmt |
| 🟢 Ewon Benedick | 1 | positive context indicators | daily-express, borneo-post |
| 🟢 Nizam Abu Bakar Titingan | 1 | positive context indicators | daily-express |
| 🟡 Anwar Ibrahim | 0 | neutral context | bernama, malaysiakini, borneo-post |
| 🟡 Rafizi Ramli | 0 | neutral context | malaysiakini |
| 🟡 Nik Nazmi | 0 | neutral context | malaysiakini |
| 🟡 Saifuddin | 0 | neutral context | malaysiakini |
| 🟡 Hamzah | 0 | neutral context | malaysiakini |
| 🟡 Fuziah | 0 | neutral context; election context | malaysiakini |
| 🟡 Onn Hafiz | 0 | neutral context | config |
| 🟡 Fuad | 0 | neutral context | daily-express |
| 🟡 Fahmi | 0 | neutral context | bernama |
| 🟡 Herve Renard | 0 | neutral context | bernama |
| 🟡 Shahril | 0 | neutral context | malaysiakini |
| 🟡 Lee Chean Chung | 0 | neutral context | malaysiakini |
| 🟡 Abdul Hadi Awang | 0 | neutral context | fmt |
| 🟡 Fatimah | 0 | neutral context | borneo-post |
| 🟡 Yadim | 0 | neutral context | borneo-post |
| 🔴 Nancy Shukri | -1 | negative context indicators | fmt, borneo-post |

*... and 1 more PERSON entities*

#### ORGANIZATION

| Name | Score | Reasoning | Sources |
|------|-------|-----------|--------|
| 🟢 Gabungan Rakyat Sabah (GRS) | 2 | positive context indicators; unity/consolidation theme | daily-express, borneo-post |
| 🟢 Pakatan Harapan (PH) | 1 | positive context indicators; election context | fmt, bernama |
| 🟢 Upko | 1 | positive context indicators | daily-express, borneo-post |
| 🟢 Petronas | 1 | positive context indicators | fmt, bernama |
| 🟢 Malaysiakini | 1 | positive context indicators | malaysiakini |
| 🟡 PKR | 0 | neutral context; election context | malaysiakini, bernama |
| 🟡 BERSAMA | 0 | neutral context | malaysiakini |
| 🟡 Wawasan Negara | 0 | neutral context | malaysiakini |
| 🟡 Bersatu | 0 | neutral context; election context | malaysiakini, fmt, nst |
| 🟡 Amanah | 0 | neutral context; election context | bernama, fmt |
| 🟡 DAP | 0 | neutral context | malaysiakini |
| 🟡 Warisan | 0 | neutral context | daily-express |
| 🟡 BN (Barisan Nasional) | 0 | neutral context | config |
| 🟡 INVOKE | 0 | neutral context | config |
| 🟡 MAG | 0 | neutral context | daily-express, borneo-post |
| 🟡 Bernama | 0 | neutral context | bernama, malaysiakini |
| 🟡 NST | 0 | neutral context | nst |
| 🟡 Daily Express | 0 | neutral context | daily-express |
| 🟡 Borneo Post | 0 | neutral context | borneo-post |
| 🟡 Yadim | 0 | neutral context | borneo-post |

*... and 9 more ORGANIZATION entities*

#### LOCATION

| Name | Score | Reasoning | Sources |
|------|-------|-----------|--------|
| 🟢 Johor | 1 | positive context indicators; election context | bernama, malaysiakini, config |
| 🟢 Sabah | 1 | positive context indicators | daily-express, borneo-post, config |
| 🟢 Sarawak | 1 | positive context indicators | borneo-post |
| 🟢 Turkmenistan | 1 | positive context indicators; unity/consolidation theme | bernama, fmt |
| 🟢 Belaga | 1 | positive context indicators | the-star |
| 🟡 Negri Sembilan | 0 | neutral context; election context | malaysiakini, the-star |
| 🟡 Kuala Lumpur | 0 | neutral context | bernama, borneo-post, daily-express |
| 🟡 Kota Kinabalu | 0 | neutral context | daily-express, borneo-post |
| 🟡 Kuching | 0 | neutral context | borneo-post |
| 🟡 Putrajaya | 0 | neutral context | daily-express, malaysiakini |
| 🟡 Penang | 0 | neutral context | the-star |
| 🟡 Ipoh | 0 | neutral context | bernama |
| 🟡 Monterrey, Mexico | 0 | neutral context | bernama |
| 🟡 Limbang | 0 | neutral context | borneo-post |
| 🟡 Lawas | 0 | neutral context | borneo-post |
| 🟡 Dalat | 0 | neutral context | borneo-post |
| 🟡 Mengkibol | 0 | neutral context; election context | malaysiakini |
| 🟡 Hulu Langat | 0 | neutral context | fmt |
| 🔴 Selangor | -1 | negative context indicators | malaysiakini |
| 🔴 Petaling Jaya | -2 | negative context indicators; conflict theme | the-star |

#### EVENT

| Name | Score | Reasoning | Sources |
|------|-------|-----------|--------|
| 🟢 Johor State Election (PRN2026) | 1 | positive context indicators; election context | bernama, malaysiakini, the-star |
| 🟢 Upko Joins GRS | 1 | positive context indicators | daily-express, borneo-post |
| 🟢 PM Anwar Turkmenistan Visit | 1 | positive context indicators | bernama, fmt |
| 🟢 Sabah SME Fest | 1 | positive context indicators | daily-express |
| 🟡 Negri Sembilan State Election | 0 | neutral context; election context | malaysiakini, the-star |
| 🟡 BERSAMA Political Venture Launch | 0 | neutral context; election context | malaysiakini |
| 🟡 World Cup 2026 | 0 | neutral context | bernama, nst, borneo-post |
| 🟡 Sarawak Media Conference | 0 | neutral context | borneo-post |
| 🟡 US-Iran Nuclear Deal | 0 | neutral context | bernama, fmt, borneo-post |
| 🔴 PN Leadership Tussle | -2 | negative context indicators; conflict theme | the-star, malaysiakini, fmt |

#### CONCEPT

| Name | Score | Reasoning | Sources |
|------|-------|-----------|--------|
| 🟢 GRS (Gabungan Rakyat Sabah) | 2 | positive context indicators; unity/consolidation theme | daily-express, borneo-post |
| 🟢 Candidate Recruitment | 1 | positive context indicators; election context | malaysiakini, bernama |
| 🟢 Malaysian Face | 1 | positive context indicators; unity/consolidation theme | malaysiakini |
| 🟡 Third Force | 0 | neutral context | malaysiakini |
| 🟡 PH Pact | 0 | neutral context; election context | fmt, bernama |
| 🟡 Seat Negotiation | 0 | neutral context; election context | config, malaysiakini |
| 🟡 Youth Voter | 0 | neutral context; election context | config, bernama |
| 🟡 Damage Control | 0 | neutral context; unity/consolidation theme | config |
| 🟡 Solo Bid | 0 | neutral context | config |
| 🟡 PN Logo Control | 0 | neutral context; election context | nst |
| 🔴 PKR Unity | -1 | negative context indicators; unity/consolidation theme; election context | malaysiakini |
| 🔴 Cost of Living | -1 | negative context indicators | config, borneo-post |
| 🔴 Inflation | -1 | negative context indicators | borneo-post |
| 🔴 Misinformation | -1 | negative context indicators | bernama, daily-express |
| 🔴 Defection | -3 | negative context indicators; defection concern | config, daily-express |
| 🔴 Bullying | -3 | negative context indicators | bernama |

---

## Methodology

- **Scoring Range:** -3 (Very Negative) to +3 (Very Positive)
- **Method:** Lexicon-based sentiment analysis with political context weighting
- **Anomaly Detection:** Z-score method with threshold of 2.0 standard deviations
- **Aggregate Calculation:** Weighted average of entity sentiments within coalitions

---

*Report generated by OpenClaw Sentiment Analysis Module*

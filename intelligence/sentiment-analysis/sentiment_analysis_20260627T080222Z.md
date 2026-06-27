# Sentiment Analysis Report

**Report Timestamp:** 20260627T080222Z
**Source Extraction:** 20260627T060030Z
**Source File:** entities_20260627T060030Z.json

## Overall Statistics

| Metric | Value |
|--------|-------|
| Total Entities | 35 |
| Mean Score | 0.257 |
| Median Score | 0 |
| Std Deviation | 1.221 |
| Min Score | -1 |
| Max Score | 3 |
| Anomalies Detected | 2 |
| Entities with Context | 35 |

*Score range: -3 (very negative) to +3 (very positive)*

## Entity Sentiments by Type

### PERSON

| Entity | Score | Polarity | Pos Indicators | Neg Indicators |
|--------|-------|----------|----------------|----------------|
| Ahmad Zahid | 0 | 0.0 | 0 | 0 |
| Anwar | 1 | 0.2 | 3 | 0 |
| Mohamad | 0 | 0.0 | 1 | 2 |
| Pairin | 3 | 0.5 | 0 | 0 |

### ORGANIZATION

| Entity | Score | Polarity | Pos Indicators | Neg Indicators |
|--------|-------|----------|----------------|----------------|
| BERSAMA | 1 | 0.25 | 1 | 0 |
| Bernama | -1 | -0.2 | 1 | 4 |
| Bersatu | -1 | -0.2 | 1 | 3 |
| Daily Express | -1 | -0.2 | 0 | 4 |
| FMT | 0 | 0.095 | 0 | 1 |
| Malaysiakini | -1 | -0.2 | 0 | 4 |
| NST | -1 | -0.2 | 1 | 3 |
| PH | 0 | 0.0 | 0 | 1 |
| Petronas | 3 | 0.5 | 0 | 0 |
| UMNO | -1 | -0.2 | 0 | 2 |

### LOCATION

| Entity | Score | Polarity | Pos Indicators | Neg Indicators |
|--------|-------|----------|----------------|----------------|
| Iran | -1 | -0.2 | 1 | 3 |
| Johor | -1 | -0.2 | 1 | 3 |
| Kuala Lumpur | 2 | 0.438 | 1 | 0 |
| Kuching | 0 | 0.04 | 2 | 1 |
| Layang-Layang | -1 | -0.2 | 1 | 3 |
| Likas | 1 | 0.2 | 3 | 0 |
| Malaysia | -1 | -0.2 | 0 | 4 |
| Myanmar | -1 | -0.215 | 1 | 2 |
| Petaling Jaya | 0 | 0.0 | 0 | 0 |
| Sabah | 1 | 0.25 | 0 | 1 |
| Sarawak | 1 | 0.233 | 1 | 1 |
| Tawau | -1 | -0.2 | 3 | 10 |

### EVENT

| Entity | Score | Polarity | Pos Indicators | Neg Indicators |
|--------|-------|----------|----------------|----------------|
| Johor Polls | 2 | 0.34 | 2 | 1 |
| Johor Polls 2026 | 2 | 0.4 | 0 | 0 |
| State Polls 2026 | 1 | 0.25 | 0 | 0 |
| World Cup | 0 | 0.0 | 0 | 0 |

### CONCEPT

| Entity | Score | Polarity | Pos Indicators | Neg Indicators |
|--------|-------|----------|----------------|----------------|
| MSMEs | 1 | 0.2 | 4 | 0 |
| e-commerce law | 1 | 0.2 | 4 | 0 |
| grassroots | 1 | 0.15 | 1 | 1 |
| oil and gas | 1 | 0.2 | 3 | 0 |
| subsidised diesel | -1 | -0.2 | 0 | 4 |

## Coalition/Party Aggregate Sentiments

### PH
- **Parties:** PH
- **Average Score:** 0
- **Individual Scores:** [0]

### BN
- **Parties:** UMNO
- **Average Score:** -1
- **Individual Scores:** [-1]

### BERSAMA
- **Parties:** BERSAMA
- **Average Score:** 1
- **Individual Scores:** [1]

## Sentiment Anomalies (z-score > 2)

| Entity Type | Entity | Score | Z-Score | Direction |
|-------------|--------|-------|---------|----------|
| PERSON | Pairin | 3 | 2.246 | positive |
| ORGANIZATION | Petronas | 3 | 2.246 | positive |

---
*Methodology: TextBlob polarity analysis with keyword indicator weighting on context snippets where entities are mentioned*

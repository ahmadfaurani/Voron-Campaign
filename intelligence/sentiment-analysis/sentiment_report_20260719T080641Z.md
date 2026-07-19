# Sentiment Analysis Report

**Classification:** TLP:AMBER
**Report Timestamp:** 20260719T080641Z
**Extraction ID:** ext_20260719_003046_phase1
**Extraction Source:** 2026-07-19T06:03:48Z
**Collection Cycle:** 2026-07-19T003046Z
**Source Count:** 23
**Analysis Method:** VADER Sentiment Analysis on fresh context snippets extracted from 2026-07-19 raw collection
**Score Range:** -3 (very negative) to +3 (very positive)
**Anomaly Threshold:** |z-score| > 2

> **Data-freshness note:** The 2026-07-19 extraction produced Phase-1 entity name lists
> only; Phase-2 per-entity context files were not regenerated for this cycle. To produce a
> genuine 2026-07-19 sentiment signal, context snippets were extracted directly from the
> 2026-07-19 raw source collection and scored with VADER. Coalition/party metadata sourced
> from the canonical per-entity files (2026-07-16 Phase-2 set) plus an analyst-extended
> affiliation map for newly-extracted figures.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Roster Entities (Phase-1 names) | 346 |
| Analysis Entities (merged) | 331 |
| Canonical Entities (from index) | 78 |
| New Entities (this cycle) | 253 |
| Roster Names Matched to Canonical | 70 |
| Sources Processed | 23 |
| Entities with Context | 308 |
| Entities without Context (fallback) | 23 |
| Overall Mean Sentiment | +0.287 |
| Overall Std Deviation | 1.009 |
| Overall Median Sentiment | +0.000 |
| Overall Raw Mean | 0.0584 |
| Overall Raw Std Dev | 0.2279 |
| Sentiment Range | [-3, +3] |
| Positive Entities | 95 |
| Neutral Entities | 205 |
| Negative Entities | 31 |
| Anomalies Detected | 26 |
| Coalitions Analyzed | 8 |
| Parties Analyzed | 13 |

### Sentiment Distribution

```
Positive (95)  ███████████████████████████████████████████████████████████████████████████████████████████████
Neutral  (205)  █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
Negative (31)  ███████████████████████████████
```

---

## Coalition Aggregate Sentiment

| Coalition | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range |
|-----------|:-:|------|:----------:|:-------:|:--------:|:-----:|
| PH | +0 | Neutral | 0.0785 | 0.1542 | 18 | [-0.192, 0.402] |
| BN | +0 | Neutral | 0.0575 | 0.0889 | 12 | [-0.063, 0.226] |
| BERSAMA | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| GRS | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| PEJUANG | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] |
| WARISAN | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| PN | -1 | Slightly Negative | -0.2014 | 0.3027 | 7 | [-0.778, 0.000] |
| GPS | -1 | Slightly Negative | -0.2083 | 0.3608 | 3 | [-0.625, 0.000] |

### Coalition Entities
- **PH** (+0, Neutral): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Anthony Loke, Maszlee, Fahmi Fadzil, Mohamad Sabu, Syed Saddiq, Steven Sim, Tan See Leng, Democratic Action Party, Malaysia United Democratic Alliance, Pakatan Harapan, Parti Amanah Negara, Parti Keadilan Rakyat
- **BN** (+0, Neutral): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Onn Hafiz, Najib Razak, Wee Ka Siong, Barisan Nasional, Malaysian Chinese Association, Malaysian Indian Congress, United Malays National Organisation
- **BERSAMA** (+0, Neutral): Parti Bersama
- **GRS** (+0, Neutral): GRS
- **PEJUANG** (+0, Neutral): Mahathir Mohamad, Pejuang
- **WARISAN** (+0, Neutral): Parti Warisan
- **PN** (-1, Slightly Negative): Muhyiddin Yassin, Abdul Hadi Awang, Azanna Ahmad Kamar, Sanusi, Parti Islam Se-Malaysia, Parti Pribumi Bersatu Malaysia, Perikatan Nasional
- **GPS** (-1, Slightly Negative): Sim Kui Hian, Tiong King Sing, Gabungan Parti Sarawak

---

## Party Aggregate Sentiment

| Party | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range | Coalition |
|-------|:-:|------|:----------:|:-------:|:--------:|:-----:|:---------:|
| MIC | +1 | Slightly Positive | 0.2255 | 0.0000 | 1 | [0.226, 0.226] | BN |
| DAP | +1 | Slightly Positive | 0.1162 | 0.2186 | 3 | [-0.099, 0.338] | PH |
| PKR | +1 | Slightly Positive | 0.1073 | 0.1559 | 9 | [0.000, 0.402] | PH |
| MUDA | +0 | Neutral | 0.0581 | 0.0822 | 2 | [0.000, 0.116] | PH |
| UMNO | +0 | Neutral | 0.0528 | 0.0846 | 8 | [-0.063, 0.184] | BN |
| BERSAMA | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | BERSAMA |
| Pejuang | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | PEJUANG |
| Warisan | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | WARISAN |
| MCA | +0 | Neutral | -0.0070 | 0.0100 | 2 | [-0.014, 0.000] | BN |
| AMANAH | +0 | Neutral | -0.0640 | 0.1109 | 3 | [-0.192, 0.000] | PH |
| PAS | -1 | Slightly Negative | -0.1588 | 0.2666 | 3 | [-0.467, 0.000] | PN |
| BERSATU | -2 | Negative | -0.3014 | 0.4140 | 3 | [-0.778, -0.035] | PN |
| GPS | -2 | Negative | -0.3125 | 0.4419 | 2 | [-0.625, 0.000] | GPS |

### Party Entities
- **MIC** (+1, Slightly Positive, → BN): Malaysian Indian Congress
- **DAP** (+1, Slightly Positive, → PH): Anthony Loke, Steven Sim, Democratic Action Party
- **PKR** (+1, Slightly Positive, → PH): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Fahmi Fadzil, Tan See Leng, Parti Keadilan Rakyat
- **MUDA** (+0, Neutral, → PH): Syed Saddiq, Malaysia United Democratic Alliance
- **UMNO** (+0, Neutral, → BN): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Onn Hafiz, Najib Razak, United Malays National Organisation
- **BERSAMA** (+0, Neutral, → BERSAMA): Parti Bersama
- **Pejuang** (+0, Neutral, → PEJUANG): Mahathir Mohamad
- **Warisan** (+0, Neutral, → WARISAN): Parti Warisan
- **MCA** (+0, Neutral, → BN): Wee Ka Siong, Malaysian Chinese Association
- **AMANAH** (+0, Neutral, → PH): Maszlee, Mohamad Sabu, Parti Amanah Negara
- **PAS** (-1, Slightly Negative, → PN): Abdul Hadi Awang, Sanusi, Parti Islam Se-Malaysia
- **BERSATU** (-2, Negative, → PN): Muhyiddin Yassin, Azanna Ahmad Kamar, Parti Pribumi Bersatu Malaysia
- **GPS** (-2, Negative, → GPS): Sim Kui Hian, Tiong King Sing

---

## Sentiment Anomalies (|z-score| > 2)

**26 anomalies detected.**

| # | Entity | Type | Score | Label | Z-Score | Direction | Coalition | Party | Contexts |
|---|--------|------|:-----:|-------|:-------:|:---------:|-----------|:------:|:--------:|
| 1 | WAN IFRA ASIA MEDIA AWARDS 2025 | EVENT | +3 | Very Positive | 3.7543 | positive | N/A | — | 1 |
| 2 | Azanna Ahmad Kamar | PERSON | -3 | Very Negative | -3.6710 | negative | PN | BERSATU | 4 |
| 3 | Myanmar | LOCATION | -3 | Very Negative | -3.6684 | negative | N/A | — | 1 |
| 4 | MRT | ORGANIZATION | +3 | Very Positive | 3.3309 | positive | N/A | — | 1 |
| 5 | Wall Street | LOCATION | -3 | Very Negative | -3.2428 | negative | N/A | — | 4 |
| 6 | PRS | ORGANIZATION | +3 | Very Positive | 3.1435 | positive | N/A | — | 2 |
| 7 | Court case | EVENT | +3 | Very Positive | 3.1295 | positive | N/A | — | 1 |
| 8 | Borneo Post | ORGANIZATION | -3 | Very Negative | -3.0467 | negative | N/A | — | 1 |
| 9 | Tiong King Sing | PERSON | -3 | Very Negative | -2.9980 | negative | GPS | GPS | 1 |
| 10 | Onn Hafiz 56-seats solo bid | CONCEPT | +3 | Very Positive | 2.9615 | positive | N/A | — | 1 |
| 11 | N9 Polls | LOCATION | +3 | Very Positive | 2.7469 | positive | N/A | — | 4 |
| 12 | green technology | CONCEPT | +3 | Very Positive | 2.6855 | positive | N/A | — | 1 |
| 13 | renewable energy | CONCEPT | +3 | Very Positive | 2.6855 | positive | N/A | — | 1 |
| 14 | West Asia | LOCATION | -2 | Negative | -2.6654 | negative | N/A | — | 3 |
| 15 | Kangar | LOCATION | -2 | Negative | -2.6044 | negative | N/A | — | 5 |
| 16 | Khatijah Abdullah | PERSON | +3 | Very Positive | 2.4736 | positive | N/A | — | 4 |
| 17 | mandate | CONCEPT | +3 | Very Positive | 2.4679 | positive | N/A | — | 3 |
| 18 | Abdul Hadi Awang | PERSON | -2 | Negative | -2.3034 | negative | PN | PAS | 5 |
| 19 | Brazil | LOCATION | +2 | Positive | 2.2463 | positive | N/A | — | 4 |
| 20 | United States | LOCATION | +2 | Positive | 2.2152 | positive | N/A | — | 7 |
| 21 | Inflation | CONCEPT | +2 | Positive | 2.1866 | positive | N/A | — | 3 |
| 22 | Hearing | EVENT | +2 | Positive | 2.1665 | positive | N/A | — | 4 |
| 23 | Samsuri | PERSON | +2 | Positive | 2.1564 | positive | N/A | — | 1 |
| 24 | DVS | ORGANIZATION | +2 | Positive | 2.0831 | positive | N/A | — | 5 |
| 25 | Arrest | EVENT | -2 | Negative | -2.0428 | negative | N/A | — | 11 |
| 26 | Zainudin | PERSON | -2 | Negative | -2.0196 | negative | N/A | — | 1 |

---

## Entity Sentiments by Type

### PERSON

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Khatijah Abdullah | +3 | Very Positive | 0.6222 | 2.4736 | ⚠️ | 4 | — | — | ✚ |
| Samsuri | +2 | Positive | 0.5499 | 2.1564 | ⚠️ | 1 | — | — | ✚ |
| Seri Anwar Ibrahim | +2 | Positive | 0.5122 | 1.9910 |  | 3 | — | — | ✚ |
| Anthony Loke Siew Fook | +2 | Positive | 0.4354 | 1.6540 |  | 2 | — | — | ✚ |
| Tan See Leng | +2 | Positive | 0.4019 | 1.5070 |  | 3 | PH | PKR | ✚ |
| Saddiq Walks Free | +2 | Positive | 0.3804 | 1.4127 |  | 1 | — | — | ✚ |
| Syed Saddiq Walks Free | +2 | Positive | 0.3804 | 1.4127 |  | 1 | — | — | ✚ |
| Steven Sim | +2 | Positive | 0.3382 | 1.2276 |  | 1 | PH | DAP | ✚ |
| Fuziah Salleh | +2 | Positive | 0.3284 | 1.1846 |  | 3 | — | — | ✚ |
| Seri Mohamad Hasan | +1 | Slightly Positive | 0.2924 | 1.0266 |  | 2 | — | — | ✚ |
| Anwar Ibrahim | +1 | Slightly Positive | 0.2592 | 0.8809 |  | 17 | PH | PKR |  |
| Salleh | +1 | Slightly Positive | 0.2463 | 0.8244 |  | 2 | — | — | ✚ |
| Mohamad Hasan | +1 | Slightly Positive | 0.1842 | 0.5519 |  | 11 | BN | UMNO |  |
| Seri Aminuddin Harun | +1 | Slightly Positive | 0.1407 | 0.3610 |  | 7 | — | — | ✚ |
| Tun | +1 | Slightly Positive | 0.1307 | 0.3172 |  | 28 | — | — | ✚ |
| Khairy Jamaluddin | +1 | Slightly Positive | 0.1277 | 0.3040 |  | 8 | BN | UMNO |  |
| Onn Hafiz | +1 | Slightly Positive | 0.1273 | 0.3022 |  | 8 | BN | UMNO | ✚ |
| Datuk Seri | +1 | Slightly Positive | 0.1172 | 0.2579 |  | 15 | — | — | ✚ |
| Syed Saddiq | +1 | Slightly Positive | 0.1162 | 0.2535 |  | 12 | PH | MUDA | ✚ |
| Datuk | +1 | Slightly Positive | 0.1130 | 0.2395 |  | 21 | — | — | ✚ |
| Alyaa Alhadjri | +1 | Slightly Positive | 0.1027 | 0.1943 |  | 1 | — | — | ✚ |
| B Nantha Kumar | +0 | Neutral | 0.0772 | 0.0824 |  | 1 | — | — | ✚ |
| Rajeentheran Suntheralingam | +0 | Neutral | 0.0478 | -0.0466 |  | 4 | — | — | ✚ |
| Aminuddin Harun | +0 | Neutral | 0.0449 | -0.0593 |  | 22 | PH | PKR |  |
| Ab Rauf Yusoh | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | BN | UMNO |  |
| Hassan Abdul Karim | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | PH | PKR |  |
| Jalaluddin Abdul Rahman | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | BN | UMNO |  |
| Mahathir Mohamad | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | PEJUANG | Pejuang |  |
| Mohd Ghazali Sabari | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | — | — |  |
| Nik Nazmi Nik Ahmad | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | PH | PKR |  |
| Nurul Izzah Anwar | +0 | Neutral | 0.0000 | -0.2563 |  | 3 | PH | PKR |  |
| Rafizi Ramli | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | PH | PKR |  |
| Sim Kui Hian | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | GPS | GPS |  |
| Abdul Razak | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Ahmad Idid | +0 | Neutral | 0.0000 | -0.2563 |  | 3 | — | — | ✚ |
| Alzafny Ahmad | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Mohamad Rafie Ab Malek | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Mohamad Rafie Abd Malek | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Mohd Faizal Ramli | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Muhammad Nazri Kassim | +0 | Neutral | 0.0000 | -0.2563 |  | 5 | — | — | ✚ |
| Razali Abu Samah | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Jalaluddin Alias | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | — | — | ✚ |
| Datuk Seri Johari Abdul Ghani | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Datuk Seri Utama Aminuddin Harun | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Datuk Tun Faisal Ismail | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Maszlee | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | PH | AMANAH | ✚ |
| Fahmi Fadzil | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | PH | PKR | ✚ |
| Johari Abdul | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Mohd Fared Mohd Khalid | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Najib Razak | +0 | Neutral | 0.0000 | -0.2563 |  | 8 | BN | UMNO | ✚ |
| Ramlan Harun | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | — | — | ✚ |
| Sanusi | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | PN | PAS | ✚ |
| Sarafudin Badlishah | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Seri Dr Ahmad Zahid | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Seri Jalaluddin Alias | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Seri Johari Abdul Ghani | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Seri Utama Aminuddin Harun | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Syed Ahmad Idid | +0 | Neutral | 0.0000 | -0.2563 |  | 3 | — | — | ✚ |
| Tengku Sarafudin Badlishah | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Wee Ka Siong | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | BN | MCA | ✚ |
| Muhyiddin Yassin | +0 | Neutral | -0.0348 | -0.4090 |  | 9 | PN | BERSATU |  |
| Ahmad Zahid Hamidi | +0 | Neutral | -0.0626 | -0.5309 |  | 14 | BN | UMNO |  |
| Anthony Loke | +0 | Neutral | -0.0988 | -0.6898 |  | 6 | PH | DAP | ✚ |
| Mohamad Sabu | -1 | Slightly Negative | -0.1921 | -1.0991 |  | 4 | PH | AMANAH | ✚ |
| Tan Sri | -1 | Slightly Negative | -0.2862 | -1.5120 |  | 3 | — | — | ✚ |
| Datuk Seri Nancy Shukri | -2 | Negative | -0.3802 | -1.9244 |  | 1 | — | — | ✚ |
| Seri Nancy Shukri | -2 | Negative | -0.3802 | -1.9244 |  | 1 | — | — | ✚ |
| Zainudin | -2 | Negative | -0.4019 | -2.0196 | ⚠️ | 1 | — | — | ✚ |
| Abdul Hadi Awang | -2 | Negative | -0.4666 | -2.3034 | ⚠️ | 5 | PN | PAS | ✚ |
| Tiong King Sing | -3 | Very Negative | -0.6249 | -2.9980 | ⚠️ | 1 | GPS | GPS |  |
| Azanna Ahmad Kamar | -3 | Very Negative | -0.7783 | -3.6710 | ⚠️ | 4 | PN | BERSATU | ✚ |

### ORGANIZATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| MRT | +3 | Very Positive | 0.8176 | 3.3309 | ⚠️ | 1 | — | — | ✚ |
| PRS | +3 | Very Positive | 0.7749 | 3.1435 | ⚠️ | 2 | — | — | ✚ |
| DVS | +2 | Positive | 0.5332 | 2.0831 | ⚠️ | 5 | — | — | ✚ |
| JPA | +2 | Positive | 0.5084 | 1.9743 |  | 8 | — | — | ✚ |
| Malay Mail | +2 | Positive | 0.4926 | 1.9050 |  | 1 | — | — | ✚ |
| KWSP | +2 | Positive | 0.4627 | 1.7738 |  | 4 | — | — | ✚ |
| Parliament | +2 | Positive | 0.4524 | 1.7286 |  | 5 | — | — | ✚ |
| DBKK | +2 | Positive | 0.4019 | 1.5070 |  | 2 | — | — | ✚ |
| ASEAN | +2 | Positive | 0.3766 | 1.3960 |  | 11 | — | — |  |
| JPJ | +2 | Positive | 0.3220 | 1.1565 |  | 6 | — | — | ✚ |
| Parti Keadilan Rakyat | +1 | Slightly Positive | 0.2596 | 0.8827 |  | 17 | PH | PKR |  |
| Suara Keadilan | +1 | Slightly Positive | 0.2463 | 0.8244 |  | 2 | — | — | ✚ |
| Malaysian Indian Congress | +1 | Slightly Positive | 0.2255 | 0.7331 |  | 18 | BN | MIC |  |
| Apple | +1 | Slightly Positive | 0.1858 | 0.5589 |  | 3 | — | — | ✚ |
| RCI | +1 | Slightly Positive | 0.1782 | 0.5256 |  | 9 | — | — | ✚ |
| Pakatan Harapan | +1 | Slightly Positive | 0.1754 | 0.5133 |  | 30 | PH | — |  |
| AirBorneo | +1 | Slightly Positive | 0.1702 | 0.4905 |  | 4 | — | — | ✚ |
| Media Mulia | +1 | Slightly Positive | 0.1555 | 0.4260 |  | 6 | — | — | ✚ |
| KPJ | +1 | Slightly Positive | 0.1547 | 0.4225 |  | 4 | — | — | ✚ |
| MOH | +1 | Slightly Positive | 0.1318 | 0.3220 |  | 25 | — | — | ✚ |
| Boeing | +1 | Slightly Positive | 0.1194 | 0.2676 |  | 7 | — | — | ✚ |
| The Star | +1 | Slightly Positive | 0.1101 | 0.2268 |  | 4 | — | — | ✚ |
| Democratic Action Party | +1 | Slightly Positive | 0.1092 | 0.2228 |  | 30 | PH | DAP |  |
| Bernama | +0 | Neutral | 0.0997 | 0.1812 |  | 21 | — | — | ✚ |
| UN | +0 | Neutral | 0.0923 | 0.1487 |  | 30 | — | — | ✚ |
| mStar | +0 | Neutral | 0.0886 | 0.1325 |  | 8 | — | — | ✚ |
| EC | +0 | Neutral | 0.0862 | 0.1219 |  | 30 | — | — | ✚ |
| Google | +0 | Neutral | 0.0796 | 0.0930 |  | 7 | — | — | ✚ |
| IMU | +0 | Neutral | 0.0706 | 0.0535 |  | 7 | — | — | ✚ |
| State Government | +0 | Neutral | 0.0633 | 0.0215 |  | 2 | — | — | ✚ |
| Barisan Nasional | +0 | Neutral | 0.0561 | -0.0101 |  | 30 | BN | — |  |
| Keadilan | +0 | Neutral | 0.0543 | -0.0180 |  | 5 | — | — | ✚ |
| CodeBlue | +0 | Neutral | 0.0506 | -0.0343 |  | 4 | — | — | ✚ |
| United Malays National Organisation | +0 | Neutral | 0.0456 | -0.0562 |  | 16 | BN | UMNO |  |
| Daily Express | +0 | Neutral | 0.0354 | -0.1010 |  | 3 | — | — | ✚ |
| TikTok | +0 | Neutral | 0.0164 | -0.1843 |  | 30 | — | — | ✚ |
| DUN | +0 | Neutral | 0.0161 | -0.1856 |  | 30 | — | — | ✚ |
| NGO | +0 | Neutral | 0.0010 | -0.2519 |  | 27 | — | — | ✚ |
| Gabungan Parti Sarawak | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | GPS | — |  |
| GRS | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | GRS | — |  |
| HAWANA | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | — | — |  |
| Malaysia United Democratic Alliance | +0 | Neutral | 0.0000 | -0.2563 |  | 23 | PH | MUDA |  |
| Ministry of Finance | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | — | — |  |
| Ministry of Home Affairs | +0 | Neutral | 0.0000 | -0.2563 |  | 6 | — | — |  |
| Parti Amanah Negara | +0 | Neutral | 0.0000 | -0.2563 |  | 3 | PH | AMANAH |  |
| Parti Bersama | +0 | Neutral | 0.0000 | -0.2563 |  | 11 | BERSAMA | BERSAMA |  |
| Parti Warisan | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | WARISAN | Warisan |  |
| Pejuang | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | PEJUANG | — |  |
| BURSA | +0 | Neutral | 0.0000 | -0.2563 |  | 6 | — | — | ✚ |
| Bursa Malaysia | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Cabinet | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| KLK | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| KPKM | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | — | — | ✚ |
| Kementerian Kesihatan | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Kementerian Kesihatan Malaysia | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Kosmo | +0 | Neutral | 0.0000 | -0.2563 |  | 6 | — | — | ✚ |
| MalaysiaGazette | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | — | — | ✚ |
| Malaysiakini | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | — | — | ✚ |
| Perodua | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Petronas | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | — | — | ✚ |
| Sinar Harian | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | — | — | ✚ |
| Spotify | +0 | Neutral | 0.0000 | -0.2563 |  | 5 | — | — | ✚ |
| Utusan Malaysia | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Vulcan Post | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | — | — | ✚ |
| World of Buzz | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| PRN | +0 | Neutral | -0.0005 | -0.2585 |  | 30 | — | — | ✚ |
| PDRM | +0 | Neutral | -0.0009 | -0.2602 |  | 2 | — | — | ✚ |
| EU | +0 | Neutral | -0.0023 | -0.2664 |  | 26 | — | — | ✚ |
| Parti Islam Se-Malaysia | +0 | Neutral | -0.0097 | -0.2988 |  | 30 | PN | PAS |  |
| Malaysian Chinese Association | +0 | Neutral | -0.0141 | -0.3181 |  | 11 | BN | MCA |  |
| Perikatan Nasional | +0 | Neutral | -0.0296 | -0.3861 |  | 30 | PN | — |  |
| NST | +0 | Neutral | -0.0395 | -0.4296 |  | 30 | — | — | ✚ |
| MCMC | +0 | Neutral | -0.0450 | -0.4537 |  | 9 | — | — | ✚ |
| FIFA | +0 | Neutral | -0.0452 | -0.4546 |  | 13 | — | — | ✚ |
| AFP | +0 | Neutral | -0.0553 | -0.4989 |  | 10 | — | — | ✚ |
| BuzzKini | +0 | Neutral | -0.0584 | -0.5125 |  | 4 | — | — | ✚ |
| Tropicana | +0 | Neutral | -0.0820 | -0.6160 |  | 4 | — | — | ✚ |
| Grab | +0 | Neutral | -0.0897 | -0.6498 |  | 5 | — | — | ✚ |
| Parti Pribumi Bersatu Malaysia | +0 | Neutral | -0.0911 | -0.6560 |  | 30 | PN | BERSATU |  |
| The Edge Malaysia | -1 | Slightly Negative | -0.1133 | -0.7534 |  | 3 | — | — | ✚ |
| Suruhanjaya Pencegahan Rasuah Malaysia | -1 | Slightly Negative | -0.1144 | -0.7582 |  | 12 | — | — |  |
| Suruhanjaya Pilihan Raya | -1 | Slightly Negative | -0.1170 | -0.7696 |  | 22 | — | — |  |
| Anadolu | -1 | Slightly Negative | -0.2384 | -1.3022 |  | 2 | — | — | ✚ |
| CNA | -2 | Negative | -0.3014 | -1.5786 |  | 3 | — | — | ✚ |
| Borneo Post | -3 | Very Negative | -0.6360 | -3.0467 | ⚠️ | 1 | — | — | ✚ |

### LOCATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| N9 Polls | +3 | Very Positive | 0.6845 | 2.7469 | ⚠️ | 4 | — | — | ✚ |
| Brazil | +2 | Positive | 0.5704 | 2.2463 | ⚠️ | 4 | — | — | ✚ |
| United States | +2 | Positive | 0.5633 | 2.2152 | ⚠️ | 7 | — | — | ✚ |
| Kuching | +2 | Positive | 0.4833 | 1.8642 |  | 5 | — | — |  |
| George Town | +2 | Positive | 0.4588 | 1.7567 |  | 1 | — | — | ✚ |
| India | +2 | Positive | 0.3502 | 1.2802 |  | 13 | — | — | ✚ |
| Klang | +1 | Slightly Positive | 0.2423 | 0.8068 |  | 7 | — | — | ✚ |
| Penang | +1 | Slightly Positive | 0.2093 | 0.6620 |  | 13 | — | — |  |
| Spain | +1 | Slightly Positive | 0.2064 | 0.6493 |  | 15 | — | — | ✚ |
| Sarawak | +1 | Slightly Positive | 0.2021 | 0.6304 |  | 23 | — | — |  |
| Parliament House | +1 | Slightly Positive | 0.1740 | 0.5071 |  | 13 | — | — |  |
| Vietnam | +1 | Slightly Positive | 0.1391 | 0.3540 |  | 4 | — | — | ✚ |
| JB | +1 | Slightly Positive | 0.1272 | 0.3018 |  | 18 | — | — | ✚ |
| Linggi | +1 | Slightly Positive | 0.1259 | 0.2961 |  | 17 | — | — |  |
| South Korea | +1 | Slightly Positive | 0.1258 | 0.2957 |  | 5 | — | — | ✚ |
| Kudat | +1 | Slightly Positive | 0.1250 | 0.2922 |  | 6 | — | — | ✚ |
| Korea | +1 | Slightly Positive | 0.1201 | 0.2707 |  | 8 | — | — | ✚ |
| Johor | +1 | Slightly Positive | 0.1186 | 0.2641 |  | 30 | — | — |  |
| Rantau | +1 | Slightly Positive | 0.1122 | 0.2360 |  | 3 | — | — |  |
| Singapore | +1 | Slightly Positive | 0.1104 | 0.2281 |  | 16 | — | — | ✚ |
| Sabah | +1 | Slightly Positive | 0.1048 | 0.2035 |  | 22 | — | — |  |
| Shah Alam | +1 | Slightly Positive | 0.1036 | 0.1983 |  | 13 | — | — | ✚ |
| Petaling Jaya | +1 | Slightly Positive | 0.1014 | 0.1886 |  | 8 | — | — | ✚ |
| Negri Sembilan | +1 | Slightly Positive | 0.1005 | 0.1847 |  | 4 | — | — | ✚ |
| UK | +0 | Neutral | 0.0785 | 0.0881 |  | 30 | — | — | ✚ |
| Thailand | +0 | Neutral | 0.0713 | 0.0566 |  | 8 | — | — | ✚ |
| Middle East | +0 | Neutral | 0.0611 | 0.0118 |  | 2 | — | — | ✚ |
| Malaysia | +0 | Neutral | 0.0554 | -0.0132 |  | 30 | — | — | ✚ |
| France | +0 | Neutral | 0.0502 | -0.0360 |  | 13 | — | — | ✚ |
| Muar | +0 | Neutral | 0.0478 | -0.0466 |  | 9 | — | — | ✚ |
| Silicon Valley | +0 | Neutral | 0.0344 | -0.1053 |  | 3 | — | — | ✚ |
| Argentina | +0 | Neutral | 0.0280 | -0.1334 |  | 27 | — | — | ✚ |
| Selangor | +0 | Neutral | 0.0215 | -0.1619 |  | 17 | — | — |  |
| Putrajaya | +0 | Neutral | 0.0135 | -0.1970 |  | 15 | — | — | ✚ |
| China | +0 | Neutral | 0.0070 | -0.2256 |  | 30 | — | — | ✚ |
| Kuala Lumpur | +0 | Neutral | 0.0032 | -0.2422 |  | 30 | — | — |  |
| N14 | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — |  |
| Pasir Gudang | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | — | — |  |
| Pertang | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — |  |
| Alor Setar | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | — | — | ✚ |
| Banting | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | — | — | ✚ |
| Batu Pahat | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Beaufort | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Beluran | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Betong | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Bintulu | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Brunei | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Bukit Gasing | +0 | Neutral | 0.0000 | -0.2563 |  | 3 | — | — | ✚ |
| Cameron Highlands | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Dungun | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Germany | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | — | — | ✚ |
| Gombak | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Hulu Selangor | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Ipoh | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | — | — | ✚ |
| Kelantan | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Kemaman | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Kota Bharu | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Kota Tinggi | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Kuala Selangor | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Kuala Terengganu | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Kuantan | +0 | Neutral | 0.0000 | -0.2563 |  | 7 | — | — | ✚ |
| Kulai | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Kunak | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Lahad Datu | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Limbang | +0 | Neutral | 0.0000 | -0.2563 |  | 3 | — | — | ✚ |
| Lipis | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Maran | +0 | Neutral | 0.0000 | -0.2563 |  | 3 | — | — | ✚ |
| Mersing | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Mexico | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| Pahang | +0 | Neutral | 0.0000 | -0.2563 |  | 9 | — | — | ✚ |
| Pasir Puteh | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Penampang | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Perlis | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Pontian | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Putatan | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Ranau | +0 | Neutral | 0.0000 | -0.2563 |  | 5 | — | — | ✚ |
| Rompin | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Samarahan | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Sandakan | +0 | Neutral | 0.0000 | -0.2563 |  | 3 | — | — | ✚ |
| Sarikei | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Segamat | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Semporna | +0 | Neutral | 0.0000 | -0.2563 |  | 5 | — | — | ✚ |
| Sepang | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Serian | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Strait of Hormuz | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Tambunan | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Tawau | +0 | Neutral | 0.0000 | -0.2563 |  | 3 | — | — | ✚ |
| Tenom | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Terengganu | +0 | Neutral | 0.0000 | -0.2563 |  | 6 | — | — | ✚ |
| Japan | +0 | Neutral | -0.0131 | -0.3137 |  | 10 | — | — | ✚ |
| Negeri Sembilan | +0 | Neutral | -0.0202 | -0.3449 |  | 30 | — | — |  |
| Perak | +0 | Neutral | -0.0356 | -0.4125 |  | 14 | — | — |  |
| Kedah | +0 | Neutral | -0.0463 | -0.4594 |  | 14 | — | — | ✚ |
| Kota Kinabalu | +0 | Neutral | -0.0523 | -0.4857 |  | 7 | — | — |  |
| England | +0 | Neutral | -0.0826 | -0.6187 |  | 30 | — | — | ✚ |
| Melaka | +0 | Neutral | -0.0856 | -0.6318 |  | 30 | — | — |  |
| US | -1 | Slightly Negative | -0.1197 | -0.7814 |  | 30 | — | — | ✚ |
| Venezuela | -1 | Slightly Negative | -0.1498 | -0.9135 |  | 9 | — | — | ✚ |
| Seremban | -1 | Slightly Negative | -0.1532 | -0.9284 |  | 13 | — | — | ✚ |
| Iran | -1 | Slightly Negative | -0.2010 | -1.1381 |  | 30 | — | — | ✚ |
| Keningau | -1 | Slightly Negative | -0.2284 | -1.2584 |  | 4 | — | — | ✚ |
| Istanbul | -1 | Slightly Negative | -0.2384 | -1.3022 |  | 2 | — | — | ✚ |
| Russia | -1 | Slightly Negative | -0.2436 | -1.3251 |  | 9 | — | — | ✚ |
| Miri | -1 | Slightly Negative | -0.2585 | -1.3904 |  | 5 | — | — | ✚ |
| Indonesia | -1 | Slightly Negative | -0.2601 | -1.3974 |  | 12 | — | — | ✚ |
| Sibu | -1 | Slightly Negative | -0.2651 | -1.4194 |  | 12 | — | — | ✚ |
| Kangar | -2 | Negative | -0.5352 | -2.6044 | ⚠️ | 5 | — | — | ✚ |
| West Asia | -2 | Negative | -0.5491 | -2.6654 | ⚠️ | 3 | — | — | ✚ |
| Wall Street | -3 | Very Negative | -0.6807 | -3.2428 | ⚠️ | 4 | — | — | ✚ |
| Myanmar | -3 | Very Negative | -0.7777 | -3.6684 | ⚠️ | 1 | — | — | ✚ |

### EVENT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| WAN IFRA ASIA MEDIA AWARDS 2025 | +3 | Very Positive | 0.9141 | 3.7543 | ⚠️ | 1 | — | — | ✚ |
| Court case | +3 | Very Positive | 0.7717 | 3.1295 | ⚠️ | 1 | — | — | ✚ |
| Hearing | +2 | Positive | 0.5522 | 2.1665 | ⚠️ | 4 | — | — | ✚ |
| FIFA World Cup 2026 | +2 | Positive | 0.4744 | 1.8251 |  | 3 | — | — | ✚ |
| Appeal | +2 | Positive | 0.3699 | 1.3666 |  | 6 | — | — | ✚ |
| Federal Court | +2 | Positive | 0.3486 | 1.2732 |  | 2 | — | — | ✚ |
| Trial | +2 | Positive | 0.3097 | 1.1025 |  | 9 | — | — | ✚ |
| nomination day | +1 | Slightly Positive | 0.2864 | 1.0003 |  | 3 | — | — | ✚ |
| Charged | +1 | Slightly Positive | 0.2774 | 0.9608 |  | 3 | — | — | ✚ |
| World Cup | +1 | Slightly Positive | 0.2134 | 0.6800 |  | 28 | — | — | ✚ |
| campaign | +1 | Slightly Positive | 0.2062 | 0.6484 |  | 17 | — | — |  |
| GE16 | +1 | Slightly Positive | 0.2003 | 0.6225 |  | 1 | — | — | ✚ |
| State Polls 2026 | +1 | Slightly Positive | 0.1895 | 0.5751 |  | 3 | — | — | ✚ |
| Probe | +1 | Slightly Positive | 0.1762 | 0.5168 |  | 3 | — | — | ✚ |
| BN Candidate Announcement (NS) | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | — | — |  |
| ceramah | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | — | — |  |
| HAWANA X TM Media Event | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | — | — |  |
| Johor State Election | +0 | Neutral | 0.0000 | -0.2563 |  | 9 | — | — |  |
| kempen | +0 | Neutral | 0.0000 | -0.2563 |  | 13 | — | — |  |
| majlis | +0 | Neutral | 0.0000 | -0.2563 |  | 10 | — | — |  |
| Negeri Sembilan State Election 2026 | +0 | Neutral | 0.0000 | -0.2563 |  | 22 | — | — |  |
| Sarawak State Election 2026 | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | — | — |  |
| walkabout | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | — | — |  |
| PRN Negeri | +0 | Neutral | 0.0000 | -0.2563 |  | 20 | — | — | ✚ |
| Piala Dunia | +0 | Neutral | 0.0000 | -0.2563 |  | 14 | — | — | ✚ |
| Pilihan Raya Negeri Johor | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| Summit | +0 | Neutral | 0.0000 | -0.2563 |  | 8 | — | — | ✚ |
| pilihan raya | +0 | Neutral | 0.0000 | -0.2563 |  | 11 | — | — | ✚ |
| pilihan raya negeri | +0 | Neutral | 0.0000 | -0.2563 |  | 10 | — | — | ✚ |
| press conference | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| semi-finals | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — | ✚ |
| sidang akhbar | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | — | — | ✚ |
| event | +0 | Neutral | -0.0330 | -0.4011 |  | 20 | — | — |  |
| rally | +0 | Neutral | -0.0631 | -0.5331 |  | 6 | — | — |  |
| Investigation | +0 | Neutral | -0.0697 | -0.5621 |  | 8 | — | — | ✚ |
| election | +0 | Neutral | -0.0727 | -0.5752 |  | 20 | — | — | ✚ |
| 2026 Elections | +0 | Neutral | -0.0850 | -0.6292 |  | 4 | — | — | ✚ |
| state election | -1 | Slightly Negative | -0.1859 | -1.0719 |  | 11 | — | — | ✚ |
| Arrest | -2 | Negative | -0.4072 | -2.0428 | ⚠️ | 11 | — | — | ✚ |

### CONCEPT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Onn Hafiz 56-seats solo bid | +3 | Very Positive | 0.7334 | 2.9615 | ⚠️ | 1 | — | — |  |
| green technology | +3 | Very Positive | 0.6705 | 2.6855 | ⚠️ | 1 | — | — | ✚ |
| renewable energy | +3 | Very Positive | 0.6705 | 2.6855 | ⚠️ | 1 | — | — | ✚ |
| mandate | +3 | Very Positive | 0.6209 | 2.4679 | ⚠️ | 3 | — | — | ✚ |
| Inflation | +2 | Positive | 0.5568 | 2.1866 | ⚠️ | 3 | — | — | ✚ |
| artificial intelligence | +2 | Positive | 0.4939 | 1.9107 |  | 1 | — | — | ✚ |
| copyright | +2 | Positive | 0.4814 | 1.8558 |  | 11 | — | — | ✚ |
| grassroots | +2 | Positive | 0.4588 | 1.7567 |  | 1 | — | — | ✚ |
| oil and gas | +1 | Slightly Positive | 0.2500 | 0.8406 |  | 1 | — | — | ✚ |
| Super El Nino food security | +1 | Slightly Positive | 0.2229 | 0.7217 |  | 0 | — | — |  |
| MADANI government | +1 | Slightly Positive | 0.2212 | 0.7142 |  | 15 | — | — |  |
| opposition | +1 | Slightly Positive | 0.1748 | 0.5107 |  | 9 | — | — | ✚ |
| Wealth tax | +1 | Slightly Positive | 0.1482 | 0.3939 |  | 0 | — | — |  |
| Bersatu own logo in N9 | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | — | — |  |
| Cost of living | +0 | Neutral | 0.0000 | -0.2563 |  | 3 | — | — |  |
| Service tax | +0 | Neutral | 0.0000 | -0.2563 |  | 1 | — | — |  |
| Third force movement | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | — | — |  |
| UEC recognition | +0 | Neutral | 0.0000 | -0.2563 |  | 0 | — | — |  |
| Reformasi | +0 | Neutral | 0.0000 | -0.2563 |  | 8 | — | — | ✚ |
| TVET | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | — | — | ✚ |
| fertiliser price | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| perpaduan | +0 | Neutral | 0.0000 | -0.2563 |  | 4 | — | — | ✚ |
| pork supply | +0 | Neutral | 0.0000 | -0.2563 |  | 2 | — | — | ✚ |
| AI | +0 | Neutral | -0.0066 | -0.2852 |  | 30 | — | — | ✚ |
| Subsidies & welfare aid | +0 | Neutral | -0.0161 | -0.3269 |  | 17 | — | — |  |
| water supply | -2 | Negative | -0.3612 | -1.8410 |  | 1 | — | — | ✚ |

---

## Methodology

1. **Entity Source:** Loaded from the 2026-07-19T003046Z extraction roster (346 Phase-1 entity names) plus the 78 canonical entities from the per-entity index. Roster names were merged into canonical entities by normalized name/alias matching (honorific-stripped); unmerged names were added as new entities (253 new).
2. **Context Extraction:** For each entity, search variants (canonical name + aliases + roster matches) were located in the 2026-07-19 raw source collection (23 sources, 23 processed, ~793205 chars). A context window (~140+170 chars) was extracted around each mention (markdown stripped, de-duplicated, capped at 30/entity).
3. **Sentiment Scoring:** Applied VADER to each context snippet; entity sentiment = mean compound across snippets.
4. **Score Mapping:** VADER compound (-1..+1) → 7-point Likert (-3..+3): +3 ≥0.6, +2 ≥0.3, +1 ≥0.1, 0 (-0.1..0.1), -1 >-0.3, -2 >-0.6, -3 ≤-0.6.
5. **Anomaly Detection:** Z-score on raw compound vs overall mean/std; flagged when |z| > 2.
6. **Coalition/Party Aggregation:** Persons + political-party/coalition orgs mapped via per-entity metadata and affiliation maps (FIGURE_AFFILIATIONS, ORG_TO_COALITION, analyst-extended NEW_FIGURE_AFFIL).

---

*Report generated by OpenCLaw Sentiment Analysis Pipeline (sentiment-analysis skill)*
*VADER: Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.*

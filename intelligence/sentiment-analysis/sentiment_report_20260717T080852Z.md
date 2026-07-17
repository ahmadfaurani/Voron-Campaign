# Sentiment Analysis Report

**Classification:** TLP:AMBER
**Report Timestamp:** 20260717T080852Z
**Extraction ID:** ext_20260717_001255_phase1
**Extraction Source:** 2026-07-17T06:10:14Z
**Collection Cycle:** 2026-07-17T001255Z
**Source Count:** 23
**Analysis Method:** VADER Sentiment Analysis on fresh context snippets extracted from 2026-07-17 raw collection
**Score Range:** -3 (very negative) to +3 (very positive)
**Anomaly Threshold:** |z-score| > 2

> **Data-freshness note:** The 2026-07-17 extraction produced Phase-1 entity name lists
> only; Phase-2 per-entity context files were not regenerated for this cycle. To produce a
> genuine 2026-07-17 sentiment signal, context snippets were extracted directly from the
> 2026-07-17 raw source collection and scored with VADER. Coalition/party metadata sourced
> from the canonical per-entity files (2026-07-16 Phase-2 set) plus an analyst-extended
> affiliation map for newly-extracted figures.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Roster Entities (Phase-1 names) | 297 |
| Analysis Entities (merged) | 278 |
| Canonical Entities (from index) | 78 |
| New Entities (this cycle) | 200 |
| Roster Names Matched to Canonical | 70 |
| Sources Processed | 23 |
| Entities with Context | 260 |
| Entities without Context (fallback) | 18 |
| Overall Mean Sentiment | +0.205 |
| Overall Std Deviation | 1.067 |
| Overall Median Sentiment | +0.000 |
| Overall Raw Mean | 0.0476 |
| Overall Raw Std Dev | 0.2403 |
| Sentiment Range | [-3, +3] |
| Positive Entities | 69 |
| Neutral Entities | 171 |
| Negative Entities | 38 |
| Anomalies Detected | 18 |
| Coalitions Analyzed | 8 |
| Parties Analyzed | 13 |

### Sentiment Distribution

```
Positive (69)  █████████████████████████████████████████████████████████████████████
Neutral  (171)  ███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
Negative (38)  ██████████████████████████████████████
```

---

## Coalition Aggregate Sentiment

| Coalition | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range |
|-----------|:-:|------|:----------:|:-------:|:--------:|:-----:|
| BN | +0 | Neutral | 0.0551 | 0.1278 | 12 | [-0.073, 0.400] |
| BERSAMA | +0 | Neutral | 0.0350 | 0.0000 | 1 | [0.035, 0.035] |
| PH | +0 | Neutral | 0.0186 | 0.0987 | 17 | [-0.192, 0.308] |
| GRS | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| WARISAN | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| PEJUANG | +0 | Neutral | -0.0786 | 0.1112 | 2 | [-0.157, 0.000] |
| PN | -1 | Slightly Negative | -0.1061 | 0.2431 | 5 | [-0.525, 0.072] |
| GPS | -1 | Slightly Negative | -0.2083 | 0.3608 | 3 | [-0.625, 0.000] |

### Coalition Entities
- **BN** (+0, Neutral): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Asyraf Wajdi Dusuki, Shamsul Anuar Nasarah, Najib, Barisan Nasional, Malaysian Chinese Association, Malaysian Indian Congress, United Malays National Organisation
- **BERSAMA** (+0, Neutral): Parti Bersama
- **PH** (+0, Neutral): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Anthony Loke, Maszlee, Fahmi Fadzil, Hannah Yeoh, Mohamad Sabu, Syed Saddiq, Democratic Action Party, Malaysia United Democratic Alliance, Pakatan Harapan, Parti Amanah Negara, Parti Keadilan Rakyat
- **GRS** (+0, Neutral): GRS
- **WARISAN** (+0, Neutral): Parti Warisan
- **PEJUANG** (+0, Neutral): Mahathir Mohamad, Pejuang
- **PN** (-1, Slightly Negative): Muhyiddin Yassin, Mas Ermieyati Samsudin, Parti Islam Se-Malaysia, Parti Pribumi Bersatu Malaysia, Perikatan Nasional
- **GPS** (-1, Slightly Negative): Sim Kui Hian, Tiong King Sing, Gabungan Parti Sarawak

---

## Party Aggregate Sentiment

| Party | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range | Coalition |
|-------|:-:|------|:----------:|:-------:|:--------:|:-----:|:---------:|
| DAP | +1 | Slightly Positive | 0.1311 | 0.1590 | 3 | [0.000, 0.308] | PH |
| MIC | +1 | Slightly Positive | 0.1296 | 0.0000 | 1 | [0.130, 0.130] | BN |
| UMNO | +0 | Neutral | 0.0657 | 0.1392 | 9 | [-0.046, 0.400] | BN |
| PAS | +0 | Neutral | 0.0528 | 0.0000 | 1 | [0.053, 0.053] | PN |
| BERSAMA | +0 | Neutral | 0.0350 | 0.0000 | 1 | [0.035, 0.035] | BERSAMA |
| MUDA | +0 | Neutral | 0.0346 | 0.0058 | 2 | [0.030, 0.039] | PH |
| PKR | +0 | Neutral | 0.0102 | 0.0511 | 8 | [-0.074, 0.105] | PH |
| Warisan | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | WARISAN |
| AMANAH | +0 | Neutral | -0.0640 | 0.1109 | 3 | [-0.192, 0.000] | PH |
| MCA | +0 | Neutral | -0.0728 | 0.0000 | 1 | [-0.073, -0.073] | BN |
| Pejuang | -1 | Slightly Negative | -0.1572 | 0.0000 | 1 | [-0.157, -0.157] | PEJUANG |
| BERSATU | -1 | Slightly Negative | -0.1714 | 0.3138 | 3 | [-0.525, 0.072] | PN |
| GPS | -2 | Negative | -0.3125 | 0.4419 | 2 | [-0.625, 0.000] | GPS |

### Party Entities
- **DAP** (+1, Slightly Positive, → PH): Anthony Loke, Hannah Yeoh, Democratic Action Party
- **MIC** (+1, Slightly Positive, → BN): Malaysian Indian Congress
- **UMNO** (+0, Neutral, → BN): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Asyraf Wajdi Dusuki, Shamsul Anuar Nasarah, Najib, United Malays National Organisation
- **PAS** (+0, Neutral, → PN): Parti Islam Se-Malaysia
- **BERSAMA** (+0, Neutral, → BERSAMA): Parti Bersama
- **MUDA** (+0, Neutral, → PH): Syed Saddiq, Malaysia United Democratic Alliance
- **PKR** (+0, Neutral, → PH): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Fahmi Fadzil, Parti Keadilan Rakyat
- **Warisan** (+0, Neutral, → WARISAN): Parti Warisan
- **AMANAH** (+0, Neutral, → PH): Maszlee, Mohamad Sabu, Parti Amanah Negara
- **MCA** (+0, Neutral, → BN): Malaysian Chinese Association
- **Pejuang** (-1, Slightly Negative, → PEJUANG): Mahathir Mohamad
- **BERSATU** (-1, Slightly Negative, → PN): Muhyiddin Yassin, Mas Ermieyati Samsudin, Parti Pribumi Bersatu Malaysia
- **GPS** (-2, Negative, → GPS): Sim Kui Hian, Tiong King Sing

---

## Sentiment Anomalies (|z-score| > 2)

**18 anomalies detected.**

| # | Entity | Type | Score | Label | Z-Score | Direction | Coalition | Party | Contexts |
|---|--------|------|:-----:|-------|:-------:|:---------:|-----------|:------:|:--------:|
| 1 | WAN IFRA ASIA MEDIA AWARDS 2025 | EVENT | +3 | Very Positive | 3.6052 | positive | N/A | — | 1 |
| 2 | Subang Jaya | LOCATION | -3 | Very Negative | -3.5622 | negative | N/A | — | 5 |
| 3 | Alexis Heng Boon Chin | PERSON | +3 | Very Positive | 3.4662 | positive | N/A | — | 4 |
| 4 | Thailand | LOCATION | +3 | Very Positive | 3.3585 | positive | N/A | — | 2 |
| 5 | Low Ley Hian | PERSON | -3 | Very Negative | -3.3516 | negative | N/A | — | 2 |
| 6 | MRT | ORGANIZATION | +3 | Very Positive | 3.2037 | positive | N/A | — | 1 |
| 7 | PRS | ORGANIZATION | +3 | Very Positive | 3.0260 | positive | N/A | — | 2 |
| 8 | Court case | EVENT | +3 | Very Positive | 3.0127 | positive | N/A | — | 1 |
| 9 | Onn Hafiz 56-seats solo bid | CONCEPT | +3 | Very Positive | 2.8534 | positive | N/A | — | 1 |
| 10 | Tiong King Sing | PERSON | -3 | Very Negative | -2.7982 | negative | GPS | GPS | 1 |
| 11 | Court of Appeal | EVENT | -3 | Very Negative | -2.7720 | negative | N/A | — | 4 |
| 12 | green technology | CONCEPT | +3 | Very Positive | 2.5916 | positive | N/A | — | 1 |
| 13 | renewable energy | CONCEPT | +3 | Very Positive | 2.5916 | positive | N/A | — | 1 |
| 14 | West Asia | LOCATION | -2 | Negative | -2.4829 | negative | N/A | — | 3 |
| 15 | Service tax | CONCEPT | +3 | Very Positive | 2.4585 | positive | N/A | — | 9 |
| 16 | Mas Ermieyati Samsudin | PERSON | -2 | Negative | -2.3847 | negative | PN | BERSATU | 2 |
| 17 | Mohamad Zainal Abdullah | PERSON | -2 | Negative | -2.3847 | negative | N/A | — | 2 |
| 18 | deposits | CONCEPT | -2 | Negative | -2.1013 | negative | N/A | — | 1 |

---

## Entity Sentiments by Type

### PERSON

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Alexis Heng Boon Chin | +3 | Very Positive | 0.8807 | 3.4662 | ⚠️ | 4 | — | — | ✚ |
| Ewon Benedick | +2 | Positive | 0.4404 | 1.6342 |  | 2 | — | — | ✚ |
| Noor Hisam Nordin | +2 | Positive | 0.4367 | 1.6188 |  | 2 | — | — | ✚ |
| Tan See Leng | +2 | Positive | 0.4019 | 1.4741 |  | 3 | — | — | ✚ |
| Shamsul Anuar Nasarah | +2 | Positive | 0.4003 | 1.4674 |  | 2 | BN | UMNO | ✚ |
| Amar-Singh HSS | +2 | Positive | 0.3818 | 1.3904 |  | 4 | — | — | ✚ |
| Lim Chong Eu | +2 | Positive | 0.3802 | 1.3838 |  | 3 | — | — | ✚ |
| Rajeentheran Suntheralingam | +2 | Positive | 0.3111 | 1.0963 |  | 4 | — | — | ✚ |
| Anthony Loke | +2 | Positive | 0.3080 | 1.0834 |  | 1 | PH | DAP | ✚ |
| Khairy Jamaluddin | +1 | Slightly Positive | 0.1702 | 0.5100 |  | 6 | BN | UMNO |  |
| Anwar Ibrahim | +1 | Slightly Positive | 0.1055 | 0.2408 |  | 20 | PH | PKR |  |
| Nik Nazmi Nik Ahmad | +0 | Neutral | 0.0500 | 0.0099 |  | 5 | PH | PKR |  |
| Ab Rauf Yusoh | +0 | Neutral | 0.0440 | -0.0151 |  | 4 | BN | UMNO |  |
| Syed Saddiq | +0 | Neutral | 0.0387 | -0.0371 |  | 18 | PH | MUDA | ✚ |
| Ahmad Zahid Hamidi | +0 | Neutral | 0.0225 | -0.1046 |  | 16 | BN | UMNO |  |
| Sam | +0 | Neutral | 0.0208 | -0.1116 |  | 30 | — | — | ✚ |
| Hassan Abdul Karim | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | PH | PKR |  |
| Jalaluddin Abdul Rahman | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | BN | UMNO |  |
| Mohamad Hasan | +0 | Neutral | 0.0000 | -0.1982 |  | 6 | BN | UMNO |  |
| Mohd Ghazali Sabari | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — |  |
| Nurul Izzah Anwar | +0 | Neutral | 0.0000 | -0.1982 |  | 4 | PH | PKR |  |
| Rafizi Ramli | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | PH | PKR |  |
| Sim Kui Hian | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | GPS | GPS |  |
| Abdul Razak | +0 | Neutral | 0.0000 | -0.1982 |  | 2 | — | — | ✚ |
| Asyraf Wajdi Dusuki | +0 | Neutral | 0.0000 | -0.1982 |  | 4 | BN | UMNO | ✚ |
| Jalaluddin Alias | +0 | Neutral | 0.0000 | -0.1982 |  | 2 | — | — | ✚ |
| Maszlee | +0 | Neutral | 0.0000 | -0.1982 |  | 4 | PH | AMANAH | ✚ |
| Zulkifli Hasan | +0 | Neutral | 0.0000 | -0.1982 |  | 8 | — | — | ✚ |
| Fahmi Fadzil | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | PH | PKR | ✚ |
| Hannah Yeoh | +0 | Neutral | 0.0000 | -0.1982 |  | 4 | PH | DAP | ✚ |
| Najib | +0 | Neutral | 0.0000 | -0.1982 |  | 4 | BN | UMNO | ✚ |
| Tan Meng Kheng | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Muhyiddin Yassin | +0 | Neutral | -0.0611 | -0.4524 |  | 5 | PN | BERSATU |  |
| Aminuddin Harun | +0 | Neutral | -0.0740 | -0.5061 |  | 20 | PH | PKR |  |
| Mahathir Mohamad | -1 | Slightly Negative | -0.1572 | -0.8522 |  | 6 | PEJUANG | Pejuang |  |
| Mohamad Sabu | -1 | Slightly Negative | -0.1921 | -0.9975 |  | 4 | PH | AMANAH | ✚ |
| B Nantha Kumar | -1 | Slightly Negative | -0.2263 | -1.1398 |  | 1 | — | — | ✚ |
| Mohd Khairi Khairudin | -2 | Negative | -0.3595 | -1.6940 |  | 2 | — | — | ✚ |
| Mas Ermieyati Samsudin | -2 | Negative | -0.5255 | -2.3847 | ⚠️ | 2 | PN | BERSATU | ✚ |
| Mohamad Zainal Abdullah | -2 | Negative | -0.5255 | -2.3847 | ⚠️ | 2 | — | — | ✚ |
| Tiong King Sing | -3 | Very Negative | -0.6249 | -2.7982 | ⚠️ | 1 | GPS | GPS |  |
| Low Ley Hian | -3 | Very Negative | -0.7579 | -3.3516 | ⚠️ | 2 | — | — | ✚ |

### ORGANIZATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| MRT | +3 | Very Positive | 0.8176 | 3.2037 | ⚠️ | 1 | — | — | ✚ |
| PRS | +3 | Very Positive | 0.7749 | 3.0260 | ⚠️ | 2 | — | — | ✚ |
| BERSIH | +2 | Positive | 0.5106 | 1.9263 |  | 1 | — | — | ✚ |
| Daily Express | +2 | Positive | 0.4679 | 1.7487 |  | 4 | — | — | ✚ |
| KWSP | +2 | Positive | 0.4627 | 1.7270 |  | 4 | — | — | ✚ |
| JPA | +2 | Positive | 0.4097 | 1.5065 |  | 4 | — | — | ✚ |
| DBKK | +2 | Positive | 0.4019 | 1.4741 |  | 2 | — | — | ✚ |
| Malay Mail | +2 | Positive | 0.4003 | 1.4674 |  | 1 | — | — | ✚ |
| SRC | +2 | Positive | 0.3674 | 1.3305 |  | 6 | — | — | ✚ |
| IHH | +2 | Positive | 0.3612 | 1.3047 |  | 1 | — | — | ✚ |
| JPJ | +1 | Slightly Positive | 0.2901 | 1.0089 |  | 14 | — | — | ✚ |
| 1MDB | +1 | Slightly Positive | 0.2895 | 1.0064 |  | 5 | — | — | ✚ |
| MMA | +1 | Slightly Positive | 0.2867 | 0.9947 |  | 21 | — | — | ✚ |
| MCMC | +1 | Slightly Positive | 0.2485 | 0.8358 |  | 13 | — | — | ✚ |
| KPJ | +1 | Slightly Positive | 0.2477 | 0.8325 |  | 4 | — | — | ✚ |
| NKF | +1 | Slightly Positive | 0.2470 | 0.8295 |  | 4 | — | — | ✚ |
| Suruhanjaya Pencegahan Rasuah Malaysia | +1 | Slightly Positive | 0.2247 | 0.7368 |  | 11 | — | — |  |
| EU | +1 | Slightly Positive | 0.1616 | 0.4742 |  | 30 | — | — | ✚ |
| Media Mulia | +1 | Slightly Positive | 0.1555 | 0.4488 |  | 6 | — | — | ✚ |
| Bernama | +1 | Slightly Positive | 0.1547 | 0.4455 |  | 19 | — | — | ✚ |
| The Star | +1 | Slightly Positive | 0.1480 | 0.4176 |  | 2 | — | — | ✚ |
| BURSA | +1 | Slightly Positive | 0.1318 | 0.3502 |  | 8 | — | — | ✚ |
| Malaysian Indian Congress | +1 | Slightly Positive | 0.1296 | 0.3411 |  | 25 | BN | MIC |  |
| WHO | +1 | Slightly Positive | 0.1114 | 0.2653 |  | 21 | — | — | ✚ |
| ASEAN | +1 | Slightly Positive | 0.1029 | 0.2300 |  | 17 | — | — |  |
| mStar | +0 | Neutral | 0.0886 | 0.1705 |  | 8 | — | — | ✚ |
| UN | +0 | Neutral | 0.0857 | 0.1584 |  | 30 | — | — | ✚ |
| Democratic Action Party | +0 | Neutral | 0.0853 | 0.1567 |  | 30 | PH | DAP |  |
| TikTok | +0 | Neutral | 0.0852 | 0.1563 |  | 29 | — | — | ✚ |
| IMU | +0 | Neutral | 0.0823 | 0.1443 |  | 6 | — | — | ✚ |
| Parti Pribumi Bersatu Malaysia | +0 | Neutral | 0.0723 | 0.1027 |  | 18 | PN | BERSATU |  |
| Parti Islam Se-Malaysia | +0 | Neutral | 0.0528 | 0.0215 |  | 30 | PN | PAS |  |
| RCI | +0 | Neutral | 0.0447 | -0.0122 |  | 12 | — | — | ✚ |
| Grab | +0 | Neutral | 0.0412 | -0.0267 |  | 16 | — | — | ✚ |
| Parti Bersama | +0 | Neutral | 0.0350 | -0.0525 |  | 18 | BERSAMA | BERSAMA |  |
| FIFA | +0 | Neutral | 0.0346 | -0.0542 |  | 14 | — | — | ✚ |
| Malaysia United Democratic Alliance | +0 | Neutral | 0.0305 | -0.0713 |  | 22 | PH | MUDA |  |
| Barisan Nasional | +0 | Neutral | 0.0138 | -0.1407 |  | 30 | BN | — |  |
| Google | +0 | Neutral | 0.0054 | -0.1757 |  | 15 | — | — | ✚ |
| Gabungan Parti Sarawak | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | GPS | — |  |
| GRS | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | GRS | — |  |
| HAWANA | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | — | — |  |
| Ministry of Home Affairs | +0 | Neutral | 0.0000 | -0.1982 |  | 2 | — | — |  |
| Parti Amanah Negara | +0 | Neutral | 0.0000 | -0.1982 |  | 2 | PH | AMANAH |  |
| Parti Keadilan Rakyat | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | PH | PKR |  |
| Parti Warisan | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | WARISAN | Warisan |  |
| Pejuang | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | PEJUANG | — |  |
| Armada | +0 | Neutral | 0.0000 | -0.1982 |  | 3 | — | — | ✚ |
| IOI | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| KLK | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Kosmo | +0 | Neutral | 0.0000 | -0.1982 |  | 8 | — | — | ✚ |
| MalaysiaGazette | +0 | Neutral | 0.0000 | -0.1982 |  | 4 | — | — | ✚ |
| Perodua | +0 | Neutral | 0.0000 | -0.1982 |  | 2 | — | — | ✚ |
| PRU | +0 | Neutral | 0.0000 | -0.1982 |  | 3 | — | — | ✚ |
| Sinar Harian | +0 | Neutral | 0.0000 | -0.1982 |  | 4 | — | — | ✚ |
| Spotify | +0 | Neutral | 0.0000 | -0.1982 |  | 5 | — | — | ✚ |
| Vulcan Post | +0 | Neutral | 0.0000 | -0.1982 |  | 4 | — | — | ✚ |
| World of Buzz | +0 | Neutral | 0.0000 | -0.1982 |  | 2 | — | — | ✚ |
| DUN | +0 | Neutral | -0.0091 | -0.2360 |  | 30 | — | — | ✚ |
| PRN | +0 | Neutral | -0.0145 | -0.2585 |  | 30 | — | — | ✚ |
| AirBorneo | +0 | Neutral | -0.0276 | -0.3130 |  | 12 | — | — | ✚ |
| NGO | +0 | Neutral | -0.0340 | -0.3396 |  | 30 | — | — | ✚ |
| Pakatan Harapan | +0 | Neutral | -0.0359 | -0.3475 |  | 30 | PH | — |  |
| PDRM | +0 | Neutral | -0.0372 | -0.3529 |  | 8 | — | — | ✚ |
| United Malays National Organisation | +0 | Neutral | -0.0458 | -0.3887 |  | 20 | BN | UMNO |  |
| CMS | +0 | Neutral | -0.0468 | -0.3929 |  | 9 | — | — | ✚ |
| Ministry of Finance | +0 | Neutral | -0.0512 | -0.4112 |  | 16 | — | — |  |
| Suruhanjaya Pilihan Raya | +0 | Neutral | -0.0676 | -0.4794 |  | 9 | — | — |  |
| Perikatan Nasional | +0 | Neutral | -0.0688 | -0.4844 |  | 30 | PN | — |  |
| Malaysian Chinese Association | +0 | Neutral | -0.0728 | -0.5011 |  | 15 | BN | MCA |  |
| Parliament | +0 | Neutral | -0.0750 | -0.5102 |  | 8 | — | — | ✚ |
| MKH | +0 | Neutral | -0.0918 | -0.5801 |  | 3 | — | — | ✚ |
| MOH | +0 | Neutral | -0.0960 | -0.5976 |  | 30 | — | — | ✚ |
| NST | -1 | Slightly Negative | -0.1133 | -0.6696 |  | 30 | — | — | ✚ |
| The Edge Malaysia | -1 | Slightly Negative | -0.1700 | -0.9055 |  | 4 | — | — | ✚ |
| PAC | -1 | Slightly Negative | -0.1912 | -0.9937 |  | 30 | — | — | ✚ |
| AFP | -1 | Slightly Negative | -0.2155 | -1.0948 |  | 12 | — | — | ✚ |
| CNA | -1 | Slightly Negative | -0.2260 | -1.1385 |  | 4 | — | — | ✚ |
| Bursa Malaysia | -1 | Slightly Negative | -0.2287 | -1.1497 |  | 2 | — | — | ✚ |
| Borneo Post | -2 | Negative | -0.3491 | -1.6507 |  | 2 | — | — | ✚ |
| JKR | -2 | Negative | -0.3679 | -1.7289 |  | 4 | — | — | ✚ |
| Dewan Rakyat | -2 | Negative | -0.4221 | -1.9544 |  | 4 | — | — | ✚ |

### LOCATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Thailand | +3 | Very Positive | 0.8548 | 3.3585 | ⚠️ | 2 | — | — | ✚ |
| Kelantan | +2 | Positive | 0.5050 | 1.9030 |  | 6 | — | — | ✚ |
| United States | +2 | Positive | 0.4716 | 1.7641 |  | 7 | — | — | ✚ |
| Italy | +2 | Positive | 0.4574 | 1.7050 |  | 1 | — | — | ✚ |
| Limbang | +2 | Positive | 0.4425 | 1.6430 |  | 5 | — | — | ✚ |
| Korea | +2 | Positive | 0.4234 | 1.5635 |  | 5 | — | — | ✚ |
| South Korea | +2 | Positive | 0.4019 | 1.4741 |  | 4 | — | — | ✚ |
| Vietnam | +2 | Positive | 0.4019 | 1.4741 |  | 4 | — | — | ✚ |
| Keningau | +2 | Positive | 0.3567 | 1.2860 |  | 8 | — | — | ✚ |
| Spain | +1 | Slightly Positive | 0.2739 | 0.9415 |  | 14 | — | — | ✚ |
| France | +1 | Slightly Positive | 0.2633 | 0.8974 |  | 2 | — | — | ✚ |
| US | +1 | Slightly Positive | 0.1858 | 0.5749 |  | 30 | — | — | ✚ |
| Sarawak | +1 | Slightly Positive | 0.1837 | 0.5662 |  | 25 | — | — |  |
| Bangladesh | +1 | Slightly Positive | 0.1739 | 0.5254 |  | 4 | — | — | ✚ |
| JB | +1 | Slightly Positive | 0.1347 | 0.3623 |  | 17 | — | — | ✚ |
| Japan | +1 | Slightly Positive | 0.1226 | 0.3119 |  | 14 | — | — | ✚ |
| Ipoh | +1 | Slightly Positive | 0.1166 | 0.2870 |  | 10 | — | — | ✚ |
| Singapore | +0 | Neutral | 0.0890 | 0.1721 |  | 22 | — | — | ✚ |
| India | +0 | Neutral | 0.0864 | 0.1613 |  | 7 | — | — | ✚ |
| Sibu | +0 | Neutral | 0.0843 | 0.1526 |  | 5 | — | — | ✚ |
| Sandakan | +0 | Neutral | 0.0787 | 0.1293 |  | 8 | — | — | ✚ |
| Klang | +0 | Neutral | 0.0566 | 0.0373 |  | 4 | — | — | ✚ |
| Perak | +0 | Neutral | 0.0516 | 0.0165 |  | 13 | — | — |  |
| Muar | +0 | Neutral | 0.0391 | -0.0355 |  | 11 | — | — | ✚ |
| Negeri Sembilan | +0 | Neutral | 0.0363 | -0.0471 |  | 30 | — | — |  |
| Ranau | +0 | Neutral | 0.0335 | -0.0588 |  | 3 | — | — | ✚ |
| Penang | +0 | Neutral | 0.0303 | -0.0721 |  | 13 | — | — |  |
| Putrajaya | +0 | Neutral | 0.0301 | -0.0729 |  | 12 | — | — | ✚ |
| Selangor | +0 | Neutral | 0.0299 | -0.0738 |  | 25 | — | — |  |
| UK | +0 | Neutral | 0.0289 | -0.0779 |  | 30 | — | — | ✚ |
| Johor | +0 | Neutral | 0.0273 | -0.0846 |  | 30 | — | — |  |
| Melaka | +0 | Neutral | 0.0251 | -0.0937 |  | 28 | — | — |  |
| Kuala Lumpur | +0 | Neutral | 0.0222 | -0.1058 |  | 30 | — | — |  |
| Sabah | +0 | Neutral | 0.0014 | -0.1923 |  | 29 | — | — |  |
| N14 | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | — | — |  |
| Pasir Gudang | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — |  |
| Pertang | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | — | — |  |
| Rantau | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — |  |
| Alor Setar | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Batu Pahat | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Beaufort | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Beluran | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Betong | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Bintulu | +0 | Neutral | 0.0000 | -0.1982 |  | 5 | — | — | ✚ |
| Brazil | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Bukit Naning | +0 | Neutral | 0.0000 | -0.1982 |  | 2 | — | — | ✚ |
| Cameron Highlands | +0 | Neutral | 0.0000 | -0.1982 |  | 4 | — | — | ✚ |
| Dungun | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Gombak | +0 | Neutral | 0.0000 | -0.1982 |  | 2 | — | — | ✚ |
| Hulu Selangor | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Kangar | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Kemaman | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Kota Bharu | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Kota Tinggi | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Kuala Selangor | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Kuala Terengganu | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Kuantan | +0 | Neutral | 0.0000 | -0.1982 |  | 7 | — | — | ✚ |
| Kudat | +0 | Neutral | 0.0000 | -0.1982 |  | 2 | — | — | ✚ |
| Kunak | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Lahad Datu | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Lipis | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Maran | +0 | Neutral | 0.0000 | -0.1982 |  | 12 | — | — | ✚ |
| Mersing | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Norway | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Pahang | +0 | Neutral | 0.0000 | -0.1982 |  | 12 | — | — | ✚ |
| Pasir Puteh | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Penampang | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Philippines | +0 | Neutral | 0.0000 | -0.1982 |  | 4 | — | — | ✚ |
| Putatan | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Rompin | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Samarahan | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Sarikei | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Segamat | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Semporna | +0 | Neutral | 0.0000 | -0.1982 |  | 5 | — | — | ✚ |
| Seremban | +0 | Neutral | 0.0000 | -0.1982 |  | 5 | — | — | ✚ |
| Serian | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Shah Alam | +0 | Neutral | 0.0000 | -0.1982 |  | 2 | — | — | ✚ |
| Tambunan | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Tenom | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| Australia | +0 | Neutral | -0.0054 | -0.2206 |  | 8 | — | — | ✚ |
| Tawau | +0 | Neutral | -0.0368 | -0.3513 |  | 7 | — | — | ✚ |
| Kota Kinabalu | +0 | Neutral | -0.0410 | -0.3688 |  | 9 | — | — |  |
| Petaling Jaya | +0 | Neutral | -0.0475 | -0.3958 |  | 5 | — | — | ✚ |
| Kuching | +0 | Neutral | -0.0598 | -0.4470 |  | 9 | — | — |  |
| Kedah | +0 | Neutral | -0.0649 | -0.4682 |  | 10 | — | — | ✚ |
| Wall Street | +0 | Neutral | -0.0929 | -0.5847 |  | 3 | — | — | ✚ |
| England | -1 | Slightly Negative | -0.1000 | -0.6142 |  | 24 | — | — | ✚ |
| Linggi | -1 | Slightly Negative | -0.1029 | -0.6263 |  | 15 | — | — |  |
| Argentina | -1 | Slightly Negative | -0.1094 | -0.6534 |  | 25 | — | — | ✚ |
| Parliament House | -1 | Slightly Negative | -0.1152 | -0.6775 |  | 24 | — | — |  |
| China | -1 | Slightly Negative | -0.1179 | -0.6887 |  | 20 | — | — | ✚ |
| Iran | -1 | Slightly Negative | -0.1395 | -0.7786 |  | 30 | — | — | ✚ |
| Germany | -1 | Slightly Negative | -0.2422 | -1.2059 |  | 4 | — | — | ✚ |
| Brunei | -1 | Slightly Negative | -0.2654 | -1.3024 |  | 4 | — | — | ✚ |
| Sepang | -1 | Slightly Negative | -0.2724 | -1.3316 |  | 3 | — | — | ✚ |
| Miri | -1 | Slightly Negative | -0.2803 | -1.3644 |  | 13 | — | — | ✚ |
| Middle East | -2 | Negative | -0.3182 | -1.5221 |  | 2 | — | — | ✚ |
| Indonesia | -2 | Negative | -0.3974 | -1.8517 |  | 8 | — | — | ✚ |
| West Asia | -2 | Negative | -0.5491 | -2.4829 | ⚠️ | 3 | — | — | ✚ |
| Subang Jaya | -3 | Very Negative | -0.8085 | -3.5622 | ⚠️ | 5 | — | — | ✚ |

### EVENT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| WAN IFRA ASIA MEDIA AWARDS 2025 | +3 | Very Positive | 0.9141 | 3.6052 | ⚠️ | 1 | — | — | ✚ |
| Court case | +3 | Very Positive | 0.7717 | 3.0127 | ⚠️ | 1 | — | — | ✚ |
| Federal Court | +2 | Positive | 0.3486 | 1.2523 |  | 2 | — | — | ✚ |
| 2026 Elections | +1 | Slightly Positive | 0.2689 | 0.9207 |  | 3 | — | — | ✚ |
| rally | +1 | Slightly Positive | 0.2129 | 0.6877 |  | 6 | — | — |  |
| State Polls 2026 | +1 | Slightly Positive | 0.1895 | 0.5903 |  | 3 | — | — | ✚ |
| Investigation | +1 | Slightly Positive | 0.1859 | 0.5753 |  | 9 | — | — | ✚ |
| World Cup | +1 | Slightly Positive | 0.1027 | 0.2291 |  | 18 | — | — | ✚ |
| Johor State Election | +0 | Neutral | 0.0175 | -0.1254 |  | 12 | — | — |  |
| Summit | +0 | Neutral | 0.0109 | -0.1528 |  | 10 | — | — | ✚ |
| BN Candidate Announcement (NS) | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | — | — |  |
| ceramah | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — |  |
| HAWANA X TM Media Event | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | — | — |  |
| kempen | +0 | Neutral | 0.0000 | -0.1982 |  | 9 | — | — |  |
| majlis | +0 | Neutral | 0.0000 | -0.1982 |  | 7 | — | — |  |
| Negeri Sembilan State Election 2026 | +0 | Neutral | 0.0000 | -0.1982 |  | 22 | — | — |  |
| Sarawak State Election 2026 | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | — | — |  |
| walkabout | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | — | — |  |
| Piala Dunia | +0 | Neutral | 0.0000 | -0.1982 |  | 14 | — | — | ✚ |
| pilihan raya | +0 | Neutral | 0.0000 | -0.1982 |  | 4 | — | — | ✚ |
| pilihan raya negeri | +0 | Neutral | 0.0000 | -0.1982 |  | 3 | — | — | ✚ |
| Pilihan Raya Negeri Johor | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| PRN Negeri | +0 | Neutral | 0.0000 | -0.1982 |  | 20 | — | — | ✚ |
| Typhoon Bavi | +0 | Neutral | 0.0000 | -0.1982 |  | 1 | — | — | ✚ |
| state election | +0 | Neutral | -0.0093 | -0.2369 |  | 5 | — | — | ✚ |
| event | +0 | Neutral | -0.0227 | -0.2926 |  | 21 | — | — |  |
| campaign | +0 | Neutral | -0.0859 | -0.5556 |  | 9 | — | — |  |
| Appeal | -1 | Slightly Negative | -0.1187 | -0.6921 |  | 15 | — | — | ✚ |
| High Court | -1 | Slightly Negative | -0.1201 | -0.6979 |  | 8 | — | — | ✚ |
| Audience | -1 | Slightly Negative | -0.1649 | -0.8843 |  | 4 | — | — | ✚ |
| Court of Appeal | -3 | Very Negative | -0.6186 | -2.7720 | ⚠️ | 4 | — | — | ✚ |

### CONCEPT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Onn Hafiz 56-seats solo bid | +3 | Very Positive | 0.7334 | 2.8534 | ⚠️ | 1 | — | — |  |
| green technology | +3 | Very Positive | 0.6705 | 2.5916 | ⚠️ | 1 | — | — | ✚ |
| renewable energy | +3 | Very Positive | 0.6705 | 2.5916 | ⚠️ | 1 | — | — | ✚ |
| Service tax | +3 | Very Positive | 0.6385 | 2.4585 | ⚠️ | 9 | — | — |  |
| opposition | +1 | Slightly Positive | 0.2412 | 0.8054 |  | 2 | — | — | ✚ |
| copyright | +1 | Slightly Positive | 0.1977 | 0.6244 |  | 15 | — | — | ✚ |
| MADANI government | +1 | Slightly Positive | 0.1804 | 0.5524 |  | 21 | — | — |  |
| Wealth tax | +1 | Slightly Positive | 0.1482 | 0.4185 |  | 0 | — | — |  |
| artificial intelligence | +0 | Neutral | 0.0725 | 0.1035 |  | 2 | — | — | ✚ |
| Bersatu own logo in N9 | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | — | — |  |
| Cost of living | +0 | Neutral | 0.0000 | -0.1982 |  | 6 | — | — |  |
| Super El Nino food security | +0 | Neutral | 0.0000 | -0.1982 |  | 2 | — | — |  |
| Third force movement | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | — | — |  |
| UEC recognition | +0 | Neutral | 0.0000 | -0.1982 |  | 0 | — | — |  |
| MediAsas | +0 | Neutral | 0.0000 | -0.1982 |  | 4 | — | — | ✚ |
| TVET | +0 | Neutral | 0.0000 | -0.1982 |  | 3 | — | — | ✚ |
| wake-up call | +0 | Neutral | 0.0000 | -0.1982 |  | 4 | — | — | ✚ |
| transport | +0 | Neutral | -0.0152 | -0.2614 |  | 10 | — | — | ✚ |
| inflation | +0 | Neutral | -0.0241 | -0.2984 |  | 13 | — | — | ✚ |
| AI | +0 | Neutral | -0.0788 | -0.5260 |  | 30 | — | — | ✚ |
| Subsidies & welfare aid | -1 | Slightly Negative | -0.1045 | -0.6330 |  | 23 | — | — |  |
| water supply | -2 | Negative | -0.3612 | -1.7010 |  | 1 | — | — | ✚ |
| deposits | -2 | Negative | -0.4574 | -2.1013 | ⚠️ | 1 | — | — | ✚ |

---

## Methodology

1. **Entity Source:** Loaded from the 2026-07-17T001255Z extraction roster (297 Phase-1 entity names) plus the 78 canonical entities from the per-entity index. Roster names were merged into canonical entities by normalized name/alias matching (honorific-stripped); unmerged names were added as new entities (200 new).
2. **Context Extraction:** For each entity, search variants (canonical name + aliases + roster matches) were located in the 2026-07-17 raw source collection (23 sources, 23 processed, ~813953 chars). A context window (~140+170 chars) was extracted around each mention (markdown stripped, de-duplicated, capped at 30/entity).
3. **Sentiment Scoring:** Applied VADER to each context snippet; entity sentiment = mean compound across snippets.
4. **Score Mapping:** VADER compound (-1..+1) → 7-point Likert (-3..+3): +3 ≥0.6, +2 ≥0.3, +1 ≥0.1, 0 (-0.1..0.1), -1 >-0.3, -2 >-0.6, -3 ≤-0.6.
5. **Anomaly Detection:** Z-score on raw compound vs overall mean/std; flagged when |z| > 2.
6. **Coalition/Party Aggregation:** Persons + political-party/coalition orgs mapped via per-entity metadata and affiliation maps (FIGURE_AFFILIATIONS, ORG_TO_COALITION, analyst-extended NEW_FIGURE_AFFIL).

---

*Report generated by OpenCLaw Sentiment Analysis Pipeline (sentiment-analysis skill)*
*VADER: Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.*

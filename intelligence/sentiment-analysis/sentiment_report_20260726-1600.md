# Sentiment Analysis Report

**Classification:** TLP:AMBER
**Generated:** 2026-07-26 16:00 +08
**Report Date:** 2026-07-26
**Report Timestamp:** 2026-07-26 16:00 +08
**Extraction ID:** ext_20260726_1400_phase1
**Extraction Source:** 2026-07-26T14:00:00+08:00
**Collection Cycle:** 2026-07-26T001445Z
**Source Count:** 24
**Analysis Method:** VADER Sentiment Analysis on fresh context snippets extracted from 2026-07-26 raw collection
**Score Range:** -3 (very negative) to +3 (very positive)
**Anomaly Threshold:** |z-score| > 2

> **Data-freshness note:** The 2026-07-26 extraction produced Phase-1 entity name lists
> only; Phase-2 per-entity context files were not regenerated for this cycle. To produce a
> genuine 2026-07-26 sentiment signal, context snippets were extracted directly from the
> 2026-07-26 raw source collection and scored with VADER. Coalition/party metadata sourced
> from the canonical per-entity files (2026-07-16 Phase-2 set) plus an analyst-extended
> affiliation map for newly-extracted figures.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Roster Entities (Phase-1 names) | 279 |
| Analysis Entities (merged) | 272 |
| Canonical Entities (from index) | 78 |
| New Entities (this cycle) | 194 |
| Roster Names Matched to Canonical | 57 |
| Sources Processed | 24 |
| Entities with Context | 250 |
| Entities without Context (fallback) | 22 |
| Overall Mean Sentiment | +0.151 |
| Overall Std Deviation | 0.935 |
| Overall Median Sentiment | +0.000 |
| Overall Raw Mean | 0.0366 |
| Overall Raw Std Dev | 0.2103 |
| Sentiment Range | [-3, +3] |
| Positive Entities | 50 |
| Neutral Entities | 196 |
| Negative Entities | 26 |
| Anomalies Detected | 26 |
| Coalitions Analyzed | 8 |
| Parties Analyzed | 16 |

### Sentiment Distribution

```
Positive (50)  ██████████████████████████████████████████████████
Neutral  (196)  ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
Negative (26)  ██████████████████████████
```

---

## Coalition Aggregate Sentiment

| Coalition | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range |
|-----------|:-:|------|:----------:|:-------:|:--------:|:-----:|
| GRS | +1 | Slightly Positive | 0.1570 | 0.2220 | 2 | [0.000, 0.314] |
| GPS | +0 | Neutral | 0.0979 | 0.1959 | 4 | [0.000, 0.392] |
| BN | +0 | Neutral | 0.0396 | 0.0549 | 12 | [0.000, 0.149] |
| PH | +0 | Neutral | 0.0339 | 0.1442 | 18 | [-0.202, 0.540] |
| PN | +0 | Neutral | 0.0279 | 0.0607 | 9 | [-0.054, 0.156] |
| BERSAMA | +0 | Neutral | 0.0209 | 0.0000 | 1 | [0.021, 0.021] |
| PEJUANG | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] |
| WARISAN | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
### Coalition Entities
- **GRS** (+1, Slightly Positive): Joachim Gunsalam, GRS
- **GPS** (+0, Neutral): Sim Kui Hian, Tiong King Sing, Gabungan Parti Sarawak, PRS
- **BN** (+0, Neutral): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Jalaluddin Alias, Najib Razak, Onn Hafiz, Barisan Nasional, Malaysian Chinese Association, Malaysian Indian Congress, United Malays National Organisation
- **PH** (+0, Neutral): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Anthony Loke, Dzulkefly Ahmad, Mohamad Sabu, Syed Saddiq, Saifuddin Nasution, Tengku Zafrul Aziz, Democratic Action Party, Malaysia United Democratic Alliance, Pakatan Harapan, Parti Amanah Negara, Parti Keadilan Rakyat, Keadilan
- **PN** (+0, Neutral): Muhyiddin Yassin, Ahmad Samsuri Mokhtar, Muhammad Sanusi, Samsuri, Abdul Hadi Awang, Hamzah Zainudin, Parti Islam Se-Malaysia, Parti Pribumi Bersatu Malaysia, Perikatan Nasional
- **BERSAMA** (+0, Neutral): Parti Bersama
- **PEJUANG** (+0, Neutral): Mahathir Mohamad, Pejuang
- **WARISAN** (+0, Neutral): Parti Warisan

---

## Party Aggregate Sentiment

| Party | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range | Coalition |
|-------|:-:|------|:----------:|:-------:|:--------:|:-----:|:---------:|
| Keadilan | +2 | Positive | 0.5399 | 0.0000 | 1 | [0.540, 0.540] | — |
| PRS | +2 | Positive | 0.3918 | 0.0000 | 1 | [0.392, 0.392] | GPS |
| GRS | +2 | Positive | 0.3139 | 0.0000 | 1 | [0.314, 0.314] | GRS |
| MIC | +1 | Slightly Positive | 0.1486 | 0.0000 | 1 | [0.149, 0.149] | BN |
| MCA | +0 | Neutral | 0.0639 | 0.0000 | 1 | [0.064, 0.064] | BN |
| PAS | +0 | Neutral | 0.0447 | 0.0802 | 5 | [-0.054, 0.156] | PN |
| BERSAMA | +0 | Neutral | 0.0209 | 0.0000 | 1 | [0.021, 0.021] | BERSAMA |
| UMNO | +0 | Neutral | 0.0208 | 0.0452 | 9 | [0.000, 0.134] | BN |
| DAP | +0 | Neutral | 0.0161 | 0.0228 | 2 | [0.000, 0.032] | PH |
| AMANAH | +0 | Neutral | 0.0115 | 0.0199 | 3 | [0.000, 0.034] | PH |
| MUDA | +0 | Neutral | 0.0080 | 0.0114 | 2 | [0.000, 0.016] | PH |
| BERSATU | +0 | Neutral | 0.0000 | 0.0000 | 3 | [0.000, 0.000] | PN |
| GPS | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] | GPS |
| Pejuang | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | PEJUANG |
| Warisan | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | WARISAN |
| PKR | +0 | Neutral | -0.0077 | 0.0978 | 9 | [-0.202, 0.183] | PH |
### Party Entities
- **Keadilan** (+2, Positive, → —): Keadilan
- **PRS** (+2, Positive, → GPS): PRS
- **GRS** (+2, Positive, → GRS): Joachim Gunsalam
- **MIC** (+1, Slightly Positive, → BN): Malaysian Indian Congress
- **MCA** (+0, Neutral, → BN): Malaysian Chinese Association
- **PAS** (+0, Neutral, → PN): Ahmad Samsuri Mokhtar, Muhammad Sanusi, Samsuri, Abdul Hadi Awang, Parti Islam Se-Malaysia
- **BERSAMA** (+0, Neutral, → BERSAMA): Parti Bersama
- **UMNO** (+0, Neutral, → BN): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Jalaluddin Alias, Najib Razak, Onn Hafiz, United Malays National Organisation
- **DAP** (+0, Neutral, → PH): Anthony Loke, Democratic Action Party
- **AMANAH** (+0, Neutral, → PH): Dzulkefly Ahmad, Mohamad Sabu, Parti Amanah Negara
- **MUDA** (+0, Neutral, → PH): Syed Saddiq, Malaysia United Democratic Alliance
- **BERSATU** (+0, Neutral, → PN): Muhyiddin Yassin, Hamzah Zainudin, Parti Pribumi Bersatu Malaysia
- **GPS** (+0, Neutral, → GPS): Sim Kui Hian, Tiong King Sing
- **Pejuang** (+0, Neutral, → PEJUANG): Mahathir Mohamad
- **Warisan** (+0, Neutral, → WARISAN): Parti Warisan
- **PKR** (+0, Neutral, → PH): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Saifuddin Nasution, Tengku Zafrul Aziz, Parti Keadilan Rakyat

---

## Sentiment Anomalies (|z-score| > 2)

**26 anomalies detected.**

| # | Entity | Type | Score | Label | Z-Score | Direction | Coalition | Party | Contexts |
|---|--------|------|:-----:|-------|:-------:|:---------:|-----------|:------:|:--------:|
| 1 | WAN IFRA ASIA MEDIA AWARDS 2025 | EVENT | +3 | Very Positive | 4.1953 | positive | N/A | — | 2 |
| 2 | Court case | EVENT | +3 | Very Positive | 3.4962 | positive | N/A | — | 1 |
| 3 | Middle East | LOCATION | -3 | Very Negative | -3.4068 | negative | N/A | — | 2 |
| 4 | The Star | ORGANIZATION | +3 | Very Positive | 3.3597 | positive | N/A | — | 1 |
| 5 | Onn Hafiz 56-seats solo bid | CONCEPT | +3 | Very Positive | 3.3140 | positive | N/A | — | 1 |
| 6 | West Asia | LOCATION | -3 | Very Negative | -3.2826 | negative | N/A | — | 5 |
| 7 | gig economy | CONCEPT | -3 | Very Negative | -3.2032 | negative | N/A | — | 1 |
| 8 | artificial intelligence | CONCEPT | +3 | Very Positive | 3.2008 | positive | N/A | — | 1 |
| 9 | Saudi Arabia | LOCATION | -3 | Very Negative | -3.0539 | negative | N/A | — | 3 |
| 10 | democratic power | CONCEPT | -3 | Very Negative | -3.0367 | negative | N/A | — | 2 |
| 11 | green technology | CONCEPT | +3 | Very Positive | 3.0149 | positive | N/A | — | 1 |
| 12 | renewable energy | CONCEPT | +3 | Very Positive | 3.0149 | positive | N/A | — | 1 |
| 13 | DVS | ORGANIZATION | +3 | Very Positive | 2.9954 | positive | N/A | — | 4 |
| 14 | national unity | CONCEPT | -2 | Negative | -2.6448 | negative | N/A | — | 2 |
| 15 | United States | LOCATION | +2 | Positive | 2.6063 | positive | N/A | — | 4 |
| 16 | Yemen | LOCATION | -2 | Negative | -2.4974 | negative | N/A | — | 4 |
| 17 | Hearing | EVENT | +2 | Positive | 2.4522 | positive | N/A | — | 4 |
| 18 | Keadilan | ORGANIZATION | +2 | Positive | 2.3937 | positive | PH | Keadilan | 4 |
| 19 | Suara Keadilan | ORGANIZATION | +2 | Positive | 2.3937 | positive | N/A | — | 1 |
| 20 | nominated assemblymen | CONCEPT | -2 | Negative | -2.3319 | negative | N/A | — | 3 |
| 21 | water supply | CONCEPT | +2 | Positive | 2.2544 | positive | N/A | — | 1 |
| 22 | Shah Alam | LOCATION | -2 | Negative | -2.2254 | negative | N/A | — | 4 |
| 23 | AirBorneo | ORGANIZATION | +2 | Positive | 2.0889 | positive | N/A | — | 4 |
| 24 | Investigation | EVENT | +2 | Positive | 2.0831 | positive | N/A | — | 4 |
| 25 | Summit | EVENT | +2 | Positive | 2.0784 | positive | N/A | — | 5 |
| 26 | Navin Mann | PERSON | +2 | Positive | 2.0080 | positive | N/A | — | 2 |
---

## Entity Sentiments by Type

### PERSON

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Navin Mann | +2 | Positive | 0.4588 | 2.0080 | ⚠️ | 2 | — | — | ✚ |
| Joachim Gunsalam | +2 | Positive | 0.3139 | 1.3189 |  | 3 | GRS | GRS | ✚ |
| Rajeentheran Suntheralingam | +1 | Slightly Positive | 0.2654 | 1.0882 |  | 4 | — | — | ✚ |
| Anwar Ibrahim | +1 | Slightly Positive | 0.1834 | 0.6982 |  | 30 | PH | PKR |  |
| Ahmad Samsuri Mokhtar | +1 | Slightly Positive | 0.1561 | 0.5683 |  | 6 | PN | PAS | ✚ |
| Ahmad Zahid Hamidi | +1 | Slightly Positive | 0.1344 | 0.4651 |  | 22 | BN | UMNO |  |
| Samsuri | +0 | Neutral | 0.0832 | 0.2216 |  | 8 | PN | PAS | ✚ |
| Alia Amira | +0 | Neutral | 0.0572 | 0.0980 |  | 16 | — | — | ✚ |
| Mohamad Sabu | +0 | Neutral | 0.0344 | -0.0105 |  | 4 | PH | AMANAH | ✚ |
| Najib Razak | +0 | Neutral | 0.0068 | -0.1417 |  | 14 | BN | UMNO | ✚ |
| Ab Rauf Yusoh | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | BN | UMNO |  |
| Aminuddin Harun | +0 | Neutral | 0.0000 | -0.1741 |  | 9 | PH | PKR |  |
| Hassan Abdul Karim | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | PH | PKR |  |
| Jalaluddin Abdul Rahman | +0 | Neutral | 0.0000 | -0.1741 |  | 2 | BN | UMNO |  |
| Khairy Jamaluddin | +0 | Neutral | 0.0000 | -0.1741 |  | 11 | BN | UMNO |  |
| Mahathir Mohamad | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | PEJUANG | Pejuang |  |
| Mohamad Hasan | +0 | Neutral | 0.0000 | -0.1741 |  | 7 | BN | UMNO |  |
| Mohd Ghazali Sabari | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | — | — |  |
| Muhyiddin Yassin | +0 | Neutral | 0.0000 | -0.1741 |  | 8 | PN | BERSATU |  |
| Nik Nazmi Nik Ahmad | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | PH | PKR |  |
| Nurul Izzah Anwar | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | PH | PKR |  |
| Rafizi Ramli | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | PH | PKR |  |
| Sim Kui Hian | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | GPS | GPS |  |
| Tiong King Sing | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | GPS | GPS |  |
| Tengku Amir Shah | +0 | Neutral | 0.0000 | -0.1741 |  | 2 | — | — | ✚ |
| Anthony Loke | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | PH | DAP | ✚ |
| Mohd Faizal Ramli | +0 | Neutral | 0.0000 | -0.1741 |  | 2 | — | — | ✚ |
| Jalaluddin Alias | +0 | Neutral | 0.0000 | -0.1741 |  | 3 | BN | UMNO | ✚ |
| Dzulkefly Ahmad | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | PH | AMANAH | ✚ |
| Abdul Hadi Awang | +0 | Neutral | 0.0000 | -0.1741 |  | 2 | PN | PAS | ✚ |
| Onn Hafiz | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | BN | UMNO | ✚ |
| Syed Saddiq | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | PH | MUDA | ✚ |
| Saifuddin Nasution | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | PH | PKR | ✚ |
| Hamzah Zainudin | +0 | Neutral | 0.0000 | -0.1741 |  | 3 | PN | BERSATU | ✚ |
| Tengku Zafrul Aziz | +0 | Neutral | -0.0506 | -0.4147 |  | 8 | PH | PKR | ✚ |
| Tun Fuad | +0 | Neutral | -0.0516 | -0.4195 |  | 2 | — | — | ✚ |
| Muhammad Sanusi | +0 | Neutral | -0.0544 | -0.4328 |  | 30 | PN | PAS | ✚ |
| Abdul Razak | -1 | Slightly Negative | -0.1017 | -0.6578 |  | 11 | — | — | ✚ |
### ORGANIZATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| The Star | +3 | Very Positive | 0.7430 | 3.3597 | ⚠️ | 1 | — | — | ✚ |
| DVS | +3 | Very Positive | 0.6664 | 2.9954 | ⚠️ | 4 | — | — | ✚ |
| Keadilan | +2 | Positive | 0.5399 | 2.3937 | ⚠️ | 4 | PH | Keadilan | ✚ |
| Suara Keadilan | +2 | Positive | 0.5399 | 2.3937 | ⚠️ | 1 | — | — | ✚ |
| AirBorneo | +2 | Positive | 0.4758 | 2.0889 | ⚠️ | 4 | — | — | ✚ |
| PRS | +2 | Positive | 0.3918 | 1.6893 |  | 2 | GPS | PRS | ✚ |
| Perodua | +1 | Slightly Positive | 0.2470 | 1.0007 |  | 2 | — | — | ✚ |
| Media Mulia | +1 | Slightly Positive | 0.1555 | 0.5655 |  | 6 | — | — | ✚ |
| KWSP | +1 | Slightly Positive | 0.1538 | 0.5574 |  | 13 | — | — | ✚ |
| Malaysian Indian Congress | +1 | Slightly Positive | 0.1486 | 0.5327 |  | 29 | BN | MIC |  |
| Barisan Nasional | +0 | Neutral | 0.0745 | 0.1803 |  | 30 | BN | — |  |
| IMU | +0 | Neutral | 0.0706 | 0.1617 |  | 7 | — | — | ✚ |
| ASEAN | +0 | Neutral | 0.0640 | 0.1303 |  | 20 | — | — |  |
| Malaysian Chinese Association | +0 | Neutral | 0.0639 | 0.1298 |  | 7 | BN | MCA |  |
| Pakatan Harapan | +0 | Neutral | 0.0576 | 0.0999 |  | 30 | PH | — |  |
| United Malays National Organisation | +0 | Neutral | 0.0464 | 0.0466 |  | 12 | BN | UMNO |  |
| UN | +0 | Neutral | 0.0459 | 0.0442 |  | 30 | — | — | ✚ |
| Apple | +0 | Neutral | 0.0453 | 0.0414 |  | 13 | — | — | ✚ |
| TikTok | +0 | Neutral | 0.0420 | 0.0257 |  | 30 | — | — | ✚ |
| Parti Islam Se-Malaysia | +0 | Neutral | 0.0384 | 0.0086 |  | 30 | PN | PAS |  |
| Democratic Action Party | +0 | Neutral | 0.0322 | -0.0209 |  | 30 | PH | DAP |  |
| Perikatan Nasional | +0 | Neutral | 0.0282 | -0.0400 |  | 30 | PN | — |  |
| PRN | +0 | Neutral | 0.0257 | -0.0518 |  | 30 | — | — | ✚ |
| Parti Bersama | +0 | Neutral | 0.0209 | -0.0747 |  | 13 | BERSAMA | BERSAMA |  |
| Google | +0 | Neutral | 0.0182 | -0.0875 |  | 21 | — | — | ✚ |
| Malaysia United Democratic Alliance | +0 | Neutral | 0.0161 | -0.0975 |  | 25 | PH | MUDA |  |
| Gabungan Parti Sarawak | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | GPS | — |  |
| GRS | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | GRS | — |  |
| HAWANA | +0 | Neutral | 0.0000 | -0.1741 |  | 7 | — | — |  |
| Ministry of Finance | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — |  |
| Ministry of Home Affairs | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — |  |
| Parti Amanah Negara | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | PH | AMANAH |  |
| Parti Pribumi Bersatu Malaysia | +0 | Neutral | 0.0000 | -0.1741 |  | 6 | PN | BERSATU |  |
| Parti Warisan | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | WARISAN | Warisan |  |
| Pejuang | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | PEJUANG | — |  |
| AFP | +0 | Neutral | 0.0000 | -0.1741 |  | 8 | — | — | ✚ |
| Bernama | +0 | Neutral | 0.0000 | -0.1741 |  | 11 | — | — | ✚ |
| Borneo Post | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | — | — | ✚ |
| Cabinet | +0 | Neutral | 0.0000 | -0.1741 |  | 2 | — | — | ✚ |
| CodeBlue | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | — | — | ✚ |
| Harian Metro | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| KLK | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Kosmo | +0 | Neutral | 0.0000 | -0.1741 |  | 8 | — | — | ✚ |
| KPKM | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | — | — | ✚ |
| Malay Mail | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | — | — | ✚ |
| MalaysiaGazette | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | — | — | ✚ |
| Malaysiakini | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | — | — | ✚ |
| MCMC | +0 | Neutral | 0.0000 | -0.1741 |  | 7 | — | — | ✚ |
| mStar | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | — | — | ✚ |
| Sabah News | +0 | Neutral | 0.0000 | -0.1741 |  | 3 | — | — | ✚ |
| Sinar Harian | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | — | — | ✚ |
| SK hynix | +0 | Neutral | 0.0000 | -0.1741 |  | 3 | — | — | ✚ |
| Spotify | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | — | — | ✚ |
| The Edge Malaysia | +0 | Neutral | 0.0000 | -0.1741 |  | 2 | — | — | ✚ |
| World Cup | +0 | Neutral | -0.0217 | -0.2773 |  | 11 | — | — | ✚ |
| NGO | +0 | Neutral | -0.0229 | -0.2830 |  | 30 | — | — | ✚ |
| MOH | +0 | Neutral | -0.0232 | -0.2844 |  | 19 | — | — | ✚ |
| BuzzKini | +0 | Neutral | -0.0257 | -0.2963 |  | 4 | — | — | ✚ |
| Tropicana | +0 | Neutral | -0.0568 | -0.4442 |  | 4 | — | — | ✚ |
| Suruhanjaya Pilihan Raya | +0 | Neutral | -0.0782 | -0.5460 |  | 10 | — | — |  |
| Vulcan Post | +0 | Neutral | -0.0846 | -0.5764 |  | 4 | — | — | ✚ |
| BURSA | +0 | Neutral | -0.0849 | -0.5779 |  | 6 | — | — | ✚ |
| NST | +0 | Neutral | -0.0878 | -0.5917 |  | 30 | — | — | ✚ |
| UNHCR | +0 | Neutral | -0.0898 | -0.6012 |  | 8 | — | — | ✚ |
| JPA | -1 | Slightly Negative | -0.1151 | -0.7215 |  | 6 | — | — | ✚ |
| FIFA | -1 | Slightly Negative | -0.1302 | -0.7933 |  | 8 | — | — | ✚ |
| Suruhanjaya Pencegahan Rasuah Malaysia | -1 | Slightly Negative | -0.1591 | -0.9308 |  | 2 | — | — |  |
| Grab | -1 | Slightly Negative | -0.1979 | -1.1153 |  | 6 | — | — | ✚ |
| Parti Keadilan Rakyat | -1 | Slightly Negative | -0.2023 | -1.1362 |  | 1 | PH | PKR |  |
| Galen Centre | -1 | Slightly Negative | -0.2023 | -1.1362 |  | 2 | — | — | ✚ |
| Parliament | -1 | Slightly Negative | -0.2120 | -1.1824 |  | 3 | — | — | ✚ |
### LOCATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| United States | +2 | Positive | 0.5846 | 2.6063 | ⚠️ | 4 | — | — | ✚ |
| Kunak | +2 | Positive | 0.3811 | 1.6385 |  | 5 | — | — | ✚ |
| Subang | +2 | Positive | 0.3484 | 1.4829 |  | 2 | — | — | ✚ |
| Bintulu | +2 | Positive | 0.3057 | 1.2799 |  | 5 | — | — | ✚ |
| Kota Kinabalu | +1 | Slightly Positive | 0.2901 | 1.2057 |  | 5 | — | — |  |
| Thailand | +1 | Slightly Positive | 0.2502 | 1.0159 |  | 16 | — | — | ✚ |
| Putatan | +1 | Slightly Positive | 0.2360 | 0.9484 |  | 7 | — | — | ✚ |
| Negri Sembilan | +1 | Slightly Positive | 0.2003 | 0.7786 |  | 1 | — | — | ✚ |
| Kemaman | +1 | Slightly Positive | 0.1931 | 0.7443 |  | 5 | — | — | ✚ |
| Ranau | +1 | Slightly Positive | 0.1676 | 0.6230 |  | 4 | — | — | ✚ |
| Negeri Sembilan | +1 | Slightly Positive | 0.1657 | 0.6140 |  | 30 | — | — |  |
| Sabah | +1 | Slightly Positive | 0.1103 | 0.3505 |  | 30 | — | — |  |
| Banting | +1 | Slightly Positive | 0.1096 | 0.3472 |  | 4 | — | — | ✚ |
| Kuching | +1 | Slightly Positive | 0.1061 | 0.3305 |  | 3 | — | — |  |
| Sarawak | +0 | Neutral | 0.0951 | 0.2782 |  | 23 | — | — |  |
| Melaka | +0 | Neutral | 0.0850 | 0.2302 |  | 13 | — | — |  |
| US | +0 | Neutral | 0.0786 | 0.1998 |  | 30 | — | — | ✚ |
| UK | +0 | Neutral | 0.0747 | 0.1812 |  | 30 | — | — | ✚ |
| Putrajaya | +0 | Neutral | 0.0744 | 0.1798 |  | 11 | — | — | ✚ |
| Sepang | +0 | Neutral | 0.0691 | 0.1546 |  | 11 | — | — | ✚ |
| Terengganu | +0 | Neutral | 0.0547 | 0.0861 |  | 9 | — | — | ✚ |
| Seremban | +0 | Neutral | 0.0427 | 0.0290 |  | 3 | — | — | ✚ |
| Kuala Lumpur | +0 | Neutral | 0.0385 | 0.0090 |  | 30 | — | — |  |
| Chennah | +0 | Neutral | 0.0262 | -0.0495 |  | 8 | — | — | ✚ |
| Hungary | +0 | Neutral | 0.0261 | -0.0499 |  | 5 | — | — | ✚ |
| Selangor | +0 | Neutral | 0.0183 | -0.0870 |  | 25 | — | — |  |
| Singapore | +0 | Neutral | 0.0139 | -0.1080 |  | 16 | — | — | ✚ |
| Rompin | +0 | Neutral | 0.0103 | -0.1251 |  | 5 | — | — | ✚ |
| Glasgow | +0 | Neutral | 0.0075 | -0.1384 |  | 17 | — | — | ✚ |
| India | +0 | Neutral | 0.0002 | -0.1731 |  | 30 | — | — | ✚ |
| Linggi | +0 | Neutral | 0.0000 | -0.1741 |  | 3 | — | — |  |
| N14 | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | — | — |  |
| Pasir Gudang | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | — | — |  |
| Penang | +0 | Neutral | 0.0000 | -0.1741 |  | 10 | — | — |  |
| Perak | +0 | Neutral | 0.0000 | -0.1741 |  | 14 | — | — |  |
| Pertang | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — |  |
| Rantau | +0 | Neutral | 0.0000 | -0.1741 |  | 2 | — | — |  |
| Ampangan | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | — | — | ✚ |
| Batu Pahat | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Beaufort | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Beluran | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Betong | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Brunei | +0 | Neutral | 0.0000 | -0.1741 |  | 2 | — | — | ✚ |
| Cameron Highlands | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Dungun | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Gombak | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Hulu Selangor | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Kangar | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Kedah | +0 | Neutral | 0.0000 | -0.1741 |  | 8 | — | — | ✚ |
| Keningau | +0 | Neutral | 0.0000 | -0.1741 |  | 5 | — | — | ✚ |
| Klang | +0 | Neutral | 0.0000 | -0.1741 |  | 3 | — | — | ✚ |
| Klang Valley | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Korea | +0 | Neutral | 0.0000 | -0.1741 |  | 7 | — | — | ✚ |
| Kota Bharu | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Kota Tinggi | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Kuala Selangor | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Kuala Terengganu | +0 | Neutral | 0.0000 | -0.1741 |  | 3 | — | — | ✚ |
| Kuantan | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Kudat | +0 | Neutral | 0.0000 | -0.1741 |  | 2 | — | — | ✚ |
| Kulai | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Lahad Datu | +0 | Neutral | 0.0000 | -0.1741 |  | 2 | — | — | ✚ |
| Limbang | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Lipis | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Maran | +0 | Neutral | 0.0000 | -0.1741 |  | 5 | — | — | ✚ |
| Mersing | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Miri | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Muar | +0 | Neutral | 0.0000 | -0.1741 |  | 5 | — | — | ✚ |
| North Sumatra | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Pahang | +0 | Neutral | 0.0000 | -0.1741 |  | 10 | — | — | ✚ |
| Pasir Puteh | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Penampang | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Perlis | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Petaling Jaya | +0 | Neutral | 0.0000 | -0.1741 |  | 3 | — | — | ✚ |
| Pontian | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Samarahan | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Sandakan | +0 | Neutral | 0.0000 | -0.1741 |  | 6 | — | — | ✚ |
| Sarikei | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Segamat | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | — | — | ✚ |
| Semporna | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Serian | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Sibu | +0 | Neutral | 0.0000 | -0.1741 |  | 3 | — | — | ✚ |
| South Korea | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Tambunan | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| Tenom | +0 | Neutral | 0.0000 | -0.1741 |  | 5 | — | — | ✚ |
| Tawau | +0 | Neutral | -0.0059 | -0.2021 |  | 12 | — | — | ✚ |
| Johor | +0 | Neutral | -0.0118 | -0.2302 |  | 25 | — | — |  |
| France | +0 | Neutral | -0.0132 | -0.2369 |  | 16 | — | — | ✚ |
| China | +0 | Neutral | -0.0553 | -0.4371 |  | 22 | — | — | ✚ |
| Argentina | +0 | Neutral | -0.0645 | -0.4808 |  | 4 | — | — | ✚ |
| Malaysia | +0 | Neutral | -0.0791 | -0.5503 |  | 30 | — | — | ✚ |
| Iran | +0 | Neutral | -0.0852 | -0.5793 |  | 30 | — | — | ✚ |
| Parliament House | -1 | Slightly Negative | -0.1272 | -0.7790 |  | 5 | — | — |  |
| Spain | -1 | Slightly Negative | -0.1732 | -0.9978 |  | 12 | — | — | ✚ |
| Japan | -1 | Slightly Negative | -0.1796 | -1.0283 |  | 5 | — | — | ✚ |
| Ipoh | -1 | Slightly Negative | -0.2465 | -1.3464 |  | 11 | — | — | ✚ |
| Indonesia | -1 | Slightly Negative | -0.2498 | -1.3621 |  | 12 | — | — | ✚ |
| Kelantan | -1 | Slightly Negative | -0.2514 | -1.3697 |  | 7 | — | — | ✚ |
| England | -2 | Negative | -0.3039 | -1.6194 |  | 7 | — | — | ✚ |
| Shah Alam | -2 | Negative | -0.4313 | -2.2254 | ⚠️ | 4 | — | — | ✚ |
| Yemen | -2 | Negative | -0.4885 | -2.4974 | ⚠️ | 4 | — | — | ✚ |
| Saudi Arabia | -3 | Very Negative | -0.6055 | -3.0539 | ⚠️ | 3 | — | — | ✚ |
| West Asia | -3 | Very Negative | -0.6536 | -3.2826 | ⚠️ | 5 | — | — | ✚ |
| Middle East | -3 | Very Negative | -0.6797 | -3.4068 | ⚠️ | 2 | — | — | ✚ |
### EVENT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| WAN IFRA ASIA MEDIA AWARDS 2025 | +3 | Very Positive | 0.9187 | 4.1953 | ⚠️ | 2 | — | — | ✚ |
| Court case | +3 | Very Positive | 0.7717 | 3.4962 | ⚠️ | 1 | — | — | ✚ |
| Hearing | +2 | Positive | 0.5522 | 2.4522 | ⚠️ | 4 | — | — | ✚ |
| Investigation | +2 | Positive | 0.4746 | 2.0831 | ⚠️ | 4 | — | — | ✚ |
| Summit | +2 | Positive | 0.4736 | 2.0784 | ⚠️ | 5 | — | — | ✚ |
| Trial | +2 | Positive | 0.3499 | 1.4901 |  | 7 | — | — | ✚ |
| Appeal | +1 | Slightly Positive | 0.1997 | 0.7757 |  | 13 | — | — | ✚ |
| Piala Dunia | +1 | Slightly Positive | 0.1604 | 0.5888 |  | 8 | — | — | ✚ |
| Negeri Sembilan polls | +1 | Slightly Positive | 0.1048 | 0.3244 |  | 10 | — | — | ✚ |
| manifesto | +0 | Neutral | 0.0470 | 0.0495 |  | 26 | — | — | ✚ |
| campaign | +0 | Neutral | 0.0188 | -0.0847 |  | 20 | — | — |  |
| election | +0 | Neutral | 0.0078 | -0.1370 |  | 14 | — | — | ✚ |
| BN Candidate Announcement (NS) | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | — | — |  |
| ceramah | +0 | Neutral | 0.0000 | -0.1741 |  | 3 | — | — |  |
| HAWANA X TM Media Event | +0 | Neutral | 0.0000 | -0.1741 |  | 7 | — | — |  |
| Johor State Election | +0 | Neutral | 0.0000 | -0.1741 |  | 3 | — | — |  |
| kempen | +0 | Neutral | 0.0000 | -0.1741 |  | 11 | — | — |  |
| majlis | +0 | Neutral | 0.0000 | -0.1741 |  | 7 | — | — |  |
| Negeri Sembilan State Election 2026 | +0 | Neutral | 0.0000 | -0.1741 |  | 9 | — | — |  |
| Sarawak State Election 2026 | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | — | — |  |
| walkabout | +0 | Neutral | 0.0000 | -0.1741 |  | 2 | — | — |  |
| pilihan raya | +0 | Neutral | 0.0000 | -0.1741 |  | 5 | — | — | ✚ |
| pilihan raya negeri | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | — | — | ✚ |
| Pilihan Raya Negeri Johor | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| PRN Negeri | +0 | Neutral | 0.0000 | -0.1741 |  | 6 | — | — | ✚ |
| sidang akhbar | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| World Cup | +0 | Neutral | -0.0217 | -0.2773 |  | 11 | — | — | ✚ |
| Glasgow 2026 | +0 | Neutral | -0.0678 | -0.4965 |  | 8 | — | — | ✚ |
| event | +0 | Neutral | -0.0820 | -0.5641 |  | 22 | — | — |  |
| Probe | +0 | Neutral | -0.0823 | -0.5655 |  | 9 | — | — | ✚ |
| rally | -1 | Slightly Negative | -0.1262 | -0.7743 |  | 3 | — | — |  |
| Charged | -1 | Slightly Negative | -0.2212 | -1.2261 |  | 1 | — | — | ✚ |
### CONCEPT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Onn Hafiz 56-seats solo bid | +3 | Very Positive | 0.7334 | 3.3140 | ⚠️ | 1 | — | — |  |
| artificial intelligence | +3 | Very Positive | 0.7096 | 3.2008 | ⚠️ | 1 | — | — | ✚ |
| green technology | +3 | Very Positive | 0.6705 | 3.0149 | ⚠️ | 1 | — | — | ✚ |
| renewable energy | +3 | Very Positive | 0.6705 | 3.0149 | ⚠️ | 1 | — | — | ✚ |
| water supply | +2 | Positive | 0.5106 | 2.2544 | ⚠️ | 1 | — | — | ✚ |
| grassroots | +2 | Positive | 0.3400 | 1.4430 |  | 1 | — | — | ✚ |
| MADANI government | +1 | Slightly Positive | 0.2677 | 1.0991 |  | 2 | — | — |  |
| copyright | +1 | Slightly Positive | 0.2458 | 0.9950 |  | 18 | — | — | ✚ |
| Super El Nino food security | +1 | Slightly Positive | 0.2229 | 0.8861 |  | 0 | — | — |  |
| take-home income | +1 | Slightly Positive | 0.2023 | 0.7881 |  | 1 | — | — | ✚ |
| Wealth tax | +1 | Slightly Positive | 0.1482 | 0.5308 |  | 0 | — | — |  |
| AI | +0 | Neutral | 0.0908 | 0.2578 |  | 30 | — | — | ✚ |
| perpaduan | +0 | Neutral | 0.0251 | -0.0547 |  | 7 | — | — | ✚ |
| Bersatu own logo in N9 | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | — | — |  |
| Cost of living | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | — | — |  |
| Service tax | +0 | Neutral | 0.0000 | -0.1741 |  | 3 | — | — |  |
| Subsidies & welfare aid | +0 | Neutral | 0.0000 | -0.1741 |  | 2 | — | — |  |
| Third force movement | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | — | — |  |
| UEC recognition | +0 | Neutral | 0.0000 | -0.1741 |  | 0 | — | — |  |
| constitutional rights | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | — | — | ✚ |
| Israeli deportation | +0 | Neutral | 0.0000 | -0.1741 |  | 1 | — | — | ✚ |
| MediAsas | +0 | Neutral | 0.0000 | -0.1741 |  | 4 | — | — | ✚ |
| pork supply | +0 | Neutral | 0.0000 | -0.1741 |  | 2 | — | — | ✚ |
| Reformasi | +0 | Neutral | 0.0000 | -0.1741 |  | 3 | — | — | ✚ |
| nominated assemblymen | -2 | Negative | -0.4537 | -2.3319 | ⚠️ | 3 | — | — | ✚ |
| national unity | -2 | Negative | -0.5195 | -2.6448 | ⚠️ | 2 | — | — | ✚ |
| democratic power | -3 | Very Negative | -0.6019 | -3.0367 | ⚠️ | 2 | — | — | ✚ |
| gig economy | -3 | Very Negative | -0.6369 | -3.2032 | ⚠️ | 1 | — | — | ✚ |
---

## Methodology

1. **Entity Source:** Loaded from the 2026-07-26T14:00+08 extraction roster (279 Phase-1 entity names) plus the 78 canonical entities from the per-entity index. Roster names were merged into canonical entities by normalized name/alias matching (honorific-stripped); unmerged names were added as new entities (194 new).
2. **Context Extraction:** For each entity, search variants (canonical name + aliases + roster matches) were located in the 2026-07-26 raw source collection (24 sources, 24 processed, ~730188 chars). A context window (~140+170 chars) was extracted around each mention (markdown stripped, de-duplicated, capped at 30/entity).
3. **Sentiment Scoring:** Applied VADER to each context snippet; entity sentiment = mean compound across snippets.
4. **Score Mapping:** VADER compound (-1..+1) → 7-point Likert (-3..+3): +3 ≥0.6, +2 ≥0.3, +1 ≥0.1, 0 (-0.1..0.1), -1 >-0.3, -2 >-0.6, -3 ≤-0.6.
5. **Anomaly Detection:** Z-score on raw compound vs overall mean/std; flagged when |z| > 2.
6. **Coalition/Party Aggregation:** Persons + political-party/coalition orgs mapped via per-entity metadata and affiliation maps (FIGURE_AFFILIATIONS, ORG_TO_COALITION, analyst-extended NEW_FIGURE_AFFIL).

---

*Report generated by OpenCLaw Sentiment Analysis Pipeline (sentiment-analysis skill)*
*VADER: Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.*

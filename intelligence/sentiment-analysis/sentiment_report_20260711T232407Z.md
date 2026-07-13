# Sentiment Analysis Report

**Classification:** TLP:AMBER
**Report Timestamp:** 20260711T232407Z
**Extraction Source:** 2026-07-11T23:07:46.271245Z
**Source Collection:** 2026-07-11T222116Z_political_collection_25sources_OPERATIONAL.json
**Source Timestamp:** 2026-07-11T222116Z
**Analysis Method:** VADER Sentiment Analysis on source article context
**Score Range:** -3 (very negative) to +3 (very positive)
**Anomaly Threshold:** |z-score| > 2

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Entities Analyzed | 255 |
| Sources Processed | 24 |
| Sources with Content | 24 |
| Entities with Context | 219 |
| Entities without Context (fallback) | 36 |
| Overall Mean Sentiment | +0.294 |
| Overall Std Deviation | 1.256 |
| Overall Median Sentiment | +0.000 |
| Sentiment Range | [-3, +3] |
| Positive Entities | 88 |
| Neutral Entities | 134 |
| Negative Entities | 33 |
| Anomalies Detected | 25 |

### Sentiment Distribution

```
Positive (88)  ████████████████████████████████████████████████████████████████████████████████████████
Neutral  (134)  ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
Negative (33)  █████████████████████████████████
```

---

## Coalition / Party Aggregate Sentiment

| Coalition | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range |
|-----------|:-:|------|:----------:|:-------:|:--------:|:-----:|
| WARISAN | +2 | Positive | 0.4593 | 0.0000 | 1 | [0.459, 0.459] |
| GPS | +2 | Positive | 0.3681 | 0.5206 | 2 | [0.000, 0.736] |
| BERSAMA | +1 | Slightly Positive | 0.1130 | 0.0979 | 3 | [0.000, 0.170] |
| INDEPENDENT | +0 | Neutral | 0.0954 | 0.2958 | 8 | [-0.021, 0.827] |
| PN | +0 | Neutral | 0.0937 | 0.1964 | 8 | [-0.009, 0.562] |
| BN | +0 | Neutral | 0.0787 | 0.3202 | 22 | [-0.743, 0.562] |
| PH | +0 | Neutral | 0.0336 | 0.1541 | 22 | [-0.495, 0.353] |
| GRS | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| PEJUANG | +0 | Neutral | 0.0000 | 0.0000 | 4 | [0.000, 0.000] |

### Coalition Entities
- **WARISAN** (+2, Positive): WARISAN
- **GPS** (+2, Positive): Abang Johari, GPS
- **BERSAMA** (+1, Slightly Positive): BERSAMA, Bersama, Parti Bersama
- **INDEPENDENT** (+0, Neutral): Alyaa Alhadjri, B Nantha Kumar, Bridget Welsh, Hakim Danish, Massila Kamalrudin, Mustapha, Qistina Nadia Dzulqarnain, Ts Dr Massila Kamalrudin
- **PN** (+0, Neutral): Muhammad Sanusi Md Nor, Noraziah Mohd Razit, Sanusi, BERSATU, Bersatu, PAS, PN, Perikatan Nasional
- **BN** (+0, Neutral): Abdul Razak, Ahmad Zahid, Ahmad Zahid Hamidi, Asyraf Wajdi Dusuki, Datuk Dr Asyraf Wajdi Dusuki, Datuk Seri Ramlan Harun, Datuk Zahari Sarip, Dr Ahmad Zahid Hamidi, Isham Ishak, Onn Abu Bakar, Onn Hafiz, Onn Hafiz Ghazi, Ramlan Harun, Ramli Ngah Talib, Tun Abdul Razak, Tun Ramli Ngah Talib, Zahari Sarip, Zahid Hamidi, BN, Barisan Nasional, MCA, UMNO
- **PH** (+0, Neutral): Amirudin Shari, Anthony Loke, Anthony Loke Siew Fook, Anwar, Anwar Ibrahim, Datuk Seri Amirudin Shari, Datuk Seri Anwar Ibrahim, Dzulkefly Ahmad, Fahmi Fadzil, Hasnah Jusid, Maszlee Malik, Mat Sabu, Mohamad Sabu, Nurul Izzah, Nurul Izzah Anwar, PM Anwar, Syed Saddiq, AMANAH, DAP, MUDA, PH, Pakatan Harapan
- **GRS** (+0, Neutral): GRS
- **PEJUANG** (+0, Neutral): Dr Mahathir Mohamad, Mahathir Mohamad, Tun Dr Mahathir Mohamad, Pejuang

---

## Sentiment Anomalies (|z-score| > 2)

**25 anomalies detected.**

| # | Entity | Type | Score | Label | Z-Score | Direction | Coalition | Mentions |
|---|--------|------|:-----:|-------|:-------:|:---------:|-----------|:--------:|
| 1 | Datuk David Chong Ket Sui | PERSON | +3 | Very Positive | 2.8928 | positive | N/A | 1 |
| 2 | David Chong Ket Sui | PERSON | +3 | Very Positive | 2.8928 | positive | N/A | 1 |
| 3 | Petronas | ORGANIZATION | +3 | Very Positive | 2.8559 | positive | N/A | 1 |
| 4 | renewable energy | CONCEPT | +3 | Very Positive | 2.8301 | positive | N/A | 1 |
| 5 | Ramli | PERSON | -3 | Very Negative | -2.7350 | negative | N/A | 2 |
| 6 | Ramli Ngah Talib | PERSON | -3 | Very Negative | -2.7350 | negative | BN | 2 |
| 7 | Tun Ramli Ngah Talib | PERSON | -3 | Very Negative | -2.7350 | negative | BN | 2 |
| 8 | abortion | CONCEPT | -3 | Very Negative | -2.6219 | negative | N/A | 1 |
| 9 | community pharmacies | CONCEPT | -3 | Very Negative | -2.6219 | negative | N/A | 1 |
| 10 | Mustapha | PERSON | +3 | Very Positive | 2.5829 | positive | INDEPENDENT | 1 |
| 11 | oil and gas | CONCEPT | -3 | Very Negative | -2.4153 | negative | N/A | 1 |
| 12 | Morocco | LOCATION | +3 | Very Positive | 2.3468 | positive | N/A | 2 |
| 13 | semi-finals | EVENT | +3 | Very Positive | 2.3468 | positive | N/A | 2 |
| 14 | KPKM | ORGANIZATION | -3 | Very Negative | -2.3140 | negative | N/A | 1 |
| 15 | budget cuts | CONCEPT | -3 | Very Negative | -2.3140 | negative | N/A | 1 |
| 16 | fertiliser price | CONCEPT | -3 | Very Negative | -2.3140 | negative | N/A | 1 |
| 17 | food subsidies | CONCEPT | -3 | Very Negative | -2.3140 | negative | N/A | 1 |
| 18 | harm reduction | CONCEPT | -3 | Very Negative | -2.3140 | negative | N/A | 1 |
| 19 | pork supply | CONCEPT | -3 | Very Negative | -2.3140 | negative | N/A | 1 |
| 20 | Abang Johari | PERSON | +3 | Very Positive | 2.2753 | positive | GPS | 3 |
| 21 | Inanam | LOCATION | -2 | Negative | -2.2029 | negative | N/A | 1 |
| 22 | Manggatal | LOCATION | -2 | Negative | -2.2029 | negative | N/A | 1 |
| 23 | water supply | CONCEPT | -2 | Negative | -2.2029 | negative | N/A | 1 |
| 24 | DVS | ORGANIZATION | +3 | Very Positive | 2.1212 | positive | N/A | 1 |
| 25 | SOBA 2025 | EVENT | -2 | Negative | -2.1064 | negative | N/A | 1 |

---

## Entity Sentiments by Type

### PERSON

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| Datuk David Chong Ket Sui | +3 | Very Positive | 0.9186 | 2.8928 | ⚠️ | 1 | — |
| David Chong Ket Sui | +3 | Very Positive | 0.9186 | 2.8928 | ⚠️ | 1 | — |
| Mustapha | +3 | Very Positive | 0.8271 | 2.5829 | ⚠️ | 1 | INDEPENDENT |
| Abang Johari | +3 | Very Positive | 0.7363 | 2.2753 | ⚠️ | 3 | GPS |
| Datuk Mohd Arifin Mohd Arif | +2 | Positive | 0.5719 | 1.7185 |  | 1 | — |
| Mohd Arifin Mohd Arif | +2 | Positive | 0.5719 | 1.7185 |  | 1 | — |
| Datuk Zahari Sarip | +2 | Positive | 0.5622 | 1.6857 |  | 1 | BN |
| Noraziah Mohd Razit | +2 | Positive | 0.5622 | 1.6857 |  | 1 | PN |
| Zahari Sarip | +2 | Positive | 0.5622 | 1.6857 |  | 1 | BN |
| Dr Ahmad Zahid Hamidi | +2 | Positive | 0.3025 | 0.8061 |  | 5 | BN |
| Asyraf Wajdi Dusuki | +1 | Slightly Positive | 0.2556 | 0.6472 |  | 2 | BN |
| Datuk Dr Asyraf Wajdi Dusuki | +1 | Slightly Positive | 0.2556 | 0.6472 |  | 2 | BN |
| Ahmad Zahid | +1 | Slightly Positive | 0.2161 | 0.5134 |  | 7 | BN |
| Ahmad Zahid Hamidi | +1 | Slightly Positive | 0.2161 | 0.5134 |  | 7 | BN |
| Zahid Hamidi | +1 | Slightly Positive | 0.2161 | 0.5134 |  | 7 | BN |
| Mat Sabu | +1 | Slightly Positive | 0.2023 | 0.4667 |  | 1 | PH |
| Mohamad Sabu | +1 | Slightly Positive | 0.2023 | 0.4667 |  | 1 | PH |
| Onn Hafiz Ghazi | +1 | Slightly Positive | 0.1889 | 0.4213 |  | 8 | BN |
| Amirudin Shari | +1 | Slightly Positive | 0.1767 | 0.3800 |  | 4 | PH |
| Anwar | +1 | Slightly Positive | 0.1295 | 0.2201 |  | 10 | PH |
| PM Anwar | +1 | Slightly Positive | 0.1140 | 0.1676 |  | 4 | PH |
| Datuk | +0 | Neutral | 0.0980 | 0.1134 |  | 10 | — |
| Datuk Seri | +0 | Neutral | 0.0514 | -0.0444 |  | 10 | — |
| Onn Hafiz | +0 | Neutral | 0.0476 | -0.0573 |  | 10 | BN |
| Tun | +0 | Neutral | 0.0021 | -0.2114 |  | 10 | — |
| Abdul Razak | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | BN |
| Ampuan Afzan Hospital | +0 | Neutral | 0.0000 | -0.2185 |  | 2 | — |
| Anthony Loke | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | PH |
| Anthony Loke Siew Fook | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | PH |
| Anwar Ibrahim | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | PH |
| Bridget Welsh | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | INDEPENDENT |
| Datuk Seri Amirudin Shari | +0 | Neutral | 0.0000 | -0.2185 |  | 3 | PH |
| Datuk Seri Anwar Ibrahim | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | PH |
| Datuk Seri Ramlan Harun | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | BN |
| Dr Ismail Abd | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| Dr Mahathir Mohamad | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | PEJUANG |
| Dzulkefly Ahmad | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | PH |
| Hakim Danish | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | INDEPENDENT |
| Isham Ishak | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | BN |
| Mahathir Mohamad | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | PEJUANG |
| Massila Kamalrudin | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | INDEPENDENT |
| Maszlee Malik | +0 | Neutral | 0.0000 | -0.2185 |  | 5 | PH |
| Mohd Taha | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Muhammad Sanusi Md Nor | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | PN |
| Nurul Izzah | +0 | Neutral | 0.0000 | -0.2185 |  | 3 | PH |
| Nurul Izzah Anwar | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | PH |
| Rafizi | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| Rafizi Ramli | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| Ramlan Harun | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | BN |
| Sanusi | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | PN |
| Syed Saddiq | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | PH |
| Ts Dr Massila Kamalrudin | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | INDEPENDENT |
| Tun Abdul Razak | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | BN |
| Tun Dr Mahathir Mohamad | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | PEJUANG |
| Alyaa Alhadjri | +0 | Neutral | -0.0213 | -0.2906 |  | 2 | INDEPENDENT |
| B Nantha Kumar | +0 | Neutral | -0.0213 | -0.2906 |  | 2 | INDEPENDENT |
| Qistina Nadia Dzulqarnain | +0 | Neutral | -0.0213 | -0.2906 |  | 2 | INDEPENDENT |
| Hasnah Jusid | +0 | Neutral | -0.0258 | -0.3059 |  | 2 | PH |
| Onn Abu Bakar | -1 | Slightly Negative | -0.2151 | -0.9470 |  | 2 | BN |
| Fahmi Fadzil | -2 | Negative | -0.4953 | -1.8961 |  | 3 | PH |
| Ramli | -3 | Very Negative | -0.7430 | -2.7350 | ⚠️ | 2 | — |
| Ramli Ngah Talib | -3 | Very Negative | -0.7430 | -2.7350 | ⚠️ | 2 | BN |
| Tun Ramli Ngah Talib | -3 | Very Negative | -0.7430 | -2.7350 | ⚠️ | 2 | BN |

### ORGANIZATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| Petronas | +3 | Very Positive | 0.9077 | 2.8559 | ⚠️ | 1 | — |
| DVS | +3 | Very Positive | 0.6908 | 2.1212 | ⚠️ | 1 | — |
| Federal Govt | +2 | Positive | 0.5145 | 1.5241 |  | 3 | — |
| WARISAN | +2 | Positive | 0.4593 | 1.3372 |  | 2 | WARISAN |
| Malay Mail | +2 | Positive | 0.3899 | 1.1021 |  | 2 | — |
| Daily Express | +2 | Positive | 0.3816 | 1.0740 |  | 2 | — |
| AMANAH | +2 | Positive | 0.3533 | 0.9781 |  | 2 | PH |
| Election Commission | +1 | Slightly Positive | 0.2884 | 0.7583 |  | 3 | — |
| SK hynix | +1 | Slightly Positive | 0.2506 | 0.6303 |  | 5 | — |
| Barisan Nasional | +1 | Slightly Positive | 0.2148 | 0.5090 |  | 10 | BN |
| MIC | +1 | Slightly Positive | 0.2132 | 0.5036 |  | 10 | — |
| ASEAN | +1 | Slightly Positive | 0.2087 | 0.4884 |  | 8 | — |
| JKNS | +1 | Slightly Positive | 0.2023 | 0.4667 |  | 1 | — |
| UMNO | +1 | Slightly Positive | 0.1933 | 0.4362 |  | 10 | BN |
| NST | +1 | Slightly Positive | 0.1859 | 0.4111 |  | 10 | — |
| BERSAMA | +1 | Slightly Positive | 0.1695 | 0.3556 |  | 10 | BERSAMA |
| Bersama | +1 | Slightly Positive | 0.1695 | 0.3556 |  | 10 | BERSAMA |
| Free Malaysia Today | +1 | Slightly Positive | 0.1532 | 0.3004 |  | 0 | — |
| Bernama | +1 | Slightly Positive | 0.1409 | 0.2587 |  | 10 | — |
| PN | +1 | Slightly Positive | 0.1392 | 0.2530 |  | 10 | PN |
| BN | +1 | Slightly Positive | 0.1354 | 0.2401 |  | 10 | BN |
| MalaysiaGazette | +1 | Slightly Positive | 0.1227 | 0.1971 |  | 6 | — |
| MUDA | +0 | Neutral | 0.0984 | 0.1148 |  | 10 | PH |
| AirBorneo | +0 | Neutral | 0.0958 | 0.1060 |  | 4 | — |
| PAS | +0 | Neutral | 0.0670 | 0.0084 |  | 10 | PN |
| mStar | +0 | Neutral | 0.0670 | 0.0084 |  | 10 | — |
| MCA | +0 | Neutral | 0.0655 | 0.0034 |  | 10 | BN |
| The Edge Malaysia | +0 | Neutral | 0.0637 | -0.0027 |  | 2 | — |
| SPR | +0 | Neutral | 0.0336 | -0.1047 |  | 10 | — |
| MACC | +0 | Neutral | 0.0190 | -0.1541 |  | 2 | — |
| MOH | +0 | Neutral | 0.0087 | -0.1890 |  | 10 | — |
| BERSIH | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| DAP | +0 | Neutral | 0.0000 | -0.2185 |  | 10 | PH |
| Dewan Rakyat | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| GPS | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | GPS |
| GRS | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | GRS |
| Grab | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| HTAR Klang | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| Kosmo | +0 | Neutral | 0.0000 | -0.2185 |  | 4 | — |
| Parti Bersama | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | BERSAMA |
| Pejuang | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | PEJUANG |
| Perikatan Nasional | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | PN |
| Sinar Harian | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Suara Keadilan | +0 | Neutral | 0.0000 | -0.2185 |  | 2 | — |
| Sultan Ahmad Shah Medical Centre | +0 | Neutral | 0.0000 | -0.2185 |  | 2 | — |
| Tengku Ampuan Afzan Hospital | +0 | Neutral | 0.0000 | -0.2185 |  | 2 | — |
| World of Buzz | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| PH | +0 | Neutral | -0.0031 | -0.2290 |  | 10 | PH |
| BERSATU | +0 | Neutral | -0.0095 | -0.2507 |  | 10 | PN |
| Bersatu | +0 | Neutral | -0.0095 | -0.2507 |  | 10 | PN |
| Pakatan Harapan | +0 | Neutral | -0.0130 | -0.2625 |  | 10 | PH |
| Malaysiakini | +0 | Neutral | -0.0213 | -0.2906 |  | 2 | — |
| CHT | +0 | Neutral | -0.0258 | -0.3059 |  | 2 | — |
| FIFA | +0 | Neutral | -0.0506 | -0.3899 |  | 4 | — |
| TikTok | -1 | Slightly Negative | -0.1294 | -0.6568 |  | 8 | — |
| Parliament | -1 | Slightly Negative | -0.1531 | -0.7370 |  | 1 | — |
| EC | -1 | Slightly Negative | -0.1910 | -0.8654 |  | 10 | — |
| Tropicana | -1 | Slightly Negative | -0.2541 | -1.0791 |  | 5 | — |
| Spotify | -2 | Negative | -0.4139 | -1.6204 |  | 5 | — |
| KPKM | -3 | Very Negative | -0.6187 | -2.3140 | ⚠️ | 1 | — |

### LOCATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| Morocco | +3 | Very Positive | 0.7574 | 2.3468 | ⚠️ | 2 | — |
| Thailand | +3 | Very Positive | 0.6401 | 1.9495 |  | 3 | — |
| Banting | +3 | Very Positive | 0.6391 | 1.9461 |  | 4 | — |
| Jementah | +2 | Positive | 0.5622 | 1.6857 |  | 1 | — |
| France | +2 | Positive | 0.5404 | 1.6118 |  | 4 | — |
| Russia | +2 | Positive | 0.4827 | 1.4164 |  | 3 | — |
| Miri | +2 | Positive | 0.4593 | 1.3372 |  | 2 | — |
| United States | +2 | Positive | 0.4535 | 1.3175 |  | 9 | — |
| Perlis | +2 | Positive | 0.4312 | 1.2420 |  | 3 | — |
| Sabah | +2 | Positive | 0.3830 | 1.0787 |  | 10 | — |
| Likas | +2 | Positive | 0.3612 | 1.0049 |  | 1 | — |
| Tawau | +2 | Positive | 0.3313 | 0.9036 |  | 4 | — |
| Buloh Kasap | +1 | Slightly Positive | 0.2811 | 0.7336 |  | 2 | — |
| Kulai | +1 | Slightly Positive | 0.2545 | 0.6435 |  | 3 | — |
| Kuala Lumpur | +1 | Slightly Positive | 0.2289 | 0.5568 |  | 10 | — |
| Kota Kinabalu | +1 | Slightly Positive | 0.2223 | 0.5344 |  | 6 | — |
| Kuching | +1 | Slightly Positive | 0.2124 | 0.5009 |  | 6 | — |
| Johor Bahru | +1 | Slightly Positive | 0.2053 | 0.4769 |  | 10 | — |
| West Asia | +1 | Slightly Positive | 0.2023 | 0.4667 |  | 1 | — |
| Sandakan | +1 | Slightly Positive | 0.1845 | 0.4064 |  | 4 | — |
| Sarawak | +1 | Slightly Positive | 0.1549 | 0.3062 |  | 10 | — |
| Machap | +1 | Slightly Positive | 0.1234 | 0.1995 |  | 10 | — |
| Penampang | +1 | Slightly Positive | 0.1109 | 0.1571 |  | 3 | — |
| Bukit Naning | +0 | Neutral | 0.0987 | 0.1158 |  | 3 | — |
| Iran | +0 | Neutral | 0.0820 | 0.0592 |  | 10 | — |
| Muar | +0 | Neutral | 0.0740 | 0.0321 |  | 4 | — |
| Johor | +0 | Neutral | 0.0670 | 0.0084 |  | 10 | — |
| Penang | +0 | Neutral | 0.0053 | -0.2005 |  | 6 | — |
| Batu Pahat | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Beluran | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Bintulu | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Boston | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| Czech | +0 | Neutral | 0.0000 | -0.2185 |  | 2 | — |
| Endau | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Iskandar Puteri | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Kedah | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Kempas | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Kota Tinggi | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Kuala Selangor | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Kudat | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Melaka | +0 | Neutral | 0.0000 | -0.2185 |  | 2 | — |
| Mersing | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Myanmar | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| N01 | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| N24 | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| N41 | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| Negeri Sembilan | +0 | Neutral | 0.0000 | -0.2185 |  | 4 | — |
| Pahang | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Perak | +0 | Neutral | 0.0000 | -0.2185 |  | 2 | — |
| Petaling Jaya | +0 | Neutral | 0.0000 | -0.2185 |  | 3 | — |
| Pontian | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Putatan | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Puteri Wangsa | +0 | Neutral | 0.0000 | -0.2185 |  | 10 | — |
| Putrajaya | +0 | Neutral | 0.0000 | -0.2185 |  | 3 | — |
| Rengit | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| Segamat | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Semporna | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Sultan Ahmad Shah | +0 | Neutral | 0.0000 | -0.2185 |  | 2 | — |
| Sultan Ismail | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| Tambunan | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Tenom | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Terengganu | +0 | Neutral | 0.0000 | -0.2185 |  | 2 | — |
| Tiram | +0 | Neutral | 0.0000 | -0.2185 |  | 3 | — |
| Uzbekistan | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Bangladesh | +0 | Neutral | -0.0129 | -0.2622 |  | 2 | — |
| Selangor | +0 | Neutral | -0.0566 | -0.4102 |  | 4 | — |
| Malaysia | +0 | Neutral | -0.0638 | -0.4346 |  | 10 | — |
| Strait of Hormuz | +0 | Neutral | -0.0766 | -0.4779 |  | 2 | — |
| Senggarang | -1 | Slightly Negative | -0.1075 | -0.5826 |  | 4 | — |
| Kelantan | -1 | Slightly Negative | -0.1998 | -0.8952 |  | 3 | — |
| Singapore | -1 | Slightly Negative | -0.2159 | -0.9497 |  | 10 | — |
| Lahad Datu | -1 | Slightly Negative | -0.2929 | -1.2105 |  | 2 | — |
| Inanam | -2 | Negative | -0.5859 | -2.2029 | ⚠️ | 1 | — |
| Manggatal | -2 | Negative | -0.5859 | -2.2029 | ⚠️ | 1 | — |

### EVENT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| semi-finals | +3 | Very Positive | 0.7574 | 2.3468 | ⚠️ | 2 | — |
| World Cup | +2 | Positive | 0.3617 | 1.0066 |  | 10 | — |
| Johor election | +2 | Positive | 0.3363 | 0.9206 |  | 9 | — |
| election | +2 | Positive | 0.3109 | 0.8345 |  | 10 | — |
| campaign | +1 | Slightly Positive | 0.2888 | 0.7597 |  | 3 | — |
| quarter-final | +1 | Slightly Positive | 0.2460 | 0.6147 |  | 3 | — |
| majlis | +1 | Slightly Positive | 0.2232 | 0.5375 |  | 3 | — |
| press conference | +1 | Slightly Positive | 0.2221 | 0.5338 |  | 5 | — |
| WAN IFRA ASIA MEDIA AWARDS 2025 | +1 | Slightly Positive | 0.1730 | 0.3675 |  | 0 | — |
| Johor Polls | +1 | Slightly Positive | 0.1130 | 0.1642 |  | 10 | — |
| state election | +1 | Slightly Positive | 0.1066 | 0.1426 |  | 10 | — |
| Johor State Election | +1 | Slightly Positive | 0.1040 | 0.1338 |  | 10 | — |
| PRN Johor | +0 | Neutral | 0.0670 | 0.0084 |  | 10 | — |
| pilihan raya | +0 | Neutral | 0.0633 | -0.0041 |  | 10 | — |
| pilihan raya negeri | +0 | Neutral | 0.0633 | -0.0041 |  | 10 | — |
| rally | +0 | Neutral | 0.0316 | -0.1115 |  | 3 | — |
| Johor Polls 2026 | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Johor State Election Results | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Pilihan Raya Negeri Johor | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| kempen | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| sidang akhbar | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| CHT Lifetime Achievement Award | +0 | Neutral | -0.0516 | -0.3933 |  | 1 | — |
| Piala Dunia | +0 | Neutral | -0.0811 | -0.4932 |  | 8 | — |
| event | -1 | Slightly Negative | -0.1063 | -0.5785 |  | 10 | — |
| ceramah | -2 | Negative | -0.4559 | -1.7626 |  | 1 | — |
| State Polls 2026 | -2 | Negative | -0.4709 | -1.8134 |  | 3 | — |
| SOBA 2025 | -2 | Negative | -0.5574 | -2.1064 | ⚠️ | 1 | — |

### CONCEPT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| renewable energy | +3 | Very Positive | 0.9001 | 2.8301 | ⚠️ | 1 | — |
| politics of hatred | +3 | Very Positive | 0.6239 | 1.8947 |  | 1 | — |
| racism | +3 | Very Positive | 0.6239 | 1.8947 |  | 1 | — |
| copyright | +2 | Positive | 0.3798 | 1.0679 |  | 10 | — |
| simple majority | +2 | Positive | 0.3644 | 1.0157 |  | 3 | — |
| subsidised diesel | +2 | Positive | 0.3612 | 1.0049 |  | 1 | — |
| deposits | +1 | Slightly Positive | 0.2483 | 0.6225 |  | 3 | — |
| doctor shortage | +1 | Slightly Positive | 0.2023 | 0.4667 |  | 1 | — |
| health insurance | +1 | Slightly Positive | 0.2023 | 0.4667 |  | 1 | — |
| anti-corruption | +1 | Slightly Positive | 0.1950 | 0.4420 |  | 4 | — |
| 56 seats | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| MADANI | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| Reformasi | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| artificial intelligence | +0 | Neutral | 0.0000 | -0.2185 |  | 1 | — |
| constituency | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| transport | +0 | Neutral | 0.0000 | -0.2185 |  | 0 | — |
| mandate | +0 | Neutral | -0.0387 | -0.3496 |  | 2 | — |
| AI | +0 | Neutral | -0.0509 | -0.3909 |  | 10 | — |
| two-thirds majority | +0 | Neutral | -0.0516 | -0.3933 |  | 1 | — |
| emergency triage | -1 | Slightly Negative | -0.2536 | -1.0774 |  | 2 | — |
| MHIT | -1 | Slightly Negative | -0.2960 | -1.2210 |  | 1 | — |
| MediAsas | -1 | Slightly Negative | -0.2960 | -1.2210 |  | 1 | — |
| water supply | -2 | Negative | -0.5859 | -2.2029 | ⚠️ | 1 | — |
| budget cuts | -3 | Very Negative | -0.6187 | -2.3140 | ⚠️ | 1 | — |
| fertiliser price | -3 | Very Negative | -0.6187 | -2.3140 | ⚠️ | 1 | — |
| food subsidies | -3 | Very Negative | -0.6187 | -2.3140 | ⚠️ | 1 | — |
| harm reduction | -3 | Very Negative | -0.6187 | -2.3140 | ⚠️ | 1 | — |
| pork supply | -3 | Very Negative | -0.6187 | -2.3140 | ⚠️ | 1 | — |
| oil and gas | -3 | Very Negative | -0.6486 | -2.4153 | ⚠️ | 1 | — |
| abortion | -3 | Very Negative | -0.7096 | -2.6219 | ⚠️ | 1 | — |
| community pharmacies | -3 | Very Negative | -0.7096 | -2.6219 | ⚠️ | 1 | — |

---

## Methodology

1. **Entity Source:** Loaded from the latest entity extraction cycle (2026-07-11T222116Z)
2. **Context Extraction:** For each entity, searched raw source article texts for sentences containing entity mentions
3. **Sentiment Scoring:** Applied VADER (Valence Aware Dictionary and sEntiment Reasoner) to each context snippet
4. **Score Mapping:** VADER compound scores (-1 to +1) mapped to 7-point Likert scale (-3 to +3):
   - +3: Very Positive (compound ≥ 0.6)
   - +2: Positive (compound ≥ 0.3)
   - +1: Slightly Positive (compound ≥ 0.1)
   - 0: Neutral (-0.1 < compound < 0.1)
   - -1: Slightly Negative (compound > -0.3)
   - -2: Negative (compound > -0.6)
   - -3: Very Negative (compound ≤ -0.6)
5. **Anomaly Detection:** Z-score calculated using overall mean and standard deviation of raw compound scores
6. **Coalition Aggregation:** Entities mapped to coalitions via organization/figure affiliation mappings

---

*Report generated by OpenCLaw Sentiment Analysis Pipeline*
*VADER: Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.*

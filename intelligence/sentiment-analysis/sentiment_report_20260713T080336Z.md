# Sentiment Analysis Report

**Classification:** TLP:AMBER
**Report Timestamp:** 20260713T080336Z
**Extraction Source:** 2026-07-13T06:04:20.268680Z
**Source Collection:** 2026-07-13T001124Z_political_collection_25sources_OPERATIONAL.json
**Source Timestamp:** 2026-07-13T001124Z
**Analysis Method:** VADER Sentiment Analysis on source article context
**Score Range:** -3 (very negative) to +3 (very positive)
**Anomaly Threshold:** |z-score| > 2

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Entities Analyzed | 271 |
| Sources Processed | 23 |
| Sources with Content | 23 |
| Entities with Context | 240 |
| Entities without Context (fallback) | 31 |
| Overall Mean Sentiment | +0.059 |
| Overall Std Deviation | 1.326 |
| Overall Median Sentiment | +0.000 |
| Sentiment Range | [-3, +3] |
| Positive Entities | 77 |
| Neutral Entities | 140 |
| Negative Entities | 54 |
| Anomalies Detected | 30 |

### Sentiment Distribution

```
Positive (77)  █████████████████████████████████████████████████████████████████████████████
Neutral  (140)  ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
Negative (54)  ██████████████████████████████████████████████████████
```

---

## Coalition / Party Aggregate Sentiment

| Coalition | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range |
|-----------|:-:|------|:----------:|:-------:|:--------:|:-----:|
| INDEPENDENT | +0 | Neutral | 0.0923 | 0.1531 | 11 | [-0.106, 0.294] |
| PEJUANG | +0 | Neutral | 0.0881 | 0.0000 | 1 | [0.088, 0.088] |
| PN | +0 | Neutral | 0.0260 | 0.0998 | 12 | [-0.043, 0.340] |
| GPS | +0 | Neutral | 0.0139 | 0.3427 | 3 | [-0.322, 0.363] |
| PH | +0 | Neutral | 0.0106 | 0.0858 | 19 | [-0.182, 0.202] |
| GRS | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| BN | +0 | Neutral | -0.0144 | 0.2147 | 19 | [-0.735, 0.324] |
| BERSAMA | +0 | Neutral | -0.0705 | 0.0000 | 2 | [-0.070, -0.070] |
| ROYAL | -2 | Negative | -0.5306 | 0.3215 | 2 | [-0.758, -0.303] |

### Coalition Entities
- **INDEPENDENT** (+0, Neutral): Alyaa Alhadjri, B Nantha Kumar, Bridget Welsh, Felicia Poh, Hakim Danish, Massila Kamalrudin, Mohamad Armin, Paul Kiong Life, Qistina Nadia Dzulqarnain, Teow Chia Ling, Ts Dr Massila Kamalrudin
- **PEJUANG** (+0, Neutral): Pejuang
- **PN** (+0, Neutral): Muhammad Sanusi Md Nor, Muhyiddin, Muhyiddin Yassin, Muhyiddin Yassin's PN, Sanusi, Tan Sri Muhyiddin Yassin, Armada, BERSATU, Bersatu, PAS, PN, Perikatan Nasional
- **GPS** (+0, Neutral): Abang Johari, Fadillah, GPS
- **PH** (+0, Neutral): Amirudin Shaari, Amirudin Shari, Anthony Loke, Anthony Loke Siew Fook, Anwar, Datuk Seri Amirudin Shari, Dzulkefly Ahmad, Fahmi Fadzil, Maszlee Malik, Mat Sabu, Mohamad Sabu, Nga, Nurul Izzah, Syed Saddiq, AMANAH, DAP, MUDA, PH, Pakatan Harapan
- **GRS** (+0, Neutral): GRS
- **BN** (+0, Neutral): Abdul Razak, Ahmad Zahid, Ahmad Zahid Hamidi, Datuk Seri Ramlan Harun, Dr Ahmad Zahid Hamidi, Ginie Lim, Isham Ishak, Jalaluddin Alias, Onn Hafiz, Onn Hafiz Ghazi, Ramlan Harun, Samsolbari, Tun Abdul Razak, Zahid Hamidi, BN, Barisan Nasional, MCA, MIC, UMNO
- **BERSAMA** (+0, Neutral): BERSAMA, Bersama
- **ROYAL** (-2, Negative): His Majesty Sultan Ibrahim, Sultan Ibrahim

---

## Sentiment Anomalies (|z-score| > 2)

**30 anomalies detected.**

| # | Entity | Type | Score | Label | Z-Score | Direction | Coalition | Mentions |
|---|--------|------|:-----:|-------|:-------:|:---------:|-----------|:--------:|
| 1 | wake-up call | CONCEPT | -3 | Very Negative | -3.1275 | negative | N/A | 1 |
| 2 | Datuk Mohd Arifin Mohd Arif | PERSON | +3 | Very Positive | 2.9839 | positive | N/A | 1 |
| 3 | Mohd Arifin Mohd Arif | PERSON | +3 | Very Positive | 2.9839 | positive | N/A | 1 |
| 4 | Petronas | ORGANIZATION | +3 | Very Positive | 2.9151 | positive | N/A | 1 |
| 5 | Middle East | LOCATION | -3 | Very Negative | -2.7210 | negative | N/A | 2 |
| 6 | His Majesty Sultan Ibrahim | PERSON | -3 | Very Negative | -2.5405 | negative | ROYAL | 2 |
| 7 | Jalaluddin Alias | PERSON | -3 | Very Negative | -2.4658 | negative | BN | 1 |
| 8 | Inanam | LOCATION | -3 | Very Negative | -2.4658 | negative | N/A | 1 |
| 9 | Likas | LOCATION | -3 | Very Negative | -2.4658 | negative | N/A | 1 |
| 10 | Manggatal | LOCATION | -3 | Very Negative | -2.4658 | negative | N/A | 1 |
| 11 | SOBA 2025 | EVENT | -3 | Very Negative | -2.4658 | negative | N/A | 1 |
| 12 | subsidised diesel | CONCEPT | -3 | Very Negative | -2.4658 | negative | N/A | 1 |
| 13 | transport | CONCEPT | -3 | Very Negative | -2.4658 | negative | N/A | 1 |
| 14 | water supply | CONCEPT | -3 | Very Negative | -2.4658 | negative | N/A | 1 |
| 15 | Federal Govt | ORGANIZATION | +3 | Very Positive | 2.4245 | positive | N/A | 1 |
| 16 | grassroots | CONCEPT | +3 | Very Positive | 2.4245 | positive | N/A | 1 |
| 17 | abortion | CONCEPT | -3 | Very Negative | -2.3823 | negative | N/A | 1 |
| 18 | community pharmacies | CONCEPT | -3 | Very Negative | -2.3823 | negative | N/A | 1 |
| 19 | Malay Mail | ORGANIZATION | +3 | Very Positive | 2.2358 | positive | N/A | 1 |
| 20 | DVS | ORGANIZATION | +3 | Very Positive | 2.2047 | positive | N/A | 1 |
| 21 | joint military exercise | EVENT | +3 | Very Positive | 2.2047 | positive | N/A | 1 |
| 22 | KPKM | ORGANIZATION | -3 | Very Negative | -2.0845 | negative | N/A | 1 |
| 23 | budget cuts | CONCEPT | -3 | Very Negative | -2.0845 | negative | N/A | 1 |
| 24 | fertiliser price | CONCEPT | -3 | Very Negative | -2.0845 | negative | N/A | 1 |
| 25 | food subsidies | CONCEPT | -3 | Very Negative | -2.0845 | negative | N/A | 1 |
| 26 | harm reduction | CONCEPT | -3 | Very Negative | -2.0845 | negative | N/A | 1 |
| 27 | pork supply | CONCEPT | -3 | Very Negative | -2.0845 | negative | N/A | 1 |
| 28 | KWSP | ORGANIZATION | +3 | Very Positive | 2.0517 | positive | N/A | 3 |
| 29 | Banting | LOCATION | +3 | Very Positive | 2.0517 | positive | N/A | 3 |
| 30 | Sekinchan | LOCATION | +3 | Very Positive | 2.0222 | positive | N/A | 1 |

---

## Entity Sentiments by Type

### PERSON

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| Datuk Mohd Arifin Mohd Arif | +3 | Very Positive | 0.9287 | 2.9839 | ⚠️ | 1 | — |
| Mohd Arifin Mohd Arif | +3 | Very Positive | 0.9287 | 2.9839 | ⚠️ | 1 | — |
| Fadillah | +2 | Positive | 0.3634 | 1.1323 |  | 2 | GPS |
| Alyaa Alhadjri | +1 | Slightly Positive | 0.2944 | 0.9063 |  | 1 | INDEPENDENT |
| B Nantha Kumar | +1 | Slightly Positive | 0.2944 | 0.9063 |  | 1 | INDEPENDENT |
| Qistina Nadia Dzulqarnain | +1 | Slightly Positive | 0.2944 | 0.9063 |  | 1 | INDEPENDENT |
| Onn Hafiz Ghazi | +1 | Slightly Positive | 0.2636 | 0.8054 |  | 5 | BN |
| Felicia Poh | +1 | Slightly Positive | 0.2384 | 0.7229 |  | 2 | INDEPENDENT |
| Abdul | +1 | Slightly Positive | 0.2123 | 0.6374 |  | 3 | — |
| Mat Sabu | +1 | Slightly Positive | 0.2023 | 0.6046 |  | 1 | PH |
| Mohamad Sabu | +1 | Slightly Positive | 0.2023 | 0.6046 |  | 1 | PH |
| Samsolbari | +1 | Slightly Positive | 0.1589 | 0.4625 |  | 3 | BN |
| Bellingham | +1 | Slightly Positive | 0.1133 | 0.3131 |  | 3 | — |
| Datuk | +0 | Neutral | 0.0929 | 0.2463 |  | 10 | — |
| Maszlee Malik | +0 | Neutral | 0.0678 | 0.1641 |  | 4 | PH |
| Syed Saddiq | +0 | Neutral | 0.0340 | 0.0534 |  | 10 | PH |
| Ahmad Zahid | +0 | Neutral | 0.0141 | -0.0118 |  | 10 | BN |
| Abdul Razak | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | BN |
| Amirudin Shaari | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | PH |
| Amirudin Shari | +0 | Neutral | 0.0000 | -0.0580 |  | 2 | PH |
| Anthony Loke Siew Fook | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | PH |
| Anwar | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | PH |
| Bridget Welsh | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | INDEPENDENT |
| Datuk Seri Amirudin Shari | +0 | Neutral | 0.0000 | -0.0580 |  | 2 | PH |
| Datuk Seri Ramlan Harun | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | BN |
| Dzulkefly Ahmad | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | PH |
| Fahmi Fadzil | +0 | Neutral | 0.0000 | -0.0580 |  | 2 | PH |
| Ginie Lim | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | BN |
| Isham Ishak | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | BN |
| James Lee | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | — |
| Massila Kamalrudin | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | INDEPENDENT |
| Mohamad Armin | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | INDEPENDENT |
| Mohd Ghazali Sabari | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Mohd Taha | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Muhammad Sanusi Md Nor | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | PN |
| Muhyiddin | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | PN |
| Muhyiddin Yassin | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | PN |
| Muhyiddin Yassin's PN | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | PN |
| Nga | +0 | Neutral | 0.0000 | -0.0580 |  | 10 | PH |
| Nurul Izzah | +0 | Neutral | 0.0000 | -0.0580 |  | 2 | PH |
| Paul Kiong Life | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | INDEPENDENT |
| Ramlan Harun | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | BN |
| Sanusi | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | PN |
| Tan Sri | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Tan Sri Muhyiddin Yassin | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | PN |
| Teow Chia Ling | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | INDEPENDENT |
| Ts Dr Massila Kamalrudin | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | INDEPENDENT |
| Tun Abdul Razak | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | BN |
| Onn Hafiz | +0 | Neutral | -0.0010 | -0.0613 |  | 10 | BN |
| Tun | +0 | Neutral | -0.0417 | -0.1946 |  | 10 | — |
| Hakim Danish | -1 | Slightly Negative | -0.1061 | -0.4055 |  | 3 | INDEPENDENT |
| Ahmad Zahid Hamidi | -1 | Slightly Negative | -0.1172 | -0.4419 |  | 5 | BN |
| Zahid Hamidi | -1 | Slightly Negative | -0.1172 | -0.4419 |  | 5 | BN |
| Anthony Loke | -1 | Slightly Negative | -0.1821 | -0.6545 |  | 3 | PH |
| Dr Ahmad Zahid Hamidi | -1 | Slightly Negative | -0.1953 | -0.6977 |  | 3 | BN |
| Datuk Seri | -1 | Slightly Negative | -0.2837 | -0.9873 |  | 10 | — |
| Sultan Ibrahim | -2 | Negative | -0.3032 | -1.0511 |  | 5 | ROYAL |
| Abang Johari | -2 | Negative | -0.3216 | -1.1114 |  | 3 | GPS |
| Jalaluddin Alias | -3 | Very Negative | -0.7351 | -2.4658 | ⚠️ | 1 | BN |
| His Majesty Sultan Ibrahim | -3 | Very Negative | -0.7579 | -2.5405 | ⚠️ | 2 | ROYAL |

### ORGANIZATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| Petronas | +3 | Very Positive | 0.9077 | 2.9151 | ⚠️ | 1 | — |
| Federal Govt | +3 | Very Positive | 0.7579 | 2.4245 | ⚠️ | 1 | — |
| Malay Mail | +3 | Very Positive | 0.7003 | 2.2358 | ⚠️ | 1 | — |
| DVS | +3 | Very Positive | 0.6908 | 2.2047 | ⚠️ | 1 | — |
| KWSP | +3 | Very Positive | 0.6441 | 2.0517 | ⚠️ | 3 | — |
| DBKK | +2 | Positive | 0.5423 | 1.7183 |  | 1 | — |
| IDEAS | +2 | Positive | 0.4939 | 1.5597 |  | 1 | — |
| LRT | +2 | Positive | 0.4939 | 1.5597 |  | 1 | — |
| Armada | +2 | Positive | 0.3400 | 1.0556 |  | 1 | PN |
| MCA | +2 | Positive | 0.3235 | 1.0016 |  | 2 | BN |
| Malaysiakini | +1 | Slightly Positive | 0.2944 | 0.9063 |  | 1 | — |
| Prasarana | +1 | Slightly Positive | 0.2944 | 0.9063 |  | 1 | — |
| AirBorneo | +1 | Slightly Positive | 0.2401 | 0.7284 |  | 2 | — |
| SPR | +1 | Slightly Positive | 0.2311 | 0.6989 |  | 7 | — |
| JKNS | +1 | Slightly Positive | 0.2023 | 0.6046 |  | 1 | — |
| Daily Express | +1 | Slightly Positive | 0.1519 | 0.4395 |  | 3 | — |
| Bernama | +1 | Slightly Positive | 0.1388 | 0.3966 |  | 10 | — |
| MIC | +1 | Slightly Positive | 0.1316 | 0.3730 |  | 10 | BN |
| MalaysiaGazette | +1 | Slightly Positive | 0.1101 | 0.3026 |  | 4 | — |
| Pejuang | +0 | Neutral | 0.0881 | 0.2306 |  | 5 | PEJUANG |
| MCMC | +0 | Neutral | 0.0864 | 0.2250 |  | 3 | — |
| The Edge Malaysia | +0 | Neutral | 0.0810 | 0.2073 |  | 3 | — |
| UMNO | +0 | Neutral | 0.0736 | 0.1831 |  | 4 | BN |
| ASEAN | +0 | Neutral | 0.0619 | 0.1447 |  | 8 | — |
| mStar | +0 | Neutral | 0.0514 | 0.1103 |  | 10 | — |
| AMANAH | +0 | Neutral | 0.0430 | 0.0828 |  | 4 | PH |
| EC | +0 | Neutral | 0.0411 | 0.0766 |  | 10 | — |
| MUDA | +0 | Neutral | 0.0170 | -0.0023 |  | 9 | PH |
| PN | +0 | Neutral | 0.0153 | -0.0079 |  | 10 | PN |
| MOH | +0 | Neutral | 0.0148 | -0.0095 |  | 10 | — |
| BERSATU | +0 | Neutral | 0.0000 | -0.0580 |  | 2 | PN |
| BN | +0 | Neutral | 0.0000 | -0.0580 |  | 10 | BN |
| Bersatu | +0 | Neutral | 0.0000 | -0.0580 |  | 2 | PN |
| Bursa Malaysia | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| DUN | +0 | Neutral | 0.0000 | -0.0580 |  | 10 | — |
| Dewan Rakyat | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Election Commission | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | — |
| FIFA | +0 | Neutral | 0.0000 | -0.0580 |  | 3 | — |
| GPS | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | GPS |
| GRS | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | GRS |
| Grab | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | — |
| HTAR Klang | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | — |
| KDN | +0 | Neutral | 0.0000 | -0.0580 |  | 3 | — |
| Kementerian Dalam Negeri | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Kosmo | +0 | Neutral | 0.0000 | -0.0580 |  | 4 | — |
| Media Mulia | +0 | Neutral | 0.0000 | -0.0580 |  | 3 | — |
| Perikatan Nasional | +0 | Neutral | 0.0000 | -0.0580 |  | 2 | PN |
| Sinar Harian | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| World of Buzz | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | — |
| NST | +0 | Neutral | -0.0260 | -0.1432 |  | 10 | — |
| PAS | +0 | Neutral | -0.0428 | -0.1982 |  | 10 | PN |
| Pakatan Harapan | +0 | Neutral | -0.0443 | -0.2031 |  | 10 | PH |
| DAP | +0 | Neutral | -0.0653 | -0.2719 |  | 10 | PH |
| BERSAMA | +0 | Neutral | -0.0705 | -0.2889 |  | 7 | BERSAMA |
| Bersama | +0 | Neutral | -0.0705 | -0.2889 |  | 7 | BERSAMA |
| Barisan Nasional | +0 | Neutral | -0.0735 | -0.2988 |  | 10 | BN |
| PH | +0 | Neutral | -0.0735 | -0.2988 |  | 10 | PH |
| BURSA | +0 | Neutral | -0.0954 | -0.3705 |  | 4 | — |
| TikTok | -1 | Slightly Negative | -0.1490 | -0.5461 |  | 9 | — |
| Apple | -1 | Slightly Negative | -0.1542 | -0.5631 |  | 4 | — |
| AFP | -1 | Slightly Negative | -0.1908 | -0.6830 |  | 4 | — |
| Boeing | -1 | Slightly Negative | -0.2156 | -0.7642 |  | 3 | — |
| Tropicana | -1 | Slightly Negative | -0.2541 | -0.8903 |  | 5 | — |
| Parliament | -2 | Negative | -0.3182 | -1.1003 |  | 1 | — |
| Spotify | -2 | Negative | -0.4139 | -1.4137 |  | 5 | — |
| SK hynix | -2 | Negative | -0.4559 | -1.5513 |  | 2 | — |
| OpenAI | -2 | Negative | -0.4606 | -1.5667 |  | 3 | — |
| KPKM | -3 | Very Negative | -0.6187 | -2.0845 | ⚠️ | 1 | — |

### LOCATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| Banting | +3 | Very Positive | 0.6441 | 2.0517 | ⚠️ | 3 | — |
| Sekinchan | +3 | Very Positive | 0.6351 | 2.0222 | ⚠️ | 1 | — |
| Japan | +2 | Positive | 0.5921 | 1.8814 |  | 2 | — |
| United States | +2 | Positive | 0.5413 | 1.7150 |  | 9 | — |
| Simpang Renggam | +2 | Positive | 0.4003 | 1.2532 |  | 1 | — |
| Kudat | +2 | Positive | 0.3790 | 1.1834 |  | 2 | — |
| France | +2 | Positive | 0.3400 | 1.0556 |  | 1 | — |
| Spain | +2 | Positive | 0.3400 | 1.0556 |  | 1 | — |
| Taiwan | +2 | Positive | 0.3250 | 1.0065 |  | 4 | — |
| Kota Kinabalu | +2 | Positive | 0.3186 | 0.9856 |  | 8 | — |
| Penang | +2 | Positive | 0.3125 | 0.9656 |  | 2 | — |
| Skudai | +1 | Slightly Positive | 0.2944 | 0.9063 |  | 1 | — |
| Sabah | +1 | Slightly Positive | 0.2886 | 0.8873 |  | 10 | — |
| Sandakan | +1 | Slightly Positive | 0.2767 | 0.8483 |  | 5 | — |
| Tawau | +1 | Slightly Positive | 0.2526 | 0.7694 |  | 3 | — |
| Myanmar | +1 | Slightly Positive | 0.2460 | 0.7478 |  | 5 | — |
| Machap | +1 | Slightly Positive | 0.2294 | 0.6934 |  | 4 | — |
| Kuching | +1 | Slightly Positive | 0.2234 | 0.6737 |  | 5 | — |
| West Asia | +1 | Slightly Positive | 0.2023 | 0.6046 |  | 1 | — |
| Putrajaya | +1 | Slightly Positive | 0.1881 | 0.5581 |  | 6 | — |
| Istana Pasir Pelangi | +1 | Slightly Positive | 0.1837 | 0.5437 |  | 6 | — |
| England | +1 | Slightly Positive | 0.1724 | 0.5067 |  | 8 | — |
| Kuala Lumpur | +1 | Slightly Positive | 0.1704 | 0.5001 |  | 10 | — |
| Terengganu | +1 | Slightly Positive | 0.1494 | 0.4313 |  | 7 | — |
| Sarawak | +1 | Slightly Positive | 0.1384 | 0.3953 |  | 10 | — |
| Argentina | +1 | Slightly Positive | 0.1298 | 0.3671 |  | 8 | — |
| Puteri Wangsa | +0 | Neutral | 0.0678 | 0.1641 |  | 4 | — |
| Strait of Hormuz | +0 | Neutral | 0.0575 | 0.1303 |  | 6 | — |
| Negeri Sembilan | +0 | Neutral | 0.0374 | 0.0645 |  | 10 | — |
| Permas | +0 | Neutral | 0.0321 | 0.0471 |  | 4 | — |
| Iran | +0 | Neutral | 0.0308 | 0.0429 |  | 10 | — |
| Johor | +0 | Neutral | 0.0271 | 0.0308 |  | 10 | — |
| Simpang Jeram | +0 | Neutral | 0.0257 | 0.0262 |  | 5 | — |
| Johor Bahru | +0 | Neutral | 0.0103 | -0.0243 |  | 5 | — |
| Batu Pahat | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Beluran | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Bintulu | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Bukit Naning | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Czech | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | — |
| Endau | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | — |
| Kedah | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Kelantan | +0 | Neutral | 0.0000 | -0.0580 |  | 2 | — |
| Kinta | +0 | Neutral | 0.0000 | -0.0580 |  | 2 | — |
| Kota Tinggi | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Kuala Selangor | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Kulai | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Melaka | +0 | Neutral | 0.0000 | -0.0580 |  | 4 | — |
| Mersing | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Miri | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Muar | +0 | Neutral | 0.0000 | -0.0580 |  | 4 | — |
| N14 | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | — |
| N41 | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | — |
| Norway | +0 | Neutral | 0.0000 | -0.0580 |  | 2 | — |
| Pahang | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Perlis | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Petaling Jaya | +0 | Neutral | 0.0000 | -0.0580 |  | 2 | — |
| Pontian | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Putatan | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Segamat | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Semporna | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Tambunan | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Tenom | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Russia | +0 | Neutral | -0.0416 | -0.1943 |  | 6 | — |
| Malaysia | +0 | Neutral | -0.0735 | -0.2988 |  | 10 | — |
| China | +0 | Neutral | -0.0865 | -0.3413 |  | 10 | — |
| Singapore | -1 | Slightly Negative | -0.1291 | -0.4809 |  | 10 | — |
| Selangor | -1 | Slightly Negative | -0.1299 | -0.4835 |  | 9 | — |
| Perak | -1 | Slightly Negative | -0.1336 | -0.4956 |  | 7 | — |
| Pasir Puteh | -1 | Slightly Negative | -0.2859 | -0.9945 |  | 2 | — |
| Indonesia | -2 | Negative | -0.3200 | -1.1062 |  | 6 | — |
| Bangladesh | -2 | Negative | -0.3516 | -1.2097 |  | 2 | — |
| Thailand | -2 | Negative | -0.3516 | -1.2097 |  | 2 | — |
| Lahad Datu | -2 | Negative | -0.3675 | -1.2617 |  | 2 | — |
| Penampang | -2 | Negative | -0.3675 | -1.2617 |  | 2 | — |
| Vietnam | -2 | Negative | -0.4559 | -1.5513 |  | 2 | — |
| Inanam | -3 | Very Negative | -0.7351 | -2.4658 | ⚠️ | 1 | — |
| Likas | -3 | Very Negative | -0.7351 | -2.4658 | ⚠️ | 1 | — |
| Manggatal | -3 | Very Negative | -0.7351 | -2.4658 | ⚠️ | 1 | — |
| Middle East | -3 | Very Negative | -0.8130 | -2.7210 | ⚠️ | 2 | — |

### EVENT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| joint military exercise | +3 | Very Positive | 0.6908 | 2.2047 | ⚠️ | 1 | — |
| campaign | +2 | Positive | 0.5265 | 1.6665 |  | 2 | — |
| 2026 Elections | +2 | Positive | 0.3890 | 1.2161 |  | 2 | — |
| Armada funds case | +2 | Positive | 0.3400 | 1.0556 |  | 1 | — |
| World Cup | +2 | Positive | 0.3070 | 0.9476 |  | 10 | — |
| Johor polls hot pan | +1 | Slightly Positive | 0.2944 | 0.9063 |  | 1 | — |
| Johor Polls | +1 | Slightly Positive | 0.2274 | 0.6868 |  | 10 | — |
| WAN IFRA ASIA MEDIA AWARDS 2025 | +1 | Slightly Positive | 0.1730 | 0.5086 |  | 0 | — |
| state visit | +1 | Slightly Positive | 0.1329 | 0.3773 |  | 7 | — |
| election | +0 | Neutral | 0.0831 | 0.2142 |  | 10 | — |
| Piala Dunia | +0 | Neutral | 0.0794 | 0.2021 |  | 8 | — |
| Johor State Election | +0 | Neutral | 0.0570 | 0.1287 |  | 5 | — |
| state election | +0 | Neutral | 0.0475 | 0.0976 |  | 6 | — |
| rally | +0 | Neutral | 0.0316 | 0.0455 |  | 3 | — |
| pilihan raya | +0 | Neutral | 0.0271 | 0.0308 |  | 10 | — |
| pilihan raya negeri | +0 | Neutral | 0.0271 | 0.0308 |  | 10 | — |
| Johor election | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| PRN Johor | +0 | Neutral | 0.0000 | -0.0580 |  | 10 | — |
| Pilihan Raya Negeri Johor | +0 | Neutral | 0.0000 | -0.0580 |  | 2 | — |
| ceramah | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | — |
| kempen | +0 | Neutral | 0.0000 | -0.0580 |  | 3 | — |
| majlis | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| quarter-final | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| Johor Polls 2026 | +0 | Neutral | -0.0352 | -0.1733 |  | 1 | — |
| Bersama loses deposits | +0 | Neutral | -0.0955 | -0.3708 |  | 0 | — |
| event | -1 | Slightly Negative | -0.1524 | -0.5572 |  | 10 | — |
| Typhoon Bavi | -1 | Slightly Negative | -0.2145 | -0.7606 |  | 7 | — |
| State Polls 2026 | -2 | Negative | -0.3773 | -1.2938 |  | 3 | — |
| SOBA 2025 | -3 | Very Negative | -0.7351 | -2.4658 | ⚠️ | 1 | — |

### CONCEPT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| grassroots | +3 | Very Positive | 0.7579 | 2.4245 | ⚠️ | 1 | — |
| digital transformation | +2 | Positive | 0.5381 | 1.7045 |  | 2 | — |
| renewable energy | +2 | Positive | 0.5287 | 1.6737 |  | 4 | — |
| cost of living | +2 | Positive | 0.4593 | 1.4464 |  | 2 | — |
| hot pan | +1 | Slightly Positive | 0.2944 | 0.9063 |  | 1 | — |
| turnout | +1 | Slightly Positive | 0.2944 | 0.9063 |  | 1 | — |
| copyright | +1 | Slightly Positive | 0.2907 | 0.8942 |  | 10 | — |
| doctor shortage | +1 | Slightly Positive | 0.2023 | 0.6046 |  | 1 | — |
| health insurance | +1 | Slightly Positive | 0.2023 | 0.6046 |  | 1 | — |
| state visit | +1 | Slightly Positive | 0.1329 | 0.3773 |  | 7 | — |
| AI | +0 | Neutral | 0.0440 | 0.0861 |  | 10 | — |
| MCA trumps DAP | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | — |
| Reformasi | +0 | Neutral | 0.0000 | -0.0580 |  | 2 | — |
| TVET | +0 | Neutral | 0.0000 | -0.0580 |  | 3 | — |
| deposits | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| perkauman | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| voter turnout | +0 | Neutral | 0.0000 | -0.0580 |  | 0 | — |
| wiped out | +0 | Neutral | 0.0000 | -0.0580 |  | 1 | — |
| artificial intelligence | +0 | Neutral | -0.0795 | -0.3184 |  | 2 | — |
| deals damage | -1 | Slightly Negative | -0.1482 | -0.5434 |  | 0 | — |
| constituency | -1 | Slightly Negative | -0.2023 | -0.7206 |  | 1 | — |
| emergency triage | -1 | Slightly Negative | -0.2536 | -0.8887 |  | 2 | — |
| MHIT | -1 | Slightly Negative | -0.2960 | -1.0276 |  | 1 | — |
| MediAsas | -1 | Slightly Negative | -0.2960 | -1.0276 |  | 1 | — |
| budget cuts | -3 | Very Negative | -0.6187 | -2.0845 | ⚠️ | 1 | — |
| fertiliser price | -3 | Very Negative | -0.6187 | -2.0845 | ⚠️ | 1 | — |
| food subsidies | -3 | Very Negative | -0.6187 | -2.0845 | ⚠️ | 1 | — |
| harm reduction | -3 | Very Negative | -0.6187 | -2.0845 | ⚠️ | 1 | — |
| pork supply | -3 | Very Negative | -0.6187 | -2.0845 | ⚠️ | 1 | — |
| abortion | -3 | Very Negative | -0.7096 | -2.3823 | ⚠️ | 1 | — |
| community pharmacies | -3 | Very Negative | -0.7096 | -2.3823 | ⚠️ | 1 | — |
| subsidised diesel | -3 | Very Negative | -0.7351 | -2.4658 | ⚠️ | 1 | — |
| transport | -3 | Very Negative | -0.7351 | -2.4658 | ⚠️ | 1 | — |
| water supply | -3 | Very Negative | -0.7351 | -2.4658 | ⚠️ | 1 | — |
| wake-up call | -3 | Very Negative | -0.9371 | -3.1275 | ⚠️ | 1 | — |

---

## Methodology

1. **Entity Source:** Loaded from the latest entity extraction cycle (2026-07-13T001124Z)
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

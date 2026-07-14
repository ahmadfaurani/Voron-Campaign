# Sentiment Analysis Report

**Classification:** TLP:AMBER
**Report Timestamp:** 20260714T080236Z
**Extraction Source:** 2026-07-14T06:03:16.716621Z
**Source Collection:** 2026-07-14T001151Z_political_collection_25sources_OPERATIONAL.json
**Source Timestamp:** 2026-07-14T001151Z
**Analysis Method:** VADER Sentiment Analysis on source article context
**Score Range:** -3 (very negative) to +3 (very positive)
**Anomaly Threshold:** |z-score| > 2

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Entities Analyzed | 269 |
| Sources Processed | 23 |
| Sources with Content | 23 |
| Entities with Context | 237 |
| Entities without Context (fallback) | 32 |
| Overall Mean Sentiment | +0.175 |
| Overall Std Deviation | 1.108 |
| Overall Median Sentiment | +0.000 |
| Sentiment Range | [-3, +3] |
| Positive Entities | 75 |
| Neutral Entities | 147 |
| Negative Entities | 47 |
| Anomalies Detected | 22 |

### Sentiment Distribution

```
Positive (75)  ███████████████████████████████████████████████████████████████████████████
Neutral  (147)  ███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
Negative (47)  ███████████████████████████████████████████████
```

---

## Coalition / Party Aggregate Sentiment

| Coalition | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range |
|-----------|:-:|------|:----------:|:-------:|:--------:|:-----:|
| ROYAL | +1 | Slightly Positive | 0.1986 | 0.0000 | 2 | [0.199, 0.199] |
| PN | +0 | Neutral | 0.0982 | 0.1731 | 6 | [-0.204, 0.267] |
| INDEPENDENT | +0 | Neutral | 0.0589 | 0.1317 | 5 | [0.000, 0.294] |
| PH | +0 | Neutral | 0.0383 | 0.1452 | 24 | [-0.281, 0.322] |
| BERSAMA | +0 | Neutral | 0.0294 | 0.0000 | 2 | [0.029, 0.029] |
| GPS | +0 | Neutral | 0.0000 | 0.0000 | 3 | [0.000, 0.000] |
| GRS | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| WARISAN | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] |
| BN | +0 | Neutral | -0.0779 | 0.1518 | 22 | [-0.421, 0.294] |

### Coalition Entities
- **ROYAL** (+1, Slightly Positive): His Majesty Sultan Ibrahim, Sultan Ibrahim
- **PN** (+0, Neutral): Muhyiddin, Armada, BERSATU, Bersatu, PAS, PN
- **INDEPENDENT** (+0, Neutral): B Nantha Kumar, Datuk Ts Dr Massila Kamalrudin, Massila Kamalrudin, Qistina Nadia Dzulqarnain, Ts Dr Massila Kamalrudin
- **PH** (+0, Neutral): Amirudin Shari, Anthony Loke, Anthony Loke Siew Fook, Anwar, Datuk Chan Foong Hin, Datuk Seri Amirudin Shari, Dzulkefly Ahmad, Loke, Mat Sabu, Mohamad Sabu, Nga, Nga Kor Ming, Nurul Izzah, Nurul Izzah Anwar, PM Anwar, Syed Saddiq, Syed Saddiq Syed Abdul Rahman, AMANAH, DAP, Keadilan, MUDA, PH, PKR, Pakatan Harapan
- **BERSAMA** (+0, Neutral): BERSAMA, Bersama
- **GPS** (+0, Neutral): Abang Johari, Tan Sri Abang Johari Openg, GPS
- **GRS** (+0, Neutral): GRS
- **WARISAN** (+0, Neutral): Shafie, WARISAN
- **BN** (+0, Neutral): Abdul Razak, Ahmad Zahid, Ahmad Zahid Hamidi, Datuk Onn Hafiz Ghazi, Datuk Seri Ahmad Zahid Hamidi, Datuk Seri Azalina Othman Said, Datuk Seri Dr Ahmad Zahid Hamidi, Datuk Seri Najib Razak, Dr Ahmad Zahid Hamidi, Isham Ishak, Najib, Najib Razak, Onn Hafiz, Onn Hafiz Ghazi, Tun Abdul Razak, Tun Sambanthan, Zahid Hamidi, BN, Barisan Nasional, MCA, MIC, UMNO

---

## Sentiment Anomalies (|z-score| > 2)

**22 anomalies detected.**

| # | Entity | Type | Score | Label | Z-Score | Direction | Coalition | Mentions |
|---|--------|------|:-----:|-------|:-------:|:---------:|-----------|:--------:|
| 1 | SK hynix | ORGANIZATION | +3 | Very Positive | 3.4645 | positive | N/A | 1 |
| 2 | renewable energy | CONCEPT | +3 | Very Positive | 3.4561 | positive | N/A | 1 |
| 3 | Court case | EVENT | +3 | Very Positive | 3.2915 | positive | N/A | 1 |
| 4 | Myanmar | LOCATION | +3 | Very Positive | 3.2316 | positive | N/A | 1 |
| 5 | N9 Polls | LOCATION | +3 | Very Positive | 3.2316 | positive | N/A | 1 |
| 6 | Apple | ORGANIZATION | +3 | Very Positive | 2.9137 | positive | N/A | 1 |
| 7 | KPKM | ORGANIZATION | -3 | Very Negative | -2.6418 | negative | N/A | 1 |
| 8 | budget cuts | CONCEPT | -3 | Very Negative | -2.6418 | negative | N/A | 1 |
| 9 | fertiliser price | CONCEPT | -3 | Very Negative | -2.6418 | negative | N/A | 1 |
| 10 | food subsidies | CONCEPT | -3 | Very Negative | -2.6418 | negative | N/A | 1 |
| 11 | pork supply | CONCEPT | -3 | Very Negative | -2.6418 | negative | N/A | 1 |
| 12 | DVS | ORGANIZATION | +3 | Very Positive | 2.6157 | positive | N/A | 1 |
| 13 | Banting | LOCATION | +3 | Very Positive | 2.4282 | positive | N/A | 3 |
| 14 | George Town | LOCATION | +3 | Very Positive | 2.3993 | positive | N/A | 1 |
| 15 | Taiwan | LOCATION | +3 | Very Positive | 2.3993 | positive | N/A | 1 |
| 16 | SOBA 2025 | EVENT | -2 | Negative | -2.3957 | negative | N/A | 1 |
| 17 | harm reduction | CONCEPT | +3 | Very Positive | 2.3512 | positive | N/A | 1 |
| 18 | MHIT | CONCEPT | -2 | Negative | -2.3351 | negative | N/A | 1 |
| 19 | MediAsas | CONCEPT | -2 | Negative | -2.3351 | negative | N/A | 1 |
| 20 | abortion | CONCEPT | -2 | Negative | -2.3351 | negative | N/A | 1 |
| 21 | community pharmacies | CONCEPT | -2 | Negative | -2.3351 | negative | N/A | 1 |
| 22 | DBKK | ORGANIZATION | +2 | Positive | 2.0195 | positive | N/A | 1 |

---

## Entity Sentiments by Type

### PERSON

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| Syed Saddiq | +2 | Positive | 0.3216 | 1.1334 |  | 10 | PH |
| PM Anwar | +2 | Positive | 0.3182 | 1.1198 |  | 2 | PH |
| Datuk Sadasivan | +1 | Slightly Positive | 0.2997 | 1.0455 |  | 2 | — |
| Qistina Nadia Dzulqarnain | +1 | Slightly Positive | 0.2944 | 1.0242 |  | 1 | INDEPENDENT |
| Loke | +1 | Slightly Positive | 0.2483 | 0.8391 |  | 5 | PH |
| Anthony Loke | +1 | Slightly Positive | 0.2367 | 0.7926 |  | 4 | PH |
| His Majesty Sultan Ibrahim | +1 | Slightly Positive | 0.1986 | 0.6396 |  | 2 | ROYAL |
| Sultan Ibrahim | +1 | Slightly Positive | 0.1986 | 0.6396 |  | 2 | ROYAL |
| Mat Sabu | +0 | Neutral | 0.0160 | -0.0935 |  | 1 | PH |
| Mohamad Sabu | +0 | Neutral | 0.0160 | -0.0935 |  | 1 | PH |
| Abang Johari | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | GPS |
| Abdul Razak | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | BN |
| Amirudin Shari | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | PH |
| Anthony Loke Siew Fook | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | PH |
| B Nantha Kumar | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | INDEPENDENT |
| Datuk Adif Zulkifli | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | — |
| Datuk Chan Foong Hin | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | PH |
| Datuk Onn Hafiz Ghazi | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | BN |
| Datuk Rubiah Haji Wang | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | — |
| Datuk Seri Ahmad Zahid Hamidi | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | BN |
| Datuk Seri Amirudin Shari | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | PH |
| Datuk Seri Azalina Othman Said | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | BN |
| Datuk Ts Dr Massila Kamalrudin | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | INDEPENDENT |
| Dzulkefly Ahmad | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | PH |
| Isham Ishak | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | BN |
| Massila Kamalrudin | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | INDEPENDENT |
| Mohd Ghazali Sabari | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Mohd Taha | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Nurul Izzah | +0 | Neutral | 0.0000 | -0.1578 |  | 2 | PH |
| Nurul Izzah Anwar | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | PH |
| Onn Hafiz Ghazi | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | BN |
| Shafie | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | WARISAN |
| Tan Sri Abang Johari Openg | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | GPS |
| Ts Dr Massila Kamalrudin | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | INDEPENDENT |
| Tun Abdul Razak | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | BN |
| Tun Sambanthan | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | BN |
| Ahmad Zahid | +0 | Neutral | -0.0207 | -0.2409 |  | 10 | BN |
| Anwar | +0 | Neutral | -0.0373 | -0.3075 |  | 7 | PH |
| Nga | -1 | Slightly Negative | -0.1055 | -0.5813 |  | 10 | PH |
| Najib | -1 | Slightly Negative | -0.1097 | -0.5982 |  | 5 | BN |
| Zahid Hamidi | -1 | Slightly Negative | -0.1405 | -0.7219 |  | 6 | BN |
| Onn Hafiz | -1 | Slightly Negative | -0.1529 | -0.7716 |  | 3 | BN |
| Ahmad Zahid Hamidi | -1 | Slightly Negative | -0.1686 | -0.8347 |  | 5 | BN |
| Datuk Seri Dr Ahmad Zahid Hamidi | -1 | Slightly Negative | -0.1686 | -0.8347 |  | 5 | BN |
| Dr Ahmad Zahid Hamidi | -1 | Slightly Negative | -0.1686 | -0.8347 |  | 5 | BN |
| Muhyiddin | -1 | Slightly Negative | -0.2040 | -0.9768 |  | 7 | PN |
| Syed Saddiq Syed Abdul Rahman | -1 | Slightly Negative | -0.2208 | -1.0443 |  | 6 | PH |
| Nga Kor Ming | -1 | Slightly Negative | -0.2810 | -1.2860 |  | 3 | PH |
| Datuk Seri Najib Razak | -2 | Negative | -0.4215 | -1.8501 |  | 2 | BN |
| Deputy Prime Minister | -2 | Negative | -0.4215 | -1.8501 |  | 2 | — |
| Najib Razak | -2 | Negative | -0.4215 | -1.8501 |  | 2 | BN |

### ORGANIZATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| SK hynix | +3 | Very Positive | 0.9022 | 3.4645 | ⚠️ | 1 | — |
| Apple | +3 | Very Positive | 0.7650 | 2.9137 | ⚠️ | 1 | — |
| DVS | +3 | Very Positive | 0.6908 | 2.6157 | ⚠️ | 1 | — |
| DBKK | +2 | Positive | 0.5423 | 2.0195 | ⚠️ | 1 | — |
| SPR | +2 | Positive | 0.3276 | 1.1575 |  | 3 | — |
| Daily Express | +2 | Positive | 0.3059 | 1.0704 |  | 3 | — |
| MCA | +1 | Slightly Positive | 0.2944 | 1.0242 |  | 1 | BN |
| Malaysiakini | +1 | Slightly Positive | 0.2944 | 1.0242 |  | 1 | — |
| Prasarana | +1 | Slightly Positive | 0.2944 | 1.0242 |  | 1 | — |
| BERSATU | +1 | Slightly Positive | 0.2666 | 0.9126 |  | 6 | PN |
| Bersatu | +1 | Slightly Positive | 0.2666 | 0.9126 |  | 6 | PN |
| Bernama | +1 | Slightly Positive | 0.2162 | 0.7103 |  | 10 | — |
| mStar | +1 | Slightly Positive | 0.1750 | 0.5448 |  | 10 | — |
| MCMC | +1 | Slightly Positive | 0.1685 | 0.5188 |  | 6 | — |
| PH | +1 | Slightly Positive | 0.1640 | 0.5007 |  | 10 | PH |
| MalaysiaGazette | +1 | Slightly Positive | 0.1468 | 0.4316 |  | 3 | — |
| DAP | +1 | Slightly Positive | 0.1343 | 0.3814 |  | 10 | PH |
| Kabinet | +1 | Slightly Positive | 0.1101 | 0.2843 |  | 4 | — |
| MUDA | +1 | Slightly Positive | 0.1085 | 0.2779 |  | 5 | PH |
| FIFA | +1 | Slightly Positive | 0.1027 | 0.2546 |  | 1 | — |
| PAS | +1 | Slightly Positive | 0.1024 | 0.2534 |  | 10 | PN |
| Armada | +1 | Slightly Positive | 0.1006 | 0.2461 |  | 5 | PN |
| Parliament | +0 | Neutral | 0.0626 | 0.0936 |  | 3 | — |
| PN | +0 | Neutral | 0.0567 | 0.0699 |  | 7 | PN |
| The Edge Malaysia | +0 | Neutral | 0.0552 | 0.0639 |  | 3 | — |
| DUN | +0 | Neutral | 0.0456 | 0.0253 |  | 10 | — |
| Kosmo | +0 | Neutral | 0.0342 | -0.0205 |  | 3 | — |
| BERSAMA | +0 | Neutral | 0.0294 | -0.0397 |  | 10 | BERSAMA |
| Bersama | +0 | Neutral | 0.0294 | -0.0397 |  | 10 | BERSAMA |
| ASEAN | +0 | Neutral | 0.0253 | -0.0562 |  | 4 | — |
| BURSA | +0 | Neutral | 0.0192 | -0.0807 |  | 6 | — |
| JKNS | +0 | Neutral | 0.0160 | -0.0935 |  | 1 | — |
| AFP | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | — |
| AMANAH | +0 | Neutral | 0.0000 | -0.1578 |  | 4 | PH |
| BN | +0 | Neutral | 0.0000 | -0.1578 |  | 10 | BN |
| BuzzKini | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | — |
| CodeBlue | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | — |
| Dewan Rakyat | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| FMT | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | — |
| GPS | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | GPS |
| GRS | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | GRS |
| Grab | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | — |
| HTAR Klang | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | — |
| Keadilan | +0 | Neutral | 0.0000 | -0.1578 |  | 2 | PH |
| MACC | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | — |
| Media Mulia | +0 | Neutral | 0.0000 | -0.1578 |  | 3 | — |
| PKR | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | PH |
| Pakatan Harapan | +0 | Neutral | 0.0000 | -0.1578 |  | 3 | PH |
| Petronas | +0 | Neutral | 0.0000 | -0.1578 |  | 4 | — |
| Sinar Harian | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| The Star | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| WARISAN | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | WARISAN |
| World of Buzz | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | — |
| Barisan Nasional | +0 | Neutral | -0.0028 | -0.1690 |  | 8 | BN |
| MOH | +0 | Neutral | -0.0253 | -0.2593 |  | 10 | — |
| MIC | +0 | Neutral | -0.0551 | -0.3790 |  | 10 | BN |
| Bursa Malaysia | +0 | Neutral | -0.0766 | -0.4653 |  | 4 | — |
| NST | +0 | Neutral | -0.0819 | -0.4866 |  | 10 | — |
| TikTok | -1 | Slightly Negative | -0.1363 | -0.7050 |  | 10 | — |
| LRT | -1 | Slightly Negative | -0.1574 | -0.7897 |  | 7 | — |
| UMNO | -1 | Slightly Negative | -0.1769 | -0.8680 |  | 10 | BN |
| Malay Mail | -1 | Slightly Negative | -0.2023 | -0.9700 |  | 1 | — |
| Vulcan Post | -1 | Slightly Negative | -0.2172 | -1.0298 |  | 4 | — |
| Tropicana | -1 | Slightly Negative | -0.2541 | -1.1780 |  | 5 | — |
| Spotify | -2 | Negative | -0.4139 | -1.8195 |  | 5 | — |
| KPKM | -3 | Very Negative | -0.6187 | -2.6418 | ⚠️ | 1 | — |

### LOCATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| Myanmar | +3 | Very Positive | 0.8442 | 3.2316 | ⚠️ | 1 | — |
| N9 Polls | +3 | Very Positive | 0.8442 | 3.2316 | ⚠️ | 1 | — |
| Banting | +3 | Very Positive | 0.6441 | 2.4282 | ⚠️ | 3 | — |
| George Town | +3 | Very Positive | 0.6369 | 2.3993 | ⚠️ | 1 | — |
| Taiwan | +3 | Very Positive | 0.6369 | 2.3993 | ⚠️ | 1 | — |
| United States | +2 | Positive | 0.4417 | 1.6156 |  | 10 | — |
| Sabah | +2 | Positive | 0.4353 | 1.5899 |  | 10 | — |
| Kota Kinabalu | +2 | Positive | 0.3178 | 1.1182 |  | 10 | — |
| Tawau | +2 | Positive | 0.3110 | 1.0909 |  | 3 | — |
| Argentina | +1 | Slightly Positive | 0.2550 | 0.8660 |  | 3 | — |
| Qatar | +1 | Slightly Positive | 0.2309 | 0.7693 |  | 3 | — |
| Sandakan | +1 | Slightly Positive | 0.1971 | 0.6336 |  | 3 | — |
| Penampang | +1 | Slightly Positive | 0.1916 | 0.6115 |  | 3 | — |
| Hamilton | +1 | Slightly Positive | 0.1591 | 0.4810 |  | 2 | — |
| Australia | +1 | Slightly Positive | 0.1582 | 0.4774 |  | 6 | — |
| Miri | +1 | Slightly Positive | 0.1480 | 0.4364 |  | 2 | — |
| China | +1 | Slightly Positive | 0.1212 | 0.3288 |  | 3 | — |
| India | +1 | Slightly Positive | 0.1185 | 0.3180 |  | 5 | — |
| Melaka | +1 | Slightly Positive | 0.1097 | 0.2827 |  | 10 | — |
| Saudi Arabia | +1 | Slightly Positive | 0.1010 | 0.2477 |  | 1 | — |
| Kuching | +0 | Neutral | 0.0987 | 0.2385 |  | 3 | — |
| KL | +0 | Neutral | 0.0918 | 0.2108 |  | 10 | — |
| France | +0 | Neutral | 0.0762 | 0.1482 |  | 5 | — |
| Sarawak | +0 | Neutral | 0.0597 | 0.0819 |  | 10 | — |
| Japan | +0 | Neutral | 0.0594 | 0.0807 |  | 3 | — |
| Strait of Hormuz | +0 | Neutral | 0.0420 | 0.0109 |  | 4 | — |
| Muar | +0 | Neutral | 0.0400 | 0.0028 |  | 10 | — |
| Kuala Lumpur | +0 | Neutral | 0.0387 | -0.0024 |  | 9 | — |
| Negeri Sembilan | +0 | Neutral | 0.0387 | -0.0024 |  | 10 | — |
| Iran | +0 | Neutral | 0.0282 | -0.0445 |  | 10 | — |
| Johor Bahru | +0 | Neutral | 0.0129 | -0.1060 |  | 4 | — |
| Istana Negara | +0 | Neutral | 0.0026 | -0.1473 |  | 6 | — |
| Bangladesh | +0 | Neutral | 0.0000 | -0.1578 |  | 3 | — |
| Batu Pahat | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Beluran | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Bintulu | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Boston | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | — |
| Bukit Naning | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Kedah | +0 | Neutral | 0.0000 | -0.1578 |  | 2 | — |
| Kota Tinggi | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Kuala Selangor | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Kudat | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Kulai | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Lahad Datu | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Machap | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Mersing | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| N14 | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | — |
| Norway | +0 | Neutral | 0.0000 | -0.1578 |  | 2 | — |
| Perlis | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Pontian | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Putatan | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Segamat | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Semporna | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Sibu | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Simpang Jeram | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Tambunan | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Tenom | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Terengganu | +0 | Neutral | 0.0000 | -0.1578 |  | 4 | — |
| Thailand | +0 | Neutral | 0.0000 | -0.1578 |  | 3 | — |
| England | +0 | Neutral | -0.0250 | -0.2581 |  | 5 | — |
| Johor | +0 | Neutral | -0.0287 | -0.2730 |  | 10 | — |
| Kelantan | +0 | Neutral | -0.0337 | -0.2931 |  | 6 | — |
| West Asia | +0 | Neutral | -0.0343 | -0.2955 |  | 4 | — |
| Ipoh | +0 | Neutral | -0.0513 | -0.3637 |  | 2 | — |
| Middle East | +0 | Neutral | -0.0665 | -0.4248 |  | 3 | — |
| Penang | +0 | Neutral | -0.0774 | -0.4685 |  | 10 | — |
| Putrajaya | +0 | Neutral | -0.0884 | -0.5127 |  | 7 | — |
| Selangor | +0 | Neutral | -0.0949 | -0.5388 |  | 10 | — |
| Negri Sembilan | +0 | Neutral | -0.0998 | -0.5585 |  | 2 | — |
| Spain | -1 | Slightly Negative | -0.1211 | -0.6440 |  | 4 | — |
| Shah Alam | -1 | Slightly Negative | -0.1224 | -0.6492 |  | 9 | — |
| Perak | -1 | Slightly Negative | -0.1768 | -0.8676 |  | 6 | — |
| Indonesia | -1 | Slightly Negative | -0.2237 | -1.0559 |  | 5 | — |
| Pahang | -1 | Slightly Negative | -0.2294 | -1.0788 |  | 2 | — |
| Inanam | -1 | Slightly Negative | -0.2732 | -1.2546 |  | 1 | — |
| Manggatal | -1 | Slightly Negative | -0.2732 | -1.2546 |  | 1 | — |
| Petaling Jaya | -1 | Slightly Negative | -0.2787 | -1.2767 |  | 2 | — |
| Singapore | -1 | Slightly Negative | -0.2868 | -1.3092 |  | 10 | — |

### EVENT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| Court case | +3 | Very Positive | 0.8591 | 3.2915 | ⚠️ | 1 | — |
| joint military exercise | +2 | Positive | 0.4753 | 1.7505 |  | 1 | — |
| campaign | +2 | Positive | 0.4192 | 1.5253 |  | 2 | — |
| Johor Polls | +2 | Positive | 0.3976 | 1.4386 |  | 4 | — |
| Appeal | +2 | Positive | 0.3747 | 1.3466 |  | 6 | — |
| Johor Polls 2026 | +2 | Positive | 0.3744 | 1.3454 |  | 1 | — |
| Bersama loses deposits | +1 | Slightly Positive | 0.2944 | 1.0242 |  | 1 | — |
| Hearing | +1 | Slightly Positive | 0.2645 | 0.9042 |  | 10 | — |
| World Cup | +1 | Slightly Positive | 0.2544 | 0.8636 |  | 9 | — |
| WAN IFRA ASIA MEDIA AWARDS 2025 | +1 | Slightly Positive | 0.1730 | 0.5368 |  | 0 | — |
| Probe | +1 | Slightly Positive | 0.1427 | 0.4152 |  | 4 | — |
| Typhoon Bavi | +1 | Slightly Positive | 0.1011 | 0.2481 |  | 2 | — |
| Piala Dunia | +0 | Neutral | 0.0931 | 0.2160 |  | 6 | — |
| PRN Negeri | +0 | Neutral | 0.0881 | 0.1960 |  | 5 | — |
| PRN JOHOR | +0 | Neutral | 0.0821 | 0.1719 |  | 10 | — |
| PRN Johor | +0 | Neutral | 0.0821 | 0.1719 |  | 10 | — |
| election | +0 | Neutral | 0.0665 | 0.1092 |  | 8 | — |
| rally | +0 | Neutral | 0.0316 | -0.0309 |  | 3 | — |
| Arrest | +0 | Neutral | 0.0000 | -0.1578 |  | 2 | — |
| Dewan Rakyat | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| GE16 | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | — |
| Johor State Election | +0 | Neutral | 0.0000 | -0.1578 |  | 2 | — |
| PRN nanti | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Pilihan Raya Negeri Johor | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| kempen | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| majlis | +0 | Neutral | 0.0000 | -0.1578 |  | 3 | — |
| pilihan raya | +0 | Neutral | 0.0000 | -0.1578 |  | 7 | — |
| pilihan raya negeri | +0 | Neutral | 0.0000 | -0.1578 |  | 6 | — |
| quarter-final | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| sidang akhbar | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | — |
| walkabout | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Investigation | +0 | Neutral | -0.0251 | -0.2585 |  | 8 | — |
| event | +0 | Neutral | -0.0291 | -0.2746 |  | 10 | — |
| state election | +0 | Neutral | -0.0333 | -0.2915 |  | 6 | — |
| State Polls 2026 | +0 | Neutral | -0.0665 | -0.4248 |  | 3 | — |
| state visit | +0 | Neutral | -0.0954 | -0.5408 |  | 4 | — |
| Trial | -1 | Slightly Negative | -0.1102 | -0.6002 |  | 10 | — |
| Charged | -1 | Slightly Negative | -0.2023 | -0.9700 |  | 1 | — |
| Federal Court | -1 | Slightly Negative | -0.2208 | -1.0443 |  | 6 | — |
| SOBA 2025 | -2 | Negative | -0.5574 | -2.3957 | ⚠️ | 1 | — |

### CONCEPT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| renewable energy | +3 | Very Positive | 0.9001 | 3.4561 | ⚠️ | 1 | — |
| harm reduction | +3 | Very Positive | 0.6249 | 2.3512 | ⚠️ | 1 | — |
| politics of hatred | +2 | Positive | 0.5123 | 1.8991 |  | 3 | — |
| wake-up call | +2 | Positive | 0.3818 | 1.3751 |  | 1 | — |
| copyright | +2 | Positive | 0.3798 | 1.3671 |  | 10 | — |
| AI | +2 | Positive | 0.3603 | 1.2888 |  | 10 | — |
| MCA trumps DAP | +1 | Slightly Positive | 0.2944 | 1.0242 |  | 1 | — |
| deals damage | +1 | Slightly Positive | 0.2944 | 1.0242 |  | 1 | — |
| deposits | +1 | Slightly Positive | 0.2944 | 1.0242 |  | 1 | — |
| wiped out | +1 | Slightly Positive | 0.2944 | 1.0242 |  | 1 | — |
| racism | +1 | Slightly Positive | 0.2470 | 0.8339 |  | 2 | — |
| Unity Government | +1 | Slightly Positive | 0.1147 | 0.3027 |  | 3 | — |
| unity government | +1 | Slightly Positive | 0.1147 | 0.3027 |  | 3 | — |
| BN Johor | +0 | Neutral | 0.0000 | -0.1578 |  | 5 | — |
| MADANI | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| Reformasi | +0 | Neutral | 0.0000 | -0.1578 |  | 3 | — |
| artificial intelligence | +0 | Neutral | 0.0000 | -0.1578 |  | 1 | — |
| perpaduan | +0 | Neutral | 0.0000 | -0.1578 |  | 3 | — |
| transport | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | — |
| turnout | +0 | Neutral | 0.0000 | -0.1578 |  | 0 | — |
| state visit | +0 | Neutral | -0.0954 | -0.5408 |  | 4 | — |
| Inflation | -1 | Slightly Negative | -0.1222 | -0.6484 |  | 2 | — |
| inflation | -1 | Slightly Negative | -0.1222 | -0.6484 |  | 2 | — |
| emergency triage | -1 | Slightly Negative | -0.2631 | -1.2141 |  | 2 | — |
| health insurance | -2 | Negative | -0.3094 | -1.4000 |  | 2 | — |
| water supply | -2 | Negative | -0.3660 | -1.6272 |  | 2 | — |
| MHIT | -2 | Negative | -0.5423 | -2.3351 | ⚠️ | 1 | — |
| MediAsas | -2 | Negative | -0.5423 | -2.3351 | ⚠️ | 1 | — |
| abortion | -2 | Negative | -0.5423 | -2.3351 | ⚠️ | 1 | — |
| community pharmacies | -2 | Negative | -0.5423 | -2.3351 | ⚠️ | 1 | — |
| budget cuts | -3 | Very Negative | -0.6187 | -2.6418 | ⚠️ | 1 | — |
| fertiliser price | -3 | Very Negative | -0.6187 | -2.6418 | ⚠️ | 1 | — |
| food subsidies | -3 | Very Negative | -0.6187 | -2.6418 | ⚠️ | 1 | — |
| pork supply | -3 | Very Negative | -0.6187 | -2.6418 | ⚠️ | 1 | — |

---

## Methodology

1. **Entity Source:** Loaded from the latest entity extraction cycle (2026-07-14T001151Z)
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

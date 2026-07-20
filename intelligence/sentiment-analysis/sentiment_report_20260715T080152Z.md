# Sentiment Analysis Report

**Classification:** TLP:AMBER
**Report Timestamp:** 20260715T080152Z
**Extraction Source:** 2026-07-15T06:02:04.093406Z
**Source Collection:** 2026-07-15T001252Z_political_collection_25sources_OPERATIONAL.json
**Source Timestamp:** 2026-07-15T001252Z
**Analysis Method:** VADER Sentiment Analysis on source article context
**Score Range:** -3 (very negative) to +3 (very positive)
**Anomaly Threshold:** |z-score| > 2

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Entities Analyzed | 251 |
| Sources Processed | 22 |
| Sources with Content | 22 |
| Entities with Context | 224 |
| Entities without Context (fallback) | 27 |
| Overall Mean Sentiment | +0.088 |
| Overall Std Deviation | 1.173 |
| Overall Median Sentiment | +0.000 |
| Sentiment Range | [-3, +3] |
| Positive Entities | 65 |
| Neutral Entities | 139 |
| Negative Entities | 47 |
| Anomalies Detected | 18 |

### Sentiment Distribution

```
Positive (65)  █████████████████████████████████████████████████████████████████
Neutral  (139)  ███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
Negative (47)  ███████████████████████████████████████████████
```

---

## Coalition / Party Aggregate Sentiment

| Coalition | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range |
|-----------|:-:|------|:----------:|:-------:|:--------:|:-----:|
| PN | +1 | Slightly Positive | 0.1789 | 0.2378 | 9 | [-0.276, 0.402] |
| BERSAMA | +0 | Neutral | 0.0602 | 0.0000 | 2 | [0.060, 0.060] |
| INDEPENDENT | +0 | Neutral | 0.0380 | 0.0537 | 2 | [0.000, 0.076] |
| PH | +0 | Neutral | 0.0370 | 0.2567 | 24 | [-0.848, 0.664] |
| GOVERNMENT | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| GRS | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| PEJUANG | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| ROYAL | +0 | Neutral | -0.0176 | 0.0000 | 1 | [-0.018, -0.018] |
| BN | +0 | Neutral | -0.0238 | 0.0633 | 19 | [-0.201, 0.042] |
| GPS | -1 | Slightly Negative | -0.2653 | 0.3619 | 3 | [-0.677, 0.000] |

### Coalition Entities
- **PN** (+1, Slightly Positive): Muhyiddin, Muhyiddin Yassin, Muhyiddin Yassin's, Tan Sri Muhyiddin Yassin, Armada, BERSATU, Bersatu, PAS, PN
- **BERSAMA** (+0, Neutral): BERSAMA, Bersama
- **INDEPENDENT** (+0, Neutral): B Nantha Kumar, Hakim Danish
- **PH** (+0, Neutral): Adam Adli, Amirudin Shari, Anthony Loke, Anthony Loke Siew Fook, Anwar, Anwar Ibrahim, Datuk Seri Amirudin Shari, Datuk Seri Anwar Ibrahim, Fahmi Fadzil, Hannah Yeoh, Mat Sabu, Nga, Nurul Izzah, Nurul Izzah Anwar, PM Anwar, Syed Saddiq, AMANAH, DAP, Keadilan, MUDA, PH, PKR, Pakatan Harapan, Parti Keadilan Rakyat
- **GOVERNMENT** (+0, Neutral): Shamsul Azri Abu Bakar
- **GRS** (+0, Neutral): GRS
- **PEJUANG** (+0, Neutral): Pejuang
- **ROYAL** (+0, Neutral): Sultan Ibrahim
- **BN** (+0, Neutral): Abdul Razak, Ahmad Zahid, Ahmad Zahid Hamidi, Azalina Othman Said, Datuk Seri Azalina Othman Said, Dr Ahmad Zahid Hamidi, Khaled Nordin, Mohamed Khaled Nordin, Onn Hafiz, Onn Hafiz Ghazi, Rosmah Mansor, Seri Rosmah Mansor, Tun Abdul Razak, Zahid Hamidi, BN, BN Johor, Barisan Nasional, MCA, UMNO
- **GPS** (-1, Slightly Negative): Michael Tiang, Tiong, GPS

---

## Sentiment Anomalies (|z-score| > 2)

**18 anomalies detected.**

| # | Entity | Type | Score | Label | Z-Score | Direction | Coalition | Mentions |
|---|--------|------|:-----:|-------|:-------:|:---------:|-----------|:--------:|
| 1 | renewable energy | CONCEPT | +3 | Very Positive | 3.4560 | positive | N/A | 1 |
| 2 | Adam Adli | PERSON | -3 | Very Negative | -3.4276 | negative | PH | 1 |
| 3 | Court case | EVENT | +3 | Very Positive | 3.2945 | positive | N/A | 1 |
| 4 | Taiwan | LOCATION | -3 | Very Negative | -3.1291 | negative | N/A | 1 |
| 5 | Michael Tiang | PERSON | -3 | Very Negative | -2.7580 | negative | GPS | 1 |
| 6 | Federal Government | ORGANIZATION | +3 | Very Positive | 2.7403 | positive | N/A | 1 |
| 7 | AFP | ORGANIZATION | -3 | Very Negative | -2.6442 | negative | N/A | 1 |
| 8 | Faisal | PERSON | -3 | Very Negative | -2.5910 | negative | N/A | 1 |
| 9 | Dewan Rakyat sitting | EVENT | -3 | Very Negative | -2.5910 | negative | N/A | 1 |
| 10 | seat allocation | CONCEPT | -3 | Very Negative | -2.5910 | negative | N/A | 1 |
| 11 | Inanam | LOCATION | -3 | Very Negative | -2.5508 | negative | N/A | 1 |
| 12 | water supply | CONCEPT | -3 | Very Negative | -2.5508 | negative | N/A | 1 |
| 13 | Fahmi Fadzil | PERSON | +3 | Very Positive | 2.5257 | positive | PH | 2 |
| 14 | King grants audience | EVENT | +3 | Very Positive | 2.5257 | positive | N/A | 2 |
| 15 | KWSP | ORGANIZATION | +3 | Very Positive | 2.4477 | positive | N/A | 3 |
| 16 | SOBA 2025 | EVENT | -2 | Negative | -2.2850 | negative | N/A | 1 |
| 17 | United States | LOCATION | +2 | Positive | 2.1018 | positive | N/A | 10 |
| 18 | DBKK | ORGANIZATION | +2 | Positive | 2.0467 | positive | N/A | 1 |

---

## Entity Sentiments by Type

### PERSON

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| Fahmi Fadzil | +3 | Very Positive | 0.6639 | 2.5257 | ⚠️ | 2 | PH |
| Muhyiddin Yassin | +2 | Positive | 0.4019 | 1.4937 |  | 1 | PN |
| Muhyiddin Yassin's | +2 | Positive | 0.4019 | 1.4937 |  | 1 | PN |
| Tan Sri Muhyiddin Yassin | +2 | Positive | 0.4019 | 1.4937 |  | 1 | PN |
| Tun | +2 | Positive | 0.3513 | 1.2943 |  | 10 | — |
| Anwar | +2 | Positive | 0.3333 | 1.2234 |  | 10 | PH |
| PM Anwar | +2 | Positive | 0.3017 | 1.0990 |  | 7 | PH |
| Zainudin | +1 | Slightly Positive | 0.2787 | 1.0084 |  | 4 | — |
| Anthony Loke | +1 | Slightly Positive | 0.2690 | 0.9702 |  | 9 | PH |
| Muhyiddin | +1 | Slightly Positive | 0.2185 | 0.7713 |  | 5 | PN |
| Tan Sri | +1 | Slightly Positive | 0.1340 | 0.4384 |  | 3 | — |
| Nga | +1 | Slightly Positive | 0.1308 | 0.4258 |  | 10 | PH |
| Hakim Danish | +0 | Neutral | 0.0760 | 0.2100 |  | 6 | INDEPENDENT |
| Syed Saddiq | +0 | Neutral | 0.0126 | -0.0398 |  | 10 | PH |
| Abdul Razak | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | BN |
| Adif Zulkifli | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | — |
| Ahmad Zahid | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | BN |
| Ahmad Zahid Hamidi | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | BN |
| Amirudin Shari | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | PH |
| Anthony Loke Siew Fook | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | PH |
| Azalina Othman Said | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | BN |
| B Nantha Kumar | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | INDEPENDENT |
| Datuk Adif Zulkifli | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | — |
| Datuk Seri Amirudin Shari | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | PH |
| Datuk Seri Azalina Othman Said | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | BN |
| Dr Ahmad Zahid Hamidi | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | BN |
| Hannah Yeoh | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | PH |
| Khaled Nordin | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | BN |
| Mat Sabu | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | PH |
| Mohamed Khaled Nordin | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | BN |
| Mohd Ghazali Sabari | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Mohd Taha | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Nurul Izzah | +0 | Neutral | 0.0000 | -0.0894 |  | 2 | PH |
| Nurul Izzah Anwar | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | PH |
| Onn Hafiz Ghazi | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | BN |
| Shamsul Azri Abu Bakar | +0 | Neutral | 0.0000 | -0.0894 |  | 2 | GOVERNMENT |
| Tun Abdul Razak | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | BN |
| Zahid Hamidi | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | BN |
| Sultan Ibrahim | +0 | Neutral | -0.0176 | -0.1587 |  | 8 | ROYAL |
| Rosmah Mansor | +0 | Neutral | -0.0405 | -0.2489 |  | 5 | BN |
| Datuk Seri Anwar Ibrahim | +0 | Neutral | -0.0645 | -0.3435 |  | 5 | PH |
| Seri Rosmah Mansor | +0 | Neutral | -0.0674 | -0.3549 |  | 3 | BN |
| Tiong | -1 | Slightly Negative | -0.1184 | -0.5558 |  | 5 | GPS |
| Datuk Seri | -1 | Slightly Negative | -0.1408 | -0.6440 |  | 9 | — |
| Datuk | -1 | Slightly Negative | -0.1628 | -0.7307 |  | 10 | — |
| Anwar Ibrahim | -1 | Slightly Negative | -0.1950 | -0.8575 |  | 6 | PH |
| Onn Hafiz | -1 | Slightly Negative | -0.2009 | -0.8807 |  | 2 | BN |
| Abdul Halim Aman | -2 | Negative | -0.4723 | -1.9498 |  | 2 | — |
| Faisal | -3 | Very Negative | -0.6351 | -2.5910 | ⚠️ | 1 | — |
| Michael Tiang | -3 | Very Negative | -0.6775 | -2.7580 | ⚠️ | 1 | GPS |
| Adam Adli | -3 | Very Negative | -0.8475 | -3.4276 | ⚠️ | 1 | PH |

### ORGANIZATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| Federal Government | +3 | Very Positive | 0.7184 | 2.7403 | ⚠️ | 1 | — |
| KWSP | +3 | Very Positive | 0.6441 | 2.4477 | ⚠️ | 3 | — |
| DBKK | +2 | Positive | 0.5423 | 2.0467 | ⚠️ | 1 | — |
| AirBorneo | +2 | Positive | 0.4939 | 1.8560 |  | 1 | — |
| MalaysiaGazette | +2 | Positive | 0.3891 | 1.4432 |  | 2 | — |
| FIFA | +2 | Positive | 0.3454 | 1.2711 |  | 2 | — |
| Parliament | +2 | Positive | 0.3043 | 1.1092 |  | 3 | — |
| Petronas | +1 | Slightly Positive | 0.2859 | 1.0367 |  | 2 | — |
| KDN | +1 | Slightly Positive | 0.2572 | 0.9237 |  | 3 | — |
| BERSATU | +1 | Slightly Positive | 0.2340 | 0.8323 |  | 10 | PN |
| Bersatu | +1 | Slightly Positive | 0.2340 | 0.8323 |  | 10 | PN |
| Daily Express | +1 | Slightly Positive | 0.1887 | 0.6539 |  | 3 | — |
| Apple | +1 | Slightly Positive | 0.1816 | 0.6259 |  | 2 | — |
| The Edge Malaysia | +1 | Slightly Positive | 0.1806 | 0.6220 |  | 2 | — |
| Pakatan Harapan | +1 | Slightly Positive | 0.1499 | 0.5010 |  | 10 | PH |
| DAP | +1 | Slightly Positive | 0.1179 | 0.3750 |  | 10 | PH |
| mStar | +1 | Slightly Positive | 0.1091 | 0.3403 |  | 10 | — |
| PAS | +1 | Slightly Positive | 0.1034 | 0.3179 |  | 10 | PN |
| Bernama | +0 | Neutral | 0.0946 | 0.2832 |  | 10 | — |
| PH | +0 | Neutral | 0.0787 | 0.2206 |  | 10 | PH |
| BURSA | +0 | Neutral | 0.0722 | 0.1950 |  | 5 | — |
| BERSAMA | +0 | Neutral | 0.0602 | 0.1477 |  | 7 | BERSAMA |
| Bersama | +0 | Neutral | 0.0602 | 0.1477 |  | 7 | BERSAMA |
| SPR | +0 | Neutral | 0.0537 | 0.1221 |  | 7 | — |
| BN | +0 | Neutral | 0.0421 | 0.0764 |  | 10 | BN |
| PKR | +0 | Neutral | 0.0414 | 0.0737 |  | 4 | PH |
| BERSIH | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| BN Johor | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | BN |
| Barisan Nasional | +0 | Neutral | 0.0000 | -0.0894 |  | 6 | BN |
| Bursa Malaysia | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| GPS | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | GPS |
| GRS | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | GRS |
| Grab | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | — |
| Keadilan | +0 | Neutral | 0.0000 | -0.0894 |  | 10 | PH |
| Kosmo | +0 | Neutral | 0.0000 | -0.0894 |  | 3 | — |
| MCA | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | BN |
| MCMC | +0 | Neutral | 0.0000 | -0.0894 |  | 2 | — |
| MUDA | +0 | Neutral | 0.0000 | -0.0894 |  | 8 | PH |
| Parti Keadilan Rakyat | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | PH |
| Pejuang | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | PEJUANG |
| Prasarana | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| SK hynix | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | — |
| Sinar Harian | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| The Star | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| World of Buzz | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | — |
| DUN | +0 | Neutral | -0.0296 | -0.2060 |  | 10 | — |
| Dewan Rakyat | +0 | Neutral | -0.0356 | -0.2296 |  | 6 | — |
| Media Mulia | +0 | Neutral | -0.0510 | -0.2903 |  | 3 | — |
| AMANAH | -1 | Slightly Negative | -0.1054 | -0.5046 |  | 4 | PH |
| Armada | -1 | Slightly Negative | -0.1093 | -0.5199 |  | 5 | PN |
| MACC | -1 | Slightly Negative | -0.1378 | -0.6322 |  | 9 | — |
| Vulcan Post | -1 | Slightly Negative | -0.1738 | -0.7740 |  | 5 | — |
| ASEAN | -1 | Slightly Negative | -0.1827 | -0.8090 |  | 4 | — |
| UMNO | -1 | Slightly Negative | -0.1862 | -0.8228 |  | 4 | BN |
| Tropicana | -1 | Slightly Negative | -0.1914 | -0.8433 |  | 5 | — |
| OpenAI | -1 | Slightly Negative | -0.2009 | -0.8807 |  | 2 | — |
| NST | -1 | Slightly Negative | -0.2384 | -1.0284 |  | 10 | — |
| TikTok | -1 | Slightly Negative | -0.2415 | -1.0407 |  | 8 | — |
| PN | -1 | Slightly Negative | -0.2760 | -1.1765 |  | 5 | PN |
| Malay Mail | -1 | Slightly Negative | -0.2960 | -1.2553 |  | 1 | — |
| Malaysiakini | -2 | Negative | -0.3175 | -1.3400 |  | 2 | — |
| Spotify | -2 | Negative | -0.4243 | -1.7607 |  | 5 | — |
| AFP | -3 | Very Negative | -0.6486 | -2.6442 | ⚠️ | 1 | — |

### LOCATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| United States | +2 | Positive | 0.5563 | 2.1018 | ⚠️ | 10 | — |
| Negri Sembilan | +2 | Positive | 0.5106 | 1.9218 |  | 1 | — |
| Ipoh | +2 | Positive | 0.4467 | 1.6701 |  | 2 | — |
| Vietnam | +2 | Positive | 0.4215 | 1.5709 |  | 1 | — |
| Banting | +2 | Positive | 0.3777 | 1.3983 |  | 4 | — |
| Kuching | +2 | Positive | 0.3769 | 1.3952 |  | 3 | — |
| Tawau | +1 | Slightly Positive | 0.2607 | 0.9375 |  | 4 | — |
| N9 Polls | +1 | Slightly Positive | 0.2303 | 0.8177 |  | 3 | — |
| Kota Kinabalu | +1 | Slightly Positive | 0.1957 | 0.6814 |  | 9 | — |
| Sabah | +1 | Slightly Positive | 0.1945 | 0.6767 |  | 10 | — |
| Penang | +1 | Slightly Positive | 0.1779 | 0.6113 |  | 8 | — |
| France | +1 | Slightly Positive | 0.1607 | 0.5436 |  | 8 | — |
| Malaysia | +1 | Slightly Positive | 0.1607 | 0.5436 |  | 10 | — |
| Miri | +1 | Slightly Positive | 0.1592 | 0.5377 |  | 4 | — |
| Kelantan | +1 | Slightly Positive | 0.1356 | 0.4447 |  | 4 | — |
| Melaka | +1 | Slightly Positive | 0.1123 | 0.3529 |  | 10 | — |
| Qatar | +0 | Neutral | 0.0952 | 0.2856 |  | 4 | — |
| Kuala Lumpur | +0 | Neutral | 0.0911 | 0.2694 |  | 10 | — |
| Australia | +0 | Neutral | 0.0869 | 0.2529 |  | 5 | — |
| Selangor | +0 | Neutral | 0.0813 | 0.2308 |  | 10 | — |
| Sarawak | +0 | Neutral | 0.0686 | 0.1808 |  | 10 | — |
| Spain | +0 | Neutral | 0.0584 | 0.1406 |  | 9 | — |
| Wall Street | +0 | Neutral | 0.0567 | 0.1339 |  | 3 | — |
| Russia | +0 | Neutral | 0.0513 | 0.1127 |  | 2 | — |
| Negeri Sembilan | +0 | Neutral | 0.0421 | 0.0764 |  | 10 | — |
| Johor Bahru | +0 | Neutral | 0.0172 | -0.0217 |  | 3 | — |
| Saudi Arabia | +0 | Neutral | 0.0155 | -0.0284 |  | 4 | — |
| Johor | +0 | Neutral | 0.0120 | -0.0421 |  | 10 | — |
| Bangladesh | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Batu Pahat | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Beluran | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Bintulu | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Bukit Naning | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| George Town | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | — |
| Istanbul | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | — |
| Kedah | +0 | Neutral | 0.0000 | -0.0894 |  | 3 | — |
| Kuala Selangor | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Kudat | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Kulai | +0 | Neutral | 0.0000 | -0.0894 |  | 2 | — |
| Lahad Datu | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Mersing | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Muar | +0 | Neutral | 0.0000 | -0.0894 |  | 7 | — |
| N14 | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | — |
| Norway | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Pahang | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Pasir Puteh | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Perak | +0 | Neutral | 0.0000 | -0.0894 |  | 2 | — |
| Perlis | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Pontian | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Putatan | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Putrajaya | +0 | Neutral | 0.0000 | -0.0894 |  | 7 | — |
| Sandakan | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Segamat | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Semporna | +0 | Neutral | 0.0000 | -0.0894 |  | 2 | — |
| Tambunan | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Tenom | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Terengganu | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| West Asia | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Indonesia | +0 | Neutral | -0.0165 | -0.1544 |  | 5 | — |
| England | +0 | Neutral | -0.0181 | -0.1607 |  | 6 | — |
| Japan | +0 | Neutral | -0.0192 | -0.1650 |  | 4 | — |
| KL | +0 | Neutral | -0.0231 | -0.1804 |  | 10 | — |
| Iran | +0 | Neutral | -0.0419 | -0.2544 |  | 10 | — |
| Penampang | +0 | Neutral | -0.0437 | -0.2615 |  | 3 | — |
| China | +0 | Neutral | -0.0603 | -0.3269 |  | 6 | — |
| Argentina | -1 | Slightly Negative | -0.1588 | -0.7149 |  | 4 | — |
| Thailand | -1 | Slightly Negative | -0.1850 | -0.8181 |  | 7 | — |
| Petaling Jaya | -2 | Negative | -0.3131 | -1.3227 |  | 3 | — |
| Kota Tinggi | -2 | Negative | -0.3175 | -1.3400 |  | 2 | — |
| Middle East | -2 | Negative | -0.3291 | -1.3857 |  | 2 | — |
| Singapore | -2 | Negative | -0.3845 | -1.6039 |  | 10 | — |
| Inanam | -3 | Very Negative | -0.6249 | -2.5508 | ⚠️ | 1 | — |
| Taiwan | -3 | Very Negative | -0.7717 | -3.1291 | ⚠️ | 1 | — |

### EVENT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| Court case | +3 | Very Positive | 0.8591 | 3.2945 | ⚠️ | 1 | — |
| King grants audience | +3 | Very Positive | 0.6639 | 2.5257 | ⚠️ | 2 | — |
| joint military exercise | +2 | Positive | 0.4753 | 1.7828 |  | 1 | — |
| Hearing | +2 | Positive | 0.4239 | 1.5803 |  | 10 | — |
| 2026 Elections | +2 | Positive | 0.4182 | 1.5579 |  | 3 | — |
| campaign | +2 | Positive | 0.4007 | 1.4889 |  | 6 | — |
| Trial | +2 | Positive | 0.3288 | 1.2057 |  | 10 | — |
| Appeal | +1 | Slightly Positive | 0.2101 | 0.7382 |  | 6 | — |
| World Cup | +1 | Slightly Positive | 0.1745 | 0.5979 |  | 10 | — |
| WAN IFRA ASIA MEDIA AWARDS 2025 | +1 | Slightly Positive | 0.1730 | 0.5920 |  | 0 | — |
| PRN Negeri | +1 | Slightly Positive | 0.1530 | 0.5133 |  | 10 | — |
| majlis | +1 | Slightly Positive | 0.1122 | 0.3525 |  | 3 | — |
| PRN JOHOR | +0 | Neutral | 0.0843 | 0.2426 |  | 5 | — |
| PRN Johor | +0 | Neutral | 0.0843 | 0.2426 |  | 5 | — |
| Piala Dunia | +0 | Neutral | 0.0651 | 0.1670 |  | 7 | — |
| pilihan raya | +0 | Neutral | 0.0481 | 0.1001 |  | 7 | — |
| pilihan raya negeri | +0 | Neutral | 0.0481 | 0.1001 |  | 7 | — |
| rally | +0 | Neutral | 0.0237 | 0.0039 |  | 4 | — |
| Arrest | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Federal Court | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| PRN nanti | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| Pilihan Raya Negeri Johor | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| ceramah | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | — |
| lawatan rasmi | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | — |
| quarter-final | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | — |
| sidang akhbar | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | — |
| state election | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| state visit | +0 | Neutral | 0.0000 | -0.0894 |  | 6 | — |
| election | +0 | Neutral | -0.0277 | -0.1985 |  | 10 | — |
| Investigation | +0 | Neutral | -0.0287 | -0.2025 |  | 7 | — |
| event | +0 | Neutral | -0.0610 | -0.3297 |  | 10 | — |
| kempen | -1 | Slightly Negative | -0.1211 | -0.5664 |  | 7 | — |
| Charged | -1 | Slightly Negative | -0.2023 | -0.8862 |  | 1 | — |
| Johor Polls | -1 | Slightly Negative | -0.2220 | -0.9638 |  | 4 | — |
| Typhoon Bavi | -1 | Slightly Negative | -0.2949 | -1.2510 |  | 3 | — |
| GE16 | -1 | Slightly Negative | -0.2975 | -1.2612 |  | 5 | — |
| Probe | -2 | Negative | -0.3125 | -1.3203 |  | 2 | — |
| State Polls 2026 | -2 | Negative | -0.3533 | -1.4810 |  | 3 | — |
| Johor election | -2 | Negative | -0.3675 | -1.5370 |  | 2 | — |
| walkabout | -2 | Negative | -0.4238 | -1.7587 |  | 2 | — |
| SOBA 2025 | -2 | Negative | -0.5574 | -2.2850 | ⚠️ | 1 | — |
| Dewan Rakyat sitting | -3 | Very Negative | -0.6351 | -2.5910 | ⚠️ | 1 | — |

### CONCEPT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|
| renewable energy | +3 | Very Positive | 0.9001 | 3.4560 | ⚠️ | 1 | — |
| wake-up call | +2 | Positive | 0.3818 | 1.4145 |  | 1 | — |
| final appeal | +2 | Positive | 0.3206 | 1.1734 |  | 2 | — |
| copyright | +1 | Slightly Positive | 0.2779 | 1.0052 |  | 10 | — |
| Inflation | +1 | Slightly Positive | 0.2658 | 0.9576 |  | 4 | — |
| inflation | +1 | Slightly Positive | 0.2658 | 0.9576 |  | 4 | — |
| MADANI | +1 | Slightly Positive | 0.2303 | 0.8177 |  | 3 | — |
| carbon tax | +0 | Neutral | 0.0468 | 0.0949 |  | 2 | — |
| mandate | +0 | Neutral | 0.0076 | -0.0595 |  | 8 | — |
| BN Johor | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | — |
| TVET | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| constituency | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | — |
| grassroots | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| racism | +0 | Neutral | 0.0000 | -0.0894 |  | 1 | — |
| state visit | +0 | Neutral | 0.0000 | -0.0894 |  | 6 | — |
| transport | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | — |
| turnout | +0 | Neutral | 0.0000 | -0.0894 |  | 0 | — |
| AI | +0 | Neutral | -0.0953 | -0.4648 |  | 10 | — |
| MediAsas | -2 | Negative | -0.4019 | -1.6725 |  | 1 | — |
| deposits | -2 | Negative | -0.4019 | -1.6725 |  | 1 | — |
| water supply | -3 | Very Negative | -0.6249 | -2.5508 | ⚠️ | 1 | — |
| seat allocation | -3 | Very Negative | -0.6351 | -2.5910 | ⚠️ | 1 | — |

---

## Methodology

1. **Entity Source:** Loaded from the latest entity extraction cycle (2026-07-15T001252Z)
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

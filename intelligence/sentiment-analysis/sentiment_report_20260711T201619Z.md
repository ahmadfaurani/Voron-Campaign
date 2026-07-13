# Sentiment Analysis Report

**Report Generated:** 20260711T201619Z
**Extraction Source:** 2026-07-11T20:14:12.815900Z
**Collection Timestamp:** 2026-07-11T182041Z
**Source Collection:** 2026-07-11T182041Z_political_collection_25sources_OPERATIONAL.json
**Sources Processed:** 24
**Analysis Method:** VADER Sentiment Analysis
**Score Range:** -3 (very negative) to +3 (very positive)
**Anomaly Threshold:** |z-score| > 2

---

## Summary

| Metric | Value |
|--------|-------|
| Total Entities Analyzed | 186 |
| Average Sentiment | 1 (0.2788) |
| Sentiment Std Dev | 0.4873 |
| Positive Entities | 135 |
| Neutral Entities | 27 |
| Negative Entities | 24 |
| Anomalies Detected | 13 |

---

## Coalition Sentiment Aggregates

| Coalition | Sentiment (-3 to +3) | Raw Score | Entity Count | Member Entities |
|-----------|----------------------|-----------|--------------|-----------------|
| BERSAMA | 1 | 0.3051 | 1 | BERSAMA |
| BN | 0 | 0.1001 | 4 | BN, Barisan Nasional, MCA, UMNO |
| GPS | 0 | 0.0000 | 1 | GPS |
| GRS | 0 | 0.0000 | 1 | GRS |
| MUDA | 0 | 0.0675 | 1 | MUDA |
| PEJUANG | 0 | 0.0000 | 1 | Pejuang |
| PH | 1 | 0.2623 | 4 | AMANAH, DAP, PH, Pakatan Harapan |
| PN | 0 | 0.1406 | 4 | BERSATU, Bersatu, PAS, PN |
| WARISAN | 2 | 0.8118 | 1 | WARISAN |

---

## Political Party Figure Aggregates

| Party | Sentiment (-3 to +3) | Raw Score | Figures Count | Figures |
|-------|----------------------|-----------|---------------|---------|
| BN | 1 | 0.3926 | 6 | Ahmad Zahid, Ahmad Zahid Hamidi, Datuk Zahari Sarip, Onn Hafiz, Onn Hafiz Ghazi, Zahid Hamidi |
| GPS | 2 | 0.7173 | 2 | Abang Johari, Wan Junaidi |
| INDEPENDENT | -2 | -0.5218 | 4 | Alyaa Alhadjri, B Nantha Kumar, Mustapha, Qistina Nadia Dzulqarnain |
| PH | 1 | 0.2898 | 11 | Anwar, Anwar Ibrahim, Datuk Seri Anwar Ibrahim, Fahmi Fadzil, Hakim Danish, Maszlee Malik, Mat Sabu, Mohamad Sabu, Nurul Izzah, Onn Abu Bakar, PM Anwar |
| PN | 1 | 0.3660 | 2 | Muhyiddin, Noraziah Mohd Razit |

---

## Sentiment Anomalies (|z-score| > 2)

| Entity | Z-Score | Sentiment | Type | Category |
|--------|---------|-----------|------|----------|
| Alyaa Alhadjri | -2.6141 | -3 | high_negative | PERSON |
| B Nantha Kumar | -2.6141 | -3 | high_negative | PERSON |
| Qistina Nadia Dzulqarnain | -2.6141 | -3 | high_negative | PERSON |
| KPKM | -2.5033 | -3 | high_negative | ORGANIZATION |
| abortion | -2.4674 | -3 | high_negative | CONCEPT |
| budget cuts | -2.5033 | -3 | high_negative | CONCEPT |
| community pharmacies | -2.4674 | -3 | high_negative | CONCEPT |
| fertiliser price | -2.5033 | -3 | high_negative | CONCEPT |
| food subsidies | -2.5033 | -3 | high_negative | CONCEPT |
| harm reduction | -2.5033 | -3 | high_negative | CONCEPT |
| politics of hatred | -2.6141 | -3 | high_negative | CONCEPT |
| pork supply | -2.5033 | -3 | high_negative | CONCEPT |
| racism | -2.6141 | -3 | high_negative | CONCEPT |

---

## Entity Sentiments by Type

### PERSON

| Entity | Sentiment | Label | Raw Score | Mentions | Z-Score | Anomaly |
|--------|-----------|-------|-----------|----------|---------|---------|
| Abang Johari | 3 | Very Positive | 0.9593 | 3 | 1.3963 |  |
| Hakim Danish | 3 | Very Positive | 0.8942 | 2 | 1.2626 |  |
| Mustapha | 3 | Very Positive | 0.8979 | 1 | 1.2703 |  |
| Ahmad Zahid | 2 | Positive | 0.5784 | 5 | 0.6147 |  |
| Datuk Zahari Sarip | 2 | Positive | 0.7320 | 1 | 0.9299 |  |
| Mat Sabu | 2 | Positive | 0.7208 | 1 | 0.9069 |  |
| Mohamad Sabu | 2 | Positive | 0.7208 | 1 | 0.9069 |  |
| Noraziah Mohd Razit | 2 | Positive | 0.7320 | 1 | 0.9299 |  |
| Ahmad Zahid Hamidi | 1 | Slightly Positive | 0.3313 | 3 | 0.1076 |  |
| Datuk | 1 | Slightly Positive | 0.1944 | 22 | -0.1733 |  |
| Datuk Seri Anwar Ibrahim | 1 | Slightly Positive | 0.1939 | 3 | -0.1744 |  |
| Onn Abu Bakar | 1 | Slightly Positive | 0.4969 | 2 | 0.4474 |  |
| Onn Hafiz | 1 | Slightly Positive | 0.2351 | 21 | -0.0897 |  |
| Onn Hafiz Ghazi | 1 | Slightly Positive | 0.2801 | 5 | 0.0026 |  |
| Tun | 1 | Slightly Positive | 0.3103 | 32 | 0.0644 |  |
| Wan Junaidi | 1 | Slightly Positive | 0.4753 | 1 | 0.4031 |  |
| Zahid Hamidi | 1 | Slightly Positive | 0.1988 | 5 | -0.1643 |  |
| Anwar | 0 | Neutral | 0.0810 | 24 | -0.4060 |  |
| Anwar Ibrahim | 0 | Neutral | 0.0727 | 8 | -0.4230 |  |
| Datuk Seri | 0 | Neutral | 0.1373 | 12 | -0.2905 |  |
| Fahmi Fadzil | 0 | Neutral | 0.0000 | 1 | -0.5722 |  |
| Maszlee Malik | 0 | Neutral | 0.0079 | 5 | -0.5559 |  |
| Muhyiddin | 0 | Neutral | 0.0000 | 1 | -0.5722 |  |
| Nurul Izzah | 0 | Neutral | 0.0000 | 2 | -0.5722 |  |
| PM Anwar | 0 | Neutral | 0.0000 | 3 | -0.5722 |  |
| Tan Sri | 0 | Neutral | 0.0000 | 1 | -0.5722 |  |
| Alyaa Alhadjri | -3 | Very Negative | -0.9951 | 1 | -2.6141 | ⚠️ |
| B Nantha Kumar | -3 | Very Negative | -0.9951 | 1 | -2.6141 | ⚠️ |
| Qistina Nadia Dzulqarnain | -3 | Very Negative | -0.9951 | 1 | -2.6141 | ⚠️ |

### ORGANIZATION

| Entity | Sentiment | Label | Raw Score | Mentions | Z-Score | Anomaly |
|--------|-----------|-------|-----------|----------|---------|---------|
| DVS | 3 | Very Positive | 0.9184 | 1 | 1.3124 |  |
| Election Commission | 3 | Very Positive | 0.9964 | 2 | 1.4723 |  |
| Petronas | 3 | Very Positive | 0.9874 | 1 | 1.4539 |  |
| AMANAH | 2 | Positive | 0.5961 | 3 | 0.6510 |  |
| Daily Express | 2 | Positive | 0.6552 | 2 | 0.7724 |  |
| JKNS | 2 | Positive | 0.7208 | 1 | 0.9069 |  |
| WARISAN | 2 | Positive | 0.8118 | 3 | 1.0937 |  |
| BERSAMA | 1 | Slightly Positive | 0.3051 | 25 | 0.0538 |  |
| BN | 1 | Slightly Positive | 0.2438 | 64 | -0.0718 |  |
| Barisan Nasional | 1 | Slightly Positive | 0.2956 | 12 | 0.0343 |  |
| Bernama | 1 | Slightly Positive | 0.1807 | 38 | -0.2014 |  |
| DAP | 1 | Slightly Positive | 0.1889 | 37 | -0.1845 |  |
| EC | 1 | Slightly Positive | 0.2237 | 356 | -0.1131 |  |
| FIFA | 1 | Slightly Positive | 0.2697 | 5 | -0.0187 |  |
| MOH | 1 | Slightly Positive | 0.2935 | 21 | 0.0301 |  |
| PAS | 1 | Slightly Positive | 0.2705 | 55 | -0.0172 |  |
| PH | 1 | Slightly Positive | 0.1844 | 113 | -0.1939 |  |
| PN | 1 | Slightly Positive | 0.1859 | 92 | -0.1908 |  |
| SK hynix | 1 | Slightly Positive | 0.4515 | 4 | 0.3542 |  |
| The Edge Malaysia | 1 | Slightly Positive | 0.3313 | 3 | 0.1076 |  |
| TikTok | 1 | Slightly Positive | 0.2279 | 14 | -0.1045 |  |
| ASEAN | 0 | Neutral | 0.1173 | 9 | -0.3314 |  |
| BERSATU | 0 | Neutral | 0.0530 | 15 | -0.4634 |  |
| BN Johor | 0 | Neutral | 0.0000 | 2 | -0.5722 |  |
| Bersatu | 0 | Neutral | 0.0530 | 15 | -0.4634 |  |
| GPS | 0 | Neutral | 0.0000 | 1 | -0.5722 |  |
| GRS | 0 | Neutral | 0.0000 | 1 | -0.5722 |  |
| Kosmo | 0 | Neutral | 0.0390 | 19 | -0.4922 |  |
| MACC | 0 | Neutral | -0.0433 | 2 | -0.6609 |  |
| MCA | 0 | Neutral | 0.0932 | 18 | -0.3810 |  |
| MUDA | 0 | Neutral | 0.0675 | 24 | -0.4337 |  |
| MalaysiaGazette | 0 | Neutral | 0.0136 | 39 | -0.5444 |  |
| Malaysiakini | 0 | Neutral | -0.0585 | 17 | -0.6923 |  |
| NST | 0 | Neutral | 0.0825 | 71 | -0.4028 |  |
| Pakatan Harapan | 0 | Neutral | 0.0796 | 9 | -0.4088 |  |
| Pejuang | 0 | Neutral | 0.0000 | 1 | -0.5722 |  |
| SPR | 0 | Neutral | 0.0773 | 25 | -0.4136 |  |
| Sinar Harian | 0 | Neutral | 0.1639 | 2 | -0.2359 |  |
| Suara Keadilan | 0 | Neutral | 0.0000 | 2 | -0.5722 |  |
| mStar | 0 | Neutral | 0.0830 | 62 | -0.4018 |  |
| AirBorneo | -1 | Slightly Negative | -0.4572 | 2 | -1.5104 |  |
| Spotify | -1 | Slightly Negative | -0.2424 | 10 | -1.0697 |  |
| Tropicana | -1 | Slightly Negative | -0.1789 | 9 | -0.9392 |  |
| UMNO | -1 | Slightly Negative | -0.2324 | 4 | -1.0490 |  |
| KPKM | -3 | Very Negative | -0.9411 | 1 | -2.5033 | ⚠️ |

### LOCATION

| Entity | Sentiment | Label | Raw Score | Mentions | Z-Score | Anomaly |
|--------|-----------|-------|-----------|----------|---------|---------|
| Bangladesh | 3 | Very Positive | 0.9155 | 2 | 1.3064 |  |
| Endau | 3 | Very Positive | 0.8372 | 1 | 1.1457 |  |
| Inanam | 3 | Very Positive | 0.9081 | 1 | 1.2912 |  |
| Kempas | 3 | Very Positive | 0.9731 | 1 | 1.4246 |  |
| Kota Kinabalu | 3 | Very Positive | 0.8487 | 6 | 1.1694 |  |
| Manggatal | 3 | Very Positive | 0.9081 | 1 | 1.2912 |  |
| Miri | 3 | Very Positive | 0.8619 | 2 | 1.1964 |  |
| Penang | 3 | Very Positive | 0.9725 | 2 | 1.4233 |  |
| Strait of Hormuz | 3 | Very Positive | 0.9938 | 1 | 1.4671 |  |
| Batu Pahat | 2 | Positive | 0.7249 | 1 | 0.9153 |  |
| Beluran | 2 | Positive | 0.7249 | 1 | 0.9153 |  |
| Bintulu | 2 | Positive | 0.7249 | 1 | 0.9153 |  |
| Buloh Kasap | 2 | Positive | 0.7846 | 2 | 1.0378 |  |
| Jementah | 2 | Positive | 0.7588 | 3 | 0.9849 |  |
| Kota Tinggi | 2 | Positive | 0.7249 | 1 | 0.9153 |  |
| Kuala Lumpur | 2 | Positive | 0.6410 | 17 | 0.7432 |  |
| Kuala Selangor | 2 | Positive | 0.7249 | 1 | 0.9153 |  |
| Kudat | 2 | Positive | 0.7249 | 1 | 0.9153 |  |
| Kulai | 2 | Positive | 0.7249 | 1 | 0.9153 |  |
| Lahad Datu | 2 | Positive | 0.8165 | 2 | 1.1033 |  |
| Likas | 2 | Positive | 0.6182 | 2 | 0.6963 |  |
| Melaka | 2 | Positive | 0.5755 | 4 | 0.6088 |  |
| Mersing | 2 | Positive | 0.7249 | 1 | 0.9153 |  |
| Negeri Sembilan | 2 | Positive | 0.6384 | 7 | 0.7378 |  |
| Penampang | 2 | Positive | 0.8078 | 4 | 1.0855 |  |
| Petaling Jaya | 2 | Positive | 0.6710 | 2 | 0.8047 |  |
| Pontian | 2 | Positive | 0.7249 | 1 | 0.9153 |  |
| Putatan | 2 | Positive | 0.7249 | 1 | 0.9153 |  |
| Putrajaya | 2 | Positive | 0.5207 | 3 | 0.4963 |  |
| Russia | 2 | Positive | 0.6306 | 3 | 0.7217 |  |
| Segamat | 2 | Positive | 0.7249 | 1 | 0.9153 |  |
| Semporna | 2 | Positive | 0.7249 | 1 | 0.9153 |  |
| Tambunan | 2 | Positive | 0.7249 | 1 | 0.9153 |  |
| Tenom | 2 | Positive | 0.7249 | 1 | 0.9153 |  |
| Terengganu | 2 | Positive | 0.8127 | 3 | 1.0954 |  |
| Thailand | 2 | Positive | 0.6323 | 3 | 0.7252 |  |
| United States | 2 | Positive | 0.5319 | 8 | 0.5192 |  |
| West Asia | 2 | Positive | 0.7208 | 1 | 0.9069 |  |
| Banting | 1 | Slightly Positive | 0.2145 | 9 | -0.1320 |  |
| Bukit Naning | 1 | Slightly Positive | 0.4982 | 3 | 0.4502 |  |
| France | 1 | Slightly Positive | 0.2102 | 5 | -0.1409 |  |
| Johor Bahru | 1 | Slightly Positive | 0.4478 | 5 | 0.3467 |  |
| Muar | 1 | Slightly Positive | 0.4155 | 3 | 0.2804 |  |
| Perak | 1 | Slightly Positive | 0.2771 | 3 | -0.0036 |  |
| Puteri Wangsa | 1 | Slightly Positive | 0.3284 | 12 | 0.1018 |  |
| Sabah | 1 | Slightly Positive | 0.3498 | 32 | 0.1456 |  |
| Sandakan | 1 | Slightly Positive | 0.2978 | 4 | 0.0389 |  |
| Sarawak | 1 | Slightly Positive | 0.1897 | 85 | -0.1828 |  |
| Selangor | 1 | Slightly Positive | 0.4156 | 4 | 0.2807 |  |
| Senggarang | 1 | Slightly Positive | 0.2485 | 4 | -0.0624 |  |
| Tiram | 1 | Slightly Positive | 0.3291 | 3 | 0.1030 |  |
| Iran | 0 | Neutral | 0.0917 | 18 | -0.3841 |  |
| Johor | 0 | Neutral | 0.1211 | 121 | -0.3237 |  |
| Kedah | 0 | Neutral | 0.0138 | 2 | -0.5439 |  |
| Kelantan | 0 | Neutral | -0.0602 | 4 | -0.6958 |  |
| Kuching | 0 | Neutral | -0.0115 | 5 | -0.5957 |  |
| Malaysia | 0 | Neutral | 0.1054 | 130 | -0.3559 |  |
| Morocco | 0 | Neutral | 0.0019 | 2 | -0.5683 |  |
| N01 | 0 | Neutral | 0.0000 | 1 | -0.5722 |  |
| N24 | 0 | Neutral | 0.0000 | 1 | -0.5722 |  |
| N41 | 0 | Neutral | 0.0000 | 1 | -0.5722 |  |
| Pahang | 0 | Neutral | 0.0337 | 5 | -0.5030 |  |
| Perlis | 0 | Neutral | 0.0998 | 4 | -0.3673 |  |
| Rengit | 0 | Neutral | 0.0000 | 1 | -0.5722 |  |
| Tawau | 0 | Neutral | 0.1555 | 4 | -0.2530 |  |
| Uzbekistan | 0 | Neutral | 0.0000 | 1 | -0.5722 |  |
| Singapore | -1 | Slightly Negative | -0.2322 | 41 | -1.0486 |  |

### EVENT

| Entity | Sentiment | Label | Raw Score | Mentions | Z-Score | Anomaly |
|--------|-----------|-------|-----------|----------|---------|---------|
| Johor Polls 2026 | 3 | Very Positive | 0.9872 | 1 | 1.4535 |  |
| quarter-final | 3 | Very Positive | 0.9821 | 3 | 1.4430 |  |
| Johor State Election | 2 | Positive | 0.6044 | 12 | 0.6680 |  |
| Johor election | 2 | Positive | 0.5763 | 10 | 0.6103 |  |
| state election | 2 | Positive | 0.6044 | 12 | 0.6680 |  |
| Johor Polls | 1 | Slightly Positive | 0.1823 | 23 | -0.1981 |  |
| Piala Dunia | 1 | Slightly Positive | 0.4409 | 8 | 0.3326 |  |
| SOBA 2025 | 1 | Slightly Positive | 0.4898 | 2 | 0.4329 |  |
| campaign | 1 | Slightly Positive | 0.4937 | 9 | 0.4409 |  |
| election | 1 | Slightly Positive | 0.2448 | 29 | -0.0700 |  |
| majlis | 1 | Slightly Positive | 0.2945 | 4 | 0.0321 |  |
| semi-finals | 1 | Slightly Positive | 0.4996 | 4 | 0.4530 |  |
| sidang akhbar | 1 | Slightly Positive | 0.1694 | 4 | -0.2246 |  |
| PRN Johor | 0 | Neutral | 0.1430 | 38 | -0.2788 |  |
| State Polls 2026 | 0 | Neutral | 0.0107 | 3 | -0.5503 |  |
| World Cup | 0 | Neutral | 0.1454 | 11 | -0.2738 |  |
| ceramah | 0 | Neutral | 0.0000 | 1 | -0.5722 |  |
| event | 0 | Neutral | -0.0569 | 14 | -0.6889 |  |
| kempen | 0 | Neutral | 0.1353 | 7 | -0.2946 |  |
| pilihan raya | 0 | Neutral | 0.0566 | 14 | -0.4560 |  |
| pilihan raya negeri | 0 | Neutral | 0.0566 | 14 | -0.4560 |  |
| rally | 0 | Neutral | 0.0316 | 3 | -0.5073 |  |

### CONCEPT

| Entity | Sentiment | Label | Raw Score | Mentions | Z-Score | Anomaly |
|--------|-----------|-------|-----------|----------|---------|---------|
| oil and gas | 3 | Very Positive | 0.9811 | 1 | 1.4410 |  |
| renewable energy | 3 | Very Positive | 0.9001 | 1 | 1.2748 |  |
| simple majority | 3 | Very Positive | 0.9975 | 2 | 1.4748 |  |
| subsidised diesel | 3 | Very Positive | 0.9086 | 1 | 1.2922 |  |
| water supply | 3 | Very Positive | 0.9081 | 1 | 1.2912 |  |
| doctor shortage | 2 | Positive | 0.7208 | 1 | 0.9069 |  |
| health insurance | 2 | Positive | 0.7208 | 1 | 0.9069 |  |
| MADANI | 1 | Slightly Positive | 0.4995 | 2 | 0.4527 |  |
| copyright | 1 | Slightly Positive | 0.3719 | 24 | 0.1910 |  |
| AI | 0 | Neutral | 0.1092 | 370 | -0.3482 |  |
| BN Johor | 0 | Neutral | 0.0000 | 2 | -0.5722 |  |
| Reformasi | 0 | Neutral | 0.0000 | 1 | -0.5722 |  |
| emergency triage | 0 | Neutral | -0.1014 | 2 | -0.7803 |  |
| MHIT | -2 | Negative | -0.5707 | 1 | -1.7433 |  |
| MediAsas | -2 | Negative | -0.5707 | 1 | -1.7433 |  |
| abortion | -3 | Very Negative | -0.9236 | 1 | -2.4674 | ⚠️ |
| budget cuts | -3 | Very Negative | -0.9411 | 1 | -2.5033 | ⚠️ |
| community pharmacies | -3 | Very Negative | -0.9236 | 1 | -2.4674 | ⚠️ |
| fertiliser price | -3 | Very Negative | -0.9411 | 1 | -2.5033 | ⚠️ |
| food subsidies | -3 | Very Negative | -0.9411 | 1 | -2.5033 | ⚠️ |
| harm reduction | -3 | Very Negative | -0.9411 | 1 | -2.5033 | ⚠️ |
| politics of hatred | -3 | Very Negative | -0.9951 | 1 | -2.6141 | ⚠️ |
| pork supply | -3 | Very Negative | -0.9411 | 1 | -2.5033 | ⚠️ |
| racism | -3 | Very Negative | -0.9951 | 1 | -2.6141 | ⚠️ |

---

## Political Figure Sentiments (with Party Affiliation)

| Figure | Sentiment | Raw Score | Mentions | Z-Score | Party | Anomaly |
|--------|-----------|-----------|----------|---------|-------|--------|
| Abang Johari | 3 | 0.9593 | 3 | 1.3963 | GPS |  |
| Hakim Danish | 3 | 0.8942 | 2 | 1.2626 | PH |  |
| Mustapha | 3 | 0.8979 | 1 | 1.2703 | INDEPENDENT |  |
| Ahmad Zahid | 2 | 0.5784 | 5 | 0.6147 | BN |  |
| Datuk Zahari Sarip | 2 | 0.7320 | 1 | 0.9299 | BN |  |
| Mat Sabu | 2 | 0.7208 | 1 | 0.9069 | PH |  |
| Mohamad Sabu | 2 | 0.7208 | 1 | 0.9069 | PH |  |
| Noraziah Mohd Razit | 2 | 0.7320 | 1 | 0.9299 | PN |  |
| Ahmad Zahid Hamidi | 1 | 0.3313 | 3 | 0.1076 | BN |  |
| Datuk Seri Anwar Ibrahim | 1 | 0.1939 | 3 | -0.1744 | PH |  |
| Onn Abu Bakar | 1 | 0.4969 | 2 | 0.4474 | PH |  |
| Onn Hafiz | 1 | 0.2351 | 21 | -0.0897 | BN |  |
| Onn Hafiz Ghazi | 1 | 0.2801 | 5 | 0.0026 | BN |  |
| Wan Junaidi | 1 | 0.4753 | 1 | 0.4031 | GPS |  |
| Zahid Hamidi | 1 | 0.1988 | 5 | -0.1643 | BN |  |
| Anwar | 0 | 0.0810 | 24 | -0.4060 | PH |  |
| Anwar Ibrahim | 0 | 0.0727 | 8 | -0.4230 | PH |  |
| Fahmi Fadzil | 0 | 0.0000 | 1 | -0.5722 | PH |  |
| Maszlee Malik | 0 | 0.0079 | 5 | -0.5559 | PH |  |
| Muhyiddin | 0 | 0.0000 | 1 | -0.5722 | PN |  |
| Nurul Izzah | 0 | 0.0000 | 2 | -0.5722 | PH |  |
| PM Anwar | 0 | 0.0000 | 3 | -0.5722 | PH |  |
| Alyaa Alhadjri | -3 | -0.9951 | 1 | -2.6141 | INDEPENDENT | ⚠️ |
| B Nantha Kumar | -3 | -0.9951 | 1 | -2.6141 | INDEPENDENT | ⚠️ |
| Qistina Nadia Dzulqarnain | -3 | -0.9951 | 1 | -2.6141 | INDEPENDENT | ⚠️ |

---
*Report generated by OpenCLaw Sentiment Analysis Pipeline*
*Classification: TLP:AMBER*

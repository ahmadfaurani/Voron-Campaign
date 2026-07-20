# Sentiment Analysis Report

**Report Generated:** 20260711T080219Z
**Extraction Source:** 2026-07-11T06:02:16.420793Z
**Collection Timestamp:** 2026-07-11T001148Z
**Source Collection:** 2026-07-11T001148Z_political_collection_25sources_OPERATIONAL.json
**Sources Processed:** 24
**Analysis Method:** VADER Sentiment Analysis
**Score Range:** -3 (very negative) to +3 (very positive)
**Anomaly Threshold:** z-score > 2 or < -2

---

## Summary

| Metric | Value |
|--------|-------|
| Total Entities Analyzed | 159 |
| Average Sentiment | 0 (0.0019) |
| Sentiment Std Dev | 0.2416 |
| Positive Entities | 49 |
| Neutral Entities | 75 |
| Negative Entities | 35 |
| Anomalies Detected | 12 |

---

## Coalition Sentiment Aggregates

| Coalition | Sentiment (-3 to +3) | Raw Score | Entity Count | Member Entities |
|-----------|----------------------|-----------|--------------|-----------------|
| BN | 0 | 0.0990 | 4 | BN, Barisan Nasional, MIC, UMNO |
| GPS | 0 | 0.0000 | 1 | GPS |
| GRS | 0 | 0.0000 | 1 | GRS |
| MUDA | 0 | 0.0000 | 1 | MUDA |
| PEJUANG | 0 | 0.0000 | 1 | Pejuang |
| PH | 0 | 0.0244 | 6 | AMANAH, BERSAMA, DAP, PH, PKR, Pakatan Harapan |
| PN | 0 | 0.0162 | 3 | Bersatu, PAS, PN |
| WARISAN | 0 | 0.0617 | 1 | WARISAN |

---

## Political Party Figure Aggregates

| Party | Sentiment (-3 to +3) | Raw Score | Figures Count | Figures |
|-------|----------------------|-----------|---------------|---------|
| BN | 0 | -0.0520 | 5 | Ahmad Zahid, Ismail Sabri, Najib Razak, Onn Hafiz, Zahid Hamidi |
| GPS | 0 | 0.1005 | 1 | Abang Johari |
| INDEPENDENT | 1 | 0.1806 | 1 | Mustapha |
| PH | 0 | 0.0375 | 12 | Anwar, Anwar Ibrahim, Datuk Seri Anwar Ibrahim, Hakim Danish, Mat Sabu, Mohamad, Mohamad Sabu, Nga, Nik Nazmi, PM Anwar, Saifuddin Nasution, Zainudin |
| PN | 0 | 0.0334 | 2 | Muhyiddin, Samsuri |

---

## Sentiment Anomalies (|z-score| > 2)

| Entity | Z-Score | Sentiment | Type | Category |
|--------|---------|-----------|------|----------|
| Mat Sabu | -2.4797 | -2 | high_negative | PERSON |
| Saifuddin Nasution | 2.2172 | 2 | high_positive | PERSON |
| DVS | 3.0581 | 2 | high_positive | ORGANIZATION |
| N17 exit plan | -2.4331 | -2 | high_negative | LOCATION |
| Penang | 2.1401 | 2 | high_positive | LOCATION |
| Petaling Jaya | -2.9419 | -2 | high_negative | LOCATION |
| West Asia | -2.7198 | -2 | high_negative | LOCATION |
| Pilihan Raya Negeri Johor | 2.1003 | 2 | high_positive | EVENT |
| abortion | -2.9060 | -2 | high_negative | CONCEPT |
| harm reduction | 2.0757 | 2 | high_positive | CONCEPT |
| politics of hatred | -3.4304 | -2 | high_negative | CONCEPT |
| racism | -2.5748 | -2 | high_negative | CONCEPT |

---

## Entity Sentiments by Type

### PERSON

| Entity | Sentiment | Raw Score | Mentions | Z-Score | Anomaly |
|--------|-----------|-----------|----------|---------|---------|
| Saifuddin Nasution | 2 | 0.5375 | 6 | 2.2172 | ⚠️ |
| Datuk Seri | 1 | 0.1747 | 23 | 0.7155 |  |
| Datuk Seri Anwar Ibrahim | 1 | 0.2386 | 13 | 0.9799 |  |
| Mustapha | 1 | 0.1806 | 2 | 0.7397 |  |
| Nik Nazmi | 1 | 0.3404 | 1 | 1.4012 |  |
| PM Anwar | 1 | 0.4714 | 4 | 1.9435 |  |
| Tan Sri | 1 | 0.4430 | 3 | 1.8260 |  |
| Abang Johari | 0 | 0.1005 | 4 | 0.4080 |  |
| Ahmad Zahid | 0 | 0.0000 | 3 | -0.0079 |  |
| Alyaa Alhadjri | 0 | 0.0000 | 3 | -0.0079 |  |
| Anwar | 0 | 0.0086 | 134 | 0.0277 |  |
| Anwar Ibrahim | 0 | 0.0953 | 25 | 0.3868 |  |
| Datuk | 0 | 0.1374 | 42 | 0.5610 |  |
| Hakim Danish | 0 | 0.0000 | 4 | -0.0079 |  |
| Mohamad | 0 | -0.1458 | 5 | -0.6113 |  |
| Muhyiddin | 0 | 0.0667 | 6 | 0.2683 |  |
| Najib Razak | 0 | 0.0000 | 1 | -0.0079 |  |
| Nga | 0 | -0.0218 | 442 | -0.0981 |  |
| Onn Hafiz | 0 | 0.0524 | 28 | 0.2089 |  |
| Samsuri | 0 | 0.0000 | 3 | -0.0079 |  |
| Tun | 0 | 0.0690 | 107 | 0.2776 |  |
| Zahid Hamidi | 0 | 0.0000 | 2 | -0.0079 |  |
| Zainudin | 0 | 0.0000 | 3 | -0.0079 |  |
| B Nantha Kumar | -1 | -0.1691 | 2 | -0.7078 |  |
| Ismail Sabri | -1 | -0.3126 | 4 | -1.3018 |  |
| Mohamad Sabu | -1 | -0.4767 | 2 | -1.9809 |  |
| Mat Sabu | -2 | -0.5972 | 2 | -2.4797 | ⚠️ |

### ORGANIZATION

| Entity | Sentiment | Raw Score | Mentions | Z-Score | Anomaly |
|--------|-----------|-----------|----------|---------|---------|
| DVS | 2 | 0.7407 | 2 | 3.0581 | ⚠️ |
| Federal Government | 1 | 0.3400 | 1 | 1.3995 |  |
| JKNS | 1 | 0.3579 | 2 | 1.4734 |  |
| Petronas | 1 | 0.3474 | 5 | 1.4300 |  |
| AMANAH | 0 | 0.0247 | 11 | 0.0943 |  |
| BERSAMA | 0 | -0.0556 | 10 | -0.2381 |  |
| BN | 0 | 0.0668 | 92 | 0.2685 |  |
| Barisan Nasional | 0 | 0.1396 | 6 | 0.5699 |  |
| Bernama | 0 | 0.0090 | 55 | 0.0295 |  |
| Bersatu | 0 | -0.0173 | 22 | -0.0794 |  |
| DAP | 0 | 0.0089 | 54 | 0.0290 |  |
| Daily Express | 0 | 0.0000 | 2 | -0.0079 |  |
| EC | 0 | 0.0838 | 892 | 0.3388 |  |
| FIFA | 0 | 0.0000 | 12 | -0.0079 |  |
| Federal Govt | 0 | 0.0000 | 1 | -0.0079 |  |
| France | 0 | 0.1204 | 22 | 0.4906 |  |
| GPS | 0 | 0.0000 | 1 | -0.0079 |  |
| GRS | 0 | 0.0000 | 1 | -0.0079 |  |
| KPKM | 0 | 0.0000 | 4 | -0.0079 |  |
| MACC | 0 | 0.1348 | 8 | 0.5503 |  |
| MIC | 0 | 0.1426 | 39 | 0.5825 |  |
| MOH | 0 | 0.0029 | 54 | 0.0042 |  |
| MUDA | 0 | 0.0000 | 30 | -0.0079 |  |
| Malaysiakini | 0 | -0.0200 | 141 | -0.0906 |  |
| Morocco | 0 | -0.1065 | 13 | -0.4489 |  |
| NST | 0 | -0.0476 | 105 | -0.2051 |  |
| PAS | 0 | 0.0345 | 182 | 0.1348 |  |
| PH | 0 | 0.0129 | 325 | 0.0456 |  |
| PKR | 0 | 0.0000 | 5 | -0.0079 |  |
| PN | 0 | 0.0313 | 197 | 0.1218 |  |
| Pakatan Harapan | 0 | 0.1554 | 8 | 0.6354 |  |
| Pejuang | 0 | 0.0000 | 1 | -0.0079 |  |
| SK hynix | 0 | -0.0140 | 16 | -0.0659 |  |
| SPR | 0 | -0.0253 | 67 | -0.1125 |  |
| Spotify | 0 | 0.0000 | 11 | -0.0079 |  |
| TikTok | 0 | -0.0280 | 32 | -0.1236 |  |
| Tropicana | 0 | -0.0129 | 12 | -0.0613 |  |
| UMNO | 0 | 0.0469 | 18 | 0.1863 |  |
| WARISAN | 0 | 0.0617 | 8 | 0.2477 |  |
| World Cup | 0 | 0.1426 | 36 | 0.5822 |  |
| Election Commission | -1 | -0.1842 | 5 | -0.7704 |  |
| Parliament | -1 | -0.3520 | 12 | -1.4648 |  |

### LOCATION

| Entity | Sentiment | Raw Score | Mentions | Z-Score | Anomaly |
|--------|-----------|-----------|----------|---------|---------|
| Penang | 2 | 0.5189 | 12 | 2.1401 | ⚠️ |
| Johor Bahru | 1 | 0.1787 | 7 | 0.7318 |  |
| Manggatal | 1 | 0.2202 | 2 | 0.9036 |  |
| Miri | 1 | 0.3712 | 2 | 1.5287 |  |
| United States | 1 | 0.4848 | 9 | 1.9989 |  |
| Banting | 0 | -0.0813 | 30 | -0.3445 |  |
| Bintulu | 0 | 0.0000 | 1 | -0.0079 |  |
| Bukit Naning | 0 | 0.0000 | 1 | -0.0079 |  |
| Endau | 0 | 0.0000 | 1 | -0.0079 |  |
| Inanam | 0 | 0.0193 | 2 | 0.0718 |  |
| Iran | 0 | -0.0962 | 74 | -0.4063 |  |
| Johor | 0 | 0.0492 | 376 | 0.1956 |  |
| Kedah | 0 | -0.1121 | 17 | -0.4718 |  |
| Kelantan | 0 | 0.0000 | 8 | -0.0079 |  |
| Kempas | 0 | 0.0000 | 4 | -0.0079 |  |
| Kuala Lumpur | 0 | -0.0387 | 30 | -0.1681 |  |
| Kuala Selangor | 0 | 0.0000 | 1 | -0.0079 |  |
| Kuching | 0 | 0.0279 | 11 | 0.1075 |  |
| Likas | 0 | 0.0000 | 3 | -0.0079 |  |
| Madinah | 0 | -0.1366 | 2 | -0.5733 |  |
| Malaysia | 0 | -0.0041 | 1069 | -0.0250 |  |
| Melaka | 0 | 0.0453 | 15 | 0.1798 |  |
| N14 Bukit Naning | 0 | 0.0000 | 1 | -0.0079 |  |
| N16 Sungai Balang | 0 | 0.0000 | 1 | -0.0079 |  |
| N32 Endau | 0 | 0.0000 | 1 | -0.0079 |  |
| N35 Pasir Raja | 0 | 0.0000 | 1 | -0.0079 |  |
| N47 Kempas | 0 | 0.0000 | 1 | -0.0079 |  |
| N47 Kempas dan N | 0 | 0.0000 | 1 | -0.0079 |  |
| Pahang | 0 | -0.0428 | 13 | -0.1850 |  |
| Penampang | 0 | 0.0980 | 9 | 0.3977 |  |
| Perak | 0 | 0.0040 | 12 | 0.0085 |  |
| Perlis | 0 | -0.0634 | 6 | -0.2702 |  |
| Putrajaya | 0 | 0.0897 | 8 | 0.3635 |  |
| Sabah | 0 | 0.0969 | 110 | 0.3934 |  |
| Sarawak | 0 | 0.0342 | 146 | 0.1338 |  |
| Selangor | 0 | 0.0416 | 9 | 0.1644 |  |
| Singapore | 0 | -0.1275 | 115 | -0.5358 |  |
| Sungai Balang | 0 | 0.0000 | 1 | -0.0079 |  |
| Tawau | 0 | 0.0000 | 4 | -0.0079 |  |
| Tenom | 0 | 0.0000 | 1 | -0.0079 |  |
| Terengganu | 0 | -0.1118 | 6 | -0.4704 |  |
| Thailand | 0 | 0.1492 | 25 | 0.6099 |  |
| Kota Kinabalu | -1 | -0.1687 | 12 | -0.7061 |  |
| Negeri Sembilan | -1 | -0.4763 | 10 | -1.9795 |  |
| Strait of Hormuz | -1 | -0.2253 | 15 | -0.9407 |  |
| N17 exit plan | -2 | -0.5859 | 1 | -2.4331 | ⚠️ |
| Petaling Jaya | -2 | -0.7088 | 11 | -2.9419 | ⚠️ |
| West Asia | -2 | -0.6552 | 3 | -2.7198 | ⚠️ |

### EVENT

| Entity | Sentiment | Raw Score | Mentions | Z-Score | Anomaly |
|--------|-----------|-----------|----------|---------|---------|
| Pilihan Raya Negeri Johor | 2 | 0.5093 | 1 | 2.1003 | ⚠️ |
| Johor State Election | 1 | 0.3694 | 9 | 1.5210 |  |
| ceramah | 1 | 0.1698 | 3 | 0.6949 |  |
| quarter-final | 1 | 0.3916 | 13 | 1.6132 |  |
| rally | 1 | 0.2670 | 6 | 1.0973 |  |
| Johor Polls | 0 | 0.0535 | 41 | 0.2138 |  |
| Johor Polls 2026 | 0 | 0.0000 | 2 | -0.0079 |  |
| PRN Johor | 0 | 0.0104 | 86 | 0.0353 |  |
| Piala Dunia | 0 | 0.0000 | 26 | -0.0079 |  |
| SOBA 2025 | 0 | 0.0000 | 2 | -0.0079 |  |
| State Polls 2026 | 0 | 0.0000 | 3 | -0.0079 |  |
| World Cup | 0 | 0.1426 | 36 | 0.5822 |  |
| campaign | 0 | -0.0000 | 53 | -0.0079 |  |
| election | 0 | 0.0592 | 50 | 0.2370 |  |
| event | 0 | 0.0225 | 29 | 0.0852 |  |
| kempen | 0 | 0.0198 | 49 | 0.0739 |  |
| majlis | 0 | 0.0000 | 6 | -0.0079 |  |
| pilihan raya | 0 | 0.0985 | 15 | 0.3998 |  |
| pilihan raya negeri | 0 | 0.1055 | 14 | 0.4290 |  |
| press conference | 0 | -0.0685 | 3 | -0.2914 |  |
| semi-finals | 0 | 0.0662 | 8 | 0.2662 |  |
| Johor election | -1 | -0.2261 | 6 | -0.9436 |  |

### CONCEPT

| Entity | Sentiment | Raw Score | Mentions | Z-Score | Anomaly |
|--------|-----------|-----------|----------|---------|---------|
| harm reduction | 2 | 0.5033 | 2 | 2.0757 | ⚠️ |
| copyright | 1 | 0.2017 | 26 | 0.8270 |  |
| oil and gas | 1 | 0.3818 | 1 | 1.5725 |  |
| AI | 0 | 0.0139 | 1626 | 0.0498 |  |
| MediAsas | 0 | -0.0020 | 3 | -0.0163 |  |
| fertiliser price | 0 | 0.0000 | 2 | -0.0079 |  |
| health insurance | 0 | 0.1521 | 2 | 0.6217 |  |
| pork supply | 0 | 0.0000 | 2 | -0.0079 |  |
| subsidised diesel | 0 | 0.0000 | 1 | -0.0079 |  |
| transport | 0 | -0.1002 | 9 | -0.4224 |  |
| unity government | 0 | 0.0000 | 1 | -0.0079 |  |
| MHIT | -1 | -0.2960 | 2 | -1.2331 |  |
| budget cuts | -1 | -0.4431 | 2 | -1.8420 |  |
| community pharmacies | -1 | -0.4688 | 2 | -1.9484 |  |
| doctor shortage | -1 | -0.3876 | 2 | -1.6123 |  |
| emergency triage | -1 | -0.3290 | 4 | -1.3695 |  |
| food subsidies | -1 | -0.4431 | 2 | -1.8420 |  |
| water supply | -1 | -0.3108 | 4 | -1.2944 |  |
| abortion | -2 | -0.7002 | 2 | -2.9060 | ⚠️ |
| politics of hatred | -2 | -0.8268 | 3 | -3.4304 | ⚠️ |
| racism | -2 | -0.6201 | 4 | -2.5748 | ⚠️ |

---

## Political Figure Sentiments (with Party Affiliation)

| Figure | Sentiment | Raw Score | Mentions | Z-Score | Party | Anomaly |
|--------|-----------|-----------|----------|---------|-------|---------|
| Saifuddin Nasution | 2 | 0.5375 | 6 | 2.2172 | PH | ⚠️ |
| Datuk Seri Anwar Ibrahim | 1 | 0.2386 | 13 | 0.9799 | PH |  |
| Mustapha | 1 | 0.1806 | 2 | 0.7397 | INDEPENDENT |  |
| Nik Nazmi | 1 | 0.3404 | 1 | 1.4012 | PH |  |
| PM Anwar | 1 | 0.4714 | 4 | 1.9435 | PH |  |
| Abang Johari | 0 | 0.1005 | 4 | 0.4080 | GPS |  |
| Ahmad Zahid | 0 | 0.0000 | 3 | -0.0079 | BN |  |
| Anwar | 0 | 0.0086 | 134 | 0.0277 | PH |  |
| Anwar Ibrahim | 0 | 0.0953 | 25 | 0.3868 | PH |  |
| Hakim Danish | 0 | 0.0000 | 4 | -0.0079 | PH |  |
| Mohamad | 0 | -0.1458 | 5 | -0.6113 | PH |  |
| Muhyiddin | 0 | 0.0667 | 6 | 0.2683 | PN |  |
| Najib Razak | 0 | 0.0000 | 1 | -0.0079 | BN |  |
| Nga | 0 | -0.0218 | 442 | -0.0981 | PH |  |
| Onn Hafiz | 0 | 0.0524 | 28 | 0.2089 | BN |  |
| Samsuri | 0 | 0.0000 | 3 | -0.0079 | PN |  |
| Zahid Hamidi | 0 | 0.0000 | 2 | -0.0079 | BN |  |
| Zainudin | 0 | 0.0000 | 3 | -0.0079 | PH |  |
| Ismail Sabri | -1 | -0.3126 | 4 | -1.3018 | BN |  |
| Mohamad Sabu | -1 | -0.4767 | 2 | -1.9809 | PH |  |
| Mat Sabu | -2 | -0.5972 | 2 | -2.4797 | PH | ⚠️ |

---
*Report generated by OpenCLaw Sentiment Analysis Pipeline*
*Classification: TLP:AMBER*

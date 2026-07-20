# Sentiment Analysis Report

**Classification:** TLP:AMBER
**Report Timestamp:** 20260718T080331Z
**Extraction ID:** ext_20260718_000553_phase1
**Extraction Source:** 2026-07-18T06:02:46Z
**Collection Cycle:** 2026-07-18T000553Z
**Source Count:** 24
**Analysis Method:** VADER Sentiment Analysis on fresh context snippets extracted from 2026-07-18 raw collection
**Score Range:** -3 (very negative) to +3 (very positive)
**Anomaly Threshold:** |z-score| > 2

> **Data-freshness note:** The 2026-07-18 extraction produced Phase-1 entity name lists
> only; Phase-2 per-entity context files were not regenerated for this cycle. To produce a
> genuine 2026-07-18 sentiment signal, context snippets were extracted directly from the
> 2026-07-18 raw source collection and scored with VADER. Coalition/party metadata sourced
> from the canonical per-entity files (2026-07-16 Phase-2 set) plus an analyst-extended
> affiliation map for newly-extracted figures.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Roster Entities (Phase-1 names) | 286 |
| Analysis Entities (merged) | 277 |
| Canonical Entities (from index) | 78 |
| New Entities (this cycle) | 199 |
| Roster Names Matched to Canonical | 67 |
| Sources Processed | 24 |
| Entities with Context | 257 |
| Entities without Context (fallback) | 20 |
| Overall Mean Sentiment | +0.166 |
| Overall Std Deviation | 1.022 |
| Overall Median Sentiment | +0.000 |
| Overall Raw Mean | 0.0330 |
| Overall Raw Std Dev | 0.2269 |
| Sentiment Range | [-3, +3] |
| Positive Entities | 68 |
| Neutral Entities | 171 |
| Negative Entities | 38 |
| Anomalies Detected | 22 |
| Coalitions Analyzed | 8 |
| Parties Analyzed | 13 |

### Sentiment Distribution

```
Positive (68)  ████████████████████████████████████████████████████████████████████
Neutral  (171)  ███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
Negative (38)  ██████████████████████████████████████
```

---

## Coalition Aggregate Sentiment

| Coalition | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range |
|-----------|:-:|------|:----------:|:-------:|:--------:|:-----:|
| BN | +1 | Slightly Positive | 0.1148 | 0.1963 | 12 | [-0.090, 0.505] |
| BERSAMA | +0 | Neutral | 0.0541 | 0.0000 | 1 | [0.054, 0.054] |
| GRS | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| PEJUANG | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] |
| WARISAN | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| PH | +0 | Neutral | -0.0122 | 0.1858 | 17 | [-0.598, 0.402] |
| PN | +0 | Neutral | -0.0730 | 0.3543 | 6 | [-0.778, 0.154] |
| GPS | -1 | Slightly Negative | -0.2083 | 0.3608 | 3 | [-0.625, 0.000] |

### Coalition Entities
- **BN** (+1, Slightly Positive): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Najib Razak, Datuk Tun Faisal Ismail Aziz, Onn Hafiz, Barisan Nasional, Malaysian Chinese Association, Malaysian Indian Congress, United Malays National Organisation
- **BERSAMA** (+0, Neutral): Parti Bersama
- **GRS** (+0, Neutral): GRS
- **PEJUANG** (+0, Neutral): Mahathir Mohamad, Pejuang
- **WARISAN** (+0, Neutral): Parti Warisan
- **PH** (+0, Neutral): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Anthony Loke, Mohamad Sabu, Maszlee, Fahmi Fadzil, Syed Saddiq, Tan See Leng, Democratic Action Party, Malaysia United Democratic Alliance, Pakatan Harapan, Parti Amanah Negara, Parti Keadilan Rakyat
- **PN** (+0, Neutral): Muhyiddin Yassin, Azanna Ahmad Kamar, Mas Ermieyati Samsudin, Parti Islam Se-Malaysia, Parti Pribumi Bersatu Malaysia, Perikatan Nasional
- **GPS** (-1, Slightly Negative): Sim Kui Hian, Tiong King Sing, Gabungan Parti Sarawak

---

## Party Aggregate Sentiment

| Party | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range | Coalition |
|-------|:-:|------|:----------:|:-------:|:--------:|:-----:|:---------:|
| MIC | +2 | Positive | 0.3225 | 0.0000 | 1 | [0.323, 0.323] | BN |
| UMNO | +1 | Slightly Positive | 0.1286 | 0.2003 | 9 | [-0.060, 0.505] | BN |
| PAS | +0 | Neutral | 0.0935 | 0.0000 | 1 | [0.093, 0.093] | PN |
| BERSAMA | +0 | Neutral | 0.0541 | 0.0000 | 1 | [0.054, 0.054] | BERSAMA |
| MUDA | +0 | Neutral | 0.0348 | 0.0493 | 2 | [0.000, 0.070] | PH |
| Pejuang | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | PEJUANG |
| Warisan | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | WARISAN |
| DAP | +0 | Neutral | -0.0056 | 0.0079 | 2 | [-0.011, 0.000] | PH |
| PKR | +0 | Neutral | -0.0167 | 0.2574 | 9 | [-0.598, 0.402] | PH |
| AMANAH | +0 | Neutral | -0.0327 | 0.0840 | 3 | [-0.128, 0.030] | PH |
| MCA | +0 | Neutral | -0.0903 | 0.0000 | 1 | [-0.090, -0.090] | BN |
| BERSATU | -1 | Slightly Negative | -0.1212 | 0.4435 | 4 | [-0.778, 0.154] | PN |
| GPS | -2 | Negative | -0.3125 | 0.4419 | 2 | [-0.625, 0.000] | GPS |

### Party Entities
- **MIC** (+2, Positive, → BN): Malaysian Indian Congress
- **UMNO** (+1, Slightly Positive, → BN): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Najib Razak, Datuk Tun Faisal Ismail Aziz, Onn Hafiz, United Malays National Organisation
- **PAS** (+0, Neutral, → PN): Parti Islam Se-Malaysia
- **BERSAMA** (+0, Neutral, → BERSAMA): Parti Bersama
- **MUDA** (+0, Neutral, → PH): Syed Saddiq, Malaysia United Democratic Alliance
- **Pejuang** (+0, Neutral, → PEJUANG): Mahathir Mohamad
- **Warisan** (+0, Neutral, → WARISAN): Parti Warisan
- **DAP** (+0, Neutral, → PH): Anthony Loke, Democratic Action Party
- **PKR** (+0, Neutral, → PH): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Fahmi Fadzil, Tan See Leng, Parti Keadilan Rakyat
- **AMANAH** (+0, Neutral, → PH): Mohamad Sabu, Maszlee, Parti Amanah Negara
- **MCA** (+0, Neutral, → BN): Malaysian Chinese Association
- **BERSATU** (-1, Slightly Negative, → PN): Muhyiddin Yassin, Azanna Ahmad Kamar, Mas Ermieyati Samsudin, Parti Pribumi Bersatu Malaysia
- **GPS** (-2, Negative, → GPS): Sim Kui Hian, Tiong King Sing

---

## Sentiment Anomalies (|z-score| > 2)

**22 anomalies detected.**

| # | Entity | Type | Score | Label | Z-Score | Direction | Coalition | Party | Contexts |
|---|--------|------|:-----:|-------|:-------:|:---------:|-----------|:------:|:--------:|
| 1 | WAN IFRA ASIA MEDIA AWARDS 2025 | EVENT | +3 | Very Positive | 3.8842 | positive | N/A | — | 1 |
| 2 | Azanna Ahmad Kamar | PERSON | -3 | Very Negative | -3.5762 | negative | PN | BERSATU | 4 |
| 3 | MRT | ORGANIZATION | +3 | Very Positive | 3.4588 | positive | N/A | — | 1 |
| 4 | PRS | ORGANIZATION | +3 | Very Positive | 3.2705 | positive | N/A | — | 2 |
| 5 | court case | EVENT | +3 | Very Positive | 3.2564 | positive | N/A | — | 1 |
| 6 | TNB | ORGANIZATION | +3 | Very Positive | 3.1502 | positive | N/A | — | 3 |
| 7 | renewable energy | CONCEPT | +3 | Very Positive | 2.9699 | positive | N/A | — | 2 |
| 8 | Tiong King Sing | PERSON | -3 | Very Negative | -2.9000 | negative | GPS | GPS | 1 |
| 9 | green technology | CONCEPT | +3 | Very Positive | 2.8103 | positive | N/A | — | 1 |
| 10 | Kinabatangan | LOCATION | -2 | Negative | -2.7876 | negative | N/A | — | 1 |
| 11 | Parti Keadilan Rakyat | ORGANIZATION | -2 | Negative | -2.7827 | negative | PH | PKR | 1 |
| 12 | Court of Appeal | EVENT | -2 | Negative | -2.7827 | negative | N/A | — | 1 |
| 13 | West Asia | LOCATION | -2 | Negative | -2.7699 | negative | N/A | — | 7 |
| 14 | Khatijah Abdullah | PERSON | +3 | Very Positive | 2.5974 | positive | N/A | — | 4 |
| 15 | United States | LOCATION | +3 | Very Positive | 2.5172 | positive | N/A | — | 7 |
| 16 | artificial intelligence | CONCEPT | +2 | Positive | 2.4907 | positive | N/A | — | 2 |
| 17 | Norway | LOCATION | -2 | Negative | -2.3657 | negative | N/A | — | 4 |
| 18 | Malay Mail | ORGANIZATION | -2 | Negative | -2.2961 | negative | N/A | — | 4 |
| 19 | deposits | CONCEPT | -2 | Negative | -2.1616 | negative | N/A | — | 1 |
| 20 | JPA | ORGANIZATION | +2 | Positive | 2.1064 | positive | N/A | — | 4 |
| 21 | Najib Razak | PERSON | +2 | Positive | 2.0804 | positive | BN | UMNO | 11 |
| 22 | Wall Street | LOCATION | -2 | Negative | -2.0201 | negative | N/A | — | 8 |

---

## Entity Sentiments by Type

### PERSON

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Khatijah Abdullah | +3 | Very Positive | 0.6222 | 2.5974 | ⚠️ | 4 | — | — | ✚ |
| Najib Razak | +2 | Positive | 0.5049 | 2.0804 | ⚠️ | 11 | BN | UMNO | ✚ |
| Tan See Leng | +2 | Positive | 0.4019 | 1.6263 |  | 3 | PH | PKR | ✚ |
| Ab Rauf Yusoh | +2 | Positive | 0.3213 | 1.2710 |  | 3 | BN | UMNO |  |
| Khairy Jamaluddin | +1 | Slightly Positive | 0.2553 | 0.9801 |  | 4 | BN | UMNO |  |
| Datuk Tun Faisal Ismail Aziz | +1 | Slightly Positive | 0.2003 | 0.7376 |  | 4 | BN | UMNO | ✚ |
| Muhyiddin Yassin | +1 | Slightly Positive | 0.1536 | 0.5318 |  | 27 | PN | BERSATU |  |
| Aminuddin Harun | +1 | Slightly Positive | 0.1002 | 0.2964 |  | 12 | PH | PKR |  |
| Syed Saddiq | +0 | Neutral | 0.0697 | 0.1619 |  | 20 | PH | MUDA | ✚ |
| Rajeentheran Suntheralingam | +0 | Neutral | 0.0478 | 0.0654 |  | 4 | — | — | ✚ |
| Hassan Abdul Karim | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | PH | PKR |  |
| Jalaluddin Abdul Rahman | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | BN | UMNO |  |
| Mahathir Mohamad | +0 | Neutral | 0.0000 | -0.1453 |  | 5 | PEJUANG | Pejuang |  |
| Mohamad Hasan | +0 | Neutral | 0.0000 | -0.1453 |  | 2 | BN | UMNO |  |
| Mohd Ghazali Sabari | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | — | — |  |
| Nik Nazmi Nik Ahmad | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | PH | PKR |  |
| Nurul Izzah Anwar | +0 | Neutral | 0.0000 | -0.1453 |  | 4 | PH | PKR |  |
| Rafizi Ramli | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | PH | PKR |  |
| Sim Kui Hian | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | GPS | GPS |  |
| Abdul Razak | +0 | Neutral | 0.0000 | -0.1453 |  | 2 | — | — | ✚ |
| Anthony Loke | +0 | Neutral | 0.0000 | -0.1453 |  | 2 | PH | DAP | ✚ |
| Jalaluddin Alias | +0 | Neutral | 0.0000 | -0.1453 |  | 2 | — | — | ✚ |
| Maszlee | +0 | Neutral | 0.0000 | -0.1453 |  | 4 | PH | AMANAH | ✚ |
| Fahmi Fadzil | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | PH | PKR | ✚ |
| Mas Ermieyati Samsudin | +0 | Neutral | 0.0000 | -0.1453 |  | 2 | PN | BERSATU | ✚ |
| Razak Exchange | +0 | Neutral | 0.0000 | -0.1453 |  | 2 | — | — | ✚ |
| Onn Hafiz | +0 | Neutral | -0.0179 | -0.2242 |  | 10 | BN | UMNO | ✚ |
| Ahmad Zahid Hamidi | +0 | Neutral | -0.0470 | -0.3525 |  | 13 | BN | UMNO |  |
| Anwar Ibrahim | +0 | Neutral | -0.0539 | -0.3829 |  | 26 | PH | PKR |  |
| Mohamad Sabu | -1 | Slightly Negative | -0.1281 | -0.7100 |  | 6 | PH | AMANAH | ✚ |
| B Nantha Kumar | -1 | Slightly Negative | -0.1759 | -0.9207 |  | 1 | — | — | ✚ |
| Tiong King Sing | -3 | Very Negative | -0.6249 | -2.9000 | ⚠️ | 1 | GPS | GPS |  |
| Azanna Ahmad Kamar | -3 | Very Negative | -0.7783 | -3.5762 | ⚠️ | 4 | PN | BERSATU | ✚ |

### ORGANIZATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| MRT | +3 | Very Positive | 0.8176 | 3.4588 | ⚠️ | 1 | — | — | ✚ |
| PRS | +3 | Very Positive | 0.7749 | 3.2705 | ⚠️ | 2 | — | — | ✚ |
| TNB | +3 | Very Positive | 0.7476 | 3.1502 | ⚠️ | 3 | — | — | ✚ |
| JPA | +2 | Positive | 0.5108 | 2.1064 | ⚠️ | 4 | — | — | ✚ |
| KWSP | +2 | Positive | 0.4627 | 1.8943 |  | 4 | — | — | ✚ |
| DBKK | +2 | Positive | 0.4019 | 1.6263 |  | 2 | — | — | ✚ |
| IHH | +2 | Positive | 0.3612 | 1.4469 |  | 1 | — | — | ✚ |
| Malaysian Indian Congress | +2 | Positive | 0.3225 | 1.2763 |  | 30 | BN | MIC |  |
| Bursa Malaysia | +2 | Positive | 0.3066 | 1.2062 |  | 6 | — | — | ✚ |
| NKF | +1 | Slightly Positive | 0.2470 | 0.9435 |  | 4 | — | — | ✚ |
| RCI | +1 | Slightly Positive | 0.2247 | 0.8452 |  | 15 | — | — | ✚ |
| JPJ | +1 | Slightly Positive | 0.1923 | 0.7024 |  | 12 | — | — | ✚ |
| BURSA | +1 | Slightly Positive | 0.1839 | 0.6653 |  | 10 | — | — | ✚ |
| Media Mulia | +1 | Slightly Positive | 0.1555 | 0.5401 |  | 6 | — | — | ✚ |
| KPJ | +1 | Slightly Positive | 0.1547 | 0.5366 |  | 4 | — | — | ✚ |
| ASEAN | +1 | Slightly Positive | 0.1448 | 0.4930 |  | 14 | — | — |  |
| Parti Pribumi Bersatu Malaysia | +1 | Slightly Positive | 0.1397 | 0.4705 |  | 30 | PN | BERSATU |  |
| Daily Express | +1 | Slightly Positive | 0.1357 | 0.4529 |  | 4 | — | — | ✚ |
| UN | +1 | Slightly Positive | 0.1300 | 0.4277 |  | 30 | — | — | ✚ |
| AFP | +1 | Slightly Positive | 0.1237 | 0.4000 |  | 19 | — | — | ✚ |
| The Star | +1 | Slightly Positive | 0.1027 | 0.3074 |  | 1 | — | — | ✚ |
| Apple | +1 | Slightly Positive | 0.1025 | 0.3065 |  | 11 | — | — | ✚ |
| Parti Islam Se-Malaysia | +0 | Neutral | 0.0935 | 0.2668 |  | 30 | PN | PAS |  |
| IPO | +0 | Neutral | 0.0929 | 0.2642 |  | 12 | — | — | ✚ |
| mStar | +0 | Neutral | 0.0886 | 0.2452 |  | 8 | — | — | ✚ |
| MOH | +0 | Neutral | 0.0809 | 0.2113 |  | 30 | — | — | ✚ |
| EU | +0 | Neutral | 0.0785 | 0.2007 |  | 23 | — | — | ✚ |
| MCMC | +0 | Neutral | 0.0748 | 0.1844 |  | 12 | — | — | ✚ |
| Parti Bersama | +0 | Neutral | 0.0541 | 0.0932 |  | 19 | BERSAMA | BERSAMA |  |
| PRN | +0 | Neutral | 0.0519 | 0.0835 |  | 30 | — | — | ✚ |
| Ministry of Finance | +0 | Neutral | 0.0339 | 0.0041 |  | 8 | — | — |  |
| State Government | +0 | Neutral | 0.0323 | -0.0029 |  | 4 | — | — | ✚ |
| Parti Amanah Negara | +0 | Neutral | 0.0300 | -0.0131 |  | 13 | PH | AMANAH |  |
| AirBorneo | +0 | Neutral | 0.0257 | -0.0320 |  | 4 | — | — | ✚ |
| Parliament | +0 | Neutral | 0.0199 | -0.0576 |  | 7 | — | — | ✚ |
| Google | +0 | Neutral | 0.0117 | -0.0937 |  | 15 | — | — | ✚ |
| PAC | +0 | Neutral | 0.0084 | -0.1083 |  | 30 | — | — | ✚ |
| Gabungan Parti Sarawak | +0 | Neutral | 0.0000 | -0.1453 |  | 4 | GPS | — |  |
| GRS | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | GRS | — |  |
| HAWANA | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | — | — |  |
| Malaysia United Democratic Alliance | +0 | Neutral | 0.0000 | -0.1453 |  | 15 | PH | MUDA |  |
| Ministry of Home Affairs | +0 | Neutral | 0.0000 | -0.1453 |  | 8 | — | — |  |
| Parti Warisan | +0 | Neutral | 0.0000 | -0.1453 |  | 2 | WARISAN | Warisan |  |
| Pejuang | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | PEJUANG | — |  |
| Suruhanjaya Pencegahan Rasuah Malaysia | +0 | Neutral | 0.0000 | -0.1453 |  | 8 | — | — |  |
| Armada | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| FMT | +0 | Neutral | 0.0000 | -0.1453 |  | 4 | — | — | ✚ |
| GLC | +0 | Neutral | 0.0000 | -0.1453 |  | 4 | — | — | ✚ |
| Harian Metro | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| IOI | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| KLK | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Kosmo | +0 | Neutral | 0.0000 | -0.1453 |  | 8 | — | — | ✚ |
| MalaysiaGazette | +0 | Neutral | 0.0000 | -0.1453 |  | 4 | — | — | ✚ |
| Malaysiakini | +0 | Neutral | 0.0000 | -0.1453 |  | 4 | — | — | ✚ |
| PBB | +0 | Neutral | 0.0000 | -0.1453 |  | 2 | — | — | ✚ |
| Perodua | +0 | Neutral | 0.0000 | -0.1453 |  | 2 | — | — | ✚ |
| PRU | +0 | Neutral | 0.0000 | -0.1453 |  | 8 | — | — | ✚ |
| Spotify | +0 | Neutral | 0.0000 | -0.1453 |  | 5 | — | — | ✚ |
| Vulcan Post | +0 | Neutral | 0.0000 | -0.1453 |  | 4 | — | — | ✚ |
| PDRM | +0 | Neutral | -0.0006 | -0.1480 |  | 3 | — | — | ✚ |
| Grab | +0 | Neutral | -0.0042 | -0.1638 |  | 7 | — | — | ✚ |
| DUN | +0 | Neutral | -0.0103 | -0.1907 |  | 30 | — | — | ✚ |
| Bernama | +0 | Neutral | -0.0105 | -0.1916 |  | 24 | — | — | ✚ |
| Democratic Action Party | +0 | Neutral | -0.0112 | -0.1947 |  | 30 | PH | DAP |  |
| Barisan Nasional | +0 | Neutral | -0.0117 | -0.1969 |  | 30 | BN | — |  |
| Pakatan Harapan | +0 | Neutral | -0.0181 | -0.2251 |  | 30 | PH | — |  |
| NST | +0 | Neutral | -0.0182 | -0.2255 |  | 30 | — | — | ✚ |
| NGO | +0 | Neutral | -0.0248 | -0.2546 |  | 30 | — | — | ✚ |
| IMU | +0 | Neutral | -0.0274 | -0.2661 |  | 12 | — | — | ✚ |
| Perikatan Nasional | +0 | Neutral | -0.0463 | -0.3494 |  | 30 | PN | — |  |
| United Malays National Organisation | +0 | Neutral | -0.0599 | -0.4094 |  | 19 | BN | UMNO |  |
| FIFA | +0 | Neutral | -0.0685 | -0.4473 |  | 26 | — | — | ✚ |
| Suruhanjaya Pilihan Raya | +0 | Neutral | -0.0739 | -0.4711 |  | 26 | — | — |  |
| Malaysian Chinese Association | +0 | Neutral | -0.0903 | -0.5434 |  | 13 | BN | MCA |  |
| The Edge Malaysia | -1 | Slightly Negative | -0.1133 | -0.6448 |  | 3 | — | — | ✚ |
| TikTok | -1 | Slightly Negative | -0.1169 | -0.6606 |  | 29 | — | — | ✚ |
| Sinar Harian | -1 | Slightly Negative | -0.1496 | -0.8048 |  | 4 | — | — | ✚ |
| Borneo Post | -1 | Slightly Negative | -0.2023 | -1.0371 |  | 1 | — | — | ✚ |
| World of Buzz | -1 | Slightly Negative | -0.2107 | -1.0741 |  | 2 | — | — | ✚ |
| CNA | -1 | Slightly Negative | -0.2260 | -1.1416 |  | 4 | — | — | ✚ |
| Cabinet | -2 | Negative | -0.3191 | -1.5520 |  | 10 | — | — | ✚ |
| Malay Mail | -2 | Negative | -0.4879 | -2.2961 | ⚠️ | 4 | — | — | ✚ |
| Parti Keadilan Rakyat | -2 | Negative | -0.5983 | -2.7827 | ⚠️ | 1 | PH | PKR |  |

### LOCATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| United States | +3 | Very Positive | 0.6040 | 2.5172 | ⚠️ | 7 | — | — | ✚ |
| India | +2 | Positive | 0.3725 | 1.4967 |  | 9 | — | — | ✚ |
| Korea | +2 | Positive | 0.3291 | 1.3054 |  | 4 | — | — | ✚ |
| England | +1 | Slightly Positive | 0.2725 | 1.0559 |  | 14 | — | — | ✚ |
| Pakistan | +1 | Slightly Positive | 0.2024 | 0.7469 |  | 4 | — | — | ✚ |
| South Korea | +1 | Slightly Positive | 0.2018 | 0.7442 |  | 4 | — | — | ✚ |
| Silicon Valley | +1 | Slightly Positive | 0.2007 | 0.7394 |  | 3 | — | — | ✚ |
| Keningau | +1 | Slightly Positive | 0.1998 | 0.7354 |  | 3 | — | — | ✚ |
| Kuching | +1 | Slightly Positive | 0.1869 | 0.6786 |  | 6 | — | — |  |
| JB | +1 | Slightly Positive | 0.1793 | 0.6451 |  | 15 | — | — | ✚ |
| Bintulu | +1 | Slightly Positive | 0.1714 | 0.6102 |  | 5 | — | — | ✚ |
| Vietnam | +1 | Slightly Positive | 0.1652 | 0.5829 |  | 8 | — | — | ✚ |
| UK | +1 | Slightly Positive | 0.1607 | 0.5631 |  | 30 | — | — | ✚ |
| Thailand | +1 | Slightly Positive | 0.1544 | 0.5353 |  | 9 | — | — | ✚ |
| Linggi | +1 | Slightly Positive | 0.1432 | 0.4859 |  | 8 | — | — |  |
| Klang | +1 | Slightly Positive | 0.1400 | 0.4718 |  | 3 | — | — | ✚ |
| Taiwan | +1 | Slightly Positive | 0.1313 | 0.4335 |  | 8 | — | — | ✚ |
| US | +1 | Slightly Positive | 0.1247 | 0.4044 |  | 30 | — | — | ✚ |
| Negri Sembilan | +1 | Slightly Positive | 0.1005 | 0.2977 |  | 4 | — | — | ✚ |
| Singapore | +0 | Neutral | 0.0989 | 0.2906 |  | 21 | — | — | ✚ |
| Kuala Lumpur | +0 | Neutral | 0.0711 | 0.1681 |  | 30 | — | — |  |
| Johor | +0 | Neutral | 0.0541 | 0.0932 |  | 30 | — | — |  |
| Sarawak | +0 | Neutral | 0.0476 | 0.0645 |  | 24 | — | — |  |
| Sandakan | +0 | Neutral | 0.0457 | 0.0561 |  | 5 | — | — | ✚ |
| Putrajaya | +0 | Neutral | 0.0453 | 0.0544 |  | 15 | — | — | ✚ |
| China | +0 | Neutral | 0.0383 | 0.0235 |  | 30 | — | — | ✚ |
| Spain | +0 | Neutral | 0.0361 | 0.0138 |  | 20 | — | — | ✚ |
| Muar | +0 | Neutral | 0.0253 | -0.0338 |  | 17 | — | — | ✚ |
| Selangor | +0 | Neutral | 0.0160 | -0.0748 |  | 24 | — | — |  |
| Seremban | +0 | Neutral | 0.0107 | -0.0982 |  | 15 | — | — | ✚ |
| Perak | +0 | Neutral | 0.0018 | -0.1374 |  | 20 | — | — |  |
| France | +0 | Neutral | 0.0012 | -0.1400 |  | 10 | — | — | ✚ |
| N14 | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | — | — |  |
| Pasir Gudang | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — |  |
| Pertang | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | — | — |  |
| Rantau | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | — | — |  |
| Alor Setar | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Bangladesh | +0 | Neutral | 0.0000 | -0.1453 |  | 4 | — | — | ✚ |
| Batu Pahat | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Beaufort | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Beluran | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Betong | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Brunei | +0 | Neutral | 0.0000 | -0.1453 |  | 2 | — | — | ✚ |
| Dungun | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Gombak | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Hulu Selangor | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Ipoh | +0 | Neutral | 0.0000 | -0.1453 |  | 10 | — | — | ✚ |
| Kangar | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Kelantan | +0 | Neutral | 0.0000 | -0.1453 |  | 5 | — | — | ✚ |
| Kemaman | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Kota Bharu | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Kota Tinggi | +0 | Neutral | 0.0000 | -0.1453 |  | 2 | — | — | ✚ |
| Kuala Selangor | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Kuala Terengganu | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Kuantan | +0 | Neutral | 0.0000 | -0.1453 |  | 7 | — | — | ✚ |
| Kudat | +0 | Neutral | 0.0000 | -0.1453 |  | 2 | — | — | ✚ |
| Kunak | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Limbang | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Lipis | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Maran | +0 | Neutral | 0.0000 | -0.1453 |  | 10 | — | — | ✚ |
| Mersing | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Pasir Puteh | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Penampang | +0 | Neutral | 0.0000 | -0.1453 |  | 3 | — | — | ✚ |
| Putatan | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Qatar | +0 | Neutral | 0.0000 | -0.1453 |  | 6 | — | — | ✚ |
| Ranau | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Rompin | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Samarahan | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Sarikei | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Segamat | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Semporna | +0 | Neutral | 0.0000 | -0.1453 |  | 5 | — | — | ✚ |
| Serian | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Sibu | +0 | Neutral | 0.0000 | -0.1453 |  | 6 | — | — | ✚ |
| Tambunan | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Tenom | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| Terengganu | +0 | Neutral | 0.0000 | -0.1453 |  | 4 | — | — | ✚ |
| Penang | +0 | Neutral | -0.0036 | -0.1612 |  | 18 | — | — |  |
| Negeri Sembilan | +0 | Neutral | -0.0134 | -0.2044 |  | 30 | — | — |  |
| Melaka | +0 | Neutral | -0.0346 | -0.2978 |  | 25 | — | — |  |
| Parliament House | +0 | Neutral | -0.0451 | -0.3441 |  | 13 | — | — |  |
| Cameron Highlands | +0 | Neutral | -0.0453 | -0.3450 |  | 5 | — | — | ✚ |
| Iran | +0 | Neutral | -0.0503 | -0.3670 |  | 30 | — | — | ✚ |
| Ukraine | +0 | Neutral | -0.0637 | -0.4261 |  | 4 | — | — | ✚ |
| Kedah | +0 | Neutral | -0.0649 | -0.4314 |  | 10 | — | — | ✚ |
| Pahang | +0 | Neutral | -0.0690 | -0.4495 |  | 14 | — | — | ✚ |
| Kota Kinabalu | +0 | Neutral | -0.0694 | -0.4512 |  | 6 | — | — |  |
| Sabah | +0 | Neutral | -0.0703 | -0.4552 |  | 26 | — | — |  |
| N9 Polls | +0 | Neutral | -0.0732 | -0.4680 |  | 6 | — | — | ✚ |
| Argentina | -1 | Slightly Negative | -0.1388 | -0.7572 |  | 28 | — | — | ✚ |
| Australia | -1 | Slightly Negative | -0.1518 | -0.8145 |  | 9 | — | — | ✚ |
| Shah Alam | -1 | Slightly Negative | -0.1575 | -0.8396 |  | 6 | — | — | ✚ |
| Germany | -1 | Slightly Negative | -0.1577 | -0.8405 |  | 9 | — | — | ✚ |
| Middle East | -1 | Slightly Negative | -0.1611 | -0.8555 |  | 3 | — | — | ✚ |
| Indonesia | -1 | Slightly Negative | -0.1655 | -0.8749 |  | 11 | — | — | ✚ |
| Petaling Jaya | -1 | Slightly Negative | -0.2365 | -1.1878 |  | 3 | — | — | ✚ |
| Miri | -1 | Slightly Negative | -0.2585 | -1.2848 |  | 5 | — | — | ✚ |
| Lahad Datu | -1 | Slightly Negative | -0.2997 | -1.4664 |  | 2 | — | — | ✚ |
| Mexico | -2 | Negative | -0.3296 | -1.5982 |  | 10 | — | — | ✚ |
| Sepang | -2 | Negative | -0.3507 | -1.6913 |  | 10 | — | — | ✚ |
| Brazil | -2 | Negative | -0.3623 | -1.7424 |  | 8 | — | — | ✚ |
| Wall Street | -2 | Negative | -0.4253 | -2.0201 | ⚠️ | 8 | — | — | ✚ |
| Norway | -2 | Negative | -0.5037 | -2.3657 | ⚠️ | 4 | — | — | ✚ |
| West Asia | -2 | Negative | -0.5954 | -2.7699 | ⚠️ | 7 | — | — | ✚ |
| Kinabatangan | -2 | Negative | -0.5994 | -2.7876 | ⚠️ | 1 | — | — | ✚ |

### EVENT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| WAN IFRA ASIA MEDIA AWARDS 2025 | +3 | Very Positive | 0.9141 | 3.8842 | ⚠️ | 1 | — | — | ✚ |
| court case | +3 | Very Positive | 0.7717 | 3.2564 | ⚠️ | 1 | — | — | ✚ |
| general election | +2 | Positive | 0.4574 | 1.8710 |  | 1 | — | — | ✚ |
| Investigation | +2 | Positive | 0.3680 | 1.4769 |  | 5 | — | — | ✚ |
| Federal Court | +2 | Positive | 0.3486 | 1.3914 |  | 2 | — | — | ✚ |
| World Cup | +1 | Slightly Positive | 0.2579 | 0.9915 |  | 22 | — | — | ✚ |
| State Polls 2026 | +1 | Slightly Positive | 0.1895 | 0.6900 |  | 3 | — | — | ✚ |
| campaign | +1 | Slightly Positive | 0.1720 | 0.6129 |  | 11 | — | — |  |
| Appeal | +1 | Slightly Positive | 0.1497 | 0.5146 |  | 11 | — | — | ✚ |
| Negeri Sembilan State Election 2026 | +0 | Neutral | 0.0947 | 0.2721 |  | 21 | — | — |  |
| pilihan raya | +0 | Neutral | 0.0803 | 0.2087 |  | 12 | — | — | ✚ |
| Summit | +0 | Neutral | 0.0424 | 0.0416 |  | 9 | — | — | ✚ |
| PRN Negeri | +0 | Neutral | 0.0378 | 0.0213 |  | 18 | — | — | ✚ |
| High Court | +0 | Neutral | 0.0318 | -0.0051 |  | 5 | — | — | ✚ |
| BN Candidate Announcement (NS) | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | — | — |  |
| ceramah | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | — | — |  |
| HAWANA X TM Media Event | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | — | — |  |
| kempen | +0 | Neutral | 0.0000 | -0.1453 |  | 9 | — | — |  |
| majlis | +0 | Neutral | 0.0000 | -0.1453 |  | 8 | — | — |  |
| Sarawak State Election 2026 | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | — | — |  |
| walkabout | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | — | — |  |
| Piala Dunia | +0 | Neutral | 0.0000 | -0.1453 |  | 21 | — | — | ✚ |
| pilihan raya negeri | +0 | Neutral | 0.0000 | -0.1453 |  | 9 | — | — | ✚ |
| Pilihan Raya Negeri Johor | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| sidang akhbar | +0 | Neutral | 0.0000 | -0.1453 |  | 3 | — | — | ✚ |
| Typhoon Bavi | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| rally | +0 | Neutral | -0.0096 | -0.1876 |  | 4 | — | — |  |
| event | +0 | Neutral | -0.0227 | -0.2454 |  | 24 | — | — |  |
| Johor State Election | +0 | Neutral | -0.0416 | -0.3287 |  | 11 | — | — |  |
| nomination day | +0 | Neutral | -0.0764 | -0.4821 |  | 5 | — | — | ✚ |
| state election | -1 | Slightly Negative | -0.1658 | -0.8762 |  | 4 | — | — | ✚ |
| Sessions Court | -1 | Slightly Negative | -0.2714 | -1.3417 |  | 1 | — | — | ✚ |
| Court of Appeal | -2 | Negative | -0.5983 | -2.7827 | ⚠️ | 1 | — | — | ✚ |

### CONCEPT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| renewable energy | +3 | Very Positive | 0.7067 | 2.9699 | ⚠️ | 2 | — | — | ✚ |
| green technology | +3 | Very Positive | 0.6705 | 2.8103 | ⚠️ | 1 | — | — | ✚ |
| artificial intelligence | +2 | Positive | 0.5980 | 2.4907 | ⚠️ | 2 | — | — | ✚ |
| Service tax | +2 | Positive | 0.4363 | 1.7780 |  | 5 | — | — |  |
| inflation | +2 | Positive | 0.4180 | 1.6973 |  | 5 | — | — | ✚ |
| Onn Hafiz 56-seats solo bid | +2 | Positive | 0.3667 | 1.4711 |  | 2 | — | — |  |
| copyright | +1 | Slightly Positive | 0.2840 | 1.1066 |  | 14 | — | — | ✚ |
| MADANI government | +1 | Slightly Positive | 0.1898 | 0.6913 |  | 18 | — | — |  |
| TVET | +1 | Slightly Positive | 0.1823 | 0.6583 |  | 7 | — | — | ✚ |
| Wealth tax | +1 | Slightly Positive | 0.1482 | 0.5080 |  | 0 | — | — |  |
| Bersatu own logo in N9 | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | — | — |  |
| Cost of living | +0 | Neutral | 0.0000 | -0.1453 |  | 6 | — | — |  |
| Super El Nino food security | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — |  |
| Third force movement | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | — | — |  |
| UEC recognition | +0 | Neutral | 0.0000 | -0.1453 |  | 0 | — | — |  |
| opposition | +0 | Neutral | 0.0000 | -0.1453 |  | 2 | — | — | ✚ |
| wake-up call | +0 | Neutral | 0.0000 | -0.1453 |  | 1 | — | — | ✚ |
| AI | +0 | Neutral | -0.0920 | -0.5509 |  | 30 | — | — | ✚ |
| Subsidies & welfare aid | -1 | Slightly Negative | -0.1239 | -0.6915 |  | 22 | — | — |  |
| transport | -2 | Negative | -0.3112 | -1.5171 |  | 8 | — | — | ✚ |
| water supply | -2 | Negative | -0.3612 | -1.7375 |  | 1 | — | — | ✚ |
| racism | -2 | Negative | -0.3790 | -1.8160 |  | 4 | — | — | ✚ |
| mandate | -2 | Negative | -0.3818 | -1.8283 |  | 3 | — | — | ✚ |
| deposits | -2 | Negative | -0.4574 | -2.1616 | ⚠️ | 1 | — | — | ✚ |

---

## Methodology

1. **Entity Source:** Loaded from the 2026-07-18T000553Z extraction roster (286 Phase-1 entity names) plus the 78 canonical entities from the per-entity index. Roster names were merged into canonical entities by normalized name/alias matching (honorific-stripped); unmerged names were added as new entities (199 new).
2. **Context Extraction:** For each entity, search variants (canonical name + aliases + roster matches) were located in the 2026-07-18 raw source collection (24 sources, 24 processed, ~914732 chars). A context window (~140+170 chars) was extracted around each mention (markdown stripped, de-duplicated, capped at 30/entity).
3. **Sentiment Scoring:** Applied VADER to each context snippet; entity sentiment = mean compound across snippets.
4. **Score Mapping:** VADER compound (-1..+1) → 7-point Likert (-3..+3): +3 ≥0.6, +2 ≥0.3, +1 ≥0.1, 0 (-0.1..0.1), -1 >-0.3, -2 >-0.6, -3 ≤-0.6.
5. **Anomaly Detection:** Z-score on raw compound vs overall mean/std; flagged when |z| > 2.
6. **Coalition/Party Aggregation:** Persons + political-party/coalition orgs mapped via per-entity metadata and affiliation maps (FIGURE_AFFILIATIONS, ORG_TO_COALITION, analyst-extended NEW_FIGURE_AFFIL).

---

*Report generated by OpenCLaw Sentiment Analysis Pipeline (sentiment-analysis skill)*
*VADER: Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.*

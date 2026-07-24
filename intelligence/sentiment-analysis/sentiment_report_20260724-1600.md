# Sentiment Analysis Report

**Classification:** TLP:AMBER
**Generated:** 2026-07-24 16:00 +08
**Report Date:** 2026-07-24
**Report Timestamp:** 2026-07-24 16:00 +08
**Extraction ID:** ext_20260724_1400_phase1
**Extraction Source:** 2026-07-24T14:00:00+08:00
**Collection Cycle:** 2026-07-24T000540Z
**Source Count:** 24
**Analysis Method:** VADER Sentiment Analysis on fresh context snippets extracted from 2026-07-24 raw collection
**Score Range:** -3 (very negative) to +3 (very positive)
**Anomaly Threshold:** |z-score| > 2

> **Data-freshness note:** The 2026-07-24 extraction produced Phase-1 entity name lists
> only; Phase-2 per-entity context files were not regenerated for this cycle. To produce a
> genuine 2026-07-24 sentiment signal, context snippets were extracted directly from the
> 2026-07-24 raw source collection and scored with VADER. Coalition/party metadata sourced
> from the canonical per-entity files (2026-07-16 Phase-2 set) plus an analyst-extended
> affiliation map for newly-extracted figures.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Roster Entities (Phase-1 names) | 245 |
| Analysis Entities (merged) | 257 |
| Canonical Entities (from index) | 78 |
| New Entities (this cycle) | 179 |
| Roster Names Matched to Canonical | 50 |
| Sources Processed | 24 |
| Entities with Context | 238 |
| Entities without Context (fallback) | 19 |
| Overall Mean Sentiment | +0.125 |
| Overall Std Deviation | 0.901 |
| Overall Median Sentiment | +0.000 |
| Overall Raw Mean | 0.0286 |
| Overall Raw Std Dev | 0.2107 |
| Sentiment Range | [-3, +3] |
| Positive Entities | 41 |
| Neutral Entities | 189 |
| Negative Entities | 27 |
| Anomalies Detected | 24 |
| Coalitions Analyzed | 8 |
| Parties Analyzed | 15 |

### Sentiment Distribution

```
Positive (41)  █████████████████████████████████████████
Neutral  (189)  █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
Negative (27)  ███████████████████████████
```

---

## Coalition Aggregate Sentiment

| Coalition | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range |
|-----------|:-:|------|:----------:|:-------:|:--------:|:-----:|
| GPS | +0 | Neutral | 0.0979 | 0.1959 | 4 | [0.000, 0.392] |
| PH | +0 | Neutral | 0.0451 | 0.1847 | 16 | [-0.121, 0.540] |
| PN | +0 | Neutral | 0.0345 | 0.1083 | 6 | [-0.114, 0.177] |
| BERSAMA | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| GRS | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| PEJUANG | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] |
| WARISAN | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| BN | +0 | Neutral | -0.0262 | 0.0880 | 13 | [-0.263, 0.119] |
### Coalition Entities
- **GPS** (+0, Neutral): Sim Kui Hian, Tiong King Sing, Gabungan Parti Sarawak, PRS
- **PH** (+0, Neutral): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Anthony Loke, Dzulkefly Ahmad, Mohamad Sabu, Syed Saddiq, Democratic Action Party, Malaysia United Democratic Alliance, Pakatan Harapan, Parti Amanah Negara, Parti Keadilan Rakyat, Keadilan
- **PN** (+0, Neutral): Muhyiddin Yassin, Hamzah Zainudin, Sanusi, Parti Islam Se-Malaysia, Parti Pribumi Bersatu Malaysia, Perikatan Nasional
- **BERSAMA** (+0, Neutral): Parti Bersama
- **GRS** (+0, Neutral): GRS
- **PEJUANG** (+0, Neutral): Mahathir Mohamad, Pejuang
- **WARISAN** (+0, Neutral): Parti Warisan
- **BN** (+0, Neutral): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Jalaluddin Alias, Saarani Mohamad, Najib Razak, Onn Hafiz, Barisan Nasional, Malaysian Chinese Association, Malaysian Indian Congress, United Malays National Organisation

---

## Party Aggregate Sentiment

| Party | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range | Coalition |
|-------|:-:|------|:----------:|:-------:|:--------:|:-----:|:---------:|
| Keadilan | +2 | Positive | 0.5399 | 0.0000 | 1 | [0.540, 0.540] | — |
| PRS | +2 | Positive | 0.3918 | 0.0000 | 1 | [0.392, 0.392] | GPS |
| AMANAH | +1 | Slightly Positive | 0.1282 | 0.3071 | 3 | [-0.121, 0.471] | PH |
| MIC | +1 | Slightly Positive | 0.1188 | 0.0000 | 1 | [0.119, 0.119] | BN |
| BERSATU | +0 | Neutral | 0.0684 | 0.1590 | 3 | [-0.114, 0.177] | PN |
| PAS | +0 | Neutral | 0.0125 | 0.0177 | 2 | [0.000, 0.025] | PN |
| BERSAMA | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | BERSAMA |
| GPS | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] | GPS |
| MUDA | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] | PH |
| Pejuang | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | PEJUANG |
| Warisan | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | WARISAN |
| PKR | +0 | Neutral | -0.0085 | 0.0226 | 7 | [-0.060, 0.000] | PH |
| DAP | +0 | Neutral | -0.0271 | 0.0383 | 2 | [-0.054, 0.000] | PH |
| UMNO | +0 | Neutral | -0.0373 | 0.0862 | 10 | [-0.263, 0.000] | BN |
| MCA | +0 | Neutral | -0.0825 | 0.0000 | 1 | [-0.083, -0.083] | BN |
### Party Entities
- **Keadilan** (+2, Positive, → —): Keadilan
- **PRS** (+2, Positive, → GPS): PRS
- **AMANAH** (+1, Slightly Positive, → PH): Dzulkefly Ahmad, Mohamad Sabu, Parti Amanah Negara
- **MIC** (+1, Slightly Positive, → BN): Malaysian Indian Congress
- **BERSATU** (+0, Neutral, → PN): Muhyiddin Yassin, Hamzah Zainudin, Parti Pribumi Bersatu Malaysia
- **PAS** (+0, Neutral, → PN): Sanusi, Parti Islam Se-Malaysia
- **BERSAMA** (+0, Neutral, → BERSAMA): Parti Bersama
- **GPS** (+0, Neutral, → GPS): Sim Kui Hian, Tiong King Sing
- **MUDA** (+0, Neutral, → PH): Syed Saddiq, Malaysia United Democratic Alliance
- **Pejuang** (+0, Neutral, → PEJUANG): Mahathir Mohamad
- **Warisan** (+0, Neutral, → WARISAN): Parti Warisan
- **PKR** (+0, Neutral, → PH): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Parti Keadilan Rakyat
- **DAP** (+0, Neutral, → PH): Anthony Loke, Democratic Action Party
- **UMNO** (+0, Neutral, → BN): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Jalaluddin Alias, Saarani Mohamad, Najib Razak, Onn Hafiz, United Malays National Organisation
- **MCA** (+0, Neutral, → BN): Malaysian Chinese Association

---

## Sentiment Anomalies (|z-score| > 2)

**24 anomalies detected.**

| # | Entity | Type | Score | Label | Z-Score | Direction | Coalition | Party | Contexts |
|---|--------|------|:-----:|-------|:-------:|:---------:|-----------|:------:|:--------:|
| 1 | WAN IFRA ASIA MEDIA AWARDS 2025 | EVENT | +3 | Very Positive | 4.2246 | positive | N/A | — | 2 |
| 2 | Strait of Hormuz | LOCATION | -3 | Very Negative | -4.0609 | negative | N/A | — | 1 |
| 3 | Court case | EVENT | +3 | Very Positive | 3.5269 | positive | N/A | — | 1 |
| 4 | The Star | ORGANIZATION | +3 | Very Positive | 3.3907 | positive | N/A | — | 1 |
| 5 | Onn Hafiz 56-seats solo bid | CONCEPT | +3 | Very Positive | 3.3452 | positive | N/A | — | 1 |
| 6 | state election | EVENT | +3 | Very Positive | 3.2322 | positive | N/A | — | 1 |
| 7 | green technology | CONCEPT | +3 | Very Positive | 3.0466 | positive | N/A | — | 1 |
| 8 | renewable energy | CONCEPT | +3 | Very Positive | 3.0466 | positive | N/A | — | 1 |
| 9 | DVS | ORGANIZATION | +3 | Very Positive | 3.0272 | positive | N/A | — | 4 |
| 10 | West Asia | LOCATION | -2 | Negative | -2.7415 | negative | N/A | — | 3 |
| 11 | Grab | ORGANIZATION | -2 | Negative | -2.6927 | negative | N/A | — | 4 |
| 12 | Klang | LOCATION | -2 | Negative | -2.6860 | negative | N/A | — | 10 |
| 13 | United States | LOCATION | +2 | Positive | 2.6390 | positive | N/A | — | 4 |
| 14 | Probe | EVENT | -2 | Negative | -2.6333 | negative | N/A | — | 6 |
| 15 | Hearing | EVENT | +2 | Positive | 2.4852 | positive | N/A | — | 4 |
| 16 | Russia | LOCATION | +2 | Positive | 2.4838 | positive | N/A | — | 4 |
| 17 | Keadilan | ORGANIZATION | +2 | Positive | 2.4268 | positive | PH | Keadilan | 4 |
| 18 | Suara Keadilan | ORGANIZATION | +2 | Positive | 2.4268 | positive | N/A | — | 1 |
| 19 | Arrest | EVENT | -2 | Negative | -2.3386 | negative | N/A | — | 4 |
| 20 | Free Malaysia Today | ORGANIZATION | +2 | Positive | 2.2878 | positive | N/A | — | 1 |
| 21 | Spain | LOCATION | +2 | Positive | 2.2522 | positive | N/A | — | 4 |
| 22 | KWSP | ORGANIZATION | +2 | Positive | 2.2370 | positive | N/A | — | 4 |
| 23 | Investigation | EVENT | +2 | Positive | 2.1169 | positive | N/A | — | 4 |
| 24 | Parti Amanah Negara | ORGANIZATION | +2 | Positive | 2.1013 | positive | PH | AMANAH | 7 |
---

## Entity Sentiments by Type

### PERSON

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Firdausi Suffian | +2 | Positive | 0.3612 | 1.5787 |  | 2 | — | — | ✚ |
| Rajeentheran Suntheralingam | +1 | Slightly Positive | 0.1877 | 0.7553 |  | 4 | — | — | ✚ |
| Muhyiddin Yassin | +1 | Slightly Positive | 0.1774 | 0.7064 |  | 4 | PN | BERSATU |  |
| Tun | +0 | Neutral | 0.0863 | 0.2741 |  | 30 | — | — | ✚ |
| Mohamad Sabu | +0 | Neutral | 0.0344 | 0.0277 |  | 4 | PH | AMANAH | ✚ |
| Asli | +0 | Neutral | 0.0193 | -0.0439 |  | 4 | — | — | ✚ |
| Ab Rauf Yusoh | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | BN | UMNO |  |
| Aminuddin Harun | +0 | Neutral | 0.0000 | -0.1355 |  | 8 | PH | PKR |  |
| Hassan Abdul Karim | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | PH | PKR |  |
| Jalaluddin Abdul Rahman | +0 | Neutral | 0.0000 | -0.1355 |  | 3 | BN | UMNO |  |
| Khairy Jamaluddin | +0 | Neutral | 0.0000 | -0.1355 |  | 3 | BN | UMNO |  |
| Mahathir Mohamad | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | PEJUANG | Pejuang |  |
| Mohd Ghazali Sabari | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | — | — |  |
| Nik Nazmi Nik Ahmad | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | PH | PKR |  |
| Nurul Izzah Anwar | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | PH | PKR |  |
| Rafizi Ramli | +0 | Neutral | 0.0000 | -0.1355 |  | 6 | PH | PKR |  |
| Sim Kui Hian | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | GPS | GPS |  |
| Tiong King Sing | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | GPS | GPS |  |
| Abdul Razak | +0 | Neutral | 0.0000 | -0.1355 |  | 8 | — | — | ✚ |
| Anthony Loke | +0 | Neutral | 0.0000 | -0.1355 |  | 3 | PH | DAP | ✚ |
| Datuk | +0 | Neutral | 0.0000 | -0.1355 |  | 11 | — | — | ✚ |
| Muhammad Nazri Kassim | +0 | Neutral | 0.0000 | -0.1355 |  | 2 | — | — | ✚ |
| Datuk Seri | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — | ✚ |
| Jalaluddin Alias | +0 | Neutral | 0.0000 | -0.1355 |  | 3 | BN | UMNO | ✚ |
| Mohd Yusri Hassan Basri | +0 | Neutral | 0.0000 | -0.1355 |  | 2 | — | — | ✚ |
| Saarani Mohamad | +0 | Neutral | 0.0000 | -0.1355 |  | 2 | BN | UMNO | ✚ |
| Zamri Md Said | +0 | Neutral | 0.0000 | -0.1355 |  | 2 | — | — | ✚ |
| Didedah Hari Ini Atau Rabu | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — | ✚ |
| Menteri Besar Perak | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Najib Razak | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | BN | UMNO | ✚ |
| Nazri | +0 | Neutral | 0.0000 | -0.1355 |  | 2 | — | — | ✚ |
| Perak | +0 | Neutral | 0.0000 | -0.1355 |  | 12 | — | — | ✚ |
| Syed Saddiq | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | PH | MUDA | ✚ |
| Sanusi | +0 | Neutral | 0.0000 | -0.1355 |  | 3 | PN | PAS | ✚ |
| Ahmad Zahid Hamidi | +0 | Neutral | -0.0024 | -0.1469 |  | 20 | BN | UMNO |  |
| Anwar Ibrahim | +0 | Neutral | -0.0598 | -0.4193 |  | 30 | PH | PKR |  |
| Mohamad Hasan | -1 | Slightly Negative | -0.1073 | -0.6448 |  | 3 | BN | UMNO |  |
| Hamzah Zainudin | -1 | Slightly Negative | -0.1140 | -0.6766 |  | 13 | PN | BERSATU | ✚ |
| Dzulkefly Ahmad | -1 | Slightly Negative | -0.1211 | -0.7103 |  | 4 | PH | AMANAH | ✚ |
| Onn Hafiz | -1 | Slightly Negative | -0.2633 | -1.3851 |  | 2 | BN | UMNO | ✚ |
### ORGANIZATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| The Star | +3 | Very Positive | 0.7430 | 3.3907 | ⚠️ | 1 | — | — | ✚ |
| DVS | +3 | Very Positive | 0.6664 | 3.0272 | ⚠️ | 4 | — | — | ✚ |
| Keadilan | +2 | Positive | 0.5399 | 2.4268 | ⚠️ | 4 | PH | Keadilan | ✚ |
| Suara Keadilan | +2 | Positive | 0.5399 | 2.4268 | ⚠️ | 1 | — | — | ✚ |
| Free Malaysia Today | +2 | Positive | 0.5106 | 2.2878 | ⚠️ | 1 | — | — | ✚ |
| KWSP | +2 | Positive | 0.4999 | 2.2370 | ⚠️ | 4 | — | — | ✚ |
| Parti Amanah Negara | +2 | Positive | 0.4713 | 2.1013 | ⚠️ | 7 | PH | AMANAH |  |
| PRS | +2 | Positive | 0.3918 | 1.7239 |  | 2 | GPS | PRS | ✚ |
| Media Mulia | +1 | Slightly Positive | 0.1555 | 0.6025 |  | 6 | — | — | ✚ |
| ASEAN | +1 | Slightly Positive | 0.1506 | 0.5792 |  | 20 | — | — |  |
| Parti Pribumi Bersatu Malaysia | +1 | Slightly Positive | 0.1419 | 0.5379 |  | 5 | PN | BERSATU |  |
| Apple | +1 | Slightly Positive | 0.1208 | 0.4378 |  | 15 | — | — | ✚ |
| Malaysian Indian Congress | +1 | Slightly Positive | 0.1188 | 0.4283 |  | 30 | BN | MIC |  |
| Perodua | +0 | Neutral | 0.0823 | 0.2551 |  | 6 | — | — | ✚ |
| AirBorneo | +0 | Neutral | 0.0822 | 0.2546 |  | 2 | — | — | ✚ |
| DUN | +0 | Neutral | 0.0794 | 0.2413 |  | 30 | — | — | ✚ |
| IMU | +0 | Neutral | 0.0706 | 0.1995 |  | 7 | — | — | ✚ |
| BURSA | +0 | Neutral | 0.0603 | 0.1507 |  | 9 | — | — | ✚ |
| NST | +0 | Neutral | 0.0515 | 0.1089 |  | 30 | — | — | ✚ |
| NGO | +0 | Neutral | 0.0279 | -0.0031 |  | 30 | — | — | ✚ |
| Parti Islam Se-Malaysia | +0 | Neutral | 0.0250 | -0.0169 |  | 30 | PN | PAS |  |
| TikTok | +0 | Neutral | 0.0235 | -0.0240 |  | 30 | — | — | ✚ |
| Google | +0 | Neutral | 0.0152 | -0.0634 |  | 22 | — | — | ✚ |
| PRN | +0 | Neutral | 0.0123 | -0.0771 |  | 30 | — | — | ✚ |
| Gabungan Parti Sarawak | +0 | Neutral | 0.0000 | -0.1355 |  | 3 | GPS | — |  |
| GRS | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | GRS | — |  |
| HAWANA | +0 | Neutral | 0.0000 | -0.1355 |  | 11 | — | — |  |
| Malaysia United Democratic Alliance | +0 | Neutral | 0.0000 | -0.1355 |  | 6 | PH | MUDA |  |
| Ministry of Finance | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — |  |
| Ministry of Home Affairs | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — |  |
| Parti Bersama | +0 | Neutral | 0.0000 | -0.1355 |  | 17 | BERSAMA | BERSAMA |  |
| Parti Keadilan Rakyat | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | PH | PKR |  |
| Parti Warisan | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | WARISAN | Warisan |  |
| Pejuang | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | PEJUANG | — |  |
| United Malays National Organisation | +0 | Neutral | 0.0000 | -0.1355 |  | 14 | BN | UMNO |  |
| AFP | +0 | Neutral | 0.0000 | -0.1355 |  | 5 | — | — | ✚ |
| Bernama | +0 | Neutral | 0.0000 | -0.1355 |  | 10 | — | — | ✚ |
| Borneo Post | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — | ✚ |
| Cabinet | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — | ✚ |
| CodeBlue | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — | ✚ |
| Harian Metro | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| KLK | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Kosmo | +0 | Neutral | 0.0000 | -0.1355 |  | 8 | — | — | ✚ |
| KPKM | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — | ✚ |
| Malay Mail | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — | ✚ |
| MalaysiaGazette | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — | ✚ |
| Malaysiakini | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — | ✚ |
| MCMC | +0 | Neutral | 0.0000 | -0.1355 |  | 12 | — | — | ✚ |
| mStar | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — | ✚ |
| Sabah News | +0 | Neutral | 0.0000 | -0.1355 |  | 3 | — | — | ✚ |
| Sinar Harian | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — | ✚ |
| Spotify | +0 | Neutral | 0.0000 | -0.1355 |  | 5 | — | — | ✚ |
| The Edge Malaysia | +0 | Neutral | 0.0000 | -0.1355 |  | 2 | — | — | ✚ |
| Barisan Nasional | +0 | Neutral | -0.0038 | -0.1536 |  | 29 | BN | — |  |
| World Cup | +0 | Neutral | -0.0084 | -0.1754 |  | 15 | — | — | ✚ |
| MOH | +0 | Neutral | -0.0189 | -0.2252 |  | 18 | — | — | ✚ |
| Perikatan Nasional | +0 | Neutral | -0.0230 | -0.2447 |  | 30 | PN | — |  |
| BuzzKini | +0 | Neutral | -0.0257 | -0.2575 |  | 4 | — | — | ✚ |
| JPA | +0 | Neutral | -0.0425 | -0.3372 |  | 8 | — | — | ✚ |
| Suruhanjaya Pencegahan Rasuah Malaysia | +0 | Neutral | -0.0530 | -0.3871 |  | 6 | — | — |  |
| Democratic Action Party | +0 | Neutral | -0.0542 | -0.3928 |  | 30 | PH | DAP |  |
| Suruhanjaya Pilihan Raya | +0 | Neutral | -0.0782 | -0.5067 |  | 10 | — | — |  |
| Tropicana | +0 | Neutral | -0.0820 | -0.5247 |  | 4 | — | — | ✚ |
| Malaysian Chinese Association | +0 | Neutral | -0.0825 | -0.5271 |  | 8 | BN | MCA |  |
| Vulcan Post | +0 | Neutral | -0.0846 | -0.5370 |  | 4 | — | — | ✚ |
| Pakatan Harapan | +0 | Neutral | -0.0895 | -0.5603 |  | 30 | PH | — |  |
| UN | -1 | Slightly Negative | -0.1164 | -0.6880 |  | 30 | — | — | ✚ |
| Galen Centre | -1 | Slightly Negative | -0.1691 | -0.9381 |  | 3 | — | — | ✚ |
| Parliament | -1 | Slightly Negative | -0.1848 | -1.0126 |  | 4 | — | — | ✚ |
| FIFA | -1 | Slightly Negative | -0.2255 | -1.2057 |  | 8 | — | — | ✚ |
| Grab | -2 | Negative | -0.5388 | -2.6927 | ⚠️ | 4 | — | — | ✚ |
### LOCATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| United States | +2 | Positive | 0.5846 | 2.6390 | ⚠️ | 4 | — | — | ✚ |
| Russia | +2 | Positive | 0.5519 | 2.4838 | ⚠️ | 4 | — | — | ✚ |
| Spain | +2 | Positive | 0.5031 | 2.2522 | ⚠️ | 4 | — | — | ✚ |
| Terengganu | +2 | Positive | 0.3578 | 1.5626 |  | 8 | — | — | ✚ |
| Miri | +1 | Slightly Positive | 0.1951 | 0.7904 |  | 2 | — | — | ✚ |
| France | +1 | Slightly Positive | 0.1643 | 0.6442 |  | 12 | — | — | ✚ |
| Kuching | +1 | Slightly Positive | 0.1372 | 0.5156 |  | 11 | — | — |  |
| England | +1 | Slightly Positive | 0.1356 | 0.5080 |  | 6 | — | — | ✚ |
| Melaka | +1 | Slightly Positive | 0.1132 | 0.4017 |  | 2 | — | — |  |
| Banting | +1 | Slightly Positive | 0.1096 | 0.3846 |  | 4 | — | — | ✚ |
| Japan | +0 | Neutral | 0.0989 | 0.3339 |  | 6 | — | — | ✚ |
| Penang | +0 | Neutral | 0.0830 | 0.2584 |  | 11 | — | — |  |
| Negeri Sembilan | +0 | Neutral | 0.0562 | 0.1312 |  | 30 | — | — |  |
| Johor | +0 | Neutral | 0.0485 | 0.0947 |  | 29 | — | — |  |
| Malaysia | +0 | Neutral | 0.0399 | 0.0538 |  | 30 | — | — | ✚ |
| Kota Kinabalu | +0 | Neutral | 0.0308 | 0.0107 |  | 8 | — | — |  |
| UK | +0 | Neutral | 0.0278 | -0.0036 |  | 30 | — | — | ✚ |
| India | +0 | Neutral | 0.0200 | -0.0406 |  | 14 | — | — | ✚ |
| Argentina | +0 | Neutral | 0.0122 | -0.0776 |  | 14 | — | — | ✚ |
| Rompin | +0 | Neutral | 0.0103 | -0.0866 |  | 5 | — | — | ✚ |
| Sarawak | +0 | Neutral | 0.0002 | -0.1346 |  | 30 | — | — |  |
| N14 | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | — | — |  |
| Pasir Gudang | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | — | — |  |
| Perak | +0 | Neutral | 0.0000 | -0.1355 |  | 12 | — | — |  |
| Pertang | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — |  |
| Rantau | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — |  |
| Batu Pahat | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Beaufort | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Beluran | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Betong | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Bintulu | +0 | Neutral | 0.0000 | -0.1355 |  | 5 | — | — | ✚ |
| Brunei | +0 | Neutral | 0.0000 | -0.1355 |  | 2 | — | — | ✚ |
| Cameron Highlands | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Dungun | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Gombak | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Hulu Selangor | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Ipoh | +0 | Neutral | 0.0000 | -0.1355 |  | 2 | — | — | ✚ |
| Kangar | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Kedah | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — | ✚ |
| Kemaman | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Keningau | +0 | Neutral | 0.0000 | -0.1355 |  | 5 | — | — | ✚ |
| Kota Bharu | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Kota Tinggi | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Kuala Selangor | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Kuala Terengganu | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Kuantan | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Kudat | +0 | Neutral | 0.0000 | -0.1355 |  | 2 | — | — | ✚ |
| Kulai | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Kunak | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Lahad Datu | +0 | Neutral | 0.0000 | -0.1355 |  | 2 | — | — | ✚ |
| Limbang | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Lipis | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Maran | +0 | Neutral | 0.0000 | -0.1355 |  | 2 | — | — | ✚ |
| Mersing | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Muar | +0 | Neutral | 0.0000 | -0.1355 |  | 5 | — | — | ✚ |
| Pahang | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — | ✚ |
| Pasir Puteh | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Penampang | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Perlis | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Petaling Jaya | +0 | Neutral | 0.0000 | -0.1355 |  | 5 | — | — | ✚ |
| Pontian | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Putatan | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Ranau | +0 | Neutral | 0.0000 | -0.1355 |  | 3 | — | — | ✚ |
| Samarahan | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Sandakan | +0 | Neutral | 0.0000 | -0.1355 |  | 5 | — | — | ✚ |
| Sarikei | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Segamat | +0 | Neutral | 0.0000 | -0.1355 |  | 4 | — | — | ✚ |
| Semporna | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Serian | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Sibu | +0 | Neutral | 0.0000 | -0.1355 |  | 3 | — | — | ✚ |
| Tambunan | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| Tawau | +0 | Neutral | 0.0000 | -0.1355 |  | 7 | — | — | ✚ |
| Tenom | +0 | Neutral | 0.0000 | -0.1355 |  | 5 | — | — | ✚ |
| Sabah | +0 | Neutral | -0.0055 | -0.1616 |  | 30 | — | — |  |
| Selangor | +0 | Neutral | -0.0157 | -0.2100 |  | 30 | — | — |  |
| Putrajaya | +0 | Neutral | -0.0343 | -0.2983 |  | 9 | — | — | ✚ |
| Linggi | +0 | Neutral | -0.0531 | -0.3875 |  | 12 | — | — |  |
| China | +0 | Neutral | -0.0540 | -0.3918 |  | 28 | — | — | ✚ |
| US | +0 | Neutral | -0.0559 | -0.4008 |  | 30 | — | — | ✚ |
| Parliament House | +0 | Neutral | -0.0821 | -0.5252 |  | 9 | — | — |  |
| South Korea | +0 | Neutral | -0.0850 | -0.5389 |  | 4 | — | — | ✚ |
| Kuala Lumpur | +0 | Neutral | -0.0935 | -0.5793 |  | 30 | — | — |  |
| Singapore | +0 | Neutral | -0.0992 | -0.6063 |  | 16 | — | — | ✚ |
| Korea | -1 | Slightly Negative | -0.2021 | -1.0947 |  | 5 | — | — | ✚ |
| Iran | -1 | Slightly Negative | -0.2258 | -1.2072 |  | 24 | — | — | ✚ |
| Kelantan | -1 | Slightly Negative | -0.2479 | -1.3120 |  | 6 | — | — | ✚ |
| Shah Alam | -1 | Slightly Negative | -0.2725 | -1.4288 |  | 3 | — | — | ✚ |
| Middle East | -2 | Negative | -0.3017 | -1.5674 |  | 6 | — | — | ✚ |
| Seremban | -2 | Negative | -0.3066 | -1.5906 |  | 6 | — | — | ✚ |
| Wall Street | -2 | Negative | -0.3225 | -1.6661 |  | 3 | — | — | ✚ |
| Sepang | -2 | Negative | -0.3389 | -1.7439 |  | 12 | — | — | ✚ |
| Indonesia | -2 | Negative | -0.3598 | -1.8431 |  | 7 | — | — | ✚ |
| Klang | -2 | Negative | -0.5374 | -2.6860 | ⚠️ | 10 | — | — | ✚ |
| West Asia | -2 | Negative | -0.5491 | -2.7415 | ⚠️ | 3 | — | — | ✚ |
| Strait of Hormuz | -3 | Very Negative | -0.8271 | -4.0609 | ⚠️ | 1 | — | — | ✚ |
### EVENT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| WAN IFRA ASIA MEDIA AWARDS 2025 | +3 | Very Positive | 0.9187 | 4.2246 | ⚠️ | 2 | — | — | ✚ |
| Court case | +3 | Very Positive | 0.7717 | 3.5269 | ⚠️ | 1 | — | — | ✚ |
| state election | +3 | Very Positive | 0.7096 | 3.2322 | ⚠️ | 1 | — | — | ✚ |
| Hearing | +2 | Positive | 0.5522 | 2.4852 | ⚠️ | 4 | — | — | ✚ |
| Investigation | +2 | Positive | 0.4746 | 2.1169 | ⚠️ | 4 | — | — | ✚ |
| election | +1 | Slightly Positive | 0.1476 | 0.5650 |  | 9 | — | — | ✚ |
| rally | +1 | Slightly Positive | 0.1286 | 0.4748 |  | 7 | — | — |  |
| Appeal | +0 | Neutral | 0.0793 | 0.2408 |  | 9 | — | — | ✚ |
| Summit | +0 | Neutral | 0.0386 | 0.0477 |  | 2 | — | — | ✚ |
| campaign | +0 | Neutral | 0.0164 | -0.0577 |  | 18 | — | — |  |
| BN Candidate Announcement (NS) | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | — | — |  |
| ceramah | +0 | Neutral | 0.0000 | -0.1355 |  | 3 | — | — |  |
| HAWANA X TM Media Event | +0 | Neutral | 0.0000 | -0.1355 |  | 11 | — | — |  |
| Johor State Election | +0 | Neutral | 0.0000 | -0.1355 |  | 2 | — | — |  |
| kempen | +0 | Neutral | 0.0000 | -0.1355 |  | 13 | — | — |  |
| majlis | +0 | Neutral | 0.0000 | -0.1355 |  | 5 | — | — |  |
| Negeri Sembilan State Election 2026 | +0 | Neutral | 0.0000 | -0.1355 |  | 11 | — | — |  |
| Sarawak State Election 2026 | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | — | — |  |
| walkabout | +0 | Neutral | 0.0000 | -0.1355 |  | 2 | — | — |  |
| Piala Dunia | +0 | Neutral | 0.0000 | -0.1355 |  | 7 | — | — | ✚ |
| pilihan raya | +0 | Neutral | 0.0000 | -0.1355 |  | 9 | — | — | ✚ |
| pilihan raya negeri | +0 | Neutral | 0.0000 | -0.1355 |  | 5 | — | — | ✚ |
| Pilihan Raya Negeri Johor | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| PRN Negeri | +0 | Neutral | 0.0000 | -0.1355 |  | 10 | — | — | ✚ |
| sidang akhbar | +0 | Neutral | 0.0000 | -0.1355 |  | 1 | — | — | ✚ |
| World Cup | +0 | Neutral | -0.0084 | -0.1754 |  | 15 | — | — | ✚ |
| event | -1 | Slightly Negative | -0.1375 | -0.7881 |  | 16 | — | — |  |
| Trial | -1 | Slightly Negative | -0.2000 | -1.0847 |  | 14 | — | — | ✚ |
| Charged | -1 | Slightly Negative | -0.2212 | -1.1853 |  | 1 | — | — | ✚ |
| Arrest | -2 | Negative | -0.4642 | -2.3386 | ⚠️ | 4 | — | — | ✚ |
| Probe | -2 | Negative | -0.5263 | -2.6333 | ⚠️ | 6 | — | — | ✚ |
### CONCEPT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Onn Hafiz 56-seats solo bid | +3 | Very Positive | 0.7334 | 3.3452 | ⚠️ | 1 | — | — |  |
| green technology | +3 | Very Positive | 0.6705 | 3.0466 | ⚠️ | 1 | — | — | ✚ |
| renewable energy | +3 | Very Positive | 0.6705 | 3.0466 | ⚠️ | 1 | — | — | ✚ |
| health insurance | +2 | Positive | 0.3802 | 1.6689 |  | 1 | — | — | ✚ |
| copyright | +1 | Slightly Positive | 0.2675 | 1.1340 |  | 18 | — | — | ✚ |
| Super El Nino food security | +1 | Slightly Positive | 0.2229 | 0.9224 |  | 0 | — | — |  |
| MADANI government | +1 | Slightly Positive | 0.1618 | 0.6324 |  | 11 | — | — |  |
| Wealth tax | +1 | Slightly Positive | 0.1482 | 0.5678 |  | 0 | — | — |  |
| Subsidies & welfare aid | +0 | Neutral | 0.0506 | 0.1046 |  | 8 | — | — |  |
| Bersatu own logo in N9 | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | — | — |  |
| Cost of living | +0 | Neutral | 0.0000 | -0.1355 |  | 2 | — | — |  |
| Service tax | +0 | Neutral | 0.0000 | -0.1355 |  | 3 | — | — |  |
| Third force movement | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | — | — |  |
| UEC recognition | +0 | Neutral | 0.0000 | -0.1355 |  | 0 | — | — |  |
| MediAsas | +0 | Neutral | 0.0000 | -0.1355 |  | 5 | — | — | ✚ |
| perpaduan | +0 | Neutral | 0.0000 | -0.1355 |  | 10 | — | — | ✚ |
| pork supply | +0 | Neutral | 0.0000 | -0.1355 |  | 2 | — | — | ✚ |
| AI | +0 | Neutral | -0.0382 | -0.3168 |  | 30 | — | — | ✚ |
| TVET | +0 | Neutral | -0.0670 | -0.4535 |  | 8 | — | — | ✚ |
| doctor shortage | -1 | Slightly Negative | -0.2500 | -1.3220 |  | 1 | — | — | ✚ |
---

## Methodology

1. **Entity Source:** Loaded from the 2026-07-24T14:00+08 extraction roster (245 Phase-1 entity names) plus the 78 canonical entities from the per-entity index. Roster names were merged into canonical entities by normalized name/alias matching (honorific-stripped); unmerged names were added as new entities (179 new).
2. **Context Extraction:** For each entity, search variants (canonical name + aliases + roster matches) were located in the 2026-07-24 raw source collection (24 sources, 24 processed, ~702521 chars). A context window (~140+170 chars) was extracted around each mention (markdown stripped, de-duplicated, capped at 30/entity).
3. **Sentiment Scoring:** Applied VADER to each context snippet; entity sentiment = mean compound across snippets.
4. **Score Mapping:** VADER compound (-1..+1) → 7-point Likert (-3..+3): +3 ≥0.6, +2 ≥0.3, +1 ≥0.1, 0 (-0.1..0.1), -1 >-0.3, -2 >-0.6, -3 ≤-0.6.
5. **Anomaly Detection:** Z-score on raw compound vs overall mean/std; flagged when |z| > 2.
6. **Coalition/Party Aggregation:** Persons + political-party/coalition orgs mapped via per-entity metadata and affiliation maps (FIGURE_AFFILIATIONS, ORG_TO_COALITION, analyst-extended NEW_FIGURE_AFFIL).

---

*Report generated by OpenCLaw Sentiment Analysis Pipeline (sentiment-analysis skill)*
*VADER: Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.*

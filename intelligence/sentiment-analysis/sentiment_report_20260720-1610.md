# Sentiment Analysis Report

**Classification:** TLP:AMBER
**Report Timestamp:** 20260720T080930Z (UTC)
**Report Timestamp (MYT):** 2026-07-20 16:10 +08
**Report Date:** 2026-07-20
**Extraction ID:** ext_20260720_000706_phase1
**Extraction Source:** 2026-07-20T06:08:07Z
**Collection Cycle:** 2026-07-20T000706Z
**Source Count:** 24
**Analysis Method:** VADER Sentiment Analysis on fresh context snippets extracted from 2026-07-20 raw collection
**Score Range:** -3 (very negative) to +3 (very positive)
**Anomaly Threshold:** |z-score| > 2

> **Data-freshness note:** The 2026-07-20 extraction produced Phase-1 entity name lists
> only; Phase-2 per-entity context files were not regenerated for this cycle. To produce a
> genuine 2026-07-20 sentiment signal, context snippets were extracted directly from the
> 2026-07-20 raw source collection and scored with VADER. Coalition/party metadata sourced
> from the canonical per-entity files (2026-07-16 Phase-2 set) plus an analyst-extended
> affiliation map for newly-extracted figures.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Roster Entities (Phase-1 names) | 255 |
| Analysis Entities (merged) | 267 |
| Canonical Entities (from index) | 78 |
| New Entities (this cycle) | 189 |
| Roster Names Matched to Canonical | 53 |
| Sources Processed | 24 |
| Entities with Context | 242 |
| Entities without Context (fallback) | 25 |
| Overall Mean Sentiment | +0.266 |
| Overall Std Deviation | 1.087 |
| Overall Median Sentiment | +0.000 |
| Overall Raw Mean | 0.0644 |
| Overall Raw Std Dev | 0.2479 |
| Sentiment Range | [-3, +3] |
| Positive Entities | 63 |
| Neutral Entities | 178 |
| Negative Entities | 26 |
| Anomalies Detected | 26 |
| Coalitions Analyzed | 8 |
| Parties Analyzed | 14 |

### Sentiment Distribution

```
Positive (63)  ███████████████████████████████████████████████████████████████
Neutral  (178)  ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
Negative (26)  ██████████████████████████
```

---

## Coalition Aggregate Sentiment

| Coalition | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range |
|-----------|:-:|------|:----------:|:-------:|:--------:|:-----:|
| GRS | +1 | Slightly Positive | 0.2108 | 0.5842 | 2 | [-0.202, 0.624] |
| PH | +0 | Neutral | 0.0796 | 0.2058 | 15 | [-0.154, 0.709] |
| BN | +0 | Neutral | 0.0702 | 0.1061 | 12 | [-0.070, 0.261] |
| BERSAMA | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| GPS | +0 | Neutral | 0.0000 | 0.0000 | 3 | [0.000, 0.000] |
| PEJUANG | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] |
| WARISAN | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| PN | +0 | Neutral | -0.0940 | 0.2776 | 7 | [-0.715, 0.098] |
### Coalition Entities
- **GRS** (+1, Slightly Positive): Hajiji Noor, GRS
- **PH** (+0, Neutral): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Fahmi Fadzil, Mohamad Sabu, Syed Saddiq, Steven Sim, Democratic Action Party, Malaysia United Democratic Alliance, Pakatan Harapan, Parti Amanah Negara, Parti Keadilan Rakyat
- **BN** (+0, Neutral): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Tun Faisal Ismail Aziz, Najib Razak, Onn Hafiz, Barisan Nasional, Malaysian Chinese Association, Malaysian Indian Congress, United Malays National Organisation
- **BERSAMA** (+0, Neutral): Parti Bersama
- **GPS** (+0, Neutral): Sim Kui Hian, Tiong King Sing, Gabungan Parti Sarawak
- **PEJUANG** (+0, Neutral): Mahathir Mohamad, Pejuang
- **WARISAN** (+0, Neutral): Parti Warisan
- **PN** (+0, Neutral): Muhyiddin Yassin, Azanna Ahmad Kamar, Abdul Hadi Awang, Sanusi, Parti Islam Se-Malaysia, Parti Pribumi Bersatu Malaysia, Perikatan Nasional

---

## Party Aggregate Sentiment

| Party | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range | Coalition |
|-------|:-:|------|:----------:|:-------:|:--------:|:-----:|:---------:|
| MCA | +1 | Slightly Positive | 0.2612 | 0.0000 | 1 | [0.261, 0.261] | BN |
| MIC | +1 | Slightly Positive | 0.2052 | 0.0000 | 1 | [0.205, 0.205] | BN |
| DAP | +1 | Slightly Positive | 0.1924 | 0.2546 | 2 | [0.012, 0.372] | PH |
| PKR | +1 | Slightly Positive | 0.1079 | 0.2456 | 8 | [0.000, 0.709] | PH |
| UMNO | +0 | Neutral | 0.0371 | 0.0856 | 9 | [-0.070, 0.201] | BN |
| PAS | +0 | Neutral | 0.0326 | 0.0564 | 3 | [0.000, 0.098] | PN |
| BERSAMA | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | BERSAMA |
| GPS | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] | GPS |
| MUDA | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] | PH |
| Pejuang | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | PEJUANG |
| Warisan | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | WARISAN |
| AMANAH | +0 | Neutral | -0.0769 | 0.1087 | 2 | [-0.154, 0.000] | PH |
| GRS | -1 | Slightly Negative | -0.2023 | 0.0000 | 1 | [-0.202, -0.202] | GRS |
| BERSATU | -1 | Slightly Negative | -0.2561 | 0.3986 | 3 | [-0.715, 0.000] | PN |
### Party Entities
- **MCA** (+1, Slightly Positive, → BN): Malaysian Chinese Association
- **MIC** (+1, Slightly Positive, → BN): Malaysian Indian Congress
- **DAP** (+1, Slightly Positive, → PH): Steven Sim, Democratic Action Party
- **PKR** (+1, Slightly Positive, → PH): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Fahmi Fadzil, Parti Keadilan Rakyat
- **UMNO** (+0, Neutral, → BN): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Tun Faisal Ismail Aziz, Najib Razak, Onn Hafiz, United Malays National Organisation
- **PAS** (+0, Neutral, → PN): Abdul Hadi Awang, Sanusi, Parti Islam Se-Malaysia
- **BERSAMA** (+0, Neutral, → BERSAMA): Parti Bersama
- **GPS** (+0, Neutral, → GPS): Sim Kui Hian, Tiong King Sing
- **MUDA** (+0, Neutral, → PH): Syed Saddiq, Malaysia United Democratic Alliance
- **Pejuang** (+0, Neutral, → PEJUANG): Mahathir Mohamad
- **Warisan** (+0, Neutral, → WARISAN): Parti Warisan
- **AMANAH** (+0, Neutral, → PH): Mohamad Sabu, Parti Amanah Negara
- **GRS** (-1, Slightly Negative, → GRS): Hajiji Noor
- **BERSATU** (-1, Slightly Negative, → PN): Muhyiddin Yassin, Azanna Ahmad Kamar, Parti Pribumi Bersatu Malaysia

---

## Sentiment Anomalies (|z-score| > 2)

**26 anomalies detected.**

| # | Entity | Type | Score | Label | Z-Score | Direction | Coalition | Party | Contexts |
|---|--------|------|:-----:|-------|:-------:|:---------:|-----------|:------:|:--------:|
| 1 | WAN IFRA ASIA MEDIA AWARDS 2025 | EVENT | +3 | Very Positive | 3.4459 | positive | N/A | — | 2 |
| 2 | Wall Street | LOCATION | -3 | Very Negative | -3.2301 | negative | N/A | — | 2 |
| 3 | South Korea | LOCATION | +3 | Very Positive | 3.1753 | positive | N/A | — | 1 |
| 4 | Azanna Ahmad Kamar | PERSON | -3 | Very Negative | -3.1450 | negative | PN | BERSATU | 4 |
| 5 | Daily Express | ORGANIZATION | +3 | Very Positive | 2.9752 | positive | N/A | — | 3 |
| 6 | Kangar | LOCATION | -3 | Very Negative | -2.9135 | negative | N/A | — | 5 |
| 7 | Trial | EVENT | +3 | Very Positive | 2.8961 | positive | N/A | — | 4 |
| 8 | Court case | EVENT | +3 | Very Positive | 2.8530 | positive | N/A | — | 1 |
| 9 | Mustapha Sakmud | PERSON | +3 | Very Positive | 2.7372 | positive | N/A | — | 2 |
| 10 | Venezuela | LOCATION | -3 | Very Negative | -2.7142 | negative | N/A | — | 4 |
| 11 | Penampang | LOCATION | -3 | Very Negative | -2.6997 | negative | N/A | — | 5 |
| 12 | Onn Hafiz 56-seats solo bid | CONCEPT | +3 | Very Positive | 2.6985 | positive | N/A | — | 1 |
| 13 | Fahmi Fadzil | PERSON | +3 | Very Positive | 2.5993 | positive | PH | PKR | 3 |
| 14 | West Asia | LOCATION | -2 | Negative | -2.4743 | negative | N/A | — | 3 |
| 15 | green technology | CONCEPT | +3 | Very Positive | 2.4448 | positive | N/A | — | 1 |
| 16 | renewable energy | CONCEPT | +3 | Very Positive | 2.4448 | positive | N/A | — | 1 |
| 17 | DVS | ORGANIZATION | +3 | Very Positive | 2.4283 | positive | N/A | — | 4 |
| 18 | United States | LOCATION | +3 | Very Positive | 2.3722 | positive | N/A | — | 5 |
| 19 | Arrest | EVENT | -2 | Negative | -2.3327 | negative | N/A | — | 8 |
| 20 | GRS | ORGANIZATION | +3 | Very Positive | 2.2569 | positive | GRS | — | 1 |
| 21 | State Government | ORGANIZATION | +3 | Very Positive | 2.2569 | positive | N/A | — | 1 |
| 22 | Khatijah Abdullah | PERSON | +3 | Very Positive | 2.2500 | positive | N/A | — | 4 |
| 23 | artificial intelligence | CONCEPT | +2 | Positive | 2.1096 | positive | N/A | — | 2 |
| 24 | Strait of Hormuz | LOCATION | -2 | Negative | -2.0879 | negative | N/A | — | 3 |
| 25 | Indonesia | LOCATION | -2 | Negative | -2.0645 | negative | N/A | — | 10 |
| 26 | Charged | EVENT | -2 | Negative | -2.0612 | negative | N/A | — | 9 |
---

## Entity Sentiments by Type

### PERSON

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Mustapha Sakmud | +3 | Very Positive | 0.7430 | 2.7372 | ⚠️ | 2 | — | — | ✚ |
| Fahmi Fadzil | +3 | Very Positive | 0.7088 | 2.5993 | ⚠️ | 3 | PH | PKR | ✚ |
| Khatijah Abdullah | +3 | Very Positive | 0.6222 | 2.2500 | ⚠️ | 4 | — | — | ✚ |
| Steven Sim | +2 | Positive | 0.3724 | 1.2425 |  | 1 | PH | DAP | ✚ |
| Rajeentheran Suntheralingam | +2 | Positive | 0.3671 | 1.2211 |  | 4 | — | — | ✚ |
| Jalaluddin Abdul Rahman | +1 | Slightly Positive | 0.2012 | 0.5520 |  | 8 | BN | UMNO |  |
| Datuk Seri | +1 | Slightly Positive | 0.1688 | 0.4213 |  | 3 | — | — | ✚ |
| Mohamad Hasan | +1 | Slightly Positive | 0.1560 | 0.3697 |  | 8 | BN | UMNO |  |
| Anwar Ibrahim | +1 | Slightly Positive | 0.1018 | 0.1510 |  | 30 | PH | PKR |  |
| Aminuddin Harun | +0 | Neutral | 0.0529 | -0.0462 |  | 15 | PH | PKR |  |
| Ahmad Zahid Hamidi | +0 | Neutral | 0.0284 | -0.1450 |  | 12 | BN | UMNO |  |
| Khairy Jamaluddin | +0 | Neutral | 0.0183 | -0.1857 |  | 10 | BN | UMNO |  |
| Datuk | +0 | Neutral | 0.0112 | -0.2144 |  | 12 | — | — | ✚ |
| Tun | +0 | Neutral | 0.0021 | -0.2511 |  | 30 | — | — | ✚ |
| Ab Rauf Yusoh | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | BN | UMNO |  |
| Hassan Abdul Karim | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | PH | PKR |  |
| Mahathir Mohamad | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | PEJUANG | Pejuang |  |
| Mohd Ghazali Sabari | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | — | — |  |
| Muhyiddin Yassin | +0 | Neutral | 0.0000 | -0.2595 |  | 5 | PN | BERSATU |  |
| Nik Nazmi Nik Ahmad | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | PH | PKR |  |
| Nurul Izzah Anwar | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | PH | PKR |  |
| Rafizi Ramli | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | PH | PKR |  |
| Sim Kui Hian | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | GPS | GPS |  |
| Tiong King Sing | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | GPS | GPS |  |
| Abdul Razak | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | — | — | ✚ |
| Mohd Faizal Ramli | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | — | — | ✚ |
| Razali Abu Samah | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | — | — | ✚ |
| Tun Faisal Ismail Aziz | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | BN | UMNO | ✚ |
| Abdul Hadi Awang | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | PN | PAS | ✚ |
| Najib Razak | +0 | Neutral | 0.0000 | -0.2595 |  | 8 | BN | UMNO | ✚ |
| Onn Hafiz | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | BN | UMNO | ✚ |
| Syed Saddiq | +0 | Neutral | 0.0000 | -0.2595 |  | 22 | PH | MUDA | ✚ |
| Sanusi | +0 | Neutral | 0.0000 | -0.2595 |  | 3 | PN | PAS | ✚ |
| Mohamad Sabu | -1 | Slightly Negative | -0.1537 | -0.8795 |  | 5 | PH | AMANAH | ✚ |
| Hajiji Noor | -1 | Slightly Negative | -0.2023 | -1.0755 |  | 3 | GRS | GRS | ✚ |
| Azanna Ahmad Kamar | -3 | Very Negative | -0.7154 | -3.1450 | ⚠️ | 4 | PN | BERSATU | ✚ |
### ORGANIZATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Daily Express | +3 | Very Positive | 0.8020 | 2.9752 | ⚠️ | 3 | — | — | ✚ |
| DVS | +3 | Very Positive | 0.6664 | 2.4283 | ⚠️ | 4 | — | — | ✚ |
| GRS | +3 | Very Positive | 0.6239 | 2.2569 | ⚠️ | 1 | GRS | — |  |
| State Government | +3 | Very Positive | 0.6239 | 2.2569 | ⚠️ | 1 | — | — | ✚ |
| Keadilan | +2 | Positive | 0.5399 | 1.9181 |  | 4 | — | — | ✚ |
| Suara Keadilan | +2 | Positive | 0.5399 | 1.9181 |  | 1 | — | — | ✚ |
| KWSP | +2 | Positive | 0.5343 | 1.8955 |  | 4 | — | — | ✚ |
| JPA | +2 | Positive | 0.4408 | 1.5184 |  | 6 | — | — | ✚ |
| PRS | +2 | Positive | 0.3918 | 1.3207 |  | 2 | — | — | ✚ |
| Grab | +2 | Positive | 0.3227 | 1.0420 |  | 3 | — | — | ✚ |
| The Star | +1 | Slightly Positive | 0.2773 | 0.8589 |  | 3 | — | — | ✚ |
| ASEAN | +1 | Slightly Positive | 0.2772 | 0.8585 |  | 21 | — | — |  |
| Malaysian Chinese Association | +1 | Slightly Positive | 0.2612 | 0.7940 |  | 5 | BN | MCA |  |
| AirBorneo | +1 | Slightly Positive | 0.2566 | 0.7754 |  | 4 | — | — | ✚ |
| Cabinet | +1 | Slightly Positive | 0.2477 | 0.7395 |  | 3 | — | — | ✚ |
| Malaysian Indian Congress | +1 | Slightly Positive | 0.2052 | 0.5681 |  | 18 | BN | MIC |  |
| Media Mulia | +1 | Slightly Positive | 0.1555 | 0.3676 |  | 6 | — | — | ✚ |
| UN | +1 | Slightly Positive | 0.1140 | 0.2003 |  | 30 | — | — | ✚ |
| Pakatan Harapan | +0 | Neutral | 0.0990 | 0.1398 |  | 30 | PH | — |  |
| Parti Islam Se-Malaysia | +0 | Neutral | 0.0977 | 0.1345 |  | 30 | PN | PAS |  |
| Google | +0 | Neutral | 0.0813 | 0.0684 |  | 23 | — | — | ✚ |
| Bernama | +0 | Neutral | 0.0656 | 0.0050 |  | 13 | — | — | ✚ |
| DUN | +0 | Neutral | 0.0567 | -0.0309 |  | 30 | — | — | ✚ |
| Apple | +0 | Neutral | 0.0453 | -0.0768 |  | 13 | — | — | ✚ |
| Barisan Nasional | +0 | Neutral | 0.0430 | -0.0861 |  | 30 | BN | — |  |
| TikTok | +0 | Neutral | 0.0415 | -0.0922 |  | 30 | — | — | ✚ |
| MOH | +0 | Neutral | 0.0391 | -0.1018 |  | 22 | — | — | ✚ |
| IMU | +0 | Neutral | 0.0320 | -0.1305 |  | 9 | — | — | ✚ |
| FIFA | +0 | Neutral | 0.0198 | -0.1797 |  | 19 | — | — | ✚ |
| NST | +0 | Neutral | 0.0153 | -0.1978 |  | 30 | — | — | ✚ |
| Perikatan Nasional | +0 | Neutral | 0.0126 | -0.2087 |  | 30 | PN | — |  |
| Democratic Action Party | +0 | Neutral | 0.0124 | -0.2095 |  | 30 | PH | DAP |  |
| PRN | +0 | Neutral | 0.0123 | -0.2099 |  | 30 | — | — | ✚ |
| Suruhanjaya Pilihan Raya | +0 | Neutral | 0.0090 | -0.2232 |  | 12 | — | — |  |
| Gabungan Parti Sarawak | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | GPS | — |  |
| HAWANA | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | — | — |  |
| Malaysia United Democratic Alliance | +0 | Neutral | 0.0000 | -0.2595 |  | 16 | PH | MUDA |  |
| Ministry of Finance | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | — | — |  |
| Ministry of Home Affairs | +0 | Neutral | 0.0000 | -0.2595 |  | 6 | — | — |  |
| Parti Amanah Negara | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | PH | AMANAH |  |
| Parti Bersama | +0 | Neutral | 0.0000 | -0.2595 |  | 17 | BERSAMA | BERSAMA |  |
| Parti Keadilan Rakyat | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | PH | PKR |  |
| Parti Warisan | +0 | Neutral | 0.0000 | -0.2595 |  | 5 | WARISAN | Warisan |  |
| Pejuang | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | PEJUANG | — |  |
| Suruhanjaya Pencegahan Rasuah Malaysia | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — |  |
| AFP | +0 | Neutral | 0.0000 | -0.2595 |  | 8 | — | — | ✚ |
| BURSA | +0 | Neutral | 0.0000 | -0.2595 |  | 7 | — | — | ✚ |
| Borneo Post | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| Bursa Malaysia | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | — | — | ✚ |
| BuzzKini | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| CodeBlue | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| KLK | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| KPKM | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| Kementerian Kesihatan | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Kementerian Kesihatan Malaysia | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Kosmo | +0 | Neutral | 0.0000 | -0.2595 |  | 6 | — | — | ✚ |
| MCMC | +0 | Neutral | 0.0000 | -0.2595 |  | 7 | — | — | ✚ |
| Malay Mail | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| MalaysiaGazette | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| Malaysiakini | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| NGO | +0 | Neutral | 0.0000 | -0.2595 |  | 21 | — | — | ✚ |
| Perodua | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | — | — | ✚ |
| Sinar Harian | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| Spotify | +0 | Neutral | 0.0000 | -0.2595 |  | 6 | — | — | ✚ |
| mStar | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| Boeing | +0 | Neutral | -0.0030 | -0.2716 |  | 4 | — | — | ✚ |
| Parti Pribumi Bersatu Malaysia | +0 | Neutral | -0.0530 | -0.4733 |  | 12 | PN | BERSATU |  |
| United Malays National Organisation | +0 | Neutral | -0.0704 | -0.5435 |  | 19 | BN | UMNO |  |
| Tropicana | +0 | Neutral | -0.0757 | -0.5649 |  | 3 | — | — | ✚ |
| Vulcan Post | +0 | Neutral | -0.0846 | -0.6008 |  | 4 | — | — | ✚ |
| The Edge Malaysia | -1 | Slightly Negative | -0.1133 | -0.7165 |  | 3 | — | — | ✚ |
| Parliament | -1 | Slightly Negative | -0.1940 | -1.0420 |  | 2 | — | — | ✚ |
### LOCATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| South Korea | +3 | Very Positive | 0.8516 | 3.1753 | ⚠️ | 1 | — | — | ✚ |
| United States | +3 | Very Positive | 0.6525 | 2.3722 | ⚠️ | 5 | — | — | ✚ |
| Germany | +2 | Positive | 0.5241 | 1.8543 |  | 4 | — | — | ✚ |
| Thailand | +2 | Positive | 0.4629 | 1.6075 |  | 2 | — | — | ✚ |
| N9 Polls | +2 | Positive | 0.4034 | 1.3675 |  | 4 | — | — | ✚ |
| Tambunan | +2 | Positive | 0.3929 | 1.3252 |  | 4 | — | — | ✚ |
| Penang | +2 | Positive | 0.3778 | 1.2643 |  | 6 | — | — |  |
| Vietnam | +1 | Slightly Positive | 0.2992 | 0.9472 |  | 2 | — | — | ✚ |
| Kuching | +1 | Slightly Positive | 0.2974 | 0.9400 |  | 5 | — | — |  |
| Spain | +1 | Slightly Positive | 0.1755 | 0.4483 |  | 23 | — | — | ✚ |
| Ipoh | +1 | Slightly Positive | 0.1702 | 0.4269 |  | 4 | — | — | ✚ |
| Kedah | +1 | Slightly Positive | 0.1289 | 0.2604 |  | 14 | — | — | ✚ |
| Japan | +1 | Slightly Positive | 0.1155 | 0.2063 |  | 6 | — | — | ✚ |
| Banting | +1 | Slightly Positive | 0.1096 | 0.1825 |  | 4 | — | — | ✚ |
| Singapore | +1 | Slightly Positive | 0.1033 | 0.1571 |  | 16 | — | — | ✚ |
| Argentina | +0 | Neutral | 0.0931 | 0.1160 |  | 24 | — | — | ✚ |
| Malaysia | +0 | Neutral | 0.0907 | 0.1063 |  | 30 | — | — | ✚ |
| Negeri Sembilan | +0 | Neutral | 0.0891 | 0.0998 |  | 30 | — | — |  |
| France | +0 | Neutral | 0.0860 | 0.0873 |  | 17 | — | — | ✚ |
| China | +0 | Neutral | 0.0857 | 0.0861 |  | 25 | — | — | ✚ |
| Ranau | +0 | Neutral | 0.0837 | 0.0780 |  | 7 | — | — | ✚ |
| India | +0 | Neutral | 0.0534 | -0.0442 |  | 15 | — | — | ✚ |
| US | +0 | Neutral | 0.0527 | -0.0470 |  | 30 | — | — | ✚ |
| Silicon Valley | +0 | Neutral | 0.0387 | -0.1035 |  | 2 | — | — | ✚ |
| UK | +0 | Neutral | 0.0244 | -0.1611 |  | 30 | — | — | ✚ |
| Parliament House | +0 | Neutral | 0.0218 | -0.1716 |  | 8 | — | — |  |
| Kota Kinabalu | +0 | Neutral | 0.0195 | -0.1809 |  | 7 | — | — |  |
| Johor | +0 | Neutral | 0.0162 | -0.1942 |  | 25 | — | — |  |
| Melaka | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — |  |
| N14 | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | — | — |  |
| Pasir Gudang | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | — | — |  |
| Perak | +0 | Neutral | 0.0000 | -0.2595 |  | 7 | — | — |  |
| Pertang | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — |  |
| Rantau | +0 | Neutral | 0.0000 | -0.2595 |  | 6 | — | — |  |
| Selangor | +0 | Neutral | 0.0000 | -0.2595 |  | 12 | — | — |  |
| Batu Pahat | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Beaufort | +0 | Neutral | 0.0000 | -0.2595 |  | 3 | — | — | ✚ |
| Beluran | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Betong | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Bintulu | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Brunei | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | — | — | ✚ |
| Bukit Gasing | +0 | Neutral | 0.0000 | -0.2595 |  | 3 | — | — | ✚ |
| Cameron Highlands | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Dungun | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Gombak | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Hulu Selangor | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Kemaman | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Keningau | +0 | Neutral | 0.0000 | -0.2595 |  | 8 | — | — | ✚ |
| Kota Bharu | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Kota Tinggi | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | — | — | ✚ |
| Kuala Selangor | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Kuala Terengganu | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | — | — | ✚ |
| Kuantan | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| Kudat | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | — | — | ✚ |
| Kulai | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Kunak | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Lahad Datu | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | — | — | ✚ |
| Limbang | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Lipis | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Maran | +0 | Neutral | 0.0000 | -0.2595 |  | 3 | — | — | ✚ |
| Mersing | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Muar | +0 | Neutral | 0.0000 | -0.2595 |  | 13 | — | — | ✚ |
| Pahang | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| Pasir Puteh | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Petaling Jaya | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | — | — | ✚ |
| Pontian | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Putatan | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Putrajaya | +0 | Neutral | 0.0000 | -0.2595 |  | 7 | — | — | ✚ |
| Rompin | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Samarahan | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| Sandakan | +0 | Neutral | 0.0000 | -0.2595 |  | 5 | — | — | ✚ |
| Sarikei | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Segamat | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Semporna | +0 | Neutral | 0.0000 | -0.2595 |  | 5 | — | — | ✚ |
| Sepang | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Seremban | +0 | Neutral | 0.0000 | -0.2595 |  | 5 | — | — | ✚ |
| Serian | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| Shah Alam | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| Sibu | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| Tawau | +0 | Neutral | 0.0000 | -0.2595 |  | 6 | — | — | ✚ |
| Tenom | +0 | Neutral | 0.0000 | -0.2595 |  | 5 | — | — | ✚ |
| Kelantan | +0 | Neutral | -0.0081 | -0.2922 |  | 10 | — | — | ✚ |
| Sabah | +0 | Neutral | -0.0106 | -0.3023 |  | 14 | — | — |  |
| Sarawak | +0 | Neutral | -0.0187 | -0.3350 |  | 22 | — | — |  |
| England | +0 | Neutral | -0.0427 | -0.4318 |  | 15 | — | — | ✚ |
| Kuala Lumpur | +0 | Neutral | -0.0917 | -0.6294 |  | 30 | — | — |  |
| Perlis | +0 | Neutral | -0.0986 | -0.6572 |  | 12 | — | — | ✚ |
| Terengganu | -1 | Slightly Negative | -0.1261 | -0.7682 |  | 10 | — | — | ✚ |
| Korea | -1 | Slightly Negative | -0.1678 | -0.9363 |  | 8 | — | — | ✚ |
| Linggi | -1 | Slightly Negative | -0.1839 | -1.0013 |  | 8 | — | — |  |
| Russia | -1 | Slightly Negative | -0.2143 | -1.1239 |  | 8 | — | — | ✚ |
| Iran | -1 | Slightly Negative | -0.2271 | -1.1755 |  | 30 | — | — | ✚ |
| Miri | -1 | Slightly Negative | -0.2585 | -1.3022 |  | 5 | — | — | ✚ |
| Klang | -1 | Slightly Negative | -0.2588 | -1.3034 |  | 4 | — | — | ✚ |
| Middle East | -2 | Negative | -0.3182 | -1.5430 |  | 1 | — | — | ✚ |
| Indonesia | -2 | Negative | -0.4475 | -2.0645 | ⚠️ | 10 | — | — | ✚ |
| Strait of Hormuz | -2 | Negative | -0.4533 | -2.0879 | ⚠️ | 3 | — | — | ✚ |
| West Asia | -2 | Negative | -0.5491 | -2.4743 | ⚠️ | 3 | — | — | ✚ |
| Penampang | -3 | Very Negative | -0.6050 | -2.6997 | ⚠️ | 5 | — | — | ✚ |
| Venezuela | -3 | Very Negative | -0.6086 | -2.7142 | ⚠️ | 4 | — | — | ✚ |
| Kangar | -3 | Very Negative | -0.6580 | -2.9135 | ⚠️ | 5 | — | — | ✚ |
| Wall Street | -3 | Very Negative | -0.7365 | -3.2301 | ⚠️ | 2 | — | — | ✚ |
### EVENT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| WAN IFRA ASIA MEDIA AWARDS 2025 | +3 | Very Positive | 0.9187 | 3.4459 | ⚠️ | 2 | — | — | ✚ |
| Trial | +3 | Very Positive | 0.7824 | 2.8961 | ⚠️ | 4 | — | — | ✚ |
| Court case | +3 | Very Positive | 0.7717 | 2.8530 | ⚠️ | 1 | — | — | ✚ |
| Hearing | +2 | Positive | 0.5522 | 1.9677 |  | 4 | — | — | ✚ |
| Appeal | +2 | Positive | 0.4619 | 1.6035 |  | 3 | — | — | ✚ |
| World Cup | +2 | Positive | 0.3518 | 1.1594 |  | 30 | — | — | ✚ |
| GE16 | +2 | Positive | 0.3255 | 1.0533 |  | 5 | — | — | ✚ |
| Investigation | +1 | Slightly Positive | 0.2712 | 0.8343 |  | 5 | — | — | ✚ |
| campaign | +1 | Slightly Positive | 0.1300 | 0.2648 |  | 24 | — | — |  |
| 2026 Elections | +1 | Slightly Positive | 0.1241 | 0.2410 |  | 3 | — | — | ✚ |
| state election | +0 | Neutral | 0.0747 | 0.0417 |  | 8 | — | — | ✚ |
| Probe | +0 | Neutral | 0.0738 | 0.0381 |  | 13 | — | — | ✚ |
| pilihan raya | +0 | Neutral | 0.0468 | -0.0708 |  | 9 | — | — | ✚ |
| Negeri Sembilan State Election 2026 | +0 | Neutral | 0.0191 | -0.1825 |  | 23 | — | — |  |
| BN Candidate Announcement (NS) | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | — | — |  |
| ceramah | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | — | — |  |
| HAWANA X TM Media Event | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | — | — |  |
| Johor State Election | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | — | — |  |
| kempen | +0 | Neutral | 0.0000 | -0.2595 |  | 16 | — | — |  |
| Sarawak State Election 2026 | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | — | — |  |
| PRN Negeri | +0 | Neutral | 0.0000 | -0.2595 |  | 17 | — | — | ✚ |
| Piala Dunia | +0 | Neutral | 0.0000 | -0.2595 |  | 30 | — | — | ✚ |
| Pilihan Raya Negeri Johor | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| election | +0 | Neutral | 0.0000 | -0.2595 |  | 16 | — | — | ✚ |
| pilihan raya negeri | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| majlis | +0 | Neutral | -0.0736 | -0.5564 |  | 4 | — | — |  |
| rally | +0 | Neutral | -0.0757 | -0.5649 |  | 5 | — | — |  |
| event | -1 | Slightly Negative | -0.1081 | -0.6956 |  | 16 | — | — |  |
| walkabout | -1 | Slightly Negative | -0.1213 | -0.7488 |  | 5 | — | — |  |
| Summit | -1 | Slightly Negative | -0.2532 | -1.2808 |  | 5 | — | — | ✚ |
| Charged | -2 | Negative | -0.4467 | -2.0612 | ⚠️ | 9 | — | — | ✚ |
| Arrest | -2 | Negative | -0.5140 | -2.3327 | ⚠️ | 8 | — | — | ✚ |
### CONCEPT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Onn Hafiz 56-seats solo bid | +3 | Very Positive | 0.7334 | 2.6985 | ⚠️ | 1 | — | — |  |
| green technology | +3 | Very Positive | 0.6705 | 2.4448 | ⚠️ | 1 | — | — | ✚ |
| renewable energy | +3 | Very Positive | 0.6705 | 2.4448 | ⚠️ | 1 | — | — | ✚ |
| artificial intelligence | +2 | Positive | 0.5874 | 2.1096 | ⚠️ | 2 | — | — | ✚ |
| mandate | +2 | Positive | 0.4890 | 1.7128 |  | 3 | — | — | ✚ |
| opposition | +2 | Positive | 0.3659 | 1.2163 |  | 4 | — | — | ✚ |
| copyright | +2 | Positive | 0.3130 | 1.0029 |  | 18 | — | — | ✚ |
| oil and gas | +1 | Slightly Positive | 0.2500 | 0.7488 |  | 1 | — | — | ✚ |
| Super El Nino food security | +1 | Slightly Positive | 0.2229 | 0.6395 |  | 0 | — | — |  |
| Wealth tax | +1 | Slightly Positive | 0.1482 | 0.3382 |  | 0 | — | — |  |
| Subsidies & welfare aid | +1 | Slightly Positive | 0.1239 | 0.2402 |  | 13 | — | — |  |
| perpaduan | +0 | Neutral | 0.0931 | 0.1160 |  | 11 | — | — | ✚ |
| MADANI government | +0 | Neutral | 0.0466 | -0.0716 |  | 22 | — | — |  |
| Bersatu own logo in N9 | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | — | — |  |
| Cost of living | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — |  |
| Service tax | +0 | Neutral | 0.0000 | -0.2595 |  | 3 | — | — |  |
| Third force movement | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | — | — |  |
| UEC recognition | +0 | Neutral | 0.0000 | -0.2595 |  | 0 | — | — |  |
| Reformasi | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| TVET | +0 | Neutral | 0.0000 | -0.2595 |  | 4 | — | — | ✚ |
| fertiliser price | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | — | — | ✚ |
| grassroots | +0 | Neutral | 0.0000 | -0.2595 |  | 1 | — | — | ✚ |
| pork supply | +0 | Neutral | 0.0000 | -0.2595 |  | 2 | — | — | ✚ |
| AI | +0 | Neutral | -0.0717 | -0.5487 |  | 30 | — | — | ✚ |
| water supply | -2 | Negative | -0.3612 | -1.7164 |  | 1 | — | — | ✚ |
---

## Methodology

1. **Entity Source:** Loaded from the 2026-07-20T000706Z extraction roster (255 Phase-1 entity names) plus the 78 canonical entities from the per-entity index. Roster names were merged into canonical entities by normalized name/alias matching (honorific-stripped); unmerged names were added as new entities (189 new).
2. **Context Extraction:** For each entity, search variants (canonical name + aliases + roster matches) were located in the 2026-07-20 raw source collection (24 sources, 24 processed, ~731765 chars). A context window (~140+170 chars) was extracted around each mention (markdown stripped, de-duplicated, capped at 30/entity).
3. **Sentiment Scoring:** Applied VADER to each context snippet; entity sentiment = mean compound across snippets.
4. **Score Mapping:** VADER compound (-1..+1) → 7-point Likert (-3..+3): +3 ≥0.6, +2 ≥0.3, +1 ≥0.1, 0 (-0.1..0.1), -1 >-0.3, -2 >-0.6, -3 ≤-0.6.
5. **Anomaly Detection:** Z-score on raw compound vs overall mean/std; flagged when |z| > 2.
6. **Coalition/Party Aggregation:** Persons + political-party/coalition orgs mapped via per-entity metadata and affiliation maps (FIGURE_AFFILIATIONS, ORG_TO_COALITION, analyst-extended NEW_FIGURE_AFFIL).

---

*Report generated by OpenCLaw Sentiment Analysis Pipeline (sentiment-analysis skill)*
*VADER: Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.*

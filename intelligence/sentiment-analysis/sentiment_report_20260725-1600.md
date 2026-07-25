# Sentiment Analysis Report

**Classification:** TLP:AMBER
**Generated:** 2026-07-25 16:00 +08
**Report Date:** 2026-07-25
**Report Timestamp:** 2026-07-25 16:00 +08
**Extraction ID:** ext_20260725_1400_phase1
**Extraction Source:** 2026-07-25T14:00:00+08:00
**Collection Cycle:** 2026-07-25T000456Z
**Source Count:** 24
**Analysis Method:** VADER Sentiment Analysis on fresh context snippets extracted from 2026-07-25 raw collection
**Score Range:** -3 (very negative) to +3 (very positive)
**Anomaly Threshold:** |z-score| > 2

> **Data-freshness note:** The 2026-07-25 extraction produced Phase-1 entity name lists
> only; Phase-2 per-entity context files were not regenerated for this cycle. To produce a
> genuine 2026-07-25 sentiment signal, context snippets were extracted directly from the
> 2026-07-25 raw source collection and scored with VADER. Coalition/party metadata sourced
> from the canonical per-entity files (2026-07-16 Phase-2 set) plus an analyst-extended
> affiliation map for newly-extracted figures.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Roster Entities (Phase-1 names) | 274 |
| Analysis Entities (merged) | 283 |
| Canonical Entities (from index) | 78 |
| New Entities (this cycle) | 205 |
| Roster Names Matched to Canonical | 54 |
| Sources Processed | 24 |
| Entities with Context | 260 |
| Entities without Context (fallback) | 23 |
| Overall Mean Sentiment | +0.085 |
| Overall Std Deviation | 0.975 |
| Overall Median Sentiment | +0.000 |
| Overall Raw Mean | 0.0235 |
| Overall Raw Std Dev | 0.2216 |
| Sentiment Range | [-3, +3] |
| Positive Entities | 53 |
| Neutral Entities | 194 |
| Negative Entities | 36 |
| Anomalies Detected | 23 |
| Coalitions Analyzed | 8 |
| Parties Analyzed | 16 |

### Sentiment Distribution

```
Positive (53)  █████████████████████████████████████████████████████
Neutral  (194)  ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
Negative (36)  ████████████████████████████████████
```

---

## Coalition Aggregate Sentiment

| Coalition | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range |
|-----------|:-:|------|:----------:|:-------:|:--------:|:-----:|
| GPS | +2 | Positive | 0.3130 | 0.3126 | 5 | [0.000, 0.726] |
| GRS | +1 | Slightly Positive | 0.2294 | 0.3244 | 2 | [0.000, 0.459] |
| PH | +0 | Neutral | 0.0592 | 0.1380 | 17 | [-0.073, 0.540] |
| BN | +0 | Neutral | 0.0511 | 0.1171 | 12 | [-0.059, 0.354] |
| PN | +0 | Neutral | 0.0498 | 0.0762 | 8 | [0.000, 0.211] |
| BERSAMA | +0 | Neutral | 0.0226 | 0.0000 | 1 | [0.023, 0.023] |
| PEJUANG | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] |
| WARISAN | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
### Coalition Entities
- **GPS** (+2, Positive): Sim Kui Hian, Tiong King Sing, Wilson Ugak Kumbong, Gabungan Parti Sarawak, PRS
- **GRS** (+1, Slightly Positive): Hajiji Noor, GRS
- **PH** (+0, Neutral): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Chong Zhemin, Anthony Loke, Dzulkefly Ahmad, Mohamad Sabu, Syed Saddiq, Democratic Action Party, Malaysia United Democratic Alliance, Pakatan Harapan, Parti Amanah Negara, Parti Keadilan Rakyat, Keadilan
- **BN** (+0, Neutral): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Jalaluddin Alias, Najib Razak, Onn Hafiz, Barisan Nasional, Malaysian Chinese Association, Malaysian Indian Congress, United Malays National Organisation
- **PN** (+0, Neutral): Muhyiddin Yassin, Ahmad Samsuri Mokhtar, Abdul Hadi Awang, Sanusi, Tuan Ibrahim, Parti Islam Se-Malaysia, Parti Pribumi Bersatu Malaysia, Perikatan Nasional
- **BERSAMA** (+0, Neutral): Parti Bersama
- **PEJUANG** (+0, Neutral): Mahathir Mohamad, Pejuang
- **WARISAN** (+0, Neutral): Parti Warisan

---

## Party Aggregate Sentiment

| Party | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range | Coalition |
|-------|:-:|------|:----------:|:-------:|:--------:|:-----:|:---------:|
| Keadilan | +2 | Positive | 0.5399 | 0.0000 | 1 | [0.540, 0.540] | — |
| GRS | +2 | Positive | 0.4588 | 0.0000 | 1 | [0.459, 0.459] | GRS |
| PRS | +2 | Positive | 0.3918 | 0.0000 | 1 | [0.392, 0.392] | GPS |
| GPS | +2 | Positive | 0.3910 | 0.3663 | 3 | [0.000, 0.726] | GPS |
| MIC | +0 | Neutral | 0.0846 | 0.0000 | 1 | [0.085, 0.085] | BN |
| PAS | +0 | Neutral | 0.0774 | 0.0872 | 5 | [0.000, 0.211] | PN |
| AMANAH | +0 | Neutral | 0.0715 | 0.0956 | 3 | [0.000, 0.180] | PH |
| UMNO | +0 | Neutral | 0.0664 | 0.1283 | 9 | [-0.037, 0.354] | BN |
| PKR | +0 | Neutral | 0.0237 | 0.0722 | 7 | [-0.073, 0.144] | PH |
| BERSAMA | +0 | Neutral | 0.0226 | 0.0000 | 1 | [0.023, 0.023] | BERSAMA |
| DAP | +0 | Neutral | 0.0170 | 0.0295 | 3 | [0.000, 0.051] | PH |
| BERSATU | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] | PN |
| MUDA | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] | PH |
| Pejuang | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | PEJUANG |
| Warisan | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | WARISAN |
| MCA | +0 | Neutral | -0.0592 | 0.0000 | 1 | [-0.059, -0.059] | BN |
### Party Entities
- **Keadilan** (+2, Positive, → —): Keadilan
- **GRS** (+2, Positive, → GRS): Hajiji Noor
- **PRS** (+2, Positive, → GPS): PRS
- **GPS** (+2, Positive, → GPS): Sim Kui Hian, Tiong King Sing, Wilson Ugak Kumbong
- **MIC** (+0, Neutral, → BN): Malaysian Indian Congress
- **PAS** (+0, Neutral, → PN): Ahmad Samsuri Mokhtar, Abdul Hadi Awang, Sanusi, Tuan Ibrahim, Parti Islam Se-Malaysia
- **AMANAH** (+0, Neutral, → PH): Dzulkefly Ahmad, Mohamad Sabu, Parti Amanah Negara
- **UMNO** (+0, Neutral, → BN): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Jalaluddin Alias, Najib Razak, Onn Hafiz, United Malays National Organisation
- **PKR** (+0, Neutral, → PH): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Parti Keadilan Rakyat
- **BERSAMA** (+0, Neutral, → BERSAMA): Parti Bersama
- **DAP** (+0, Neutral, → PH): Chong Zhemin, Anthony Loke, Democratic Action Party
- **BERSATU** (+0, Neutral, → PN): Muhyiddin Yassin, Parti Pribumi Bersatu Malaysia
- **MUDA** (+0, Neutral, → PH): Syed Saddiq, Malaysia United Democratic Alliance
- **Pejuang** (+0, Neutral, → PEJUANG): Mahathir Mohamad
- **Warisan** (+0, Neutral, → WARISAN): Parti Warisan
- **MCA** (+0, Neutral, → BN): Malaysian Chinese Association

---

## Sentiment Anomalies (|z-score| > 2)

**23 anomalies detected.**

| # | Entity | Type | Score | Label | Z-Score | Direction | Coalition | Party | Contexts |
|---|--------|------|:-----:|-------|:-------:|:---------:|-----------|:------:|:--------:|
| 1 | Bursa Malaysia | ORGANIZATION | -3 | Very Negative | -4.1773 | negative | N/A | — | 2 |
| 2 | WAN IFRA ASIA MEDIA AWARDS 2025 | EVENT | +3 | Very Positive | 4.0404 | positive | N/A | — | 2 |
| 3 | Germany | LOCATION | -3 | Very Negative | -3.2760 | negative | N/A | — | 4 |
| 4 | The Star | ORGANIZATION | +3 | Very Positive | 3.2474 | positive | N/A | — | 1 |
| 5 | Onn Hafiz 56-seats solo bid | CONCEPT | +3 | Very Positive | 3.2041 | positive | N/A | — | 1 |
| 6 | Wilson Ugak Kumbong | PERSON | +3 | Very Positive | 3.1720 | positive | GPS | GPS | 2 |
| 7 | West Asia | LOCATION | -3 | Very Negative | -2.9944 | negative | N/A | — | 7 |
| 8 | gig economy | CONCEPT | -3 | Very Negative | -2.9804 | negative | N/A | — | 2 |
| 9 | Parliament | ORGANIZATION | -3 | Very Negative | -2.9763 | negative | N/A | — | 1 |
| 10 | Parliament House | LOCATION | -3 | Very Negative | -2.9763 | negative | N/A | — | 1 |
| 11 | green technology | CONCEPT | +3 | Very Positive | 2.9202 | positive | N/A | — | 1 |
| 12 | renewable energy | CONCEPT | +3 | Very Positive | 2.9202 | positive | N/A | — | 1 |
| 13 | DVS | ORGANIZATION | +3 | Very Positive | 2.9017 | positive | N/A | — | 4 |
| 14 | democratic power | CONCEPT | -3 | Very Negative | -2.8224 | negative | N/A | — | 2 |
| 15 | Charged | EVENT | -2 | Negative | -2.5968 | negative | N/A | — | 5 |
| 16 | United States | LOCATION | +2 | Positive | 2.5325 | positive | N/A | — | 4 |
| 17 | Izzat Shameer | PERSON | +2 | Positive | 2.5320 | positive | N/A | — | 7 |
| 18 | Spain | LOCATION | -2 | Negative | -2.4217 | negative | N/A | — | 8 |
| 19 | Keadilan | ORGANIZATION | +2 | Positive | 2.3308 | positive | PH | Keadilan | 4 |
| 20 | Suara Keadilan | ORGANIZATION | +2 | Positive | 2.3308 | positive | N/A | — | 1 |
| 21 | Argentina | LOCATION | -2 | Negative | -2.1761 | negative | N/A | — | 6 |
| 22 | nominated assemblymen | CONCEPT | -2 | Negative | -2.1536 | negative | N/A | — | 3 |
| 23 | Investigation | EVENT | +2 | Positive | 2.0360 | positive | N/A | — | 4 |
---

## Entity Sentiments by Type

### PERSON

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Wilson Ugak Kumbong | +3 | Very Positive | 0.7263 | 3.1720 | ⚠️ | 2 | GPS | GPS | ✚ |
| Izzat Shameer | +2 | Positive | 0.5845 | 2.5320 | ⚠️ | 7 | — | — | ✚ |
| Hajiji Noor | +2 | Positive | 0.4588 | 1.9647 |  | 2 | GRS | GRS | ✚ |
| Tiong King Sing | +2 | Positive | 0.4468 | 1.9106 |  | 3 | GPS | GPS |  |
| Firdausi Suffian | +2 | Positive | 0.3612 | 1.5242 |  | 2 | — | — | ✚ |
| Onn Hafiz | +2 | Positive | 0.3539 | 1.4913 |  | 3 | BN | UMNO | ✚ |
| Predeep Nambiar | +2 | Positive | 0.3185 | 1.3315 |  | 2 | — | — | ✚ |
| Rajeentheran Suntheralingam | +1 | Slightly Positive | 0.2654 | 1.0919 |  | 4 | — | — | ✚ |
| Abdul Hadi Awang | +1 | Slightly Positive | 0.2107 | 0.8450 |  | 2 | PN | PAS | ✚ |
| Ahmad Zahid Hamidi | +1 | Slightly Positive | 0.1922 | 0.7615 |  | 16 | BN | UMNO |  |
| Dzulkefly Ahmad | +1 | Slightly Positive | 0.1800 | 0.7065 |  | 5 | PH | AMANAH | ✚ |
| Anwar Ibrahim | +1 | Slightly Positive | 0.1440 | 0.5440 |  | 30 | PH | PKR |  |
| Tuan Ibrahim | +1 | Slightly Positive | 0.1198 | 0.4348 |  | 3 | PN | PAS | ✚ |
| Aminuddin Harun | +0 | Neutral | 0.0951 | 0.3233 |  | 18 | PH | PKR |  |
| Jalaluddin Abdul Rahman | +0 | Neutral | 0.0887 | 0.2944 |  | 16 | BN | UMNO |  |
| Mohamad Sabu | +0 | Neutral | 0.0344 | 0.0493 |  | 4 | PH | AMANAH | ✚ |
| Sanusi | +0 | Neutral | 0.0253 | 0.0083 |  | 8 | PN | PAS | ✚ |
| Ab Rauf Yusoh | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | BN | UMNO |  |
| Hassan Abdul Karim | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | PH | PKR |  |
| Khairy Jamaluddin | +0 | Neutral | 0.0000 | -0.1059 |  | 9 | BN | UMNO |  |
| Mahathir Mohamad | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | PEJUANG | Pejuang |  |
| Mohamad Hasan | +0 | Neutral | 0.0000 | -0.1059 |  | 11 | BN | UMNO |  |
| Mohd Ghazali Sabari | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | — | — |  |
| Muhyiddin Yassin | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | PN | BERSATU |  |
| Nik Nazmi Nik Ahmad | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | PH | PKR |  |
| Nurul Izzah Anwar | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | PH | PKR |  |
| Rafizi Ramli | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | PH | PKR |  |
| Sim Kui Hian | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | GPS | GPS |  |
| Abdul Razak | +0 | Neutral | 0.0000 | -0.1059 |  | 6 | — | — | ✚ |
| Chong Zhemin | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | PH | DAP | ✚ |
| Anne Muhammad | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | — | — | ✚ |
| Anthony Loke | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | PH | DAP | ✚ |
| Mohd Faizal Ramli | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | — | — | ✚ |
| Ahmad Samsuri Mokhtar | +0 | Neutral | 0.0000 | -0.1059 |  | 3 | PN | PAS | ✚ |
| Jalaluddin Alias | +0 | Neutral | 0.0000 | -0.1059 |  | 3 | BN | UMNO | ✚ |
| Sathia | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | — | — | ✚ |
| Najib Razak | +0 | Neutral | 0.0000 | -0.1059 |  | 8 | BN | UMNO | ✚ |
| Syed Saddiq | +0 | Neutral | 0.0000 | -0.1059 |  | 8 | PH | MUDA | ✚ |
| Rafie | -1 | Slightly Negative | -0.2626 | -1.2911 |  | 4 | — | — | ✚ |
### ORGANIZATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| The Star | +3 | Very Positive | 0.7430 | 3.2474 | ⚠️ | 1 | — | — | ✚ |
| DVS | +3 | Very Positive | 0.6664 | 2.9017 | ⚠️ | 4 | — | — | ✚ |
| Keadilan | +2 | Positive | 0.5399 | 2.3308 | ⚠️ | 4 | PH | Keadilan | ✚ |
| Suara Keadilan | +2 | Positive | 0.5399 | 2.3308 | ⚠️ | 1 | — | — | ✚ |
| PRS | +2 | Positive | 0.3918 | 1.6624 |  | 2 | GPS | PRS | ✚ |
| AirBorneo | +1 | Slightly Positive | 0.2858 | 1.1840 |  | 4 | — | — | ✚ |
| Microsoft | +1 | Slightly Positive | 0.2732 | 1.1271 |  | 1 | — | — | ✚ |
| KWSP | +1 | Slightly Positive | 0.2500 | 1.0224 |  | 8 | — | — | ✚ |
| Media Mulia | +1 | Slightly Positive | 0.1555 | 0.5959 |  | 6 | — | — | ✚ |
| Perodua | +1 | Slightly Positive | 0.1235 | 0.4515 |  | 4 | — | — | ✚ |
| ASEAN | +1 | Slightly Positive | 0.1103 | 0.3919 |  | 12 | — | — |  |
| IMU | +0 | Neutral | 0.0988 | 0.3400 |  | 5 | — | — | ✚ |
| NST | +0 | Neutral | 0.0960 | 0.3273 |  | 30 | — | — | ✚ |
| Malaysian Indian Congress | +0 | Neutral | 0.0846 | 0.2759 |  | 30 | BN | MIC |  |
| DUN | +0 | Neutral | 0.0839 | 0.2727 |  | 30 | — | — | ✚ |
| Apple | +0 | Neutral | 0.0615 | 0.1716 |  | 14 | — | — | ✚ |
| Democratic Action Party | +0 | Neutral | 0.0511 | 0.1247 |  | 30 | PH | DAP |  |
| MIPP | +0 | Neutral | 0.0506 | 0.1224 |  | 4 | — | — | ✚ |
| Google | +0 | Neutral | 0.0487 | 0.1139 |  | 23 | — | — | ✚ |
| PRN | +0 | Neutral | 0.0375 | 0.0633 |  | 30 | — | — | ✚ |
| TikTok | +0 | Neutral | 0.0362 | 0.0575 |  | 30 | — | — | ✚ |
| Pakatan Harapan | +0 | Neutral | 0.0353 | 0.0534 |  | 30 | PH | — |  |
| Parti Islam Se-Malaysia | +0 | Neutral | 0.0314 | 0.0358 |  | 30 | PN | PAS |  |
| AFP | +0 | Neutral | 0.0296 | 0.0277 |  | 6 | — | — | ✚ |
| Parti Bersama | +0 | Neutral | 0.0226 | -0.0039 |  | 12 | BERSAMA | BERSAMA |  |
| Perikatan Nasional | +0 | Neutral | 0.0109 | -0.0567 |  | 30 | PN | — |  |
| Suruhanjaya Pilihan Raya | +0 | Neutral | 0.0086 | -0.0671 |  | 11 | — | — |  |
| NGO | +0 | Neutral | 0.0082 | -0.0689 |  | 30 | — | — | ✚ |
| Gabungan Parti Sarawak | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | GPS | — |  |
| GRS | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | GRS | — |  |
| HAWANA | +0 | Neutral | 0.0000 | -0.1059 |  | 7 | — | — |  |
| Malaysia United Democratic Alliance | +0 | Neutral | 0.0000 | -0.1059 |  | 12 | PH | MUDA |  |
| Ministry of Finance | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | — | — |  |
| Ministry of Home Affairs | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | — | — |  |
| Parti Amanah Negara | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | PH | AMANAH |  |
| Parti Pribumi Bersatu Malaysia | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | PN | BERSATU |  |
| Parti Warisan | +0 | Neutral | 0.0000 | -0.1059 |  | 6 | WARISAN | Warisan |  |
| Pejuang | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | PEJUANG | — |  |
| Bernama | +0 | Neutral | 0.0000 | -0.1059 |  | 10 | — | — | ✚ |
| Borneo Post | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | — | — | ✚ |
| CodeBlue | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | — | — | ✚ |
| Harian Metro | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| KLK | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Kosmo | +0 | Neutral | 0.0000 | -0.1059 |  | 8 | — | — | ✚ |
| KPKM | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | — | — | ✚ |
| Malay Mail | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | — | — | ✚ |
| MalaysiaGazette | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | — | — | ✚ |
| Malaysiakini | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | — | — | ✚ |
| MCMC | +0 | Neutral | 0.0000 | -0.1059 |  | 8 | — | — | ✚ |
| mStar | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | — | — | ✚ |
| Sabah News | +0 | Neutral | 0.0000 | -0.1059 |  | 3 | — | — | ✚ |
| Sinar Harian | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | — | — | ✚ |
| Spotify | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | — | — | ✚ |
| The Edge Malaysia | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | — | — | ✚ |
| Barisan Nasional | +0 | Neutral | -0.0100 | -0.1511 |  | 30 | BN | — |  |
| BuzzKini | +0 | Neutral | -0.0257 | -0.2219 |  | 4 | — | — | ✚ |
| UN | +0 | Neutral | -0.0303 | -0.2427 |  | 30 | — | — | ✚ |
| United Malays National Organisation | +0 | Neutral | -0.0370 | -0.2729 |  | 13 | BN | UMNO |  |
| MOH | +0 | Neutral | -0.0399 | -0.2860 |  | 13 | — | — | ✚ |
| JPA | +0 | Neutral | -0.0531 | -0.3456 |  | 13 | — | — | ✚ |
| Malaysian Chinese Association | +0 | Neutral | -0.0592 | -0.3731 |  | 5 | BN | MCA |  |
| BURSA | +0 | Neutral | -0.0603 | -0.3781 |  | 13 | — | — | ✚ |
| Parti Keadilan Rakyat | +0 | Neutral | -0.0734 | -0.4372 |  | 4 | PH | PKR |  |
| Tropicana | +0 | Neutral | -0.0820 | -0.4760 |  | 4 | — | — | ✚ |
| Vulcan Post | +0 | Neutral | -0.0846 | -0.4877 |  | 4 | — | — | ✚ |
| Suruhanjaya Pencegahan Rasuah Malaysia | -1 | Slightly Negative | -0.1591 | -0.8240 |  | 2 | — | — |  |
| UNHCR | -1 | Slightly Negative | -0.1796 | -0.9165 |  | 4 | — | — | ✚ |
| Grab | -1 | Slightly Negative | -0.1979 | -0.9991 |  | 6 | — | — | ✚ |
| Galen Centre | -1 | Slightly Negative | -0.2023 | -1.0189 |  | 2 | — | — | ✚ |
| FIFA | -1 | Slightly Negative | -0.2110 | -1.0582 |  | 9 | — | — | ✚ |
| World Cup | -1 | Slightly Negative | -0.2176 | -1.0880 |  | 12 | — | — | ✚ |
| Parliament | -3 | Very Negative | -0.6360 | -2.9763 | ⚠️ | 1 | — | — | ✚ |
| Bursa Malaysia | -3 | Very Negative | -0.9021 | -4.1773 | ⚠️ | 2 | — | — | ✚ |
### LOCATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| United States | +2 | Positive | 0.5846 | 2.5325 | ⚠️ | 4 | — | — | ✚ |
| Glasgow | +1 | Slightly Positive | 0.2933 | 1.2178 |  | 25 | — | — | ✚ |
| Thailand | +1 | Slightly Positive | 0.2931 | 1.2169 |  | 21 | — | — | ✚ |
| Negri Sembilan | +1 | Slightly Positive | 0.2615 | 1.0743 |  | 4 | — | — | ✚ |
| Chennah | +1 | Slightly Positive | 0.2462 | 1.0052 |  | 6 | — | — | ✚ |
| Linggi | +1 | Slightly Positive | 0.2311 | 0.9371 |  | 15 | — | — |  |
| Kota Kinabalu | +1 | Slightly Positive | 0.2110 | 0.8464 |  | 9 | — | — |  |
| India | +1 | Slightly Positive | 0.1888 | 0.7462 |  | 17 | — | — | ✚ |
| Petaling Jaya | +1 | Slightly Positive | 0.1619 | 0.6248 |  | 4 | — | — | ✚ |
| Japan | +1 | Slightly Positive | 0.1547 | 0.5923 |  | 6 | — | — | ✚ |
| Kota Bharu | +1 | Slightly Positive | 0.1462 | 0.5539 |  | 5 | — | — | ✚ |
| Kuching | +1 | Slightly Positive | 0.1273 | 0.4686 |  | 3 | — | — |  |
| Banting | +1 | Slightly Positive | 0.1096 | 0.3887 |  | 4 | — | — | ✚ |
| Penang | +0 | Neutral | 0.0889 | 0.2953 |  | 12 | — | — |  |
| Malaysia | +0 | Neutral | 0.0805 | 0.2574 |  | 30 | — | — | ✚ |
| Subang | +0 | Neutral | 0.0561 | 0.1473 |  | 9 | — | — | ✚ |
| Negeri Sembilan | +0 | Neutral | 0.0559 | 0.1464 |  | 30 | — | — |  |
| Melaka | +0 | Neutral | 0.0408 | 0.0782 |  | 6 | — | — |  |
| Russia | +0 | Neutral | 0.0405 | 0.0769 |  | 7 | — | — | ✚ |
| Perak | +0 | Neutral | 0.0348 | 0.0511 |  | 16 | — | — |  |
| Sarawak | +0 | Neutral | 0.0328 | 0.0421 |  | 20 | — | — |  |
| Kuala Lumpur | +0 | Neutral | 0.0311 | 0.0344 |  | 30 | — | — |  |
| China | +0 | Neutral | 0.0191 | -0.0197 |  | 24 | — | — | ✚ |
| Selangor | +0 | Neutral | 0.0133 | -0.0459 |  | 30 | — | — |  |
| Rompin | +0 | Neutral | 0.0103 | -0.0594 |  | 5 | — | — | ✚ |
| Johor | +0 | Neutral | 0.0090 | -0.0653 |  | 26 | — | — |  |
| UK | +0 | Neutral | 0.0064 | -0.0770 |  | 30 | — | — | ✚ |
| N14 | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | — | — |  |
| Pasir Gudang | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | — | — |  |
| Pertang | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — |  |
| Rantau | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | — | — |  |
| Batu Pahat | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Beaufort | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Beluran | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Betong | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Bintulu | +0 | Neutral | 0.0000 | -0.1059 |  | 5 | — | — | ✚ |
| Brunei | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | — | — | ✚ |
| Cameron Highlands | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Dungun | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Gombak | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Hulu Selangor | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Ipoh | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Kangar | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Kedah | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | — | — | ✚ |
| Kelantan | +0 | Neutral | 0.0000 | -0.1059 |  | 3 | — | — | ✚ |
| Kemaman | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Keningau | +0 | Neutral | 0.0000 | -0.1059 |  | 5 | — | — | ✚ |
| Klang | +0 | Neutral | 0.0000 | -0.1059 |  | 8 | — | — | ✚ |
| Klang Valley | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Korea | +0 | Neutral | 0.0000 | -0.1059 |  | 5 | — | — | ✚ |
| Kota Tinggi | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Kuala Selangor | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Kuala Terengganu | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Kuantan | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Kudat | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | — | — | ✚ |
| Kulai | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Kunak | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Lahad Datu | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | — | — | ✚ |
| Limbang | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Lipis | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Maran | +0 | Neutral | 0.0000 | -0.1059 |  | 13 | — | — | ✚ |
| Mersing | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Miri | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Muar | +0 | Neutral | 0.0000 | -0.1059 |  | 5 | — | — | ✚ |
| North Sumatra | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Pahang | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | — | — | ✚ |
| Pasir Puteh | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Penampang | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Perlis | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Pontian | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Putatan | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Samarahan | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Sarikei | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Segamat | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | — | — | ✚ |
| Semporna | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Seremban | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | — | — | ✚ |
| Serian | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Shah Alam | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | — | — | ✚ |
| Sibu | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | — | — | ✚ |
| South Korea | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | — | — | ✚ |
| Strait of Hormuz | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Tambunan | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| Tawau | +0 | Neutral | 0.0000 | -0.1059 |  | 6 | — | — | ✚ |
| Tenom | +0 | Neutral | 0.0000 | -0.1059 |  | 5 | — | — | ✚ |
| Terengganu | +0 | Neutral | 0.0000 | -0.1059 |  | 5 | — | — | ✚ |
| Singapore | +0 | Neutral | -0.0158 | -0.1772 |  | 18 | — | — | ✚ |
| US | +0 | Neutral | -0.0429 | -0.2995 |  | 30 | — | — | ✚ |
| Wall Street | +0 | Neutral | -0.0513 | -0.3375 |  | 2 | — | — | ✚ |
| Putrajaya | +0 | Neutral | -0.0515 | -0.3384 |  | 6 | — | — | ✚ |
| Sabah | +0 | Neutral | -0.0753 | -0.4458 |  | 25 | — | — |  |
| Hungary | +0 | Neutral | -0.0880 | -0.5031 |  | 2 | — | — | ✚ |
| Iran | +0 | Neutral | -0.0976 | -0.5464 |  | 30 | — | — | ✚ |
| Ranau | -1 | Slightly Negative | -0.1000 | -0.5572 |  | 5 | — | — | ✚ |
| Indonesia | -1 | Slightly Negative | -0.1359 | -0.7193 |  | 15 | — | — | ✚ |
| Venezuela | -1 | Slightly Negative | -0.1825 | -0.9296 |  | 8 | — | — | ✚ |
| Sepang | -1 | Slightly Negative | -0.1933 | -0.9783 |  | 11 | — | — | ✚ |
| Saudi Arabia | -1 | Slightly Negative | -0.1953 | -0.9874 |  | 4 | — | — | ✚ |
| Sandakan | -1 | Slightly Negative | -0.2064 | -1.0375 |  | 7 | — | — | ✚ |
| Hodeidah | -1 | Slightly Negative | -0.2604 | -1.2812 |  | 3 | — | — | ✚ |
| Yemen | -1 | Slightly Negative | -0.2604 | -1.2812 |  | 3 | — | — | ✚ |
| Ampangan | -1 | Slightly Negative | -0.2626 | -1.2911 |  | 4 | — | — | ✚ |
| England | -2 | Negative | -0.3170 | -1.5366 |  | 22 | — | — | ✚ |
| Middle East | -2 | Negative | -0.3873 | -1.8539 |  | 5 | — | — | ✚ |
| France | -2 | Negative | -0.3922 | -1.8760 |  | 8 | — | — | ✚ |
| Argentina | -2 | Negative | -0.4587 | -2.1761 | ⚠️ | 6 | — | — | ✚ |
| Spain | -2 | Negative | -0.5131 | -2.4217 | ⚠️ | 8 | — | — | ✚ |
| Parliament House | -3 | Very Negative | -0.6360 | -2.9763 | ⚠️ | 1 | — | — |  |
| West Asia | -3 | Very Negative | -0.6400 | -2.9944 | ⚠️ | 7 | — | — | ✚ |
| Germany | -3 | Very Negative | -0.7024 | -3.2760 | ⚠️ | 4 | — | — | ✚ |
### EVENT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| WAN IFRA ASIA MEDIA AWARDS 2025 | +3 | Very Positive | 0.9187 | 4.0404 | ⚠️ | 2 | — | — | ✚ |
| Investigation | +2 | Positive | 0.4746 | 2.0360 | ⚠️ | 4 | — | — | ✚ |
| Summit | +2 | Positive | 0.3651 | 1.5418 |  | 5 | — | — | ✚ |
| Glasgow 2026 | +1 | Slightly Positive | 0.2490 | 1.0179 |  | 16 | — | — | ✚ |
| Hearing | +1 | Slightly Positive | 0.1368 | 0.5115 |  | 6 | — | — | ✚ |
| Negeri Sembilan polls | +0 | Neutral | 0.0910 | 0.3048 |  | 6 | — | — | ✚ |
| Negri Sembilan polls | +0 | Neutral | 0.0740 | 0.2281 |  | 4 | — | — | ✚ |
| Piala Dunia | +0 | Neutral | 0.0629 | 0.1780 |  | 7 | — | — | ✚ |
| election | +0 | Neutral | 0.0562 | 0.1477 |  | 11 | — | — | ✚ |
| manifesto | +0 | Neutral | 0.0451 | 0.0976 |  | 30 | — | — | ✚ |
| Trial | +0 | Neutral | 0.0240 | 0.0024 |  | 23 | — | — | ✚ |
| event | +0 | Neutral | 0.0179 | -0.0251 |  | 25 | — | — |  |
| campaign | +0 | Neutral | 0.0100 | -0.0608 |  | 21 | — | — |  |
| Appeal | +0 | Neutral | 0.0053 | -0.0820 |  | 17 | — | — | ✚ |
| BN Candidate Announcement (NS) | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | — | — |  |
| ceramah | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | — | — |  |
| HAWANA X TM Media Event | +0 | Neutral | 0.0000 | -0.1059 |  | 7 | — | — |  |
| Johor State Election | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | — | — |  |
| kempen | +0 | Neutral | 0.0000 | -0.1059 |  | 7 | — | — |  |
| majlis | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — |  |
| Negeri Sembilan State Election 2026 | +0 | Neutral | 0.0000 | -0.1059 |  | 18 | — | — |  |
| Sarawak State Election 2026 | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | — | — |  |
| walkabout | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | — | — |  |
| pilihan raya | +0 | Neutral | 0.0000 | -0.1059 |  | 6 | — | — | ✚ |
| pilihan raya negeri | +0 | Neutral | 0.0000 | -0.1059 |  | 5 | — | — | ✚ |
| Pilihan Raya Negeri Johor | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| PRN Negeri | +0 | Neutral | 0.0000 | -0.1059 |  | 10 | — | — | ✚ |
| sidang akhbar | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| state election | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | — | — | ✚ |
| Court case | +0 | Neutral | -0.0151 | -0.1741 |  | 2 | — | — | ✚ |
| rally | -1 | Slightly Negative | -0.1262 | -0.6755 |  | 3 | — | — |  |
| Probe | -1 | Slightly Negative | -0.1843 | -0.9377 |  | 7 | — | — | ✚ |
| World Cup | -1 | Slightly Negative | -0.2176 | -1.0880 |  | 12 | — | — | ✚ |
| Charged | -2 | Negative | -0.5519 | -2.5968 | ⚠️ | 5 | — | — | ✚ |
### CONCEPT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Onn Hafiz 56-seats solo bid | +3 | Very Positive | 0.7334 | 3.2041 | ⚠️ | 1 | — | — |  |
| green technology | +3 | Very Positive | 0.6705 | 2.9202 | ⚠️ | 1 | — | — | ✚ |
| renewable energy | +3 | Very Positive | 0.6705 | 2.9202 | ⚠️ | 1 | — | — | ✚ |
| mandate | +2 | Positive | 0.4512 | 1.9304 |  | 3 | — | — | ✚ |
| oil and gas | +2 | Positive | 0.4404 | 1.8817 |  | 1 | — | — | ✚ |
| opposition | +2 | Positive | 0.3401 | 1.4290 |  | 2 | — | — | ✚ |
| copyright | +1 | Slightly Positive | 0.2741 | 1.1311 |  | 18 | — | — | ✚ |
| Subsidies & welfare aid | +1 | Slightly Positive | 0.2288 | 0.9267 |  | 5 | — | — |  |
| Super El Nino food security | +1 | Slightly Positive | 0.2263 | 0.9154 |  | 1 | — | — |  |
| Wealth tax | +1 | Slightly Positive | 0.1482 | 0.5629 |  | 0 | — | — |  |
| MADANI government | +1 | Slightly Positive | 0.1340 | 0.4988 |  | 3 | — | — |  |
| AI | +0 | Neutral | 0.0310 | 0.0340 |  | 30 | — | — | ✚ |
| Bersatu own logo in N9 | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | — | — |  |
| Cost of living | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | — | — |  |
| Service tax | +0 | Neutral | 0.0000 | -0.1059 |  | 3 | — | — |  |
| Third force movement | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | — | — |  |
| UEC recognition | +0 | Neutral | 0.0000 | -0.1059 |  | 0 | — | — |  |
| constitutional rights | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | — | — | ✚ |
| Israeli deportation | +0 | Neutral | 0.0000 | -0.1059 |  | 1 | — | — | ✚ |
| MediAsas | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | — | — | ✚ |
| perpaduan | +0 | Neutral | 0.0000 | -0.1059 |  | 4 | — | — | ✚ |
| pork supply | +0 | Neutral | 0.0000 | -0.1059 |  | 2 | — | — | ✚ |
| BN-PN understanding | -1 | Slightly Negative | -0.1700 | -0.8732 |  | 2 | — | — | ✚ |
| take-home income | -1 | Slightly Negative | -0.1769 | -0.9043 |  | 4 | — | — | ✚ |
| party switch | -2 | Negative | -0.3228 | -1.5628 |  | 4 | — | — | ✚ |
| nominated assemblymen | -2 | Negative | -0.4537 | -2.1536 | ⚠️ | 3 | — | — | ✚ |
| democratic power | -3 | Very Negative | -0.6019 | -2.8224 | ⚠️ | 2 | — | — | ✚ |
| gig economy | -3 | Very Negative | -0.6369 | -2.9804 | ⚠️ | 2 | — | — | ✚ |
---

## Methodology

1. **Entity Source:** Loaded from the 2026-07-25T14:00+08 extraction roster (274 Phase-1 entity names) plus the 78 canonical entities from the per-entity index. Roster names were merged into canonical entities by normalized name/alias matching (honorific-stripped); unmerged names were added as new entities (205 new).
2. **Context Extraction:** For each entity, search variants (canonical name + aliases + roster matches) were located in the 2026-07-25 raw source collection (24 sources, 24 processed, ~737057 chars). A context window (~140+170 chars) was extracted around each mention (markdown stripped, de-duplicated, capped at 30/entity).
3. **Sentiment Scoring:** Applied VADER to each context snippet; entity sentiment = mean compound across snippets.
4. **Score Mapping:** VADER compound (-1..+1) → 7-point Likert (-3..+3): +3 ≥0.6, +2 ≥0.3, +1 ≥0.1, 0 (-0.1..0.1), -1 >-0.3, -2 >-0.6, -3 ≤-0.6.
5. **Anomaly Detection:** Z-score on raw compound vs overall mean/std; flagged when |z| > 2.
6. **Coalition/Party Aggregation:** Persons + political-party/coalition orgs mapped via per-entity metadata and affiliation maps (FIGURE_AFFILIATIONS, ORG_TO_COALITION, analyst-extended NEW_FIGURE_AFFIL).

---

*Report generated by OpenCLaw Sentiment Analysis Pipeline (sentiment-analysis skill)*
*VADER: Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.*

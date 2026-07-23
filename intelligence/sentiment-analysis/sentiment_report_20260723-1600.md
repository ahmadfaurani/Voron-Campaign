# Sentiment Analysis Report

**Classification:** TLP:AMBER
**Generated:** 2026-07-23 16:00 +08
**Report Date:** 2026-07-23
**Report Timestamp:** 2026-07-23 16:00 +08
**Extraction ID:** ext_20260723_1400_phase1
**Extraction Source:** 2026-07-23T14:00:00+08:00
**Collection Cycle:** 2026-07-23T000644Z
**Source Count:** 24
**Analysis Method:** VADER Sentiment Analysis on fresh context snippets extracted from 2026-07-23 raw collection
**Score Range:** -3 (very negative) to +3 (very positive)
**Anomaly Threshold:** |z-score| > 2

> **Data-freshness note:** The 2026-07-23 extraction produced Phase-1 entity name lists
> only; Phase-2 per-entity context files were not regenerated for this cycle. To produce a
> genuine 2026-07-23 sentiment signal, context snippets were extracted directly from the
> 2026-07-23 raw source collection and scored with VADER. Coalition/party metadata sourced
> from the canonical per-entity files (2026-07-16 Phase-2 set) plus an analyst-extended
> affiliation map for newly-extracted figures.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Roster Entities (Phase-1 names) | 246 |
| Analysis Entities (merged) | 260 |
| Canonical Entities (from index) | 78 |
| New Entities (this cycle) | 182 |
| Roster Names Matched to Canonical | 52 |
| Sources Processed | 24 |
| Entities with Context | 235 |
| Entities without Context (fallback) | 25 |
| Overall Mean Sentiment | +0.100 |
| Overall Std Deviation | 0.864 |
| Overall Median Sentiment | +0.000 |
| Overall Raw Mean | 0.0253 |
| Overall Raw Std Dev | 0.1988 |
| Sentiment Range | [-3, +3] |
| Positive Entities | 40 |
| Neutral Entities | 192 |
| Negative Entities | 28 |
| Anomalies Detected | 22 |
| Coalitions Analyzed | 8 |
| Parties Analyzed | 16 |

### Sentiment Distribution

```
Positive (40)  ████████████████████████████████████████
Neutral  (192)  ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
Negative (28)  ████████████████████████████
```

---

## Coalition Aggregate Sentiment

| Coalition | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range |
|-----------|:-:|------|:----------:|:-------:|:--------:|:-----:|
| GPS | +0 | Neutral | 0.0762 | 0.1986 | 5 | [-0.134, 0.392] |
| WARISAN | +0 | Neutral | 0.0129 | 0.0000 | 1 | [0.013, 0.013] |
| PH | +0 | Neutral | 0.0028 | 0.0973 | 16 | [-0.255, 0.270] |
| BERSAMA | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| PEJUANG | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] |
| PN | +0 | Neutral | -0.0122 | 0.0758 | 4 | [-0.101, 0.051] |
| BN | +0 | Neutral | -0.0288 | 0.1022 | 12 | [-0.262, 0.114] |
| GRS | -1 | Slightly Negative | -0.1342 | 0.0000 | 1 | [-0.134, -0.134] |
### Coalition Entities
- **GPS** (+0, Neutral): Sim Kui Hian, Tiong King Sing, Abang Johari, Gabungan Parti Sarawak, PRS
- **WARISAN** (+0, Neutral): Parti Warisan
- **PH** (+0, Neutral): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Anthony Loke, Mohamad Sabu, Syed Saddiq, Saifuddin Nasution, Democratic Action Party, Malaysia United Democratic Alliance, Pakatan Harapan, Parti Amanah Negara, Parti Keadilan Rakyat, Keadilan
- **BERSAMA** (+0, Neutral): Parti Bersama
- **PEJUANG** (+0, Neutral): Mahathir Mohamad, Pejuang
- **PN** (+0, Neutral): Muhyiddin Yassin, Parti Islam Se-Malaysia, Parti Pribumi Bersatu Malaysia, Perikatan Nasional
- **BN** (+0, Neutral): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Bung Moktar Radin, Najib Razak, Onn Hafiz, Barisan Nasional, Malaysian Chinese Association, Malaysian Indian Congress, United Malays National Organisation
- **GRS** (-1, Slightly Negative): GRS

---

## Party Aggregate Sentiment

| Party | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range | Coalition |
|-------|:-:|------|:----------:|:-------:|:--------:|:-----:|:---------:|
| PRS | +2 | Positive | 0.3918 | 0.0000 | 1 | [0.392, 0.392] | GPS |
| Keadilan | +1 | Slightly Positive | 0.2700 | 0.0000 | 1 | [0.270, 0.270] | — |
| PBB | +1 | Slightly Positive | 0.1235 | 0.0000 | 1 | [0.123, 0.123] | — |
| MIC | +1 | Slightly Positive | 0.1142 | 0.0000 | 1 | [0.114, 0.114] | BN |
| BERSATU | +0 | Neutral | 0.0508 | 0.0008 | 2 | [0.050, 0.051] | PN |
| MUDA | +0 | Neutral | 0.0276 | 0.0390 | 2 | [0.000, 0.055] | PH |
| Warisan | +0 | Neutral | 0.0129 | 0.0000 | 1 | [0.013, 0.013] | WARISAN |
| DAP | +0 | Neutral | 0.0037 | 0.0052 | 2 | [0.000, 0.007] | PH |
| PKR | +0 | Neutral | 0.0006 | 0.0018 | 8 | [0.000, 0.005] | PH |
| BERSAMA | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | BERSAMA |
| GPS | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] | GPS |
| MCA | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | BN |
| Pejuang | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | PEJUANG |
| PAS | +0 | Neutral | -0.0493 | 0.0000 | 1 | [-0.049, -0.049] | PN |
| UMNO | +0 | Neutral | -0.0522 | 0.1044 | 9 | [-0.262, 0.000] | BN |
| AMANAH | -1 | Slightly Negative | -0.1273 | 0.1800 | 2 | [-0.255, 0.000] | PH |
### Party Entities
- **PRS** (+2, Positive, → GPS): PRS
- **Keadilan** (+1, Slightly Positive, → —): Keadilan
- **PBB** (+1, Slightly Positive, → —): Abang Johari
- **MIC** (+1, Slightly Positive, → BN): Malaysian Indian Congress
- **BERSATU** (+0, Neutral, → PN): Muhyiddin Yassin, Parti Pribumi Bersatu Malaysia
- **MUDA** (+0, Neutral, → PH): Syed Saddiq, Malaysia United Democratic Alliance
- **Warisan** (+0, Neutral, → WARISAN): Parti Warisan
- **DAP** (+0, Neutral, → PH): Anthony Loke, Democratic Action Party
- **PKR** (+0, Neutral, → PH): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Saifuddin Nasution, Parti Keadilan Rakyat
- **BERSAMA** (+0, Neutral, → BERSAMA): Parti Bersama
- **GPS** (+0, Neutral, → GPS): Sim Kui Hian, Tiong King Sing
- **MCA** (+0, Neutral, → BN): Malaysian Chinese Association
- **Pejuang** (+0, Neutral, → PEJUANG): Mahathir Mohamad
- **PAS** (+0, Neutral, → PN): Parti Islam Se-Malaysia
- **UMNO** (+0, Neutral, → BN): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Bung Moktar Radin, Najib Razak, Onn Hafiz, United Malays National Organisation
- **AMANAH** (-1, Slightly Negative, → PH): Mohamad Sabu, Parti Amanah Negara

---

## Sentiment Anomalies (|z-score| > 2)

**22 anomalies detected.**

| # | Entity | Type | Score | Label | Z-Score | Direction | Coalition | Party | Contexts |
|---|--------|------|:-----:|-------|:-------:|:---------:|-----------|:------:|:--------:|
| 1 | WAN IFRA ASIA MEDIA AWARDS 2025 | EVENT | +3 | Very Positive | 4.4930 | positive | N/A | — | 2 |
| 2 | grassroots | CONCEPT | -3 | Very Negative | -3.7563 | negative | N/A | — | 4 |
| 3 | Court case | EVENT | +3 | Very Positive | 3.7537 | positive | N/A | — | 1 |
| 4 | The Star | ORGANIZATION | +3 | Very Positive | 3.6094 | positive | N/A | — | 1 |
| 5 | Onn Hafiz 56-seats solo bid | CONCEPT | +3 | Very Positive | 3.5611 | positive | N/A | — | 1 |
| 6 | Strait of Hormuz | LOCATION | -3 | Very Negative | -3.3303 | negative | N/A | — | 1 |
| 7 | Parliament | ORGANIZATION | -3 | Very Negative | -3.3258 | negative | N/A | — | 1 |
| 8 | green technology | CONCEPT | +3 | Very Positive | 3.2448 | positive | N/A | — | 1 |
| 9 | renewable energy | CONCEPT | +3 | Very Positive | 3.2448 | positive | N/A | — | 1 |
| 10 | West Asia | LOCATION | -2 | Negative | -3.0819 | negative | N/A | — | 4 |
| 11 | Khatijah Abdullah | PERSON | +3 | Very Positive | 3.0019 | positive | N/A | — | 4 |
| 12 | Wall Street | LOCATION | -2 | Negative | -2.8636 | negative | N/A | — | 4 |
| 13 | United States | LOCATION | +2 | Positive | 2.8128 | positive | N/A | — | 4 |
| 14 | opposition | CONCEPT | -2 | Negative | -2.7394 | negative | N/A | — | 4 |
| 15 | Hearing | EVENT | +2 | Positive | 2.6498 | positive | N/A | — | 4 |
| 16 | Suara Keadilan | ORGANIZATION | +2 | Positive | 2.5880 | positive | N/A | — | 1 |
| 17 | Dewan Rakyat | ORGANIZATION | +2 | Positive | 2.4406 | positive | N/A | — | 1 |
| 18 | water supply | CONCEPT | +2 | Positive | 2.4406 | positive | N/A | — | 1 |
| 19 | KWSP | ORGANIZATION | +2 | Positive | 2.3868 | positive | N/A | — | 4 |
| 20 | Indonesia | LOCATION | -2 | Negative | -2.1998 | negative | N/A | — | 18 |
| 21 | DVS | ORGANIZATION | +2 | Positive | 2.1072 | positive | N/A | — | 6 |
| 22 | Rajeentheran Suntheralingam | PERSON | +2 | Positive | 2.0584 | positive | N/A | — | 4 |
---

## Entity Sentiments by Type

### PERSON

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Khatijah Abdullah | +3 | Very Positive | 0.6222 | 3.0019 | ⚠️ | 4 | — | — | ✚ |
| Rajeentheran Suntheralingam | +2 | Positive | 0.4346 | 2.0584 | ⚠️ | 4 | — | — | ✚ |
| Abang Johari | +1 | Slightly Positive | 0.1235 | 0.4939 |  | 4 | GPS | PBB | ✚ |
| Tun | +1 | Slightly Positive | 0.1155 | 0.4536 |  | 30 | — | — | ✚ |
| Datuk Seri | +1 | Slightly Positive | 0.1033 | 0.3923 |  | 7 | — | — | ✚ |
| Datuk | +0 | Neutral | 0.0723 | 0.2364 |  | 10 | — | — | ✚ |
| Muhyiddin Yassin | +0 | Neutral | 0.0502 | 0.1252 |  | 8 | PN | BERSATU |  |
| Asli | +0 | Neutral | 0.0193 | -0.0302 |  | 4 | — | — | ✚ |
| Anwar Ibrahim | +0 | Neutral | 0.0051 | -0.1016 |  | 30 | PH | PKR |  |
| Ab Rauf Yusoh | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | BN | UMNO |  |
| Aminuddin Harun | +0 | Neutral | 0.0000 | -0.1272 |  | 12 | PH | PKR |  |
| Hassan Abdul Karim | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | PH | PKR |  |
| Jalaluddin Abdul Rahman | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | BN | UMNO |  |
| Khairy Jamaluddin | +0 | Neutral | 0.0000 | -0.1272 |  | 6 | BN | UMNO |  |
| Mahathir Mohamad | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | PEJUANG | Pejuang |  |
| Mohamad Hasan | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | BN | UMNO |  |
| Mohd Ghazali Sabari | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | — | — |  |
| Nik Nazmi Nik Ahmad | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | PH | PKR |  |
| Nurul Izzah Anwar | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | PH | PKR |  |
| Rafizi Ramli | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | PH | PKR |  |
| Sim Kui Hian | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | GPS | GPS |  |
| Tiong King Sing | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | GPS | GPS |  |
| Abdul Razak | +0 | Neutral | 0.0000 | -0.1272 |  | 3 | — | — | ✚ |
| Ahmad Faez Abdul Razak | +0 | Neutral | 0.0000 | -0.1272 |  | 2 | — | — | ✚ |
| Anthony Loke | +0 | Neutral | 0.0000 | -0.1272 |  | 3 | PH | DAP | ✚ |
| Muhammad Nazri Kassim | +0 | Neutral | 0.0000 | -0.1272 |  | 2 | — | — | ✚ |
| Datuk Seri Aminuddin Ha | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| Bung Moktar Radin | +0 | Neutral | 0.0000 | -0.1272 |  | 3 | BN | UMNO | ✚ |
| Menteri Besar PH | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Najib Razak | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | BN | UMNO | ✚ |
| Onn Hafiz | +0 | Neutral | 0.0000 | -0.1272 |  | 2 | BN | UMNO | ✚ |
| Punya | +0 | Neutral | 0.0000 | -0.1272 |  | 9 | — | — | ✚ |
| Syed Saddiq | +0 | Neutral | 0.0000 | -0.1272 |  | 8 | PH | MUDA | ✚ |
| Saifuddin Nasution | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | PH | PKR | ✚ |
| Nazri | +0 | Neutral | -0.0765 | -0.5120 |  | 6 | — | — | ✚ |
| Ahmad Zahid Hamidi | -1 | Slightly Negative | -0.2071 | -1.1688 |  | 15 | BN | UMNO |  |
| Razak | -1 | Slightly Negative | -0.2188 | -1.2276 |  | 7 | — | — | ✚ |
| Mohamad Sabu | -1 | Slightly Negative | -0.2545 | -1.4072 |  | 10 | PH | AMANAH | ✚ |
### ORGANIZATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| The Star | +3 | Very Positive | 0.7430 | 3.6094 | ⚠️ | 1 | — | — | ✚ |
| Suara Keadilan | +2 | Positive | 0.5399 | 2.5880 | ⚠️ | 1 | — | — | ✚ |
| Dewan Rakyat | +2 | Positive | 0.5106 | 2.4406 | ⚠️ | 1 | — | — | ✚ |
| KWSP | +2 | Positive | 0.4999 | 2.3868 | ⚠️ | 4 | — | — | ✚ |
| DVS | +2 | Positive | 0.4443 | 2.1072 | ⚠️ | 6 | — | — | ✚ |
| PRS | +2 | Positive | 0.3918 | 1.8432 |  | 2 | GPS | PRS | ✚ |
| AirBorneo | +1 | Slightly Positive | 0.2929 | 1.3458 |  | 2 | — | — | ✚ |
| Keadilan | +1 | Slightly Positive | 0.2700 | 1.2306 |  | 8 | PH | Keadilan | ✚ |
| Perodua | +1 | Slightly Positive | 0.2470 | 1.1150 |  | 2 | — | — | ✚ |
| Apple | +1 | Slightly Positive | 0.1651 | 0.7031 |  | 16 | — | — | ✚ |
| Media Mulia | +1 | Slightly Positive | 0.1555 | 0.6548 |  | 6 | — | — | ✚ |
| Malaysian Indian Congress | +1 | Slightly Positive | 0.1142 | 0.4471 |  | 27 | BN | MIC |  |
| DUN | +0 | Neutral | 0.0881 | 0.3158 |  | 30 | — | — | ✚ |
| Google | +0 | Neutral | 0.0823 | 0.2867 |  | 22 | — | — | ✚ |
| ASEAN | +0 | Neutral | 0.0725 | 0.2374 |  | 20 | — | — |  |
| PRN | +0 | Neutral | 0.0579 | 0.1639 |  | 30 | — | — | ✚ |
| Malaysia United Democratic Alliance | +0 | Neutral | 0.0551 | 0.1499 |  | 8 | PH | MUDA |  |
| Parti Pribumi Bersatu Malaysia | +0 | Neutral | 0.0514 | 0.1313 |  | 12 | PN | BERSATU |  |
| IMU | +0 | Neutral | 0.0449 | 0.0986 |  | 11 | — | — | ✚ |
| TikTok | +0 | Neutral | 0.0136 | -0.0588 |  | 30 | — | — | ✚ |
| Parti Warisan | +0 | Neutral | 0.0129 | -0.0624 |  | 6 | WARISAN | Warisan |  |
| Barisan Nasional | +0 | Neutral | 0.0102 | -0.0759 |  | 15 | BN | — |  |
| Grab | +0 | Neutral | 0.0102 | -0.0759 |  | 4 | — | — | ✚ |
| Democratic Action Party | +0 | Neutral | 0.0073 | -0.0905 |  | 30 | PH | DAP |  |
| World Cup | +0 | Neutral | 0.0059 | -0.0976 |  | 16 | — | — | ✚ |
| HAWANA | +0 | Neutral | 0.0000 | -0.1272 |  | 7 | — | — |  |
| Malaysian Chinese Association | +0 | Neutral | 0.0000 | -0.1272 |  | 2 | BN | MCA |  |
| Ministry of Finance | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | — | — |  |
| Ministry of Home Affairs | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — |  |
| Parti Amanah Negara | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | PH | AMANAH |  |
| Parti Bersama | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | BERSAMA | BERSAMA |  |
| Parti Keadilan Rakyat | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | PH | PKR |  |
| Pejuang | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | PEJUANG | — |  |
| Suruhanjaya Pencegahan Rasuah Malaysia | +0 | Neutral | 0.0000 | -0.1272 |  | 2 | — | — |  |
| Borneo Post | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| CodeBlue | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| Harian Metro | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| JPA | +0 | Neutral | 0.0000 | -0.1272 |  | 6 | — | — | ✚ |
| KLK | +0 | Neutral | 0.0000 | -0.1272 |  | 5 | — | — | ✚ |
| Kosmo | +0 | Neutral | 0.0000 | -0.1272 |  | 7 | — | — | ✚ |
| KPKM | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| Malay Mail | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| MalaysiaGazette | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| Malaysiakini | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| MCMC | +0 | Neutral | 0.0000 | -0.1272 |  | 8 | — | — | ✚ |
| mStar | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| Sabah News | +0 | Neutral | 0.0000 | -0.1272 |  | 3 | — | — | ✚ |
| Sinar Harian | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| Spotify | +0 | Neutral | 0.0000 | -0.1272 |  | 5 | — | — | ✚ |
| State Government | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| UN | +0 | Neutral | -0.0061 | -0.1579 |  | 30 | — | — | ✚ |
| NGO | +0 | Neutral | -0.0205 | -0.2303 |  | 28 | — | — | ✚ |
| BuzzKini | +0 | Neutral | -0.0257 | -0.2565 |  | 4 | — | — | ✚ |
| AFP | +0 | Neutral | -0.0293 | -0.2746 |  | 6 | — | — | ✚ |
| Bernama | +0 | Neutral | -0.0324 | -0.2902 |  | 13 | — | — | ✚ |
| Pakatan Harapan | +0 | Neutral | -0.0383 | -0.3199 |  | 30 | PH | — |  |
| Parti Islam Se-Malaysia | +0 | Neutral | -0.0493 | -0.3752 |  | 30 | PN | PAS |  |
| Tropicana | +0 | Neutral | -0.0568 | -0.4129 |  | 4 | — | — | ✚ |
| Suruhanjaya Pilihan Raya | +0 | Neutral | -0.0580 | -0.4189 |  | 8 | — | — |  |
| Vulcan Post | +0 | Neutral | -0.0846 | -0.5527 |  | 4 | — | — | ✚ |
| NST | +0 | Neutral | -0.0922 | -0.5909 |  | 30 | — | — | ✚ |
| MOH | +0 | Neutral | -0.0933 | -0.5965 |  | 30 | — | — | ✚ |
| Cabinet | +0 | Neutral | -0.0953 | -0.6065 |  | 6 | — | — | ✚ |
| Perikatan Nasional | -1 | Slightly Negative | -0.1011 | -0.6357 |  | 30 | PN | — |  |
| The Edge Malaysia | -1 | Slightly Negative | -0.1133 | -0.6970 |  | 3 | — | — | ✚ |
| Gabungan Parti Sarawak | -1 | Slightly Negative | -0.1342 | -0.8022 |  | 3 | GPS | — |  |
| GRS | -1 | Slightly Negative | -0.1342 | -0.8022 |  | 3 | GRS | — |  |
| BURSA | -1 | Slightly Negative | -0.1375 | -0.8188 |  | 17 | — | — | ✚ |
| FIFA | -1 | Slightly Negative | -0.1569 | -0.9163 |  | 5 | — | — | ✚ |
| Bursa Malaysia | -1 | Slightly Negative | -0.1864 | -1.0647 |  | 6 | — | — | ✚ |
| United Malays National Organisation | -1 | Slightly Negative | -0.2624 | -1.4469 |  | 11 | BN | UMNO |  |
| Parliament | -3 | Very Negative | -0.6360 | -3.3258 | ⚠️ | 1 | — | — | ✚ |
### LOCATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| United States | +2 | Positive | 0.5846 | 2.8128 | ⚠️ | 4 | — | — | ✚ |
| Kuching | +2 | Positive | 0.3218 | 1.4911 |  | 7 | — | — |  |
| Terengganu | +1 | Slightly Positive | 0.2385 | 1.0722 |  | 12 | — | — | ✚ |
| Seremban | +1 | Slightly Positive | 0.2075 | 0.9163 |  | 11 | — | — | ✚ |
| England | +1 | Slightly Positive | 0.1884 | 0.8202 |  | 5 | — | — | ✚ |
| France | +1 | Slightly Positive | 0.1819 | 0.7876 |  | 9 | — | — | ✚ |
| India | +1 | Slightly Positive | 0.1624 | 0.6895 |  | 15 | — | — | ✚ |
| Banting | +1 | Slightly Positive | 0.1096 | 0.4239 |  | 4 | — | — | ✚ |
| South Korea | +1 | Slightly Positive | 0.1061 | 0.4063 |  | 3 | — | — | ✚ |
| Spain | +0 | Neutral | 0.0911 | 0.3309 |  | 7 | — | — | ✚ |
| Russia | +0 | Neutral | 0.0843 | 0.2967 |  | 5 | — | — | ✚ |
| Ranau | +0 | Neutral | 0.0804 | 0.2771 |  | 5 | — | — | ✚ |
| Korea | +0 | Neutral | 0.0636 | 0.1926 |  | 5 | — | — | ✚ |
| Sarawak | +0 | Neutral | 0.0591 | 0.1700 |  | 22 | — | — |  |
| Argentina | +0 | Neutral | 0.0346 | 0.0468 |  | 30 | — | — | ✚ |
| Kota Kinabalu | +0 | Neutral | 0.0265 | 0.0060 |  | 8 | — | — |  |
| Negeri Sembilan | +0 | Neutral | 0.0264 | 0.0055 |  | 30 | — | — |  |
| Klang | +0 | Neutral | 0.0201 | -0.0262 |  | 18 | — | — | ✚ |
| Sibu | +0 | Neutral | 0.0176 | -0.0387 |  | 10 | — | — | ✚ |
| Rompin | +0 | Neutral | 0.0103 | -0.0754 |  | 5 | — | — | ✚ |
| Kuala Lumpur | +0 | Neutral | 0.0031 | -0.1117 |  | 30 | — | — |  |
| UK | +0 | Neutral | 0.0001 | -0.1267 |  | 30 | — | — | ✚ |
| Linggi | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — |  |
| Melaka | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — |  |
| N14 | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | — | — |  |
| Pasir Gudang | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | — | — |  |
| Penang | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — |  |
| Pertang | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | — | — |  |
| Rantau | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | — | — |  |
| Selangor | +0 | Neutral | 0.0000 | -0.1272 |  | 16 | — | — |  |
| Batu Pahat | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Beaufort | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Beluran | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Betong | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Bintulu | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Brunei | +0 | Neutral | 0.0000 | -0.1272 |  | 6 | — | — | ✚ |
| Cameron Highlands | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Dungun | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Gombak | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Hulu Selangor | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Kangar | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Kedah | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| Kelantan | +0 | Neutral | 0.0000 | -0.1272 |  | 2 | — | — | ✚ |
| Kemaman | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Keningau | +0 | Neutral | 0.0000 | -0.1272 |  | 5 | — | — | ✚ |
| Kota Bharu | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Kota Tinggi | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Kuala Selangor | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Kuala Terengganu | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Kuantan | +0 | Neutral | 0.0000 | -0.1272 |  | 6 | — | — | ✚ |
| Kudat | +0 | Neutral | 0.0000 | -0.1272 |  | 2 | — | — | ✚ |
| Kulai | +0 | Neutral | 0.0000 | -0.1272 |  | 3 | — | — | ✚ |
| Kunak | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Lahad Datu | +0 | Neutral | 0.0000 | -0.1272 |  | 2 | — | — | ✚ |
| Limbang | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Lipis | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Maran | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| Mersing | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Muar | +0 | Neutral | 0.0000 | -0.1272 |  | 5 | — | — | ✚ |
| N95 tanpa subsidi naik  | +0 | Neutral | 0.0000 | -0.1272 |  | 2 | — | — | ✚ |
| N97 price raised  | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Pahang | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| Pasir Puteh | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Penampang | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Perlis | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Pontian | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Putatan | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Putrajaya | +0 | Neutral | 0.0000 | -0.1272 |  | 9 | — | — | ✚ |
| Samarahan | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Sarikei | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Segamat | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| Semporna | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Serian | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Shah Alam | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| Tambunan | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Tawau | +0 | Neutral | 0.0000 | -0.1272 |  | 6 | — | — | ✚ |
| Tenom | +0 | Neutral | 0.0000 | -0.1272 |  | 5 | — | — | ✚ |
| Thailand | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Sepang | +0 | Neutral | -0.0029 | -0.1418 |  | 9 | — | — | ✚ |
| Malaysia | +0 | Neutral | -0.0063 | -0.1589 |  | 30 | — | — | ✚ |
| Ipoh | +0 | Neutral | -0.0065 | -0.1599 |  | 8 | — | — | ✚ |
| US | +0 | Neutral | -0.0214 | -0.2349 |  | 30 | — | — | ✚ |
| Parliament House | +0 | Neutral | -0.0313 | -0.2847 |  | 4 | — | — |  |
| Middle East | +0 | Neutral | -0.0356 | -0.3063 |  | 2 | — | — | ✚ |
| Johor | +0 | Neutral | -0.0487 | -0.3722 |  | 27 | — | — |  |
| Singapore | +0 | Neutral | -0.0497 | -0.3772 |  | 20 | — | — | ✚ |
| Petaling Jaya | +0 | Neutral | -0.0631 | -0.4446 |  | 5 | — | — | ✚ |
| China | +0 | Neutral | -0.0726 | -0.4924 |  | 30 | — | — | ✚ |
| Sabah | -1 | Slightly Negative | -0.1274 | -0.7680 |  | 25 | — | — |  |
| Perak | -1 | Slightly Negative | -0.1379 | -0.8208 |  | 14 | — | — |  |
| Miri | -1 | Slightly Negative | -0.1436 | -0.8494 |  | 9 | — | — | ✚ |
| Sandakan | -1 | Slightly Negative | -0.1747 | -1.0058 |  | 7 | — | — | ✚ |
| Iran | -1 | Slightly Negative | -0.2415 | -1.3418 |  | 30 | — | — | ✚ |
| Indonesia | -2 | Negative | -0.4121 | -2.1998 | ⚠️ | 18 | — | — | ✚ |
| Wall Street | -2 | Negative | -0.5441 | -2.8636 | ⚠️ | 4 | — | — | ✚ |
| West Asia | -2 | Negative | -0.5875 | -3.0819 | ⚠️ | 4 | — | — | ✚ |
| Strait of Hormuz | -3 | Very Negative | -0.6369 | -3.3303 | ⚠️ | 1 | — | — | ✚ |
### EVENT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| WAN IFRA ASIA MEDIA AWARDS 2025 | +3 | Very Positive | 0.9187 | 4.4930 | ⚠️ | 2 | — | — | ✚ |
| Court case | +3 | Very Positive | 0.7717 | 3.7537 | ⚠️ | 1 | — | — | ✚ |
| Hearing | +2 | Positive | 0.5522 | 2.6498 | ⚠️ | 4 | — | — | ✚ |
| Investigation | +1 | Slightly Positive | 0.1313 | 0.5331 |  | 8 | — | — | ✚ |
| election | +1 | Slightly Positive | 0.1137 | 0.4446 |  | 14 | — | — | ✚ |
| Trial | +0 | Neutral | 0.0903 | 0.3269 |  | 11 | — | — | ✚ |
| Negeri Sembilan State Election 2026 | +0 | Neutral | 0.0223 | -0.0151 |  | 18 | — | — |  |
| World Cup | +0 | Neutral | 0.0059 | -0.0976 |  | 16 | — | — | ✚ |
| BN Candidate Announcement (NS) | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | — | — |  |
| ceramah | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — |  |
| HAWANA X TM Media Event | +0 | Neutral | 0.0000 | -0.1272 |  | 7 | — | — |  |
| Johor State Election | +0 | Neutral | 0.0000 | -0.1272 |  | 2 | — | — |  |
| kempen | +0 | Neutral | 0.0000 | -0.1272 |  | 7 | — | — |  |
| majlis | +0 | Neutral | 0.0000 | -0.1272 |  | 7 | — | — |  |
| Sarawak State Election 2026 | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | — | — |  |
| walkabout | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | — | — |  |
| Piala Dunia | +0 | Neutral | 0.0000 | -0.1272 |  | 12 | — | — | ✚ |
| pilihan raya | +0 | Neutral | 0.0000 | -0.1272 |  | 5 | — | — | ✚ |
| pilihan raya negeri | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| Pilihan Raya Negeri Johor | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| PRN Negeri | +0 | Neutral | 0.0000 | -0.1272 |  | 10 | — | — | ✚ |
| Probe | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| state election | +0 | Neutral | 0.0000 | -0.1272 |  | 1 | — | — | ✚ |
| Appeal | +0 | Neutral | -0.0007 | -0.1308 |  | 8 | — | — | ✚ |
| campaign | +0 | Neutral | -0.0064 | -0.1594 |  | 24 | — | — |  |
| Arrest | +0 | Neutral | -0.0736 | -0.4974 |  | 8 | — | — | ✚ |
| rally | -1 | Slightly Negative | -0.1262 | -0.7619 |  | 3 | — | — |  |
| event | -1 | Slightly Negative | -0.1503 | -0.8831 |  | 16 | — | — |  |
| Charged | -2 | Negative | -0.3704 | -1.9900 |  | 5 | — | — | ✚ |
### CONCEPT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Onn Hafiz 56-seats solo bid | +3 | Very Positive | 0.7334 | 3.5611 | ⚠️ | 1 | — | — |  |
| green technology | +3 | Very Positive | 0.6705 | 3.2448 | ⚠️ | 1 | — | — | ✚ |
| renewable energy | +3 | Very Positive | 0.6705 | 3.2448 | ⚠️ | 1 | — | — | ✚ |
| water supply | +2 | Positive | 0.5106 | 2.4406 | ⚠️ | 1 | — | — | ✚ |
| mandate | +2 | Positive | 0.3964 | 1.8663 |  | 6 | — | — | ✚ |
| copyright | +1 | Slightly Positive | 0.2458 | 1.1089 |  | 18 | — | — | ✚ |
| Super El Nino food security | +1 | Slightly Positive | 0.2229 | 0.9938 |  | 0 | — | — |  |
| Wealth tax | +1 | Slightly Positive | 0.1482 | 0.6181 |  | 0 | — | — |  |
| AI | +1 | Slightly Positive | 0.1096 | 0.4239 |  | 30 | — | — | ✚ |
| MADANI government | +0 | Neutral | 0.0948 | 0.3495 |  | 8 | — | — |  |
| Cost of living | +0 | Neutral | 0.0842 | 0.2962 |  | 9 | — | — |  |
| perpaduan | +0 | Neutral | 0.0734 | 0.2419 |  | 6 | — | — | ✚ |
| Bersatu own logo in N9 | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | — | — |  |
| Service tax | +0 | Neutral | 0.0000 | -0.1272 |  | 3 | — | — |  |
| Subsidies & welfare aid | +0 | Neutral | 0.0000 | -0.1272 |  | 21 | — | — |  |
| Third force movement | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | — | — |  |
| UEC recognition | +0 | Neutral | 0.0000 | -0.1272 |  | 0 | — | — |  |
| fertiliser price | +0 | Neutral | 0.0000 | -0.1272 |  | 2 | — | — | ✚ |
| MediAsas | +0 | Neutral | 0.0000 | -0.1272 |  | 4 | — | — | ✚ |
| pork supply | +0 | Neutral | 0.0000 | -0.1272 |  | 2 | — | — | ✚ |
| emergency triage | -1 | Slightly Negative | -0.1759 | -1.0119 |  | 1 | — | — | ✚ |
| doctor shortage | -1 | Slightly Negative | -0.2500 | -1.3845 |  | 1 | — | — | ✚ |
| opposition | -2 | Negative | -0.5194 | -2.7394 | ⚠️ | 4 | — | — | ✚ |
| grassroots | -3 | Very Negative | -0.7216 | -3.7563 | ⚠️ | 4 | — | — | ✚ |
---

## Methodology

1. **Entity Source:** Loaded from the 2026-07-23T14:00+08 extraction roster (246 Phase-1 entity names) plus the 78 canonical entities from the per-entity index. Roster names were merged into canonical entities by normalized name/alias matching (honorific-stripped); unmerged names were added as new entities (182 new).
2. **Context Extraction:** For each entity, search variants (canonical name + aliases + roster matches) were located in the 2026-07-23 raw source collection (24 sources, 24 processed, ~716542 chars). A context window (~140+170 chars) was extracted around each mention (markdown stripped, de-duplicated, capped at 30/entity).
3. **Sentiment Scoring:** Applied VADER to each context snippet; entity sentiment = mean compound across snippets.
4. **Score Mapping:** VADER compound (-1..+1) → 7-point Likert (-3..+3): +3 ≥0.6, +2 ≥0.3, +1 ≥0.1, 0 (-0.1..0.1), -1 >-0.3, -2 >-0.6, -3 ≤-0.6.
5. **Anomaly Detection:** Z-score on raw compound vs overall mean/std; flagged when |z| > 2.
6. **Coalition/Party Aggregation:** Persons + political-party/coalition orgs mapped via per-entity metadata and affiliation maps (FIGURE_AFFILIATIONS, ORG_TO_COALITION, analyst-extended NEW_FIGURE_AFFIL).

---

*Report generated by OpenCLaw Sentiment Analysis Pipeline (sentiment-analysis skill)*
*VADER: Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.*

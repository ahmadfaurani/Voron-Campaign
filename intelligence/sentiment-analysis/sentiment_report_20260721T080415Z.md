# Sentiment Analysis Report

**Classification:** TLP:AMBER
**Report Timestamp:** 20260721T080415Z
**Extraction ID:** ext_20260721_1400_phase1
**Extraction Source:** 2026-07-21T14:00:00+08:00
**Collection Cycle:** 2026-07-21T001251Z
**Source Count:** 24
**Analysis Method:** VADER Sentiment Analysis on fresh context snippets extracted from 2026-07-21 raw collection
**Score Range:** -3 (very negative) to +3 (very positive)
**Anomaly Threshold:** |z-score| > 2

> **Data-freshness note:** The 2026-07-21 extraction produced Phase-1 entity name lists
> only; Phase-2 per-entity context files were not regenerated for this cycle. To produce a
> genuine 2026-07-21 sentiment signal, context snippets were extracted directly from the
> 2026-07-21 raw source collection and scored with VADER. Coalition/party metadata sourced
> from the canonical per-entity files (2026-07-16 Phase-2 set) plus an analyst-extended
> affiliation map for newly-extracted figures.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Roster Entities (Phase-1 names) | 257 |
| Analysis Entities (merged) | 267 |
| Canonical Entities (from index) | 78 |
| New Entities (this cycle) | 189 |
| Roster Names Matched to Canonical | 51 |
| Sources Processed | 24 |
| Entities with Context | 242 |
| Entities without Context (fallback) | 25 |
| Overall Mean Sentiment | +0.311 |
| Overall Std Deviation | 0.983 |
| Overall Median Sentiment | +0.000 |
| Overall Raw Mean | 0.0658 |
| Overall Raw Std Dev | 0.2238 |
| Sentiment Range | [-3, +3] |
| Positive Entities | 68 |
| Neutral Entities | 180 |
| Negative Entities | 19 |
| Anomalies Detected | 24 |
| Coalitions Analyzed | 8 |
| Parties Analyzed | 16 |

### Sentiment Distribution

```
Positive (68)  ████████████████████████████████████████████████████████████████████
Neutral  (180)  ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
Negative (19)  ███████████████████
```

---

## Coalition Aggregate Sentiment

| Coalition | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range |
|-----------|:-:|------|:----------:|:-------:|:--------:|:-----:|
| WARISAN | +2 | Positive | 0.4944 | 0.0000 | 1 | [0.494, 0.494] |
| PEJUANG | +0 | Neutral | 0.0635 | 0.0898 | 2 | [0.000, 0.127] |
| GPS | +0 | Neutral | 0.0379 | 0.0759 | 4 | [0.000, 0.152] |
| PH | +0 | Neutral | 0.0365 | 0.1470 | 16 | [-0.192, 0.540] |
| BN | +0 | Neutral | 0.0107 | 0.2356 | 11 | [-0.536, 0.463] |
| BERSAMA | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] |
| GRS | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] |
| PN | -1 | Slightly Negative | -0.1278 | 0.3190 | 6 | [-0.778, 0.029] |
### Coalition Entities
- **WARISAN** (+2, Positive): Parti Warisan
- **PEJUANG** (+0, Neutral): Mahathir Mohamad, Pejuang
- **GPS** (+0, Neutral): Sim Kui Hian, Tiong King Sing, Abang Johari, Gabungan Parti Sarawak
- **PH** (+0, Neutral): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Anthony Loke, Mohamad Sabu, Nga, Syed Saddiq, Democratic Action Party, Malaysia United Democratic Alliance, Pakatan Harapan, Parti Amanah Negara, Parti Keadilan Rakyat, Keadilan
- **BN** (+0, Neutral): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Bung Moktar Radin, Najib Razak, Barisan Nasional, Malaysian Chinese Association, Malaysian Indian Congress, United Malays National Organisation
- **BERSAMA** (+0, Neutral): Parti Bersama
- **GRS** (+0, Neutral): Joachim, GRS
- **PN** (-1, Slightly Negative): Muhyiddin Yassin, Azanna Ahmad Kamar, Sanusi, Parti Islam Se-Malaysia, Parti Pribumi Bersatu Malaysia, Perikatan Nasional

---

## Party Aggregate Sentiment

| Party | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range | Coalition |
|-------|:-:|------|:----------:|:-------:|:--------:|:-----:|:---------:|
| Keadilan | +2 | Positive | 0.5399 | 0.0000 | 1 | [0.540, 0.540] | — |
| Warisan | +2 | Positive | 0.4944 | 0.0000 | 1 | [0.494, 0.494] | WARISAN |
| MIC | +1 | Slightly Positive | 0.1805 | 0.0000 | 1 | [0.180, 0.180] | BN |
| PBB | +1 | Slightly Positive | 0.1517 | 0.0000 | 1 | [0.152, 0.152] | — |
| Pejuang | +1 | Slightly Positive | 0.1270 | 0.0000 | 1 | [0.127, 0.127] | PEJUANG |
| DAP | +0 | Neutral | 0.0286 | 0.0253 | 3 | [0.000, 0.048] | PH |
| MUDA | +0 | Neutral | 0.0192 | 0.0272 | 2 | [0.000, 0.038] | PH |
| PAS | +0 | Neutral | 0.0143 | 0.0202 | 2 | [0.000, 0.029] | PN |
| PKR | +0 | Neutral | 0.0114 | 0.0405 | 7 | [-0.022, 0.101] | PH |
| BERSAMA | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | BERSAMA |
| GPS | +0 | Neutral | 0.0000 | 0.0000 | 2 | [0.000, 0.000] | GPS |
| GRS | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | GRS |
| MCA | +0 | Neutral | 0.0000 | 0.0000 | 1 | [0.000, 0.000] | BN |
| UMNO | +0 | Neutral | -0.0056 | 0.2733 | 8 | [-0.536, 0.463] | BN |
| AMANAH | +0 | Neutral | -0.0960 | 0.1358 | 2 | [-0.192, 0.000] | PH |
| BERSATU | -1 | Slightly Negative | -0.2594 | 0.4494 | 3 | [-0.778, 0.000] | PN |
### Party Entities
- **Keadilan** (+2, Positive, → —): Keadilan
- **Warisan** (+2, Positive, → WARISAN): Parti Warisan
- **MIC** (+1, Slightly Positive, → BN): Malaysian Indian Congress
- **PBB** (+1, Slightly Positive, → —): Abang Johari
- **Pejuang** (+1, Slightly Positive, → PEJUANG): Mahathir Mohamad
- **DAP** (+0, Neutral, → PH): Anthony Loke, Nga, Democratic Action Party
- **MUDA** (+0, Neutral, → PH): Syed Saddiq, Malaysia United Democratic Alliance
- **PAS** (+0, Neutral, → PN): Sanusi, Parti Islam Se-Malaysia
- **PKR** (+0, Neutral, → PH): Aminuddin Harun, Anwar Ibrahim, Hassan Abdul Karim, Nik Nazmi Nik Ahmad, Nurul Izzah Anwar, Rafizi Ramli, Parti Keadilan Rakyat
- **BERSAMA** (+0, Neutral, → BERSAMA): Parti Bersama
- **GPS** (+0, Neutral, → GPS): Sim Kui Hian, Tiong King Sing
- **GRS** (+0, Neutral, → GRS): Joachim
- **MCA** (+0, Neutral, → BN): Malaysian Chinese Association
- **UMNO** (+0, Neutral, → BN): Ab Rauf Yusoh, Ahmad Zahid Hamidi, Jalaluddin Abdul Rahman, Khairy Jamaluddin, Mohamad Hasan, Bung Moktar Radin, Najib Razak, United Malays National Organisation
- **AMANAH** (+0, Neutral, → PH): Mohamad Sabu, Parti Amanah Negara
- **BERSATU** (-1, Slightly Negative, → PN): Muhyiddin Yassin, Azanna Ahmad Kamar, Parti Pribumi Bersatu Malaysia

---

## Sentiment Anomalies (|z-score| > 2)

**24 anomalies detected.**

| # | Entity | Type | Score | Label | Z-Score | Direction | Coalition | Party | Contexts |
|---|--------|------|:-----:|-------|:-------:|:---------:|-----------|:------:|:--------:|
| 1 | WAN IFRA ASIA MEDIA AWARDS 2025 | EVENT | +3 | Very Positive | 3.8102 | positive | N/A | — | 2 |
| 2 | Azanna Ahmad Kamar | PERSON | -3 | Very Negative | -3.7712 | negative | PN | BERSATU | 4 |
| 3 | artificial intelligence | CONCEPT | +3 | Very Positive | 3.6752 | positive | N/A | — | 1 |
| 4 | Strait of Hormuz | LOCATION | -3 | Very Negative | -3.3321 | negative | N/A | — | 2 |
| 5 | Court case | EVENT | +3 | Very Positive | 3.1534 | positive | N/A | — | 1 |
| 6 | Indonesia | LOCATION | -3 | Very Negative | -3.0412 | negative | N/A | — | 8 |
| 7 | The Star | ORGANIZATION | +3 | Very Positive | 3.0252 | positive | N/A | — | 1 |
| 8 | Onn Hafiz 56-seats solo bid | CONCEPT | +3 | Very Positive | 2.9823 | positive | N/A | — | 1 |
| 9 | West Asia | LOCATION | -2 | Negative | -2.7473 | negative | N/A | — | 3 |
| 10 | Trial | EVENT | +3 | Very Positive | 2.7460 | positive | N/A | — | 6 |
| 11 | green technology | CONCEPT | +3 | Very Positive | 2.7013 | positive | N/A | — | 1 |
| 12 | Ahmad Zahid Hamidi | PERSON | -2 | Negative | -2.6887 | negative | BN | UMNO | 12 |
| 13 | DVS | ORGANIZATION | +3 | Very Positive | 2.6830 | positive | N/A | — | 4 |
| 14 | Khatijah Abdullah | PERSON | +3 | Very Positive | 2.4855 | positive | N/A | — | 4 |
| 15 | Azam Baki | PERSON | +3 | Very Positive | 2.4373 | positive | N/A | — | 2 |
| 16 | United States | LOCATION | +3 | Very Positive | 2.4252 | positive | N/A | — | 5 |
| 17 | Parliament | ORGANIZATION | -2 | Negative | -2.2617 | negative | N/A | — | 3 |
| 18 | Wilfred Madius Tangau | PERSON | +2 | Positive | 2.1960 | positive | N/A | — | 3 |
| 19 | Siti Hasmah | PERSON | +2 | Positive | 2.1683 | positive | N/A | — | 4 |
| 20 | Keadilan | ORGANIZATION | +2 | Positive | 2.1179 | positive | PH | Keadilan | 4 |
| 21 | Suara Keadilan | ORGANIZATION | +2 | Positive | 2.1179 | positive | N/A | — | 1 |
| 22 | KWSP | ORGANIZATION | +2 | Positive | 2.0928 | positive | N/A | — | 4 |
| 23 | Probe | EVENT | +2 | Positive | 2.0888 | positive | N/A | — | 2 |
| 24 | Suruhanjaya Pilihan Raya | ORGANIZATION | -2 | Negative | -2.0351 | negative | N/A | — | 8 |
---

## Entity Sentiments by Type

### PERSON

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| Khatijah Abdullah | +3 | Very Positive | 0.6222 | 2.4855 | ⚠️ | 4 | — | — | ✚ |
| Azam Baki | +3 | Very Positive | 0.6114 | 2.4373 | ⚠️ | 2 | — | — | ✚ |
| Wilfred Madius Tangau | +2 | Positive | 0.5574 | 2.1960 | ⚠️ | 3 | — | — | ✚ |
| Siti Hasmah | +2 | Positive | 0.5512 | 2.1683 | ⚠️ | 4 | — | — | ✚ |
| Jalaluddin Abdul Rahman | +2 | Positive | 0.4629 | 1.7739 |  | 2 | BN | UMNO |  |
| Datuk Seri | +2 | Positive | 0.3523 | 1.2798 |  | 4 | — | — | ✚ |
| Mustafa | +2 | Positive | 0.3062 | 1.0738 |  | 4 | — | — | ✚ |
| Datu Mustapha | +1 | Slightly Positive | 0.2500 | 0.8227 |  | 2 | — | — | ✚ |
| Ram Singh | +1 | Slightly Positive | 0.2500 | 0.8227 |  | 2 | — | — | ✚ |
| Datuk | +1 | Slightly Positive | 0.1844 | 0.5297 |  | 9 | — | — | ✚ |
| Abang Johari | +1 | Slightly Positive | 0.1517 | 0.3836 |  | 7 | GPS | PBB | ✚ |
| Tun | +1 | Slightly Positive | 0.1416 | 0.3384 |  | 30 | — | — | ✚ |
| Mahathir Mohamad | +1 | Slightly Positive | 0.1270 | 0.2732 |  | 12 | PEJUANG | Pejuang |  |
| Asli | +1 | Slightly Positive | 0.1238 | 0.2589 |  | 19 | — | — | ✚ |
| Khairy Jamaluddin | +1 | Slightly Positive | 0.1173 | 0.2299 |  | 9 | BN | UMNO |  |
| Anwar Ibrahim | +1 | Slightly Positive | 0.1014 | 0.1589 |  | 30 | PH | PKR |  |
| Nga | +0 | Neutral | 0.0480 | -0.0797 |  | 30 | PH | DAP | ✚ |
| Rajeentheran Suntheralingam | +0 | Neutral | 0.0478 | -0.0806 |  | 4 | — | — | ✚ |
| Syed Saddiq | +0 | Neutral | 0.0384 | -0.1226 |  | 16 | PH | MUDA | ✚ |
| Ab Rauf Yusoh | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | BN | UMNO |  |
| Hassan Abdul Karim | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | PH | PKR |  |
| Mohamad Hasan | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | BN | UMNO |  |
| Mohd Ghazali Sabari | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | — | — |  |
| Muhyiddin Yassin | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | PN | BERSATU |  |
| Nik Nazmi Nik Ahmad | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | PH | PKR |  |
| Nurul Izzah Anwar | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | PH | PKR |  |
| Rafizi Ramli | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | PH | PKR |  |
| Sim Kui Hian | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | GPS | GPS |  |
| Tiong King Sing | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | GPS | GPS |  |
| Abdul Razak | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| Ampuan Pahang | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| Anthony Loke | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | PH | DAP | ✚ |
| Mohd Faizal Ramli | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| Bung Moktar Radin | +0 | Neutral | 0.0000 | -0.2942 |  | 3 | BN | UMNO | ✚ |
| Joachim | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | GRS | GRS | ✚ |
| Zulkifli Mohamad Al-Bakri | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| Najib Razak | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | BN | UMNO | ✚ |
| Razak | +0 | Neutral | 0.0000 | -0.2942 |  | 8 | — | — | ✚ |
| Sanusi | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | PN | PAS | ✚ |
| Tengku Ampuan Pahang | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| Aminuddin Harun | +0 | Neutral | -0.0219 | -0.3920 |  | 24 | PH | PKR |  |
| Mohamad Sabu | -1 | Slightly Negative | -0.1921 | -1.1524 |  | 4 | PH | AMANAH | ✚ |
| Ahmad Zahid Hamidi | -2 | Negative | -0.5360 | -2.6887 | ⚠️ | 12 | BN | UMNO |  |
| Azanna Ahmad Kamar | -3 | Very Negative | -0.7783 | -3.7712 | ⚠️ | 4 | PN | BERSATU | ✚ |
### ORGANIZATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| The Star | +3 | Very Positive | 0.7430 | 3.0252 | ⚠️ | 1 | — | — | ✚ |
| DVS | +3 | Very Positive | 0.6664 | 2.6830 | ⚠️ | 4 | — | — | ✚ |
| Keadilan | +2 | Positive | 0.5399 | 2.1179 | ⚠️ | 4 | PH | Keadilan | ✚ |
| Suara Keadilan | +2 | Positive | 0.5399 | 2.1179 | ⚠️ | 1 | — | — | ✚ |
| KWSP | +2 | Positive | 0.5343 | 2.0928 | ⚠️ | 4 | — | — | ✚ |
| State Government | +2 | Positive | 0.5093 | 1.9812 |  | 1 | — | — | ✚ |
| Parti Warisan | +2 | Positive | 0.4944 | 1.9146 |  | 4 | WARISAN | Warisan |  |
| PRS | +2 | Positive | 0.3918 | 1.4562 |  | 2 | — | — | ✚ |
| Suruhanjaya Pencegahan Rasuah Malaysia | +2 | Positive | 0.3784 | 1.3964 |  | 3 | — | — |  |
| Grab | +2 | Positive | 0.3227 | 1.1475 |  | 3 | — | — | ✚ |
| Malaysian Indian Congress | +1 | Slightly Positive | 0.1805 | 0.5122 |  | 18 | BN | MIC |  |
| World Cup | +1 | Slightly Positive | 0.1785 | 0.5033 |  | 27 | — | — | ✚ |
| Media Mulia | +1 | Slightly Positive | 0.1555 | 0.4005 |  | 6 | — | — | ✚ |
| EC | +0 | Neutral | 0.0977 | 0.1423 |  | 30 | — | — | ✚ |
| UN | +0 | Neutral | 0.0853 | 0.0869 |  | 30 | — | — | ✚ |
| ASEAN | +0 | Neutral | 0.0622 | -0.0163 |  | 17 | — | — |  |
| IMU | +0 | Neutral | 0.0617 | -0.0185 |  | 8 | — | — | ✚ |
| Apple | +0 | Neutral | 0.0453 | -0.0918 |  | 13 | — | — | ✚ |
| Democratic Action Party | +0 | Neutral | 0.0379 | -0.1248 |  | 30 | PH | DAP |  |
| Google | +0 | Neutral | 0.0374 | -0.1271 |  | 24 | — | — | ✚ |
| Pakatan Harapan | +0 | Neutral | 0.0326 | -0.1485 |  | 30 | PH | — |  |
| Parti Islam Se-Malaysia | +0 | Neutral | 0.0286 | -0.1664 |  | 30 | PN | PAS |  |
| JPA | +0 | Neutral | 0.0253 | -0.1811 |  | 8 | — | — | ✚ |
| TikTok | +0 | Neutral | 0.0235 | -0.1892 |  | 30 | — | — | ✚ |
| FIFA | +0 | Neutral | 0.0200 | -0.2048 |  | 20 | — | — | ✚ |
| PRN | +0 | Neutral | 0.0123 | -0.2392 |  | 30 | — | — | ✚ |
| BURSA | +0 | Neutral | 0.0014 | -0.2879 |  | 11 | — | — | ✚ |
| Gabungan Parti Sarawak | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | GPS | — |  |
| GRS | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | GRS | — |  |
| HAWANA | +0 | Neutral | 0.0000 | -0.2942 |  | 11 | — | — |  |
| Malaysia United Democratic Alliance | +0 | Neutral | 0.0000 | -0.2942 |  | 8 | PH | MUDA |  |
| Malaysian Chinese Association | +0 | Neutral | 0.0000 | -0.2942 |  | 3 | BN | MCA |  |
| Ministry of Finance | +0 | Neutral | 0.0000 | -0.2942 |  | 5 | — | — |  |
| Ministry of Home Affairs | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | — | — |  |
| Parti Amanah Negara | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | PH | AMANAH |  |
| Parti Bersama | +0 | Neutral | 0.0000 | -0.2942 |  | 11 | BERSAMA | BERSAMA |  |
| Parti Keadilan Rakyat | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | PH | PKR |  |
| Parti Pribumi Bersatu Malaysia | +0 | Neutral | 0.0000 | -0.2942 |  | 8 | PN | BERSATU |  |
| Pejuang | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | PEJUANG | — |  |
| Bernama | +0 | Neutral | 0.0000 | -0.2942 |  | 11 | — | — | ✚ |
| Boeing | +0 | Neutral | 0.0000 | -0.2942 |  | 6 | — | — | ✚ |
| Borneo Post | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | — | — | ✚ |
| BuzzKini | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | — | — | ✚ |
| Daily Express | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| DUN | +0 | Neutral | 0.0000 | -0.2942 |  | 30 | — | — | ✚ |
| Harian Metro | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| JKNS | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | — | — | ✚ |
| Kementerian Kesihatan | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Kementerian Kesihatan Malaysia | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| KLK | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| Kosmo | +0 | Neutral | 0.0000 | -0.2942 |  | 8 | — | — | ✚ |
| KPKM | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | — | — | ✚ |
| Malay Mail | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | — | — | ✚ |
| MalaysiaGazette | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | — | — | ✚ |
| Malaysiakini | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | — | — | ✚ |
| MCMC | +0 | Neutral | 0.0000 | -0.2942 |  | 16 | — | — | ✚ |
| mStar | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | — | — | ✚ |
| NGO | +0 | Neutral | 0.0000 | -0.2942 |  | 23 | — | — | ✚ |
| Perodua | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| Sabah News | +0 | Neutral | 0.0000 | -0.2942 |  | 3 | — | — | ✚ |
| Sinar Harian | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | — | — | ✚ |
| Spotify | +0 | Neutral | 0.0000 | -0.2942 |  | 6 | — | — | ✚ |
| Perikatan Nasional | +0 | Neutral | -0.0170 | -0.3701 |  | 30 | PN | — |  |
| MOH | +0 | Neutral | -0.0178 | -0.3737 |  | 20 | — | — | ✚ |
| Barisan Nasional | +0 | Neutral | -0.0180 | -0.3746 |  | 24 | BN | — |  |
| Tropicana | +0 | Neutral | -0.0410 | -0.4773 |  | 8 | — | — | ✚ |
| NST | +0 | Neutral | -0.0552 | -0.5408 |  | 30 | — | — | ✚ |
| Cabinet | +0 | Neutral | -0.0701 | -0.6073 |  | 8 | — | — | ✚ |
| Vulcan Post | +0 | Neutral | -0.0846 | -0.6721 |  | 4 | — | — | ✚ |
| United Malays National Organisation | +0 | Neutral | -0.0892 | -0.6927 |  | 15 | BN | UMNO |  |
| The Edge Malaysia | -1 | Slightly Negative | -0.1133 | -0.8003 |  | 3 | — | — | ✚ |
| CodeBlue | -1 | Slightly Negative | -0.1240 | -0.8481 |  | 4 | — | — | ✚ |
| AirBorneo | -1 | Slightly Negative | -0.1664 | -1.0375 |  | 16 | — | — | ✚ |
| Bursa Malaysia | -1 | Slightly Negative | -0.2352 | -1.3449 |  | 4 | — | — | ✚ |
| Suruhanjaya Pilihan Raya | -2 | Negative | -0.3897 | -2.0351 | ⚠️ | 8 | — | — |  |
| Parliament | -2 | Negative | -0.4404 | -2.2617 | ⚠️ | 3 | — | — | ✚ |
### LOCATION

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| United States | +3 | Very Positive | 0.6087 | 2.4252 | ⚠️ | 5 | — | — | ✚ |
| Spain | +2 | Positive | 0.4682 | 1.7975 |  | 16 | — | — | ✚ |
| Tambunan | +2 | Positive | 0.3143 | 1.1100 |  | 5 | — | — | ✚ |
| Japan | +1 | Slightly Positive | 0.2537 | 0.8393 |  | 5 | — | — | ✚ |
| Samarahan | +1 | Slightly Positive | 0.2133 | 0.6588 |  | 5 | — | — | ✚ |
| Korea | +1 | Slightly Positive | 0.2077 | 0.6338 |  | 8 | — | — | ✚ |
| Putrajaya | +1 | Slightly Positive | 0.2004 | 0.6011 |  | 11 | — | — | ✚ |
| Muar | +1 | Slightly Positive | 0.1981 | 0.5909 |  | 9 | — | — | ✚ |
| Singapore | +1 | Slightly Positive | 0.1887 | 0.5489 |  | 17 | — | — | ✚ |
| UK | +1 | Slightly Positive | 0.1769 | 0.4962 |  | 30 | — | — | ✚ |
| Kota Kinabalu | +1 | Slightly Positive | 0.1719 | 0.4738 |  | 7 | — | — |  |
| Sarawak | +1 | Slightly Positive | 0.1382 | 0.3233 |  | 29 | — | — |  |
| Maran | +1 | Slightly Positive | 0.1315 | 0.2933 |  | 6 | — | — | ✚ |
| Wall Street | +1 | Slightly Positive | 0.1133 | 0.2120 |  | 3 | — | — | ✚ |
| Middle East | +1 | Slightly Positive | 0.1108 | 0.2008 |  | 2 | — | — | ✚ |
| Banting | +1 | Slightly Positive | 0.1096 | 0.1955 |  | 4 | — | — | ✚ |
| Russia | +1 | Slightly Positive | 0.1006 | 0.1553 |  | 4 | — | — | ✚ |
| Pahang | +1 | Slightly Positive | 0.1003 | 0.1539 |  | 14 | — | — | ✚ |
| Negeri Sembilan | +0 | Neutral | 0.0952 | 0.1312 |  | 30 | — | — |  |
| Malaysia | +0 | Neutral | 0.0945 | 0.1280 |  | 30 | — | — | ✚ |
| Penang | +0 | Neutral | 0.0937 | 0.1245 |  | 10 | — | — |  |
| Kuching | +0 | Neutral | 0.0748 | 0.0400 |  | 12 | — | — |  |
| Argentina | +0 | Neutral | 0.0637 | -0.0096 |  | 30 | — | — | ✚ |
| Sepang | +0 | Neutral | 0.0530 | -0.0574 |  | 6 | — | — | ✚ |
| China | +0 | Neutral | 0.0395 | -0.1177 |  | 25 | — | — | ✚ |
| Kuala Lumpur | +0 | Neutral | 0.0393 | -0.1186 |  | 30 | — | — |  |
| Johor | +0 | Neutral | 0.0129 | -0.2365 |  | 28 | — | — |  |
| US | +0 | Neutral | 0.0013 | -0.2883 |  | 30 | — | — | ✚ |
| Linggi | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | — | — |  |
| N14 | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | — | — |  |
| Pasir Gudang | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | — | — |  |
| Perak | +0 | Neutral | 0.0000 | -0.2942 |  | 7 | — | — |  |
| Pertang | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | — | — |  |
| Rantau | +0 | Neutral | 0.0000 | -0.2942 |  | 6 | — | — |  |
| Selangor | +0 | Neutral | 0.0000 | -0.2942 |  | 16 | — | — |  |
| Batu Pahat | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Beaufort | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Beluran | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Betong | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Bintulu | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Brunei | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| Bukit Gasing | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| Cameron Highlands | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Dungun | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Gombak | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Hulu Selangor | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Ipoh | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| Kangar | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Kelantan | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| Kemaman | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Keningau | +0 | Neutral | 0.0000 | -0.2942 |  | 5 | — | — | ✚ |
| Klang | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | — | — | ✚ |
| Kota Bharu | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Kota Tinggi | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Kuala Selangor | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Kuala Terengganu | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Kuantan | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | — | — | ✚ |
| Kudat | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| Kulai | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Kunak | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Lahad Datu | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| Limbang | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Lipis | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Mersing | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Pasir Puteh | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Penampang | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Petaling Jaya | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| Pontian | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Putatan | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Ranau | +0 | Neutral | 0.0000 | -0.2942 |  | 3 | — | — | ✚ |
| Rompin | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Sandakan | +0 | Neutral | 0.0000 | -0.2942 |  | 5 | — | — | ✚ |
| Sarikei | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Segamat | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | — | — | ✚ |
| Serian | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| Shah Alam | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| Sibu | +0 | Neutral | 0.0000 | -0.2942 |  | 10 | — | — | ✚ |
| Tawau | +0 | Neutral | 0.0000 | -0.2942 |  | 6 | — | — | ✚ |
| Tenom | +0 | Neutral | 0.0000 | -0.2942 |  | 5 | — | — | ✚ |
| Terengganu | +0 | Neutral | 0.0000 | -0.2942 |  | 4 | — | — | ✚ |
| Sabah | +0 | Neutral | -0.0118 | -0.3469 |  | 20 | — | — |  |
| France | +0 | Neutral | -0.0125 | -0.3500 |  | 6 | — | — | ✚ |
| Perlis | +0 | Neutral | -0.0198 | -0.3826 |  | 5 | — | — | ✚ |
| Iran | +0 | Neutral | -0.0510 | -0.5220 |  | 30 | — | — | ✚ |
| England | +0 | Neutral | -0.0522 | -0.5274 |  | 9 | — | — | ✚ |
| Melaka | +0 | Neutral | -0.0553 | -0.5412 |  | 8 | — | — |  |
| India | +0 | Neutral | -0.0744 | -0.6265 |  | 17 | — | — | ✚ |
| Parliament House | -1 | Slightly Negative | -0.2202 | -1.2779 |  | 6 | — | — |  |
| Semporna | -1 | Slightly Negative | -0.2360 | -1.3485 |  | 11 | — | — | ✚ |
| Miri | -1 | Slightly Negative | -0.2585 | -1.4490 |  | 5 | — | — | ✚ |
| Seremban | -1 | Slightly Negative | -0.2833 | -1.5598 |  | 6 | — | — | ✚ |
| Kedah | -1 | Slightly Negative | -0.2960 | -1.6165 |  | 16 | — | — | ✚ |
| West Asia | -2 | Negative | -0.5491 | -2.7473 | ⚠️ | 3 | — | — | ✚ |
| Indonesia | -3 | Very Negative | -0.6149 | -3.0412 | ⚠️ | 8 | — | — | ✚ |
| Strait of Hormuz | -3 | Very Negative | -0.6800 | -3.3321 | ⚠️ | 2 | — | — | ✚ |
### EVENT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| WAN IFRA ASIA MEDIA AWARDS 2025 | +3 | Very Positive | 0.9187 | 3.8102 | ⚠️ | 2 | — | — | ✚ |
| Court case | +3 | Very Positive | 0.7717 | 3.1534 | ⚠️ | 1 | — | — | ✚ |
| Trial | +3 | Very Positive | 0.6805 | 2.7460 | ⚠️ | 6 | — | — | ✚ |
| Probe | +2 | Positive | 0.5334 | 2.0888 | ⚠️ | 2 | — | — | ✚ |
| Appeal | +2 | Positive | 0.4619 | 1.7694 |  | 3 | — | — | ✚ |
| Hearing | +2 | Positive | 0.4418 | 1.6796 |  | 5 | — | — | ✚ |
| Investigation | +1 | Slightly Positive | 0.2363 | 0.7615 |  | 7 | — | — | ✚ |
| state election | +1 | Slightly Positive | 0.2195 | 0.6865 |  | 2 | — | — | ✚ |
| election | +1 | Slightly Positive | 0.1879 | 0.5453 |  | 13 | — | — | ✚ |
| World Cup | +1 | Slightly Positive | 0.1785 | 0.5033 |  | 27 | — | — | ✚ |
| rally | +0 | Neutral | 0.0711 | 0.0235 |  | 9 | — | — |  |
| campaign | +0 | Neutral | 0.0560 | -0.0440 |  | 21 | — | — |  |
| BN Candidate Announcement (NS) | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | — | — |  |
| ceramah | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | — | — |  |
| HAWANA X TM Media Event | +0 | Neutral | 0.0000 | -0.2942 |  | 11 | — | — |  |
| Johor State Election | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — |  |
| kempen | +0 | Neutral | 0.0000 | -0.2942 |  | 13 | — | — |  |
| majlis | +0 | Neutral | 0.0000 | -0.2942 |  | 8 | — | — |  |
| Negeri Sembilan State Election 2026 | +0 | Neutral | 0.0000 | -0.2942 |  | 21 | — | — |  |
| Sarawak State Election 2026 | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | — | — |  |
| walkabout | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | — | — |  |
| Piala Dunia | +0 | Neutral | 0.0000 | -0.2942 |  | 24 | — | — | ✚ |
| pilihan raya | +0 | Neutral | 0.0000 | -0.2942 |  | 7 | — | — | ✚ |
| pilihan raya negeri | +0 | Neutral | 0.0000 | -0.2942 |  | 3 | — | — | ✚ |
| Pilihan Raya Negeri Johor | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| PRN Negeri | +0 | Neutral | 0.0000 | -0.2942 |  | 17 | — | — | ✚ |
| sidang akhbar | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| event | +0 | Neutral | -0.0737 | -0.6234 |  | 23 | — | — |  |
| Charged | -1 | Slightly Negative | -0.2523 | -1.4213 |  | 8 | — | — | ✚ |
### CONCEPT

| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |
|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|
| artificial intelligence | +3 | Very Positive | 0.8885 | 3.6752 | ⚠️ | 1 | — | — | ✚ |
| Onn Hafiz 56-seats solo bid | +3 | Very Positive | 0.7334 | 2.9823 | ⚠️ | 1 | — | — |  |
| green technology | +3 | Very Positive | 0.6705 | 2.7013 | ⚠️ | 1 | — | — | ✚ |
| renewable energy | +2 | Positive | 0.3725 | 1.3700 |  | 4 | — | — | ✚ |
| water supply | +2 | Positive | 0.3697 | 1.3575 |  | 3 | — | — | ✚ |
| opposition | +2 | Positive | 0.3659 | 1.3405 |  | 4 | — | — | ✚ |
| perpaduan | +2 | Positive | 0.3213 | 1.1413 |  | 3 | — | — | ✚ |
| Super El Nino food security | +2 | Positive | 0.3125 | 1.1019 |  | 2 | — | — |  |
| copyright | +1 | Slightly Positive | 0.2622 | 0.8772 |  | 17 | — | — | ✚ |
| Wealth tax | +1 | Slightly Positive | 0.1482 | 0.3679 |  | 0 | — | — |  |
| MADANI government | +1 | Slightly Positive | 0.1071 | 0.1843 |  | 9 | — | — |  |
| AI | +0 | Neutral | 0.0974 | 0.1410 |  | 30 | — | — | ✚ |
| Subsidies & welfare aid | +0 | Neutral | 0.0134 | -0.2343 |  | 24 | — | — |  |
| Cost of living | +0 | Neutral | 0.0088 | -0.2548 |  | 7 | — | — |  |
| Bersatu own logo in N9 | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | — | — |  |
| Service tax | +0 | Neutral | 0.0000 | -0.2942 |  | 3 | — | — |  |
| Third force movement | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | — | — |  |
| UEC recognition | +0 | Neutral | 0.0000 | -0.2942 |  | 0 | — | — |  |
| fertiliser price | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| oil and gas | +0 | Neutral | 0.0000 | -0.2942 |  | 1 | — | — | ✚ |
| pork supply | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| TVET | +0 | Neutral | 0.0000 | -0.2942 |  | 2 | — | — | ✚ |
| mandate | -2 | Negative | -0.3425 | -1.8243 |  | 4 | — | — | ✚ |
---

## Methodology

1. **Entity Source:** Loaded from the 2026-07-21T14:00+08 extraction roster (257 Phase-1 entity names) plus the 78 canonical entities from the per-entity index. Roster names were merged into canonical entities by normalized name/alias matching (honorific-stripped); unmerged names were added as new entities (189 new).
2. **Context Extraction:** For each entity, search variants (canonical name + aliases + roster matches) were located in the 2026-07-21 raw source collection (24 sources, 24 processed, ~742864 chars). A context window (~140+170 chars) was extracted around each mention (markdown stripped, de-duplicated, capped at 30/entity).
3. **Sentiment Scoring:** Applied VADER to each context snippet; entity sentiment = mean compound across snippets.
4. **Score Mapping:** VADER compound (-1..+1) → 7-point Likert (-3..+3): +3 ≥0.6, +2 ≥0.3, +1 ≥0.1, 0 (-0.1..0.1), -1 >-0.3, -2 >-0.6, -3 ≤-0.6.
5. **Anomaly Detection:** Z-score on raw compound vs overall mean/std; flagged when |z| > 2.
6. **Coalition/Party Aggregation:** Persons + political-party/coalition orgs mapped via per-entity metadata and affiliation maps (FIGURE_AFFILIATIONS, ORG_TO_COALITION, analyst-extended NEW_FIGURE_AFFIL).

---

*Report generated by OpenCLaw Sentiment Analysis Pipeline (sentiment-analysis skill)*
*VADER: Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.*

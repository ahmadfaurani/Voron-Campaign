# POLITICAL NEWS COLLECTION REPORT
**Classification:** TLP:AMBER — Internal Operational Use  
**Report Date:** 2026-06-14 00:04 UTC  
**Collection Timestamp:** 20260614_000105  
**Collection Cycle:** Automated Daily Collection  

---

## EXECUTIVE SUMMARY

**Collection Status:** ✅ SUCCESS  
**Sources Monitored:** 7/7 (100%)  
**Total Content Collected:** 158,803 characters  
**Total Entities Extracted:** 63 unique entities  

---

## COLLECTION RESULTS

| Source | Status | Content Length | Entities Found | File |
|--------|--------|----------------|----------------|------|
| Bernama | ✅ Success | 16,520 chars | 22 | `20260614_000105_bernama.json` |
| Malaysiakini | ✅ Success | 16,559 chars | 23 | `20260614_000105_malaysiakini.json` |
| The Star | ✅ Success | 59,047 chars | 28 | `20260614_000105_thestar.json` |
| NST | ✅ Success | 1,369 chars | 2 | `20260614_000105_nst.json` |
| FMT | ✅ Success | 9,416 chars | 16 | `20260614_000105_fmt.json` |
| Daily Express | ✅ Success | 26,624 chars | 20 | `20260614_000105_dailyexpress.json` |
| Borneo Post | ✅ Success | 29,260 chars | 22 | `20260614_000105_borneopost.json` |

**Firecrawl API:** `http://localhost:3002/v2/scrape`  
**Output Directory:** `/home/p62operator/.openclaw/workspace-hoi/intelligence/raw/`

---

## ENTITY EXTRACTION SUMMARY

**Extraction Timestamp:** 2026-06-14T00:04:18 UTC  
**Output File:** `/home/p62operator/.openclaw/workspace-hoi/intelligence/entities/20260614_000105-entities.json`

### Entity Breakdown

| Category | Count | Description |
|----------|-------|-------------|
| PERSON | 17 | Politicians, officials, analysts |
| ORGANIZATION | 20 | Parties, coalitions, government bodies |
| LOCATION | 17 | States, constituencies, regions |
| EVENT | 7 | Political events, investigations, scandals |
| CONCEPT | 2 | Policies, narratives |
| **TOTAL** | **63** | Unique entities across all sources |

---

## TOP ENTITIES BY MENTION COUNT

### 📍 Top Persons (by mentions across sources)

| Rank | Entity | Mentions | Sources |
|------|--------|----------|---------|
| 1 | MB (Menteri Besar) | 127 | 6 sources |
| 2 | MP (Member of Parliament) | 125 | 6 sources |
| 3 | PM (Prime Minister) | 39 | 5 sources |
| 4 | Anwar (Anwar Ibrahim) | 28 | 3 sources |
| 5 | Minister | 17 | 5 sources |
| 6 | Fahmi (Fahmi Fadzil) | 7 | 3 sources |
| 7 | Onn (Onn Hafiz) | 6 | 1 source |

### 🏢 Top Organizations (by mentions across sources)

| Rank | Entity | Mentions | Sources |
|------|--------|----------|---------|
| 1 | Bernama | 125 | 2 sources |
| 2 | Malaysiakini | 120 | 1 source |
| 3 | PH (Pakatan Harapan) | 106 | 4 sources |
| 4 | PN (Perikatan Nasional) | 60 | 6 sources |
| 5 | NST | 46 | 7 sources |
| 6 | PAS | 32 | 4 sources |
| 7 | BN (Barisan Nasional) | 18 | 4 sources |
| 8 | MIC | 17 | 4 sources |
| 9 | BERSATU | 13 | 2 sources |
| 10 | PKR | 8 | 2 sources |

### 📍 Top Locations (by mentions across sources)

| Rank | Entity | Mentions | Sources |
|------|--------|----------|---------|
| 1 | Sabah | 109 | 4 sources |
| 2 | Sarawak | 47 | 3 sources |
| 3 | KL (Kuala Lumpur) | 30 | 4 sources |
| 4 | Johor | 20 | 3 sources |
| 5 | Penang | 7 | 1 source |
| 6 | Kuala Lumpur | 6 | 3 sources |
| 7 | Kuching | 6 | 1 source |
| 8 | Kota Kinabalu | 5 | 1 source |
| 9 | Kelantan | 5 | 2 sources |
| 10 | Petaling Jaya | 3 | 2 sources |

---

## KEY OBSERVATIONS

### Regional Focus
- **Sabah and Sarawak** dominate location mentions (156 combined), indicating strong Borneo political coverage
- Regional sources (Daily Express, Borneo Post) contributed significant content (55,884 chars combined)

### Political Landscape
- **PH (Pakatan Harapan)** leads coalition mentions with 106 mentions across 4 sources
- **PN (Perikatan Nasional)** follows with 60 mentions across all 6 sources that mentioned coalitions
- **BN (Barisan Nasional)** has 18 mentions across 4 sources

### Leadership Coverage
- **Anwar Ibrahim** (PM) is the most mentioned individual politician with 28 mentions
- **Fahmi Fadzil** (Communications Minister) has 7 mentions
- **Onn Hafiz** (Johor MB) has 6 mentions from Daily Express coverage

### Content Distribution
- **The Star** produced the most content (59,047 chars, 28 entities)
- **NST** had minimal content (1,369 chars, 2 entities) — may indicate scraping issues or low news volume
- Average content per source: 22,686 chars

---

## NEXT STEPS

1. **Sentiment Analysis** — Scheduled for 08:00 UTC daily
2. **Narrative Tracking** — Runs every 4 hours
3. **Daily Brief Generation** — Scheduled for 09:00 UTC

---

## SYSTEM STATUS

| Component | Status | Details |
|-----------|--------|---------|
| Firecrawl API | ✅ Operational | `http://localhost:3002` |
| Collection | ✅ Complete | 7/7 sources scraped |
| Entity Extraction | ✅ Complete | 63 entities extracted |
| Raw Storage | ✅ Saved | `/home/p62operator/.openclaw/workspace-hoi/intelligence/raw/` |
| Entity Storage | ✅ Saved | `/home/p62operator/.openclaw/workspace-hoi/intelligence/entities/` |

---

**Report Generated:** 2026-06-14 00:04 UTC  
**Skill Used:** `political-news-collection` + `entity-extraction`  
**Classification:** TLP:AMBER

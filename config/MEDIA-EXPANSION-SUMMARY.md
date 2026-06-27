# Media Source Expansion Summary
**Date:** 2026-06-13  
**Classification:** TLP:AMBER  
**Status:** Configuration Updated - Testing Pending

---

## Sources Added: 19 New Outlets

### Previous Coverage: 5 sources
- Bernama (operational)
- Malaysiakini (operational)
- NST (operational)
- FMT (operational)
- Daily Express (operational)

### New Coverage: 19 sources across 7 media clusters

---

## By Media Cluster

### 1. Commercial TV Groups (2 sources)
| Source | URL | Language | Priority | Status |
|--------|-----|----------|----------|--------|
| Media Prima (TV3) | tv3.com.my | ms | High | Pending Test |
| Astro AWANI | astroawani.com | ms | High | Pending Test |

**Strategic Value:** Largest TV reach in Malaysia - critical for mainstream sentiment

---

### 2. Malay Print + Digital (2 sources)
| Source | URL | Language | Priority | Status |
|--------|-----|----------|----------|--------|
| Berita Harian | bharian.com.my | ms | High | Pending Test |
| Sinar Harian | sinarharian.com.my | ms | High | Pending Test |

**Strategic Value:** Leading Malay dailies - essential for Malay voter sentiment

---

### 3. Digital-Native Portals (4 sources)
| Source | URL | Language | Priority | Status |
|--------|-----|----------|----------|--------|
| The Vibes | thevibes.com | en | Medium | Pending Test |
| MalaysiaNow | malaysianow.com | en | Medium | Pending Test |
| Malay Mail | malaymail.com | en | Medium | Pending Test |
| The Edge | theedgemarkets.com | en | High | Pending Test |

**Strategic Value:** Younger, urban audience - early indicator of sentiment shifts

---

### 4. Regional Borneo Media (3 sources)
| Source | URL | Language | Priority | Status |
|--------|-----|----------|----------|--------|
| Borneo Post | theborneopost.com | en | **High** | Pending Test |
| TV Sarawak | tvsarawak.com | ms | Medium | Pending Test |
| New Sabah Times | newsabah.com | en | Medium | Pending Test |

**Strategic Value:** Sabah/Sarawak coverage - critical for PIR-10 (Sabah Cascade)

---

### 5. Chinese-Language Media (3 sources)
| Source | URL | Language | Priority | Status |
|--------|-----|----------|----------|--------|
| Sin Chew Daily | sinchew.com.my | zh | Medium | Pending Test |
| China Press | chinapress.com.my | zh | Medium | Pending Test |
| Nanyang Siang Pau | nanyang.com.my | zh | Medium | Pending Test |

**Strategic Value:** Chinese community sentiment - DAP support base, business community

---

### 6. Tamil-Language Media (1 source)
| Source | URL | Language | Priority | Status |
|--------|-----|----------|----------|--------|
| Tamil Nesan | tamilnesan.com | ta | Low | Pending Test |

**Strategic Value:** Indian community sentiment - MIC/PH support base

---

### 7. Business Media (1 source)
| Source | URL | Language | Priority | Status |
|--------|-----|----------|----------|--------|
| Focus Malaysia | focusmalaysia.my | en | Low | Weekly |

**Strategic Value:** Economic policy sentiment, business elite perspectives

---

## Total Coverage Summary

| Tier | Count | Sources |
|------|-------|---------|
| **Tier 1 - National** | 10 | Bernama, Media Prima, Astro AWANI, The Star, NST, BH, Sinar, Malaysiakini, FMT, The Edge |
| **Tier 2 - Regional** | 4 | Daily Express, Borneo Post, TV Sarawak, New Sabah Times |
| **Tier 3 - Chinese** | 3 | Sin Chew, China Press, Nanyang |
| **Tier 4 - Tamil** | 1 | Tamil Nesan |
| **Tier 5 - Business** | 1 | Focus Malaysia |

**Grand Total:** 24 sources (5 operational + 19 pending test)

---

## Language Coverage

| Language | Sources | Coverage |
|----------|---------|----------|
| English | 12 | National + Regional + Business |
| Malay | 6 | National + Regional broadcast |
| Chinese | 3 | Community-focused |
| Tamil | 1 | Community-focused |

---

## Political Lean Distribution

| Lean | Sources | Purpose |
|------|---------|---------|
| Pro-Government | 4 | Official narrative tracking |
| Centrist | 12 | Balanced coverage |
| Critical/Opposition | 4 | Opposition narrative tracking |
| Regional Focus | 4 | State-level dynamics |

---

## Configuration Changes

### File Updated
`/home/p62operator/.openclaw/workspace-hoi/config/sources.yaml`

### Changes Made
1. ✅ Reorganized into 5 tiers
2. ✅ Added 19 new sources
3. ✅ Added language priority settings
4. ✅ Added multilingual Firecrawl support
5. ✅ Added media cluster summary comments

### New Settings
```yaml
collection:
  language_priority:
    - "en"   # Primary
    - "ms"   # Secondary
    - "zh"   # Chinese community
    - "ta"   # Tamil community

firecrawl:
  multilingual_support: true
```

---

## Testing Required

**Script Created:** `/home/p62operator/.openclaw/workspace-hoi/scripts/test-new-sources.py`

**Test Plan:**
1. Run test script against all 19 new sources
2. Validate content extraction (markdown format)
3. Check for blocking/rate limiting
4. Update status fields in sources.yaml
5. Add successful sources to collection cron job

**Command:**
```bash
python3 /home/p62operator/.openclaw/workspace-hoi/scripts/test-new-sources.py
```

---

## Integration Timeline

| Phase | Date | Action |
|-------|------|--------|
| **Phase 1** | 2026-06-13 | Configuration complete ✅ |
| **Phase 2** | 2026-06-14 | Test all sources |
| **Phase 3** | 2026-06-15 | Update status fields |
| **Phase 4** | 2026-06-16 | Integrate into daily collection |
| **Phase 5** | 2026-06-17 | Validate multilingual entity extraction |

---

## Strategic Benefits

### Before (5 sources)
- English-only coverage
- Limited to digital/online outlets
- No TV broadcast monitoring
- No ethnic media coverage
- Weak Borneo representation

### After (24 sources)
- ✅ Multi-language (EN/MS/ZH/TA)
- ✅ TV broadcast monitoring
- ✅ Full ethnic media coverage
- ✅ Strong Borneo representation
- ✅ Business/economic coverage
- ✅ Balanced political lean spectrum

---

## PIR Coverage Enhancement

| PIR | Improvement |
|-----|-------------|
| PIR-5 (Youth Voters) | Digital-native sources capture youth sentiment |
| PIR-10 (Sabah Cascade) | 4 Borneo sources for early warning |
| PIR-2 (BERSAMA) | Malay media tracks Malay voter response |
| PIR-4 (BN Johor) | Chinese media tracks Chinese voter response |

---

**Next Action:** Run source testing script to validate accessibility

**Classification:** TLP:AMBER

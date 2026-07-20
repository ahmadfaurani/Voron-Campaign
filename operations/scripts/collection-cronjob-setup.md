# VoronDRQ 7 Stakeholders - Automated Collection Cronjob

**Purpose:** Automatically collect C-suite stakeholder data from Tier 1 Malaysian banks  
**Frequency:** Every 4 hours  
**Classification:** TLP:AMBER  
**Workspace:** `/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/`

---

## Cronjob Configuration

```bash
hermes cron create "0 */4 * * *" \
  --name "VoronDRQ Stakeholder Collection" \
  --prompt "
Collect VoronDRQ 7 stakeholder data from Malaysian Tier 1 banks.

TARGETS (Priority Order):
1. Maybank Berhad (IN PROGRESS - 3/7 confirmed)
2. CIMB Bank Berhad
3. Public Bank Berhad
4. RHB Bank Berhad
5. Hong Leong Bank Berhad
6. AmBank Berhad
7. Bank Islam Malaysia Berhad
8. Bank Rakyat

SEARCH STRATEGY:
For each bank, search for:
- 'Chief Financial Officer' OR 'Group CFO'
- 'Chief Risk Officer' OR 'Group CRO'
- 'Chief Information Officer' OR 'Group CIO' OR 'Chief Technology Officer' OR 'CTO'
- 'Chief Information Security Officer' OR 'CISO' OR 'Head of Cybersecurity'
- 'Chief Compliance Officer' OR 'Head of Compliance'
- 'Chief Audit Executive' OR 'Head of Internal Audit'
- 'Head of GRC' OR 'Governance Risk Compliance'

Use web_search and web_extract tools.
Save findings to /home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/{bank-name}-stakeholders-{date}.md
Update master CSV: prospect-database-enriched-v{version}.csv

CONFIDENCE SCORING:
- HIGH (80-100): Exact role match + company match + Malaysia + official source URL
- MEDIUM (60-79): Related role OR subsidiary OR regional scope
- LOW (0-59): Role mismatch OR unclear affiliation OR outdated

VALIDATION:
- Track source URL for every contact
- Normalize role titles to standard 7 stakeholder roles
- Normalize company names to legal entity names
- NO fabrication or guessing of missing data

OUTPUT:
1. Markdown report per bank with confirmed + pending stakeholders
2. Updated CSV with all collected data
3. Telegram alert if HIGH confidence stakeholders found
4. Summary of collection progress (% coverage per bank)
"
```

---

## Expected Output per Run

### Collection Report (Markdown)
- Bank name
- Confirmed stakeholders (HIGH confidence)
- Pending stakeholders (MEDIUM/LOW confidence)
- Source URLs for audit trail
- Collection timestamp

### Database Update (CSV)
- Append new stakeholders to `prospect-database-enriched-v{version}.csv`
- Increment version number on each successful run
- Maintain deduplication by institution_name + role

### Telegram Alert
```
🎯 VoronDRQ Stakeholder Update

Bank: CIMB Bank Berhad
New HIGH Confidence: 2
- CFO: [Name]
- CRO: [Name]

Total Coverage: 5/7 (71%)
Database: v0.2
Sources: The Edge, NST, Fintech News MY
```

---

## Manual Triggers

To run collection immediately:
```bash
hermes cron run --job-id {job_id_from_list}
```

To check job status:
```bash
hermes cron list
```

---

## Data Retention

- **Markdown Reports:** Keep indefinitely (audit trail)
- **CSV Versions:** Keep last 10 versions
- **Source URLs:** Preserve in CSV for verification

---

## Troubleshooting

### Issue: Firecrawl MCP timeout
**Solution:** Fall back to web_search + web_extract (already configured)

### Issue: Duplicate entries in CSV
**Solution:** Run deduplication script:
```bash
cd /home/p62operator/.openclaw/workspace-hoi/voron-stakeholders
sort -u prospect-database-enriched-v*.csv > prospect-database-enriched-v{new}.csv
```

### Issue: Low confidence scores
**Solution:** Flag for manual review + LinkedIn export merge

---

**Created:** 2026-07-09  
**Last Updated:** 2026-07-09  
**Owner:** VoronDRQ 7 Campaign Team  
**Classification:** TLP:AMBER

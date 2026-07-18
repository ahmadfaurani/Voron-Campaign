#!/usr/bin/env python3
"""Apply v5.5 updates to the voron/main root master CSV (which already has v5.4 updates)."""
import csv

MASTER = '/home/p62operator/.openclaw/workspace-hoi/prospect-database-7stakeholders.csv'
ENRICHED_V55 = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.5.csv'

STAKEHOLDER_COLS = [
    'Chief Information Security Officer',
    'Head of Governance Risk & Compliance',
    'Chief Financial Officer',
    'Chief Risk Officer',
    'Head of Compliance',
    'Chief Information Officer',
    'Head of Internal Audit',
]

# Read the enriched v5.5 (authoritative for new data)
with open(ENRICHED_V55, 'r', encoding='utf-8-sig') as f:
    enriched_rows = {r['Institution_Name'].strip(): r for r in csv.DictReader(f) if r.get('Institution_Name','').strip()}

# Read root master CSV (voron/main version with v5.4 updates)
with open(MASTER, 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    master_rows = list(reader)

print(f'Loaded root master CSV: {len(master_rows)} rows')

# Only apply v5.5 NEW contacts (not notes/flags) to institutions that got new roles
ENRICHED_INSTITUTIONS = [
    'Sarawak State Financial Corporation (SSFC)',
    'DuitNow (by PayNet)',
    'FPX (by PayNet)',
    'JomPAY (by PayNet)',
    'Me2U (by PayNet)',
    'PayDirect (by PayNet)',
    'PayNet Card (by PayNet)',
]

updated = 0
for row in master_rows:
    name = row.get('Institution_Name', '').strip()
    if name in ENRICHED_INSTITUTIONS and name in enriched_rows:
        enriched = enriched_rows[name]
        changed = False
        for col in STAKEHOLDER_COLS:
            v_master = row.get(col, '').strip()
            v_enriched = enriched.get(col, '').strip()
            # Only update if master is empty AND enriched has real data (not a NOT FOUND/DUPLICATE/ENTITY note)
            if not v_master and v_enriched:
                if not v_enriched.startswith('NOT FOUND') and not v_enriched.startswith('DUPLICATE') and not v_enriched.startswith('ENTITY'):
                    row[col] = v_enriched
                    changed = True
        if changed:
            updated += 1
            filled = sum(1 for c in STAKEHOLDER_COLS if row.get(c,'').strip())
            print(f'  Updated: {name} -> {filled}/7')

# Write back master CSV
with open(MASTER, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(master_rows)

print(f'\nRoot master CSV updated: {updated} institutions enriched with v5.5 data')
print(f'File: {MASTER}')

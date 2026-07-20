#!/usr/bin/env python3
"""Update master 7stakeholders CSV with restored data from enriched v4.6."""
import csv

ENRICHED = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v4.6.csv'
MASTER = '/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv'

role_cols = [
    'Chief Information Security Officer',
    'Head of Governance Risk & Compliance',
    'Chief Financial Officer',
    'Chief Risk Officer',
    'Head of Compliance',
    'Chief Information Officer',
    'Head of Internal Audit'
]

# Read enriched v4.6
with open(ENRICHED, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    enriched_rows = list(reader)

# Build lookup by Institution_Name
enriched_lookup = {}
for r in enriched_rows:
    name = r.get('Institution_Name', '').strip()
    if name:
        enriched_lookup[name] = r

# Read master CSV
with open(MASTER, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    fieldnames = [fn for fn in reader.fieldnames if fn is not None]
    master_rows = list(reader)

# Clean None keys
for row in master_rows:
    if None in row:
        for k in list(row.keys()):
            if k is None:
                row.pop(k)

# Update master with enriched data where master is empty
updated = 0
for mrow in master_rows:
    name = mrow.get('Institution_Name', '').strip()
    erow = enriched_lookup.get(name)
    if erow:
        for col in role_cols:
            cur = mrow.get(col, '').strip()
            new = erow.get(col, '').strip()
            if new and not cur:
                mrow[col] = new
                updated += 1

print(f"Updated {updated} role fields in master CSV")

# Write updated master CSV
with open(MASTER, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(master_rows)

print(f"Wrote updated master CSV: {MASTER}")

# Stats
total = 0
filled = 0
for row in master_rows:
    for col in role_cols:
        total += 1
        if row.get(col, '').strip():
            filled += 1
print(f"Master CSV: {filled}/{total} roles filled ({100*filled/total:.1f}%)")
print(f"Master institutions: {len(master_rows)}")

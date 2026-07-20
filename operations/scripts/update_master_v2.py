#!/usr/bin/env python3
"""Update master 7stakeholders CSV - add missing institutions and update roles."""
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

# Build master lookup
master_names = {r.get('Institution_Name', '').strip() for r in master_rows}

# Update existing + add new
updated = 0
added = 0

# First update existing
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

# Then add missing institutions that have data in enriched
key_institutions = [
    'Zurich Life Insurance Malaysia Berhad',
    'Zurich Takaful Malaysia Berhad',
    'Manulife Takaful Malaysia Berhad',
    'Sun Life Malaysia Assurance Berhad',
    'UOB Malaysia Berhad',
]

for name in key_institutions:
    if name not in master_names:
        erow = enriched_lookup.get(name)
        if erow and any(erow.get(c, '').strip() for c in role_cols):
            new_row = {fn: erow.get(fn, '') for fn in fieldnames}
            master_rows.append(new_row)
            added += 1
            print(f"Added to master: {name}")

print(f"Updated {updated} role fields in master CSV")
print(f"Added {added} new institutions to master CSV")

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

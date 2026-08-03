#!/usr/bin/env python3
"""
Merge v5.90-clean and v6.0-merged-clean into a single canonical prospect database.

Strategy:
  - v6.0-merged-clean is the base (231 institutions, superset)
  - For each common institution, replace v6.0 cell with v5.90 data when:
      a) v6.0 cell is empty, OR
      b) v6.0 cell is 'NOT YET RESEARCHED' and v5.90 has real data
  - All v6.0-only institutions (16 fintech) preserved as-is

Output: prospect-database-canonical.csv
"""
import csv

ROLES = [
    'Chief Information Security Officer',
    'Head of Governance Risk & Compliance',
    'Chief Financial Officer',
    'Chief Risk Officer',
    'Head of Compliance',
    'Chief Information Officer',
    'Head of Internal Audit',
]
COLS = ['Tier', 'Segment', 'Institution_Name'] + ROLES

PLACEHOLDERS = {'', 'NOT YET RESEARCHED', 'NOT YET RESEARCHED '}


def load(f):
    with open(f, newline='') as fh:
        return {r['Institution_Name']: r for r in csv.DictReader(fh)}


def is_placeholder(val):
    return val.strip() in PLACEHOLDERS


def main():
    v6 = load('prospect-database-v6.0-merged-clean.csv')
    v590 = load('prospect-database-enriched-v5.90-clean.csv')

    merged_filled = 0      # v6 was empty
    merged_overwrote = 0  # v6 was 'NOT YET RESEARCHED'
    merged_named = 0
    merged_context = 0

    with open('prospect-database-v6.0-merged-clean.csv', newline='') as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)

    for row in rows:
        inst = row['Institution_Name']
        if inst in v590:
            for r in ROLES:
                v5_val = v590[inst][r].strip()
                v6_val = row[r].strip()
                if v5_val and not v6_val:
                    # v6 was empty — fill from v5.90
                    row[r] = v590[inst][r]
                    merged_filled += 1
                    if '|' in v5_val:
                        merged_named += 1
                    else:
                        merged_context += 1
                elif v5_val and is_placeholder(v6_val):
                    # v6 had placeholder — overwrite with real data
                    row[r] = v590[inst][r]
                    merged_overwrote += 1
                    if '|' in v5_val:
                        merged_named += 1
                    else:
                        merged_context += 1

    with open('prospect-database-canonical.csv', 'w', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=COLS)
        writer.writeheader()
        writer.writerows(rows)

    # Stats
    with open('prospect-database-canonical.csv', newline='') as fh:
        reader = csv.DictReader(fh)
        final_rows = list(reader)
        filled = sum(1 for row in final_rows for v in row.values() if v.strip())
        total = len(final_rows) * len(COLS)

    print('=== Merge complete ===')
    print(f'Institutions: {len(final_rows)}')
    print(f'Filled from empty: {merged_filled}')
    print(f'Overwrote placeholders: {merged_overwrote}')
    print(f'Total merged: {merged_filled + merged_overwrote} ({merged_named} named contacts, {merged_context} entity context)')
    print(f'Filled cells: {filled}/{total} ({filled/total*100:.1f}%)')
    print(f'Output: prospect-database-canonical.csv')


if __name__ == '__main__':
    main()

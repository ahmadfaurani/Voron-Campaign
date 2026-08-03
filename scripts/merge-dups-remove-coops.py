#!/usr/bin/env python3
"""
Merge duplicate cooperative entries, then remove ALL cooperatives from canonical file.

Duplicates identified:
  1. Koperasi PDRM (Polis Diraja Malaysia) ≡ Koperasi Polis Diraja Malaysia
  2. Koperasi Tentera Malaysia ≡ Koperasi Angkatan Tentera
  3. Bank Kerjasama Rakyat Malaysia Berhad ≡ Bank Rakyat Malaysia

Merge strategy per pair:
  - Keep the name from the row with MORE filled cells
  - For each role, prefer the non-empty, non-placeholder value (prefer named contacts > entity context > empty)
  - After merging, remove all rows where Segment contains 'Cooperatives' or institution is a koperasi

Output: prospect-database-canonical.csv (overwritten)
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


def is_placeholder(val):
    return val.strip() in PLACEHOLDERS


def cell_rank(val):
    """Higher is better: named contact (pipe) > entity context > placeholder."""
    v = val.strip()
    if v in PLACEHOLDERS:
        return 0
    if not v:
        return 0
    if '|' in v:
        return 3  # named contact with structured data
    return 2  # entity context annotation


def merge_rows(ra, rb):
    """Merge two rows, preferring better cell data. Returns merged row."""
    merged = dict(ra)  # start with A
    # Pick the name with more filled cells
    a_filled = sum(1 for r in ROLES if not is_placeholder(ra[r]))
    b_filled = sum(1 for r in ROLES if not is_placeholder(rb[r]))
    if b_filled > a_filled:
        merged['Institution_Name'] = rb['Institution_Name']
        merged['Segment'] = rb['Segment']
    # Merge each role cell
    for role in ROLES:
        if cell_rank(rb[role]) > cell_rank(ra[role]):
            merged[role] = rb[role]
    return merged


# Duplicate pairs: (name_a, name_b)
DUPLICATE_PAIRS = [
    ('Koperasi PDRM (Polis Diraja Malaysia)', 'Koperasi Polis Diraja Malaysia'),
    ('Koperasi Tentera Malaysia', 'Koperasi Angkatan Tentera'),
    ('Bank Kerjasama Rakyat Malaysia Berhad', 'Bank Rakyat Malaysia'),
]

# Names to remove (the loser of each merge + all cooperatives)
REMOVE_NAMES = set()
for a, b in DUPLICATE_PAIRS:
    REMOVE_NAMES.add(a)  # will keep only the merged survivor


def is_cooperative(row):
    seg = row['Segment'].strip().lower()
    name = row['Institution_Name'].strip().lower()
    return 'cooperat' in seg or 'koperasi' in name


def main():
    with open('prospect-database-canonical.csv', newline='') as fh:
        rows = list(csv.DictReader(fh))

    by_name = {r['Institution_Name']: r for r in rows}

    # Merge duplicates
    merged_survivors = []
    for a, b in DUPLICATE_PAIRS:
        ra = by_name[a]
        rb = by_name[b]
        merged = merge_rows(ra, rb)

        # Decide survivor name: prefer the one with more filled cells post-merge
        a_filled = sum(1 for r in ROLES if not is_placeholder(ra[r]))
        b_filled = sum(1 for r in ROLES if not is_placeholder(rb[r]))
        survivor_name = merged['Institution_Name']

        # Mark both originals for removal
        REMOVE_NAMES.add(a)
        REMOVE_NAMES.add(b)

        print(f'Merged: {a} + {b} → {survivor_name}')
        print(f'  A had {a_filled} filled, B had {b_filled} filled')
        for role in ROLES:
            if cell_rank(rb[role]) > cell_rank(ra[role]):
                print(f"  Took B's {role}: {rb[role][:60]}...")
        merged_survivors.append(merged)
        print()

    # Remove duplicates + all cooperatives
    before = len(rows)
    survivors = [r for r in rows if r['Institution_Name'] not in REMOVE_NAMES and not is_cooperative(r)]
    removed_coops = [r['Institution_Name'] for r in rows if is_cooperative(r) and r['Institution_Name'] not in REMOVE_NAMES]

    # Add back merged survivors (they're not cooperatives — e.g. Bank Rakyat is Development FIs)
    # Actually check: if the merged survivor is a cooperative, don't add it back
    for m in merged_survivors:
        if not is_cooperative(m):
            survivors.append(m)
            print(f'Kept merged survivor (non-coop): {m["Institution_Name"]}')
        else:
            print(f'Removed merged survivor (coop): {m["Institution_Name"]}')

    # Re-sort
    survivors.sort(key=lambda r: (int(r['Tier']), r['Segment'].strip(), r['Institution_Name'].strip()))

    after = len(survivors)
    coops_removed = before - after

    with open('prospect-database-canonical.csv', 'w', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=COLS)
        writer.writeheader()
        writer.writerows(survivors)

    # Stats
    filled = sum(1 for row in survivors for v in row.values() if v.strip())
    total = len(survivors) * len(COLS)

    print(f'\n=== Merge + removal complete ===')
    print(f'Before: {before} institutions')
    print(f'After: {after} institutions')
    print(f'Removed: {coops_removed} ({len(DUPLICATE_PAIRS)} duplicate pairs merged, rest were cooperatives)')
    print(f'Filled cells: {filled}/{total} ({filled/total*100:.1f}%)')
    print(f'Output: prospect-database-canonical.csv')


if __name__ == '__main__':
    main()

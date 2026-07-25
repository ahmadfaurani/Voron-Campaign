#!/usr/bin/env python3
"""Calculate coverage statistics for v5.45 CSV."""
import csv

csv_path = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.45.csv'
with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    headers = next(reader)
    rows = list(reader)

total_inst = len(rows)
field_names = headers[3:10]  # 7 stakeholder roles

# Overall stats
total_cells = total_inst * 7
filled_cells = 0
role_exists_cells = 0
not_found_cells = 0

for row in rows:
    for j in range(3, 10):
        val = row[j].strip() if j < len(row) else ''
        if not val:
            not_found_cells += 1
        elif 'NOT FOUND' in val:
            not_found_cells += 1
        elif 'ROLE EXISTS' in val:
            role_exists_cells += 1
        else:
            filled_cells += 1

print(f"Total institutions: {total_inst}")
print(f"Total stakeholder cells: {total_cells}")
print(f"  Filled (name identified): {filled_cells} ({filled_cells/total_cells*100:.1f}%)")
print(f"  Role exists, name not disclosed: {role_exists_cells} ({role_exists_cells/total_cells*100:.1f}%)")
print(f"  Not found: {not_found_cells} ({not_found_cells/total_cells*100:.1f}%)")
print(f"  Effective coverage (filled + role exists): {filled_cells + role_exists_cells} ({(filled_cells + role_exists_cells)/total_cells*100:.1f}%)")

# Per-role stats
print(f"\n--- Per-role coverage ---")
for j, role in enumerate(field_names, start=3):
    filled = 0
    exists = 0
    nf = 0
    for row in rows:
        val = row[j].strip() if j < len(row) else ''
        if not val or 'NOT FOUND' in val:
            nf += 1
        elif 'ROLE EXISTS' in val:
            exists += 1
        else:
            filled += 1
    print(f"  {role}: {filled} filled, {exists} role-exists, {nf} not-found")

# Per-institution coverage
print(f"\n--- Coverage distribution ---")
coverage_dist = {}
for row in rows:
    filled = sum(1 for j in range(3, 10) if j < len(row) and row[j].strip() and 'NOT FOUND' not in row[j])
    coverage_dist[filled] = coverage_dist.get(filled, 0) + 1

for k in sorted(coverage_dist.keys()):
    print(f"  {k}/7 filled: {coverage_dist[k]} institutions")

# Institutions with all 7 filled
print(f"\n--- Institutions with 7/7 filled ---")
for row in rows:
    filled = sum(1 for j in range(3, 10) if j < len(row) and row[j].strip() and 'NOT FOUND' not in row[j])
    if filled == 7:
        print(f"  {row[2]}")

# Changed institutions summary
print(f"\n--- Institutions updated in v5.45 ---")
updated_insts = ['SMBC', 'MARA', 'PUNB', 'Mizuho', 'ICBC', 'BNP Paribas', 'Citibank']
for row in rows:
    inst = row[2] if len(row) > 2 else ''
    for ui in updated_insts:
        if ui.lower() in inst.lower():
            filled = sum(1 for j in range(3, 10) if j < len(row) and row[j].strip() and 'NOT FOUND' not in row[j])
            exists = sum(1 for j in range(3, 10) if j < len(row) and 'ROLE EXISTS' in row[j])
            print(f"  {inst}: {filled} filled, {exists} role-exists, {7-filled-exists} not-found")
            break

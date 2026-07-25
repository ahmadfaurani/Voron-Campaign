#!/usr/bin/env python3
"""Search for SMBC and other institutions in v5.44 CSV."""
import csv

csv_path = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.44.csv'
with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    headers = next(reader)
    rows = list(reader)

# Search for SMBC, Sumitomo, Mizuho
search_terms = ['SMBC', 'Sumitomo', 'Mizuho', 'MUFG', 'Bank of Tokyo']
print("--- Japanese bank rows ---")
for i, row in enumerate(rows):
    inst_name = row[2] if len(row) > 2 else ''
    for t in search_terms:
        if t.lower() in inst_name.lower():
            print(f"\n=== Row {i}: {inst_name} ===")
            for j, h in enumerate(headers):
                if j < len(row) and row[j].strip():
                    print(f"  [{j}] {h}: {row[j][:150]}")
            break

# Also check what rows have "NOT FOUND" for CISO
print("\n\n--- All rows with CISO = NOT FOUND ---")
not_found_ciso = []
for i, row in enumerate(rows):
    if len(row) > 3 and 'NOT FOUND' in row[3]:
        not_found_ciso.append((i, row[2]))
print(f"Total: {len(not_found_ciso)} institutions with CISO NOT FOUND")
for idx, (i, name) in enumerate(not_found_ciso[:20]):
    print(f"  Row {i}: {name}")

# Count coverage per institution
print("\n\n--- Coverage summary ---")
for i, row in enumerate(rows):
    if len(row) < 10:
        continue
    filled = sum(1 for j in range(3, 10) if row[j].strip() and 'NOT FOUND' not in row[j])
    if filled <= 3:
        print(f"  Row {i}: {row[2]} - {filled}/7 filled")

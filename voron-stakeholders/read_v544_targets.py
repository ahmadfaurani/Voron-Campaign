#!/usr/bin/env python3
"""Read and analyze the v5.44 CSV for target institutions."""
import csv
import os

csv_path = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.44.csv'
with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    headers = next(reader)
    rows = list(reader)

print(f"Total rows: {len(rows)}")
print(f"Headers ({len(headers)}):")
for i, h in enumerate(headers):
    print(f"  [{i}] {h}")

# Find rows for SMBC, MARA, PUNB, Mizuho, ICBC, BNP Paribas, Citibank, TEKUN
targets = ['SMBC', 'MARA', 'PUNB', 'Mizuho', 'ICBC', 'BNP Paribas', 'Citibank', 'TEKUN']
print("\n--- Target institution rows ---")
for i, row in enumerate(rows):
    inst_name = row[2] if len(row) > 2 else ''
    for t in targets:
        if t.lower() in inst_name.lower():
            print(f"\n=== Row {i}: {inst_name} ===")
            for j, h in enumerate(headers):
                if j < len(row) and row[j].strip():
                    val = row[j][:120]
                    print(f"  [{j}] {h}: {val}")
            break

#!/usr/bin/env python3
import csv
with open('/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.24.csv', encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
roles = ['Chief Risk Officer','Head of Compliance','Chief Information Officer']
for r in rows:
    if r['Institution_Name'] in ('Soft Space Sdn Bhd','Prudential BSN Takaful Berhad'):
        print(f"\n=== {r['Institution_Name']} ===")
        for col in roles:
            print(f"  {col}: {r[col][:140]}")
print(f"\nTotal rows: {len(rows)}")

#!/usr/bin/env python3
import csv
import io

# Read the master CSV
with open('/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv', 'r', encoding='utf-8') as f:
    content = f.read()

reader = csv.DictReader(io.StringIO(content))
fieldnames = [f for f in reader.fieldnames if f is not None]
rows = []
for row in reader:
    clean_row = {k: v for k, v in row.items() if k is not None}
    rows.append(clean_row)

print(f"Master CSV rows: {len(rows)}")
updates = []

# Update HLB CISO
for row in rows:
    if row.get('Institution_Name') == 'Hong Leong Bank Berhad' or row.get('Institution') == 'Hong Leong Bank Berhad':
        # Find the CISO column
        for key in row:
            if 'CISO' in str(key) or 'Information Security' in str(key):
                row[key] = 'Dr. Simon Hoh (CISO) [TheOrg, conf 65]'
                updates.append(f"HLB {key} updated")
                break
        break

# Print column names to understand schema
if rows:
    print(f"Columns: {list(rows[0].keys())}")

# Write back
output = io.StringIO()
writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction='ignore')
writer.writeheader()
writer.writerows(rows)

with open('/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv', 'w', encoding='utf-8', newline='') as f:
    f.write(output.getvalue())

print(f"Master CSV updates: {updates}")
print("Master CSV written back")

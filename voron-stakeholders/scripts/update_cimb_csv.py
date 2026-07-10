#!/usr/bin/env python3
"""Update CIMB Bank Berhad stakeholder data in master database"""

import csv
from datetime import datetime

INPUT_FILE = "/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv"
OUTPUT_FILE = "/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv"

# CIMB stakeholders collected (HIGH confidence)
cimb_stakeholders = {
    "Chief Information Security Officer": "Charles Samuel (Group CISO)",
    "Head of Governance Risk & Compliance": "Kwan Keen Yew (Group Chief Integrity & Governance Officer)",
    "Chief Financial Officer": "Khairul Rifaie (Group Chief Financial & Strategy Officer)",
    "Chief Risk Officer": "Vera Handajani (Group CRO)",
    "Head of Compliance": "Kwan Keen Yew (Group Chief Legal & Compliance Officer)",
    "Chief Information Officer": "Ros Aziah Mohd Yusoff (Group CTO)",
    "Head of Internal Audit": "Amran Mohamad (Group Chief Internal Auditor)"
}

# Read the CSV
with open(INPUT_FILE, 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

print(f"Read {len(rows)} rows with fields: {fieldnames}")

# Update CIMB Bank Berhad row
updated = 0
for row in rows:
    if row['Institution_Name'] == 'CIMB Bank Berhad':
        print(f"Found CIMB row: {row}")
        for role, name in cimb_stakeholders.items():
            if role in row:
                row[role] = name
                print(f"  Updated {role}: {name}")
        updated += 1

if updated == 0:
    print("ERROR: CIMB Bank Berhad not found!")
    exit(1)

# Write back
with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"\n✅ Updated {updated} row(s)")
print(f"Output: {OUTPUT_FILE}")

# Show updated CIMB row
for row in rows:
    if row['Institution_Name'] == 'CIMB Bank Berhad':
        print(f"\nUpdated CIMB row:")
        for field in fieldnames:
            print(f"  {field}: {row[field]}")
        break

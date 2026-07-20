#!/usr/bin/env python3
"""VoronDRQ Enrichment v5.0 - Update from v4.9 to v5.0
Adds 10 new stakeholder roles across 5 institutions.
Classification: TLP:AMBER
"""
import csv
import shutil
from datetime import datetime

SRC = 'prospect-database-enriched-v4.9.csv'
DST = 'prospect-database-enriched-v5.0.csv'

# Copy v4.9 as base
shutil.copy2(SRC, DST)

# Read all rows
with open(DST, encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# Define updates: {institution_name_substring: {role_column: new_value}}
updates = {
    'Lonpac Insurance Bhd': {
        'Chief Financial Officer': 'Ng Seng Khin (Group Chief Financial Officer, designated 24 Jan 2025; CFO of Lonpac since 2019) [Official: lpicapital.com/about-us/management-team, conf 90]',
        'Head of Internal Audit': 'Irene Hwang Siew Ling (Group Chief Internal Auditor, designated 24 Jan 2025; Chief Internal Auditor of Lonpac since 1998; MIA CA, CPA Malaysia) [Official: lpicapital.com/about-us/management-team, conf 90]',
    },
    'Sun Life Malaysia Assurance Berhad': {
        'Chief Financial Officer': 'Lim Chin Har / Chew Lim (Chief Financial Officer) [LinkedIn: my.linkedin.com/in/chew-lim-209a05397, conf 65; cross-ref official mgmt page image: sunlifemalaysia.com/about-us/leadership/management-team]',
    },
    'Manulife Takaful Malaysia Berhad': {
        'Chief Financial Officer': 'Ng Chun Nam (Chief Financial Officer, Manulife Insurance Berhad - management shared) [Official: Manulife Annual Report 2024, conf 85]',
        'Chief Information Officer': 'Bernard Sia (Chief Information Officer, Manulife Insurance Berhad - management shared) [Official: Manulife Annual Report 2024, conf 85]',
    },
    'Manulife Insurance Berhad': {
        'Chief Financial Officer': 'Ng Chun Nam (Chief Financial Officer) [Official: Manulife Annual Report 2024, conf 85]',
        'Chief Information Officer': 'Bernard Sia (Chief Information Officer) [Official: Manulife Annual Report 2024, conf 85]',
    },
    'Kurnia Insurans (Malaysia) Berhad': {
        'Chief Information Officer': 'Ganesan Vaithilingam (CIO) [The Org: theorg.com/org/amgeneral-insurance-berhad, conf 60 - marked Unverified]; CEO: Puneet Pasricha (CEO, AmGeneral Insurance Berhad) [Official: amassurance.com.my, conf 90]',
        'Head of Compliance': 'Peter Ong (Chief Compliance Officer) [The Org: theorg.com/org/amgeneral-insurance-berhad, conf 60 - marked Unverified]',
        'Head of Internal Audit': 'Tan Bee Chuan (Chief Internal Auditor) [The Org: theorg.com/org/amgeneral-insurance-berhad, conf 60 - marked Unverified]',
    },
}

# Apply updates
changes = []
for row in rows:
    name = row['Institution_Name']
    for target_name, role_updates in updates.items():
        if target_name in name:
            for role_col, new_val in role_updates.items():
                old_val = row.get(role_col, '').strip()
                row[role_col] = new_val
                changes.append((name, role_col, 'FILLED' if not old_val else 'UPDATED', old_val[:40], new_val[:40]))

# Write updated CSV
with open(DST, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Summary
print(f"VoronDRQ Enrichment v5.0 Update Complete")
print(f"Source: {SRC}")
print(f"Output: {DST}")
print(f"Total institutions: {len(rows)}")
print(f"Changes made: {len(changes)}")
print()
for name, role, action, old, new in changes:
    print(f"  [{action}] {name}")
    print(f"    Role: {role}")
    print(f"    New:  {new}...")
    print()

# Calculate coverage stats
roles = ['Chief Information Security Officer','Head of Governance Risk & Compliance','Chief Financial Officer','Chief Risk Officer','Head of Compliance','Chief Information Officer','Head of Internal Audit']
total_filled = 0
total_possible = 0
full_count = 0
for r in rows:
    filled = sum(1 for role in roles if r.get(role,'').strip())
    total_filled += filled
    total_possible += 7
    if filled == 7:
        full_count += 1
print(f"\n=== Coverage Stats (v5.0) ===")
print(f"Total institutions: {len(rows)}")
print(f"Total roles filled: {total_filled}/{total_possible} ({100*total_filled/total_possible:.1f}%)")
print(f"Institutions with 7/7: {full_count}")
print(f"Institutions with >=1 contact: {sum(1 for r in rows if any(r.get(role,'').strip() for role in roles))}")

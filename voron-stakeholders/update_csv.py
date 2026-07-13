#!/usr/bin/env python3
"""Update enriched CSV v1.9 to v2.0 with new stakeholder data."""
import csv
import shutil
from datetime import datetime

SOURCE = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v1.9.csv'
DEST = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v2.0.csv'
MASTER = '/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv'

# Read the current CSV
rows = []
fieldnames = []
with open(SOURCE, 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        rows.append(row)

print(f"Read {len(rows)} rows from v1.9")

# Updates dictionary: institution_name -> {role_column: value}
updates = {
    # === ISLAMIC BANK SUBSIDIARIES (from parent bank group data) ===
    'CIMB Islamic Bank Berhad': {
        'Chief Information Security Officer': 'Charles Samuel (Group CISO) [Group-level: CIMB Bank]',
        'Head of Governance Risk & Compliance': 'Kwan Keen Yew (Group Chief Integrity & Governance Officer) [Group-level: CIMB Bank]',
        'Chief Financial Officer': 'Khairul Rifaie (Group Chief Financial & Strategy Officer) [Group-level: CIMB Bank]',
        'Chief Risk Officer': 'Vera Handajani (Group CRO) [Group-level: CIMB Bank]',
        'Head of Compliance': 'Kwan Keen Yew (Group Chief Legal & Compliance Officer) [Group-level: CIMB Bank]',
        'Chief Information Officer': 'Ros Aziah Mohd Yusoff (Group CTO) [group-level: CIMB Bank]',
        'Head of Internal Audit': 'Amran Mohamad (Group Chief Internal Auditor) [Group-level: CIMB Bank]',
    },
    'Maybank Islamic Berhad': {
        'Chief Information Security Officer': 'Devinder Singh (Group CISO) [Group-level: Maybank]',
        'Chief Financial Officer': 'Shafiq Abdul Jabbar (Group CFO) [Group-level: Maybank]',
        'Chief Risk Officer': 'Mohamed Rezwan Abdullah Ismail (Group CRO) [Group-level: Maybank]',
        'Chief Information Officer': 'Giorgio Migliarina (Group Chief Technology & Digital Officer) [Group-level: Maybank]',
    },
    'RHB Islamic Bank Berhad': {
        'Chief Information Security Officer': 'Soon Yap (CISO) [Group-level: RHB Bank]',
        'Head of Governance Risk & Compliance': 'Azman Shah Md Yaman (Group Chief Legal & Governance Officer) [Group-level: RHB Bank]',
        'Chief Financial Officer': 'Mohamed Bin Rastam Shahrom (Group CFO) [Group-level: RHB Bank]',
        'Chief Risk Officer': 'Dr Chong Han Hwee (Group CRO) [Group-level: RHB Bank]',
        'Head of Compliance': 'Fazlina Mohamed Ghazalli (Group CCO) [Group-level: RHB Bank]',
        'Chief Information Officer': 'Wong Kwang Leh (Group CTO) [Group-level: RHB Bank]',
        'Head of Internal Audit': 'Tan Boon Ching (Group Chief Internal Auditor) [Group-level: RHB Bank]',
    },
    'Hong Leong Islamic Bank Berhad': {
        'Chief Financial Officer': 'Malkit Singh (CFO) [Group-level: Hong Leong Bank]',
        'Chief Risk Officer': 'Justin Soong (Group CRO) [Group-level: Hong Leong Bank]',
        'Head of Compliance': 'Jack Babani (CCO) [Group-level: Hong Leong Bank]',
        'Chief Information Officer': 'William Streitberg (Chief Info & Tech Officer) [Group-level: Hong Leong Bank]',
        'Head of Internal Audit': 'Chua Yew Lim (Chief Internal Auditor) [Group-level: Hong Leong Bank]',
    },
    'AmBank Islamic Berhad': {
        'Chief Information Security Officer': 'Malini Kanesamoorthy (CISO) [Group-level: AmBank]',
        'Chief Financial Officer': 'Phuah Shok Cheng (Group CFO) [Group-level: AmBank]',
        'Chief Risk Officer': 'Shamsul Bahrom Bin Mohamed Ibrahim (Group CRO) [Group-level: AmBank]',
        'Head of Compliance': 'Faradina Binti Mohammad Ghouse (Group CCO) [Group-level: AmBank]',
        'Chief Information Officer': 'Wong Eng Teng (Group Chief Fintech & Technology Officer) [Group-level: AmBank]',
        'Head of Internal Audit': 'Ng Ek Leong (Group Chief Internal Auditor) [Group-level: AmBank]',
    },
    'Public Islamic Bank Berhad': {
        'Chief Financial Officer': 'Yik Sook Ling (CFO) [Group-level: Public Bank]',
        'Chief Risk Officer': 'Loh Jasmine (CRO) [Group-level: Public Bank]',
        'Head of Compliance': 'Tan Shien Doon (CCO) [Group-level: Public Bank]',
        'Chief Information Officer': 'Fam Yoke Fong (Senior GM, IT) [Group-level: Public Bank]',
        'Head of Internal Audit': 'Lim Then Fui (Group Chief Internal Auditor) [Group-level: Public Bank]',
    },

    # === INVESTMENT BANK SUBSIDIARIES (from parent bank group data) ===
    'Alliance Investment Bank Berhad': {
        'Chief Information Security Officer': 'William Song (Group CISO) [Group-level: Alliance Bank]',
        'Chief Financial Officer': 'Ronnie Royston Fernandiz (Group CFO) [Group-level: Alliance Bank]',
        'Chief Risk Officer': 'Jacob Abraham (Group CRO) [Group-level: Alliance Bank]',
        'Head of Compliance': 'Jacob Abraham (Group CRO, also responsible for Group Compliance) [Group-level: Alliance Bank]',
        'Chief Information Officer': 'Nantha Kumar Subramanian (Group Chief Digital & Info Officer) [Group-level: Alliance Bank]',
        'Head of Internal Audit': 'Andrew Ng Yin Min (Group Chief Internal Auditor) [Group-level: Alliance Bank]',
    },
    'Hong Leong Investment Bank Berhad': {
        'Chief Financial Officer': 'Malkit Singh (CFO) [Group-level: Hong Leong Bank]',
        'Chief Risk Officer': 'Justin Soong (Group CRO) [Group-level: Hong Leong Bank]',
        'Head of Compliance': 'Jack Babani (CCO) [Group-level: Hong Leong Bank]',
        'Chief Information Officer': 'William Streitberg (Chief Info & Tech Officer) [Group-level: Hong Leong Bank]',
        'Head of Internal Audit': 'Chua Yew Lim (Chief Internal Auditor) [Group-level: Hong Leong Bank]',
    },
    'Bank Rakyat Investment Bank Berhad': {
        'Chief Financial Officer': 'Nor Haimee Zakaria (Chief Finance Officer) [Group-level: Bank Rakyat]',
        'Chief Risk Officer': 'Azni Azaddin (Group Chief Risk Officer) [Group-level: Bank Rakyat]',
        'Head of Compliance': 'Jufree Soaidin (Group Chief Compliance Officer) [Group-level: Bank Rakyat]',
    },

    # === NEW DATA FROM WEB SEARCHES ===
    'EXIM Bank Malaysia': {
        'Head of Governance Risk & Compliance': 'Wan Noorazli Maula Wan Suleiman (Head of Legal, Governance & Recovery) [Official: exim.com.my]',
        'Chief Risk Officer': 'Abdul Hadi Jusoh (Chief Risk Officer) [Official: exim.com.my]',
        'Head of Compliance': 'Nizam Samad (Chief Compliance Officer) [Official: exim.com.my]',
        'Head of Internal Audit': 'Shahrul Farelli Zulkiffli (Chief Internal Auditor) [Official: exim.com.my]',
    },
    'Citibank Berhad': {
        'Chief Financial Officer': 'Tan Alyse (Chief Financial Officer/Controller) [LinkedIn: my.linkedin.com/in/tan-alyse-2658791a0]',
    },
    'Zurich Life Insurance Malaysia Berhad': {
        'Chief Financial Officer': 'Pauline Teoh (CEO, appointed 1 Nov 2024) [Official: zurich.com.my]',
    },
    'Zurich Takaful Malaysia Berhad': {
        'Chief Financial Officer': 'Nur Fatihah Mustafa (CEO, Zurich Takaful) [Official: zurich.com.my]',
    },
    'Prudential BSN Takaful Berhad': {
        'Chief Financial Officer': 'Kelvin Wong (Officer-in-Charge cum CFO) [Official: prubsn.com.my]',
    },
    'Sun Life Malaysia Assurance Berhad': {
        'Chief Financial Officer': 'Ho Teck Seng (President & CEO) [Official: sunlifemalaysia.com]',
    },
}

# Apply updates
updated_count = 0
new_stakeholder_count = 0
for row in rows:
    inst_name = row.get('Institution_Name', '').strip()
    if inst_name in updates:
        for role_col, value in updates[inst_name].items():
            current_val = row.get(role_col, '').strip()
            if not current_val:  # Only fill empty cells
                row[role_col] = value
                new_stakeholder_count += 1
        updated_count += 1

print(f"Updated {updated_count} institutions, added {new_stakeholder_count} new stakeholder entries")

# Write the updated CSV
with open(DEST, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Written to {DEST}")

# Now update the master CSV as well
master_rows = []
with open(MASTER, 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    master_fieldnames = reader.fieldnames
    for row in reader:
        master_rows.append(row)

print(f"\nRead {len(master_rows)} rows from master CSV")

# Apply same updates to master
master_updated = 0
master_new = 0
for row in master_rows:
    inst_name = row.get('Institution_Name', '').strip()
    if inst_name in updates:
        for role_col, value in updates[inst_name].items():
            current_val = row.get(role_col, '').strip()
            if not current_val:
                row[role_col] = value
                master_new += 1
        master_updated += 1

print(f"Updated {master_updated} institutions in master, added {master_new} new stakeholder entries")

# Also sync Maybank IB data from enriched to master
enriched_by_name = {r['Institution_Name']: r for r in rows}
for row in master_rows:
    inst_name = row.get('Institution_Name', '').strip()
    if inst_name in enriched_by_name:
        for col in fieldnames[3:]:  # Skip Tier, Segment, Institution_Name
            current = row.get(col, '').strip()
            enriched_val = enriched_by_name[inst_name].get(col, '').strip()
            if not current and enriched_val:
                row[col] = enriched_val
                master_new += 1

with open(MASTER, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=master_fieldnames)
    writer.writeheader()
    writer.writerows(master_rows)

print(f"Written to {MASTER}")

# Summary statistics
filled_count = 0
empty_count = 0
total_roles = 0
filled_roles = 0
roles = ['Chief Information Security Officer', 'Head of Governance Risk & Compliance', 
         'Chief Financial Officer', 'Chief Risk Officer', 'Head of Compliance', 
         'Chief Information Officer', 'Head of Internal Audit']

for row in rows:
    has_data = False
    for r in roles:
        val = row.get(r, '').strip()
        if val:
            filled_roles += 1
            has_data = True
    if has_data:
        filled_count += 1
    else:
        empty_count += 1
    total_roles += 7

print(f"\n=== SUMMARY ===")
print(f"Total institutions: {len(rows)}")
print(f"Filled (>=1 role): {filled_count}")
print(f"Empty (0 roles): {empty_count}")
print(f"Total roles possible: {total_roles}")
print(f"Total roles filled: {filled_roles}")
print(f"Overall coverage: {filled_roles}/{total_roles} ({100*filled_roles/total_roles:.1f}%)")

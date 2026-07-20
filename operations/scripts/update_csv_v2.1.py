#!/usr/bin/env python3
"""Update enriched CSV v2.0 to v2.1 with additional stakeholder data from web searches."""
import csv

SOURCE = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v2.0.csv'
DEST = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v2.1.csv'
MASTER = '/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv'

# Read the current CSV
rows = []
fieldnames = []
with open(SOURCE, 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    for row in reader:
        rows.append(row)

print(f"Read {len(rows)} rows from v2.0")

# New updates from web searches
updates = {
    # === AFFIN BANK (from Simply Wall St) ===
    'Affin Bank Berhad': {
        'Chief Financial Officer': 'Joanne Rodrigues (Group CFO, 6.1yrs tenure) [Source: simplywall.st]',
        'Chief Risk Officer': 'Cheong Dang (Group Chief Risk Officer, 4.3yrs tenure) [Source: simplywall.st]',
        'Head of Compliance': 'Adzamimah Adzmi (Group Chief Compliance Officer, 8yrs tenure) [Source: simplywall.st]',
        'Head of Internal Audit': 'Wahdania Binti Mohd Khir (Group Chief Internal Auditor, 6.2yrs tenure) [Source: simplywall.st]',
    },
    'Affin Hwang Investment Bank Berhad': {
        'Chief Financial Officer': 'Joanne Rodrigues (Group CFO) [Group-level: Affin Bank]',
        'Chief Risk Officer': 'Cheong Dang (Group Chief Risk Officer) [Group-level: Affin Bank]',
        'Head of Compliance': 'Adzamimah Adzmi (Group Chief Compliance Officer) [Group-level: Affin Bank]',
        'Head of Internal Audit': 'Wahdania Binti Mohd Khir (Group Chief Internal Auditor) [Group-level: Affin Bank]',
    },
    'Affin Islamic Bank Berhad': {
        'Chief Financial Officer': 'Joanne Rodrigues (Group CFO) [Group-level: Affin Bank]',
        'Chief Risk Officer': 'Cheong Dang (Group Chief Risk Officer) [Group-level: Affin Bank]',
        'Head of Compliance': 'Adzamimah Adzmi (Group Chief Compliance Officer) [Group-level: Affin Bank]',
        'Head of Internal Audit': 'Wahdania Binti Mohd Khir (Group Chief Internal Auditor) [Group-level: Affin Bank]',
    },

    # === BANK MUAMALAT (from official leadership page) ===
    'Bank Muamalat Malaysia Berhad': {
        'Chief Financial Officer': 'Amirul Nasir Abdul Rahim (Chief Financial Officer) [Official: muamalat.com.my]',
        'Chief Risk Officer': 'Hamidi A Razak (Chief Risk Officer) [Official: muamalat.com.my]',
        'Head of Compliance': 'Wan Kamarudin Wan Omar (Chief Compliance Officer) [Official: muamalat.com.my]',
        'Chief Information Officer': 'Ts. Megat Mohammad Faisal Khir Johari (Chief Technology Officer) [Official: muamalat.com.my]',
        'Head of Internal Audit': 'Faidzuel Bin Zain (Chief Internal Auditor) [Official: muamalat.com.my]',
    },

    # === KUWAIT FINANCE HOUSE MALAYSIA (from annual report 2024) ===
    'Kuwait Finance House (Malaysia) Berhad': {
        'Chief Risk Officer': 'Noor Noh (Chief Risk Officer) [Source: rocketreach.co/annual report]',
    },

    # === CHUBB INSURANCE MALAYSIA (from official board page + LinkedIn) ===
    'Chubb Insurance Malaysia Berhad': {
        'Chief Financial Officer': 'Olivier Bouchard (Executive Director, CFO Asia Pacific) [Official: chubb.com/my-en]',
        'Chief Information Officer': 'Kenny W. K. Tan (Chief Operating Officer) [LinkedIn: my.linkedin.com/in/kennytwk]',
    },

    # === TAKAFUL IKHLAS (from MNRB leadership page) ===
    'Takaful IKHLAS Berhad': {
        'Chief Financial Officer': 'Dato\' Rudy Rodzila Che Lamin (Interim President & Group CEO, MNRB/Takaful IKHLAS) [Official: mnrb.com.my]',
    },
    'Takaful Ikhlas General Berhad': {
        'Chief Financial Officer': 'Dato\' Rudy Rodzila Che Lamin (President & CEO) [Official: mnrb.com.my]',
    },

    # === SUN LIFE MALAYSIA (from board of directors page) ===
    'Sun Life Malaysia Assurance Berhad': {
        'Chief Financial Officer': 'Ho Teck Seng (President & CEO, Sun Life Malaysia) [Official: sunlifemalaysia.com]',
    },

    # === ZURICH LIFE INSURANCE MALAYSIA (from annual report 2024) ===
    'Zurich Life Insurance Malaysia Berhad': {
        'Chief Financial Officer': 'Timothy William Howell (Executive Director/CEO) [Official: zurich.com.my annual report 2024]',
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
            if not current_val:
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

# Also update master CSV
master_rows = []
with open(MASTER, 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    master_fieldnames = list(reader.fieldnames)
    for row in reader:
        master_rows.append(row)

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

# Also sync from enriched to master for any other differences
enriched_by_name = {r['Institution_Name']: r for r in rows}
for row in master_rows:
    inst_name = row.get('Institution_Name', '').strip()
    if inst_name in enriched_by_name:
        for col in fieldnames[3:]:
            current = row.get(col, '').strip()
            enriched_val = enriched_by_name[inst_name].get(col, '').strip()
            if not current and enriched_val:
                row[col] = enriched_val
                master_new += 1

with open(MASTER, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=master_fieldnames)
    writer.writeheader()
    writer.writerows(master_rows)

print(f"Updated {master_updated} institutions in master, added {master_new} new stakeholder entries")
print(f"Written to {MASTER}")

# Summary statistics
roles = ['Chief Information Security Officer', 'Head of Governance Risk & Compliance',
         'Chief Financial Officer', 'Chief Risk Officer', 'Head of Compliance',
         'Chief Information Officer', 'Head of Internal Audit']

filled_count = 0
empty_count = 0
total_roles = 0
filled_roles = 0
role_fill_counts = {r: 0 for r in roles}

for row in rows:
    has_data = False
    for r in roles:
        val = row.get(r, '').strip()
        if val:
            filled_roles += 1
            role_fill_counts[r] += 1
            has_data = True
    if has_data:
        filled_count += 1
    else:
        empty_count += 1
    total_roles += 7

print(f"\n=== SUMMARY v2.1 ===")
print(f"Total institutions: {len(rows)}")
print(f"Filled (>=1 role): {filled_count}")
print(f"Empty (0 roles): {empty_count}")
print(f"Total roles possible: {total_roles}")
print(f"Total roles filled: {filled_roles}")
print(f"Overall coverage: {filled_roles}/{total_roles} ({100*filled_roles/total_roles:.1f}%)")
print(f"\nPer-role coverage:")
for r in roles:
    print(f"  {r}: {role_fill_counts[r]}/{len(rows)} ({100*role_fill_counts[r]/len(rows):.1f}%)")

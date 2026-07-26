#!/usr/bin/env python3
"""Update CSV with Kenanga Investment Bank data"""
import csv

csv_path = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.50.csv'

# Read all rows
with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

updates_made = 0

# Kenanga Investment Bank Berhad - Management Team
kenanga_data = {
    'Chief Financial Officer': 'Cheong Boon Kak (Group Chief Financial and Operations Officer)',
    'Chief Risk Officer': 'Tai Yan Fee (Group Chief Risk Officer)',
    'Head of Compliance': 'Choo Siew Fun (Group Chief Compliance and Ethics Officer)',
    'Chief Information Officer': 'Low Jia Yee (Chief Technology Officer)',
    'Head of Internal Audit': 'Terence Tan Kian Meng (Group Chief Internal Auditor)',
    'Chief Information Security Officer': 'NOT FOUND - not publicly disclosed',
    'Head of Governance Risk & Compliance': 'NOT FOUND - no dedicated GRC head identified',
}

for i, row in enumerate(rows):
    name = row.get('Institution_Name', '')
    # Match Kenanga entries
    if 'Kenanga' in name and ('Investment Bank' in name or 'IB' in name or 'Kenanga Investment' in name):
        for role, value in kenanga_data.items():
            current = row.get(role, '')
            if not current or current.startswith('NOT FOUND'):
                if not value.startswith('NOT FOUND') or not current:
                    row[role] = value
                    updates_made += 1
                    print(f'  Updated row {i} ({name}) {role}: {value[:60]}')
        # Also check if this is a 0/7 or low-coverage row that should get all data
        role_cols = ['Chief Information Security Officer', 'Head of Governance Risk & Compliance', 'Chief Financial Officer', 'Chief Risk Officer', 'Head of Compliance', 'Chief Information Officer', 'Head of Internal Audit']
        filled = sum(1 for c in role_cols if row.get(c, '') and not row.get(c, '').startswith('NOT FOUND'))
        print(f'  Row {i} ({name}) now has {filled}/7 roles filled')

# Write back
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f'\nTotal updates: {updates_made}')
print(f'Total rows: {len(rows)}')

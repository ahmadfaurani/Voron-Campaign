#!/usr/bin/env python3
"""Update CSV with AIA and other newly scraped institution data"""
import csv

csv_path = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.50.csv'

# Read all rows
with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames) if reader.fieldnames else []
    rows = list(reader)

updates_made = 0

# AIA Bhd leadership data from https://www.aia.com.my/en/about-aia/aia-subsidiaries/about-aia-bhd/leadership-team.html
aia_data = {
    'Chief Financial Officer': 'Edwin Peh (Chief Financial Officer)',
    'Chief Risk Officer': 'Tan Teoh Guan (Chief Risk Officer)',
    'Chief Information Officer': 'Sherlly Yuan Xiaoli (Chief Technology Officer)',
    'Head of Compliance': 'Datin Veronica Selvanayagy (General Counsel - oversees Legal, Corporate Governance, Corporate Security)',
    'Head of Governance Risk & Compliance': 'Datin Veronica Selvanayagy (General Counsel - oversees Legal, Corporate Governance, Corporate Security)',
}

for i, row in enumerate(rows):
    name = row.get('Institution_Name', '')
    # Match AIA entries
    if 'AIA' in name and 'Bhd' in name and 'Takaful' not in name and 'General' not in name:
        for role, value in aia_data.items():
            if role in row:
                current = row.get(role, '')
                if not current or current.startswith('NOT FOUND') or current.strip() == '':
                    row[role] = value
                    updates_made += 1
                    print(f'  Updated row {i} ({name}) {role}: {value[:70]}')
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

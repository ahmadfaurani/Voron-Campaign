#!/usr/bin/env python3
"""Update v5.3 → v5.4: Add KWSP/EPF, PBSNB, PNSB, SenangPay, Wise, Nium/Instarem roles."""
import csv
import shutil

SRC = 'prospect-database-enriched-v5.3.csv'
DST = 'prospect-database-enriched-v5.4.csv'
shutil.copy2(SRC, DST)

# Define updates: (institution_name_substring, role_column, value)
updates = [
    # === KWSP / EPF (3 rows: Alternative Assets, Direct Investments, Real Estate) ===
    # All 3 rows get the same EPF leadership data
    ('KWSP Investment Division', 'Chief Information Security Officer',
     'Jasmine Goh (Head of Department – Digital Security) [Official: kwsp.gov.my/corporate/about-us/organisation-structure, conf 98]'),
    ('KWSP Investment Division', 'Head of Governance Risk & Compliance',
     'Nora Badaruddin (Head of Department – Integrity & Corporate Governance) [Official: kwsp.gov.my, conf 98]'),
    ('KWSP Investment Division', 'Chief Financial Officer',
     'Ahmad Rizal Omar (Chief Financial Officer) [Official: kwsp.gov.my, conf 98]'),
    ('KWSP Investment Division', 'Chief Risk Officer',
     'Rozlina Abdul Samad (Head of Department – Risk Management) [Official: kwsp.gov.my, conf 98]'),
    ('KWSP Investment Division', 'Head of Compliance',
     'Chong Yee Leng (Head of Department – Operations Compliance) [Official: kwsp.gov.my, conf 98]'),
    ('KWSP Investment Division', 'Chief Information Officer',
     'Afhzal Abdul Rahman (Chief Digital Technology Officer) [Official: kwsp.gov.my, conf 98]'),
    ('KWSP Investment Division', 'Head of Internal Audit',
     'Mohammad Nasir Ismail (Head of Department – Internal Audit) [Official: kwsp.gov.my, conf 98]'),

    # === Permodalan BSN Berhad (PBSNB) ===
    ('Permodalan BSN Berhad', 'Chief Financial Officer',
     'Suzylah Mohamed Noor (Head of Finance and HR Shared Services) [Official: pbsn.com.my/management-team/, conf 90]'),
    ('Permodalan BSN Berhad', 'Chief Risk Officer',
     'Wong Ching Fai @ Christopher (Head of Risk and Compliance) [Official: pbsn.com.my/management-team/, conf 95]'),
    ('Permodalan BSN Berhad', 'Head of Compliance',
     'Wong Ching Fai @ Christopher (Head of Risk and Compliance) [Official: pbsn.com.my/management-team/, conf 95]'),

    # === Permodalan Negeri Selangor Berhad (PNSB) ===
    ('Permodalan Negeri Selangor', 'Chief Financial Officer',
     'Ahmad Zamwawi Bin Ahmad Nazari (Senior General Manager – Finance) [Official: pnsb.com.my/info-korporat/, conf 95]'),
    ('Permodalan Negeri Selangor', 'Head of Internal Audit',
     'Mohammed Hanafi Bin Muhi (Senior Manager – Integrity, Audit & Governance) [Official: pnsb.com.my/info-korporat/, conf 95]'),
    ('Permodalan Negeri Selangor', 'Head of Governance Risk & Compliance',
     'Mohammed Hanafi Bin Muhi (Senior Manager – Integrity, Audit & Governance) [Official: pnsb.com.my/info-korporat/, conf 90]'),

    # === SenangPay Sdn Bhd ===
    ('SenangPay', 'Chief Financial Officer',
     'Mohd Mutalib (VP Finance and Account) [LinkedIn, conf 70]'),

    # === Wise (formerly TransferWise) Malaysia Sdn Bhd ===
    ('Wise (formerly TransferWise)', 'Chief Financial Officer',
     'Emmanuel Thomassin (Chief Financial Officer, Wise Plc global) [Official: owners.wise.com/governance/leadership-team, conf 95]'),
    ('Wise (formerly TransferWise)', 'Chief Information Officer',
     'Harsh Sinha (Chief Technology Officer, Wise Plc global) [Official: owners.wise.com/governance/leadership-team, conf 95]'),
    ('Wise (formerly TransferWise)', 'Head of Compliance',
     'Nita Patel (Group Chief Compliance Officer, Wise Plc global) [Official: owners.wise.com/governance/leadership-team, conf 95]'),

    # === Instarem Sdn Bhd (Nium) ===
    ('Instarem Sdn Bhd', 'Chief Financial Officer',
     'Andre Mancl (Chief Financial Officer, Nium global) [Official: nium.com/about-us, conf 95]'),
    ('Instarem Sdn Bhd', 'Chief Information Officer',
     'Sekhar Cidambi (Chief Technology Officer, Nium global) [Official: nium.com/about-us, conf 95]'),
    ('Instarem Sdn Bhd', 'Chief Risk Officer',
     'Amaresh Mohan (Chief Risk and Compliance Officer, Nium global) [Official: nium.com/about-us, conf 95]'),
    ('Instarem Sdn Bhd', 'Head of Compliance',
     'Amaresh Mohan (Chief Risk and Compliance Officer, Nium global) [Official: nium.com/about-us, conf 95]'),
]

# Read, update, write
rows = []
with open(DST, 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

update_count = 0
updated_institutions = set()
for row in rows:
    name = row.get('Institution_Name', '')
    for inst_substr, role_col, value in updates:
        if inst_substr.lower() in name.lower():
            if not row.get(role_col, '').strip():  # Only fill if empty
                row[role_col] = value
                update_count += 1
                updated_institutions.add(name)
                print(f'  UPDATED: [{name}] {role_col} = {value[:60]}...')

with open(DST, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f'\n=== Update Complete ===')
print(f'Total cells updated: {update_count}')
print(f'Institutions touched: {len(updated_institutions)}')
for inst in sorted(updated_institutions):
    print(f'  - {inst}')

# Verify coverage
roles = ['Chief Information Security Officer','Head of Governance Risk & Compliance','Chief Financial Officer','Chief Risk Officer','Head of Compliance','Chief Information Officer','Head of Internal Audit']
print(f'\n=== Coverage Check ===')
with open(DST, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    total_filled = 0
    total_possible = 0
    full_coverage = 0
    for row in reader:
        name = row.get('Institution_Name','').strip()
        if not name:
            continue
        filled = sum(1 for r in roles if row.get(r,'').strip())
        total_filled += filled
        total_possible += 7
        if filled == 7:
            full_coverage += 1
        # Show updated institutions
        for inst_substr, _, _ in updates:
            if inst_substr.lower() in name.lower():
                print(f'  [{filled}/7] {name}')
                break

print(f'\nTotal roles filled: {total_filled}/{total_possible} ({total_filled/total_possible*100:.1f}%)')
print(f'Full coverage (7/7): {full_coverage}')

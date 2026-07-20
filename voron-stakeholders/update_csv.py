#!/usr/bin/env python3
import csv
import io

# Read the current enriched CSV
with open('/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v3.7.csv', 'r', encoding='utf-8') as f:
    content = f.read()

# Parse CSV
reader = csv.DictReader(io.StringIO(content))
fieldnames = [f for f in reader.fieldnames if f is not None]
rows = []
for row in reader:
    # Remove None keys
    clean_row = {k: v for k, v in row.items() if k is not None}
    rows.append(clean_row)

print(f"Total rows: {len(rows)}")
updates = []

# Update 1: Hong Leong Bank Berhad - CISO = Dr. Simon Hoh
for row in rows:
    if row.get('Institution_Name') == 'Hong Leong Bank Berhad':
        old_ciso = row.get('Chief Information Security Officer', '')
        row['Chief Information Security Officer'] = 'Dr. Simon Hoh (CISO) [TheOrg: theorg.com/org/hong-leong-bank/org-chart/dr-simon-hoh, conf 65]'
        updates.append(f"HLB CISO updated")
        break

# Update 2: Hong Leong Islamic Bank Berhad - CISO = Dr. Simon Hoh (group-level)
for row in rows:
    if row.get('Institution_Name') == 'Hong Leong Islamic Bank Berhad':
        row['Chief Information Security Officer'] = 'Dr. Simon Hoh (CISO) [Group-level: Hong Leong Bank, TheOrg, conf 60]'
        updates.append(f"HLB Islamic CISO updated")
        break

# Update 3: Mizuho Bank Malaysia - Add CEO info as context
for row in rows:
    if row.get('Institution_Name') == 'Mizuho Bank (Malaysia) Berhad':
        row['Chief Information Security Officer'] = 'CEO: Daisuke Ihara (Executive Director/CEO, appointed 1 Jul 2026, Certified AML Specialist) [Official: mizuhogroup.com Profile of Directors PDF, conf 95]; Chairman: Dato Dr Zaha Rina binti Zahari'
        updates.append("Mizuho: added CEO Daisuke Ihara (context)")
        break

# Update 4: HSBC Malaysia - Add CEO confirmation to GRC field
for row in rows:
    if row.get('Institution_Name') == 'HSBC Bank Malaysia Berhad':
        row['Head of Governance Risk & Compliance'] = "Brian McGuire (Chief Risk & Compliance Officer) [TheOfficialBoard]; CEO: Dato Omar Siddiq (CEO and Head of Banking) [Official: hsbc.com.my, conf 95]"
        updates.append("HSBC: added CEO Dato Omar Siddiq to GRC field")
        break

# Update 5: Citibank Berhad - Add CEO info to GRC field
for row in rows:
    if row.get('Institution_Name') == 'Citibank Berhad':
        row['Head of Governance Risk & Compliance'] = 'CEO: Vikram Singh (CEO Citi Malaysia, effective 1 May 2023) [Official: theasianbanker.com, conf 90]; Country Lead: Divya Nair; Head of Commercial Bank: Shawn Khong [TheOfficialBoard]'
        updates.append("Citibank: added CEO Vikram Singh to GRC field")
        break

# Update 6: Credit Suisse Malaysia - Note about UBS merger
for row in rows:
    if row.get('Institution_Name') == 'Credit Suisse (Malaysia) Berhad':
        row['Chief Information Security Officer'] = 'ENTITY STATUS: Credit Suisse acquired by UBS; parent banks merged 31 May 2024. Entity likely absorbed/restructured. [Source: ubs.com press release, conf 85]'
        updates.append("Credit Suisse: added UBS merger status note")
        break

# Write updated CSV
output = io.StringIO()
writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction='ignore')
writer.writeheader()
writer.writerows(rows)
updated_content = output.getvalue()

# Write to v3.8
new_path = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v3.8.csv'
with open(new_path, 'w', encoding='utf-8', newline='') as f:
    f.write(updated_content)

print(f"\nUpdates made:")
for u in updates:
    print(f"  - {u}")
print(f"\nWritten to: {new_path}")
print(f"File size: {len(updated_content)} chars")

# Coverage stats for T1 banks
t1_banks = [
    'Maybank Berhad', 'CIMB Bank Berhad', 'Public Bank Berhad', 'RHB Bank Berhad',
    'Hong Leong Bank Berhad', 'AmBank (M) Berhad', 'Bank Islam Malaysia Berhad',
    'Bank Rakyat Malaysia', 'OCBC Bank (Malaysia) Berhad', 'UOB Malaysia Berhad',
    'HSBC Bank Malaysia Berhad', 'Standard Chartered Bank Malaysia Berhad',
    'Citibank Berhad', 'Bank of China (Malaysia) Berhad', 'ICBC (Malaysia) Berhad',
    'Credit Suisse (Malaysia) Berhad', 'Mizuho Bank (Malaysia) Berhad',
    'Sumitomo Mitsui Banking Corporation Malaysia Berhad', 'Deutsche Bank (Malaysia) Berhad',
    'BNP Paribas Malaysia Berhad', 'Bank Muamalat Malaysia Berhad',
    'Maybank Investment Bank Berhad', 'CIMB Investment Bank Berhad',
    'RHB Investment Bank Berhad', 'Hong Leong Investment Bank Berhad',
    'Public Investment Bank Berhad', 'Maybank Islamic Berhad',
    'CIMB Islamic Bank Berhad', 'RHB Islamic Bank Berhad',
    'AmBank Islamic Berhad', 'Hong Leong Islamic Bank Berhad', 'Public Islamic Bank Berhad'
]

print(f"\n--- T1 Bank Coverage (7 target roles) ---")
total_found = 0
total_target = 0
for bank in t1_banks:
    for row in rows:
        if row.get('Institution_Name') == bank:
            found = 0
            for col in ['Chief Information Security Officer', 'Head of Governance Risk & Compliance',
                       'Chief Financial Officer', 'Chief Risk Officer', 'Head of Compliance',
                       'Chief Information Officer', 'Head of Internal Audit']:
                val = row.get(col, '').strip()
                if val and not val.startswith('ENTITY STATUS') and not val.startswith('CEO:'):
                    found += 1
            total_found += found
            total_target += 7
            pct = round(found/7*100)
            print(f"  {bank}: {found}/7 ({pct}%)")
            break

print(f"\nTotal T1 coverage: {total_found}/{total_target} ({round(total_found/total_target*100)}%)")

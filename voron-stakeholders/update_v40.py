#!/usr/bin/env python3
"""Update enriched CSV from v3.9 to v4.0 with new stakeholder findings."""
import csv
import shutil

src = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v3.9.csv'
dst = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v4.0.csv'

# Copy v3.9 to v4.0
shutil.copy2(src, dst)

# Read all rows
with open(dst, 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# Define updates: {institution_name: {column_name: value}}
updates = {
    # Bank of China - CIO from LeadIQ
    'Bank of China (Malaysia) Berhad': {
        'Chief Information Officer': 'K.W.C. (Senior VP, Head of IT) [LeadIQ, MEDIUM-65]'
    },

    # Family Takaful Berhad -> STMKB (Takaful Malaysia subsidiary)
    'Family Takaful Berhad': {
        'Chief Financial Officer': 'New Kheng Chee (Group CFO) [takaful-malaysia.com.my, HIGH-90]',
        'Chief Information Officer': 'Nazaruddin Adha bin Md Noor (CTO) [takaful-malaysia.com.my, HIGH-90]',
        'Head of Compliance': 'Redzuan bin Abu [takaful-malaysia.com.my, HIGH-90]',
        'Head of Internal Audit': 'Zuhairi bin Ismail (Chief Internal Auditor) [takaful-malaysia.com.my, HIGH-90]',
        'Head of Governance Risk & Compliance': 'Shizal Fisham bin Ramli (Chief Governance Officer) [takaful-malaysia.com.my, HIGH-90]'
    },

    # General Takaful Berhad -> STMAB (Takaful Malaysia subsidiary)
    'General Takaful Berhad': {
        'Chief Financial Officer': 'New Kheng Chee (Group CFO) [takaful-malaysia.com.my, HIGH-90]',
        'Chief Information Officer': 'Nazaruddin Adha bin Md Noor (CTO) [takaful-malaysia.com.my, HIGH-90]',
        'Head of Compliance': 'Redzuan bin Abu [takaful-malaysia.com.my, HIGH-90]',
        'Head of Internal Audit': 'Zuhairi bin Ismail (Chief Internal Auditor) [takaful-malaysia.com.my, HIGH-90]',
        'Head of Governance Risk & Compliance': 'Shizal Fisham bin Ramli (Chief Governance Officer) [takaful-malaysia.com.my, HIGH-90]'
    },

    # HSBC Amanah Takaful -> FWD Takaful Berhad (acquired by FWD Group)
    'HSBC Amanah Takaful (Malaysia) Berhad': {
        'Chief Financial Officer': 'Muhammad Afiq bin Hamzah (Acting CFO) [fwd.com.my, HIGH-85]',
        'Head of Compliance': 'Lim Weng Leong [fwd.com.my, HIGH-85]'
    },

    # Takaful Am General Berhad -> Takaful Ikhlas General (MNRB Holdings)
    'Takaful Am General Berhad': {
        'Chief Financial Officer': 'Sharmini Perampalam (EVP & Group CFO) [mnrb.com.my, HIGH-90]',
        'Chief Information Officer': 'Aaron Loo (SVP & Group Chief Transformation Officer) [mnrb.com.my, MEDIUM-65]',
        'Head of Compliance': 'Abd Ghafur Ahmad (SVP & Group Chief Compliance Officer) [mnrb.com.my, HIGH-90]',
        'Head of Internal Audit': 'Haniza Filzah Hayani Abu Haniffa (SVP & Group Chief Internal Auditor) [mnrb.com.my, HIGH-90]'
    },

    # KWSP/EPF - 7/7 roles!
    'Kumpulan Wang Simpanan Pekerja (KWSP)': {
        'Chief Information Security Officer': 'Jasmine Goh (Head of Digital Security) [kwsp.gov.my via Wayback, MEDIUM-75]',
        'Head of Governance Risk & Compliance': 'Mohd Dali Jasmin (Head of Integrity & Corporate Governance) [kwsp.gov.my via Wayback, MEDIUM-75]',
        'Chief Financial Officer': 'Mohamad Hafiz Kassim (Chief Finance Officer) [kwsp.gov.my via Wayback, MEDIUM-75]',
        'Chief Risk Officer': 'Rozlina Abd Samad (Head of Risk Management) [kwsp.gov.my via Wayback, MEDIUM-75]',
        'Head of Compliance': 'Chong Yee Leng (Head of Operational Compliance) [kwsp.gov.my via Wayback, MEDIUM-75]',
        'Chief Information Officer': 'Afhzal Abdul Rahman (Chief Digital Technology Officer) [kwsp.gov.my via Wayback, MEDIUM-75]',
        'Head of Internal Audit': 'Mohammad Nasir Ismail (Head of Internal Audit) [kwsp.gov.my via Wayback, MEDIUM-75]'
    },

    # PNB - 5/7 roles (CISO and technology CIO not publicly disclosed)
    'Permodalan Nasional Berhad (PNB)': {
        'Head of Governance Risk & Compliance': 'Sahlawati Mustafa (Group Head, Compliance & Integrity) [pnb.com.my, HIGH-90]',
        'Chief Financial Officer': 'Mohd Irwan Ahmad Mustafa (Group Chief Strategy & Financial Officer) [pnb.com.my, HIGH-90]',
        'Chief Risk Officer': 'Mohd Azmir Mohd Jani (Chief Risk Officer) [pnb.com.my, HIGH-90]',
        'Head of Compliance': 'Sahlawati Mustafa (Group Head, Compliance & Integrity) [pnb.com.my, HIGH-90]',
        'Head of Internal Audit': 'Noramly Bachok @ Abdul Aziz (Group Head, Internal Audit) [pnb.com.my, HIGH-90]'
    },

    # SJPP - Acting Principal Officer found
    'Syarikat Jaminan Pembiayaan Perniagaan (SJPP)': {
        'Head of Governance Risk & Compliance': 'Juanita Rusmini binti Abdul Jalil (Acting Principal Officer) [sjpp.com.my, HIGH-80]'
    }
}

# Apply updates
updated_count = 0
for row in rows:
    name = row.get('Institution_Name', '')
    if name in updates:
        for col, val in updates[name].items():
            row[col] = val
        updated_count += 1
        print(f"Updated: {name}")

print(f"\nTotal institutions updated: {updated_count}")

# Clean rows: remove None keys and ensure all values are strings
clean_rows = []
for row in rows:
    clean_row = {}
    for k, v in row.items():
        if k is not None:
            clean_row[k] = str(v) if v is not None else ''
    # Ensure all fieldnames are present
    for fn in fieldnames:
        if fn not in clean_row:
            clean_row[fn] = ''
    clean_rows.append(clean_row)

# Write v4.0
with open(dst, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=[fn for fn in fieldnames if fn is not None])
    writer.writeheader()
    writer.writerows(clean_rows)

print(f"Written v4.0 to {dst}")

# Verify
with open(dst, 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows_v40 = list(reader)

    roles = ['Chief Information Security Officer','Head of Governance Risk & Compliance','Chief Financial Officer','Chief Risk Officer','Head of Compliance','Chief Information Officer','Head of Internal Audit']
    enriched = 0
    empty = 0
    total_cells = 0
    full_count = 0
    for r in rows_v40:
        filled = 0
        for role in roles:
            val = r.get(role) or ''
            if val.strip():
                filled += 1
                total_cells += 1
        if filled > 0:
            enriched += 1
        else:
            empty += 1
        if filled == 7:
            full_count += 1

    print(f"\nv4.0 Statistics:")
    print(f"  Total institutions: {len(rows_v40)}")
    print(f"  Enriched (>=1 role): {enriched}")
    print(f"  Empty (0 roles): {empty}")
    print(f"  Fully enriched (7/7): {full_count}")
    print(f"  Total filled cells: {total_cells}")
    print(f"  Cell fill rate: {total_cells/(len(rows_v40)*7)*100:.1f}%")
    print(f"  Enrichment rate: {enriched/len(rows_v40)*100:.1f}%")

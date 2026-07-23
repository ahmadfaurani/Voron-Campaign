#!/usr/bin/env python3
"""Update prospect database to v5.33 with new findings from enrichment session."""
import csv

# Read v5.32
with open('prospect-database-enriched-v5.32.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

print(f"Loaded {len(rows)} rows from v5.32")
print(f"Fields: {fieldnames}")

# ===== NEW FINDINGS FROM THIS SESSION =====

# 1. Sumitomo Mitsui Banking Corporation Malaysia Berhad
# From FY2025 Financial Statements PDF (scraped)
# Anand Mahadevan: Executive Director (appointed 26 May 2025), Regional CRO and Co-Head of Risk Management APAC
smbc_cro = 'Anand Mahadevan (Executive Director, Regional Chief Risk Officer and Co-Head of Risk Management Dept for APAC and India at SMBC Singapore; appointed 26 May 2025) [Official: SMBC Malaysia FY2025 Audited Financial Statements PDF, conf 85. Regional CRO role covering APAC. Board-level CRO oversight also via Lim Tuang Ooi (BRMC Chairman, INED). Hiroshi Nishimura resigned 9 May 2025.]'

# 2. Bank of America Malaysia Berhad -- NEW INSTITUTION (Tier 1 Licensed Bank)
# From FY2024 Financial Statements PDF (scraped)
# CEO/Executive Director: Gautam Padmakar Puntambekar (current, 2024)
# Previous CEO: Raymond Yeoh Cheng Seong (2023)
# CFO/Officer primarily responsible: Wong Poh Leng
boa_new = {
    'Tier': '1',
    'Segment': 'Licensed Banks',
    'Institution_Name': 'Bank of America Malaysia Berhad',
    'Chief Information Security Officer': 'NOT FOUND [Bank of America Malaysia FY2024 Financial Statements PDF does not name CISO. BAC Group CISO is shared. Source: BAMB FY2024 FS PDF, conf 90]',
    'Head of Governance Risk & Compliance': 'NOT FOUND [BAMB FY2024 FS PDF does not name GRC head. Source: BAMB FY2024 FS PDF, conf 90]',
    'Chief Financial Officer': 'Wong Poh Leng (Officer primarily responsible for the financial management of Bank of America Malaysia Berhad) [Official: BAMB FY2024 Financial Statements - Statutory Declaration pursuant to Section 251(1) Companies Act 2016, conf 95]. CEO/Executive Director: Gautam Padmakar Puntambekar (current CEO, appointed before FY2024) [Official: BAMB FY2024 FS - Directors and Remuneration, conf 95]. Previous CEO: Raymond Yeoh Cheng Seong (FY2023). Chairman: Anthony Lim Choon Eng (appointed 26 March 2024).',
    'Chief Risk Officer': 'NOT FOUND [BAMB FY2024 FS PDF does not name CRO. Source: BAMB FY2024 FS PDF, conf 90]',
    'Head of Compliance': 'NOT FOUND [BAMB FY2024 FS PDF does not name Head of Compliance/CCO. Source: BAMB FY2024 FS PDF, conf 90]',
    'Chief Information Officer': 'NOT FOUND [BAMB FY2024 FS PDF does not name CIO/CTO. Source: BAMB FY2024 FS PDF, conf 90]',
    'Head of Internal Audit': 'NOT FOUND [BAMB FY2024 FS PDF does not name CAE/CIA. Source: BAMB FY2024 FS PDF, conf 90]'
}

# 3. Zurich General Takaful Malaysia Berhad (= Zurich Takaful Malaysia Berhad in CSV)
# From AR 2025 PDF (scraped)
# CEO: Shamsul Azman Bin Alias
# Executive Directors: Matthew William Swinfen Cottrell (resigned 7 April 2025), Matthew James Vincent (appointed 7 August 2025)
zt_cfo = 'NOT FOUND [Zurich General Takaful AR 2025 PDF (full review, 266KB): No CFO named in Corporate Governance Statement or Notes to Financial Statements. CEO Shamsul Azman Bin Alias is the sole executive director with remuneration disclosed. Executive Directors Matthew Swinfen Cottrell (resigned Apr 2025) and Matthew James Vincent (appointed Aug 2025) have remuneration paid by other Zurich Group entities. No officer primarily responsible for financial management named in statutory declaration section. Source: Zurich General Takaful Malaysia Berhad AR 2025 PDF, conf 95]'

# ===== APPLY UPDATES =====
updates_applied = 0
new_rows_added = 0

for row in rows:
    name = row['Institution_Name']

    # SMBC updates - CRO
    if 'Sumitomo Mitsui' in name:
        old = row.get('Chief Risk Officer', '')
        if old.startswith('NOT FOUND') or not old:
            row['Chief Risk Officer'] = smbc_cro
            updates_applied += 1
            print(f"  UPDATED {name} [Chief Risk Officer]")
        else:
            row['Chief Risk Officer'] = old + ' | ' + smbc_cro
            updates_applied += 1
            print(f"  ENRICHED {name} [Chief Risk Officer]")

    # Zurich Takaful updates - CFO
    if 'Zurich Takaful' in name and 'General' not in name:
        old = row.get('Chief Financial Officer', '')
        if (old.startswith('NOT FOUND') and 'AR 2024' in old) or not old:
            row['Chief Financial Officer'] = zt_cfo
            updates_applied += 1
            print(f"  UPDATED {name} [Chief Financial Officer]")

# Check if Bank of America Malaysia already exists
boa_exists = any('Bank of America' in r['Institution_Name'] for r in rows)
if not boa_exists:
    rows.append(boa_new)
    new_rows_added += 1
    print(f"  ADDED NEW: Bank of America Malaysia Berhad")
else:
    print(f"  Bank of America Malaysia already exists - updating instead")
    for row in rows:
        if 'Bank of America' in row['Institution_Name']:
            for k, v in boa_new.items():
                if k in ['Tier', 'Segment', 'Institution_Name']:
                    continue
                if not row.get(k) or row[k].startswith('NOT FOUND'):
                    row[k] = v
                    updates_applied += 1

print(f"\nTotal updates applied: {updates_applied}")
print(f"New rows added: {new_rows_added}")
print(f"Total rows now: {len(rows)}")

# Write v5.33
outfile = 'prospect-database-enriched-v5.33.csv'
with open(outfile, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
print(f"\nWrote {outfile}")

#!/usr/bin/env python3
"""Update prospect database CSV with new findings from research session."""
import csv

# Read the current CSV
with open('prospect-database-enriched-v5.28.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

print(f"Loaded {len(rows)} rows, columns: {fieldnames}")

# Track updates
updates = []

# 1. Update iPay88 (both rows) with CRO from NTT DATA Payment Services
for idx, row in enumerate(rows):
    name = row['Institution_Name']
    
    if 'iPay88' in name and row['Chief Risk Officer'].startswith('NOT FOUND'):
        old_val = row['Chief Risk Officer']
        new_val = ("Khushwant Singh (Group Chief Risk & Credit Officer, NTT DATA Payment Services - parent co formerly GHL Systems)"
                   " [Source: LinkedIn linkedin.com/company/nttdataps/, conf 85 - confirmed via CRO Summit 2026 panel & eKYC webinar]")
        row['Chief Risk Officer'] = new_val
        updates.append((idx, name, 'Chief Risk Officer', old_val[:50], new_val[:80]))
    
    # Update CISO context for iPay88 to note parent company change
    if 'iPay88' in name and 'Alex Wah' in row.get('Chief Information Security Officer', ''):
        old_val = row['Chief Information Security Officer']
        if 'NTT DATA' not in old_val and 'GHL' not in old_val:
            row['Chief Information Security Officer'] = old_val + " [Parent: NTT DATA Payment Services (formerly GHL Systems Berhad), acquired by NTT DATA Japan]"
            updates.append((idx, name, 'Chief Information Security Officer', '[context update]', '[added NTT DATA parent context]'))

# 2. Update senangPay with DOKU acquisition context
for idx, row in enumerate(rows):
    if 'SenangPay' in row['Institution_Name'] or 'senangPay' in row['Institution_Name']:
        name = row['Institution_Name']
        for col in ['Chief Information Security Officer', 'Head of Governance Risk & Compliance', 
                     'Chief Risk Officer', 'Head of Compliance', 'Chief Information Officer', 'Head of Internal Audit']:
            if row[col].startswith('NOT FOUND') and 'DOKU' not in row[col]:
                old_val = row[col]
                row[col] = ("NOT FOUND [senangPay acquired by DOKU (Indonesia) in 2022; LinkedIn shows 51-200 employees;"
                           " key employees: Joshua Abraham, Kenneth Kuan, Muhammad Hasni Madzaki, Paulina Vina - roles unconfirmed."
                           " Source: linkedin.com/company/senangpay/]")
                updates.append((idx, name, col, old_val[:50], '[DOKU context added]'))
        # Update CFO context
        if 'Mohd Mutalib' in row.get('Chief Financial Officer', ''):
            row['Chief Financial Officer'] = row['Chief Financial Officer'] + " [senangPay is now a DOKU Company (acquired 2022)]"
            updates.append((idx, name, 'Chief Financial Officer', '[context update]', '[DOKU context added]'))

# 3. Update Billplz with LinkedIn employee context
for idx, row in enumerate(rows):
    if 'Billplz' in row['Institution_Name']:
        name = row['Institution_Name']
        for col in ['Chief Information Security Officer', 'Head of Governance Risk & Compliance',
                     'Chief Financial Officer', 'Chief Risk Officer', 'Head of Compliance',
                     'Chief Information Officer', 'Head of Internal Audit']:
            if row[col].startswith('NOT FOUND') and 'Arzumy' not in row[col] and 'LinkedIn' not in row[col]:
                old_val = row[col]
                row[col] = ("NOT FOUND [Billplz: 11-50 employees, Shah Alam. LinkedIn key employees: Arzumy MD (likely CEO/founder),"
                           " Azril Azmi, Muhammad Fariduddin Fauzi, Nazroof Hakim - role titles unconfirmed."
                           " Source: linkedin.com/company/billplz/]")
                updates.append((idx, name, col, old_val[:50], '[Billplz LinkedIn context added]'))

# 4. Update Jirnexu with LinkedIn context
for idx, row in enumerate(rows):
    if 'Jirnexu' in row['Institution_Name']:
        name = row['Institution_Name']
        for col in ['Chief Information Security Officer', 'Head of Governance Risk & Compliance',
                     'Chief Financial Officer', 'Chief Risk Officer', 'Head of Compliance',
                     'Chief Information Officer', 'Head of Internal Audit']:
            if row[col].startswith('NOT FOUND') and ('Jirnexu' not in row[col] or 'LinkedIn' not in row[col]):
                old_val = row[col]
                row[col] = ("NOT FOUND [Jirnexu: 51-200 employees, Bangsar South KL. Behind RinggitPlus.com & CompareHero."
                           " LinkedIn notable employee: Ali Fancy - role unconfirmed. Founded 2012."
                           " Source: linkedin.com/company/jirnexu/]")
                updates.append((idx, name, col, old_val[:50], '[Jirnexu LinkedIn context added]'))

# 5. Update Soft Space with additional context
for idx, row in enumerate(rows):
    if 'Soft Space' in row['Institution_Name']:
        name = row['Institution_Name']
        for col in ['Chief Information Security Officer', 'Head of Governance Risk & Compliance',
                     'Chief Risk Officer', 'Head of Compliance', 'Head of Internal Audit']:
            if row[col].startswith('NOT FOUND') and 'LinkedIn' not in row[col]:
                old_val = row[col]
                row[col] = ("NOT FOUND [Soft Space: No LinkedIn company page (tried 5 URL variants, all 404)."
                           " Existing fills: Rick Leong (Acting CFO), Nicholas Lim (CTO)."
                           " Source: softspace.com.my, theorg.com]")
                updates.append((idx, name, col, old_val[:50], '[Soft Space context added]'))

# 6. Update KDI Save with research context
for idx, row in enumerate(rows):
    if 'KDI Save' in row['Institution_Name']:
        name = row['Institution_Name']
        for col in ['Chief Information Security Officer', 'Head of Governance Risk & Compliance',
                     'Chief Financial Officer', 'Chief Risk Officer', 'Head of Compliance',
                     'Chief Information Officer', 'Head of Internal Audit']:
            if row[col].startswith('NOT FOUND') and ('KDI' not in row[col] or 'search' not in row[col].lower()):
                old_val = row[col]
                row[col] = ("NOT FOUND [KDI Save: No LinkedIn company page (404). No public website found."
                           " Web search returned only Korean Development Institute results. Likely early-stage digital bank.]")
                updates.append((idx, name, col, old_val[:50], '[KDI Save context added]'))

# 7. Update PayNet NOT FOUND entries with anti-bot context
for idx, row in enumerate(rows):
    name = row['Institution_Name']
    if name == 'PayNet (PayNet Malaysia Sdn Bhd)':
        for col in ['Head of Governance Risk & Compliance', 'Chief Risk Officer', 'Head of Compliance', 'Head of Internal Audit']:
            if row[col].startswith('NOT FOUND') and 'anti-bot' not in row[col].lower():
                old_val = row[col]
                row[col] = ("NOT FOUND [PayNet website anti-bot protected - Firecrawl stealth/enhanced proxy failed."
                           " No LinkedIn page (tried 2 URLs, both 404). Existing fills: Meling Mudin (CISO),"
                           " Tan Wei Tze (CFO), Teh Lip Guan (CTO).]")
                updates.append((idx, name, col, old_val[:50], '[PayNet anti-bot context added]'))

# Write updated CSV
output_file = 'prospect-database-enriched-v5.29.csv'
with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"\nTotal updates made: {len(updates)}")
print(f"Output file: {output_file}")

# Print summary of updates
for idx, name, col, old, new in updates:
    print(f"  Row {idx}: {name} | {col}: {new}")

# Count fills before and after
leadership_cols = ['Chief Information Security Officer', 'Head of Governance Risk & Compliance',
                    'Chief Financial Officer', 'Chief Risk Officer', 'Head of Compliance',
                    'Chief Information Officer', 'Head of Internal Audit']

actual_fills = 0
for col in leadership_cols:
    for r in rows:
        val = r[col].strip()
        if not val.startswith('NOT FOUND'):
            actual_fills += 1

total_cells = len(rows) * 7
print(f"\nActual name fills: {actual_fills}/{total_cells} ({actual_fills*100/total_cells:.1f}%)")
print(f"NOT FOUND: {total_cells - actual_fills}/{total_cells} ({(total_cells - actual_fills)*100/total_cells:.1f}%)")

# Per-column breakdown
print("\n=== Per-column fill rates ===")
for col in leadership_cols:
    filled = sum(1 for r in rows if not r[col].strip().startswith('NOT FOUND'))
    print(f"  {col}: {filled}/{len(rows)} ({filled*100/len(rows):.1f}%)")

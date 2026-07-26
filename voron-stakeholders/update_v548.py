#!/usr/bin/env python3
"""Update prospect-database-enriched-v5.47.csv with v5.48 findings."""
import csv
import shutil
from datetime import datetime

csv_path = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.47.csv'

# Create backup
backup_path = csv_path.replace('v5.47', 'v5.47.bak')
shutil.copy2(csv_path, backup_path)
print(f"Backup created: {backup_path}")

# Read the CSV
with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    headers = next(reader)
    rows = list(reader)

print(f"Loaded {len(rows)} institutions")
print(f"Headers: {headers}")

# Define updates: (institution_name_match, column_index, new_value)
updates = [
    # Berjaya Sompo - CIO gap is genuine. Official leadership page lists 8 members, no CIO.
    (
        'Berjaya Sompo Insurance',
        8,  # Chief Information Officer
        'NOT FOUND [Genuine gap confirmed Jul 2026: Official leadership-team page (berjayasompo.com.my/leadership-team) lists 8 Management Team members: CEO (Soo Wai Har), CCO (Vanessa Ngew), Chief Consumer & SME Officer (Phang Yin Peng), CFO (Rina Aprila Afianty), CHRO (Jun Ishak), Chief Compliance & Legal Officer (Tricia Mallika Appaduray), COO (Eng Chun Mun), Chief Claims Officer (Teh Yau Kun). No dedicated CIO/CTO listed. IT oversight likely falls under COO Eng Chun Mun.]'
    ),
    # Tokio Marine Life - GRC gap should be composite (CRO + Compliance)
    (
        'Tokio Marine Life Insurance Malaysia',
        4,  # Head of Governance Risk & Compliance
        'Andrew Ngou Chee Mun (CRO) + Loh Chee Hoong (Head of Compliance) [Composite - GRC function split between Risk and Compliance; no dedicated GRC head. Official leadership page (tokiomarine.com/my/en/life/about-us/our-board-of-directors-and-management-team.html) lists 9 SMT members, none with GRC title. CRO and Head of Compliance sourced from Malaysian Insurance Directory 2025/2026.]'
    ),
    # Maybank IB - GRC gap should be composite (CRO + CCO)
    (
        'Maybank Investment Bank',
        4,  # Head of Governance Risk & Compliance
        'Cheryl Cheng Siew Ying (CRO) + Farhan Nor Diyana Samsudin (CCO) [Composite - GRC function split between Risk and Compliance at Maybank IB level; no dedicated GRC head. Group-level Maybank has Ho Mun Wah as Head of GRC but not at IB subsidiary. CRO and CCO confirmed via Maybank IB SORMIC FY2023.]'
    ),
    # Boost Bank - GRC gap should be composite (CRO + CCO)
    (
        'Boost Bank Berhad',
        4,  # Head of Governance Risk & Compliance
        'Puteri Syurga (CRO) + Dr Mohanamerry Vedamanikam (CCO) [Composite - GRC function split between Risk and Compliance; no dedicated GRC head. Official leadership page (myboostbank.co/our-leadership-boost-bank) lists 6 members, no GRC head. CRO and CCO confirmed from official source.]'
    ),
    # Bank Rakyat - Audit gap is genuine. Management Committee page lists 8 members, no Head of Internal Audit.
    (
        'Bank Rakyat Malaysia',
        9,  # Head of Internal Audit
        'NOT FOUND [Genuine gap confirmed Jul 2026: Official Management Committee page (bankrakyat.com.my/portal-main/leaders/management-committee) lists 8 members: Group CEO (Ahmad Shahril Mohd Shariff), CFO (Nor Haimee Zakaria), Chief Retail Banking Officer (Khairudin Abdul Rahman), COO (Amren Faisal Fadzil), Chief Strategy & Sustainability Officer (Mohamad Taufik Mahamad Zakaria), Group CRO (Azni Azaddin), Chief People Officer (Elina Ahmad), Group Chief Compliance Officer (Jufree Soaidin). No dedicated Head of Internal Audit listed on management committee. Internal Audit function likely reports to Board Audit Committee directly.]'
    ),
]

# Apply updates
update_count = 0
for inst_match, col_idx, new_value in updates:
    for row in rows:
        if inst_match.lower() in row[2].lower():
            old_val = row[col_idx][:100]
            row[col_idx] = new_value
            update_count += 1
            print(f"Updated: {row[2]} | Col {col_idx} ({headers[col_idx]})")
            print(f"  Old: {old_val}...")
            print(f"  New: {new_value[:100]}...")
            break

print(f"\nTotal updates applied: {update_count}")

# Write updated CSV as v5.48
new_csv_path = csv_path.replace('v5.47', 'v5.48')
with open(new_csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"New CSV written: {new_csv_path}")

# Calculate new statistics
filled = 0
total = 0
gaps_by_col = [0]*7
for row in rows:
    for i in range(3, 10):
        total += 1
        val = row[i].strip()
        if val and not val.upper().startswith('NOT FOUND') and not val.upper().startswith('ENTITY NON-EXISTENT'):
            filled += 1
        else:
            gaps_by_col[i-3] += 1

print(f"\nNew Statistics (v5.48):")
print(f"  Filled cells: {filled}/{total} ({filled/total*100:.1f}%)")
print(f"  Gaps: {total-filled} ({(total-filled)/total*100:.1f}%)")
print(f"\nGaps by role:")
role_names = ['CISO', 'GRC', 'CFO', 'CRO', 'Compliance', 'CIO', 'Audit']
for i, name in enumerate(role_names):
    print(f"  {name}: {gaps_by_col[i]}")

# Count 1-gap institutions
one_gap_count = 0
for row in rows:
    gap_count = 0
    for i in range(3, 10):
        val = row[i].strip()
        if not val or val.upper().startswith('NOT FOUND') or val.upper().startswith('ENTITY NON-EXISTENT'):
            gap_count += 1
    if gap_count == 1:
        one_gap_count += 1

print(f"\n  Institutions with exactly 1 gap: {one_gap_count}")

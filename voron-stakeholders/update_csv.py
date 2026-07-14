#!/usr/bin/env python3
"""Update enriched CSV v3.4 → v3.5 with new findings."""
import csv
import shutil

# Read the current CSV
src = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v3.4.csv'
dst = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v3.5.csv'

# Copy v3.4 to v3.5 as starting point
shutil.copy2(src, dst)

# Read all rows
with open(dst, 'r', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

updates_made = []

# === UPDATE 1: QBE Insurance (Malaysia) Sdn Bhd ===
# Source: https://www.qbe.com/my/about-qbe/executive-team (OFFICIAL - HIGH confidence)
for i, r in enumerate(rows):
    if r['Institution_Name'] == 'QBE Insurance (Malaysia) Sdn Bhd':
        r['Chief Financial Officer'] = 'Vivien Wong (Head of Finance, joined May 2026, 25+ yrs finance leadership, CPA Australia & MIA) [Official: qbe.com/my/about-qbe/executive-team]'
        r['Chief Risk Officer'] = 'Mohd Farid Bin Othman (Head of Risk, joined Dec 2018, 20+ yrs internal audit/risk, MIA member) [Official: qbe.com/my/about-qbe/executive-team]'
        r['Head of Compliance'] = 'Jaysree Kaliappan (Head of Compliance, joined Jul 2025, 14+ yrs compliance/operational risk, ICA Intl Diploma in GRC) [Official: qbe.com/my/about-qbe/executive-team]'
        updates_made.append(f"Row {i}: QBE Insurance - Added CFO, CRO, Compliance - 3/7 roles filled")
        break

# === UPDATE 2: Manulife Insurance Berhad ===
# Fix: CISO field incorrectly contained CEO name - clear it
for i, r in enumerate(rows):
    if r['Institution_Name'] == 'Manulife Insurance Berhad':
        old_ciso = r['Chief Information Security Officer']
        if 'Vibha' in old_ciso and 'Group CEO' in old_ciso:
            r['Chief Information Security Officer'] = ''
            updates_made.append(f"Row {i}: Manulife Insurance - Corrected CISO field (was CEO name, now cleared)")
        break

# Write updated CSV
with open(dst, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Calculate coverage stats
total_institutions = len(rows)
total_target = total_institutions * 7
filled = 0
for r in rows:
    for col in ['Chief Information Security Officer', 'Head of Governance Risk & Compliance',
                'Chief Financial Officer', 'Chief Risk Officer', 'Head of Compliance',
                'Chief Information Officer', 'Head of Internal Audit']:
        if r.get(col, '').strip():
            filled += 1

print(f"=== CSV UPDATE COMPLETE ===")
print(f"Source: v3.4 -> Output: v3.5")
print(f"Total institutions: {total_institutions}")
print(f"Total target roles: {total_target}")
print(f"Filled roles: {filled}")
print(f"Overall coverage: {filled}/{total_target} ({filled/total_target*100:.1f}%)")
print(f"\nUpdates made this cycle:")
for u in updates_made:
    print(f"  + {u}")

# Show QBE final state
print(f"\nQBE Insurance Malaysia final state:")
for r in rows:
    if 'QBE' in r['Institution_Name']:
        for col in fieldnames:
            if col not in ['Tier', 'Segment', 'Institution_Name']:
                val = r.get(col, '')
                status = 'FILLED' if val.strip() else 'EMPTY'
                print(f"  [{status}] {col}: {val[:120] if val else '(empty)'}")

# Show Manulife final state
print(f"\nManulife Insurance Berhad final state:")
for r in rows:
    if r['Institution_Name'] == 'Manulife Insurance Berhad':
        for col in fieldnames:
            if col not in ['Tier', 'Segment', 'Institution_Name']:
                val = r.get(col, '')
                status = 'FILLED' if val.strip() else 'EMPTY'
                print(f"  [{status}] {col}: {val[:120] if val else '(empty)'}")

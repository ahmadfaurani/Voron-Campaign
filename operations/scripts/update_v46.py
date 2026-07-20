#!/usr/bin/env python3
"""Update enriched CSV to v4.6 - restore deleted data and add new findings."""
import csv
import shutil

BASE = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders'

# Read current v4.5
with open(f'{BASE}/prospect-database-enriched-v4.5.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    fieldnames = [fn for fn in reader.fieldnames if fn is not None]
    rows = list(reader)

# Clean any None keys from rows
for row in rows:
    if None in row:
        for k in list(row.keys()):
            if k is None:
                row.pop(k)

# Read v4.1 backup for restoration
with open(f'{BASE}/prospect-database-enriched-v4.1.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows_v41 = list(reader)

v41_lookup = {r.get('Institution_Name','').strip(): r for r in rows_v41}

role_cols = [
    'Chief Information Security Officer',
    'Head of Governance Risk & Compliance',
    'Chief Financial Officer',
    'Chief Risk Officer',
    'Head of Compliance',
    'Chief Information Officer',
    'Head of Internal Audit'
]

# --- RESTORE deleted data from v4.1 ---
restore_targets = [
    'Zurich Life Insurance Malaysia Berhad',
    'Zurich Takaful Malaysia Berhad',
    'Manulife Takaful Malaysia Berhad',
    'Kurnia Insurans (Malaysia) Berhad',
    'Sun Life Malaysia Assurance Berhad'
]

restored = 0
for row in rows:
    name = row.get('Institution_Name','').strip()
    if name in restore_targets:
        old = v41_lookup.get(name)
        if old:
            for col in role_cols:
                old_val = old.get(col, '').strip()
                cur_val = row.get(col, '').strip()
                if old_val and not cur_val:
                    row[col] = old_val
                    restored += 1

print(f"Restored {restored} role fields from v4.1 backup")

# --- UPDATE Sun Life Malaysia Assurance with scraped board data ---
for row in rows:
    name = row.get('Institution_Name','').strip()
    if name == 'Sun Life Malaysia Assurance Berhad':
        row['Chief Information Security Officer'] = 'CEO: Ho Teck Seng (President & CEO, effective 1 July 2025, succeeding Raymond Lew) [Official: sunlifemalaysia.com, conf 95]'
        row['Head of Governance Risk & Compliance'] = "Board Chairman: Dato' Noorazman Abd. Aziz (Ind. Director, appointed 13 May 2022) [Official: sunlifemalaysia.com, conf 95]; RMC Chair: Nigel Hazell (Ind. Director, Risk Mgmt Cmte Chairman) [Official: sunlifemalaysia.com, conf 95]"
        row['Chief Risk Officer'] = 'Nigel Hazell (Board Risk Management Committee Chairman, Ind. Director, appointed 13 May 2022) [Official: sunlifemalaysia.com/about-us/leadership/board-of-directors-assurance/, conf 95]'
        row['Head of Internal Audit'] = 'Wong Ah Kow (Board Audit Committee Chairman, Ind. Director, appointed 22 Sep 2022) [Official: sunlifemalaysia.com/about-us/leadership/board-of-directors-assurance/, conf 95]'
        print("Updated Sun Life Malaysia Assurance with board data")
        break

# --- UPDATE Sun Life Malaysia Takaful ---
for row in rows:
    name = row.get('Institution_Name','').strip()
    if 'Sun Life Malaysia Takaful' in name:
        row['Chief Information Security Officer'] = 'ED: Puneet Nayyar (Executive Director, Chief Actuary Sun Life Asia, appointed 12 Aug 2025) [Official: sunlifemalaysia.com, conf 95]'
        row['Head of Governance Risk & Compliance'] = "Board Chairman: Dato' Noorazman Abd Aziz (appointed 13 May 2022) [Official: sunlifemalaysia.com, conf 95]"
        row['Chief Risk Officer'] = 'Datin K. Komalavalli A/P K.R. Gopal (Chairperson of Risk Management Committee, Ind. Director, appointed 2 Sep 2022) [Official: sunlifemalaysia.com, conf 95]'
        row['Head of Internal Audit'] = 'Vivien Kusumowardhani (Chairperson of Audit Committee, Ind. Director, appointed 19 Aug 2022) [Official: sunlifemalaysia.com, conf 95]'
        print("Updated Sun Life Malaysia Takaful with board data")
        break

# --- UPDATE UOB Malaysia - add CISO from web search finding ---
for row in rows:
    name = row.get('Institution_Name','').strip()
    if name == 'UOB Malaysia Berhad' or 'UOB' in name:
        cur = row.get('Chief Information Security Officer','').strip()
        if not cur:
            row['Chief Information Security Officer'] = 'Tobias Gondrom (Group CISO, UOB Group) [Web search, conf 75]'
            print(f"Updated {name} CISO")
        break

# --- Statistics ---
total_roles = 0
filled_roles = 0
for row in rows:
    for col in role_cols:
        total_roles += 1
        if row.get(col, '').strip():
            filled_roles += 1

print(f"\nTotal: {filled_roles}/{total_roles} roles filled ({100*filled_roles/total_roles:.1f}%)")
print(f"Total institutions: {len(rows)}")

# Write v4.6
out = f'{BASE}/prospect-database-enriched-v4.6.csv'
with open(out, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"\nWrote v4.6 CSV: {out}")

# Show per-institution coverage for updated ones
print("\n=== Updated Institutions Coverage ===")
for row in rows:
    name = row.get('Institution_Name','').strip()
    if name in restore_targets or 'Sun Life' in name or 'UOB' in name:
        filled = sum(1 for c in role_cols if row.get(c,'').strip())
        print(f"  {name}: {filled}/7")

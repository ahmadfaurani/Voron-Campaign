#!/usr/bin/env python3
"""
VoronDRQ Stakeholder Database Update v5.3
==========================================
Date: 2026-07-17
Agent: VoronDRQ Stakeholder Collection Agent (Cron Job)
Classification: TLP:AMBER

Changes:
1. MIDF Amanah Investment Bank Berhad — 3 NEW roles (CFO, CRO, CIO) from MBSB Bank Group
2. Phillip Securities (Malaysia) Sdn Bhd — 5 NEW roles (CFO, CRO, Compliance, CIO, IA) + CEO note
3. Sumitomo Mitsui Banking Corporation Malaysia Berhad — 2 NEW roles (CRO, IA) board-level
4. Zurich Life Insurance Malaysia Berhad — 1 NEW role (IA/Audit Cmte Chair) + CEO note
5. Zurich Takaful Malaysia Berhad — CEO note added

Sources:
- https://www.midf.com.my/key-management (Official — MIDF CEO confirmed)
- https://www.mbsb.com/corporate_about_team.html (Official — MBSB Bank Group execs)
- https://www.phillipcapital.com.my/core-management-team/ (Official — Phillip Capital Malaysia)
- https://www.phillipinvest.com.my/the-management-team/ (Official — Phillip Investment management)
- https://www.smbc.co.jp/asia/malaysia/SMBCMY-board-of-directors.pdf (Official — SMBC Board)
- https://www.smbc.co.jp/asia/malaysia/financial-statement-31Dec2024.pdf (Official — SMBC financials)
- https://www.zurich.com.my/about-zurich/the-zurich-story/our-leaders (Official — Zurich Malaysia leaders)
- Zurich Life Insurance Malaysia Berhad AR 2025 (Annual Report — board/audit committee info)

Research Method: 3 parallel subagents (Insurance/Takaful, CISO Research, Banks/Investment)
Total institutions researched: 19 across 3 parallel workstreams
New roles added: 11 (+1 CEO note)
"""

import csv
import os
import shutil
from datetime import datetime

MASTER_CSV = "/home/p62operator/.openclaw/workspace-hoi/vorondrq-rmit-campaign/prospect-database-7stakeholders.csv"
BACKUP_CSV = "/home/p62operator/.openclaw/workspace-hoi/vorondrq-rmit-campaign/prospect-database-7stakeholders.csv.bak-v53"
ENRICHED_DIR = "/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders"

# Role column names in the master CSV
ROLES = [
    'Chief Information Security Officer',
    'Head of Governance Risk & Compliance',
    'Chief Financial Officer',
    'Chief Risk Officer',
    'Head of Compliance',
    'Chief Information Officer',
    'Head of Internal Audit',
]

# Updates to apply: {Institution_Name: {role_column: new_value}}
# For empty cells: fill them. For cells with "overwrite" flag: replace.
UPDATES = {
    # 1. MIDF Amanah Investment Bank Berhad — 3 NEW roles from MBSB Bank Group
    "MIDF Amanah Investment Bank Berhad": {
        'Chief Information Security Officer': 'CEO: Azizi Mustafa (Chief Executive Officer, MIDF Berhad) [Official: midf.com.my/key-management, conf 95]',
        'Chief Financial Officer': 'Shahnaz Jammal (Group Chief Financial Officer, MBSB Bank) [Official: mbsb.com/corporate_about_team.html, conf 80 - Group-level]',
        'Chief Risk Officer': 'Laurence Ong Wooi Keat (Group Chief Risk Officer, MBSB Bank) [Official: mbsb.com/corporate_about_team.html, conf 80 - Group-level]',
        'Chief Information Officer': 'Noor Azman Bin Abdul Karim (Group Chief Technology Officer, MBSB Bank) [Official: mbsb.com/corporate_about_team.html, conf 80 - Group-level]',
    },

    # 2. Phillip Securities (Malaysia) Sdn Bhd — 5 NEW roles + CEO note (OVERWRITE scraping note)
    "Phillip Securities (Malaysia) Sdn Bhd": {
        'Chief Information Security Officer': 'CEO: Andy Lim Say Kiat (Group Managing Director, PhillipCapital Malaysia) [Official: phillipcapital.com.my/core-management-team/, conf 95]; Group Chairperson: Datin Hajjah Nona Binti Salleh [Official: phillipcapital.com.my, conf 95]',
        'Chief Financial Officer': 'Alina Sim (HOD Finance / CFO) [Official: phillipinvest.com.my/the-management-team/, conf 95]',
        'Chief Risk Officer': 'Ramli Abd Hamid (Head of Legal, Compliance & Risk Management) [Official: phillipinvest.com.my/the-management-team/, conf 95 - combined Legal/Compliance/Risk role]',
        'Head of Compliance': 'Ramli Abd Hamid (Head of Legal, Compliance & Risk Management) [Official: phillipinvest.com.my/the-management-team/, conf 95 - combined role]',
        'Chief Information Officer': 'Yorck Oliver Ago Reuber (IT Director) [Official: phillipinvest.com.my/the-management-team/, conf 95]',
        'Head of Internal Audit': 'Fatin Fitriana Amran (Head of Internal Audit) [Official: phillipinvest.com.my/the-management-team/, conf 95]',
    },

    # 3. Sumitomo Mitsui Banking Corporation Malaysia Berhad — 2 NEW roles (board-level)
    "Sumitomo Mitsui Banking Corporation Malaysia Berhad": {
        'Chief Risk Officer': 'Lim Tuang Ooi (Board Risk Management Committee Chairman, Ind. Non-Exec Director) [Official: smbc.co.jp/asia/malaysia/SMBCMY-board-of-directors.pdf, conf 85 - board-level oversight]',
        'Head of Internal Audit': 'Lo Nyen Khing (Board Audit Committee Chairman, Ind. Non-Exec Director) [Official: smbc.co.jp/asia/malaysia/SMBCMY-board-of-directors.pdf, conf 85 - board-level oversight]',
    },

    # 4. Zurich Life Insurance Malaysia Berhad — CEO note + Audit Committee Chair
    "Zurich Life Insurance Malaysia Berhad": {
        'Chief Information Security Officer': 'CEO: Pauline Teoh (Chief Executive Officer) [Official: zurich.com.my/about-zurich/the-zurich-story/our-leaders, conf 95]; Country Head: Junior Cho [Official: zurich.com.my, conf 95]',
        'Head of Internal Audit': 'Onn Kien Hoe (Audit Committee Chair) [Zurich Life Insurance Malaysia Berhad AR 2025, conf 85 - board-level oversight]',
    },

    # 5. Zurich Takaful Malaysia Berhad — CEO note
    "Zurich Takaful Malaysia Berhad": {
        'Chief Information Security Officer': 'CEO: Nur Fatihah Mustafa (Chief Executive Officer) [Official: zurich.com.my/about-zurich/the-zurich-story/our-leaders, conf 95]; Exec Director: Junior Cho [Official: zurich.com.my, conf 95]',
    },
}

# Institutions where CISO column should be overwritten (not just filled)
OVERWRITE_CISO = {
    "Phillip Securities (Malaysia) Sdn Bhd",  # Has scraping note, replace with CEO note
}

def main():
    # Backup
    shutil.copy2(MASTER_CSV, BACKUP_CSV)
    print(f"Backup created: {BACKUP_CSV}")

    # Read
    with open(MASTER_CSV, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    print(f"Total institutions in DB: {len(rows)}")

    # Apply updates
    changes = []
    for row in rows:
        name = row.get('Institution_Name', '').strip()
        if name in UPDATES:
            for role, new_val in UPDATES[name].items():
                old_val = row.get(role, '').strip()

                if name in OVERWRITE_CISO and role == 'Chief Information Security Officer':
                    # Overwrite the scraping note with CEO note
                    row[role] = new_val
                    changes.append((name, role, 'OVERWRITTEN', old_val[:60], new_val[:80]))
                elif not old_val:
                    # Fill empty cell
                    row[role] = new_val
                    changes.append((name, role, 'ADDED', '', new_val[:80]))
                else:
                    # Cell already has data — skip (don't overwrite existing)
                    print(f"  SKIP (already filled): {name} / {role} = {old_val[:60]}")

    # Write updated master CSV
    with open(MASTER_CSV, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n{'='*80}")
    print(f"CHANGES APPLIED: {len(changes)}")
    print(f"{'='*80}")
    for name, role, action, old, new in changes:
        role_short = role.replace('Chief Information Security Officer', 'CISO').replace('Head of Governance Risk & Compliance', 'GRC').replace('Chief Financial Officer', 'CFO').replace('Chief Risk Officer', 'CRO').replace('Head of Compliance', 'Compliance').replace('Chief Information Officer', 'CIO').replace('Head of Internal Audit', 'IA')
        print(f"  [{action:11}] {name[:42]:42} {role_short:12}")
        if action == 'ADDED':
            print(f"           -> {new}")
        elif action == 'OVERWRITTEN':
            print(f"           was: {old}")
            print(f"           ->  {new}")

    # Summary stats
    print(f"\n{'='*80}")
    print("POST-UPDATE COVERAGE SUMMARY")
    print(f"{'='*80}")
    total_cells = 0
    filled_cells = 0
    for row in rows:
        for role in ROLES:
            total_cells += 1
            if row.get(role, '').strip():
                filled_cells += 1
    pct = filled_cells / total_cells * 100 if total_cells > 0 else 0
    print(f"Total cells: {total_cells}")
    print(f"Filled cells: {filled_cells}")
    print(f"Coverage: {pct:.1f}%")

    # Per-role breakdown
    print(f"\nPer-role completion:")
    for role in ROLES:
        count = sum(1 for row in rows if row.get(role, '').strip())
        pct = count / len(rows) * 100 if rows else 0
        role_short = role.replace('Chief Information Security Officer', 'CISO').replace('Head of Governance Risk & Compliance', 'GRC').replace('Chief Financial Officer', 'CFO').replace('Chief Risk Officer', 'CRO').replace('Head of Compliance', 'Compliance').replace('Chief Information Officer', 'CIO').replace('Head of Internal Audit', 'IA')
        print(f"  {role_short:12}: {count:3d}/{len(rows)} ({pct:.1f}%)")

    # Coverage distribution
    print(f"\nCoverage distribution:")
    coverage_buckets = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    for row in rows:
        count = sum(1 for role in ROLES if row.get(role, '').strip())
        coverage_buckets[count] = coverage_buckets.get(count, 0) + 1
    for k in sorted(coverage_buckets.keys()):
        bar = '#' * coverage_buckets[k]
        print(f"  {k}/7: {coverage_buckets[k]:3d} {bar}")

    print(f"\nv5.3 update complete.")

if __name__ == '__main__':
    main()

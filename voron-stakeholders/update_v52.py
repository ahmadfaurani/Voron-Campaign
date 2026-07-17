#!/usr/bin/env python3
"""
VoronDRQ Stakeholder Database Update v5.2
==========================================
Date: 2026-07-17
Agent: VoronDRQ Stakeholder Collection Agent (Cron Job)
Classification: TLP:AMBER

Changes:
1. MoneyMatch Sdn Bhd — 4 NEW roles (CISO, CFO, CIO, Compliance) from official page
2. Bank Rakyat Investment Bank Berhad — 2 NEW roles (IA, CIO) from official page
3. Zurich Life Insurance Malaysia Berhad — DATA FIX: Clear 4 corrupted cells (CEO data fragments)
4. Zurich Takaful Malaysia Berhad — DATA FIX: Clear 3 corrupted cells (CEO data fragments)

Sources:
- https://www.moneymatch.co/about-us (Official)
- https://rmanagement.com.my/en/leadership/ (Official)
- https://www.zurich.com.my/about-zurich/the-zurich-story/our-leaders (Official — confirmed only CEOs listed)
- https://www.generali.com.my/about-generali/leadership (Official — verified existing data)
- https://www.hla.com.my/en/know-us/leadership.html (Official — verified existing data)
- https://www.fwd.com.my/about-us/ins/meet-our-team (Official — verified existing data)
- https://www.berjayasompo.com.my/leadership-team (Official — verified existing data)
- https://www.takaful-malaysia.com.my/en/about-us/our-leaders/ (Official — verified existing data)
"""

import csv
import os
import shutil
from datetime import datetime

MASTER_CSV = "/home/p62operator/.openclaw/workspace-hoi/vorondrq-rmit-campaign/prospect-database-7stakeholders.csv"
BACKUP_CSV = "/home/p62operator/.openclaw/workspace-hoi/vorondrq-rmit-campaign/prospect-database-7stakeholders.csv.bak-v52"
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
UPDATES = {
    # 1. MoneyMatch Sdn Bhd — 4 NEW roles from official page
    "MoneyMatch Sdn Bhd": {
        'Chief Information Security Officer': 'Poorya (Chief Information & Security Officer) [Official: moneymatch.co/about-us, conf 90 - note: first name only displayed]',
        'Chief Financial Officer': 'Anees Aisyah (Chief Financial Officer) [Official: moneymatch.co/about-us, conf 92]',
        'Chief Information Officer': 'Jerry Chee (Chief Technology Officer) [Official: moneymatch.co/about-us, conf 92]',
        'Head of Compliance': 'Thavalogan (Head of Compliance) [Official: moneymatch.co/about-us, conf 88 - note: first name only displayed]',
    },
    
    # 2. Bank Rakyat Investment Bank Berhad — 2 NEW roles from official page
    "Bank Rakyat Investment Bank Berhad": {
        'Head of Internal Audit': 'Fuhaizad Asmar Omar (Senior Manager Audit, Compliance & Governance) [Official: rmanagement.com.my/en/leadership, conf 85 - note: subsidiary-level, combined Audit+Compliance+Governance role]',
        'Chief Information Officer': 'Ismat Nazarul Mat Isa (Senior Manager Finance & IT) [Official: rmanagement.com.my/en/leadership, conf 82 - note: subsidiary-level, combined Finance & IT role]',
    },
    
    # 3. Zurich Life Insurance Malaysia Berhad — DATA FIX: Clear corrupted cells
    #    Previous update misaligned CEO data into wrong columns
    "Zurich Life Insurance Malaysia Berhad": {
        'Chief Information Security Officer': '',  # Was: CEO fragment — CLEAR
        'Head of Governance Risk & Compliance': '',  # Was: entity name fragment — CLEAR
        'Chief Financial Officer': '',  # Was: "conf 95]" fragment — CLEAR
        'Chief Risk Officer': '',  # Was: Country CEO data — CLEAR
    },
    
    # 4. Zurich Takaful Malaysia Berhad — DATA FIX: Clear corrupted cells
    "Zurich Takaful Malaysia Berhad": {
        'Chief Information Security Officer': '',  # Was: CEO data — CLEAR
        'Head of Governance Risk & Compliance': '',  # Was: Country CEO data — CLEAR
        'Chief Information Officer': '',  # Was: note fragment — CLEAR
    },
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
                if new_val:  # Setting a new value
                    if not old_val:  # Only fill empty cells
                        row[role] = new_val
                        changes.append((name, role, 'ADDED', old_val[:50], new_val[:80]))
                    else:
                        # Cell already has data — skip (don't overwrite existing)
                        print(f"  SKIP (already filled): {name} / {role}")
                else:  # Clearing a corrupted cell
                    if old_val and ('CEO:' in old_val or 'conf 95]' in old_val or 'Note:' in old_val or 'zurich.com.my' == old_val[:13]):
                        row[role] = ''
                        changes.append((name, role, 'CLEARED', old_val[:50], '(empty)'))
                    elif old_val:
                        print(f"  SKIP (not clearly corrupted): {name} / {role} = {old_val[:60]}")
    
    # Write
    with open(MASTER_CSV, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\n{'='*80}")
    print(f"CHANGES APPLIED: {len(changes)}")
    print(f"{'='*80}")
    for name, role, action, old, new in changes:
        role_short = role.replace('Chief Information Security Officer', 'CISO').replace('Head of Governance Risk & Compliance', 'GRC').replace('Chief Financial Officer', 'CFO').replace('Chief Risk Officer', 'CRO').replace('Head of Compliance', 'Compliance').replace('Chief Information Officer', 'CIO').replace('Head of Internal Audit', 'IA')
        print(f"  [{action:7}] {name[:40]:40} {role_short:12}")
        if action == 'ADDED':
            print(f"           -> {new}")
        elif action == 'CLEARED':
            print(f"           was: {old}")
    
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
    
    print(f"\nv5.2 update complete.")

if __name__ == '__main__':
    main()

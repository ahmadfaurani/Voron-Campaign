#!/usr/bin/env python3
"""
Fix broken tier values (row numbers 192-215) and sort canonical file by Tier → Segment → Institution.
"""
import csv

ROLES = [
    'Chief Information Security Officer',
    'Head of Governance Risk & Compliance',
    'Chief Financial Officer',
    'Chief Risk Officer',
    'Head of Compliance',
    'Chief Information Officer',
    'Head of Internal Audit',
]
COLS = ['Tier', 'Segment', 'Institution_Name'] + ROLES

# Tier → Segment mapping from the 207 well-formed rows:
#   Tier 1: Licensed Banks
#   Tier 2: Insurers, Investment Banks, Takaful
#   Tier 3: Cooperatives, Development FIs, MSBs
#   Tier 4: Card Schemes, E-Money, Payment Operators
#   Tier 5: GLC-Linked
#   Tier 6: Fintech Registered, Fintech Sandbox

# Fix mapping for the 24 broken rows: (Institution_Name → (Tier, Segment))
TIER_FIX = {
    # Tier 1 — Licensed Banks
    'Affin Bank Berhad': (1, 'Licensed Banks'),
    'Kuwait Finance House (Malaysia) Berhad': (1, 'Licensed Banks'),
    'AEON Digital Bank (AEON Financial Service)': (1, 'Licensed Banks'),

    # Tier 2 — Insurers / Investment Banks
    'AXA Affin General Insurance Berhad': (2, 'Insurers'),
    'JF Apex Securities Berhad': (2, 'Investment Banks'),
    'TA Securities Holdings Berhad': (2, 'Investment Banks'),

    # Tier 3 — Development FIs / Cooperatives / Asset Management (new segment)
    'Credit Guarantee Corporation Malaysia Berhad': (3, 'Development FIs'),
    'Malaysia Debt Ventures Berhad': (3, 'Development FIs'),
    'Pengurusan Danaharta Nasional Berhad': (3, 'Development FIs'),
    'CIMB-Principal Asset Management Berhad': (3, 'Asset Management'),
    'Public Mutual Berhad': (3, 'Asset Management'),
    'RHB Asset Management Sdn Bhd': (3, 'Asset Management'),
    'Hong Leong Asset Management Berhad': (3, 'Asset Management'),
    'Maybank Asset Management Group Sdn Bhd': (3, 'Asset Management'),
    'Bank Kerjasama Rakyat Malaysia Berhad': (3, 'Cooperatives'),
    'Koperasi PDRM (Polis Diraja Malaysia)': (3, 'Cooperatives'),
    'Majlis Peruntingan Bank-Bank Islam Malaysia (MBSM)': (3, 'Cooperatives'),
    'Majlis Perundingan Bank-Bank Islam Malaysia (MBSM)': (3, 'Cooperatives'),

    # Tier 4 — Payment Operators
    'Maybank QRPay': (4, 'Payment Operators'),
    'CIMB Clicks Pay': (4, 'Payment Operators'),

    # Tier 6 — Fintech
    'Curlec Sdn Bhd': (6, 'Fintech Registered'),
    'FavePay Malaysia Sdn Bhd': (6, 'Fintech Registered'),
    'HelloGold Malaysia Sdn Bhd': (6, 'Fintech Sandbox'),
    'CompareHero (by Jirnexu)': (6, 'Fintech Registered'),
    'RinggitPlus (by Jirnexu)': (6, 'Fintech Registered'),
}

VALID_TIERS = {'1', '2', '3', '4', '5', '6'}


def main():
    with open('prospect-database-canonical.csv', newline='') as fh:
        rows = list(csv.DictReader(fh))

    fixed = 0
    for row in rows:
        t = row['Tier'].strip()
        if t not in VALID_TIERS:
            inst = row['Institution_Name'].strip()
            if inst in TIER_FIX:
                row['Tier'] = str(TIER_FIX[inst][0])
                row['Segment'] = TIER_FIX[inst][1]
                fixed += 1
            else:
                print(f'WARNING: no fix for {inst} (Tier={t})')

    # Sort by Tier (int), Segment (alpha), Institution_Name (alpha)
    rows.sort(key=lambda r: (int(r['Tier']), r['Segment'].strip(), r['Institution_Name'].strip()))

    with open('prospect-database-canonical.csv', 'w', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=COLS)
        writer.writeheader()
        writer.writerows(rows)

    # Summary
    from collections import Counter
    tier_counts = Counter(r['Tier'] for r in rows)
    seg_by_tier = {}
    for r in rows:
        t = r['Tier']
        seg_by_tier.setdefault(t, set()).add(r['Segment'].strip())

    print(f'=== Tier fix + sort complete ===')
    print(f'Fixed {fixed} rows with broken tier values')
    print()
    for t in sorted(tier_counts.keys(), key=int):
        print(f'Tier {t}: {tier_counts[t]} institutions — segments: {sorted(seg_by_tier[t])}')
    print(f'\nTotal: {len(rows)} institutions')
    print(f'Output: prospect-database-canonical.csv')


if __name__ == '__main__':
    main()

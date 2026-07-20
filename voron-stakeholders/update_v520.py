#!/usr/bin/env python3
"""Update v5.19 -> v5.20: Fill TNG Digital Internal Audit, Boost CISO, ShopeePay Compliance"""

import csv
import shutil
from datetime import datetime

SRC = 'prospect-database-enriched-v5.19.csv'
DST = 'prospect-database-enriched-v5.20.csv'

# Copy source to destination
shutil.copy2(SRC, DST)

# Read the CSV
with open(DST, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

updates = []

# ============================================================
# UPDATE 1: TNG Digital Internal Audit (Rows 184, 190, 191, 192)
# Hairul Imran - Director, Internal Audit at TNG Digital
# Source: LinkedIn - https://my.linkedin.com/in/hairulimran
# Confidence: 80
# ============================================================
tng_ia_value = "Hairul Imran|Director, Internal Audit|80|https://my.linkedin.com/in/hairulimran|TNG Digital Director of Internal Audit [LinkedIn confirmed]"

for row_idx in [184, 190, 191, 192]:
    if row_idx <= len(rows):
        row = rows[row_idx - 1]
        old_val = row.get('Head of Internal Audit', '').strip()
        if not old_val or old_val in ['NOT FOUND', 'TBC', 'TBD', 'N/A', '-']:
            row['Head of Internal Audit'] = tng_ia_value
            updates.append((row_idx, row['Institution_Name'], 'Head of Internal Audit', 'Hairul Imran'))

# ============================================================
# UPDATE 2: Boost CISO (Rows 24, 37)
# Shankar Krishnan - CISO at Axiata Digital group and subsidiaries (Boost)
# Source: LinkedIn - https://my.linkedin.com/in/shankyk + theorg.com
# Confidence: 85
# Note: Also serves as CTO at Boost Bank (listed on official leadership page)
# ============================================================
boost_ciso_value = "Shankar Krishnan|Chief Information Security Officer|85|https://my.linkedin.com/in/shankyk|CISO Axiata Digital group/Boost [LinkedIn + theorg.com confirmed. Also CTO at Boost Bank]"

for row_idx in [24, 37]:
    if row_idx <= len(rows):
        row = rows[row_idx - 1]
        old_val = row.get('Chief Information Security Officer', '').strip()
        if not old_val or old_val in ['NOT FOUND', 'TBC', 'TBD', 'N/A', '-']:
            row['Chief Information Security Officer'] = boost_ciso_value
            updates.append((row_idx, row['Institution_Name'], 'Chief Information Security Officer', 'Shankar Krishnan'))

# ============================================================
# UPDATE 3: ShopeePay Compliance (Rows 174, 175)
# Fadhli Azman - Head of Compliance at ShopeePay/Monee Malaysia
# Source: LinkedIn - https://my.linkedin.com/in/fadhli-azman-150273b9
# Confidence: 85
# ============================================================
shopeepay_compliance_value = "Fadhli Azman|Head of Compliance|85|https://my.linkedin.com/in/fadhli-azman-150273b9|Head of Compliance ShopeePay/Monee Malaysia [LinkedIn confirmed]"

for row_idx in [174, 175]:
    if row_idx <= len(rows):
        row = rows[row_idx - 1]
        old_val = row.get('Head of Compliance', '').strip()
        if not old_val or old_val in ['NOT FOUND', 'TBC', 'TBD', 'N/A', '-']:
            row['Head of Compliance'] = shopeepay_compliance_value
            updates.append((row_idx, row['Institution_Name'], 'Head of Compliance', 'Fadhli Azman'))

# Write updated CSV
with open(DST, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Summary
print(f"v5.20 update complete.")
print(f"Total updates applied: {len(updates)}")
for row_idx, inst, role, name in updates:
    print(f"  Row {row_idx}: {inst} -> {role} = {name}")

# Count completeness
roles = ['Chief Information Security Officer', 'Head of Governance Risk & Compliance', 
         'Chief Financial Officer', 'Chief Risk Officer', 'Head of Compliance',
         'Chief Information Officer', 'Head of Internal Audit']
bad = ['', 'NOT FOUND', 'TBC', 'TBD', 'N/A', '-']

filled = 0
total = len(rows) * 7
full_7 = 0
for row in rows:
    cnt = sum(1 for r in roles if row.get(r, '').strip() not in bad)
    filled += cnt
    if cnt == 7:
        full_7 += 1

print(f"\nCompleteness: {filled}/{total} ({filled/total*100:.1f}%)")
print(f"Fully complete (7/7): {full_7} institutions")

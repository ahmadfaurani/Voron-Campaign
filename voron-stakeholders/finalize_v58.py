#!/usr/bin/env python3
"""
VoronDRQ v5.8 Finalization: cleanup + master CSV update + PNB CISO NOT FOUND
"""
import csv

# 1. Clean v5.8: remove corrupted empty row, mark PNB CISO NOT FOUND
SRC = 'prospect-database-enriched-v5.8.csv'
with open(SRC, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

role_cols = ['Chief Information Security Officer', 'Head of Governance Risk & Compliance',
             'Chief Financial Officer', 'Chief Risk Officer', 'Head of Compliance',
             'Chief Information Officer', 'Head of Internal Audit']
by_name = {r['Institution_Name']: r for r in rows}

# Remove corrupted empty rows
before = len(rows)
rows = [r for r in rows if r['Institution_Name'].strip()]
removed = before - len(rows)
print(f"Removed {removed} corrupted empty row(s). Rows: {before} -> {len(rows)}")

# Mark PNB CISO as NOT FOUND (confirmed via firecrawl - no CISO on leadership page)
if 'Permodalan Nasional Berhad (PNB)' in by_name:
    r = by_name['Permodalan Nasional Berhad (PNB)']
    if not r['Chief Information Security Officer'].strip():
        r['Chief Information Security Officer'] = 'NOT FOUND [PNB leadership page (pnb.com.my/en/leadership-en) confirmed no CISO/Head of InfoSec/CTO/CIO/Head of IT listed. CISO function likely embedded under Group CTO Ts Izzat Aziz or not publicly disclosed. Firecrawl scrape verified.]'
        print("Marked PNB CISO as NOT FOUND")

# Write cleaned v5.8
with open(SRC, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# 2. Update MASTER CSV (prospect-database-7stakeholders.csv in voron-prospects)
MASTER = '/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv'
with open(MASTER, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    mrows = list(reader)
    mfields = reader.fieldnames

# Master CSV uses different column names - find them
print(f"\nMaster CSV columns: {mfields}")
print(f"Master CSV rows: {len(mrows)}")

# The master CSV has role-column schema. Update institutions that changed.
# Map enriched names to master names (fuzzy)
by_name_m = {r['Institution_Name']: r for r in mrows}

# Find which master columns map to which roles
# Looking at the header: Chief Information Security Officer, Head of Governance Risk & Compliance, etc.
# They should be the same as enriched
m_role_cols = [c for c in mfields if c in role_cols]
print(f"Master role columns: {m_role_cols}")

updated_count = 0
for ename, erow in by_name.items():
    if not ename.strip():
        continue
    # Find matching master row (exact or fuzzy)
    mrow = None
    if ename in by_name_m:
        mrow = by_name_m[ename]
    else:
        # fuzzy: check if any master name contains the enriched name or vice versa
        for mn, mr in by_name_m.items():
            if ename.lower() in mn.lower() or mn.lower() in ename.lower():
                mrow = mr
                break
    if mrow:
        for col in m_role_cols:
            eval_val = erow.get(col, '').strip()
            mval = mrow.get(col, '').strip()
            if eval_val and not mval:
                # Update master with enriched value (first 200 chars to keep manageable)
                mrow[col] = eval_val[:300]
                updated_count += 1

with open(MASTER, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=mfields)
    writer.writeheader()
    writer.writerows(mrows)

print(f"\nMaster CSV updated: {updated_count} role cells updated")

# 3. Final stats
from collections import Counter
coverage = Counter()
total_filled = 0
for r in rows:
    filled = sum(1 for c in role_cols if r.get(c,'').strip())
    coverage[filled] += 1
    total_filled += filled

print(f"\n=== FINAL v5.8 Stats ===")
print(f"Total institutions: {len(rows)}")
print(f"Total roles filled: {total_filled}/{len(rows)*7} ({100*total_filled/(len(rows)*7):.1f}%)")
print(f"Full coverage (7/7): {coverage[7]}")
for k in sorted(coverage.keys()):
    print(f"  {k}/7: {coverage[k]}")

#!/usr/bin/env python3
"""Analyze gap distribution in v5.46 CSV to find highest-ROI enrichment targets."""
import csv

with open('prospect-database-enriched-v5.46.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

ROLE_COLS = [
    'Chief Information Security Officer',
    'Head of Governance Risk & Compliance',
    'Chief Financial Officer',
    'Chief Risk Officer',
    'Head of Compliance',
    'Chief Information Officer',
    'Head of Internal Audit',
]

def is_real_name(val):
    """Check if a cell has a real name (not NOT FOUND or empty)."""
    if not val or val.strip() == '':
        return False
    v = val.strip().upper()
    if v.startswith('NOT FOUND') or v.startswith('NOT PUBLICLY') or v.startswith('NOT AVAILABLE'):
        return False
    if 'NOT FOUND' in v or 'NOT PUBLICLY DISCLOSED' in v:
        return False
    return True

# Analyze each institution
results = []
for i, r in enumerate(rows):
    name = r['Institution_Name']
    tier = r['Tier']
    segment = r['Segment']
    filled = 0
    gaps = 0
    gap_roles = []
    for col in ROLE_COLS:
        val = r.get(col, '')
        if is_real_name(val):
            filled += 1
        else:
            gaps += 1
            gap_roles.append(col.split()[0])  # Short role name
    results.append({
        'idx': i,
        'name': name,
        'tier': tier,
        'segment': segment,
        'filled': filled,
        'gaps': gaps,
        'gap_roles': gap_roles,
    })

# Sort by gaps (most gaps first), then by filled (most filled first for near-complete institutions)
results.sort(key=lambda x: (-x['gaps'], -x['filled']))

print("=" * 100)
print(f"TOP 40 INSTITUTIONS WITH MOST GAPS (out of {len(rows)} total)")
print("=" * 100)
print(f"{'#':>3} {'Gaps':>4} {'Fill':>4} {'Tier':>4} {'Segment':<25} {'Institution':<50} {'Missing Roles'}")
print("-" * 150)

for r in results[:40]:
    gap_str = ', '.join(r['gap_roles'])
    print(f"{r['idx']:>3} {r['gaps']:>4} {r['filled']:>4} {r['tier']:>4} {r['segment'][:25]:<25} {r['name'][:50]:<50} {gap_str}")

print()
print("=" * 100)
print("INSTITUTIONS WITH 6-7 GAPS (highest ROI for new research)")
print("=" * 100)

high_gap = [r for r in results if r['gaps'] >= 6]
print(f"Count: {len(high_gap)} institutions with 6+ gaps")
for r in high_gap:
    gap_str = ', '.join(r['gap_roles'])
    print(f"  Row {r['idx']:>3} | {r['name']:<50} | Gaps={r['gaps']} Filled={r['filled']} | {gap_str}")

print()
print("=" * 100)
print("INSTITUTIONS NEAR COMPLETION (5+ filled, 1-2 gaps)")
print("=" * 100)

near_complete = [r for r in results if r['filled'] >= 5 and r['gaps'] <= 2]
print(f"Count: {len(near_complete)} institutions near completion")
for r in near_complete:
    gap_str = ', '.join(r['gap_roles'])
    print(f"  Row {r['idx']:>3} | {r['name']:<50} | Filled={r['filled']} Gaps={r['gaps']} | Missing: {gap_str}")

print()
print("=" * 100)
print("SUMMARY STATISTICS")
print("=" * 100)

total_cells = len(rows) * 7
total_filled = sum(r['filled'] for r in results)
total_gaps = sum(r['gaps'] for r in results)
print(f"Total institutions: {len(rows)}")
print(f"Total cells: {total_cells}")
print(f"Total filled (real names): {total_filled} ({total_filled/total_cells*100:.1f}%)")
print(f"Total gaps: {total_gaps} ({total_gaps/total_cells*100:.1f}%)")
print()

# Gap by role
print("Gap rate by role:")
for col in ROLE_COLS:
    filled_count = sum(1 for r in results if is_real_name(rows[r['idx']].get(col, '')))
    gap_count = len(rows) - filled_count
    print(f"  {col}: {filled_count}/{len(rows)} filled ({gap_count} gaps, {gap_count/len(rows)*100:.1f}% gap)")

# Gap by segment
print()
print("Gap rate by segment:")
segments = {}
for r in results:
    seg = r['segment']
    if seg not in segments:
        segments[seg] = {'count': 0, 'filled': 0, 'gaps': 0}
    segments[seg]['count'] += 1
    segments[seg]['filled'] += r['filled']
    segments[seg]['gaps'] += r['gaps']

for seg, data in sorted(segments.items(), key=lambda x: -x[1]['gaps']):
    total_seg_cells = data['count'] * 7
    print(f"  {seg}: {data['count']} inst, {data['filled']}/{total_seg_cells} filled ({data['gaps']} gaps, {data['gaps']/total_seg_cells*100:.1f}% gap)")

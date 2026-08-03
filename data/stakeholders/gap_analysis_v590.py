#!/usr/bin/env python3
"""Gap analysis for v5.89 — identify best targets for v5.90 enrichment cycle."""

import csv

path = 'prospect-database-enriched-v5.89.csv'

role_cols = [
    'Chief Information Security Officer',
    'Head of Governance Risk & Compliance',
    'Chief Financial Officer',
    'Chief Risk Officer',
    'Head of Compliance',
    'Chief Information Officer',
    'Head of Internal Audit'
]

role_short = {
    'Chief Information Security Officer': 'CISO',
    'Head of Governance Risk & Compliance': 'GRC',
    'Chief Financial Officer': 'CFO',
    'Chief Risk Officer': 'CRO',
    'Head of Compliance': 'Compliance',
    'Chief Information Officer': 'CIO',
    'Head of Internal Audit': 'IA'
}

def is_gap(val):
    v = (val or '').strip()
    return (not v or
            v.upper().startswith('NOT FOUND') or
            v.upper().startswith('NOT PUBLICLY') or
            v.upper().startswith('NOT SEPARATELY') or
            v.upper().startswith('ENTITY LIKELY') or
            v.upper().startswith('ENTITY WOUND') or
            v.upper().startswith('ENTITY TYPE') or
            v.upper().startswith('SHARES ') or
            v.upper().startswith('NOT YET RESEARCHED') or
            v.upper().startswith('NOT FOUND '))

def is_named(val):
    v = (val or '').strip()
    return v and not is_gap(v)

def is_entity(val):
    v = (val or '').strip()
    return v.upper().startswith(('ENTITY WOUND','ENTITY TYPE','SHARES ','ENTITY LIKELY'))

with open(path, newline='', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"Total institutions: {len(rows)}")
print()

# Per-role coverage
print("=== Role Coverage ===")
for col in role_cols:
    named = sum(1 for r in rows if is_named(r.get(col, '')))
    entity = sum(1 for r in rows if is_entity(r.get(col, '')))
    gaps = sum(1 for r in rows if is_gap(r.get(col, '')) and not is_entity(r.get(col, '')))
    pct = (named + entity) / len(rows) * 100
    print(f"  {role_short[col]:12s}: named={named:3d} entity={entity:3d} notfound={gaps:3d}  ({pct:.1f}% covered)")

# Quick wins: institutions with 1-2 NOT FOUND gaps (not entity-classified) and 3+ named
print()
print("=== Quick Wins (1-2 NOT FOUND gaps, 3+ named) ===")
quick_wins = []
for r in rows:
    name = r.get('Institution_Name', '')
    tier = r.get('Tier', '')
    segment = r.get('Segment', '')
    gap_count = 0
    gap_roles = []
    named_count = 0
    for col in role_cols:
        v = (r.get(col, '') or '').strip()
        if is_named(v):
            named_count += 1
        elif is_gap(v) and not is_entity(v):
            gap_count += 1
            gap_roles.append(role_short[col])
    if 1 <= gap_count <= 2 and named_count >= 3:
        quick_wins.append((gap_count, gap_roles, name, tier, segment, named_count))

quick_wins.sort(key=lambda x: (-x[5], x[0]))
print(f"Total quick wins: {len(quick_wins)}")
for i, (gc, gr, name, tier, seg, named) in enumerate(quick_wins[:30]):
    roles_str = ",".join(gr)
    print(f"  {i+1:2d}. [{tier}] {name[:50]:50s} | {seg[:15]:15s} | named:{named}/7 gaps:{gc} roles:{roles_str}")

# Institutions with 0 named, 3+ NOT FOUND
print()
print("=== Institutions with 0 named, 3+ NOT FOUND ===")
zero_named = []
for r in rows:
    name = r.get('Institution_Name', '')
    tier = r.get('Tier', '')
    segment = r.get('Segment', '')
    named_count = sum(1 for col in role_cols if is_named(r.get(col, '')))
    entity_count = sum(1 for col in role_cols if is_entity(r.get(col, '')))
    notfound_count = sum(1 for col in role_cols if is_gap(r.get(col, '')) and not is_entity(r.get(col, '')))
    if named_count == 0 and notfound_count >= 3:
        zero_named.append((tier, name, segment, notfound_count, entity_count))

zero_named.sort(key=lambda x: (-x[3], x[0]))
for i, (tier, name, seg, nf, entity) in enumerate(zero_named[:20]):
    print(f"  {i+1:2d}. [{tier}] {name[:50]:50s} | {seg[:15]:15s} | notfound:{nf} entity:{entity}")

# Per-segment gap summary
print()
print("=== Per-Segment Gap Summary ===")
from collections import defaultdict
seg_stats = defaultdict(lambda: {'total': 0, 'named': 0, 'entity': 0, 'notfound': 0})
for r in rows:
    seg = r.get('Segment', 'Unknown')
    seg_stats[seg]['total'] += 7
    for col in role_cols:
        v = (r.get(col, '') or '').strip()
        if is_named(v):
            seg_stats[seg]['named'] += 1
        elif is_entity(v):
            seg_stats[seg]['entity'] += 1
        elif is_gap(v):
            seg_stats[seg]['notfound'] += 1

for seg in sorted(seg_stats.keys()):
    s = seg_stats[seg]
    pct = (s['named'] + s['entity']) / s['total'] * 100
    print(f"  {seg[:30]:30s} | cells:{s['total']:4d} named:{s['named']:3d} entity:{s['entity']:3d} notfound:{s['notfound']:3d} ({pct:.1f}%)")

# Detailed quick-win list for research (with gap details)
print()
print("=== DETAILED QUICK WIN TARGETS FOR v5.90 ===")
for i, (gc, gr, name, tier, seg, named) in enumerate(quick_wins[:15]):
    # Find the actual institution row
    for r in rows:
        if r.get('Institution_Name', '') == name:
            print(f"\n--- Target {i+1}: {name} (Tier {tier}, {seg}) ---")
            print(f"  Named: {named}/7, Gaps: {gc} ({','.join(gr)})")
            for col in role_cols:
                v = (r.get(col, '') or '').strip()
                if is_gap(v) and not is_entity(v):
                    print(f"  GAP {role_short[col]}: {v[:120]}")
            break

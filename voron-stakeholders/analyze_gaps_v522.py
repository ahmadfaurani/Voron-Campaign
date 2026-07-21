#!/usr/bin/env python3
import csv
from collections import defaultdict

with open('/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.21.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

roles = ['Chief Information Security Officer','Head of Governance Risk & Compliance','Chief Financial Officer','Chief Risk Officer','Head of Compliance','Chief Information Officer','Head of Internal Audit']
role_short = {'Chief Information Security Officer':'CISO','Head of Governance Risk & Compliance':'GRC','Chief Financial Officer':'CFO','Chief Risk Officer':'CRO','Head of Compliance':'Compliance','Chief Information Officer':'CIO','Head of Internal Audit':'IA'}

# Build a lookup
by_inst_name = {}
for r in rows:
    by_inst_name[r['Institution_Name']] = r

def categorize_nf(text, inst, seg):
    t = text.lower()
    if 'discontinued' in t or 'defunct' in t or 'parked domain' in t:
        return 'DEFUNCT'
    if 'tencent' in t or 'ant group' in t or 'no malaysia-specific' in t or 'handled at' in t and 'hq' in t:
        return 'FOREIGN_SUB'
    if 'parent' in t and ('hq' in t or 'group hq' in t):
        return 'FOREIGN_SUB'
    if 'cooperative' in t or 'koperasi' in t or seg == 'Cooperatives':
        return 'COOP'
    if 'government' in t or 'registrar' in t or "don't publicly list" in t or 'not publicly' in t and 'entity' in t:
        return 'GOV'
    if 'js-rendered' in t:
        return 'JS_RENDERED'
    return 'POTENTIALLY_FINDABLE'

not_found_institutions = []
for r in rows:
    inst = r['Institution_Name']
    seg = r['Segment']
    tier = r['Tier']
    nf_roles = []
    for col in roles:
        v = r.get(col,'').strip()
        if v.startswith('NOT FOUND'):
            nf_roles.append((col, categorize_nf(v, inst, seg)))
    if nf_roles:
        not_found_institutions.append((inst, seg, tier, nf_roles))

# Findable = POTENTIALLY_FINDABLE or JS_RENDERED
findable_by_inst = defaultdict(list)
for inst, seg, tier, nf_roles in not_found_institutions:
    for col, cat in nf_roles:
        if cat in ('POTENTIALLY_FINDABLE', 'JS_RENDERED'):
            findable_by_inst[(inst, seg, tier, cat)].append(col)

print(f"=== GAP ANALYSIS v5.21 ===")
print(f"Total institutions: {len(rows)}")
print(f"Total cells: {len(rows)*7}")
named = sum(1 for r in rows for col in roles if r.get(col,'').strip() and not r.get(col,'').strip().startswith('NOT FOUND'))
notfound = sum(1 for r in rows for col in roles if r.get(col,'').strip().startswith('NOT FOUND'))
print(f"Named: {named}, NOT FOUND: {notfound}, Empty: {len(rows)*7 - named - notfound}")
print()

# Count by category
cat_counts = defaultdict(int)
for inst, seg, tier, nf_roles in not_found_institutions:
    for col, cat in nf_roles:
        cat_counts[cat] += 1
print("--- NOT FOUND by category ---")
for cat, c in sorted(cat_counts.items(), key=lambda x: -x[1]):
    print(f"  {cat}: {c}")
print()

print(f"--- Potentially findable institutions ({len(findable_by_inst)}) ---")
sorted_insts = sorted(findable_by_inst.items(), key=lambda x: -len(x[1]))
for (inst, seg, tier, cat), gaps in sorted_insts[:40]:
    short_gaps = [role_short[g] for g in gaps]
    print(f"  [T{tier}|{seg}|{cat[:4]}] {inst}: {len(gaps)} -> {short_gaps}")

# CISO-specific gaps (highest priority)
print()
print("=== CISO GAPS (highest leverage) ===")
ciso_gaps = []
for r in rows:
    v = r.get('Chief Information Security Officer','').strip()
    if v.startswith('NOT FOUND'):
        cat = categorize_nf(v, r['Institution_Name'], r['Segment'])
        if cat in ('POTENTIALLY_FINDABLE', 'JS_RENDERED'):
            ciso_gaps.append((r['Institution_Name'], r['Segment'], r['Tier'], cat, v[:200]))
print(f"Findable CISO gaps: {len(ciso_gaps)}")
for inst, seg, tier, cat, snip in ciso_gaps[:25]:
    print(f"  [T{tier}|{seg}] {inst}: {snip[:150]}")

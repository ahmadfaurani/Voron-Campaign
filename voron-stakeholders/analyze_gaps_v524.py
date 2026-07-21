#!/usr/bin/env python3
import csv
from collections import defaultdict

with open('/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.23.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

roles = ['Chief Information Security Officer','Head of Governance Risk & Compliance','Chief Financial Officer','Chief Risk Officer','Head of Compliance','Chief Information Officer','Head of Internal Audit']
role_short = {'Chief Information Security Officer':'CISO','Head of Governance Risk & Compliance':'GRC','Chief Financial Officer':'CFO','Chief Risk Officer':'CRO','Head of Compliance':'Compliance','Chief Information Officer':'CIO','Head of Internal Audit':'IA'}

def categorize_nf(text, inst, seg):
    t = text.lower()
    if 'discontinued' in t or 'defunct' in t or 'parked domain' in t:
        return 'DEFUNCT'
    if 'tencent' in t or 'ant group' in t or 'no malaysia-specific' in t or ('handled at' in t and 'hq' in t):
        return 'FOREIGN_SUB'
    if 'parent' in t and ('hq' in t or 'group hq' in t):
        return 'FOREIGN_SUB'
    if 'cooperative' in t or 'koperasi' in t or seg == 'Cooperatives':
        return 'COOP'
    if 'government' in t or 'registrar' in t or ("don't publicly list" in t) or ('not publicly' in t and 'entity' in t):
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

findable_by_inst = defaultdict(list)
for inst, seg, tier, nf_roles in not_found_institutions:
    for col, cat in nf_roles:
        if cat in ('POTENTIALLY_FINDABLE', 'JS_RENDERED'):
            findable_by_inst[(inst, seg, tier, cat)].append(col)

print(f"=== GAP ANALYSIS v5.23 ===")
print(f"Total institutions: {len(rows)}")
print(f"Total cells: {len(rows)*7}")
named = sum(1 for r in rows for col in roles if r.get(col,'').strip() and not r.get(col,'').strip().startswith('NOT FOUND'))
notfound = sum(1 for r in rows for col in roles if r.get(col,'').strip().startswith('NOT FOUND'))
print(f"Named: {named} ({100*named/(len(rows)*7):.1f}%), NOT FOUND: {notfound} ({100*notfound/(len(rows)*7):.1f}%), Empty: {len(rows)*7 - named - notfound}")
print()

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
for (inst, seg, tier, cat), gaps in sorted_insts[:45]:
    short_gaps = [role_short[g] for g in gaps]
    print(f"  [T{tier}|{seg}|{cat[:4]}] {inst}: {len(gaps)} -> {short_gaps}")

print()
print("=== Per-segment coverage ===")
seg_stats = defaultdict(lambda: {'named':0,'nf':0,'total':0})
for r in rows:
    seg = r['Segment']
    for col in roles:
        v = r.get(col,'').strip()
        seg_stats[seg]['total'] += 1
        if v and not v.startswith('NOT FOUND'):
            seg_stats[seg]['named'] += 1
        elif v.startswith('NOT FOUND'):
            seg_stats[seg]['nf'] += 1
for seg in sorted(seg_stats.keys(), key=lambda s: -seg_stats[s]['total']):
    s = seg_stats[seg]
    pct = 100*s['named']/s['total'] if s['total'] else 0
    print(f"  {seg}: {s['named']}/{s['total']} ({pct:.0f}%) named, {s['nf']} NF")

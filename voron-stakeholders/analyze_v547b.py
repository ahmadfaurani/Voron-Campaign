#!/usr/bin/env python3
import csv, re
from collections import defaultdict

path = "/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.46.csv"
with open(path, encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

roles = ['Chief Information Security Officer','Head of Governance Risk & Compliance',
         'Chief Financial Officer','Chief Risk Officer','Head of Compliance',
         'Chief Information Officer','Head of Internal Audit']

# A cell is a REAL NAME if it contains a person name pattern (not NOT FOUND, not gap text)
def is_real_name(val):
    if not val or not val.strip():
        return False
    v = val.strip()
    gap_markers = ['NOT FOUND', 'not found', 'Not publicly disclosed', 'Not disclosed',
                   'Anti-bot block', 'JS-rendered', 'Pre-launch', 'Research confirmed',
                   'ENTITY LIKELY', 'No dedicated', 'No standalone', 'No public',
                   'N/A', '—', '-', 'not publicly', 'non-disclosure', 'non-existent']
    for marker in gap_markers:
        if marker.lower() in v.lower():
            return False
    # Check if it looks like a name (has uppercase letters, possibly Malay/Chinese/Indian name)
    # Real names typically have at least 2 words
    words = v.split()
    if len(words) < 2:
        return False
    return True

# Count real names vs gaps
total_real = 0
total_gap = 0
gap_by_role = defaultdict(int)
real_by_role = defaultdict(int)

for r in rows:
    for role in roles:
        val = r.get(role,'').strip()
        if is_real_name(val):
            total_real += 1
            real_by_role[role] += 1
        else:
            total_gap += 1
            gap_by_role[role] += 1

print("=== REAL NAME COVERAGE (actual stakeholders, not gap confirmations) ===")
print(f"Total: {total_real}/{len(rows)*7} ({total_real/(len(rows)*7)*100:.1f}%) real names")
print(f"Gaps: {total_gap}/{len(rows)*7} ({total_gap/(len(rows)*7)*100:.1f}%)")
print()
for role in roles:
    short = role.replace('Chief Information Security Officer','CISO').replace('Head of Governance Risk & Compliance','GRC').replace('Chief Financial Officer','CFO').replace('Chief Risk Officer','CRO').replace('Head of Compliance','Compliance').replace('Chief Information Officer','CIO').replace('Head of Internal Audit','Audit')
    print(f"  {short}: {real_by_role[role]} real / {gap_by_role[role]} gaps ({gap_by_role[role]/(real_by_role[role]+gap_by_role[role])*100:.0f}% gap)")

# Find institutions with most ACTIONABLE gaps (empty or NOT FOUND without specific research notes)
print("\n=== INSTITUTIONS WITH MOST GAPS (targetable) ===")
inst_data = []
for r in rows:
    inst = r.get('Institution_Name','')
    tier = r.get('Tier','')
    segment = r.get('Segment','')
    gaps = []
    real = 0
    for role in roles:
        val = r.get(role,'').strip()
        short = role.replace('Chief Information Security Officer','CISO').replace('Head of Governance Risk & Compliance','GRC').replace('Chief Financial Officer','CFO').replace('Chief Risk Officer','CRO').replace('Head of Compliance','Compliance').replace('Chief Information Officer','CIO').replace('Head of Internal Audit','Audit')
        if is_real_name(val):
            real += 1
        else:
            gaps.append(short)
    if gaps:
        inst_data.append((len(gaps), real, inst, tier, segment, gaps))

inst_data.sort(reverse=True)
for cnt, real, inst, tier, segment, gaps in inst_data[:30]:
    print(f"  {cnt} gaps ({real} filled) | {inst} | {tier}/{segment} | {', '.join(gaps)}")

# Focus on Development Finance and Tier 2/3 that have gaps
print("\n=== DEV FINANCE + TIER 2/3 WITH GAPS ===")
for cnt, real, inst, tier, segment, gaps in inst_data:
    if 'Development' in segment or tier in ('2','3','Tier 2','Tier 3'):
        print(f"  {cnt} gaps ({real} filled) | {inst} | {tier}/{segment} | {', '.join(gaps)}")

# Count by gap type
print("\n=== GAP TYPE BREAKDOWN ===")
empty_gaps = 0
notfound_gaps = 0
other_gaps = 0
for r in rows:
    for role in roles:
        val = r.get(role,'').strip()
        if not is_real_name(val):
            if not val:
                empty_gaps += 1
            elif 'NOT FOUND' in val.upper() or 'not found' in val.lower():
                notfound_gaps += 1
            else:
                other_gaps += 1
print(f"  Empty cells: {empty_gaps}")
print(f"  NOT FOUND (researched): {notfound_gaps}")
print(f"  Other gap text: {other_gaps}")

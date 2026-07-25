#!/usr/bin/env python3
import csv
from collections import defaultdict

path = "/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.46.csv"
with open(path, encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

roles = ['Chief Information Security Officer','Head of Governance Risk & Compliance',
         'Chief Financial Officer','Chief Risk Officer','Head of Compliance',
         'Chief Information Officer','Head of Internal Audit']

GAP_VALUES = {'', '—', '-', 'N/A', 'Not publicly disclosed', 'Not disclosed',
              'Research confirmed: not publicly disclosed',
              'Anti-bot block - not accessible', 'JS-rendered - not accessible',
              'Pre-launch - not disclosed'}

# Segment coverage
seg_counts = defaultdict(int)
seg_filled = defaultdict(int)
seg_total = defaultdict(int)

for r in rows:
    tier = r.get('Tier','')
    segment = r.get('Segment','')
    key = f"{tier} | {segment}"
    seg_counts[key] += 1
    for role in roles:
        val = r.get(role,'').strip()
        seg_total[key] += 1
        if val and val not in GAP_VALUES:
            seg_filled[key] += 1

print("=== SEGMENT COVERAGE ===")
for key in sorted(seg_counts.keys()):
    filled = seg_filled[key]
    total = seg_total[key]
    pct = filled/total*100 if total else 0
    print(f"{key}: {seg_counts[key]} inst, {filled}/{total} filled ({pct:.0f}%), gaps={total-filled}")

# Identify Development Finance institutions (Segment B) - not yet started
print("\n=== DEVELOPMENT FINANCE INSTITUTIONS (Segment B) ===")
dev_finance_keywords = ['BSN','Agrobank','SME Bank','EXIM','BPMB','PNB','MARA','CGC','MDV',
                        'Danaharta','SJPP','Tekun','Bank Simpanan','LPPSA','Co-op']
for r in rows:
    inst = r.get('Institution_Name','')
    if any(kw.lower() in inst.lower() for kw in dev_finance_keywords):
        tier = r.get('Tier','')
        segment = r.get('Segment','')
        filled_roles = []
        gap_roles = []
        for role in roles:
            val = r.get(role,'').strip()
            short = role.split()[0] if 'Information' not in role else role.replace('Chief Information Officer','CIO').replace('Head of Internal Audit','Audit').replace('Head of Governance Risk & Compliance','GRC').replace('Head of Compliance','Compliance').replace('Chief Information Security Officer','CISO')
            if val and val not in GAP_VALUES:
                filled_roles.append(f"{short}={val[:30]}")
            else:
                gap_roles.append(short)
        print(f"\n{inst} [{tier}/{segment}]")
        print(f"  Filled: {len(filled_roles)}/7 | Gaps: {', '.join(gap_roles)}")
        for fr in filled_roles:
            print(f"    {fr}")

# Tier 2/3 banks
print("\n=== TIER 2 & 3 BANKS (Segment E) ===")
tier23_keywords = ['Alliance','Affin','Muamalat','KFH','Kuwait','Bank Islam','Bank Rakyat',
                   'AmBank','Am Investment','Bank of China','ICBC','Standard Chartered',
                   'Citibank','Citi','OCBC','UOB','HSBC','MUFG','Sumitomo','Mizuho',
                   'BNP Paribas','Deutsche','JPMorgan','Bank of America','ANZ']
for r in rows:
    inst = r.get('Institution_Name','')
    tier = r.get('Tier','')
    if tier in ('Tier 2','Tier 3','2','3') or any(kw.lower() in inst.lower() for kw in ['Alliance','Affin','Muamalat','KFH','Kuwait']):
        segment = r.get('Segment','')
        gap_roles = []
        for role in roles:
            val = r.get(role,'').strip()
            short = role.replace('Chief Information Security Officer','CISO').replace('Head of Governance Risk & Compliance','GRC').replace('Chief Financial Officer','CFO').replace('Chief Risk Officer','CRO').replace('Head of Compliance','Compliance').replace('Chief Information Officer','CIO').replace('Head of Internal Audit','Audit')
            if not val or val in GAP_VALUES:
                gap_roles.append(short)
        print(f"  {inst} [{tier}/{segment}] gaps: {', '.join(gap_roles)}")

# Top gap institutions (most fillable - those with actual names missing, not confirmed gaps)
print("\n=== TOP 25 GAP INSTITUTIONS (most missing roles) ===")
inst_gaps = []
for r in rows:
    inst = r.get('Institution_Name','')
    tier = r.get('Tier','')
    segment = r.get('Segment','')
    gaps = []
    for role in roles:
        val = r.get(role,'').strip()
        if not val or val in GAP_VALUES:
            short = role.replace('Chief Information Security Officer','CISO').replace('Head of Governance Risk & Compliance','GRC').replace('Chief Financial Officer','CFO').replace('Chief Risk Officer','CRO').replace('Head of Compliance','Compliance').replace('Chief Information Officer','CIO').replace('Head of Internal Audit','Audit')
            gaps.append(short)
    if gaps:
        inst_gaps.append((len(gaps), inst, tier, segment, gaps))

inst_gaps.sort(reverse=True)
for cnt, inst, tier, segment, gaps in inst_gaps[:25]:
    print(f"  {cnt} gaps | {inst} | {tier}/{segment} | {', '.join(gaps)}")

total_gaps = sum(1 for r in rows for role in roles if not r.get(role,'').strip() or r.get(role,'').strip() in GAP_VALUES)
total_filled = len(rows)*7 - total_gaps
print(f"\n=== TOTAL: {len(rows)} institutions, {total_filled}/{len(rows)*7} filled ({total_filled/(len(rows)*7)*100:.1f}%), {total_gaps} gaps ===")

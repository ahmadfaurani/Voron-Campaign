import csv
from collections import defaultdict

rows = []
with open('/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.44.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for r in reader:
        rows.append(r)

roles = ['Chief Information Security Officer','Head of Governance Risk & Compliance','Chief Financial Officer','Chief Risk Officer','Head of Compliance','Chief Information Officer','Head of Internal Audit']
short = {'Chief Information Security Officer':'CISO','Head of Governance Risk & Compliance':'GRC','Chief Financial Officer':'CFO','Chief Risk Officer':'CRO','Head of Compliance':'Comp','Chief Information Officer':'CIO','Head of Internal Audit':'IA'}

def is_filled(v):
    if not v or v.strip() == '':
        return False
    v = v.strip()
    if v.startswith('NOT FOUND') or 'NOT FOUND' in v[:30]:
        return False
    return True

inst_gaps = []
for r in rows:
    tier = r['Tier']; seg = r['Segment']; name = r['Institution_Name']
    filled = 0; missing_roles = []
    for role in roles:
        if is_filled(r[role]):
            filled += 1
        else:
            missing_roles.append(short[role])
    inst_gaps.append((tier, seg, name, filled, missing_roles))

print("=== FILLED COUNT DISTRIBUTION ===")
counts = defaultdict(int)
for g in inst_gaps:
    counts[g[3]] += 1
for k in sorted(counts.keys()):
    print(f"  {k}/7: {counts[k]} institutions")

total_filled = sum(g[3] for g in inst_gaps)
total_cells = len(rows) * 7
print(f"\nTotal institutions: {len(rows)}")
print(f"Total cells: {total_cells}")
print(f"Total filled: {total_filled}")
print(f"Coverage: {total_filled/total_cells*100:.1f}%")
print(f"Total gaps: {total_cells - total_filled}")

print("\n=== TIER 1 LICENSED BANKS - ALL GAPS ===")
t1 = [g for g in inst_gaps if g[0] == '1']
t1.sort(key=lambda x: x[3])
for tier, seg, name, filled, missing in t1:
    if filled < 7:
        print(f"  {filled}/7 | {name} | missing: {','.join(missing)}")

print(f"\n=== DEVELOPMENT FIs - ALL GAPS ===")
dev = [g for g in inst_gaps if g[1] in ('Development FIs','Development Finance','Development')]
dev.sort(key=lambda x: x[3])
for tier, seg, name, filled, missing in dev:
    if filled < 7:
        print(f"  {filled}/7 | {name} | missing: {','.join(missing)}")

print(f"\n=== INSURERS/TAKAFUL - ALL GAPS (sorted by fills) ===")
ins = [g for g in inst_gaps if g[1] in ('Insurers','Takaful','Insurance')]
ins.sort(key=lambda x: x[3])
for tier, seg, name, filled, missing in ins:
    if filled < 7:
        print(f"  {filled}/7 | {name} ({seg}) | missing: {','.join(missing)}")

print(f"\n=== INVESTMENT BANKS / ASSET MGMT - ALL GAPS ===")
inv = [g for g in inst_gaps if g[1] in ('Asset Management','Investment Banks','Fund Management','Asset Mgmt')]
inv.sort(key=lambda x: x[3])
for tier, seg, name, filled, missing in inv:
    if filled < 7:
        print(f"  {filled}/7 | {name} ({seg}) | missing: {','.join(missing)}")

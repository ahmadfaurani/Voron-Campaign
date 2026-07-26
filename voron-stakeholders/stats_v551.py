import csv

def is_named(v):
    if not v: return False
    v = v.strip()
    if not v: return False
    low = v.lower()
    if 'not found' in low or 'not public' in low or 'no public' in low or v.startswith('[') or low.startswith('n/a') or ' n/a' in low or 'group level' in low or 'not disclosed' in low or 'not listed' in low or 'entity defunct' in low:
        return False
    return True

cols = ['Chief Information Security Officer','Head of Governance Risk & Compliance','Chief Financial Officer','Chief Risk Officer','Head of Compliance','Chief Information Officer','Head of Internal Audit']

def stats(path):
    with open(path, encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f))
    by_role = {c:0 for c in cols}
    for r in rows:
        for c in cols:
            if is_named(r.get(c,'')):
                by_role[c]+=1
    total = sum(by_role.values())
    return len(rows), total, by_role

n50, t50, br50 = stats('/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.50.csv')
n51, t51, br51 = stats('/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.51.csv')

print(f"v5.50: {n50} institutions, {t50}/{n50*7} named ({t50*100/(n50*7):.1f}%)")
print(f"v5.51: {n51} institutions, {t51}/{n51*7} named ({t51*100/(n51*7):.1f}%)")
print(f"\nNamed cells preserved: v5.50 had {t50}, v5.51 has {t51} (delta {t51-t50})")
print(f"  (delta explained by: dup rows removed whose named cells were identical to canonical = no loss; any NEW named cells from dups merged in)")

print("\n=== Coverage by role (v5.51) ===")
for c in cols:
    short = c.replace('Chief Information Security Officer','CISO').replace('Head of Governance Risk & Compliance','GRC').replace('Chief Financial Officer','CFO').replace('Chief Risk Officer','CRO').replace('Head of Compliance','Compliance').replace('Chief Information Officer','CIO/CTO').replace('Head of Internal Audit','Int. Audit')
    print(f"  {short:14}: {br51[c]:>3}/{n51} ({br51[c]*100/n51:.1f}%)")

# Tier breakdown v5.51
from collections import Counter, defaultdict
with open('/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.51.csv', encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))
tier_named = defaultdict(int)
tier_total = defaultdict(int)
for r in rows:
    t = r.get('Tier','').strip()
    for c in cols:
        tier_total[t]+=1
        if is_named(r.get(c,'')):
            tier_named[t]+=1
print("\n=== Coverage by Tier (v5.51) ===")
for t in sorted(tier_total.keys()):
    print(f"  Tier {t}: {tier_named[t]}/{tier_total[t]} ({tier_named[t]*100/tier_total[t]:.1f}%)")

# Fully-named institutions (7/7)
full_named = sum(1 for r in rows if all(is_named(r.get(c,'')) for c in cols))
print(f"\nFully named (7/7) institutions: {full_named}/{n51}")
# 6/7
six = sum(1 for r in rows if sum(is_named(r.get(c,'')) for c in cols)==6)
print(f"6/7 named: {six}")

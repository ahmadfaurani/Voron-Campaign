import csv

def load(path):
    with open(path, encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f))
    return {r.get('Institution_Name','').strip(): r for r in rows}

v551 = load('/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.51.csv')
canon = load('/home/p62operator/.openclaw/workspace-hoi/vorondrq-rmit-campaign/prospects/prospect-database-7stakeholders.csv')

targets = [
    ('Public Bank Berhad', 'Chief Information Security Officer', 'Irene Deng'),
    ('Public Islamic Bank Berhad', 'Chief Information Security Officer', 'Irene Deng'),
    ('Bank Muamalat Malaysia Berhad', 'Chief Information Security Officer', 'Ismamuradi'),
]

print("=== 4 PENDING T1 FILLS: v5.51 (working) vs canonical ===\n")
for inst, role, keyname in targets:
    print(f"## {inst} / {role}")
    rv = v551.get(inst, {}).get(role, '[institution not in v5.51]')
    cv = canon.get(inst, {}).get(role, '[institution not in canonical]')
    print(f"  v5.51:      {rv[:110]}")
    print(f"  canonical:  {cv[:110]}")
    print(f"  -> v5.51 contains '{keyname}': {keyname.lower() in rv.lower()}")
    print()

# ICBC
print("## ICBC (search)")
for n in v551:
    if 'icbc' in n.lower() or 'industrial' in n.lower() and 'china' in n.lower():
        print(f"  v5.51 has: {n}")
for n in canon:
    if 'icbc' in n.lower() or 'industrial' in n.lower() and 'china' in n.lower():
        print(f"  canon has: {n}")
# ICBC CFO
for inst in v551:
    if 'icbc' in inst.lower() or ('industrial' in inst.lower() and 'commercial' in inst.lower()):
        cfo = v551[inst].get('Chief Financial Officer','')
        print(f"  v5.51 {inst} CFO: {cfo[:110]}")
for inst in canon:
    if 'icbc' in inst.lower() or ('industrial' in inst.lower() and 'commercial' in inst.lower()):
        cfo = canon[inst].get('Chief Financial Officer','')
        print(f"  canon {inst} CFO: {cfo[:110]}")

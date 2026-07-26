import csv

def load(path):
    with open(path, encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

v542 = load('/home/p62operator/.openclaw/workspace-hoi/vorondrq-rmit-campaign/operations/prospect-databases/prospect-database-enriched-v5.42.csv')
v551 = load('/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.51.csv')

def nameset(rows):
    return set(r.get('Institution_Name','').strip() for r in rows)

n542, n551 = nameset(v542), nameset(v551)
print(f"v5.42: {len(v542)} rows, {len(n542)} unique names")
print(f"v5.51: {len(v551)} rows, {len(n551)} unique names")

# header comparison
h542 = list(v542[0].keys()) if v542 else []
h551 = list(v551[0].keys()) if v551 else []
print(f"\nv5.42 header ({len(h542)} cols): {h542}")
print(f"v5.51 header ({len(h551)} cols): {h551}")
print(f"Headers identical: {h542 == h551}")

# institution overlap
common = n542 & n551
only542 = n542 - n551
only551 = n551 - n542
print(f"\nCommon institutions: {len(common)}")
print(f"Only in v5.42: {len(only542)}")
print(f"Only in v5.51: {len(only551)}")

if only542:
    print("\n=== In v5.42 but NOT v5.51 (sample 25) ===")
    for n in sorted(only542)[:25]:
        print(f"  {n}")
if only551:
    print(f"\n=== In v5.51 but NOT v5.42 (first 25 of {len(only551)}) ===")
    for n in sorted(only551)[:25]:
        print(f"  {n}")

# check if v5.51 names are a superset (v5.42 ⊂ v5.51)?
print(f"\nv5.42 is subset of v5.51: {n542.issubset(n551)}")
print(f"v5.51 is subset of v5.42: {n551.issubset(n542)}")

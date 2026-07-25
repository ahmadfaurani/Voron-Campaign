import csv
from collections import defaultdict

with open('prospect-database-enriched-v5.45.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

roles = ['Chief Information Security Officer','Head of Governance Risk & Compliance',
         'Chief Financial Officer','Chief Risk Officer','Head of Compliance',
         'Chief Information Officer','Head of Internal Audit']

def status(v):
    v = (v or '').strip()
    if not v:
        return 'notfound'
    vl = v.lower()
    if vl.startswith('not ') or vl.startswith('notfound') or vl.startswith('none') or 'no dedicated' in vl[:30] or 'no standalone' in vl[:40] or vl.startswith('confirmed absence'):
        return 'notfound'
    if 'role exists' in vl[:30]:
        return 'exists'
    return 'filled'

inst_cov = []
for i, r in enumerate(rows):
    inst = r['Institution_Name']
    fc = sum(1 for ro in roles if status(r.get(ro,''))=='filled')
    ec = sum(1 for ro in roles if status(r.get(ro,''))=='exists')
    nf = sum(1 for ro in roles if status(r.get(ro,''))=='notfound')
    inst_cov.append((fc, ec, nf, inst, r.get('Segment',''), i+2))

total_cells = len(rows)*7
filled = sum(1 for r in rows for ro in roles if status(r.get(ro,''))=='filled')
exists = sum(1 for r in rows for ro in roles if status(r.get(ro,''))=='exists')
notfound = sum(1 for r in rows for ro in roles if status(r.get(ro,''))=='notfound')
print(f"Total institutions: {len(rows)} | cells: {total_cells}")
print(f"Filled: {filled}, Exists(no name): {exists}, NotFound: {notfound}")
print(f"Effective coverage: {(filled+exists)/total_cells*100:.1f}%")
print()

zero = [x for x in inst_cov if x[0]==0 and x[1]==0]
low = [x for x in inst_cov if 0 < (x[0]+x[1]) <= 2]
print(f"=== 0/7 (no fills, no role-exists): {len(zero)} ===")
for fc, ec, nf, inst, seg, rown in sorted(zero)[:50]:
    print(f"  Row {rown} [{seg}] {inst}")
print()
print(f"=== 1-2/7: {len(low)} ===")
for fc, ec, nf, inst, seg, rown in sorted(low)[:60]:
    print(f"  {fc}f+{ec}e Row {rown} [{seg}] {inst}")

print()
print("=== PER-ROLE ===")
for ro in roles:
    f = sum(1 for r in rows if status(r.get(ro,''))=='filled')
    e = sum(1 for r in rows if status(r.get(ro,''))=='exists')
    n = sum(1 for r in rows if status(r.get(ro,''))=='notfound')
    print(f"  {ro}: filled={f}, exists={e}, notfound={n}")

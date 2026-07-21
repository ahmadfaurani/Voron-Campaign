import csv
from collections import Counter

def load(p):
    with open(p,newline='',encoding='utf-8-sig') as f:
        rows=list(csv.reader(f))
    h=rows[0]; d=[r for r in rows[1:] if any(c.strip() for c in r)]
    for r in d:
        while len(r)<len(h): r.append("")
    return h,d

def usable(v):
    v=v.strip()
    if not v or v.upper().startswith("NOT FOUND"): return False
    return True

h,d=load("runs/prospects-latest.csv")
stake=h[3:]
names=[r[2].strip() for r in d]
dups=[(n,c) for n,c in Counter(names).items() if c>1]
print("DUPLICATE INSTITUTION NAMES in current DB:")
for n,c in dups:
    print(f"  {n} x{c}")
    for r in d:
        if r[2].strip()==n:
            u=sum(1 for x in r[3:3+7] if usable(x))
            print(f"     T{r[0]} {r[1]} | {u}/7 usable | cells: {[x[:30] for x in r[3:3+7]]}")

# T1 detail
print("\n=== TIER 1 DETAIL (current) ===")
t1=[r for r in d if r[0].strip()=="1"]
sevencount=0
for r in sorted(t1,key=lambda x:x[2]):
    u=sum(1 for x in r[3:3+7] if usable(x))
    roles=[stake[i].split()[0]+" "+stake[i].split()[-1] for i,x in enumerate(r[3:3+7]) if not usable(x)]
    missing=[stake[i] for i,x in enumerate(r[3:3+7]) if not usable(x)]
    mark="7/7" if u==7 else f"{u}/7"
    if u==7: sevencount+=1
    print(f"  {mark} | {r[2].strip()} | missing: {missing if missing else '-'}")
print(f"\nT1 total rows: {len(t1)} | distinct: {len(set(r[2].strip() for r in t1))}")
print(f"T1 true 7/7: {sevencount}")

# Tier/segment for T1
print("\nT1 segments:", dict(Counter(r[1].strip() for r in t1)))

# Full tier x segment matrix
print("\nTIER x SEGMENT MATRIX:")
mat={}
for r in d:
    mat.setdefault(r[0].strip(),{}).setdefault(r[1].strip(),0)
    mat[r[0].strip()][r[1].strip()]+=1
segs=sorted({r[1].strip() for r in d})
print(f"{'Tier':>5} | "+" | ".join(f"{s[:10]:>10}" for s in segs)+" | TOT")
for t in sorted(mat):
    row=[mat[t].get(s,0) for s in segs]
    print(f"  T{t:>3} | "+" | ".join(f"{v:>10}" for v in row)+f" | {sum(row)}")

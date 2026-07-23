import csv, json, re, hashlib
from collections import Counter

CSV_PATH = "operations/prospect-databases/prospect-database-enriched-v5.22.csv"
SNAPSHOT_OUT = "runs/snapshot-v522-20260721-1653.json"

ROLE_SHORT = {
 "Chief Information Security Officer":"CISO",
 "Head of Governance Risk & Compliance":"GRC",
 "Chief Financial Officer":"CFO",
 "Chief Risk Officer":"CRO",
 "Head of Compliance":"Compliance",
 "Chief Information Officer":"CIO",
 "Head of Internal Audit":"IA",
}

with open(CSV_PATH, newline='', encoding='utf-8-sig') as f:
    content = f.read()
    f.seek(0)
    rows = list(csv.reader(f))

header = rows[0]
data = [r for r in rows[1:] if any(c.strip() for c in r)]
scols = header[3:]
n_roles = len(scols)
total = len(data)
file_md5 = hashlib.md5(content.encode()).hexdigest()

def classify(val):
    v = val.strip()
    if not v: return "EMPTY"
    up = v.upper()
    if up.startswith("ENTITY-NON-EXISTENT") or up.startswith("ENTITY NON"): return "NONEXISTENT"
    if up.startswith("NOT FOUND") or up.startswith("NOTFOUND"): return "NOT_FOUND"
    if up in ("N/A","NA","-","--","TBD","UNKNOWN","PENDING"): return "EMPTY"
    return "NAMED"

def name_only(val):
    v = re.split(r'\s*\|', val.strip())[0].strip()
    v = re.split(r'\s*\[', v)[0].strip()
    return v[:50]

tier_counts = Counter(r[0].strip() for r in data if r[0].strip())
seg_counts = Counter(r[1].strip() for r in data if r[1].strip())

cls_counts = Counter()
role_stats = {}
for i, role in enumerate(scols):
    rs = Counter()
    for r in data:
        while len(r) < 3+n_roles: r.append("")
        c = classify(r[3+i]); rs[c]+=1; cls_counts[c]+=1
    role_stats[role] = dict(rs)

total_cells = total*n_roles
role_named = [(role, role_stats[role].get("NAMED",0)) for role in scols]

per_row_named=[]
inst_records=[]
for r in data:
    while len(r) < 3+n_roles: r.append("")
    named_idx=[i for i in range(n_roles) if classify(r[3+i])=="NAMED"]
    contacts={ROLE_SHORT.get(scols[i],scols[i]): name_only(r[3+i]) for i in named_idx}
    per_row_named.append(len(named_idx))
    inst_records.append({
        "tier":r[0].strip(),"segment":r[1].strip(),"name":r[2].strip(),
        "named":len(named_idx),"contacts":contacts
    })

with_any=sum(1 for n in per_row_named if n>0)
fully=sum(1 for n in per_row_named if n==7)
empty_rows=sum(1 for n in per_row_named if n==0)
density=Counter(per_row_named)

tier1=[x for x in inst_records if x["tier"]=="1"]
t1_with=sum(1 for x in tier1 if x["named"]>0)
t1_full=sum(1 for x in tier1 if x["named"]==7)
t1_empty=[x["name"] for x in tier1 if x["named"]==0]

print("HEADER:", header)
print("FILE_MD5:", file_md5)
print("TOTAL INSTITUTIONS:", total, "| ROLES:", n_roles, "| TOTAL CELLS:", total_cells)
print("\nTIER:", dict(sorted(tier_counts.items())))
print("\nSEGMENT:")
for k,v in seg_counts.most_common(): print(f"  {k}: {v}")
print("\nCELL CLASSIFICATION:")
for k in ["NAMED","NOT_FOUND","NONEXISTENT","EMPTY"]:
    print(f"  {k}: {cls_counts[k]} ({cls_counts[k]/total_cells*100:.1f}%)")
print("\nPER-ROLE NAMED (ranked):")
for role,n in sorted(role_named,key=lambda x:-x[1]):
    print(f"  {ROLE_SHORT.get(role,role):12s}: {n}/{total} ({n/total*100:.1f}%)")
print("\nROW DENSITY (NAMED/7):")
for k in sorted(density.keys(),reverse=True): print(f"  {k}/7: {density[k]}")
print(f"\n>=1 NAMED: {with_any}/{total} ({with_any/total*100:.1f}%)")
print(f"Fully 7/7: {fully}/{total} ({fully/total*100:.1f}%)")
print(f"0 NAMED (has NOT_FOUND): {empty_rows}/{total} ({empty_rows/total*100:.1f}%)")
print(f"\n=== TIER 1 ({len(tier1)} banks) ===")
print(f"  >=1 NAMED: {t1_with}/{len(tier1)} ({t1_with/len(tier1)*100:.1f}%)")
print(f"  fully 7/7: {t1_full}/{len(tier1)}")
print(f"  0 NAMED: {len(t1_empty)} -> {t1_empty}")
print("\nTier 1 full detail:")
for x in sorted(tier1,key=lambda z:(-z["named"],z["name"])):
    roles = ", ".join(f"{r}:{nm}" for r,nm in x["contacts"].items()) if x["contacts"] else "NONE"
    print(f"  [{x['named']}/7] {x['name']} -> {roles}")

snapshot={
 "file":CSV_PATH,"md5":file_md5,"total":total,"n_roles":n_roles,"total_cells":total_cells,
 "tier_counts":dict(tier_counts),"seg_counts":dict(seg_counts),
 "cell_classification":dict(cls_counts),
 "role_named":{ROLE_SHORT.get(r,r):n for r,n in role_named},
 "density":dict(density),"with_any":with_any,"fully":fully,"zero_named":empty_rows,
 "tier1":{"count":len(tier1),"with_named":t1_with,"fully7":t1_full,"empty":t1_empty},
 "institutions":inst_records
}
with open(SNAPSHOT_OUT,"w") as f: json.dump(snapshot,f,indent=2)
print("\nSNAPSHOT SAVED:", SNAPSHOT_OUT)

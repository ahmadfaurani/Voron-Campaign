import csv, json, sys
from collections import Counter, defaultdict

CSV_PATH = "runs/prospects-latest.csv"

with open(CSV_PATH, newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
data = rows[1:]
print("HEADER:", header)
print("TOTAL ROWS (excl header):", len(data))

# Identify stakeholder columns (D onwards = index 3+)
stakeholder_cols = header[3:]
print("STAKEHOLDER COLS:", stakeholder_cols, "=> count:", len(stakeholder_cols))

# Empty trailing row guard
data = [r for r in data if any(c.strip() for c in r)]
print("NON-EMPTY ROWS:", len(data))

# Tier counts
tier_counts = Counter(r[0].strip() for r in data if r[0].strip())
print("\nTIER COUNTS:", dict(sorted(tier_counts.items())))

# Segment counts
seg_counts = Counter(r[1].strip() for r in data if r[1].strip())
print("\nSEGMENT COUNTS:")
for k,v in seg_counts.most_common():
    print(f"  {k}: {v}")

# Per-row enrichment: count usable contacts (non-empty AND not 'NOT FOUND')
def usable(val):
    v = val.strip()
    if not v: return False
    if v.upper() in ("NOT FOUND","NOTFOUND","N/A","NA","-","--"): return False
    return True

def populated_raw(val):
    return bool(val.strip())

per_row_usable = []
per_row_raw = []
for r in data:
    # pad row
    while len(r) < len(header): r.append("")
    contacts = r[3:3+len(stakeholder_cols)]
    u = sum(1 for c in contacts if usable(c))
    raw = sum(1 for c in contacts if populated_raw(c))
    per_row_usable.append(u)
    per_row_raw.append(raw)

total = len(data)
with_any_usable = sum(1 for u in per_row_usable if u>0)
with_any_raw = sum(1 for u in per_row_raw if u>0)
completely_empty = sum(1 for u in per_row_raw if u==0)
print(f"\nENRICHMENT (usable contacts, excluding NOT FOUND):")
print(f"  Prospects with >=1 usable contact: {with_any_usable}/{total} = {with_any_usable/total*100:.1f}%")
print(f"  Completely empty (no cells populated at all): {completely_empty}/{total} = {completely_empty/total*100:.1f}%")
print(f"\nENRICHMENT (raw populated cells, including NOT FOUND):")
print(f"  Prospects with >=1 populated cell: {with_any_raw}/{total} = {with_any_raw/total*100:.1f}%")

# Per-stakeholder-role completion (usable)
print("\nPER-ROLE COMPLETION (usable contacts):")
role_usable = []
for i, role in enumerate(stakeholder_cols):
    col_vals = [r[3+i] if len(r)>3+i else "" for r in data]
    u = sum(1 for v in col_vals if usable(v))
    raw = sum(1 for v in col_vals if populated_raw(v))
    notfound = sum(1 for v in col_vals if v.strip().upper()=="NOT FOUND")
    role_usable.append((role, u, raw, notfound, total))
    print(f"  {role}: usable={u}/{total} ({u/total*100:.1f}%), raw_populated={raw}, NOT_FOUND={notfound}")

# Rank roles by usable completion
print("\nROLE RANKING (by usable completion rate):")
for role,u,raw,nf,t in sorted(role_usable, key=lambda x:-x[1]):
    print(f"  {role}: {u}/{t} = {u/t*100:.1f}%")

# Total usable contact cells
total_usable_cells = sum(u for _,u,_,_,_ in role_usable)
total_raw_cells = sum(raw for _,_,raw,_,_ in role_usable)
total_possible = total*len(stakeholder_cols)
print(f"\nTOTAL USABLE CONTACT CELLS: {total_usable_cells}/{total_possible} = {total_usable_cells/total_possible*100:.1f}%")
print(f"TOTAL RAW POPULATED CELLS: {total_raw_cells}/{total_possible} = {total_raw_cells/total_possible*100:.1f}%")

# Tier 1 banks with contact data — priority
print("\n=== TIER 1 LICENSED BANKS (priority) ===")
tier1 = [r for r in data if r[0].strip()=="1"]
print(f"Tier 1 count: {len(tier1)}")
tier1_with = 0
tier1_full = []
for r in tier1:
    while len(r) < len(header): r.append("")
    contacts = r[3:3+len(stakeholder_cols)]
    u = sum(1 for c in contacts if usable(c))
    if u>0:
        tier1_with+=1
        tier1_full.append((r[2].strip(), u, [stakeholder_cols[i] for i,c in enumerate(contacts) if usable(c)]))
print(f"Tier 1 with >=1 usable contact: {tier1_with}/{len(tier1)} = {tier1_with/len(tier1)*100:.1f}%")
print("Tier 1 institutions & their populated roles:")
for name,u,roles in tier1_full:
    print(f"  - {name}: {u} contacts -> {', '.join(roles)}")

# Tier 1 with NO usable contacts
print("\nTier 1 institutions with NO usable contacts (outreach blockers):")
tier1_empty = [r[2].strip() for r in tier1 if sum(1 for c in r[3:3+len(stakeholder_cols)] if usable(c))==0]
for n in tier1_empty:
    print(f"  - {n}")

# Save snapshot for comparison
snapshot = {
    "header": header,
    "total": total,
    "tier_counts": dict(tier_counts),
    "seg_counts": dict(seg_counts),
    "with_any_usable": with_any_usable,
    "completely_empty": completely_empty,
    "role_usable": {r[0]: r[1] for r in role_usable},
    "total_usable_cells": total_usable_cells,
    "institutions": [r[2].strip() for r in data],
    "tier1_with_contacts": [t[0] for t in tier1_full],
}
with open("runs/snapshot-current.json","w") as f:
    json.dump(snapshot, f, indent=2)
print("\nSnapshot saved to runs/snapshot-current.json")

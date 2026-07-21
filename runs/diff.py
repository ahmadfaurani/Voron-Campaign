import csv, json
from collections import Counter

def load(path):
    with open(path, newline='', encoding='utf-8-sig') as f:
        rows = list(csv.reader(f))
    header = rows[0]; data = rows[1:]
    data = [r for r in data if any(c.strip() for c in r)]
    for r in data:
        while len(r) < len(header): r.append("")
    return header, data

def usable(val):
    v = val.strip()
    if not v: return False
    if v.upper().startswith("NOT FOUND"): return False
    if v.upper() in ("N/A","NA","-","--"): return False
    return True

h_old, old = load("runs/prospects-prestreamline.csv")
h_new, new = load("runs/prospects-latest.csv")
print("OLD rows:", len(old), "| NEW rows:", len(new))

stake_old = h_old[3:]
stake_new = h_new[3:]
assert stake_old == stake_new, "stakeholder columns differ!"

def idx(data):
    d = {}
    for r in data:
        d[r[2].strip()] = r
    return d

old_idx = idx(old)
new_idx = idx(new)
old_names = set(old_idx)
new_names = set(new_idx)
removed = old_names - new_names
added = new_names - old_names
print(f"REMOVED: {len(removed)} | ADDED: {len(added)}")
if added:
    for n in sorted(added): print("  +", n)

print("\nREMOVED by tier:")
for t in sorted(Counter(old_idx[n][0] for n in removed)):
    print(f"  T{t}: {Counter(old_idx[n][0] for n in removed)[t]}")
print("REMOVED by segment:")
for s,c in Counter(old_idx[n][1] for n in removed).most_common():
    print(f"  {s}: {c}")

print("\nREMOVED institutions (usable contacts they had pre-streamline):")
rem_with = 0
for n in sorted(removed):
    r = old_idx[n]
    contacts = r[3:3+len(stake_old)]
    u = sum(1 for c in contacts if usable(c))
    if u>0: rem_with+=1
    roles = [stake_old[i] for i,c in enumerate(contacts) if usable(c)]
    tag = f"HAD {u}" if u>0 else "EMPTY"
    extra = f" -> {', '.join(roles)}" if roles else ""
    print(f"  [{tag}] T{r[0]} {r[1]} | {n}{extra}")
print(f"\nOf {len(removed)} removed: {rem_with} had >=1 usable contact, {len(removed)-rem_with} empty/NOT-FOUND-only.")

def total_usable(data, ncol):
    return sum(sum(1 for c in r[3:3+ncol] if usable(c)) for r in data)
tu_old = total_usable(old, len(stake_old))
tu_new = total_usable(new, len(stake_new))
print(f"\nTOTAL USABLE CELLS: old={tu_old} -> new={tu_new}  delta={tu_new-tu_old}")
print(f"  old rate: {tu_old}/{len(old)*7} = {tu_old/(len(old)*7)*100:.1f}%")
print(f"  new rate: {tu_new}/{len(new)*7} = {tu_new/(len(new)*7)*100:.1f}%")

print("\nPER-ROLE USABLE (old -> new):")
for i, role in enumerate(stake_old):
    o = sum(1 for r in old if usable(r[3+i]))
    n = sum(1 for r in new if usable(r[3+i]))
    print(f"  {role}: {o} -> {n} (delta {n-o:+d})")

old_with = sum(1 for r in old if any(usable(c) for c in r[3:3+len(stake_old)]))
new_with = sum(1 for r in new if any(usable(c) for c in r[3:3+len(stake_new)]))
print(f"\n>=1 usable: old {old_with}/{len(old)} ({old_with/len(old)*100:.1f}%) -> new {new_with}/{len(new)} ({new_with/len(new)*100:.1f}%)")

# Retained institutions losing real named contacts
print("\nRETAINED institutions that LOST a real named contact (name present old, absent new):")
retained = old_names.intersection(new_names)
lost_real = []
for n in retained:
    ro = old_idx[n]; rn = new_idx[n]
    def names_from(r):
        s=set()
        for c in r[3:3+len(stake_old)]:
            if usable(c):
                for part in c.split(","):
                    part=part.strip()
                    if part and "NOT FOUND" not in part.upper():
                        s.add(part.lower())
        return s
    dropped = names_from(ro) - names_from(rn)
    if dropped:
        lost_real.append((n, dropped))
print(f"  count: {len(lost_real)}")
for n,dropped in lost_real[:25]:
    print(f"    {n}: lost {sorted(dropped)}")

summary = {
  "old_total": len(old), "new_total": len(new),
  "removed_count": len(removed), "added_count": len(added),
  "removed_with_contacts": rem_with,
  "removed_empty_only": len(removed)-rem_with,
  "tu_old": tu_old, "tu_new": tu_new, "tu_delta": tu_new-tu_old,
  "old_with_contact": old_with, "new_with_contact": new_with,
  "removed_names": sorted(removed), "added_names": sorted(added),
  "lost_real_in_retained": [(n, sorted(d)) for n,d in lost_real],
}
json.dump(summary, open("runs/diff-summary.json","w"), indent=2)
print("\nSaved runs/diff-summary.json")

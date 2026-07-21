import csv, re

def load(path):
    with open(path, newline='', encoding='utf-8-sig') as f:
        rows = list(csv.reader(f))
    h = rows[0]; data = [r for r in rows[1:] if any(c.strip() for c in r)]
    for r in data:
        while len(r)<len(h): r.append("")
    return h, data

def usable(v):
    v=v.strip()
    if not v or v.upper().startswith("NOT FOUND"): return False
    return True

def bare_names(cell):
    # split multiple people on comma, strip titles in parens/brackets, lowercase
    out=set()
    for part in cell.split(","):
        p = part.strip()
        # cut at '(' or '['
        p = re.split(r'[\(\[]', p)[0].strip()
        if p and "NOT FOUND" not in p.upper() and len(p)>1:
            out.add(p.lower())
    return out

h_old, old = load("runs/prospects-prestreamline.csv")
h_new, new = load("runs/prospects-latest.csv")
old_idx = {r[2].strip():r for r in old}
new_idx = {r[2].strip():r for r in new}
retained = set(old_idx).intersection(set(new_idx))

# For each retained institution, compare bare-name SETS across all 7 stakeholder cols
total_lost_bare = 0
total_gained_bare = 0
examples_lost = []
examples_gained = []
name_mismatch = []
for n in retained:
    ro = old_idx[n]; rn = new_idx[n]
    old_names=set()
    new_names=set()
    for i in range(7):
        if usable(ro[3+i]): old_names |= bare_names(ro[3+i])
        if usable(rn[3+i]): new_names |= bare_names(rn[3+i])
    lost = old_names - new_names
    gained = new_names - old_names
    total_lost_bare += len(lost)
    total_gained_bare += len(gained)
    if lost: examples_lost.append((n,sorted(lost)))
    if gained: examples_gained.append((n,sorted(gained)))
    if lost or gained: name_mismatch.append(n)

print(f"Retained institutions: {len(retained)}")
print(f"Bare-name losses (real names present old, missing new): {total_lost_bare}")
print(f"Bare-name gains (real names present new, missing old): {total_gained_bare}")
print(f"Institutions with ANY bare-name mismatch: {len(name_mismatch)}")
if examples_lost:
    print("\nSample bare-name LOSSES (would indicate real data loss):")
    for n,l in examples_lost[:15]:
        print(f"  {n}: {l}")
if examples_gained:
    print("\nSample bare-name GAINS (would indicate new enrichment):")
    for n,g in examples_gained[:15]:
        print(f"  {n}: {g}")
print("\n=> If losses=0 and gains=0, streamline preserved all real contact names (only titles/sources stripped).")

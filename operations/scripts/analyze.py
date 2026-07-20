import csv, json, re
from collections import Counter, defaultdict

SRC = 'root-csv.csv'
with open(SRC, encoding='utf-8-sig', newline='') as f:
    raw = f.read()

# Use csv module with proper dialect
f = open(SRC, encoding='utf-8-sig', newline='')
reader = csv.reader(f)
rows = list(reader)
f.close()

header = rows[0]
data = rows[1:]
print("HEADER:", header)
print("RAW DATA ROWS:", len(data))

# Identify phantom Sun Life row (unescaped quote fragment)
phantom_idx = []
clean = []
for i, r in enumerate(data):
    # Phantom: row that is mostly empty / fragmented, typically has very few cols or Sun Life fragment
    name = r[2].strip() if len(r) > 2 else ''
    ncols = len(r)
    # A real row should have name in col C and >=10 cols. Phantom tends to be a fragment.
    is_phantom = False
    if name == '' and ncols < 5:
        is_phantom = True
    # detect Sun Life fragment: a row whose institution name is empty but has trailing fragment text
    if ncols >= 3 and r[2].strip() == '' and any(c.strip() for c in r[:3] if c):
        # leftover fragment
        frag = ' '.join(x.strip() for x in r if x.strip())
        if 'Sun Life' in frag or frag.startswith('"') or (ncols <= 4 and len(frag) < 60):
            is_phantom = True
    if is_phantom:
        phantom_idx.append((i, r))
    else:
        clean.append(r)

print("PHANTOM ROWS:", len(phantom_idx))
for i,r in phantom_idx:
    print("  phantom line", i+2, ":", r)

print("CLEAN (REAL) ROWS:", len(clean))

# Column indices (0-based)
# A=0 Tier, B=1 Segment, C=2 Institution, D=3 CISO, E=4 GRC, F=5 CFO, G=6 CRO, H=7 Compliance, I=8 CIO, J=9 IA
ROLE_COLS = [('CISO',3),('GRC',4),('CFO',5),('CRO',6),('Compliance',7),('CIO',8),('IA',9)]

def is_placeholder(cell):
    c = cell.strip()
    if not c:
        return None  # empty
    # NOT FOUND placeholder
    if c.upper().startswith('NOT FOUND') or c.startswith('NOT FOUND') or 'NOT FOUND' in c.upper()[:20]:
        return 'notfound'
    # CEO misfiled in CISO: cell starts with CEO: or contains "CEO:" pattern / CEO misfiled
    if c.upper().startswith('CEO:') or c.upper().startswith('CEO '):
        return 'ceo_misfiled'
    if re.search(r'\bCEO\b', c) and ('misfiled' in c.lower() or c.upper().startswith('CEO')):
        return 'ceo_misfiled'
    return 'real'

def classify(cell):
    """Returns ('empty', None) | ('notfound', txt) | ('ceo_misfiled', txt) | ('real', txt)"""
    c = cell.strip()
    if not c:
        return ('empty', None)
    cu = c.upper()
    if cu.startswith('NOT FOUND') or 'NOT FOUND' in cu[:25]:
        return ('notfound', c)
    if cu.startswith('CEO:') or cu.startswith('CEO '):
        return ('ceo_misfiled', c)
    return ('real', c)

# Tally
tier = Counter()
seg = Counter()
role_nominal = Counter()   # any non-empty
role_true = Counter()       # 'real' only
role_notfound = Counter()
role_ceo = Counter()
with_at_least_one_real = 0
with_at_least_one_nominal = 0
completely_empty = 0
no_real_contact = 0  # empty OR only notfound/ceo-misfiled
full7_nominal = []
full7_true = []
per_inst = []
true_cell_total = 0
nominal_cell_total = 0
ceo_misfiled_insts = []
notfound_insts = []

for r in clean:
    tier[r[0].strip()] += 1
    seg[r[1].strip()] += 1
    name = r[2].strip()
    inst_roles = {}
    n_real = 0
    n_nominal = 0
    for role, ci in ROLE_COLS:
        cell = r[ci] if ci < len(r) else ''
        kind, txt = classify(cell)
        inst_roles[role] = (kind, txt)
        if kind != 'empty':
            role_nominal[role] += 1
            nominal_cell_total += 1
        if kind == 'real':
            role_true[role] += 1
            true_cell_total += 1
            n_real += 1
        if kind == 'notfound':
            role_notfound[role] += 1
        if kind == 'ceo_misfiled' and role == 'CISO':
            role_ceo[role] += 1
            ceo_misfiled_insts.append(name)
        if kind == 'notfound':
            notfound_insts.append((name, role))
        if kind != 'empty':
            n_nominal += 1
    if n_real >= 1:
        with_at_least_one_real += 1
    if n_nominal >= 1:
        with_at_least_one_nominal += 1
    if n_nominal == 0:
        completely_empty += 1
    if n_real == 0:
        no_real_contact += 1
    if n_nominal == 7:
        full7_nominal.append(name)
    if n_real == 7:
        full7_true.append(name)
    per_inst.append((r[0].strip(), r[1].strip(), name, n_real, n_nominal, inst_roles))

N = len(clean)
possible_cells = N * 7

print("\n=== TOTAL REAL INSTITUTIONS:", N, "===")
print("TIER:", dict(sorted(tier.items())))
print("SEGMENT:", dict(sorted(seg.items(), key=lambda x:-x[1])))

print("\n=== ROLE COMPLETION ===")
print(f"{'Role':12} {'Nom':>5} {'True':>5} {'NF':>4} {'CEOmis':>6} {'Nom%':>6} {'True%':>6}")
for role, ci in ROLE_COLS:
    nom = role_nominal[role]; tru = role_true[role]
    print(f"{role:12} {nom:5} {tru:5} {role_notfound[role]:4} {role_ceo[role]:6} {nom/N*100:5.1f}% {tru/N*100:5.1f}%")

print("\n=== ENRICHMENT RATE ===")
print(f"With >=1 contact (NOMINAL): {with_at_least_one_nominal}/{N} = {with_at_least_one_nominal/N*100:.1f}%")
print(f"With >=1 REAL contact (TRUE): {with_at_least_one_real}/{N} = {with_at_least_one_real/N*100:.1f}%")
print(f"Completely empty: {completely_empty}/{N} = {completely_empty/N*100:.1f}%")
print(f"No real contact (empty+only placeholders): {no_real_contact}/{N} = {no_real_contact/N*100:.1f}%")

print("\n=== CELL FILL ===")
print(f"Nominal cells: {nominal_cell_total}/{possible_cells} = {nominal_cell_total/possible_cells*100:.1f}%")
print(f"TRUE cells: {true_cell_total}/{possible_cells} = {true_cell_total/possible_cells*100:.1f}%")

print("\n=== FULL 7/7 ===")
print(f"Nominal full 7/7: {len(full7_nominal)}")
print(f"TRUE full 7/7: {len(full7_true)}")

print("\n=== CEO MISFILED IN CISO (count):", len(ceo_misfiled_insts), "===")
for n in ceo_misfiled_insts[:40]:
    print("  -", n)

print("\n=== NOT FOUND PLACEHOLDERS (count):", len(notfound_insts), "cells across", len(set(x[0] for x in notfound_insts)), "institutions ===")

# Tier 1 analysis
print("\n=== TIER 1 ANALYSIS ===")
t1 = [p for p in per_inst if p[0] == '1']
print(f"T1 total: {len(t1)}")
t1_with_real = [p for p in t1 if p[3] >= 1]
t1_full_true = [p for p in t1 if p[3] == 7]
t1_full_nominal = [p for p in t1 if p[4] == 7]
print(f"T1 with >=1 real contact: {len(t1_with_real)}")
print(f"T1 TRUE full 7/7: {len(t1_full_true)}")
print(f"T1 NOMINAL full 7/7: {len(t1_full_nominal)}")
print("\nT1 TRUE full 7/7 institutions:")
for p in t1_full_true:
    print("  ✓", p[2])
print("\nT1 detail (name, real_count, nominal_count, missing-real roles):")
for p in sorted(t1, key=lambda x:-x[3]):
    missing_real = [r for r,_ in ROLE_COLS if p[5][r][0] != 'real']
    flag = ''
    if p[5]['CISO'][0] == 'notfound': flag += ' [CISO=NOTFOUND]'
    if p[5]['CISO'][0] == 'ceo_misfiled': flag += ' [CISO=CEO-misfiled]'
    print(f"  {p[3]}/7r {p[4]}/7n  {p[2]}  missing_real={missing_real}{flag}")

# Save machine state for next run
state = {
    "last_check": "2026-07-19T13:25:00Z",
    "git_commit_latest_known": "7c4941f",
    "git_commit_latest_msg": "v5.13: 3/7 cluster resolution - 11 institutions, +10 net roles",
    "git_commit_latest_at": "2026-07-19T12:56:53Z",
    "csv_source": "ROOT prospect-database-7stakeholders.csv (task URL prospects/ still 404)",
    "total": N,
    "raw_rows": len(data),
    "tier": dict(sorted(tier.items())),
    "segment": dict(sorted(seg.items(), key=lambda x:-x[1])),
    "role_pop_nominal": {r: role_nominal[r] for r,_ in ROLE_COLS},
    "role_pop_true": {r: role_true[r] for r,_ in ROLE_COLS},
    "role_notfound": {r: role_notfound[r] for r,_ in ROLE_COLS},
    "role_ceo_misfiled_ciso": role_ceo['CISO'],
    "role_completion_pct_nominal": {r: round(role_nominal[r]/N*100,1) for r,_ in ROLE_COLS},
    "role_completion_pct_true": {r: round(role_true[r]/N*100,1) for r,_ in ROLE_COLS},
    "with_contacts_nominal": with_at_least_one_nominal,
    "with_contacts_true": with_at_least_one_real,
    "empty": completely_empty,
    "no_real_contact": no_real_contact,
    "enrichment_rate_nominal": round(with_at_least_one_nominal/N*100,1),
    "enrichment_rate_true": round(with_at_least_one_real/N*100,1),
    "total_cells_nominal": nominal_cell_total,
    "total_cells_true": true_cell_total,
    "possible_cells": possible_cells,
    "cell_fill_rate_nominal": round(nominal_cell_total/possible_cells*100,1),
    "cell_fill_rate_true": round(true_cell_total/possible_cells*100,1),
    "full_all_nominal": len(full7_nominal),
    "full_all_true": len(full7_true),
    "t1_total": len(t1),
    "t1_with_real": len(t1_with_real),
    "t1_full_nominal": len(t1_full_nominal),
    "t1_full_true": len(t1_full_true),
    "t1_full_names_true": [p[2] for p in t1_full_true],
    "ceo_misfiled_insts": ceo_misfiled_insts,
    "notfound_cell_count": len(notfound_insts),
    "notfound_inst_count": len(set(x[0] for x in notfound_insts)),
}
with open('state_current.json','w') as f:
    json.dump(state, f, indent=2, ensure_ascii=False)
print("\nSaved state_current.json")

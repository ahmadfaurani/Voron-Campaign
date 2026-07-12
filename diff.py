import json

prev = json.load(open("/home/p62operator/.hermes/memories/voron-prospect-monitor.json"))
curr = json.load(open("/home/p62operator/.openclaw/workspace-hoi/vorondrq-rmit-campaign/analysis.json"))

print("=== CORE METRICS: prev -> curr ===")
for k in ["total_prospects","prospects_with_contacts","empty_prospects","enrichment_rate","fully_enriched","total_contact_cells"]:
    p, c = prev.get(k), curr.get(k)
    flag = "  (CHANGED)" if p!=c else ""
    print(f"  {k:28s} {p} -> {c}{flag}")

print("\n=== GIT COMMIT ===")
print(f"  prev: {prev.get('git_commit')}  ({prev.get('git_commit_msg','')})")
print(f"  curr: e0929b6 (origin/main tip, unchanged)")

print("\n=== TIER COUNTS diff ===")
pt, ct = prev['tier_counts'], curr['tier_counts']
for t in sorted(set(pt)|set(ct), key=lambda x:int(x)):
    p,c = pt.get(t,0), ct.get(t,0)
    flag = "  (CHANGED)" if p!=c else ""
    print(f"  Tier {t}: {p} -> {c}{flag}")

print("\n=== SEGMENT COUNTS diff ===")
ps, cs = prev['segment_counts'], curr['segment_counts']
for s in sorted(set(ps)|set(cs)):
    p,c = ps.get(s,0), cs.get(s,0)
    flag = "  (CHANGED)" if p!=c else ""
    if p!=c: print(f"  {s}: {p} -> {c}{flag}")
if all(ps.get(s,0)==cs.get(s,0) for s in set(ps)|set(cs)):
    print("  (no changes)")

print("\n=== STAKEHOLDER POPULATED diff ===")
pk, ck = prev['stakeholder_populated'], curr['stakeholder_populated']
for role in sorted(set(pk)|set(ck)):
    p,c = pk.get(role,0), ck.get(role,0)
    flag = f"  (+{c-p})" if c>p else ("  (DECREASED)" if c<p else "")
    print(f"  {role}: {p} -> {c}{flag}")

print("\n=== ENRICHED INSTITUTIONS diff (contact count per institution) ===")
pe, ce = prev['enriched_institutions'], curr['all_institution_contact_counts']
all_names = set(pe)|set(ce)
new_inst = []
increased = []
decreased = []
for n in all_names:
    p, c = pe.get(n,0), ce.get(n,0)
    if p==0 and c>0: new_inst.append((n,c))
    elif c>p: increased.append((n,p,c))
    elif c<p: decreased.append((n,p,c))
print(f"  New institutions w/ contacts (was 0): {len(new_inst)}")
for n,c in sorted(new_inst, key=lambda x:-x[1]):
    print(f"    + {n}: {c}")
print(f"  Increased contacts: {len(increased)}")
for n,p,c in sorted(increased, key=lambda x:-(x[2]-x[1])):
    print(f"    ~ {n}: {p} -> {c} (+{c-p})")
print(f"  Decreased/removed: {len(decreased)}")
for n,p,c in sorted(decreased, key=lambda x:x[2]-x[1]):
    print(f"    - {n}: {p} -> {c}")

print("\n=== TIER1 BANKS WITH CONTACTS diff ===")
pt1 = set(prev['tier1_banks_with_contacts'])
ct1 = set(curr['tier1_banks_with_contacts'])
print(f"  prev count: {len(pt1)}  curr count: {len(ct1)}")
print(f"  newly contactable: {sorted(ct1-pt1)}")
print(f"  dropped: {sorted(pt1-ct1)}")

print("\n=== SUMMARY ===")
changed = (prev['total_prospects']!=curr['total_prospects'] or
           prev['prospects_with_contacts']!=curr['prospects_with_contacts'] or
           prev['total_contact_cells']!=curr['total_contact_cells'] or
           len(new_inst) or len(increased) or len(decreased) or
           ct1!=pt1)
print("  STATE CHANGED SINCE LAST RUN" if changed else "  NO CHANGES SINCE LAST RUN (identical to prev commit e0929b6)")

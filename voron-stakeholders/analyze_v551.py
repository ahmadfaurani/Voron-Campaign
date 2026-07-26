import csv

path = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.50.csv'
with open(path, encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

cols = ['Chief Information Security Officer','Head of Governance Risk & Compliance','Chief Financial Officer','Chief Risk Officer','Head of Compliance','Chief Information Officer','Head of Internal Audit']

print("Total institutions:", len(rows))
print("Columns:", list(rows[0].keys()))
print()

def is_named(v):
    if not v: return False
    v = v.strip()
    if not v: return False
    low = v.lower()
    if 'not publicly' in low or 'gap:' in low or 'n/a' in low or v.startswith('[') or 'no public' in low:
        return False
    return True

named_by_role = {c:0 for c in cols}
for r in rows:
    for c in cols:
        if is_named(r.get(c,'')):
            named_by_role[c] += 1
print("Named by role:")
for c in cols:
    print(f"  {c}: {named_by_role[c]}/{len(rows)}")

print("\n=== TIER 1 institutions with gaps ===")
tier1_gaps = []
for r in rows:
    tier = r.get('Tier','').strip()
    if tier != 'Tier 1':
        continue
    gaps = [c for c in cols if not is_named(r.get(c,''))]
    if gaps:
        tier1_gaps.append((r.get('Institution_Name',''), gaps, {c:r.get(c,'')[:120] for c in gaps}))
        print(f"  {r.get('Institution_Name','')}: {len(gaps)} gaps")
        for c in gaps:
            print(f"     {c}: {r.get(c,'')[:150]}")

print(f"\nTier 1 with gaps: {len(tier1_gaps)} institutions")

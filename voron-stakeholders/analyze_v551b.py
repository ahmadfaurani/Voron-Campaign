import csv

path = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.50.csv'
with open(path, encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

cols = ['Chief Information Security Officer','Head of Governance Risk & Compliance','Chief Financial Officer','Chief Risk Officer','Head of Compliance','Chief Information Officer','Head of Internal Audit']

# Show sample cell values - a few named and a few gap-looking
print("=== SAMPLE: First 5 institutions, all 7 roles (first 100 chars each) ===")
for r in rows[:5]:
    print(f"\n## {r.get('Tier','')} | {r.get('Institution_Name','')}")
    for c in cols:
        val = r.get(c,'')
        print(f"  {c}: {val[:100]}")

# Count by tier
from collections import Counter
tier_counts = Counter(r.get('Tier','') for r in rows)
print("\n=== Institutions by Tier ===")
for t,c in sorted(tier_counts.items()):
    print(f"  {t}: {c}")

# Find cells that look like gaps across ALL tiers
print("\n=== Cells that look like GAPS (containing 'not' or 'gap' or 'N/A') by tier ===")
gap_by_tier = {}
for r in rows:
    tier = r.get('Tier','').strip()
    for c in cols:
        v = r.get(c,'').strip().lower()
        if 'not public' in v or 'no public' in v or v.startswith('gap') or 'n/a' in v or 'group level' in v or 'not disclosed' in v or 'not listed' in v:
            gap_by_tier.setdefault(tier,[]).append((r.get('Institution_Name',''), c, r.get(c,'')[:80]))

for tier in sorted(gap_by_tier.keys()):
    print(f"\n--- {tier}: {len(gap_by_tier[tier])} gap cells ---")
    for inst, c, val in gap_by_tier[tier][:8]:
        print(f"  {inst} | {c}: {val}")

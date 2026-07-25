import csv
with open('prospect-database-enriched-v5.45.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

roles = ['Chief Information Security Officer','Head of Governance Risk & Compliance',
         'Chief Financial Officer','Chief Risk Officer','Head of Compliance',
         'Chief Information Officer','Head of Internal Audit']

# Sample values for CISO role to see formats
print("=== CISO VALUES SAMPLE (first 30 unique short ones) ===")
seen = set()
for r in rows:
    v = (r.get('Chief Information Security Officer') or '').strip()
    if v and v not in seen:
        seen.add(v)
        if len(v) < 80:
            print(repr(v))
            if len(seen) >= 30:
                break

print()
print("=== HSBC row CISO ===")
for r in rows:
    if 'HSBC' in r['Institution_Name']:
        print(r['Institution_Name'])
        for ro in roles:
            print(f"  {ro}: {repr(r.get(ro,'')[:120])}")
        break

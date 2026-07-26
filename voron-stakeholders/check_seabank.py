import csv

path = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.50.csv'
with open(path, encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

cols = ['Chief Information Security Officer','Head of Governance Risk & Compliance','Chief Financial Officer','Chief Risk Officer','Head of Compliance','Chief Information Officer','Head of Internal Audit']

for r in rows:
    if 'SeaBank' in r.get('Institution_Name','') or 'Sea Bank' in r.get('Institution_Name',''):
        print(f"\n## {r.get('Institution_Name','')} | Tier={r.get('Tier','')} Seg={r.get('Segment','')}")
        for c in cols:
            print(f"  {c}: {r.get(c,'')[:90]}")

#!/usr/bin/env python3
import csv

with open('/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.23.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

roles = ['Chief Information Security Officer','Head of Governance Risk & Compliance','Chief Financial Officer','Chief Risk Officer','Head of Compliance','Chief Information Officer','Head of Internal Audit']
role_short = {'Chief Information Security Officer':'CISO','Head of Governance Risk & Compliance':'GRC','Chief Financial Officer':'CFO','Chief Risk Officer':'CRO','Head of Compliance':'Compliance','Chief Information Officer':'CIO','Head of Internal Audit':'IA'}

for r in rows:
    nm = r['Institution_Name']
    if nm in ('Prudential BSN Takaful Berhad','Soft Space Sdn Bhd','Zurich Life Insurance Malaysia Berhad','Zurich Takaful Malaysia Berhad'):
        print(f"\n========= {nm} | T{r['Tier']} | {r['Segment']} =========")
        for col in roles:
            v = r.get(col,'').strip()
            tag = role_short[col]
            print(f"\n  --- {tag} ---")
            print(f"  {v}")

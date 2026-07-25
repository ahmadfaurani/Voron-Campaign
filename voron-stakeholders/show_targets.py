import csv
with open('prospect-database-enriched-v5.45.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

roles = ['Chief Information Security Officer','Head of Governance Risk & Compliance',
         'Chief Financial Officer','Chief Risk Officer','Head of Compliance',
         'Chief Information Officer','Head of Internal Audit']
short = ['CISO','GRC','CFO','CRO','Comp','CIO','IA']

def st(v):
    v=(v or '').strip().lower()
    if not v or v.startswith('not ') or v.startswith('none') or 'no dedicated' in v[:30] or 'confirmed absence' in v[:25]:
        return '-'
    if 'role exists' in v[:30]:
        return 'E'
    return 'X'

targets = ['Boost Bank','GX Bank','GXBank','KAF Digital','Ryt Bank','SeaBank','AEON Bank',
           'Allianz','AmMetLife','Manulife','Sun Life','Zurich','LPPSA','Tekun','BSN',
           'Prudential BSN Takaful','Tokio Marine','Generali','Chubb','QBE','MCIS','Kurnia',
           'Takaful IKHLAS','Syarikat Takaful','Takaful Am','Great Eastern','Prudential','AIA','Etiqa','Hong Leong Assurance','MPI','AIA']

print(f"{'Row':>4} {'Inst':<55} {'CISO':>4} {'GRC':>3} {'CFO':>3} {'CRO':>3} {'Cmp':>3} {'CIO':>3} {'IA':>3} {'Seg':<18}")
for i,r in enumerate(rows):
    inst=r['Institution_Name']
    if any(t.lower() in inst.lower() for t in targets):
        marks=' '.join(f"{short[j]}:{st(r.get(roles[j],''))}" for j in range(7))
        rown=i+2
        print(f"{rown:>4} {inst[:54]:<55} {marks}  [{r.get('Segment','')}]")

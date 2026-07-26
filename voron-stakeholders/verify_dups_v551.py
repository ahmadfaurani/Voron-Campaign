import csv

path = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.50.csv'
with open(path, encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

cols = ['Chief Information Security Officer','Head of Governance Risk & Compliance','Chief Financial Officer','Chief Risk Officer','Head of Compliance','Chief Information Officer','Head of Internal Audit']

def is_named(v):
    if not v: return False
    v = v.strip()
    if not v: return False
    low = v.lower()
    if 'not found' in low or 'not public' in low or 'no public' in low or v.startswith('[') or 'n/a' in low or 'group level' in low or 'not disclosed' in low or 'not listed' in low:
        return False
    return True

groups = {
    'Ryt Bank': ['Ryt Bank Berhad', 'Ryt Bank Berhad (YTL Digital)'],
    'BigPay': ['BigPay (Capital A)', 'BigPay Malaysia Sdn Bhd'],
    'TNG Digital': ["Touch 'n Go eWallet (TNG Digital Sdn Bhd)", 'TNG Digital Sdn Bhd', 'Touch n Go eWallet Sdn Bhd'],
    'Setel': ['Setel (PETRONAS Dagangan)', 'Setel by PETRONAS Dagangan Berhad'],
    'Tabung Haji': ['Tabung Haji', 'Lembaga Tabung Haji'],
    'Razer Pay': ['Razer Pay (Razer Fintech)', 'Razer Pay Malaysia Sdn Bhd'],
    'Boost': ['Boost (Axiata + RHB)', 'Axiata Digital Services Sdn Bhd (Boost)', 'Boost Bank Berhad'],
}

for gname, names in groups.items():
    print(f"\n========== {gname} ==========")
    for n in names:
        matches = [r for r in rows if r.get('Institution_Name','')==n]
        if not matches:
            print(f"  [MISS] '{n}'")
            continue
        for r in matches:
            nn = sum(1 for c in cols if is_named(r.get(c,'')))
            print(f"  '{n}': Tier={r.get('Tier','')}, Seg={r.get('Segment','')[:30]}, named={nn}/7")
            for c in cols:
                if is_named(r.get(c,'')):
                    print(f"     {c}: {r.get(c,'')[:75]}")

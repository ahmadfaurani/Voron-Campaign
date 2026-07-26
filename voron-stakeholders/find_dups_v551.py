import csv

path = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.50.csv'
with open(path, encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

cols = ['Chief Information Security Officer','Head of Governance Risk & Compliance','Chief Financial Officer','Chief Risk Officer','Head of Compliance','Chief Information Officer','Head of Internal Audit']

def is_named(v):
    if not v: return False
    v = v.strip()
    if not v: return False
    low = v.lower()
    if 'not found' in low or 'not public' in low or 'no public' in low or v.startswith('[') or 'n/a' in low or 'group level' in low or 'not disclosed' in low or 'not listed' in low:
        return False
    return True

# Suspected duplicate pairs (from v5.50 report)
suspects = [
    ('GX Bank Berhad', 'GXBank Berhad'),
    ('Ryt Bank Berhad', 'Ryt Bank Berhad'),
    ('GrabPay (Grab Malaysia)', 'GrabPay Malaysia Sdn Bhd'),
    ('ShopeePay (Monee Malaysia)', 'ShopeePay Malaysia Sdn Bhd'),
    ('WeChat Pay Malaysia (Tencent)', 'WeChat Pay Malaysia Sdn Bhd'),
    ('Money Match Sdn Bhd', 'MoneyMatch Sdn Bhd'),
    ('iPay88 (M) Sdn Bhd', 'iPay88 (Malaysia) Sdn Bhd'),
    ('MARA', 'MARA (Majlis Amanah Rakyat)'),
    ('AEON Bank Berhad', 'AEON Bank (M) Berhad'),
]

# Build index
name_to_rows = {}
for i, r in enumerate(rows):
    n = r.get('Institution_Name','')
    name_to_rows.setdefault(n, []).append(i)

print("=== DUPLICATE PAIR ANALYSIS ===\n")
for a, b in suspects:
    ra = name_to_rows.get(a, [])
    rb = name_to_rows.get(b, [])
    if not ra and not rb:
        print(f"[MISS] neither found: '{a}' / '{b}'")
        continue
    if not ra:
        # try fuzzy
        for n in name_to_rows:
            if a.lower().replace(' ','') in n.lower().replace(' ',''):
                ra = name_to_rows[n]
                print(f"[fuzzy a] '{a}' -> '{n}'")
                break
    if not rb:
        for n in name_to_rows:
            if b.lower().replace(' ','') in n.lower().replace(' ',''):
                rb = name_to_rows[n]
                print(f"[fuzzy b] '{b}' -> '{n}'")
                break
    print(f"\n## '{a}' (rows {ra}) vs '{b}' (rows {rb})")
    if ra and rb:
        r1 = rows[ra[0]]
        r2 = rows[rb[0]]
        n1 = sum(1 for c in cols if is_named(r1.get(c,'')))
        n2 = sum(1 for c in cols if is_named(r2.get(c,'')))
        print(f"  '{a}': Tier={r1.get('Tier','')}, named={n1}/7, Seg={r1.get('Segment','')[:40]}")
        print(f"  '{b}': Tier={r2.get('Tier','')}, named={n2}/7, Seg={r2.get('Segment','')[:40]}")
        for c in cols:
            v1 = r1.get(c,'')[:60]
            v2 = r2.get(c,'')[:60]
            mark = ''
            if is_named(r1.get(c,'')) and not is_named(r2.get(c,'')):
                mark = '  <-- A has name'
            elif not is_named(r1.get(c,'')) and is_named(r2.get(c,'')):
                mark = '  <-- B has name'
            elif is_named(r1.get(c,'')) and is_named(r2.get(c,'')) and r1.get(c,'')!=r2.get(c,''):
                mark = '  <-- BOTH named, DIFFER'
            print(f"  {c[:35]:35} | A:{('Y' if is_named(r1.get(c,'')) else '-')} B:{('Y' if is_named(r2.get(c,'')) else '-')}{mark}")

# Also list all institution names for manual dup spotting
print("\n=== ALL INSTITUTION NAMES (sorted) ===")
names = sorted(name_to_rows.keys())
for n in names:
    cnt = len(name_to_rows[n])
    extra = f"  *** {cnt} rows" if cnt>1 else ""
    print(f"  {n}{extra}")

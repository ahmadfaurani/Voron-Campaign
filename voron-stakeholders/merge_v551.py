import csv, re

src = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.50.csv'
dst = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.51.csv'

with open(src, encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

cols = ['Chief Information Security Officer','Head of Governance Risk & Compliance','Chief Financial Officer','Chief Risk Officer','Head of Compliance','Chief Information Officer','Head of Internal Audit']

def is_named(v):
    if not v: return False
    v = v.strip()
    if not v: return False
    low = v.lower()
    if 'not found' in low or 'not public' in low or 'no public' in low or v.startswith('[') or ' n/a' in low or low.startswith('n/a') or 'group level' in low or 'not disclosed' in low or 'not listed' in low or 'entity defunct' in low or 'entitydefunct' in low:
        return False
    return True

def get_conf(v):
    if not v: return 0
    # pipe format: Name|Title|conf|url
    if '|' in v:
        parts = v.split('|')
        if len(parts) >= 3:
            try:
                return float(parts[2])
            except ValueError:
                pass
    # bracket format: ... [Official: ...] or [ASEAN...] -> conf ~90
    if is_named(v):
        if '[official' in v.lower() or 'official:' in v.lower():
            return 95
        if '[asean' in v.lower() or 'asean' in v.lower():
            return 85
        if 'linkedin' in v.lower():
            return 80
        return 70
    return 0

def best_value(vals):
    """Pick best value from a list of candidate cell values."""
    named = [v for v in vals if v and is_named(v)]
    if named:
        # pick highest confidence
        named.sort(key=lambda v: get_conf(v), reverse=True)
        return named[0]
    # no named - pick the most detailed gap (longest non-empty)
    gaps = [v for v in vals if v and v.strip()]
    if gaps:
        gaps.sort(key=lambda v: len(v), reverse=True)
        return gaps[0]
    return ''

# Merge groups: canonical name -> list of duplicate names to merge in
merge_groups = [
    ('GX Bank Berhad', ['GXBank Berhad']),
    ('Ryt Bank Berhad', ['Ryt Bank Berhad (YTL Digital)']),
    ('GrabPay Malaysia Sdn Bhd', ['GrabPay (Grab Malaysia)']),
    ('ShopeePay Malaysia Sdn Bhd', ['ShopeePay (Monee Malaysia)']),
    ('WeChat Pay Malaysia Sdn Bhd', ['WeChat Pay Malaysia (Tencent)']),
    ('MoneyMatch Sdn Bhd', ['Money Match Sdn Bhd']),
    ('iPay88 (M) Sdn Bhd', ['iPay88 (Malaysia) Sdn Bhd']),
    ('MARA (Majlis Amanah Rakyat)', ['MARA']),
    ('AEON Bank (M) Berhad', ['AEON Bank Berhad']),
    ('TNG Digital Sdn Bhd', ["Touch 'n Go eWallet (TNG Digital Sdn Bhd)", 'Touch n Go eWallet Sdn Bhd']),
    ('Setel by PETRONAS Dagangan Berhad', ['Setel (PETRONAS Dagangan)']),
    ('Lembaga Tabung Haji', ['Tabung Haji']),
    ('BigPay Malaysia Sdn Bhd', ['BigPay (Capital A)']),
    ('Razer Pay Malaysia Sdn Bhd', ['Razer Pay (Razer Fintech)']),
    ('Boost Bank Berhad', ['Boost (Axiata + RHB)']),
]

# Build name->row index
name_to_row = {}
for r in rows:
    name_to_row[r.get('Institution_Name','')] = r

merged_count = 0
merge_log = []
# Process merges
for canonical, dups in merge_groups:
    crow = name_to_row.get(canonical)
    if crow is None:
        # try fuzzy
        for n in name_to_row:
            if n.lower().replace(' ','').replace('(','').replace(')','') == canonical.lower().replace(' ','').replace('(','').replace(')',''):
                crow = name_to_row[n]
                canonical_actual = n
                break
        if crow is None:
            merge_log.append(f"[SKIP] canonical not found: {canonical}")
            continue
    dup_rows = []
    for d in dups:
        drow = name_to_row.get(d)
        if drow is None:
            for n in name_to_row:
                if n.lower().replace(' ','').replace('(','').replace(')','') == d.lower().replace(' ','').replace('(','').replace(')',''):
                    drow = name_to_row[n]
                    break
        if drow is None:
            merge_log.append(f"[SKIP] dup not found: {d} (canonical={canonical})")
            continue
        dup_rows.append(drow)
    if not dup_rows:
        continue
    before_named = sum(1 for c in cols if is_named(crow.get(c,'')))
    # merge each column
    for c in cols:
        vals = [crow.get(c,'')] + [dr.get(c,'') for dr in dup_rows]
        best = best_value(vals)
        crow[c] = best
    after_named = sum(1 for c in cols if is_named(crow.get(c,'')))
    # mark dup rows for removal
    for dr in dup_rows:
        dr['_REMOVE_'] = '1'
    merged_count += len(dup_rows)
    merge_log.append(f"[MERGE] {canonical}: +{len(dup_rows)} dups, named {before_named}->{after_named}/7")

# Fix SeaBank - clear wrongly inherited Ryt Bank data
seabank_err = "NOT FOUND [Jul 2026 DATA FIX: prior values were erroneously inherited from Ryt Bank (rytbank.my). Cleared. SeaBank Malaysia Berhad (Sea Group) is distinct from Ryt Bank; leadership not yet researched from correct source.]"
for r in rows:
    if r.get('Institution_Name','') == 'SeaBank Malaysia Berhad':
        for c in cols:
            r[c] = seabank_err
        merge_log.append("[FIX] SeaBank Malaysia Berhad: cleared wrongly-inherited Ryt Bank data")

# Remove flagged rows
rows_out = [r for r in rows if r.get('_REMOVE_') != '1']
# clean the temp field
for r in rows_out:
    r.pop('_REMOVE_', None)

# Write
with open(dst, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_out)

print("=== MERGE LOG ===")
for line in merge_log:
    print(line)
print(f"\nRows: {len(rows)} -> {len(rows_out)} (removed {len(rows)-len(rows_out)} duplicates)")
print(f"Merged groups: {sum(1 for l in merge_log if l.startswith('[MERGE]'))}")
print(f"Wrote: {dst}")

# Post-merge coverage
total_cells = len(rows_out)*7
named_cells = sum(1 for r in rows_out for c in cols if is_named(r.get(c,'')))
print(f"\nPost-merge coverage: {named_cells}/{total_cells} named ({named_cells*100/total_cells:.1f}%)")

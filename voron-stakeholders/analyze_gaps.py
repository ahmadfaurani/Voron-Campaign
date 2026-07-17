import csv

with open('prospect-database-enriched-v4.8.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
# cols: 0=Tier, 1=Segment, 2=Institution_Name, 3=CISO, 4=GRC, 5=CFO, 6=CRO, 7=Compliance, 8=CIO, 9=IA

total = len(rows) - 1
filled_roles = 0
high_conf = 0
medium_conf = 0
empty_insts = []
low_insts = []  # 1-3 roles
segments = {}

for i, row in enumerate(rows[1:], start=1):
    filled = 0
    for j in range(3, 10):
        val = row[j].strip() if j < len(row) and row[j] else ""
        if val:
            filled += 1
            filled_roles += 1
            if "conf 9" in val or "conf 8" in val:
                high_conf += 1
            elif "conf" in val:
                medium_conf += 1
    seg = row[1] if len(row) > 1 else ""
    segments.setdefault(seg, {"total": 0, "filled": 0, "empty": 0})
    segments[seg]["total"] += 1
    segments[seg]["filled"] += filled
    if filled == 0:
        segments[seg]["empty"] += 1
        empty_insts.append((seg, row[2] if len(row) > 2 else ""))
    elif filled <= 3:
        low_insts.append((filled, seg, row[2] if len(row) > 2 else ""))

print(f"=== OVERALL COVERAGE ===")
print(f"Total institutions: {total}")
print(f"Total target roles: {total*7}")
print(f"Filled roles: {filled_roles} ({filled_roles/(total*7)*100:.1f}%)")
print(f"HIGH conf (80+): {high_conf}")
print(f"MEDIUM conf: {medium_conf}")
print(f"Empty (0/7): {len(empty_insts)}")
print(f"Low (1-3/7): {len(low_insts)}")

print(f"\n=== BY SEGMENT ===")
for seg, d in sorted(segments.items(), key=lambda x: -x[1]['total']):
    cov = d['filled']/(d['total']*7)*100 if d['total'] else 0
    print(f"  {seg}: {d['total']} insts, {d['filled']}/{d['total']*7} roles ({cov:.0f}%), {d['empty']} empty")

print(f"\n=== PRIORITY EMPTY INSTITUTIONS (real institutions, not products) ===")
skip_keywords = ['Card', 'Wallet', 'E-Money', 'Koperasi', 'Pay (', 'OctoPay', 'MAE by', 'Setel', 'ShopeePay (Monee', 'WeChat Pay', 'Razer Pay', 'Alipay', 'Axiata Digital', 'KWSP Investment Division', 'PNB Capital', 'PNB Equity', 'PNB Income', 'JCL Corporation']
for seg, name in empty_insts:
    if any(k in name for k in skip_keywords):
        continue
    print(f"  0/7  {seg}  |  {name}")

print(f"\n=== LOW COVERAGE INSTITUTIONS (1-3/7) ===")
for filled, seg, name in sorted(low_insts):
    print(f"  {filled}/7  {seg}  |  {name}")

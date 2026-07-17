import csv
with open('prospect-database-enriched-v4.8.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    rows = list(reader)
header = rows[0]
targets = ['MSIG', 'AmMetLife', 'QBE Insurance', 'Allianz General', 'Allianz Life', 'AEON Bank', 'KAF Digital', 'SeaBank', 'Zurich Takaful', 'Takaful IKHLAS', 'Prudential BSN', 'MIDF', 'Phillip Securities', 'Mizuho', 'Deutsche Bank']
for i, row in enumerate(rows):
    name = row[2] if len(row) > 2 else ""
    for t in targets:
        if t.lower() in name.lower():
            filled = 0
            vals = []
            for j in range(3, 10):
                v = row[j].strip() if j < len(row) and row[j] else ""
                if v:
                    filled += 1
                    vals.append(f"  [{header[j]}]: {v[:100]}")
            print(f"ROW {i}: {name} | Segment={row[1]} | {filled}/7")
            for v in vals:
                print(v)
            print()

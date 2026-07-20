import csv

csv_path = "/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v4.8.csv"

target_keywords = [
    "QBE", "MSIG", "AmMetLife", "Allianz General", "Allianz Life",
    "AEON Bank", "KAF Digital", "MIDF", "Phillip", "SeaBank", "Ryt Bank",
    "Manulife Insurance", "Manulife Holdings",
    "Zurich Life", "Zurich Takaful", "Zurich General",
    "Prudential BSN", "PruBSN",
]

with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    header = next(reader)
    print("HEADER:", header)
    print()
    
    total_rows = 0
    for i, row in enumerate(reader, start=2):
        total_rows = i
        inst = row[2] if len(row) > 2 else ""
        for target in target_keywords:
            if target.lower() in inst.lower():
                filled = sum(1 for v in row[3:] if v.strip())
                print(f"Row {i}: {inst} | Filled: {filled}/7")
                for j, (col, val) in enumerate(zip(header[3:], row[3:])):
                    status = "+" if val.strip() else "-"
                    if val.strip():
                        print(f"  {status} {col}: {val[:100]}")
                    else:
                        print(f"  {status} {col}: (empty)")
                print()
                break

print(f"Total rows: {total_rows}")

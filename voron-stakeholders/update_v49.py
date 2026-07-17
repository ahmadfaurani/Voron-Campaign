"""
VoronDRQ Enrichment Update v4.9
- Adds QBE Insurance GRC role from official annual report
- Updates SeaBank Malaysia note (rebranded to Ryt Bank)
- Updates Manulife Insurance with CEO confirmation from official board page
"""
import csv
import shutil
from datetime import datetime

src = "/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v4.8.csv"
dst = "/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v4.9.csv"

# Copy the source file
shutil.copy2(src, dst)

# Read all rows
with open(dst, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

print(f"Header: {header}")
print(f"Total rows: {len(rows)}")

# Find column indices
# Columns: Tier, Segment, Institution_Name, CISO, GRC, CFO, CRO, Compliance, CIO, IA
CISO_IDX = 3
GRC_IDX = 4
CFO_IDX = 5
CRO_IDX = 6
COMP_IDX = 7
CIO_IDX = 8
IA_IDX = 9

updates_made = 0

for i, row in enumerate(rows):
    inst = row[2] if len(row) > 2 else ""
    
    # 1. QBE Insurance (Malaysia) - Add GRC entry
    if "QBE Insurance (Malaysia)" in inst and not row[GRC_IDX].strip():
        row[GRC_IDX] = "Jeyasakthi Ratnasingam (Head of Risk & Compliance for Asia, since Nov 2024, Intl Diploma in GRC) [Official: QBE Annual Report 2024, conf 90]"
        print(f"  UPDATED Row {i+2}: {inst} -> Added GRC: Jeyasakthi Ratnasingam")
        updates_made += 1
    
    # 2. SeaBank Malaysia - Update CISO note with rebranding info
    if inst.strip() == "SeaBank Malaysia Berhad":
        row[CISO_IDX] = "Entity rebranded to Ryt Bank Berhad (YTL Digital Capital + Sea Limited JV, licensed Dec 2024). CEO: Melvin Ooi (Ryt Bank). Full leadership data in Ryt Bank rows (166/167): CFO Wilson Soon, CRO Yeoh Xin Yi, Compliance Muhammad Nasir Bin Hassan, CIO Nic Ngoo. [Source: alphasoutheastasia.com, rytbank.my]"
        print(f"  UPDATED Row {i+2}: {inst} -> Updated note with Ryt Bank rebranding info")
        updates_made += 1
    
    # 3. Manulife Insurance Berhad - Update Compliance with CEO confirmation
    if inst.strip() == "Manulife Insurance Berhad" and "Senthil Woon" in row[COMP_IDX]:
        row[COMP_IDX] = "Senthil Woon (Chief Compliance Officer) [RocketReach, conf 50]; CEO: Vibha Hamsi Coburn (confirmed [Official: manulife.com.my board page, conf 95]); Board Risk Cmte Chair: Arthur Jay Belfer; Audit Cmte Chair: Vijayam Nadarajah [Official: manulife.com.my]"
        print(f"  UPDATED Row {i+2}: {inst} -> Enhanced Compliance entry with CEO confirmation")
        updates_made += 1

print(f"\nTotal updates: {updates_made}")

# Write back
with open(dst, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)
    writer.writerows(rows)

print(f"\nWritten to: {dst}")

# Verify
with open(dst, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

# Count filled roles
total_filled = 0
total_roles = 0
for row in rows:
    for val in row[3:]:
        total_roles += 1
        if val.strip():
            total_filled += 1

print(f"Verification: {total_filled}/{total_roles} roles filled ({total_filled/total_roles*100:.1f}%)")
print(f"Total institutions: {len(rows)}")

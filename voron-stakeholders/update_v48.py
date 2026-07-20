import csv
import shutil
from datetime import datetime

# Read the current CSV
with open('prospect-database-enriched-v4.7.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
print(f"Header: {header}")
print(f"Total rows: {len(rows)}")

# Define updates: {row_index: {col_index: new_value}}
# Columns: 0=Tier, 1=Segment, 2=Institution_Name, 3=CISO, 4=Head of GRC, 5=CFO, 6=CRO, 7=Head of Compliance, 8=CIO, 9=Head of IA

updates = {}

# Row 33 - Berjaya Sompo Insurance Berhad (update source annotations)
updates[33] = {
    5: "Rina Aprila Afianty (Chief Financial Officer) [Official: berjayasompo.com.my/leadership-team, conf 95]",
    7: "Tricia Mallika Appaduray (Chief Compliance and Legal Officer) [Official: berjayasompo.com.my/leadership-team, conf 95]",
}

# Row 57 - FWD Insurance Berhad (update source annotations, fix Anita Menon title)
updates[57] = {
    4: "Anita Menon (Acting Head of Risk, oversees governance) [Official: fwd.com.my/about-us/ins/meet-our-team, conf 80]",
    5: "Yeoh Eng Hun (Chief Financial Officer) [Official: fwd.com.my/about-us/ins/meet-our-team, conf 95]",
    6: "Anita Menon (Acting Head of Risk) [Official: fwd.com.my/about-us/ins/meet-our-team, conf 95]",
    9: "Cheryl Lim (Head of Internal Audit) [Official: fwd.com.my, conf 75 - not on current leadership page]",
}

# Row 69 - HSBC Amanah Takaful / FWD Takaful (update source annotations)
updates[69] = {
    5: "Muhammad Afiq bin Hamzah (Acting Chief Financial Officer) [Official: fwd.com.my/about-us/tkfl/meet-our-team, conf 95]",
    7: "Lim Weng Leong (Head of Compliance) [Official: fwd.com.my/about-us/tkfl/meet-our-team, conf 95]",
}

# Row 128 - Manulife Insurance Berhad (FIX GARBLED DATA)
updates[128] = {
    3: "",
    4: "",
    5: "",
    6: "",
    7: "Senthil Woon (Chief Compliance Officer) [RocketReach, conf 50]; Board Risk Cmte Chair: Arthur Jay Belfer [Official: manulife.com.my]",
    8: "",
    9: "",
}

# Row 129 - Manulife Takaful Malaysia Berhad (FIX GARBLED DATA)
updates[129] = {
    3: "",
    4: "",
}

# Row 154 - PruBSN Takaful (update source annotation for CFO)
updates[154] = {
    5: "Kelvin Wong (Chief Financial Officer) [Official: prubsn.com.my/en/about-us/about-prubsn/our-leaders, conf 95]",
}

# Row 190 - Tokio Marine Life Insurance Malaysia Bhd (FIX: CISO column had CEO data)
updates[190] = {
    3: "",
    5: "Tham Kok Yoke (Chief Financial Officer) [Official: tokiomarine.com/my/en/life/about-us/our-board-of-directors-and-management-team.html, conf 95]",
}

# Apply updates
changes = 0
for row_idx, col_updates in updates.items():
    row_name = rows[row_idx][2]
    print(f"\nUpdating Row {row_idx}: {row_name}")
    for col_idx, new_val in col_updates.items():
        old_val = rows[row_idx][col_idx][:80] if rows[row_idx][col_idx] else "(empty)"
        if new_val != rows[row_idx][col_idx]:
            rows[row_idx][col_idx] = new_val
            changes += 1
            if new_val:
                print(f"  [{header[col_idx]}]: -> {new_val[:80]}")
            else:
                print(f"  [{header[col_idx]}]: CLEARED (was: {old_val[:60]})")

print(f"\nTotal field changes: {changes}")

# Write v4.8
output_file = 'prospect-database-enriched-v4.8.csv'
with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"\nWritten: {output_file}")

# Compute coverage stats
total_institutions = len(rows) - 1
total_roles = total_institutions * 7
filled_roles = 0
high_conf = 0
medium_conf = 0

for row in rows[1:]:
    for j in range(3, 10):
        val = row[j].strip() if row[j] else ""
        if val:
            filled_roles += 1
            if "conf 9" in val or "conf 8" in val:
                high_conf += 1
            elif "conf" in val:
                medium_conf += 1

print(f"\n=== Coverage Stats ===")
print(f"Total institutions: {total_institutions}")
print(f"Total target roles: {total_roles}")
print(f"Filled roles: {filled_roles}")
print(f"Coverage: {filled_roles}/{total_roles} = {filled_roles/total_roles*100:.1f}%")
print(f"HIGH conf (80+): {high_conf}")
print(f"MEDIUM conf (60-79): {medium_conf}")

# Check the specific institutions we updated
print(f"\n=== Updated Institution Coverage ===")
for row_idx in sorted(updates.keys()):
    row = rows[row_idx]
    filled = sum(1 for j in range(3, 10) if row[j].strip())
    print(f"  Row {row_idx} {row[2]}: {filled}/7")

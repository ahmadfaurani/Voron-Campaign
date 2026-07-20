#!/usr/bin/env python3
"""Update prospect database to v3.6 with new stakeholder data."""
import csv
import shutil
from datetime import datetime

DATE = "2026-07-14"

# Source file
SRC = "/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v3.5.csv"
DST = "/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v3.6.csv"

# Copy source to destination
shutil.copy2(SRC, DST)

# Define updates: institution_name -> {column_name: value}
updates = {
    # 1. PayNet (Payments Network Malaysia Sdn Bhd) - 2/7
    "PayNet (PayNet Malaysia Sdn Bhd)": {
        "Chief Financial Officer": "Tan Wei Tze|Chief Financial Officer|95|https://www.paynet.my/about-us/corporate-profile/leadership.html|PayNet CFO",
        "Chief Information Officer": "Teh Lip Guan|Chief Technology Officer|95|https://www.paynet.my/about-us/corporate-profile/leadership.html|PayNet CTO (maps to CIO/CTO role)",
    },
    
    # 2. TNG Digital Sdn Bhd - 5/7 (CFO, CIO, CRO, Compliance, GRC)
    "TNG Digital Sdn Bhd": {
        "Chief Financial Officer": "Lai Mee Fong|Chief Financial Officer|95|https://www.touchngo.com.my/about-us/leadership/|TNG Digital CFO",
        "Chief Information Officer": "Desmond Chin Ye Foong|Chief Technology Officer|95|https://www.touchngo.com.my/about-us/leadership/|TNG Digital CTO (maps to CIO/CTO role)",
        "Chief Risk Officer": "Dunstan Gerald Maurice|Chief Risk, Compliance & Governance Officer|95|https://www.touchngo.com.my/about-us/leadership/|Combined CRO/Compliance/GRC role",
        "Head of Compliance": "Dunstan Gerald Maurice|Chief Risk, Compliance & Governance Officer|95|https://www.touchngo.com.my/about-us/leadership/|Combined CRO/Compliance/GRC role",
        "Head of Governance Risk & Compliance": "Dunstan Gerald Maurice|Chief Risk, Compliance & Governance Officer|95|https://www.touchngo.com.my/about-us/leadership/|Combined CRO/Compliance/GRC role",
    },
    "Touch 'n Go eWallet (TNG Digital Sdn Bhd)": {
        "Chief Financial Officer": "Lai Mee Fong|Chief Financial Officer|95|https://www.touchngo.com.my/about-us/leadership/|TNG Digital CFO",
        "Chief Information Officer": "Desmond Chin Ye Foong|Chief Technology Officer|95|https://www.touchngo.com.my/about-us/leadership/|TNG Digital CTO (maps to CIO/CTO role)",
        "Chief Risk Officer": "Dunstan Gerald Maurice|Chief Risk, Compliance & Governance Officer|95|https://www.touchngo.com.my/about-us/leadership/|Combined CRO/Compliance/GRC role",
        "Head of Compliance": "Dunstan Gerald Maurice|Chief Risk, Compliance & Governance Officer|95|https://www.touchngo.com.my/about-us/leadership/|Combined CRO/Compliance/GRC role",
        "Head of Governance Risk & Compliance": "Dunstan Gerald Maurice|Chief Risk, Compliance & Governance Officer|95|https://www.touchngo.com.my/about-us/leadership/|Combined CRO/Compliance/GRC role",
    },
    "Touch n Go eWallet Sdn Bhd": {
        "Chief Financial Officer": "Lai Mee Fong|Chief Financial Officer|95|https://www.touchngo.com.my/about-us/leadership/|TNG Digital CFO",
        "Chief Information Officer": "Desmond Chin Ye Foong|Chief Technology Officer|95|https://www.touchngo.com.my/about-us/leadership/|TNG Digital CTO (maps to CIO/CTO role)",
        "Chief Risk Officer": "Dunstan Gerald Maurice|Chief Risk, Compliance & Governance Officer|95|https://www.touchngo.com.my/about-us/leadership/|Combined CRO/Compliance/GRC role",
        "Head of Compliance": "Dunstan Gerald Maurice|Chief Risk, Compliance & Governance Officer|95|https://www.touchngo.com.my/about-us/leadership/|Combined CRO/Compliance/GRC role",
        "Head of Governance Risk & Compliance": "Dunstan Gerald Maurice|Chief Risk, Compliance & Governance Officer|95|https://www.touchngo.com.my/about-us/leadership/|Combined CRO/Compliance/GRC role",
    },
    
    # 3. Ryt Bank (YTL Digital Bank Berhad) - 4/7
    "Ryt Bank Berhad": {
        "Chief Financial Officer": "Wilson Soon|Chief Financial Officer (Acting CEO)|95|https://www.rytbank.my/about-us/|Ryt Bank CFO; acting CEO after Melvin Ooi departure",
        "Chief Risk Officer": "Yeoh Xin Yi|Chief Risk Officer|95|https://www.rytbank.my/about-us/|Ryt Bank CRO",
        "Head of Compliance": "Muhammad Nasir Bin Hassan|Chief Compliance Officer|95|https://www.rytbank.my/about-us/|Ryt Bank Chief Compliance Officer",
        "Chief Information Officer": "Nic Ngoo|Chief Technology Officer|95|https://www.rytbank.my/about-us/|Ryt Bank CTO (maps to CIO/CTO role)",
    },
    "Ryt Bank Berhad (YTL Digital)": {
        "Chief Financial Officer": "Wilson Soon|Chief Financial Officer (Acting CEO)|95|https://www.rytbank.my/about-us/|Ryt Bank CFO; acting CEO after Melvin Ooi departure",
        "Chief Risk Officer": "Yeoh Xin Yi|Chief Risk Officer|95|https://www.rytbank.my/about-us/|Ryt Bank CRO",
        "Head of Compliance": "Muhammad Nasir Bin Hassan|Chief Compliance Officer|95|https://www.rytbank.my/about-us/|Ryt Bank Chief Compliance Officer",
        "Chief Information Officer": "Nic Ngoo|Chief Technology Officer|95|https://www.rytbank.my/about-us/|Ryt Bank CTO (maps to CIO/CTO role)",
    },
    
    # 4. Boost Bank Berhad - 4/7
    "Boost Bank Berhad": {
        "Chief Financial Officer": "Steven Lim|Chief Financial Officer|95|https://myboostbank.co/our-leadership-boost-bank|Boost Bank CFO",
        "Chief Information Officer": "Shankar Krishnan|Chief Technology Officer|95|https://myboostbank.co/our-leadership-boost-bank|Boost Bank CTO (maps to CIO/CTO role)",
        "Head of Compliance": "Dr Mohanamerry Vedamanikam|Chief Compliance Officer|95|https://myboostbank.co/our-leadership-boost-bank|Boost Bank Chief Compliance Officer",
        "Chief Risk Officer": "Puteri Syurga|Chief Risk Officer|95|https://myboostbank.co/our-leadership-boost-bank|Boost Bank CRO",
    },
    
    # 5. iPay88 - 1/7 (CISO from RocketReach)
    "iPay88 (M) Sdn Bhd": {
        "Chief Information Security Officer": "Alex Wah|Head of IT Cum CISO|70|https://rocketreach.co/ipay88-management_b5e52ecdf42e67ac|iPay88 CISO (RocketReach source - MEDIUM confidence)",
    },
    "iPay88 (Malaysia) Sdn Bhd": {
        "Chief Information Security Officer": "Alex Wah|Head of IT Cum CISO|70|https://rocketreach.co/ipay88-management_b5e52ecdf42e67ac|iPay88 CISO (RocketReach source - MEDIUM confidence)",
    },
}

# Read the CSV
rows = []
with open(DST, 'r', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        rows.append(row)

# Apply updates
updated_count = 0
for row in rows:
    name = row.get('Institution_Name', '').strip()
    if name in updates:
        for col, val in updates[name].items():
            if col in row and not row[col].strip():
                row[col] = val
                updated_count += 1
                print(f"  Updated: {name} -> {col} = {val.split('|')[0]}")
            elif col in row and row[col].strip():
                print(f"  SKIP (already filled): {name} -> {col}")

# Write updated CSV
with open(DST, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"\nTotal updates: {updated_count}")
print(f"Output: {DST}")

# Calculate new stats
total_filled = 0
total_roles = 0
filled_institutions = 0
empty_institutions = 0
seven_seven = 0

for row in rows:
    roles = [row.get('Chief Information Security Officer','').strip(), 
             row.get('Head of Governance Risk & Compliance','').strip(), 
             row.get('Chief Financial Officer','').strip(), 
             row.get('Chief Risk Officer','').strip(), 
             row.get('Head of Compliance','').strip(), 
             row.get('Chief Information Officer','').strip(), 
             row.get('Head of Internal Audit','').strip()]
    fc = sum(1 for r in roles if r)
    total_filled += fc
    total_roles += 7
    if fc > 0:
        filled_institutions += 1
    else:
        empty_institutions += 1
    if fc == 7:
        seven_seven += 1

print(f"\n=== Updated Statistics ===")
print(f"Total institutions: {len(rows)}")
print(f"Filled institutions: {filled_institutions}")
print(f"Empty institutions: {empty_institutions}")
print(f"Total roles filled: {total_filled}/{total_roles} ({total_filled/total_roles*100:.1f}%)")
print(f"Institutions at 7/7: {seven_seven}")

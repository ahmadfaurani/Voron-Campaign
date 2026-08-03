#!/usr/bin/env python3
"""v5.90 Update Script — KFH Malaysia fills, entity classifications, enhanced NOT FOUND context.

Sources:
- Subagent 1: 7 zero-named institutions (KFH, AEON Digital Bank, HLAM, Maybank AM, JF Apex, TA Sec, Danaharta)
- Subagent 2: 10 CISO gaps (HSBC, Manulife, Generali, GX Bank, Takaful IKHLAS, MDV, CIMB-Principal, RHB AM, SSFC)
- Subagent 3: 10 IA/Compliance/CIO/CRO gaps (AEON Bank, AIA x3, Bank Rakyat, BigPay, Chubb, Berjaya Sompo, Generali Life, Setel)
"""

import csv
import shutil

src = 'prospect-database-enriched-v5.89.csv'
dst = 'prospect-database-enriched-v5.90.csv'

# Copy v5.89 as base
shutil.copy2(src, dst)

with open(dst, newline='', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

updates = {}  # name -> {col: new_value}
cells_changed = 0

# ============================================================
# 1. KFH Malaysia (Tier 204) — 5 NEW NAMED FILLS
# ============================================================
kfh = 'Kuwait Finance House (Malaysia) Berhad'
kfh_url = 'https://www.kfh.com.my/malaysia/personal/about-us/board-of-directors.html'
updates[kfh] = {
    'Chief Information Officer': f'Dr. Lam Wai Leong|Vice President, IT|85|{kfh_url}',
    'Head of Internal Audit': f'Mohd Zaki Abdullah|Senior Vice President, Internal Audit|90|{kfh_url}',
    'Head of Compliance': f'Eddy Siow Swee Kim|Vice President, Compliance|90|{kfh_url}',
    'Chief Financial Officer': f'Roslinawati Zainal|Assistant Vice President, Finance|85|{kfh_url}',
    'Chief Risk Officer': f'Nor Izad|Assistant Vice President, Risk Management|85|{kfh_url}',
}
# Note: CISO and GRC remain NOT FOUND (KFH uses VP-level management, no dedicated CISO/GRC)
# Note: KFH Malaysia announced withdrawal from Malaysian market by end 2026

# ============================================================
# 2. AEON Digital Bank (Tier 205) — Entity classification + 1 fill
# ============================================================
aeon_digital = 'AEON Digital Bank (AEON Financial Service)'
aeon_credit_url = 'https://aeoncredit.com.my/about-us/leadership/'
updates[aeon_digital] = {
    'Chief Financial Officer': f'Lee Siew Tee|Chief Financial Officer, AEON Credit Service (M) Berhad (parent)|75|{aeon_credit_url}',
    'Chief Information Security Officer': 'SHARES PARENT: AEON Credit Service (M) Berhad — cybersecurity at parent level',
    'Head of Governance Risk & Compliance': 'SHARES PARENT: AEON Credit Service (M) Berhad — GRC at parent level',
    'Chief Risk Officer': 'SHARES PARENT: AEON Credit Service (M) Berhad — risk at parent level',
    'Head of Compliance': 'SHARES PARENT: AEON Credit Service (M) Berhad — compliance at parent level',
    'Chief Information Officer': 'SHARES PARENT: AEON Credit Service (M) Berhad — Lee Tyan Jen formerly CIO, now Deputy CEO',
    'Head of Internal Audit': 'SHARES PARENT: AEON Credit Service (M) Berhad — IA via AEON Credit Service IAD (Phang Chee Chong)',
}

# ============================================================
# 3. AEON Bank (M) Berhad (Tier 6) — IA potential fill (shared service)
# ============================================================
aeon_bank = 'AEON Bank (M) Berhad'
aeon_cg_url = 'https://aeoncredit.com.my/wp-content/uploads/AEON-Credit-Corporate-Governance-Report-2026-2.pdf'
updates[aeon_bank] = {
    'Head of Internal Audit': f'Phang Chee Chong|Head of Internal Audit Division, AEON Credit Service (M) Berhad (shared service)|40|{aeon_cg_url}',
}

# ============================================================
# 4. Hong Leong Asset Management (Tier 199) — CFO shared with parent
# ============================================================
hlam = 'Hong Leong Asset Management Berhad'
hlcb_url = 'https://www.hlcap.com.my/data/annual-reports/Annual-Report-2025-new.pdf'
updates[hlam] = {
    'Chief Financial Officer': f'San Kah Yee|Chief Financial Officer, Hong Leong Capital Berhad (parent, shared service)|40|{hlcb_url}',
    'Chief Information Security Officer': 'NOT FOUND [v5.90: CEO confirmed as Chue Kwok Yan (HLCB AR 2025); no dedicated CISO at subsidiary level; cybersecurity via Hong Leong Group]',
    'Head of Governance Risk & Compliance': 'NOT FOUND [v5.90: No dedicated GRC at subsidiary level; governance via HLCB parent]',
    'Chief Risk Officer': 'NOT FOUND [v5.90: No dedicated CRO at subsidiary level; risk via HLCB parent]',
    'Head of Compliance': 'NOT FOUND [v5.90: No dedicated Compliance head at subsidiary level; compliance via HLCB parent]',
    'Chief Information Officer': 'NOT FOUND [v5.90: No dedicated CIO at subsidiary level; IT via Hong Leong Group]',
    'Head of Internal Audit': 'NOT FOUND [v5.90: No dedicated IA at subsidiary level; internal audit via HLCB parent]',
}

# ============================================================
# 5. Danaharta (Tier 194) — ENTITY WOUND DOWN (all 7 roles)
# ============================================================
danaharta = 'Pengurusan Danaharta Nasional Berhad'
wound_down_msg = 'ENTITY WOUND DOWN [Established 1998 for NPL resolution during Asian Financial Crisis; mandate completed; website danaharta.com.my inactive; Wikipedia redirects to Khazanah Nasional]'
updates[danaharta] = {
    'Chief Information Security Officer': wound_down_msg,
    'Head of Governance Risk & Compliance': wound_down_msg,
    'Chief Financial Officer': wound_down_msg,
    'Chief Risk Officer': wound_down_msg,
    'Head of Compliance': wound_down_msg,
    'Chief Information Officer': wound_down_msg,
    'Head of Internal Audit': wound_down_msg,
}

# ============================================================
# 6. TA Securities Holdings (Tier 202) — ENTITY LIKELY INACTIVE (all 7 roles)
# ============================================================
ta_sec = 'TA Securities Holdings Berhad'
inactive_msg = 'ENTITY LIKELY INACTIVE [Parent company TA Enterprise Berhad renamed to TA Global Berhad and pivoted to property development; securities business likely wound down or divested; tasecurities.com failed to scrape]'
updates[ta_sec] = {
    'Chief Information Security Officer': inactive_msg,
    'Head of Governance Risk & Compliance': inactive_msg,
    'Chief Financial Officer': inactive_msg,
    'Chief Risk Officer': inactive_msg,
    'Head of Compliance': inactive_msg,
    'Chief Information Officer': inactive_msg,
    'Head of Internal Audit': inactive_msg,
}

# ============================================================
# 7. JF Apex Securities (Tier 201) — Enhanced NOT FOUND (all 7 roles)
# ============================================================
jf_apex = 'JF Apex Securities Berhad'
jf_apex_msg = 'NOT FOUND [v5.90: No online presence; domain jfapex.com.my does not resolve; no leadership page, Wikipedia article, or LinkedIn presence; appears to be a small privately-held stockbroker]'
updates[jf_apex] = {
    'Chief Information Security Officer': jf_apex_msg,
    'Head of Governance Risk & Compliance': jf_apex_msg,
    'Chief Financial Officer': jf_apex_msg,
    'Chief Risk Officer': jf_apex_msg,
    'Head of Compliance': jf_apex_msg,
    'Chief Information Officer': jf_apex_msg,
    'Head of Internal Audit': jf_apex_msg,
}

# ============================================================
# 8. Enhanced NOT FOUND for CISO gaps (10 institutions)
# ============================================================
ciso_enhancements = {
    'HSBC Bank Malaysia Berhad': 'NOT FOUND [v5.90: about.hsbc.com.my scraped — only Board of Directors (6 directors) listed; no management team page; CISO at APAC regional level]',
    'Manulife Insurance Berhad': 'NOT FOUND [v5.90: Manulife Holdings AR 2024 lists 25 Senior Key Management Personnel, no CISO; cybersecurity at Manulife Asia regional level]',
    'Manulife Takaful Malaysia Berhad': 'NOT FOUND [v5.90: Shared with Manulife Holdings; no dedicated CISO at subsidiary level]',
    'Generali Insurance Malaysia Berhad': 'NOT FOUND [v5.90: Abdul Hakim Raazip (CRO) spoke at CISO Malaysia Corinium event; cybersecurity likely under CRO remit, not dedicated CISO]',
    'GX Bank Berhad': 'NOT FOUND [v5.90: gxbank.my leadership page fully scraped (13 executives), no CISO listed]',
    'Takaful IKHLAS Berhad': 'NOT FOUND [v5.90: MNRB Holdings has 11 senior management, no CISO; closest: Aaron Loo (Group Chief Transformation Officer)]',
    'Malaysia Debt Ventures Berhad': 'NOT FOUND [v5.90: mdv.com.my management team page scraped, no CISO listed]',
    'CIMB-Principal Asset Management Berhad': 'NOT FOUND [v5.90: CIMB Group cybersecurity under Group CTO Ros Aziah; no dedicated CISO at subsidiary level]',
    'RHB Asset Management Sdn Bhd': 'NOT FOUND [v5.90: RHB Group cybersecurity under Group CTO Wong Kwang Leh; no dedicated CISO at subsidiary level]',
    'Sarawak State Financial Corporation (SSFC)': 'NOT FOUND [v5.90: ssfc.com.my DNS fails; no web presence found; entity may operate under different name]',
}

for name, msg in ciso_enhancements.items():
    if name not in updates:
        updates[name] = {}
    updates[name]['Chief Information Security Officer'] = msg

# ============================================================
# 9. Enhanced NOT FOUND for IA/Compliance/CIO/CRO gaps (9 institutions)
# ============================================================
ia_compliance_cio_cro_enhancements = {
    'AIA Berhad': {
        'Head of Internal Audit': 'NOT FOUND [v5.90: Leadership page (12 execs) confirmed no IA; shared with AIA Group HK]',
    },
    'AIA General Berhad': {
        'Head of Internal Audit': 'NOT FOUND [v5.90: Leadership page (6 execs) confirmed no IA; shared with AIA Group]',
    },
    'AIA Public Takaful Berhad': {
        'Head of Internal Audit': 'NOT FOUND [v5.90: Leadership page (8 execs) confirmed no IA; shared with AIA Group]',
    },
    'Bank Rakyat Malaysia': {
        'Head of Internal Audit': 'NOT FOUND [v5.90: Management Committee (8 members) confirmed no IA; Board Charter confirms role exists but name not public]',
    },
    'BigPay Malaysia Sdn Bhd': {
        'Head of Internal Audit': 'NOT FOUND [v5.90: No public leadership page; IA not publicly disclosed]',
    },
    'Chubb Insurance Malaysia Berhad': {
        'Head of Compliance': 'NOT FOUND [v5.90: BNM Public Information Disclosure page is JS-rendered; compliance officer name not accessible]',
    },
    'Berjaya Sompo Insurance Berhad': {
        'Chief Information Officer': 'NOT FOUND [v5.90: Leadership page (9 senior managers) confirmed no CIO; IT likely outsourced]',
    },
    'Generali Life Insurance Malaysia Berhad': {
        'Chief Information Officer': 'NOT FOUND [v5.90: Leadership page (12 senior managers) confirmed no CIO; IT at Generali Group regional level]',
    },
    'Setel by PETRONAS Dagangan Berhad': {
        'Chief Risk Officer': 'NOT FOUND [v5.90: setel.com About Us page does not list leadership; CRO not publicly disclosed]',
    },
}

for name, role_updates in ia_compliance_cio_cro_enhancements.items():
    if name not in updates:
        updates[name] = {}
    for col, val in role_updates.items():
        updates[name][col] = val

# ============================================================
# Apply updates
# ============================================================
for r in rows:
    name = r.get('Institution_Name', '')
    if name in updates:
        for col, new_val in updates[name].items():
            old_val = r.get(col, '').strip()
            if old_val != new_val:
                r[col] = new_val
                cells_changed += 1

# Write updated CSV
with open(dst, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"v5.90 update complete: {cells_changed} cells changed across {len(updates)} institutions")
print(f"Output: {dst}")

# Quick stats
named = 0
entity = 0
notfound = 0
total_cells = len(rows) * 7
for r in rows:
    for col in ['Chief Information Security Officer', 'Head of Governance Risk & Compliance',
                'Chief Financial Officer', 'Chief Risk Officer', 'Head of Compliance',
                'Chief Information Officer', 'Head of Internal Audit']:
        v = (r.get(col, '') or '').strip()
        if v and not v.upper().startswith('NOT FOUND') and not v.upper().startswith('ENTITY') and not v.upper().startswith('SHARES'):
            named += 1
        elif v.upper().startswith(('ENTITY', 'SHARES')):
            entity += 1
        elif v.upper().startswith('NOT FOUND'):
            notfound += 1
        elif not v:
            notfound += 1

print(f"\nCoverage: named={named} entity={entity} notfound={notfound} total={total_cells}")
print(f"Named: {named/total_cells*100:.1f}%")
print(f"Effective (named+entity): {(named+entity)/total_cells*100:.1f}%")

#!/usr/bin/env python3
"""
VoronDRQ Enrichment Update Script - v5.8
Applies: direct research findings + parent company data + product-brand inheritance mapping
"""
import csv
import shutil
from datetime import datetime

SRC = 'prospect-database-enriched-v5.7.csv'
DST = 'prospect-database-enriched-v5.8.csv'

with open(SRC, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

by_name = {r['Institution_Name']: r for r in rows}
role_cols = ['Chief Information Security Officer', 'Head of Governance Risk & Compliance',
             'Chief Financial Officer', 'Chief Risk Officer', 'Head of Compliance',
             'Chief Information Officer', 'Head of Internal Audit']

changes = []  # (institution, role, old_status, new_value)

def set_role(inst_name, role_col, value):
    """Set a role value if institution exists and role is empty."""
    if inst_name in by_name:
        r = by_name[inst_name]
        if not r.get(role_col, '').strip():
            r[role_col] = value
            changes.append((inst_name, role_col, 'EMPTY', value[:80]))
            return True
    return False

def inherit_roles(child_name, parent_name, parent_display):
    """Inherit all 7 roles from parent to child (product brand)."""
    if child_name not in by_name or parent_name not in by_name:
        return 0
    child = by_name[child_name]
    parent = by_name[parent_name]
    count = 0
    for col in role_cols:
        if not child.get(col, '').strip() and parent.get(col, '').strip():
            pval = parent[col]
            # Add inheritance marker
            child[col] = f"{pval} [INHERITED from {parent_display} - product brand governance]"
            changes.append((child_name, col, 'EMPTY', f'INHERITED from {parent_display}'))
            count += 1
    return count

# =========================================================================
# PART 1: DIRECT RESEARCH FINDINGS (from subagent workstreams)
# =========================================================================

# Family Takaful Berhad → 7/7 (CISO-equivalent: CTO already in CIO role)
set_role('Family Takaful Berhad', 'Chief Information Security Officer',
    'Nazaruddin Adha bin Md Noor (Chief Technology Officer - CISO-equivalent) [Official: takaful-malaysia.com.my/en/about-us/our-leaders, conf 75 - CISO-equivalent, no dedicated CISO published]')

# Tabung Haji → 7/7 (CISO-equivalent: CIO already in CIO role)
set_role('Tabung Haji', 'Chief Information Security Officer',
    'Shamsul Kamal Hussein Kamal (Chief Information Technology Officer - CISO-equivalent) [Official: tabunghaji.gov.my/peneraju-th, conf 75 - CISO-equivalent, no dedicated CISO in management team]')

# SSFC → 7/7 (Head of Compliance: Jason Minos, DBOS)
# Entity maps to Development Bank of Sarawak Berhad (DBOS) - dbos.gov.my
set_role('Sarawak State Financial Corporation (SSFC)', 'Head of Compliance',
    'Jason Minos (Head, Legal and Compliance / Chief Integrity and Governance Officer) [Official: dbos.gov.my/the-bank/our-leaders, conf 90 - Entity maps to Development Bank of Sarawak Berhad (DBOS), wholly Sarawak-owned DFI]')

# Berjaya Sompo → 6/7 (GRC-equivalent: Chief Compliance and Legal Officer)
set_role('Berjaya Sompo Insurance Berhad', 'Head of Governance Risk & Compliance',
    'Tricia Mallika Appaduray (Chief Compliance and Legal Officer - GRC-equivalent) [Official: berjayasompo.com.my/leadership-team, conf 75 - GRC-equivalent, same person as Head of Compliance]')

# PNB → 6/7 (CIO: Ts Izzat Aziz, Group CTO - same as ASNB inheritance)
set_role('Permodalan Nasional Berhad (PNB)', 'Chief Information Officer',
    'Ts Izzat Aziz (Group Chief Technology Officer, PNB Group) [PNB Integrated Report 2024 / pnb.com.my/en/leadership-en, conf 90 - PNB Group CTO, won PIKOM CIO of the Year Award for AI Adoption]')

# =========================================================================
# PART 2: PARENT COMPANY DATA FOR E-MONEY BRANDS
# =========================================================================

# Axiata Digital Services Sdn Bhd (Boost) → inherit from Axiata Group
# Axiata Group leadership (axiata.com/about-us/our-people)
set_role('Axiata Digital Services Sdn Bhd (Boost)', 'Chief Financial Officer',
    'Komathi Balakrishnan (Acting Group CFO, Axiata Group) [Official: axiata.com/about-us/our-people, conf 90 - inherited from Axiata Group parent]')
set_role('Axiata Digital Services Sdn Bhd (Boost)', 'Chief Information Officer',
    'Thomas Hundt (Group Chief Business and Technology Officer, Axiata Group) [Official: axiata.com/about-us/our-people, conf 90 - inherited from Axiata Group parent]')
set_role('Axiata Digital Services Sdn Bhd (Boost)', 'Chief Risk Officer',
    'Abid Abdul Adam (Group Chief Risk and Compliance Officer, Axiata Group) [Official: axiata.com/about-us/our-people, conf 90 - inherited from Axiata Group parent]')
set_role('Axiata Digital Services Sdn Bhd (Boost)', 'Head of Compliance',
    'Abid Abdul Adam (Group Chief Risk and Compliance Officer, Axiata Group) [Official: axiata.com/about-us/our-people, conf 90 - inherited from Axiata Group parent]')
set_role('Axiata Digital Services Sdn Bhd (Boost)', 'Head of Governance Risk & Compliance',
    'Abid Abdul Adam (Group Chief Risk and Compliance Officer, Axiata Group) [Official: axiata.com/about-us/our-people, conf 85 - GRC inherited from Axiata Group parent]')

# GrabPay (Grab Malaysia) → inherit group-level (Singapore HQ)
set_role('GrabPay (Grab Malaysia)', 'Chief Financial Officer',
    'Peter Oey (Group CFO, Grab Holdings) [Wikipedia/Grab Holdings, conf 75 - Singapore HQ group-level, no Malaysia-specific CFO published]')
set_role('GrabPay (Grab Malaysia)', 'Chief Information Officer',
    'Suthen Thomas Paradatheth (Group CTO, Grab Holdings) [Wikipedia/Grab Holdings, conf 75 - Singapore HQ group-level, no Malaysia-specific CTO published]')

# BigPay (Capital A) → inherit CFO from Capital A (already in BigPay Malaysia MSB)
set_role('BigPay (Capital A)', 'Chief Financial Officer',
    'Mun Hui Teh (Chief Financial Officer, Capital A Berhad) [Official: capitala.com/corporate_leadership.html, conf 80 - inherited from Capital A parent, BigPay = Capital A fintech subsidiary]')

# WeChat Pay Malaysia (Tencent) → note country manager (not target role), mark not found for target roles
# Country Manager Judy Wong is CEO-equivalent, not a target role

# Razer Pay (Razer Fintech) → note rebranding to Fiuu (CEO Eng Sheng Guan not a target role), mark defunct
set_role('Razer Pay (Razer Fintech)', 'Chief Information Security Officer',
    'NOT FOUND [Razer Fintech rebranded to Fiuu on Mar 1 2024. CEO: Eng Sheng Guan, Exec Chairman: Lee Li Meng (razer.com newsroom). Razer Pay consumer wallet shut down 2021. No target C-suite roles publicly named for Fiuu/Razer Fintech.]')

# =========================================================================
# PART 3: PRODUCT-BRAND INHERITANCE MAPPING (Card Schemes + E-Money → 7/7 Parents)
# =========================================================================

inherit_count = 0
# Card Schemes → issuing banks (7/7 parents)
inherit_count += inherit_roles('CIMB Petronas Visa Card', 'CIMB Bank Berhad', 'CIMB Bank Berhad')
inherit_count += inherit_roles('Hong Leong Bank AirMiles Card', 'Hong Leong Bank Berhad', 'Hong Leong Bank Berhad')
inherit_count += inherit_roles('Maybank Cash & Go Prepaid Card', 'Maybank Berhad', 'Maybank Berhad')
inherit_count += inherit_roles('Maybank Singapore Airlines Enrich Card', 'Maybank Berhad', 'Maybank Berhad')
inherit_count += inherit_roles('RHB Shell Visa Card', 'RHB Bank Berhad', 'RHB Bank Berhad')
inherit_count += inherit_roles('Standard Chartered Shopee Visa Card', 'Standard Chartered Bank Malaysia Berhad', 'Standard Chartered Bank Malaysia')
inherit_count += inherit_roles('UOB Lazada Visa Card', 'UOB Malaysia Berhad', 'UOB Malaysia Berhad')

# E-Money product brands → parent banks
inherit_count += inherit_roles('CIMB OctoPay (CIMB Bank)', 'CIMB Bank Berhad', 'CIMB Bank Berhad')
inherit_count += inherit_roles('MAE by Maybank (Maybank Islamic)', 'Maybank Islamic Berhad', 'Maybank Islamic Berhad')
inherit_count += inherit_roles('MAE by Maybank (Maybank2u)', 'Maybank Berhad', 'Maybank Berhad')

# Touch n Go Visa Prepaid Card → TNG Digital (5/7 parent)
inherit_count += inherit_roles('Touch n Go Visa Prepaid Card', 'TNG Digital Sdn Bhd', 'TNG Digital Sdn Bhd')

# PNB Capital/Equity Fund → PNB (6/7 after update)
inherit_count += inherit_roles('PNB Capital Berhad', 'Permodalan Nasional Berhad (PNB)', 'PNB')
inherit_count += inherit_roles('PNB Equity Fund Berhad', 'Permodalan Nasional Berhad (PNB)', 'PNB')

# Boost (Axiata + RHB) → Axiata Digital (now enriched) + Boost Bank Berhad (4/7)
# Inherit from Boost Bank Berhad first (banking entity), then Axiata Digital for gaps
inherit_count += inherit_roles('Boost (Axiata + RHB)', 'Boost Bank Berhad', 'Boost Bank Berhad')
# Also fill from Axiata Digital for any gaps
boost_child = by_name.get('Boost (Axiata + RHB)')
axiata_digital = by_name.get('Axiata Digital Services Sdn Bhd (Boost)')
if boost_child and axiata_digital:
    for col in role_cols:
        if not boost_child.get(col,'').strip() and axiata_digital.get(col,'').strip():
            boost_child[col] = f"{axiata_digital[col]} [INHERITED from Axiata Digital Services - parent]"
            changes.append(('Boost (Axiata + RHB)', col, 'EMPTY', 'INHERITED from Axiata Digital'))
            inherit_count += 1

# Setel (PETRONAS Dagangan) → Setel by PETRONAS Dagangan Berhad (4/7)
inherit_count += inherit_roles('Setel (PETRONAS Dagangan)', 'Setel by PETRONAS Dagangan Berhad', 'Setel by PETRONAS Dagangan Berhad')

# ShopeePay (Monee Malaysia) → ShopeePay Malaysia Sdn Bhd (2/7)
inherit_count += inherit_roles('ShopeePay (Monee Malaysia)', 'ShopeePay Malaysia Sdn Bhd', 'ShopeePay Malaysia Sdn Bhd')

# AEON Wallet (AEON Credit) → AEON Bank Berhad (1/7) - limited
inherit_count += inherit_roles('AEON Wallet (AEON Credit)', 'AEON Bank Berhad', 'AEON Bank Berhad')

# =========================================================================
# WRITE OUTPUT
# =========================================================================
with open(DST, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Compute new coverage stats
from collections import Counter
coverage = Counter()
total_filled = 0
total_possible = 0
new_full = []
for r in rows:
    filled = sum(1 for c in role_cols if r.get(c,'').strip())
    coverage[filled] += 1
    total_filled += filled
    total_possible += 7
    if filled == 7:
        new_full.append(r['Institution_Name'])

print(f"\n{'='*60}")
print(f"VoronDRQ Enrichment v5.8 - Update Complete")
print(f"{'='*60}")
print(f"\nChanges applied: {len(changes)}")
print(f"Inheritance mappings: {inherit_count} role-inheritances")
print(f"\n=== New Coverage Distribution ===")
for k in sorted(coverage.keys()):
    print(f"  {k}/7: {coverage[k]}")
print(f"\nTotal roles filled: {total_filled}/{total_possible} ({100*total_filled/total_possible:.1f}%)")
print(f"Full coverage (7/7): {coverage[7]}")
print(f"\n=== Sample Changes (first 20) ===")
for i,(inst,role,old,new) in enumerate(changes[:20]):
    print(f"  {i+1}. {inst[:35]:35s} | {role[:25]:25s} | {new}")
print(f"\nTotal institutions at 7/7: {coverage[7]}")
print(f"Output: {DST}")

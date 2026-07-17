#!/usr/bin/env python3
"""VoronDRQ Stakeholder Database Update - v5.1
Updates master CSV with findings from 3 parallel research subagents.
Classification: TLP:AMBER
"""
import csv
import os
import shutil
from datetime import datetime

MASTER_CSV = "/home/p62operator/.openclaw/workspace-hoi/vorondrq-rmit-campaign/prospect-database-7stakeholders.csv"
ENRICHED_CSV = "/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.1.csv"
MASTER_COPY = "/home/p62operator/.openclaw/workspace-hoi/vorondrq-rmit-campaign/prospect-database-7stakeholders.csv"

ROLE_FIELDS = [
    'Chief Information Security Officer',
    'Head of Governance Risk & Compliance',
    'Chief Financial Officer',
    'Chief Risk Officer',
    'Head of Compliance',
    'Chief Information Officer',
    'Head of Internal Audit'
]

# Define updates: {institution_name: {role_field: new_value}}
# Only update cells that are currently empty, or where we have better official data
UPDATES = {
    # === Development Finance Institutions (Group 1) ===
    "Agrobank Malaysia": {
        'Chief Information Officer': 'Nolan Jeffrey A/L Abdul Hai (Group Chief Information Technology Officer) [Official: agrobank.com.my/home/corporate-info/senior-leadership/, conf 95]'
    },
    "Bank Pembangunan Malaysia Berhad (BPMB)": {
        'Chief Information Officer': 'Hairil Izwar Abd Rahman (Group Chief Digital & Technology Officer) [Official: bpmb.com.my/about-us/leadership, conf 95]',
        'Chief Financial Officer': 'Hee Wei Jean (Group Chief Financial Officer) [Official: bpmb.com.my/about-us/leadership, conf 95]',
        'Chief Risk Officer': 'Mohammad Azam Ahmad (Group Chief Risk Officer) [Official: bpmb.com.my/about-us/leadership, conf 95]',
        'Head of Compliance': 'Rohayati Talha (Group Chief Compliance Officer) [Official: bpmb.com.my/about-us/leadership, conf 95]',
        'Head of Internal Audit': 'Hasrul Farid Hasnan (Group Chief Internal Auditor) [Official: bpmb.com.my/about-us/leadership, conf 95]'
    },
    "EXIM Bank Malaysia": {
        'Chief Information Officer': 'Hairil Izwar Abd Rahman (Group Chief Digital & Technology Officer, BPMB Group post-merger May 2025) [Official: bpmb.com.my, conf 90]'
    },
    "SME Bank Berhad": {
        'Chief Information Officer': 'Hairil Izwar Abd Rahman (Group Chief Digital & Technology Officer, BPMB Group post-merger May 2025) [Official: bpmb.com.my, conf 90]'
    },
    "PUNB": {
        'Head of Governance Risk & Compliance': 'Mohd Sulaiman Khazali (Head, Internal Audit & Risk Management) [Official: punb.com.my/our-organization, conf 90]'
    },
    
    # === Insurance & Takaful (Group 2) ===
    "Great Eastern Life Assurance (Malaysia) Berhad": {
        'Chief Information Officer': 'Vincent Chin Kok Lean (Division Head, Information Technology) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Chief Financial Officer': 'Loke Chang Yueh (CFO) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Chief Risk Officer': 'Teo Chun Seng (CRO) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Head of Compliance': 'Helen Quat Li Huang (Head of Compliance) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Head of Internal Audit': 'Audra Chung Kit Li (Head of Internal Audit) [Malaysian Insurance Directory 2025/2026, conf 90]'
    },
    "Great Eastern General Insurance (Malaysia) Berhad": {
        'Chief Financial Officer': 'Cheng Chuen Chee (CFO) [Malaysian Insurance Directory 2025/2026, conf 90]'
    },
    "Hong Leong Assurance Berhad": {
        'Chief Information Officer': 'Low Tek Chee (Chief Technology Officer) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Head of Compliance': 'Lee Noushi (Head of Compliance) [Malaysian Insurance Directory 2025/2026, conf 90]'
    },
    "Liberty General Insurance Berhad": {
        'Chief Information Officer': 'Ganesan Vaithilingam (Chief Information Officer) [Malaysian Insurance Directory 2025/2026, conf 90]'
    },
    "AIA General Berhad": {
        'Chief Information Officer': 'Yee Theen Gee (Associate Director, Technology & Operations) [Official: aia.com.my, conf 90]'
    },
    "Tokio Marine Life Insurance Malaysia Bhd": {
        'Chief Information Officer': 'Nicholas Tan Chin Yau (Chief Information Officer) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Chief Risk Officer': 'Andrew Ngou Chee Mun (Chief Risk Officer) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Head of Compliance': 'Loh Chee Hoong (Head of Compliance) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Head of Internal Audit': 'Wong Kah Keong (Head of Internal Audit) [Malaysian Insurance Directory 2025/2026, conf 90]'
    },
    "Manulife Insurance Berhad": {
        'Chief Risk Officer': 'Mohd Naim Mohd Arsad (Chief Risk Officer) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Chief Information Officer': 'Bernard Sia (Chief Information Officer) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Head of Compliance': 'Senthil Woon Wai Keong (Head of Compliance) [Malaysian Insurance Directory 2025/2026, conf 90]'
    },
    "MCIS Insurance Berhad": {
        'Chief Risk Officer': 'Nurliana binti Mat Lazim (Chief Risk Officer) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Head of Compliance': 'Norlin Fatima Albakri (Head of Compliance) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Head of Internal Audit': 'Noor Hayati binti Abu Yaziz (Head of Internal Audit) [Malaysian Insurance Directory 2025/2026, conf 90]'
    },
    "Chubb Insurance Malaysia Berhad": {
        'Chief Risk Officer': 'Ng Khai Yan (Chief Risk Officer) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Head of Internal Audit': 'Chong Keh Bin (Head of Internal Audit) [Malaysian Insurance Directory 2025/2026, conf 90]'
    },
    "MSIG Insurance (Malaysia) Bhd": {
        'Chief Information Officer': 'Chin Jee Gwan (EVP - Information Technology, Digital, Bancassurance & Branding) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Chief Risk Officer': 'Kelvin Hii Chee Yun (Chief Risk Officer) [Malaysian Insurance Directory 2025/2026, conf 90]'
    },
    "Berjaya Sompo Insurance Berhad": {
        'Chief Information Security Officer': 'Mohamad Azman bin Soaed (Senior Manager - Information Security) [Malaysian Insurance Directory 2025/2026, conf 70]',
        'Chief Risk Officer': 'Samson Liew Zyun Fung (Head of Risk Management) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Head of Compliance': 'Tricia Mallika Appaduray (Head of Compliance) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Head of Internal Audit': 'Kesavan Raj A/L Krishnan (Head of Internal Audit) [Malaysian Insurance Directory 2025/2026, conf 90]'
    },
    "Takaful IKHLAS Berhad": {
        'Chief Information Officer': 'Lee Kok Seong (Senior VP & Chief Information Officer) [Malaysian Insurance Directory 2025/2026, conf 90]'
    },
    "Family Takaful Berhad": {
        'Chief Risk Officer': 'Shizal Fisham Ramli (Chief Risk Officer) [Malaysian Insurance Directory 2025/2026, conf 85 - note: same name appears at Takaful Malaysia GRC; cross-entity role]'
    },
    "Prudential BSN Takaful Berhad": {
        'Chief Risk Officer': 'Anita Menon (Chief Risk Officer) [Malaysian Insurance Directory 2025/2026, conf 85 - note: also listed at FWD as Acting Head of Risk; may indicate job change]',
        'Chief Financial Officer': 'Kelvin Wong (CFO) [Malaysian Insurance Directory 2025/2026, conf 90]'
    },
    "Prudential Assurance Malaysia Berhad": {
        'Chief Financial Officer': 'Ankur Bassi (CFO) [Malaysian Insurance Directory 2025/2026, conf 90]',
        'Head of Compliance': 'Krishnakumar Ramasubramaniam (Head of Compliance/Risk/Legal) [Malaysian Insurance Directory 2025/2026, conf 85 - covers compliance + risk functions]'
    },
    "Generali Insurance Malaysia Berhad": {
        'Head of Internal Audit': 'Vivian Ho (Chief Internal Auditor) [Malaysian Insurance Directory 2025/2026, conf 90]'
    },
    
    # === Banks, Investment Banks, GLC-Linked (Group 3) ===
    "Kenanga Investment Bank Berhad": {
        'Chief Information Officer': 'Low Jia Yee (Chief Technology Officer) [Official: kenanga.com.my/who-we-are/our-people/company/kenanga-investment-bank-berhad, conf 95]'
    },
    "MIDF Amanah Investment Bank Berhad": {
        'Head of Compliance': 'Meor Ibrahim Othman (SVP/Head, Group Compliance) [Official: midf.com.my/key-management, conf 90]',
        'Head of Internal Audit': 'Zanariah Daud (SVP/Head, Group Control Assurance Services) [Official: midf.com.my/key-management, conf 90]'
    },
    "PayNet (PayNet Malaysia Sdn Bhd)": {
        'Chief Financial Officer': 'Tan Wei Tze (Chief Financial Officer) [Official: paynet.my/about-us/corporate-profile/leadership.html, conf 95]',
        'Chief Information Officer': 'Teh Lip Guan (Chief Technology Officer) [Official: paynet.my/about-us/corporate-profile/leadership.html, conf 95]'
    },
    "Maybank Investment Bank Berhad": {
        'Chief Information Officer': 'Adrian Tan Kai Thern (Head, Information Technology) [Official: maybank2u.com.my/Investment-bank/en/about-us/our-leadership/senior-management.page, conf 95]'
    },
    "Khazanah Nasional Berhad": {
        'Chief Information Officer': 'Dr Farid Mohamed Sani (Head, Digitalisation - closest to IT CIO role) [Official: khazanah.com.my/responsible-stewardship/leadership/investment-management, conf 60]'
    },
}

def update_csv():
    """Update the master CSV with new findings."""
    with open(MASTER_CSV, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    
    updated_count = 0
    new_cells = 0
    updated_institutions = []
    
    for row in rows:
        inst = row.get('Institution_Name', '').strip()
        if inst in UPDATES:
            updates = UPDATES[inst]
            for role_field, new_value in updates.items():
                current = row.get(role_field, '').strip()
                if not current:
                    # Empty cell - fill it
                    row[role_field] = new_value
                    new_cells += 1
                    updated_institutions.append((inst, role_field, "NEW"))
                else:
                    # Cell has data - only update if new data is from a better source
                    # Check if new data has higher confidence or is from official source
                    if 'Official' in new_value and 'Official' not in current and 'conf 95' in new_value:
                        row[role_field] = new_value
                        new_cells += 1
                        updated_institutions.append((inst, role_field, "UPGRADED"))
                    elif 'Official' in new_value and 'Official' not in current and 'conf 90' in new_value:
                        row[role_field] = new_value
                        new_cells += 1
                        updated_institutions.append((inst, role_field, "UPGRADED"))
    
    # Write updated master CSV
    with open(MASTER_CSV, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    # Also write enriched CSV copy
    with open(ENRICHED_CSV, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    return new_cells, updated_institutions, rows

def compute_stats(rows):
    """Compute coverage statistics."""
    total_insts = len(rows)
    total_roles_possible = total_insts * 7
    total_roles_found = 0
    full_coverage = 0
    six_seven = 0
    five_seven = 0
    below_five = 0
    
    for r in rows:
        filled = sum(1 for f in ROLE_FIELDS if r.get(f, '').strip())
        total_roles_found += filled
        if filled == 7:
            full_coverage += 1
        elif filled == 6:
            six_seven += 1
        elif filled == 5:
            five_seven += 1
        elif filled < 5:
            below_five += 1
    
    return {
        'total_insts': total_insts,
        'total_roles_possible': total_roles_possible,
        'total_roles_found': total_roles_found,
        'coverage_pct': round(total_roles_found / total_roles_possible * 100, 1),
        'full_coverage': full_coverage,
        'six_seven': six_seven,
        'five_seven': five_seven,
        'below_five': below_five
    }

if __name__ == '__main__':
    print("VoronDRQ Stakeholder Database Update - v5.1")
    print("=" * 60)
    
    # Backup
    backup_path = MASTER_CSV.replace('.csv', '.bak-v5.0.csv')
    shutil.copy2(MASTER_CSV, backup_path)
    print(f"Backup created: {backup_path}")
    
    new_cells, updates_log, rows = update_csv()
    
    stats = compute_stats(rows)
    
    print(f"\nNew/Updated cells: {new_cells}")
    print(f"Institutions updated: {len(set(u[0] for u in updates_log))}")
    print()
    for inst, role, action in updates_log:
        print(f"  [{action}] {inst[:50]} -> {role[:40]}")
    
    print(f"\n=== Coverage Statistics (v5.1) ===")
    print(f"Total Institutions: {stats['total_insts']}")
    print(f"Total Roles Found: {stats['total_roles_found']}/{stats['total_roles_possible']}")
    print(f"Coverage: {stats['coverage_pct']}%")
    print(f"Full Coverage (7/7): {stats['full_coverage']}")
    print(f"6/7 Coverage: {stats['six_seven']}")
    print(f"5/7 Coverage: {stats['five_seven']}")
    print(f"<5/7 Coverage: {stats['below_five']}")
    
    print(f"\nUpdated CSV: {MASTER_CSV}")
    print(f"Enriched CSV: {ENRICHED_CSV}")

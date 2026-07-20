#!/usr/bin/env python3
"""
VoronDRQ Enrichment v5.17 Update Script
- Allianz family IA fills + CFO/CIO upgrades (IAR 2024 + CG Report 2024 via Wayback Machine)
- FWD Takaful confirmation (no change)
- Zurich Takaful IA fill (AR 2025 board-level)
- Mizuho IA fill (board-level) + CRO/Compliance NOT FOUND documented
- PruBSN CRO stale downgrade (Anita Menon → NOT FOUND)
- ICBC CRO reclassification (board-level → NOT FOUND) + Compliance downgrade
- MIIB entity non-existent confirmation (6 empty → ENTITY NON-EXISTENT)
"""
import csv
import shutil
import os
from datetime import datetime

MASTER_PATH = "/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv"
ENRICHED_DIR = "/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders"
VORON_CAMPIGN = "/home/p62operator/.openclaw/workspace-hoi/Voron-Campaign"

VERSION = "v5.17"
NEW_ENRICHED = os.path.join(ENRICHED_DIR, f"prospect-database-enriched-{VERSION}.csv")

# Role columns
ROLE_COLS = [
    'Chief Information Security Officer',
    'Head of Governance Risk & Compliance',
    'Chief Financial Officer',
    'Chief Risk Officer',
    'Head of Compliance',
    'Chief Information Officer',
    'Head of Internal Audit'
]

# === UPDATE DATA ===
# Format: { institution_name_substring: { role_col: new_value } }
UPDATES = {
    # 1. Allianz General Insurance Company (Malaysia) Berhad
    "Allianz General Insurance Company (Malaysia) Berhad": {
        'Chief Financial Officer': 'Chin Xiao Wei (CFO Allianz General) [Official: Allianz Malaysia IAR 2024 p.110 via Wayback Machine, conf 95 — upgraded from 90]',
        'Chief Information Officer': 'David Brandl (Chief Information Technology Officer, Group) [Official: Allianz Malaysia IAR 2024 p.111 via Wayback Machine, conf 90 — upgraded from 70. Group CIO covering AMB, Allianz General, Allianz Life]',
        'Head of Internal Audit': 'Narayana Samy Naidu Renugopal (Group Head of Internal Audit Department) [Official: Allianz Malaysia CG Report 2024 via Wayback Machine, conf 88. Group-level IA covering all AMB subsidiaries. Named in CG Report key management personnel.]',
        'Chief Information Security Officer': 'NOT FOUND [CISO not in 16-member Senior Management Team Profile (IAR 2024 p.107-115) or CG Report 2024 (104pp). CG Report mentions "IT Security Officer" only generically p.134. Sources: IAR 2024 + CG Report 2024 via Wayback Machine, conf 35]',
        'Head of Governance Risk & Compliance': 'NOT FOUND [No "Head of GRC" in IAR 2024 16-member Senior Management Team or CG Report 2024. "Governance and Control Committee" mentioned generically p.132 but no named head. Sources: IAR 2024 + CG Report 2024 via Wayback Machine, conf 35]',
        'Chief Risk Officer': 'NOT FOUND [No current CRO in IAR 2024 16-member Senior Management Team or CG Report 2024. Charles Ong Eng Chow (CEO of Allianz Life) was CRO 2005-2010 (historical only). Sources: IAR 2024 + CG Report 2024, conf 35]',
        'Head of Compliance': 'NOT FOUND [Compliance function mentioned generically in IAR 2024 (pp.132, 158) and CG Report 2024 but no named Head of Compliance in 16-member senior management team. Sources: IAR 2024 + CG Report 2024, conf 35]',
    },
    # 2. Allianz Life Insurance Malaysia Berhad
    "Allianz Life Insurance Malaysia Berhad": {
        'Chief Financial Officer': 'Giulio Slavich (CFO AMB & Allianz Life) [Official: Allianz Malaysia IAR 2024 p.110 + CG Report 2024 via Wayback Machine, conf 95 — upgraded from 90. CFO of both AMB holding and Allianz Life]',
        'Chief Information Officer': 'David Brandl (Chief Information Technology Officer, Group) [Official: Allianz Malaysia IAR 2024 p.111 via Wayback Machine, conf 90 — upgraded from 70. Group CIO covering Allianz Life]',
        'Head of Internal Audit': 'Narayana Samy Naidu Renugopal (Group Head of Internal Audit Department) [Official: Allianz Malaysia CG Report 2024 via Wayback Machine, conf 88. Group-level IA covering Allianz Life.]',
        'Chief Information Security Officer': 'NOT FOUND [CISO not in IAR 2024 16-member Senior Management Team or CG Report 2024. Sources: IAR 2024 + CG Report 2024 via Wayback Machine, conf 35]',
        'Head of Governance Risk & Compliance': 'NOT FOUND [No Head of GRC named in IAR 2024 or CG Report 2024. Sources: IAR 2024 + CG Report 2024, conf 35]',
        'Chief Risk Officer': 'NOT FOUND [No current CRO. Charles Ong Eng Chow was CRO 2005-2010, now CEO. Sources: IAR 2024 + CG Report 2024, conf 35]',
        'Head of Compliance': 'NOT FOUND [Compliance function mentioned generically, no named head. Sources: IAR 2024 + CG Report 2024, conf 35]',
    },
    # 3. Allianz Takaful Berhad
    "Allianz Takaful Berhad": {
        'Chief Financial Officer': 'Chin Xiao Wei (CFO) [SimplyWallSt lists "Xiao Chin" = Chin Xiao Wei. IAR 2024 confirms CFO of Allianz General but Takaful NOT mentioned in IAR. Group CFO may cover Takaful but unconfirmed. Source: SimplyWallSt + IAR 2024 cross-ref, conf 70]',
        'Chief Information Officer': 'David Brandl (Chief Information Technology Officer, Group) [Official: Allianz Malaysia IAR 2024 p.111 via Wayback Machine, conf 80 — upgraded from 70. Group CIO likely covers Takaful but IAR 2024 does not mention Takaful]',
        'Head of Internal Audit': 'Narayana Samy Naidu Renugopal (Group Head of Internal Audit Department) [Official: Allianz Malaysia CG Report 2024 via Wayback Machine, conf 78. Group-level IA likely covers Takaful but IAR 2024 does not mention Takaful]',
        'Chief Information Security Officer': 'NOT FOUND [IAR 2024 does NOT mention Allianz Takaful Berhad at all (report covers AMB, Allianz General, Allianz Life only). No separate Allianz Takaful management disclosure found. Sources: IAR 2024 + CG Report 2024, conf 35]',
        'Head of Governance Risk & Compliance': 'NOT FOUND [IAR 2024 does not mention Allianz Takaful. Sources: IAR 2024 + CG Report 2024, conf 35]',
        'Chief Risk Officer': 'NOT FOUND [IAR 2024 does not mention Allianz Takaful. Sources: IAR 2024 + CG Report 2024, conf 35]',
        'Head of Compliance': 'NOT FOUND [IAR 2024 does not mention Allianz Takaful. Sources: IAR 2024 + CG Report 2024, conf 35]',
    },
    # 4. FWD Takaful Berhad (formerly HSBC Amanah Takaful) — confirmation only
    "HSBC Amanah Takaful (Malaysia) Berhad": {
        'Chief Financial Officer': 'Muhammad Afiq bin Hamzah (Acting Chief Financial Officer) [Official: fwd.com.my/about-us/tkfl/meet-our-team, conf 95 — confirmed. Title is "Acting CFO"]',
        'Head of Compliance': 'Lim Weng Leong (Head of Compliance) [Official: fwd.com.my/about-us/tkfl/meet-our-team, conf 95 — confirmed. 1 of 6 executive management team members]',
        'Chief Information Security Officer': 'NOT FOUND [CISO not on official 6-executive team page (fwd.com.my). 6 execs: CEO, Acting CFO, Chief Partnership Distribution Officer, Head of Agency, Head of Compliance, Head of Shariah. Sources: fwd.com.my, conf 35]',
        'Head of Governance Risk & Compliance': 'NOT FOUND [No Head of GRC on official team page. Sources: fwd.com.my, conf 35]',
        'Chief Risk Officer': 'NOT FOUND [No CRO on official team page. Risk Committee TOR PDF linked but no named CRO. Sources: fwd.com.my, conf 35]',
        'Chief Information Officer': 'NOT FOUND [No CIO/CTO on official team page. Sources: fwd.com.my, conf 35]',
        'Head of Internal Audit': 'NOT FOUND [No Head of IA on official team page. Audit Committee TOR PDF linked but no named CAE. Sources: fwd.com.my, conf 35]',
    },
    # 5. Zurich Life Insurance Malaysia Berhad — NOT FOUND documentation upgrade
    "Zurich Life Insurance Malaysia Berhad": {
        'Head of Internal Audit': 'Onn Kien Hoe (Chairman of Audit Committee) [Official: Zurich Life Insurance Malaysia Berhad AR 2025, conf 85 — board-level oversight, not executive CAE]',
        'Chief Information Security Officer': 'NOT FOUND [AR 2025 PDF (146pp, signed financial statements) only names board directors. No senior management disclosed. Sources: zurich.com.my AR 2025, conf 35]',
        'Head of Governance Risk & Compliance': 'NOT FOUND [AR 2025 does not name GRC head. Sources: zurich.com.my AR 2025, conf 35]',
        'Chief Financial Officer': 'NOT FOUND [AR 2025 financial statements signed by directors only; no CFO named. Sources: zurich.com.my AR 2025, conf 35]',
        'Chief Risk Officer': 'NOT FOUND [Board Risk Mgmt & Sustainability Committee chaired by Donald Joshua Jaganathan (board-level). Executive CRO not disclosed. Sources: zurich.com.my AR 2025, conf 35]',
        'Head of Compliance': 'NOT FOUND [AR 2025 does not name compliance head. Sources: zurich.com.my AR 2025, conf 35]',
        'Chief Information Officer': 'NOT FOUND [AR 2025 does not name CIO. Sources: zurich.com.my AR 2025, conf 35]',
    },
    # 6. Zurich Takaful Malaysia Berhad — NEW IA fill + NOT FOUND documentation
    "Zurich Takaful Malaysia Berhad": {
        'Head of Internal Audit': 'Jan Yoke Lan (Chairperson of Audit Committee) [Official: Zurich Takaful Malaysia Berhad AR 2025, conf 80 — board-level oversight, not executive CAE. Chief Internal Auditor management position referenced but not named in AR 2025.]',
        'Chief Information Security Officer': 'NOT FOUND [AR 2025 PDF (148pp) only names board directors. CEO is Nur Fatihah Mustafa. CISO not named. Sources: zurich.com.my AR 2025, conf 35]',
        'Head of Governance Risk & Compliance': 'NOT FOUND [AR 2025 does not name GRC head. Sources: zurich.com.my AR 2025, conf 35]',
        'Chief Financial Officer': 'NOT FOUND [AR 2025 does not name CFO. Sources: zurich.com.my AR 2025, conf 35]',
        'Chief Risk Officer': 'NOT FOUND [Datuk Dr. Hafsah binti Hashim is Chairperson of Risk Mgmt & Sustainability Committee (board-level). Executive CRO not named. Sources: zurich.com.my AR 2025, conf 35]',
        'Head of Compliance': 'NOT FOUND [AR 2025 does not name compliance head. Sources: zurich.com.my AR 2025, conf 35]',
        'Chief Information Officer': 'NOT FOUND [AR 2025 does not name CIO. Sources: zurich.com.my AR 2025, conf 35]',
    },
    # 7. Mizuho Bank (Malaysia) Berhad — NEW IA fill + CRO/Compliance NOT FOUND documented
    "Mizuho Bank (Malaysia) Berhad": {
        'Head of Internal Audit': 'Lim Kim Seng (Chairman of Board Audit Committee) [Official: Mizuho MY Profile of Directors PDF + Board & Board Committees Composition PDF, conf 80 — board-level oversight. Chief Internal Auditor (CIA) management position referenced in Audited FS but explicitly not named. Lim Kim Seng is qualified CA (ICAS), ex-Group Chief Internal Auditor of Hong Leong Bank (retired 2014).]',
        'Chief Risk Officer': 'NOT FOUND [Audited FS FYE Mar 2025 (146pp) explicitly references "Chief Risk Officer (CRO)" position but does NOT name the individual. Abdul Khalil bin Abdul Hamid is Chairman of Board Risk Management Committee (board-level, not executive CRO). Sources: Mizuho MY Audited FS, Pillar 3 Disclosure, Profile of Directors, conf 40]',
        'Head of Compliance': 'NOT FOUND [Audited FS FYE Mar 2025 explicitly references "Chief Compliance Officer (CCO)" position but does NOT name the individual. Mr. Akichika Tsuboi listed as "Complaint Unit" contact on mizuhogroup.com (not Head of Compliance). Sources: Mizuho MY Audited FS, Pillar 3 Disclosure, conf 40]',
        # CISO, GRC, CIO already have NOT FOUND entries — keep them
    },
    # 8. Prudential BSN Takaful Berhad — CRO stale downgrade
    "Prudential BSN Takaful Berhad": {
        'Chief Financial Officer': 'Kelvin Wong (Chief Financial Officer) [Official: prubsn.com.my/en/about-us/about-prubsn/our-leaders, conf 95 — confirmed on official ExCo page as of Jul 2026]',
        'Chief Risk Officer': 'NOT FOUND [STALE: Anita Menon was previously listed as CRO (conf 85) but is NOT on current PruBSN ExCo as of Jul 2026 scrape. 2025 Audited FS confirms "Chief Risk Officer (CRO) / Chief Compliance Officer" role exists but does NOT disclose the name. Anita Menon may have departed. Sources: prubsn.com.my ExCo page, 2025 Audited FS, theorg.com (unverified), conf 30]',
        'Chief Information Security Officer': 'NOT FOUND [CISO not mentioned in official ExCo (8 members), 2025 Audited FS, or Board Charter. 2025 FS mentions "Head of Technology Risk" but not CISO. Sources: prubsn.com.my, 2025 Audited FS, conf 35]',
        'Head of Governance Risk & Compliance': 'NOT FOUND [GRC role not mentioned in ExCo, 2025 Audited FS, or Board Charter. Sources: prubsn.com.my, 2025 Audited FS, conf 35]',
        'Head of Compliance': 'NOT FOUND [2025 Audited FS mentions "Chief Risk Officer (CRO) / Chief Compliance Officer" as combined role but does not disclose name. Sources: prubsn.com.my, 2025 Audited FS, conf 35]',
        'Chief Information Officer': 'NOT FOUND [CIO not mentioned in ExCo, 2025 Audited FS, or Board Charter. Sources: prubsn.com.my, 2025 Audited FS, conf 35]',
        'Head of Internal Audit': 'NOT FOUND [2025 Audited FS mentions "Chief Internal Auditor / GwIA Chief Internal Auditor" confirming role exists but name not disclosed. Sources: prubsn.com.my, 2025 Audited FS, conf 35]',
    },
    # 9. ICBC (Malaysia) Berhad — CRO reclassification + compliance downgrade
    "ICBC (Malaysia) Berhad": {
        'Chief Risk Officer': 'NOT FOUND [BOARD-LEVEL RECLASSIFICATION: Sum Leng Kuang is Chairman of Board Risk Management Committee (board-level, not executive CRO). The actual executive CRO is NOT publicly disclosed. Previous entry at conf 85 was board-level, not executive. Sources: malaysia.icbc.com.cn Directors page, conf 40]',
        'Head of Internal Audit': 'NOT FOUND [BOARD-LEVEL RECLASSIFICATION: Chin Chee Kong is Chairman of Audit Committee (board-level, not executive CAE). The actual executive IA head is NOT publicly disclosed. Sources: malaysia.icbc.com.cn Directors page, conf 40]',
        'Head of Compliance': 'Liau Cheek [RocketReach, conf 55 — could not verify with official source. ICBC MY website and Pillar 3 PDF (31 Dec 2025) do not mention any compliance officer by name. Downgraded from conf 65.]',
        # CISO, GRC, CFO, CIO already NOT FOUND — keep them
    },
    # 10. Malaysia International Islamic Bank IB — entity non-existent confirmation
    "Malaysia International Islamic Bank IB": {
        'Head of Governance Risk & Compliance': 'ENTITY NON-EXISTENT [Entity does not exist as a licensed Islamic bank in Malaysia. Not on BNM-sourced Wikipedia list of 18 licensed Islamic banks. Source: en.wikipedia.org/wiki/List_of_banks_in_Malaysia, conf 0]',
        'Chief Financial Officer': 'ENTITY NON-EXISTENT [Entity does not exist as a licensed Islamic bank in Malaysia. Source: en.wikipedia.org/wiki/List_of_banks_in_Malaysia, conf 0]',
        'Chief Risk Officer': 'ENTITY NON-EXISTENT [Entity does not exist as a licensed Islamic bank in Malaysia. Source: en.wikipedia.org/wiki/List_of_banks_in_Malaysia, conf 0]',
        'Head of Compliance': 'ENTITY NON-EXISTENT [Entity does not exist as a licensed Islamic bank in Malaysia. Source: en.wikipedia.org/wiki/List_of_banks_in_Malaysia, conf 0]',
        'Chief Information Officer': 'ENTITY NON-EXISTENT [Entity does not exist as a licensed Islamic bank in Malaysia. Source: en.wikipedia.org/wiki/List_of_banks_in_Malaysia, conf 0]',
        'Head of Internal Audit': 'ENTITY NON-EXISTENT [Entity does not exist as a licensed Islamic bank in Malaysia. Source: en.wikipedia.org/wiki/List_of_banks_in_Malaysia, conf 0]',
    },
}


def update_master_csv():
    """Read master CSV, apply updates, write back."""
    # Backup
    backup_path = MASTER_PATH + f".bak-pre-{VERSION}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    shutil.copy2(MASTER_PATH, backup_path)
    print(f"Backup: {backup_path}")

    with open(MASTER_PATH, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames

    updated_count = 0
    for row in rows:
        name = row['Institution_Name']
        for target_name, updates in UPDATES.items():
            if target_name.lower() in name.lower():
                for col, new_val in updates.items():
                    old_val = row.get(col, '').strip()
                    row[col] = new_val
                    if old_val != new_val:
                        print(f"  UPDATED: {name} | {col[:35]}")
                updated_count += 1
                break

    print(f"\nInstitutions updated: {updated_count}")

    with open(MASTER_PATH, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Master CSV written: {MASTER_PATH}")
    return rows


def create_enriched_csv(master_rows):
    """Copy updated master to enriched v5.17."""
    # Copy from master (which is already updated)
    fieldnames = list(master_rows[0].keys())
    with open(NEW_ENRICHED, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(master_rows)
    print(f"Enriched CSV written: {NEW_ENRICHED}")

    # Also copy to Voron-Campaign
    vc_path = os.path.join(VORON_CAMPIGN, f"prospect-database-enriched-{VERSION}.csv")
    shutil.copy2(NEW_ENRICHED, vc_path)
    print(f"Voron-Campaign copy: {vc_path}")

    # Also update the master CSV in Voron-Campaign
    vc_master = os.path.join(VORON_CAMPIGN, "prospect-database-7stakeholders.csv")
    shutil.copy2(MASTER_PATH, vc_master)
    print(f"Voron-Campaign master: {vc_master}")


def compute_stats(rows):
    """Compute coverage statistics."""
    total_filled = 0
    total_roles = 0
    empty = 0
    notfound = 0
    nonexistent = 0

    for r in rows:
        for col in ROLE_COLS:
            val = r.get(col, '').strip()
            total_roles += 1
            if not val:
                empty += 1
            elif val.startswith('ENTITY NON-EXISTENT') or val.startswith('ENTITY NON-EXISTENT'):
                nonexistent += 1
            elif val.startswith('NOT FOUND') or val.startswith('NOTFOUND'):
                notfound += 1
            else:
                total_filled += 1

    coverage = 100 * total_filled / total_roles if total_roles > 0 else 0
    return {
        'total_institutions': len(rows),
        'total_roles': total_roles,
        'filled': total_filled,
        'coverage': coverage,
        'notfound': notfound,
        'empty': empty,
        'nonexistent': nonexistent,
    }


def coverage_buckets(rows):
    """Count institutions per coverage bucket."""
    from collections import defaultdict
    buckets = defaultdict(int)
    for r in rows:
        filled = 0
        for col in ROLE_COLS:
            val = r.get(col, '').strip()
            if val and not val.startswith('NOT FOUND') and not val.startswith('NOTFOUND') and not val.startswith('ENTITY NON-EXISTENT'):
                filled += 1
        buckets[filled] += 1
    return dict(sorted(buckets.items(), reverse=True))


if __name__ == '__main__':
    print(f"=== VoronDRQ Enrichment {VERSION} Update ===\n")

    rows = update_master_csv()
    create_enriched_csv(rows)

    stats = compute_stats(rows)
    buckets = coverage_buckets(rows)

    print(f"\n=== Coverage Statistics ===")
    print(f"Total institutions: {stats['total_institutions']}")
    print(f"Total roles: {stats['total_roles']}")
    print(f"Filled: {stats['filled']} ({stats['coverage']:.1f}%)")
    print(f"NOT FOUND: {stats['notfound']}")
    print(f"ENTITY NON-EXISTENT: {stats['nonexistent']}")
    print(f"Empty: {stats['empty']}")

    print(f"\nCoverage buckets:")
    for k, v in buckets.items():
        print(f"  {k}/7: {v} institutions")

#!/usr/bin/env python3
"""
VoronDRQ Enrichment v5.12 Update Script
- 3 NEW role additions (4/7 → 5/7 promotions)
- 30 NOT FOUND audit trail entries across 11 institutions
- Focus: 4/7 cluster resolution
"""
import csv
import shutil
import os
from datetime import datetime

MASTER_CSV = '/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv'
ENRICHED_SRC = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.11.csv'
ENRICHED_DST = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.12.csv'
MASTER_DST = '/home/p62operator/.openclaw/workspace-hoi/vorondrq-rmit-campaign/prospect-database-7stakeholders.csv'

ROLE_COLS = [
    'Chief Information Security Officer',
    'Head of Governance Risk & Compliance',
    'Chief Financial Officer',
    'Chief Risk Officer',
    'Head of Compliance',
    'Chief Information Officer',
    'Head of Internal Audit',
]

# ====== NEW ROLE ADDITIONS (3) ======
# Format: (Institution_Name, role_column, value)
NEW_ROLES = [
    (
        'FWD Insurance Berhad',
        'Head of Compliance',
        'Anita Menon (Chief Governance Officer, oversees compliance) [Official: fwd.com.my/about-us/fmh/meet-our-team, conf 65 - same person as Head of GRC; Chief Governance Officer title covers compliance function]'
    ),
    (
        'Takaful Am General Berhad',
        'Head of Governance Risk & Compliance',
        'Shizal Fisham bin Ramli (Ketua Pegawai Tadbir Urus / Chief Governance Officer, Takaful Malaysia group) [Official: takaful-malaysia.com.my/tentang-kami/barisan-kepimpinan/, conf 60 - covers Governance component of GRC; Compliance separately headed by Redzuan bin Abu]'
    ),
    (
        'Takaful IKHLAS Berhad',
        'Head of Governance Risk & Compliance',
        'Abd Ghafur Ahmad (Senior VP & Group Chief Compliance Officer, MNRB Group) [Official: mnrb.com.my/about-us/our-leadership, conf 75 - Group Chief Compliance Officer functionally covers GRC; same person as Head of Compliance column]'
    ),
]

# ====== NOT FOUND AUDIT TRAIL ENTRIES (30) ======
# Format: (Institution_Name, role_column, NOT_FOUND_value)
NOT_FOUND_ENTRIES = [
    # FWD Insurance Berhad (2 NOT FOUND)
    ('FWD Insurance Berhad', 'Chief Information Security Officer',
     'NOT FOUND [Official: fwd.com.my/about-us/ins/meet-our-team (4 execs) + fwd.com.my/about-us/fmh/meet-our-team (9 execs) — no CISO listed. CISO function may report under COO (Tang Ai Hoong). conf 30]'),
    ('FWD Insurance Berhad', 'Chief Information Officer',
     'NOT FOUND [Official: fwd.com.my/about-us/ins/meet-our-team + fwd.com.my/about-us/fmh/meet-our-team — no CIO listed. CIO function may be combined with COO (Tang Ai Hoong). conf 30]'),

    # Manulife Insurance Berhad (3 NOT FOUND)
    ('Manulife Insurance Berhad', 'Chief Information Security Officer',
     'NOT FOUND [Official: manulife.com.my Board of Directors page only — no Senior Management Team page exists. Corporate Governance page mentions Group Risk Management Committee but no CISO named. conf 25]'),
    ('Manulife Insurance Berhad', 'Head of Governance Risk & Compliance',
     'NOT FOUND [Official: manulife.com.my Corporate Governance page — Group Risk Management Committee Terms of Reference PDF linked but no Head of GRC named publicly. conf 25]'),
    ('Manulife Insurance Berhad', 'Head of Internal Audit',
     'NOT FOUND [Official: manulife.com.my Corporate Governance page — Group Audit Committee Terms of Reference PDF linked but no Head of Internal Audit named publicly. conf 25]'),

    # QBE Insurance (Malaysia) Sdn Bhd (3 NOT FOUND)
    ('QBE Insurance (Malaysia) Sdn Bhd', 'Chief Information Security Officer',
     'NOT FOUND [Official: qbe.com/my — no public leadership page exists. /about-us and /our-people return 404. Site map returned 0 links. No CISO publicly identified. conf 20]'),
    ('QBE Insurance (Malaysia) Sdn Bhd', 'Chief Information Officer',
     'NOT FOUND [Official: qbe.com/my — no public leadership page. No CIO publicly listed. conf 20]'),
    ('QBE Insurance (Malaysia) Sdn Bhd', 'Head of Internal Audit',
     'NOT FOUND [Official: qbe.com/my — no public leadership page. No Head of Internal Audit publicly listed. conf 20]'),

    # Takaful Am General Berhad (2 NOT FOUND)
    ('Takaful Am General Berhad', 'Chief Information Security Officer',
     'NOT FOUND [Official: takaful-malaysia.com.my/tentang-kami/barisan-kepimpinan/ (18 execs) — no CISO listed. CISO function may report under CTO (Nazaruddin Adha bin Md Noor). conf 30]'),
    ('Takaful Am General Berhad', 'Chief Risk Officer',
     'NOT FOUND [Official: takaful-malaysia.com.my/tentang-kami/barisan-kepimpinan/ (18 execs) — no CRO listed. Risk function may sit under CFO (New Kheng Chee) or Chief Governance Officer. conf 30]'),

    # Takaful IKHLAS Berhad (2 NOT FOUND)
    ('Takaful IKHLAS Berhad', 'Chief Information Security Officer',
     'NOT FOUND [Official: takaful-ikhlas.com.my/corporate/our-leadership (6 SMT execs) + mnrb.com.my/about-us/our-leadership (11 group execs) — no CISO listed at subsidiary or group level. CISO function may report under CIO (Lee Kok Seong). conf 30]'),
    ('Takaful IKHLAS Berhad', 'Chief Risk Officer',
     'NOT FOUND [Official: mnrb.com.my/about-us/our-leadership (11 group execs) — no Group CRO listed. CRO function may be integrated into Group Chief Compliance Officer (Abd Ghafur Ahmad). conf 30]'),

    # ICBC (Malaysia) Berhad (3 NOT FOUND)
    ('ICBC (Malaysia) Berhad', 'Head of Governance Risk & Compliance',
     'NOT FOUND [Official: malaysia.icbc.com.cn/en/column/1438058793782362235.html (Directors page, 5 directors) — no Senior Management page exists. BNM Pillar 3 Disclosure 31 Dec 2025 names only CEO as attestee. conf 35]'),
    ('ICBC (Malaysia) Berhad', 'Chief Financial Officer',
     'NOT FOUND [Official: malaysia.icbc.com.cn + BNM Pillar 3 Disclosure 31 Dec 2025 + 16 years of GP8 quarterly filings — CFO not named in any public source. CEO (Geng Hao) is only executive director on Board. conf 35]'),
    ('ICBC (Malaysia) Berhad', 'Chief Information Officer',
     'NOT FOUND [Official: malaysia.icbc.com.cn + 16 years of Pillar 3 Disclosures (2010-2025) + 16 years of quarterly financial results — CIO not named in any public source. conf 35]'),

    # Boost Bank Berhad (3 NOT FOUND)
    ('Boost Bank Berhad', 'Chief Information Security Officer',
     'NOT FOUND [Official: myboostbank.co/our-leadership-boost-bank (9 senior leaders + 8 directors) — no CISO listed. CISO function likely combined with CTO (Shankar Krishnan). conf 40]'),
    ('Boost Bank Berhad', 'Head of Governance Risk & Compliance',
     'NOT FOUND [Official: myboostbank.co/our-leadership-boost-bank — GRC function split between CRO (Puteri Syurga) and CCO (Dr Mohanamerry Vedamanikam). No standalone Head of GRC. conf 40]'),
    ('Boost Bank Berhad', 'Head of Internal Audit',
     'NOT FOUND [Official: myboostbank.co/our-leadership-boost-bank + myboostbank.co/corporate-governance — Head of Internal Audit not publicly listed. Board Audit Committee chaired by David Lau Nai Pek. conf 40]'),

    # Ryt Bank Berhad (3 NOT FOUND)
    ('Ryt Bank Berhad', 'Chief Information Security Officer',
     'NOT FOUND [Official: rytbank.my/about-us/ (9 senior leaders + 5 directors) — no CISO listed. CISO function likely combined with CTO (Nic Ngoo). conf 40]'),
    ('Ryt Bank Berhad', 'Head of Governance Risk & Compliance',
     'NOT FOUND [Official: rytbank.my/about-us/ — GRC function split between CRO (Yeoh Xin Yi) and CCO (Muhamaad Nasir Bin Hassan). No standalone Head of GRC. conf 40]'),
    ('Ryt Bank Berhad', 'Head of Internal Audit',
     'NOT FOUND [Official: rytbank.my/about-us/ — Head of Internal Audit not publicly listed. conf 40]'),

    # Ryt Bank Berhad (YTL Digital) (3 NOT FOUND — same as Ryt Bank Berhad)
    ('Ryt Bank Berhad (YTL Digital)', 'Chief Information Security Officer',
     'NOT FOUND [Official: rytbank.my/about-us/ (9 senior leaders + 5 directors) — no CISO listed. CISO function likely combined with CTO (Nic Ngoo). conf 40]'),
    ('Ryt Bank Berhad (YTL Digital)', 'Head of Governance Risk & Compliance',
     'NOT FOUND [Official: rytbank.my/about-us/ — GRC function split between CRO (Yeoh Xin Yi) and CCO (Muhamaad Nasir Bin Hassan). conf 40]'),
    ('Ryt Bank Berhad (YTL Digital)', 'Head of Internal Audit',
     'NOT FOUND [Official: rytbank.my/about-us/ — Head of Internal Audit not publicly listed. conf 40]'),

    # Instarem Sdn Bhd (3 NOT FOUND)
    ('Instarem Sdn Bhd', 'Chief Information Security Officer',
     'NOT FOUND [Official: nium.com/about-us (7 global execs) — no global or Malaysia-specific CISO listed. CISO function overseen by CTO (Sekhar Cidambi). conf 30]'),
    ('Instarem Sdn Bhd', 'Head of Governance Risk & Compliance',
     'NOT FOUND [Official: nium.com/about-us — no Malaysia-specific Head of GRC. Global Chief Risk and Compliance Officer (Amaresh Mohan) functionally covers GRC for all Nium markets including Malaysia. conf 35]'),
    ('Instarem Sdn Bhd', 'Head of Internal Audit',
     'NOT FOUND [Official: nium.com/about-us — no global or Malaysia-specific Head of Internal Audit listed. Likely outsourced or below C-suite. conf 25]'),

    # MoneyMatch Sdn Bhd (3 NOT FOUND)
    ('MoneyMatch Sdn Bhd', 'Head of Governance Risk & Compliance',
     'NOT FOUND [Official: moneymatch.co/about-us (15 leaders) — no GRC role listed. GRC function may be combined under Head of Compliance (Thavalogan). conf 30]'),
    ('MoneyMatch Sdn Bhd', 'Chief Risk Officer',
     'NOT FOUND [Official: moneymatch.co/about-us (15 leaders) — no CRO listed. Risk function likely distributed across CEO, COO, and Head of Compliance. conf 30]'),
    ('MoneyMatch Sdn Bhd', 'Head of Internal Audit',
     'NOT FOUND [Official: moneymatch.co/about-us (15 leaders) — no Head of Internal Audit listed. As BNM-licensed MSB, internal audit function required but may be outsourced. conf 30]'),
]


def update_master_csv():
    """Update the master 7stakeholders CSV with new roles and NOT FOUND entries."""
    # Backup
    backup_path = MASTER_CSV + f'.bak-pre-v5.12-{datetime.now().strftime("%Y%m%d-%H%M%S")}'
    shutil.copy2(MASTER_CSV, backup_path)
    print(f"Backup created: {backup_path}")

    with open(MASTER_CSV, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames

    updates_applied = 0
    notfound_applied = 0
    not_found_institutions = set()

    # Apply NEW role additions
    for inst_name, role_col, value in NEW_ROLES:
        for row in rows:
            if row.get('Institution_Name', '') == inst_name:
                existing = row.get(role_col, '').strip()
                if not existing:
                    row[role_col] = value
                    updates_applied += 1
                    print(f"  + {inst_name} → {role_col}: ADDED")
                else:
                    print(f"  ! {inst_name} → {role_col}: already filled, skipping")
                break

    # Apply NOT FOUND entries
    for inst_name, role_col, value in NOT_FOUND_ENTRIES:
        for row in rows:
            if row.get('Institution_Name', '') == inst_name:
                existing = row.get(role_col, '').strip()
                if not existing:
                    row[role_col] = value
                    notfound_applied += 1
                    not_found_institutions.add(inst_name)
                else:
                    print(f"  ! {inst_name} → {role_col}: already filled, skipping NOT FOUND")
                break

    # Write updated master CSV
    with open(MASTER_CSV, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Also write to the campaign directory copy
    with open(MASTER_DST, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n=== Master CSV Update Summary ===")
    print(f"  NEW roles added: {updates_applied}")
    print(f"  NOT FOUND entries added: {notfound_applied}")
    print(f"  Institutions with NOT FOUND entries: {len(not_found_institutions)}")
    return rows, fieldnames


def update_enriched_csv():
    """Copy enriched v5.11 to v5.12 and append new contact rows."""
    shutil.copy2(ENRICHED_SRC, ENRICHED_DST)

    # Read existing enriched CSV to get schema
    with open(ENRICHED_DST, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        existing_rows = list(reader)
        fieldnames = reader.fieldnames

    print(f"\nEnriched CSV schema fields: {fieldnames}")
    print(f"Existing enriched rows: {len(existing_rows)}")

    # Build new rows for the 3 NEW role additions
    new_rows = []
    for inst_name, role_col, value in NEW_ROLES:
        # Parse the value to extract name, title, source, confidence
        # Format: "Name (Title) [Official: URL, conf XX - notes]"
        import re
        name_match = re.match(r'([^(]+)\s*\(([^)]+)\)\s*\[([^]]+)\]', value)
        if name_match:
            name = name_match.group(1).strip()
            title = name_match.group(2).strip()
            meta = name_match.group(3).strip()
            # Extract source URL and confidence
            url_match = re.search(r'(https?://[^\s,]+)', meta)
            conf_match = re.search(r'conf\s+(\d+)', meta)
            source = url_match.group(1) if url_match else ''
            confidence = conf_match.group(1) if conf_match else ''
            notes = meta
        else:
            name = value
            title = ''
            source = ''
            confidence = ''
            notes = ''

        # Determine tier/segment from master CSV
        tier = ''
        segment = ''
        with open(MASTER_CSV, 'r', encoding='utf-8-sig') as f:
            mreader = csv.DictReader(f)
            for mrow in mreader:
                if mrow.get('Institution_Name') == inst_name:
                    tier = mrow.get('Tier', '')
                    segment = mrow.get('Segment', '')
                    break

        new_row = {fn: '' for fn in fieldnames}
        # Try to match common field names
        for fn in fieldnames:
            fn_lower = fn.lower().replace(' ', '_')
            if fn_lower in ['tier']:
                new_row[fn] = tier
            elif fn_lower in ['segment']:
                new_row[fn] = segment
            elif fn_lower in ['institution_name', 'institution', 'company', 'company_name']:
                new_row[fn] = inst_name
            elif fn_lower in ['role', 'target_role', 'stakeholder_role']:
                new_row[fn] = role_col
            elif fn_lower in ['name', 'full_name', 'stakeholder_name', 'contact_name']:
                new_row[fn] = name
            elif fn_lower in ['title', 'exact_title', 'job_title']:
                new_row[fn] = title
            elif fn_lower in ['source', 'source_url', 'url']:
                new_row[fn] = source
            elif fn_lower in ['confidence', 'confidence_score', 'score']:
                new_row[fn] = confidence
            elif fn_lower in ['notes', 'notes_notes', 'remarks']:
                new_row[fn] = notes
            elif fn_lower in ['collection_date', 'date', 'date_collected']:
                new_row[fn] = '2026-07-19'
            elif fn_lower in ['version']:
                new_row[fn] = 'v5.12'

        new_rows.append(new_row)

    # Append new rows
    with open(ENRICHED_DST, 'a', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        for row in new_rows:
            writer.writerow(row)

    print(f"  New rows appended to enriched CSV: {len(new_rows)}")
    return len(new_rows)


def compute_stats(rows):
    """Compute coverage statistics after update."""
    total_filled = 0
    total_possible = 0
    coverage_dist = {}
    promotions = {'4_to_5': [], 'other': []}

    for row in rows:
        inst_name = row.get('Institution_Name', 'Unknown')
        filled = 0
        for rc in ROLE_COLS:
            total_possible += 1
            val = row.get(rc, '').strip()
            if val and not val.startswith('NOT FOUND') and len(val) > 2:
                filled += 1
                total_filled += 1

        coverage_dist[filled] = coverage_dist.get(filled, 0) + 1
        # Track promotions (institutions that went from 4/7 to 5/7)
        if filled == 5 and inst_name in [x[0] for x in NEW_ROLES]:
            promotions['4_to_5'].append(inst_name)

    return total_filled, total_possible, coverage_dist, promotions


def main():
    print("=" * 60)
    print("VoronDRQ Enrichment v5.12 Update")
    print("=" * 60)

    rows, fieldnames = update_master_csv()
    new_enriched = update_enriched_csv()

    total_filled, total_possible, coverage_dist, promotions = compute_stats(rows)

    print(f"\n{'=' * 60}")
    print(f"FINAL STATISTICS (v5.12)")
    print(f"{'=' * 60}")
    print(f"  Total institutions: {len(rows)}")
    print(f"  Total roles filled: {total_filled}/{total_possible} = {100*total_filled/total_possible:.1f}%")
    print(f"\n  Coverage Distribution:")
    for k in sorted(coverage_dist.keys(), reverse=True):
        print(f"    {k}/7: {coverage_dist[k]} institutions")
    print(f"\n  Promotions (4/7 → 5/7): {len(promotions['4_to_5'])}")
    for inst in promotions['4_to_5']:
        print(f"    - {inst}")
    print(f"\n  New enriched rows: {new_enriched}")


if __name__ == '__main__':
    main()

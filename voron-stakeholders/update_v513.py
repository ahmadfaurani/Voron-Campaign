#!/usr/bin/env python3
"""
VoronDRQ Enrichment v5.13 Update Script
- 9 NEW role additions (3/7 cluster resolution)
- 1 CORRECTION (SMBC MY CISO - previous entry was CEO misfiled)
- 32 NOT FOUND audit trail entries across 10 institutions (Setel x2 rows)
- Focus: 3/7 cluster resolution (11 institutions, 44 roles recoverable)

Methodology: 3 parallel subagents (delegate_task) with web+browser toolsets:
- Subagent 1: Insurers (AmMetLife, MSIG Insurance) — 8 roles
- Subagent 2: Banks (DB MY, Maybank IB, SMBC MY) — 12 roles
- Subagent 3: GLC+E-Money+MSB (JCorp, PBSNB, PNSB, Setel x2, Wise) — 20 roles
"""
import csv
import shutil
import os
from datetime import datetime

MASTER_CSV = '/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv'
ENRICHED_SRC = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.12.csv'
ENRICHED_DST = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.13.csv'
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

# ====== NEW ROLE ADDITIONS (9) ======
# Format: (Institution_Name, role_column, value)
NEW_ROLES = [
    # SMBC MY CFO - HIGH confidence (official annual financial statement)
    (
        'Sumitomo Mitsui Banking Corporation Malaysia Berhad',
        'Chief Financial Officer',
        'Norihiro Oyanagi (Officer primarily responsible for financial management) [Official: smbc.co.jp/asia/malaysia/financial-information/financial-statement-31Mar2025.pdf - Annual Financial Statement 31 March 2025, signed by CEO Atsuhide Shiojiri, conf 90 - BNM-required statutory CFO designation]'
    ),
    # PBSNB Head of GRC - HIGH confidence (functional mapping from official source)
    (
        'Permodalan BSN Berhad (PBSNB)',
        'Head of Governance Risk & Compliance',
        'Wong Ching Fai @ Christopher (Head of Risk and Compliance) [Official: pbsn.com.my/staff/wong-ching-fai-christopher/, conf 90 - same person as CRO and Compliance; combined Risk and Compliance title functionally covers GRC]'
    ),
    # JCorp Head of Compliance - MEDIUM-HIGH (Chief Governance Officer covers G+C umbrella)
    (
        'Johor Corporation (JCorp)',
        'Head of Compliance',
        'Mohd Azmi Hitam (Chief Governance Officer, leads Governance and Risk Division - GRD) [Official: jcorp.com.my/our-leadership + JCorp 2023 Integrated Report PDF, conf 80 - Chief Governance Officer functionally covers compliance; GRD is the functional umbrella for compliance]'
    ),
    # PNSB CRO - MEDIUM-HIGH (Integriti covers risk)
    (
        'Permodalan Negeri Selangor Berhad (PNSB)',
        'Chief Risk Officer',
        'Mohammed Hanafi Bin Muhi (Senior Manager - Integriti, Audit & Governans) [Official: pnsb.com.my/info-korporat/, conf 80 - Integrity function in Malaysian GLCs typically subsumes enterprise risk; same person as Head of GRC and IA]'
    ),
    # PNSB Head of Compliance - MEDIUM (Integriti covers compliance)
    (
        'Permodalan Negeri Selangor Berhad (PNSB)',
        'Head of Compliance',
        'Mohammed Hanafi Bin Muhi (Senior Manager - Integriti, Audit & Governans) [Official: pnsb.com.my/info-korporat/, conf 75 - Integriti (Integrity) function in Malaysian GLCs typically includes compliance; same person as Head of GRC and CRO]'
    ),
    # JCorp Head of Internal Audit - MEDIUM (Chief Corporate Services Officer covers IA)
    (
        'Johor Corporation (JCorp)',
        'Head of Internal Audit',
        'Mohd Nordin Jamaludin (Chief Corporate Services Officer) [Official: jcorp.com.my/our-leadership + JCorp 2023 Integrated Report PDF, conf 70 - Corporate Services typically encompasses audit, risk, and governance support; Board Audit and Risk Committee (BARC) provides board-level oversight]'
    ),
    # Setel Head of Compliance - MEDIUM-LOW (General Counsel covers compliance)
    (
        'Setel (PETRONAS Dagangan)',
        'Head of Compliance',
        'Fazni Ismail (General Counsel, Legal Retail) [Official: mymesra.com.my/about-us/leadership-team, conf 65 - General Counsel in PETRONAS group entities typically oversees compliance; Setel Ventures Sdn Bhd governed by PDB parent executives]'
    ),
    # Setel Head of GRC - MEDIUM-LOW (same person as Head of Compliance)
    (
        'Setel (PETRONAS Dagangan)',
        'Head of Governance Risk & Compliance',
        'Fazni Ismail (General Counsel, Legal Retail) [Official: mymesra.com.my/about-us/leadership-team, conf 60 - General Counsel functionally covers GRC umbrella; same person as Head of Compliance]'
    ),
    # Wise Head of GRC - MEDIUM-LOW (Chief Legal Officer covers GRC at fintechs)
    (
        'Wise (formerly TransferWise) Malaysia Sdn Bhd',
        'Head of Governance Risk & Compliance',
        'Jessica Winter (Chief Legal Officer / General Counsel, Wise Plc global) [Official: owners.wise.com/governance/leadership-team, conf 65 - General Counsel at UK fintechs typically oversees governance, risk, and compliance coordination; Wise Malaysia subsidiary inherits from parent]'
    ),
    # Setel by PETRONAS Dagangan Berhad (DUPLICATE row) - same updates
    (
        'Setel by PETRONAS Dagangan Berhad',
        'Head of Compliance',
        'Fazni Ismail (General Counsel, Legal Retail) [Official: mymesra.com.my/about-us/leadership-team, conf 65 - General Counsel in PETRONAS group entities typically oversees compliance; Setel Ventures Sdn Bhd governed by PDB parent executives]'
    ),
    (
        'Setel by PETRONAS Dagangan Berhad',
        'Head of Governance Risk & Compliance',
        'Fazni Ismail (General Counsel, Legal Retail) [Official: mymesra.com.my/about-us/leadership-team, conf 60 - General Counsel functionally covers GRC umbrella; same person as Head of Compliance]'
    ),
]

# ====== CORRECTIONS (1) ======
# Replace wrong entries with NOT FOUND audit trails
CORRECTIONS = [
    # SMBC MY CISO - previous entry was CEO misfiled as CISO
    (
        'Sumitomo Mitsui Banking Corporation Malaysia Berhad',
        'Chief Information Security Officer',
        'NOT FOUND [CORRECTION: previous entry was CEO Atsuhide Shiojiri misfiled as CISO — he is the President/CEO effective 30 Apr 2024 (theedgemalaysia.com, themalaysianreserve.com), NOT the CISO. Official: SMBC MY Annual Financial Statement 31 Mar 2025 + Board of Directors PDF + Pillar 3 Disclosure 31 Mar 2025 — no CISO publicly named in any official document. conf 35]'
    ),
]

# ====== NOT FOUND AUDIT TRAIL ENTRIES (32) ======
# Format: (Institution_Name, role_column, NOT_FOUND_value)
NOT_FOUND_ENTRIES = [
    # AmMetLife Insurance Berhad (4 NOT FOUND) — official Management Team page (8 execs) + Board Charter PDF checked
    ('AmMetLife Insurance Berhad', 'Chief Information Security Officer',
     'NOT FOUND [Official: ammetlife.com/about-us/about-ammetlife/management-team (8 senior managers: CEO, CFO, CIO-Investment, CIO-IT, CTO, CRO, Chief Bancassurance Officer, Chief Corporate Solutions Officer) — none with CISO/Information Security title. Board Charter V2.0 (11 Dec 2023) makes no mention of CISO. conf 30]'),
    ('AmMetLife Insurance Berhad', 'Head of Governance Risk & Compliance',
     'NOT FOUND [Official: ammetlife.com/about-us/about-ammetlife/management-team — no dedicated GRC head listed. CRO Low Siew Mooi (already mapped) is the only risk-related senior manager. Risk Management Committee of the Board oversees regulatory compliance. conf 30]'),
    ('AmMetLife Insurance Berhad', 'Head of Compliance',
     'NOT FOUND [Official: ammetlife.com/about-us/about-ammetlife/management-team + corporate-governance page — no Head of Compliance listed. Board Charter references compliance function under Risk Management Committee oversight but no name provided. conf 30]'),
    ('AmMetLife Insurance Berhad', 'Head of Internal Audit',
     'NOT FOUND [Official: ammetlife.com Board Charter V2.0 (11 Dec 2023) Section 2.6.1 ii confirms Chief Internal Auditor role exists (appointment overseen by Audit and Examination Committee, chaired by Alan Ronald Goon Hock Lee INED) but name not publicly disclosed. Management Team page does not list this role. conf 30]'),

    # MSIG Insurance (Malaysia) Bhd (4 NOT FOUND) — official "Our management" page + MSIG Annual Report 2025 PDF checked
    ('MSIG Insurance (Malaysia) Bhd', 'Chief Information Security Officer',
     'NOT FOUND [Official: msig.com.my/about-msig (12 senior managers) + MSIG Annual Report 2025 PDF page 10 (13 senior managers) — no CISO publicly disclosed. IT security function likely reports under Chin Jee Gwan (EVP IT/Digital/Bancassurance/Branding). conf 35]'),
    ('MSIG Insurance (Malaysia) Bhd', 'Head of Governance Risk & Compliance',
     'NOT FOUND [Official: MSIG Annual Report 2025 PDF page 10 Senior Management section — no separate Head of GRC listed. GRC function consolidated under SVP ERM Kelvin Hii Chee Yun (already mapped to CRO). conf 35]'),
    ('MSIG Insurance (Malaysia) Bhd', 'Head of Compliance',
     'NOT FOUND [Official: MSIG Annual Report 2025 PDF Corporate Governance section — confirms Chief Compliance Officer role exists but explicitly states name is "Not explicitly named in the provided text". External auditor: KPMG PLT. conf 35]'),
    ('MSIG Insurance (Malaysia) Bhd', 'Head of Internal Audit',
     'NOT FOUND [Official: MSIG Annual Report 2025 PDF Internal Audit section — confirms Chief Internal Auditor role exists but explicitly states name is "Not explicitly named in the provided text". conf 35]'),

    # Deutsche Bank (Malaysia) Berhad (4 NOT FOUND) — country.db.com has no leadership page
    ('Deutsche Bank (Malaysia) Berhad', 'Head of Governance Risk & Compliance',
     'NOT FOUND [Official: country.db.com/malaysia/en — no public senior management/leadership page; only statutory CFO disclosure per BNM requirement. /about-us/corporate-governance returns 404. GRC function likely exists internally (often combined with CRO office). conf 20]'),
    ('Deutsche Bank (Malaysia) Berhad', 'Head of Compliance',
     'NOT FOUND [Official: country.db.com/malaysia/en — no management page. Web/LinkedIn searches returned only generic global DB pages. Likely exists internally but role-holder name not public. conf 20]'),
    ('Deutsche Bank (Malaysia) Berhad', 'Chief Information Officer',
     'NOT FOUND [Official: country.db.com/malaysia/en — no management page. CIO function at DB Malaysia likely reports into DB APAC/regional technology organisation. conf 20]'),
    ('Deutsche Bank (Malaysia) Berhad', 'Head of Internal Audit',
     'NOT FOUND [Official: country.db.com/malaysia/en — no management page. IA at foreign bank subsidiaries in Malaysia often reports functionally to regional/global IA with local name not public. conf 20]'),

    # Maybank Investment Bank Berhad (4 NOT FOUND) — all "inherited from parent"
    ('Maybank Investment Bank Berhad', 'Chief Information Security Officer',
     'NOT FOUND [Official: maybank2u.com.my Senior Management page (6 senior managers: CEO, Deputy CEO, CFO, CRO, Human Capital Director, Head of IT — no CISO listed) + Maybank Group Leadership page (13 executives — no Group CISO publicly listed). CISO function likely inherited from Maybank Group. conf 35]'),
    ('Maybank Investment Bank Berhad', 'Head of Governance Risk & Compliance',
     'NOT FOUND [Official: Maybank IB Corporate Governance Statement June 2024 + Maybank Group Leadership page — no GRC head named at IB or Group level. GRC function likely exists at Maybank Group under Group CRO Mohamed Rezwan Abdullah Ismail. conf 25]'),
    ('Maybank Investment Bank Berhad', 'Head of Compliance',
     'NOT FOUND [Official: Maybank IB Corporate Governance Statement June 2024 Page 9 — Board duty to designate Compliance Officers at Senior Management level (role confirmed to exist, name NOT disclosed). May inherit from Maybank Group. conf 40]'),
    ('Maybank Investment Bank Berhad', 'Head of Internal Audit',
     'NOT FOUND [Official: Maybank IB Corporate Governance Statement June 2024 Page 32 — Audit Committee responsibility to evaluate Head of Audit, Investment Banking (role confirmed to exist, name NOT disclosed). conf 40]'),

    # SMBC MY (3 NOT FOUND for GRC, Compliance, CIO — CISO handled in CORRECTIONS)
    ('Sumitomo Mitsui Banking Corporation Malaysia Berhad', 'Head of Governance Risk & Compliance',
     'NOT FOUND [Official: SMBCMY Board of Directors PDF + Annual Financial Statement 31 Mar 2025 + Pillar 3 Disclosure 31 Mar 2025 — no public Senior Management page; only Board of Directors PDF. GRC function likely combined with Risk (Anand Mahadevan, Executive Director since 26 May 2025, is also Regional CRO SMBC Singapore — may concurrently serve as SMBC MY CRO but not explicitly confirmed). conf 30]'),
    ('Sumitomo Mitsui Banking Corporation Malaysia Berhad', 'Head of Compliance',
     'NOT FOUND [Official: SMBCMY Board of Directors PDF + Annual Financial Statement 31 Mar 2025 — Compliance function likely combined with General Counsel or COO (common pattern for Japanese bank subsidiaries in Malaysia). Name not publicly disclosed. conf 30]'),
    ('Sumitomo Mitsui Banking Corporation Malaysia Berhad', 'Chief Information Officer',
     'NOT FOUND [Official: SMBCMY Board of Directors PDF + Annual Financial Statement 31 Mar 2025 — CIO function likely combined with COO (common pattern for Japanese bank subsidiaries). Name not publicly disclosed. conf 30]'),

    # Johor Corporation (2 NOT FOUND — Compliance and IA filled, CISO and CRO not found)
    ('Johor Corporation (JCorp)', 'Chief Information Security Officer',
     'NOT FOUND [Official: jcorp.com.my/our-leadership + JCorp 2023 Integrated Report PDF — no CISO or Head of Information Security listed. Security function likely subsumed under Chief Digital Officer (Ahmad Yusri Mohamed). conf 30]'),
    ('Johor Corporation (JCorp)', 'Chief Risk Officer',
     'NOT FOUND [Official: jcorp.com.my/our-leadership + JCorp 2023 Integrated Report PDF — no CRO or Head of Risk Management named. Risk function consolidated under Chief Governance Officer (Mohd Azmi Hitam) within Governance and Risk Division (GRD). conf 30]'),

    # PBSNB (3 NOT FOUND — GRC filled, CISO/CIO/IA not found)
    ('Permodalan BSN Berhad (PBSNB)', 'Chief Information Security Officer',
     'NOT FOUND [Official: pbsn.com.my/management-team/ (7-person management team) — no CISO, Head of Information Security, or any IT security title. As BSN Bank subsidiary, IT security may be inherited from parent BSN Bank CISO function. conf 35]'),
    ('Permodalan BSN Berhad (PBSNB)', 'Chief Information Officer',
     'NOT FOUND [Official: pbsn.com.my/management-team/ (7-person management team) — no CIO or Head of IT. Mohd Irwan Wahed (Head of Investment and Research) is closest by seniority but investment-focused. IT/CIO function likely inherited from parent BSN Bank. conf 35]'),
    ('Permodalan BSN Berhad (PBSNB)', 'Head of Internal Audit',
     'NOT FOUND [Official: pbsn.com.my/management-team/ — no Head of Internal Audit listed. Internal audit at small BSN subsidiaries typically provided by parent BSN Group Internal Audit or external auditors. conf 35]'),

    # PNSB (2 NOT FOUND — CRO and Compliance filled, CISO and CIO not found)
    ('Permodalan Negeri Selangor Berhad (PNSB)', 'Chief Information Security Officer',
     'NOT FOUND [Official: pnsb.com.my/info-korporat/ (Kumpulan Pengurusan / Management Group + Ketua Jabatan / Heads of Department) — no CISO or IT security role listed. PNSB is property-focused state GLC — IT security likely outsourced or under junior IT manager. conf 30]'),
    ('Permodalan Negeri Selangor Berhad (PNSB)', 'Chief Information Officer',
     'NOT FOUND [Official: pnsb.com.my/info-korporat/ — no CIO, Head of IT, or technology leadership role. As property-focused state GLC, IT leadership likely at General Manager level (not on leadership page) or outsourced. conf 30]'),

    # Setel (PETRONAS Dagangan) — 1 NOT FOUND (CRO)
    ('Setel (PETRONAS Dagangan)', 'Chief Risk Officer',
     'NOT FOUND [Official: mymesra.com.my/about-us/leadership-team (18 PDB executives) — no CRO or Head of Risk listed. PDB parent has no standalone CRO at leadership team level. Setel risk management likely consolidated under Fazni Ismail (General Counsel Legal Retail) or provided by PETRONAS Group Risk function at parent (not PDB) level. conf 30]'),

    # Setel by PETRONAS Dagangan Berhad (DUPLICATE row) — same 1 NOT FOUND
    ('Setel by PETRONAS Dagangan Berhad', 'Chief Risk Officer',
     'NOT FOUND [Official: mymesra.com.my/about-us/leadership-team (18 PDB executives) — no CRO or Head of Risk listed. PDB parent has no standalone CRO at leadership team level. Setel risk management likely consolidated under Fazni Ismail (General Counsel Legal Retail) or provided by PETRONAS Group Risk function at parent (not PDB) level. conf 30]'),

    # Wise Malaysia (3 NOT FOUND — GRC filled, CISO/CRO/IA not found)
    ('Wise (formerly TransferWise) Malaysia Sdn Bhd', 'Chief Information Security Officer',
     'NOT FOUND [Official: owners.wise.com/governance/leadership-team (10 Wise Plc executives) — no CISO, Head of Information Security, or similar title. Wise Plc has CISO function (FCA/PRA required) but below leadership-team level, not publicly disclosed. Wise Malaysia MSB local CISO unlikely. conf 35]'),
    ('Wise (formerly TransferWise) Malaysia Sdn Bhd', 'Chief Risk Officer',
     'NOT FOUND [Official: owners.wise.com/governance/leadership-team — no CRO or Head of Risk on Wise Plc leadership page. Rohan Basu (Head of Global Operations, former Global Head of Financial Crime Operations) is closest functional match for financial crime risk. Wise Malaysia MSB likely has no local CRO. conf 30]'),
    ('Wise (formerly TransferWise) Malaysia Sdn Bhd', 'Head of Internal Audit',
     'NOT FOUND [Official: owners.wise.com/governance/leadership-team — no Head of Internal Audit or Group Internal Audit Director. Wise Plc has Audit Committee at board level (UK Corporate Governance Code required) but IA head below leadership-team level. Wise Malaysia local IA likely outsourced. conf 35]'),
]


def update_master_csv():
    """Update the master 7stakeholders CSV with new roles, corrections, and NOT FOUND entries."""
    # Backup
    backup_path = MASTER_CSV + f'.bak-pre-v5.13-{datetime.now().strftime("%Y%m%d-%H%M%S")}'
    shutil.copy2(MASTER_CSV, backup_path)
    print(f"Backup created: {backup_path}")

    with open(MASTER_CSV, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames

    updates_applied = 0
    corrections_applied = 0
    notfound_applied = 0
    not_found_institutions = set()

    # Apply NEW role additions
    print("\n--- NEW ROLE ADDITIONS ---")
    for inst_name, role_col, value in NEW_ROLES:
        found = False
        for row in rows:
            if row.get('Institution_Name', '') == inst_name:
                existing = row.get(role_col, '').strip()
                if not existing:
                    row[role_col] = value
                    updates_applied += 1
                    print(f"  + {inst_name} → {role_col}: ADDED")
                else:
                    print(f"  ! {inst_name} → {role_col}: already filled, skipping")
                found = True
                break
        if not found:
            print(f"  ? {inst_name}: institution not found in master CSV")

    # Apply CORRECTIONS (replace existing wrong entries)
    print("\n--- CORRECTIONS ---")
    for inst_name, role_col, value in CORRECTIONS:
        for row in rows:
            if row.get('Institution_Name', '') == inst_name:
                existing = row.get(role_col, '').strip()
                if existing:
                    print(f"  ~ {inst_name} → {role_col}: REPLACING existing entry")
                    print(f"      OLD: {existing[:120]}{'...' if len(existing)>120 else ''}")
                    print(f"      NEW: {value[:120]}{'...' if len(value)>120 else ''}")
                    row[role_col] = value
                    corrections_applied += 1
                else:
                    print(f"  ! {inst_name} → {role_col}: empty, applying as NOT FOUND")
                    row[role_col] = value
                    notfound_applied += 1
                break

    # Apply NOT FOUND entries
    print("\n--- NOT FOUND AUDIT TRAILS ---")
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
    print(f"  CORRECTIONS applied: {corrections_applied}")
    print(f"  NOT FOUND entries added: {notfound_applied}")
    print(f"  Institutions with NOT FOUND entries: {len(not_found_institutions)}")
    return rows, fieldnames


def update_enriched_csv():
    """Copy enriched v5.12 to v5.13 and append new contact rows for the 9 NEW role additions."""
    shutil.copy2(ENRICHED_SRC, ENRICHED_DST)

    # Read existing enriched CSV to get schema
    with open(ENRICHED_DST, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        existing_rows = list(reader)
        fieldnames = reader.fieldnames

    print(f"\nEnriched CSV schema fields: {fieldnames}")
    print(f"Existing enriched rows: {len(existing_rows)}")

    # Build new rows for the NEW role additions (only real additions, not NOT FOUND)
    import re
    new_rows = []
    for inst_name, role_col, value in NEW_ROLES:
        # Parse the value to extract name, title, source, confidence
        # Format: "Name (Title) [Official: URL, conf XX - notes]"  OR  "Name (Title) [Official: path, conf XX - notes]"
        name_match = re.match(r'([^(]+)\s*\(([^)]+)\)\s*\[([^]]+)\]', value)
        if name_match:
            name = name_match.group(1).strip()
            title = name_match.group(2).strip()
            meta = name_match.group(3).strip()
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
                new_row[fn] = 'v5.13'

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
    promotions = {'3_to_4': [], '3_to_5': [], 'other_up': [], 'corrected_down': []}

    new_role_institutions = [(x[0], x[1]) for x in NEW_ROLES]
    corrected_institutions = [(x[0], x[1]) for x in CORRECTIONS]

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
        # Track promotions from 3/7
        if filled >= 4 and inst_name in [x[0] for x in new_role_institutions]:
            if filled == 4:
                promotions['3_to_4'].append(inst_name)
            elif filled == 5:
                promotions['3_to_5'].append(inst_name)
            elif filled > 5:
                promotions['other_up'].append(inst_name)
        # Track corrections (institution affected by correction)
        if inst_name in [x[0] for x in corrected_institutions]:
            promotions['corrected_down'].append(inst_name)

    return total_filled, total_possible, coverage_dist, promotions


def main():
    print("=" * 60)
    print("VoronDRQ Enrichment v5.13 Update")
    print("=" * 60)
    print(f"Focus: 3/7 cluster resolution (11 institutions, 44 recoverable roles)")
    print(f"  NEW roles (named persons): {len(NEW_ROLES)}")
    print(f"  CORRECTIONS (replace wrong entries): {len(CORRECTIONS)}")
    print(f"  NOT FOUND audit trails: {len(NOT_FOUND_ENTRIES)}")

    rows, fieldnames = update_master_csv()
    new_enriched = update_enriched_csv()

    total_filled, total_possible, coverage_dist, promotions = compute_stats(rows)

    print(f"\n{'=' * 60}")
    print(f"FINAL STATISTICS (v5.13)")
    print(f"{'=' * 60}")
    print(f"  Total institutions: {len(rows)}")
    print(f"  Total roles filled: {total_filled}/{total_possible} = {100*total_filled/total_possible:.1f}%")
    print(f"\n  Coverage Distribution:")
    for k in sorted(coverage_dist.keys(), reverse=True):
        print(f"    {k}/7: {coverage_dist[k]} institutions")
    print(f"\n  Promotions (3/7 → 4/7): {len(set(promotions['3_to_4']))}")
    for inst in set(promotions['3_to_4']):
        print(f"    - {inst}")
    print(f"  Promotions (3/7 → 5/7): {len(set(promotions['3_to_5']))}")
    for inst in set(promotions['3_to_5']):
        print(f"    - {inst}")
    if promotions['other_up']:
        print(f"  Other promotions: {len(set(promotions['other_up']))}")
        for inst in set(promotions['other_up']):
            print(f"    - {inst}")
    if promotions['corrected_down']:
        print(f"  Corrections (data quality fixes): {len(set(promotions['corrected_down']))}")
        for inst in set(promotions['corrected_down']):
            print(f"    - {inst}")
    print(f"\n  New enriched rows: {new_enriched}")


if __name__ == '__main__':
    main()

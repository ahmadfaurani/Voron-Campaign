#!/usr/bin/env python3
"""
VoronDRQ Enrichment v5.16 Update Script
Negative-finding documentation + 2 new HIGH-confidence role fills + 1 upgrade

Changes:
  NEW FILLS (2) — Maybank Investment Bank Berhad:
    1. Head of Compliance = Farhan Nor Diyana Samsudin (Chief Compliance Officer)
       Source: Maybank IB SORMIC FY2023 (Statement on Risk Management and Internal
       Control), official document. conf 90.
    2. Head of Internal Audit = Rafirah Muhammad Arif (Chief Audit Executive)
       Source: Maybank IB SORMIC FY2023, official document. conf 90.
    Net: Maybank IB 3/7 -> 5/7.

  UPGRADE (1) — Deutsche Bank (Malaysia) Berhad:
    CFO Liew Yeh Yin confidence 90 -> 95. Confirmed in FY2025 Audited FS
    Statutory Declaration (page 50): "I, Liew Yeh Yin, being the Officer
    primarily responsible for the financial management of Deutsche Bank
    (Malaysia) Berhad." Also confirmed in FY2024 FS (page 48).

  NOT FOUND AUDIT TRAILS (23 empty cells -> documented with official sources):
    J.P. Morgan Chase Bank Malaysia Berhad (6): CISO, GRC, CFO, CRO, CIO, IA
      Checked 7 CG statements (2019-2025), 4 financial reports, 1 climate
      disclosure. CG statements mention 9-10 Senior Management members but do
      NOT name them individually. 4Q financial reports (which contain the
      statutory CFO statement) fail to scrape.
    Deutsche Bank (Malaysia) Berhad (4): GRC, Comp, CIO, IA
      FY2024 FS mentions Head of Compliance and Head of Internal Audit roles
      (pages 18, 25, 30) but does NOT name individuals. FY2025 FS, FY2025
      Pillar 3 (69pp), CG statements 2017-2019 checked.
    AmMetLife Insurance Berhad (4): CISO, GRC, Comp, IA
      Management Team page (8 execs, no CISO/comp/IA/GRC). Board Charter PDF
      references Chief Internal Auditor role but does not name person. Annual
      report not publicly accessible.
    MSIG Insurance (Malaysia) Bhd (4): CISO, GRC, Comp, IA
      Annual Report 2025 (172pp) references CCO (Page 61) and Chief Internal
      Auditor (Pages 64-65) roles but does NOT name individuals. About MSIG
      page lists 12 senior managers, none with compliance/IA/CISO/GRC title.
    Maybank Investment Bank Berhad (2): CISO, GRC
      Senior Management page (5 members), SORMIC FY2023, CG Statement June 2024
      (37pp) checked. No CISO or GRC head named. Likely at Maybank Group level.
    SMBC Malaysia (3): GRC, Comp, CIO
      Annual Audited FS 31 Mar 2025 (60pp), Pillar 3 Disclosure 31 Mar 2025
      (49pp), Board of Directors PDF checked. Only CEO and CFO named.
"""
import csv
import shutil
import os
from datetime import datetime

ENRICHED_SRC = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.15.csv'
ENRICHED_DST = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.16.csv'
MASTER_SRC  = '/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv'
MASTER_BAK  = '/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv.bak-pre-v5.16-' + datetime.now().strftime('%Y%m%d-%H%M%S')

ROLE_COLS = [
    'Chief Information Security Officer',
    'Head of Governance Risk & Compliance',
    'Chief Financial Officer',
    'Chief Risk Officer',
    'Head of Compliance',
    'Chief Information Officer',
    'Head of Internal Audit',
]

# ====== NEW FILLS ======
NEW_FILLS = [
    # Maybank IB Head of Compliance — HIGH confidence (official SORMIC FY2023 document)
    (
        'Maybank Investment Bank Berhad',
        'Head of Compliance',
        'Farhan Nor Diyana Samsudin (Chief Compliance Officer, Maybank Investment Bank Berhad) [Official: Maybank IB SORMIC FY2023 (Statement on Risk Management and Internal Control, FY ended 31 Dec 2023) — "Reviewed and cleared by: Group Audit Compliance: Farhan Nor Diyana Samsudin, Chief Compliance Officer, Maybank Investment Bank Berhad"; maybank2u.com.my iwov-resources PDF, conf 90]',
    ),
    # Maybank IB Head of Internal Audit — HIGH confidence (official SORMIC FY2023 document)
    (
        'Maybank Investment Bank Berhad',
        'Head of Internal Audit',
        'Rafirah Muhammad Arif (Chief Audit Executive, Maybank Investment Bank Berhad) [Official: Maybank IB SORMIC FY2023 — "The GCAE is assisted by Puan Rafirah Muhammad Arif, the Chief Audit Executive (CAE) appointed to oversee the IA function of Maybank IB"; Certified Fraud Examiner, 13 years capital market experience; maybank2u.com.my iwov-resources PDF, conf 90]',
    ),
]

# ====== UPGRADES (replace existing cell with higher-confidence version) ======
UPGRADES = [
    # Deutsche Bank MY CFO — upgrade conf 90 -> 95 (confirmed in FY2025 Audited FS page 50)
    (
        'Deutsche Bank (Malaysia) Berhad',
        'Chief Financial Officer',
        'Liew Yeh Yin (Officer primarily responsible for the financial management of Deutsche Bank (Malaysia) Berhad) [Official: Deutsche Bank Malaysia FY2025 Audited Financial Statements Statutory Declaration (page 50): "I, Liew Yeh Yin, being the Officer primarily responsible for the financial management of Deutsche Bank (Malaysia) Berhad"; also confirmed FY2024 FS page 48; deutschehelix.db.com/malaysia, conf 95]',
    ),
]

# ====== NOT FOUND audit trails (empty cells -> documented negative findings) ======
# Only applied to cells that are currently EMPTY (not already NOT FOUND or filled).
NOT_FOUND = {
    'J.P. Morgan Chase Bank Malaysia Berhad': {
        'Chief Information Security Officer': 'NOT FOUND [Checked 7 CG statements (2019-2025), 4 financial reports (2016-2018), 1 climate disclosure, LinkedIn/web searches. CG statements mention 9-10 Senior Management members but do NOT name them individually. No CISO named in any official JPM Malaysia source. Sources: jpmorgan.com/MY/en/about-us, conf 40]',
        'Head of Governance Risk & Compliance': 'NOT FOUND [Same sources checked as CISO. No Head of GRC named in any JPM Malaysia official source. Sources: jpmorgan.com/MY/en/about-us CG statements 2019-2025, conf 40]',
        'Chief Financial Officer': 'NOT FOUND [4Q2023/4Q2024/4Q2025 Financial Reports (which contain the statutory "Statement by CEO and Officer primarily responsible for financial management" naming the CFO) consistently FAIL to scrape. 2016-2018 reports scrape but signing pages excluded. CFO name likely exists in 4Q reports but inaccessible. Sources: jpmorgan.com/MY/en/about-us financial reports, conf 42]',
        'Chief Risk Officer': 'NOT FOUND [Same sources checked. No CRO named in any JPM Malaysia official source. Sources: jpmorgan.com/MY/en/about-us CG statements 2019-2025, conf 40]',
        'Chief Information Officer': 'NOT FOUND [Same sources checked. No CIO/Head of IT named in any JPM Malaysia official source. Sources: jpmorgan.com/MY/en/about-us CG statements 2019-2025, conf 40]',
        'Head of Internal Audit': 'NOT FOUND [Same sources checked. No Head of Internal Audit named in any JPM Malaysia official source. Sources: jpmorgan.com/MY/en/about-us CG statements 2019-2025, conf 40]',
    },
    'Deutsche Bank (Malaysia) Berhad': {
        'Head of Governance Risk & Compliance': 'NOT FOUND [Checked FY2024/FY2025 audited FS, FY2025 Pillar 3 Disclosure (69pp), CG statements 2017/2018/2019. No Head of GRC named. Sources: deutschehelix.db.com/malaysia/company/financial-statements, conf 40]',
        'Head of Compliance': 'NOT FOUND [FY2024 FS mentions "Head of Compliance" role exists (pages 18, 25, 30) but does NOT name the individual. NRC recommends appointment but no name provided. Sources: deutschehelix.db.com/malaysia FY2024 FS, conf 42]',
        'Chief Information Officer': 'NOT FOUND [Checked all available official Deutsche Bank Malaysia sources. No CIO/Head of IT named in any document. Sources: deutschehelix.db.com/malaysia FY2024 FS, FY2025 FS, FY2025 Pillar 3, conf 40]',
        'Head of Internal Audit': 'NOT FOUND [FY2024 FS mentions "Head of Internal Audit" and "Chief Internal Auditor - Malaysia" roles exist (pages 18, 25, 30) but does NOT name the individual. Sources: deutschehelix.db.com/malaysia FY2024 FS, conf 42]',
    },
    'AmMetLife Insurance Berhad': {
        'Chief Information Security Officer': 'NOT FOUND [Checked official Management Team page (8 executives listed, no CISO), Corporate Governance page, Board Charter PDF (13pp), LinkedIn company page (0 matches). CIO Loh Tian Hu may oversee infosec functionally but does not hold CISO title. Sources: ammetlife.com/about-us/about-ammetlife/management-team, conf 40]',
        'Head of Governance Risk & Compliance': 'NOT FOUND [No dedicated Head of GRC role disclosed. CRO Low Siew Mooi covers risk function; compliance likely falls under risk but no GRC-specific head named. Sources: ammetlife.com Management Team page, Corporate Governance page, Board Charter PDF, conf 40]',
        'Head of Compliance': 'NOT FOUND [Checked Corporate Governance page (Board committees only, no management-level compliance head named), Board Charter PDF (mentions compliance function generically but no individual named), LinkedIn (0 matches). Annual report not publicly accessible. Sources: ammetlife.com/about-us/about-ammetlife/corporate-governance, conf 40]',
        'Head of Internal Audit': 'NOT FOUND [Board Charter PDF (Section 2.6.2 ii) references "Chief Internal Auditor" as a role but does NOT name the person. Management Team page lists no internal audit head. LinkedIn 0 matches. Sources: ammetlife.com Board Charter V2.0 approved 11Dec2023 PDF, conf 40]',
    },
    'MSIG Insurance (Malaysia) Bhd': {
        'Chief Information Security Officer': 'NOT FOUND [Checked About MSIG page (12 senior managers listed, no CISO), Annual Report 2025 (172pp, no CISO/Head of Information Security mentioned), Corporate Profile PDF (10pp), Interim FS PDF (29pp), LinkedIn (0 matches). CIO Chin Jee Gwan may oversee infosec but does not hold CISO title. Sources: msig.com.my/media/1gqllqgr/msig_annual_report_2025.pdf, conf 40]',
        'Head of Governance Risk & Compliance': 'NOT FOUND [No dedicated Head of GRC role disclosed. CRO Kelvin Hii covers risk. Board Compliance & Risk Management Committee exists at board level but no management-level GRC head named. Sources: MSIG Annual Report 2025 (172pp), msig.com.my, conf 40]',
        'Head of Compliance': 'NOT FOUND [Annual Report 2025 references "Chief Compliance Officer (CCO)" role in Corporate Governance Disclosure (Page 61) but does NOT name the individual. About MSIG management page lists 12 senior managers, none with compliance title. Sources: msig.com.my/media/1gqllqgr/msig_annual_report_2025.pdf, conf 40]',
        'Head of Internal Audit': 'NOT FOUND [Annual Report 2025 references "Chief Internal Auditor" role in Internal Audit section (Pages 64-65) but does NOT name the individual. CEO Ang Yien Chia noted as administrative reporting line. Sources: msig.com.my/media/1gqllqgr/msig_annual_report_2025.pdf, conf 40]',
    },
    'Maybank Investment Bank Berhad': {
        'Chief Information Security Officer': 'NOT FOUND [Checked Senior Management page (5 members, none CISO), SORMIC FY2023 (discusses Cyber and Technology Risk Management Framework but does NOT name a CISO), CG Statement June 2024 (37pp, no CISO named). CISO function likely shared with Maybank Group level but not publicly disclosed. Sources: maybank2u.com.my Investment-bank senior-management page, SORMIC FY2023, CG Statement June 2024, conf 40]',
        'Head of Governance Risk & Compliance': 'NOT FOUND [No GRC head listed on Senior Management page, SORMIC FY2023, or CG Statement June 2024. GRC function may be integrated within CRO role (Cheryl Cheng) or at Maybank Group level. Sources: maybank2u.com.my Investment-bank, SORMIC FY2023, conf 40]',
    },
    'Sumitomo Mitsui Banking Corporation Malaysia Berhad': {
        'Head of Governance Risk & Compliance': 'NOT FOUND [Annual Audited FS 31 Mar 2025 (60pp) only discloses Board of Directors (5 members) and CFO (Norihiro Oyanagi). Pillar 3 Disclosure 31 Mar 2025 (49pp) mentions BRMC, RMC, ALCO, Credit Committee but no GRC head named. Sources: smbc.co.jp/asia/malaysia FS & Pillar 3 PDFs, conf 35]',
        'Head of Compliance': 'NOT FOUND [Annual Audited FS 31 Mar 2025 (60pp) does not name Head of Compliance/CCO. Pillar 3 Disclosure 31 Mar 2025 (49pp) discusses risk management governance but does NOT name a compliance officer. Sources: smbc.co.jp/asia/malaysia FS & Pillar 3 PDFs, conf 35]',
        'Chief Information Officer': 'NOT FOUND [Annual Audited FS 31 Mar 2025 (60pp) no CIO/Head of IT named. Pillar 3 Disclosure 31 Mar 2025 (49pp) no CIO named. Sources: smbc.co.jp/asia/malaysia FS & Pillar 3 PDFs, conf 35]',
    },
}


def update_csv():
    # Backup master
    shutil.copy2(MASTER_SRC, MASTER_BAK)
    print(f'Backed up master to {MASTER_BAK}')

    # Read source enriched CSV
    with open(ENRICHED_SRC, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    print(f'Loaded {len(rows)} rows from v5.15')

    new_fills_applied = 0
    upgrades_applied = 0
    notfound_applied = 0

    for r in rows:
        inst = r['Institution_Name']

        # Apply NEW FILLS
        for (fi, frole, fval) in NEW_FILLS:
            if inst == fi:
                r[frole] = fval
                new_fills_applied += 1
                print(f'  NEW FILL: {inst} -> {frole}')

        # Apply UPGRADES (replace existing cell with higher-confidence version)
        for (ui, urole, uval) in UPGRADES:
            if inst == ui:
                r[urole] = uval
                upgrades_applied += 1
                print(f'  UPGRADE: {inst} -> {urole}')

        # Apply NOT FOUND audit trails (only for EMPTY cells)
        if inst in NOT_FOUND:
            for role, val in NOT_FOUND[inst].items():
                current = r.get(role, '').strip()
                if not current:
                    r[role] = val
                    notfound_applied += 1
                    print(f'  NOT FOUND: {inst} -> {role} documented')

    print(f'\nSummary: {new_fills_applied} new fills, {upgrades_applied} upgrades, {notfound_applied} NOT FOUND audit trails')

    # Write enriched v5.16
    with open(ENRICHED_DST, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f'Wrote enriched CSV: {ENRICHED_DST}')

    # Compute coverage stats
    filled = 0
    notfound = 0
    empty = 0
    total = len(rows) * 7
    coverage_dist = {}
    for r in rows:
        cnt = 0
        for role in ROLE_COLS:
            v = r.get(role, '')
            if v and 'NOT FOUND' not in v:
                cnt += 1
                filled += 1
            elif v and 'NOT FOUND' in v:
                notfound += 1
            else:
                empty += 1
        coverage_dist[cnt] = coverage_dist.get(cnt, 0) + 1

    print(f'\n=== v5.16 Coverage Stats ===')
    print(f'Total rows: {len(rows)}')
    print(f'Total target roles: {total}')
    print(f'Filled: {filled} ({filled/total*100:.1f}%)')
    print(f'NOT FOUND entries: {notfound}')
    print(f'Empty cells: {empty}')
    print(f'Coverage distribution (roles per inst):')
    for k in sorted(coverage_dist.keys(), reverse=True):
        print(f'  {k}/7: {coverage_dist[k]} institutions')

    return rows, coverage_dist, filled, total, notfound, empty


def update_master(rows):
    """Update the master CSV (role-column schema) — mirror the new fills, upgrades, and NOT FOUND entries."""
    with open(MASTER_SRC, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        m_fieldnames = reader.fieldnames
        m_rows = list(reader)
    print(f'\nLoaded master CSV: {len(m_rows)} rows')

    # Build a lookup of changed institutions from the enriched rows
    changed = {}
    for r in rows:
        inst = r['Institution_Name']
        changed[inst] = {role: r[role] for role in ROLE_COLS}

    updated = 0
    for m in m_rows:
        inst = m['Institution_Name']
        if inst in changed:
            for role in ROLE_COLS:
                if role in m and changed[inst][role] and m[role] != changed[inst][role]:
                    # Only update if master cell differs (new fill, upgrade, or newly-documented NOT FOUND)
                    m[role] = changed[inst][role]
                    updated += 1
    print(f'Master CSV: {updated} cells updated')

    with open(MASTER_SRC, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=m_fieldnames)
        writer.writeheader()
        writer.writerows(m_rows)
    print(f'Wrote master CSV: {MASTER_SRC}')


if __name__ == '__main__':
    rows, coverage_dist, filled, total, notfound, empty = update_csv()
    update_master(rows)
    print('\n=== v5.16 update complete ===')

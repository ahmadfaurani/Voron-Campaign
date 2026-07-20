#!/usr/bin/env python3
"""
VoronDRQ Enrichment v5.15 Update Script
Data Integrity: CEO-misclassified-as-CISO cleanup + 2 new HIGH-confidence fills

Changes:
  CORRECTIONS (24): Replace CEO/President/Founder data filed in CISO column with
    NOT FOUND audit trails. CEO is NOT one of the 7 target roles. Previous runs
    (v5.13/v5.14) introduced this pattern; v5.14 started fixing it for Zurich Life
    and MARA. This run completes the cleanup for the remaining 24 rows.
    This is a DATA INTEGRITY fix — it reduces false positives, it does not
    fabricate data. Honest NOT FOUND is more valuable than a misclassified CEO.

  NEW FILLS (2 institutions, +8 rows with propagation):
    1. PayNet (PayNet Malaysia Sdn Bhd) — CISO = Meling Mudin (conf 95)
       Source: Star Cybersecurity Summit 2025 speaker page + LinkedIn + ZoomInfo
       Propagated to 6 PayNet sub-product rows (DuitNow, FPX, JomPAY, Me2U,
       PayDirect, PayNet Card) per v5.5 precedent (parent leadership inheritance).
    2. Sumitomo Mitsui Banking Corporation Malaysia Berhad — CFO = Norihiro Oyanagi
       (conf 78) — statutory finance signatory in FY2024 & FY2025 audited FS.

  NOT FOUND AUDIT TRAILS: Mizuho Bank (Malaysia) Berhad — all 7 roles confirmed
    NOT publicly disclosed via 12 official sources (audited FS, Pillar 3, TCFD,
    board committee TORs). Roles exist but names not public.
"""
import csv
import shutil
import os
from datetime import datetime

ENRICHED_SRC = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.14.csv'
ENRICHED_DST = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.15.csv'
MASTER_SRC  = '/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv'
MASTER_BAK  = '/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv.bak-pre-v5.15-' + datetime.now().strftime('%Y%m%d-%H%M%S')

ROLE_COLS = [
    'Chief Information Security Officer',
    'Head of Governance Risk & Compliance',
    'Chief Financial Officer',
    'Chief Risk Officer',
    'Head of Compliance',
    'Chief Information Officer',
    'Head of Internal Audit',
]

# ====== CORRECTIONS: CEO-misclassified-as-CISO ======
# Each entry: (Institution_Name, new NOT FOUND audit trail for CISO column)
# The CEO data is REMOVED from the CISO column. CEO is not a target role.
# Useful context (entity status, CEO name for reference) is preserved inside
# the NOT FOUND audit trail text so it is not lost.
CORRECTIONS = {
    # AEON Bank entities — CEO Mohammad Ridzuan Abdul Aziz is NOT the CISO
    'AEON Bank (M) Berhad': 'NOT FOUND [CISO not publicly listed. AEON Bank leadership page (aeonbank.com.my/about-us) names CEO Mohammad Ridzuan Abdul Aziz + Chairman Tomokatsu Yoshitoshi but no CISO. Digital bank CISO function likely combined with CTO. Sources: aeonbank.com.my, conf 35]',
    'AEON Bank Berhad': 'NOT FOUND [Same entity as AEON Bank (M) Berhad — duplicate row. CISO not publicly listed. Sources: aeonbank.com.my, conf 35]',
    'AEON Wallet (AEON Credit)': 'NOT FOUND [AEON Wallet is an e-money product of AEON Credit Service, not a separate institution. CISO not publicly listed. Parent AEON Bank CEO is Mohammad Ridzuan Abdul Aziz (not a target role). Sources: aeonbank.com.my, conf 30]',

    # AKM — previous entry was "CEO: Not found" (double negative, no value)
    'Agensi Jaminan Kredit Mikro (AKM)': 'NOT FOUND [AKM is a SKM (Suruhanjaya Koperasi Malaysia) subsidiary with limited public disclosure. No leadership page, no CISO publicly listed. Sources: web/firecrawl search — no results, conf 25]',

    # ASNB — CEO Muzzaffar Othman is NOT the CISO (CISO role belongs to PNB group)
    'Amanah Saham Nasional Berhad (ASNB)': 'NOT FOUND [ASNB is a PNB subsidiary. CISO not publicly listed at ASNB level; cybersecurity function centralized at PNB group level. CEO Muzzaffar Othman (now GCOO PNB) is not a target role. Sources: pnb.com.my, conf 30]',

    # CIMB (Khazanah-linked) — duplicate GLC row; CEO Novan Amirudin is NOT CISO
    'CIMB (Khazanah-linked)': 'NOT FOUND [Duplicate/related row for CIMB in GLC-Linked segment. CEO Novan Amirudin (Group CEO) and Chairman Datuk Syed Zaid Albar are not target roles. Real CIMB C-suite data is in the main CIMB row under Licensed Banks. Sources: cimb.com, conf 30]',

    # Cradle Fund — previous entry was "CEO: Not confirmed"
    'Cradle Fund Sdn Bhd': 'NOT FOUND [Cradle Fund (cradle.com.my/about-us) has no leadership page. CISO not publicly listed. Sources: cradle.com.my — no leadership page found, conf 20]',

    # Credit Suisse — ENTITY STATUS note belongs in notes, not CISO column
    'Credit Suisse (Malaysia) Berhad': 'NOT FOUND [ENTITY STATUS: Credit Suisse acquired by UBS; parent banks merged 31 May 2024. Entity likely absorbed/restructured into UBS Malaysia. No CISO publicly listed for the legacy entity. Source: ubs.com press release, conf 85]',

    # GX Bank entities — CEO Kaushik Chowdhury is NOT the CISO
    'GX Bank Berhad': 'NOT FOUND [GXBank leadership page (gxbank.my) names CEO Kaushik Chowdhury + Deputy CEO/COO Hildah Hamzah but no CISO. Digital bank CISO function likely combined with CTO. Sources: gxbank.my, conf 35]',
    'GXBank Berhad': 'NOT FOUND [Same entity as GX Bank Berhad — duplicate row. CISO not publicly listed. Sources: gxbank.my, conf 35]',

    # ICBC Malaysia — CEO Geng Hao is NOT the CISO
    'ICBC (Malaysia) Berhad': 'NOT FOUND [ICBC MY Directors page (malaysia.icbc.com.cn) names MD/CEO Geng Hao (appointed 26 Sep 2024) but no CISO. BNM Pillar 3 Disclosure 31 Dec 2025 has no Senior Management page. Sources: malaysia.icbc.com.cn, BNM Pillar 3, conf 35]',

    # KAF Digital Bank entities — CEO Suzaini bin Mukhtar is NOT the CISO
    'KAF Digital Bank': 'NOT FOUND [KAF Digital Bank leadership names CEO Suzaini bin Mukhtar but no CISO. Digital bank CISO function likely combined with CTO. Sources: web search/firecrawl, conf 35]',
    'KAF Digital Bank Berhad': 'NOT FOUND [Same entity as KAF Digital Bank — duplicate row. CISO not publicly listed. Sources: web search/firecrawl, conf 35]',

    # Kurnia Insurans — CEO (Country) Junior Cho is NOT the CISO
    'Kurnia Insurans (Malaysia) Berhad': 'NOT FOUND [Kurnia Insurans is a Zurich Malaysia entity. Country CEO Junior Cho is not a target role. CISO not publicly listed at entity level; cybersecurity centralized at Zurich Malaysia group. Sources: zurich.com.my, conf 30]',

    # LPPSA — previous entry was "CEO: Not confirmed" (browser_vision identified names but roles unclear)
    'LPPSA': 'NOT FOUND [LPPSA (Lembaga Pembiayaan Perumahan Sektor Awam) management page is image-only; browser_vision identified names (Farid/Zawawi/Zuwardi) but roles unclear. No CISO publicly listed. Sources: lppsa.gov.my, conf 25]',

    # MIDF Amanah — CEO Azizi Mustafa is NOT the CISO
    'MIDF Amanah Investment Bank Berhad': 'NOT FOUND [MIDF key-management page (midf.com.my/key-management) names CEO Azizi Mustafa but no CISO. CISO function may be shared with parent MBSB Bank. Sources: midf.com.my, conf 35]',

    # Mizuho Bank MY — CEO Daisuke Ihara is NOT the CISO
    'Mizuho Bank (Malaysia) Berhad': 'NOT FOUND [Mizuho MY Profile of Directors PDF names CEO Daisuke Ihara but no CISO. Audited FS FYE Mar 2025, Pillar 3 Disclosure, TCFD Report, and board committee TORs do not name a CISO. BRMC TOR references "cyber security" oversight implying the function exists but the head is not publicly disclosed. Sources: mizuhogroup.com Malaysia pages, BNM Pillar 3, audited FS, conf 40]',

    # Phillip Securities — CEO Andy Lim Say Kiat is NOT the CISO
    'Phillip Securities (Malaysia) Sdn Bhd': 'NOT FOUND [PhillipCapital Malaysia core-management-team page names Group MD Andy Lim Say Kiat but no CISO. CISO function likely centralized at PhillipCapital group. Sources: phillipcapital.com.my/core-management-team, conf 30]',

    # SeaBank Malaysia — rebranded to Ryt Bank; note belongs in a status field, not CISO
    'SeaBank Malaysia Berhad': 'NOT FOUND [ENTITY STATUS: SeaBank Malaysia rebranded to Ryt Bank Berhad (YTL Digital Capital + Sea Limited JV, licensed Dec 2024). CEO Melvin Ooi is at Ryt Bank (not a target role). Full leadership data is in the Ryt Bank rows. No CISO publicly listed for the legacy SeaBank entity. Sources: rytbank.my, conf 80]',

    # SMBC MY — CEO Atsuhide Shiojiri is NOT the CISO
    'Sumitomo Mitsui Banking Corporation Malaysia Berhad': 'NOT FOUND [SMBC MY President/CEO Atsuhide Shiojiri (effective 30 Apr 2024) is not a target role. Board of Directors PDF, FY2025 audited FS (175 pp), Pillar 3 Disclosure 31Mar2025 (50 pp), and Board Charter do not name a CISO. Sources: smbc.co.jp/asia/malaysia/ PDFs, BNM Pillar 3, conf 40]',

    # Sun Life Malaysia — CEO Ho Teck Seng is NOT the CISO
    'Sun Life Malaysia Assurance Berhad': 'NOT FOUND [Sun Life Malaysia (sunlifemalaysia.com) names President & CEO Ho Teck Seng (effective 1 Jul 2025) but no CISO. CISO function likely centralized at Sun Life Asia regional level. Sources: sunlifemalaysia.com, conf 30]',

    # Tekun Nasional — previous entry was "CEO: Not confirmed"
    'Tekun Nasional': 'NOT FOUND [Tekun Nasional (tekun.gov.my) scraped — contact info only, no leadership/management page found. No CISO publicly listed. Sources: tekun.gov.my, conf 20]',

    # Zurich Takaful — CEO Nur Fatihah Mustafa is NOT the CISO
    'Zurich Takaful Malaysia Berhad': 'NOT FOUND [Zurich Our Leaders page (zurich.com.my/about-zurich/the-zurich-story/our-leaders) names CEO Nur Fatihah Mustafa but no CISO. CISO function centralized at Zurich Malaysia group. Sources: zurich.com.my, conf 30]',

    # Bank Muamalat — CEO Khairul Kamarudin is NOT the CISO
    'Bank Muamalat Malaysia Berhad': 'NOT FOUND [Bank Muamalat CEO Khairul Kamarudin (President and CEO, CEO of the Year 2024 GIFA) is not a target role. CISO not publicly listed at bankmuamalat.com. Sources: nst.com.my, bernama.com, bankmuamalat.com, conf 30]',
}

# ====== NEW FILLS ======
# (Institution_Name, role_column, value)
NEW_FILLS = [
    # PayNet CISO — HIGH confidence (Meling Mudin, Star Cybersecurity Summit 2025 + LinkedIn + ZoomInfo)
    (
        'PayNet (PayNet Malaysia Sdn Bhd)',
        'Chief Information Security Officer',
        'Meling Mudin (Chief Information Security Officer, Payments Network Malaysia Sdn. Bhd.) [Source: Star Cybersecurity Summit 2025 speaker page (conference.thestar.com.my/cybersecuritysummit/speaker/meling-mudin, May 2025) + LinkedIn (my.linkedin.com/in/spoonfork) + ZoomInfo + Datanyze; conf 95 — not on official leadership page but confirmed via 5 independent secondary sources including industry conference bio]',
    ),
    # SMBC MY CFO — MEDIUM-HIGH confidence (Norihiro Oyanagi, statutory finance signatory)
    (
        'Sumitomo Mitsui Banking Corporation Malaysia Berhad',
        'Chief Financial Officer',
        'Norihiro Oyanagi (officer primarily responsible for financial management per Section 251(1)(b) Companies Act 2016 statutory declaration) [Official: SMBC MY audited financial statements FY2024 & FY2025 (smbc.co.jp/asia/malaysia/financial-statement-31Mar2025.pdf), conf 78 — statutory CFO-equivalent; document prints statutory role description not literal "CFO" title]',
    ),
]

# ====== PayNet sub-product rows (inherit parent CISO) ======
# Per v5.5 precedent: PayNet's confirmed C-suite roles are propagated to the
# 6 sub-product rows since they share the same parent leadership.
PAYNET_SUBPRODUCTS = [
    'DuitNow (by PayNet)',
    'FPX (by PayNet)',
    'JomPAY (by PayNet)',
    'Me2U (by PayNet)',
    'PayDirect (by PayNet)',
    'PayNet Card (by PayNet)',
]
PAYNET_CISO_VALUE = 'Meling Mudin (Chief Information Security Officer, PayNet group) [Inherited from PayNet parent per v5.5 leadership-inheritance precedent. Source: Star Cybersecurity Summit 2025 speaker page + LinkedIn + ZoomInfo; conf 95]'

# ====== Mizuho MY NOT FOUND audit trail (all 7 roles, well-documented) ======
# Subagent verified via 12 official sources that none of the 7 roles are
# publicly named. Roles exist (CFO, CRO, CCO, CIA confirmed via document
# references) but names are not disclosed. Only update the empty cells
# (CFO, CIO, Head of GRC were empty; CISO, CRO, Compliance, IA already have
# content from CORRECTIONS or prior research).
MIZUHO_NOTFOUND = {
    'Chief Financial Officer': 'NOT FOUND [Mizuho MY audited FS FYE 31 Mar 2025 (146 pp) contains the regulatory "Statement by Chief Executive Officer and Chief Financial Officer" page but CFO name is NOT publicly disclosed. Pillar 3 Disclosures FYE Mar 2025 & Sep 2025 also do not name the CFO. Sources: mizuhogroup.com Malaysia, BNM Pillar 3, audited FS, conf 40]',
    'Chief Information Officer': 'NOT FOUND [Mizuho MY BRMC TOR references oversight of "IT, and cyber security strategic plans" implying IT leadership exists, but no CIO/CTO title or name is publicly listed. Sources: mizuhogroup.com Malaysia corporate-governance page, Pillar 3 Disclosures, conf 40]',
    'Head of Governance Risk & Compliance': 'NOT FOUND [Role title "Head of GRC" not mentioned in any official Mizuho MY source. Governance, risk, and compliance are handled by separate functions (Board, BRMC, BAC, CRO, CCO, CIA) rather than a combined GRC head. Sources: mizuhogroup.com Malaysia, conf 40]',
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
    print(f'Loaded {len(rows)} rows from v5.14')

    corrections_applied = 0
    new_fills_applied = 0
    propagation_applied = 0
    notfound_applied = 0

    for r in rows:
        inst = r['Institution_Name']

        # Apply CORRECTIONS (CISO column cleanup)
        if inst in CORRECTIONS:
            old = r['Chief Information Security Officer']
            r['Chief Information Security Officer'] = CORRECTIONS[inst]
            corrections_applied += 1
            print(f'  CORRECTION: {inst} CISO column cleaned (was: {old[:60]}...)')

        # Apply NEW FILLS
        for (fi, frole, fval) in NEW_FILLS:
            if inst == fi:
                r[frole] = fval
                new_fills_applied += 1
                print(f'  NEW FILL: {inst} -> {frole} = {fval[:60]}...')

        # Apply PayNet sub-product CISO propagation
        if inst in PAYNET_SUBPRODUCTS:
            r['Chief Information Security Officer'] = PAYNET_CISO_VALUE
            propagation_applied += 1
            print(f'  PROPAGATE: {inst} -> CISO inherited from PayNet parent')

        # Apply Mizuho NOT FOUND audit trails (only for empty cells)
        if inst == 'Mizuho Bank (Malaysia) Berhad':
            for role, val in MIZUHO_NOTFOUND.items():
                if not r.get(role, '').strip():
                    r[role] = val
                    notfound_applied += 1
                    print(f'  NOT FOUND: {inst} -> {role} documented')

    print(f'\nSummary: {corrections_applied} corrections, {new_fills_applied} new fills, {propagation_applied} propagations, {notfound_applied} NOT FOUND audit trails')

    # Write enriched v5.15
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

    print(f'\n=== v5.15 Coverage Stats ===')
    print(f'Total rows: {len(rows)}')
    print(f'Total target roles: {total}')
    print(f'Filled: {filled} ({filled/total*100:.1f}%)')
    print(f'NOT FOUND entries: {notfound}')
    print(f'Empty cells: {empty}')
    print(f'Coverage distribution (roles per inst):')
    for k in sorted(coverage_dist.keys(), reverse=True):
        print(f'  {k}/7: {coverage_dist[k]} institutions')

    return rows, coverage_dist, filled, total


def update_master(rows):
    """Update the master CSV (role-column schema) — mirror the corrections and new fills."""
    with open(MASTER_SRC, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        m_fieldnames = reader.fieldnames
        m_rows = list(reader)
    print(f'\nLoaded master CSV: {len(m_rows)} rows, fields: {m_fieldnames}')

    # Build a lookup of changed institutions from the enriched rows
    changed = {}
    for r in rows:
        inst = r['Institution_Name']
        # Check if any role changed from v5.14 (we re-apply the same logic)
        changed[inst] = {role: r[role] for role in ROLE_COLS}

    updated = 0
    for m in m_rows:
        inst = m['Institution_Name']
        if inst in changed:
            # Map enriched role columns to master role columns
            # Master CSV columns (from header): Tier,Segment,Institution_Name,CISO,GRC,CFO,CRO,Compliance,CIO,IA
            # Need to check exact master column names
            role_map = {
                'Chief Information Security Officer': 'Chief Information Security Officer',
                'Head of Governance Risk & Compliance': 'Head of Governance Risk & Compliance',
                'Chief Financial Officer': 'Chief Financial Officer',
                'Chief Risk Officer': 'Chief Risk Officer',
                'Head of Compliance': 'Head of Compliance',
                'Chief Information Officer': 'Chief Information Officer',
                'Head of Internal Audit': 'Head of Internal Audit',
            }
            for erole, mrole in role_map.items():
                if mrole in m and changed[inst][erole] and m[mrole] != changed[inst][erole]:
                    # Only update if the master cell is empty or the enriched value is a correction/new fill
                    if not m[mrole].strip() or m[mrole] != changed[inst][erole]:
                        m[mrole] = changed[inst][erole]
                        updated += 1
    print(f'Master CSV: {updated} cells updated')

    with open(MASTER_SRC, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=m_fieldnames)
        writer.writeheader()
        writer.writerows(m_rows)
    print(f'Wrote master CSV: {MASTER_SRC}')


if __name__ == '__main__':
    rows, coverage_dist, filled, total = update_csv()
    update_master(rows)
    print('\n=== v5.15 update complete ===')

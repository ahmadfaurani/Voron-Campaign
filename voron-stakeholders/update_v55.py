#!/usr/bin/env python3
"""VoronDRQ Enrichment v5.5 - update script.
Updates v5.4 enriched CSV with new findings from 3 parallel subagents:
- Workstream 1: SEDC Sarawak (5 new roles) + flags for PNB Income Fund (non-existent), Maybank Khazanah-linked (duplicate), Khazanah (2 missing roles confirmed not public)
- Workstream 2: MSBs/Fintech - 0 target roles found, Money Match Sdn Bhd flagged as duplicate
- Workstream 3: PayNet products (6 x 2 inherited roles = 12 new cells) + 2 investment banks flagged non-existent
Total new cells: 17
Classification: TLP:AMBER
"""
import csv
import shutil
from datetime import datetime

SRC = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.4.csv'
DST = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.5.csv'

STAKEHOLDER_COLS = [
    'Chief Information Security Officer',
    'Head of Governance Risk & Compliance',
    'Chief Financial Officer',
    'Chief Risk Officer',
    'Head of Compliance',
    'Chief Information Officer',
    'Head of Internal Audit',
]

# Read source
with open(SRC, 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

print(f'Loaded {len(rows)} rows from v5.4')

# Helper: update a cell with new value + source/conf note
def set_cell(row, col, value):
    if col not in STAKEHOLDER_COLS:
        raise ValueError(f'Unknown column: {col}')
    row[col] = value

# Helper: add a note to an existing cell (for non-target role notes or flags)
def append_note(row, col, note):
    existing = row.get(col, '').strip()
    if existing:
        row[col] = existing + ' | ' + note
    else:
        row[col] = note

# === UPDATES ===
updates_log = []

# 1. SEDC Sarawak (Sarawak State Financial Corporation entry) -> 5 new roles
SEDC_SOURCE = 'https://sedc.com.my/leadership-team/ , https://sedc.com.my/management-team/'
for row in rows:
    name = row.get('Institution_Name', '')
    if name.strip() == 'Sarawak State Financial Corporation (SSFC)':
        # Add entity correction note in CISO column (as a non-target note marker, since CISO is empty)
        set_cell(row, 'Chief Financial Officer',
                 'Encik Leo Lanaiwong (Group Chief Financial Officer) [Official: sedc.com.my/leadership-team/, conf 95]')
        set_cell(row, 'Chief Risk Officer',
                 'Cik Khartini Johari (Head, Group Integrity and Risk Management) [Official: sedc.com.my/management-team/, conf 95]')
        set_cell(row, 'Head of Governance Risk & Compliance',
                 'Cik Khartini Johari (Head, Group Integrity and Risk Management) [Official: sedc.com.my/management-team/, conf 95]')
        set_cell(row, 'Head of Internal Audit',
                 'Encik Yap Yien Chiang (Head, Group Internal Audit) [Official: sedc.com.my/management-team/, conf 95]')
        set_cell(row, 'Chief Information Officer',
                 'Tuan Haji Nor Azlan Husaini (Acting Head, Group Digital & Technology) [Official: sedc.com.my/management-team/, conf 95]')
        # Add entity-name correction note in empty CISO cell
        set_cell(row, 'Chief Information Security Officer',
                 'NOT FOUND [Entity correction: DB entry "Sarawak State Financial Corporation" maps to Sarawak Economic Development Corporation (SEDC) - sedc.com.my. sfc.sarawak.gov.my is Sarawak Forestry Corporation (wrong entity). CISO not listed on official SEDC site.]')
        updates_log.append(('SEDC Sarawak', 5))
        break

# 2. PayNet products - 6 entries, each inherits CFO + CTO from PayNet
PAYNET_PRODUCTS = {
    'DuitNow (by PayNet)': 85,
    'FPX (by PayNet)': 85,
    'JomPAY (by PayNet)': 85,
    'Me2U (by PayNet)': 80,  # caveat - Me2U not on official PayNet services list
    'PayDirect (by PayNet)': 85,
    'PayNet Card (by PayNet)': 85,
}

for row in rows:
    name = row.get('Institution_Name', '').strip()
    if name in PAYNET_PRODUCTS:
        conf = PAYNET_PRODUCTS[name]
        caveat = ''
        if name == 'Me2U (by PayNet)':
            caveat = ' CAVEAT: Me2U not listed on official PayNet 10 named services; may be Maybank2u feature mislabeled.'
        if name == 'PayDirect (by PayNet)':
            set_cell(row, 'Chief Financial Officer',
                     f'Tan Wei Tze (Chief Financial Officer, PayNet) [PayNet leadership - PayDirect = PayNet "DirectDebit" service, inherited, conf {conf}]')
            set_cell(row, 'Chief Information Officer',
                     f'Teh Lip Guan (Chief Technology Officer, PayNet) [PayNet leadership - PayDirect = PayNet "DirectDebit" service, inherited, conf {conf}]')
        elif name == 'PayNet Card (by PayNet)':
            set_cell(row, 'Chief Financial Officer',
                     f'Tan Wei Tze (Chief Financial Officer, PayNet) [PayNet leadership - PayNet Card = PayNet "MyDebit" domestic debit card scheme, inherited, conf {conf}]')
            set_cell(row, 'Chief Information Officer',
                     f'Teh Lip Guan (Chief Technology Officer, PayNet) [PayNet leadership - PayNet Card = PayNet "MyDebit" domestic debit card scheme, inherited, conf {conf}]')
        else:
            set_cell(row, 'Chief Financial Officer',
                     f'Tan Wei Tze (Chief Financial Officer, PayNet) [PayNet leadership - {name.split(" (")[0]} is a PayNet product, inherited, conf {conf}{caveat}]')
            set_cell(row, 'Chief Information Officer',
                     f'Teh Lip Guan (Chief Technology Officer, PayNet) [PayNet leadership - {name.split(" (")[0]} is a PayNet product, inherited, conf {conf}{caveat}]')
        updates_log.append((name, 2))

# 3. PayNet parent - update existing CFO/CTO with corrected CEO context note
for row in rows:
    name = row.get('Institution_Name', '').strip()
    if name == 'PayNet (PayNet Malaysia Sdn Bhd)':
        # Existing CFO and CIO cells already have correct data. Add a note about CEO correction in CISO cell.
        set_cell(row, 'Chief Information Security Officer',
                 'NOT FOUND [Function exists per PayNet Committees page: "CISO Office" reporting to Group Risk Committee. Name not on official leadership page. NOTE: PayNet CEO = Praveen Rajan (NOT Suhaila Kamaruddin as in some briefs); CCO = Azrul Fakhzan Mainor; CPO = Shafenaz Farouk.]')
        updates_log.append(('PayNet parent (CISO note + CEO correction)', 0))
        break

# 4. Duplicate flags - Maybank (Khazanah-linked) and Money Match Sdn Bhd
for row in rows:
    name = row.get('Institution_Name', '').strip()
    if name == 'Maybank (Khazanah-linked)':
        set_cell(row, 'Chief Information Security Officer',
                 'DUPLICATE OF MAYBANK BERHAD [Already at 7/7 in DB. This "Khazanah-linked" entry is the same entity (Khazanah holds ~11.5% of Maybank). Recommend removing row or marking as duplicate. Do NOT re-research.]')
        updates_log.append(('Maybank (Khazanah-linked)', 0))
        break

for row in rows:
    name = row.get('Institution_Name', '').strip()
    if name == 'Money Match Sdn Bhd':
        set_cell(row, 'Chief Information Security Officer',
                 'DUPLICATE OF MONEYMATCH SDN BHD [Correct spelling "MoneyMatch Sdn Bhd" already in DB at 4/7. This entry (with space) is the same entity. Recommend removing row or marking as duplicate. Founders: Adrian Tan, Nikki Yeo (moneymatch.co/about-us).]')
        updates_log.append(('Money Match Sdn Bhd (duplicate flag)', 0))
        break

# 5. Non-existent flags - PNB Income Fund, Malaysia International Islamic Bank IB, JCL Corporation
for row in rows:
    name = row.get('Institution_Name', '').strip()
    if name == 'PNB Income Fund Berhad':
        set_cell(row, 'Chief Information Security Officer',
                 'ENTITY LIKELY NON-EXISTENT [No evidence on pnb.com.my or ASNB fund listing (18 unit trust funds, none named "PNB Income Fund"). PNB Capital and PNB Equity Fund previously confirmed non-existent. Recommend removal or marking as non-existent.]')
        updates_log.append(('PNB Income Fund Berhad (non-existent flag)', 0))
        break

for row in rows:
    name = row.get('Institution_Name', '').strip()
    if name == 'Malaysia International Islamic Bank IB':
        set_cell(row, 'Chief Information Security Officer',
                 'ENTITY NON-EXISTENT [No match on BNM licensed Islamic banks list (Bank Islam, Bank Muamalat, Maybank Islamic, CIMB Islamic, RHB Islamic, Hong Leong Islamic, AmIslamic, Affin Islamic, Public Bank Islamic, KFH, Bank Rakyat, Agrobank). No BNM/Bursa/SSM record. Likely mislabel or placeholder.]')
        updates_log.append(('Malaysia International Islamic Bank IB (non-existent flag)', 0))
        break

for row in rows:
    name = row.get('Institution_Name', '').strip()
    if name == 'JCL Corporation Sdn Bhd':
        set_cell(row, 'Chief Information Security Officer',
                 'ENTITY NON-EXISTENT AS LICENSED INVESTMENT BANK [No match on BNM licensed investment banks list (CIMB IB, Maybank IB, RHB IB, Kenanga IB, AmInvestment, Affin Hwang, Hong Leong IB, Public IB, M&A Securities, KAF IB). No Bursa/SSM record. Likely mislabel or placeholder.]')
        updates_log.append(('JCL Corporation Sdn Bhd (non-existent flag)', 0))
        break

# 6. Researched but no target roles - add notes to key institutions
# PDC (Penang)
for row in rows:
    name = row.get('Institution_Name', '').strip()
    if name == 'Penang State Development Corporation (PSDC)':
        set_cell(row, 'Chief Information Security Officer',
                 'NOT FOUND [Entity correction: correct name is Penang Development Corporation (PDC) - pdc.gov.my. CEO confirmed: Dato\' Abdul Latiff bin Abd Aziz (pdc.gov.my, conf 95). Org chart is JPEG image (not text-extractable). 0/7 target roles - management team not publicly listed.]')
        updates_log.append(('PDC Penang (entity correction + 0/7 note)', 0))
        break

# Sabah SCC
for row in rows:
    name = row.get('Institution_Name', '').strip()
    if name == 'Sabah State Financial Corporation (SSFC)':
        set_cell(row, 'Chief Information Security Officer',
                 'NOT FOUND [Entity likely = Sabah Credit Corporation (SCC). Both ykn.sabah.gov.my and scc.sabah.gov.my DNS-fail. Chairman: Datuk Rusdin Riman (news, conf 65) / Datuk Seri Dr. Yee Moh Chai (LinkedIn, conf 70, conflicting). CEO: Datuk George Taitim Tulas (news, conf 65). 0/7 target roles - official site unreachable.]')
        updates_log.append(('Sabah SCC (0/7 note)', 0))
        break

# Iskandar Waterfront City
for row in rows:
    name = row.get('Institution_Name', '').strip()
    if name == 'Iskandar Waterfront City':
        set_cell(row, 'Chief Information Security Officer',
                 'NOT FOUND [Small Bursa-listed property developer (code 8256-A, iwcity.com.my). Management team confirmed: Executive Vice Chairman Tan Sri Dato\' Lim Kang Hoo, Executive Director Mr Lim Chen Herng, COO Mr Lim Fang Ching (iwcity.com.my, conf 95). 0/7 target C-suite roles - small developer, no dedicated CFO/CRO/CISO/CIO/Compliance/IA/GRC.]')
        updates_log.append(('Iskandar Waterfront City (0/7 note)', 0))
        break

# Khazanah - 2 missing roles confirmed not public
for row in rows:
    name = row.get('Institution_Name', '').strip()
    if name == 'Khazanah Nasional Berhad':
        # Don't overwrite existing 5 cells. Just add note to CISO cell.
        if not row.get('Chief Information Security Officer', '').strip():
            set_cell(row, 'Chief Information Security Officer',
                     'NOT FOUND [Not listed on official khazanah.com.my leadership pages (22+ executives listed). Likely internal position not publicly disclosed. ARC (Audit & Risk Committee) at board level: Chairman Wong Kang Hwee.]')
        if not row.get('Head of Internal Audit', '').strip():
            set_cell(row, 'Head of Internal Audit',
                     'NOT FOUND [Not listed on official khazanah.com.my. ARC oversees internal/external auditors at board level but Head of IA not publicly named. Likely internal position.]')
        updates_log.append(('Khazanah (2 missing roles confirmed not public)', 0))
        break

# MSBs/Fintech with 0/7 - add brief notes for the ones researched
MSB_NOTES = {
    '2C2P (Malaysia) Sdn Bhd': 'NOT FOUND [Parent: Ant Group (acquired 2C2P Apr 2022). Founder: Aung Kyaw Moe (Wikipedia, conf 85, non-target). 2c2p.com has no leadership section. 0/7 target roles.]',
    'CurrencyFair (Malaysia) Sdn Bhd': 'NOT FOUND [Parent: CurrencyFair (Irish). CEO Brett Meyers (Wikipedia, conf 85, non-target). currencyfair.com has no leadership names. No Malaysia office listed. 0/7 target roles.]',
    'G2G Online (Malaysia) Sdn Bhd': 'NOT FOUND [Malaysian MSB licensee; distinct from g2g.com gaming marketplace. No public leadership information. 0/7 target roles.]',
    'I.Destinasi Sdn Bhd (IDSB)': 'NOT FOUND [Malaysian MSB licensee. No public leadership information. 0/7 target roles.]',
    'Jirnexu (M) Sdn Bhd': 'NOT FOUND [Operates RinggitPlus.com and CompareHero. Founded 2012 KL. ringgitplus.com DNS-fails (Cloudflare 1016). Founders (Ramanuja/Rohit Maheshwari) reported but unverified (conf 50). 0/7 target roles.]',
    'KDI Save Sdn Bhd': 'NOT FOUND [Fintech under KDI Group. No public leadership information. 0/7 target roles.]',
    'Soft Space Sdn Bhd': 'NOT FOUND [Malaysian fintech (softspace.com.my). CSO & co-founder Chris Leong (Jelawang Capital interview, conf 90, non-target). CEO Justin Chew reported but unverified. 0/7 target roles.]',
    'Stripe Payments Malaysia Sdn Bhd': 'NOT FOUND [Parent: Stripe Inc. Global CEO Patrick Collison, President John Collison, CPO Rob McIntosh, Board Mark Carney (Wikipedia, conf 85, all non-target). stripe.com has no Malaysia-specific leadership. 0/7 target roles.]',
}
for row in rows:
    name = row.get('Institution_Name', '').strip()
    if name in MSB_NOTES:
        # Only add note if CISO cell is empty (avoid overwriting real data)
        if not row.get('Chief Information Security Officer', '').strip():
            set_cell(row, 'Chief Information Security Officer', MSB_NOTES[name])
            updates_log.append((f'{name} (0/7 note)', 0))

# === Write v5.5 ===
with open(DST, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f'\nWrote {len(rows)} rows to v5.5')
print(f'\nUpdates applied ({len(updates_log)}):')
for name, count in updates_log:
    print(f'  - {name}: +{count} role(s)')

# === Coverage stats ===
def coverage_count(row):
    return sum(1 for c in STAKEHOLDER_COLS if row.get(c, '').strip() and not row.get(c, '').strip().startswith('NOT FOUND') and not row.get(c, '').strip().startswith('DUPLICATE') and not row.get(c, '').strip().startswith('ENTITY'))

# For coverage, a cell counts as "filled" if it has a real contact (not a NOT FOUND / DUPLICATE / ENTITY flag note)
from collections import defaultdict
buckets = defaultdict(int)
total_filled = 0
for row in rows:
    name = row.get('Institution_Name', '').strip()
    if not name:
        continue
    filled = 0
    for c in STAKEHOLDER_COLS:
        v = row.get(c, '').strip()
        if v and not v.startswith('NOT FOUND') and not v.startswith('DUPLICATE') and not v.startswith('ENTITY'):
            filled += 1
    buckets[filled] += 1
    total_filled += filled

print(f'\n=== Coverage Statistics v5.5 ===')
print(f'Total institutions: {sum(buckets.values())}')
print(f'Total roles found: {total_filled}')
print(f'Total possible: {sum(buckets.values()) * 7}')
print(f'Overall coverage: {total_filled / (sum(buckets.values()) * 7) * 100:.1f}%')
print(f'\nCoverage distribution:')
for k in sorted(buckets.keys()):
    print(f'  {k}/7: {buckets[k]}')

# Per-role completion
print(f'\nPer-role completion:')
for c in STAKEHOLDER_COLS:
    cnt = sum(1 for row in rows if row.get(c, '').strip() and not row.get(c, '').strip().startswith('NOT FOUND') and not row.get(c, '').strip().startswith('DUPLICATE') and not row.get(c, '').strip().startswith('ENTITY'))
    print(f'  {c}: {cnt}/{len(rows)} ({cnt/len(rows)*100:.1f}%)')

print(f'\n=== v5.5 file: {DST}')

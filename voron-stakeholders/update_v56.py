#!/usr/bin/env python3
"""VoronDRQ Enrichment v5.6 - update script.
Updates v5.5 enriched CSV with new findings from 3 parallel subagents researching
remaining 0/7 fintech institutions (payment gateways, e-wallets, niche e-money).

New roles added (7 cells across 5 institutions):
- Wallex Sdn Bhd: Head of Compliance = Dee Patria Adithana (parent M-DAQ, conf 80)
- Xendit Technologies (Malaysia) Sdn Bhd: CIO/CTO = Bo Chen (parent Xendit CTO, conf 80)
- BigPay Malaysia Sdn Bhd: CFO = Mun Hui Teh (parent Capital A CFO, conf 80)
- ShopeePay Malaysia Sdn Bhd: CFO = Tony Hou (parent Sea Limited CFO, conf 80)
- Setel by PETRONAS Dagangan Berhad: 3 roles (CFO, CIO/CTO, Head of IA from parent PDB, conf 80 each)

Audit notes added (4 institutions researched with 0 target roles):
- Billplz Sdn Bhd: CEO Nazroof Hakim confirmed (non-target); no public C-suite
- ToyyibPay Sdn Bhd: no leadership found at all
- GrabPay Malaysia Sdn Bhd: parent CEO/COO confirmed (non-target); CFO not verifiable (SEC EDGAR blocked)
- Razer Pay Malaysia Sdn Bhd: DEFUNCT (shut down 2021, domains expired) - flag for removal

Classification: TLP:AMBER
"""
import csv
from collections import defaultdict

SRC = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.5.csv'
DST = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.6.csv'

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

print(f'Loaded {len(rows)} rows from v5.5')

def set_cell(row, col, value):
    if col not in STAKEHOLDER_COLS:
        raise ValueError(f'Unknown column: {col}')
    row[col] = value

updates_log = []

# === NEW ROLES (7 cells) ===

# 1. Wallex Sdn Bhd - Head of Compliance (inherited from parent M-DAQ, Indonesia-based)
for row in rows:
    if row.get('Institution_Name', '').strip() == 'Wallex Sdn Bhd':
        set_cell(row, 'Head of Compliance',
                 'Dee Patria Adithana, GRCP (Legal & Compliance Counsel, M-DAQ Global - parent) [Official: wallex.asia/en-sg/about-us + LinkedIn id.linkedin.com/in/dee-patria-adithana, conf 80 - Indonesia-based, inherited to Wallex Malaysia entity. Wallex.com DNS-fails; correct domain wallex.asia. M-DAQ HQ Singapore, PJ Malaysia office.]')
        # Add note to CISO about research
        set_cell(row, 'Chief Information Security Officer',
                 'NOT FOUND [Wallex = M-DAQ Global cross-border payments brand. Parent CEO: Tan Choon Seng (Group CEO M-DAQ, conf 90). No CISO/CFO/CRO/CTO/IA/GRC publicly named at Wallex or M-DAQ. Only compliance counsel (Indonesia-based) found.]')
        updates_log.append(('Wallex Sdn Bhd', 1))
        break

# 2. Xendit Technologies (Malaysia) Sdn Bhd - CIO/CTO (inherited from parent Xendit)
for row in rows:
    if row.get('Institution_Name', '').strip() == 'Xendit Technologies (Malaysia) Sdn Bhd':
        set_cell(row, 'Chief Information Officer',
                 'Bo Chen (Chief Technology Officer, Xendit - parent) [Official: xendit.co/en/company/, conf 80 - inherited to Malaysia entity. Xendit acquired Payex (BNM-licensed) 2023, full acquisition 2025. Malaysia Country Manager: Jayson Poon (official press release Oct 2025, conf 98, non-target). GM Malaysia: Jason Siew (press release Sep 2025, conf 98, non-target). Parent CEO: Moses Lo, COO: Tessa Wijaya (non-target).]')
        set_cell(row, 'Chief Information Security Officer',
                 'NOT FOUND [Malaysia entity formed via Payex acquisition 2023-2025. No Malaysia-specific CISO/CFO/CRO/Compliance/IA/GRC publicly listed. Parent Xendit (Indonesia unicorn) CTO inherited for CIO/CTO role. Offices in Penang + KL, 4500+ MY businesses onboarded.]')
        updates_log.append(('Xendit Technologies (Malaysia) Sdn Bhd', 1))
        break

# 3. BigPay Malaysia Sdn Bhd - CFO (inherited from parent Capital A)
for row in rows:
    if row.get('Institution_Name', '').strip() == 'BigPay Malaysia Sdn Bhd':
        set_cell(row, 'Chief Financial Officer',
                 'Mun Hui Teh (Chief Financial Officer, Capital A Berhad - parent) [Official: capitala.com/corporate_leadership.html, conf 80 - inherited to BigPay. BigPay = Capital A (formerly AirAsia) fintech subsidiary, BNM-licensed e-money issuer. bigpayme.com has no leadership page. Capital A Deputy CEO Effendy Shahul Hamid oversees financial services portfolio (non-target). No BigPay-specific C-suite publicly published.]')
        set_cell(row, 'Chief Information Security Officer',
                 'NOT FOUND [No BigPay-specific or Capital A CISO/CRO/CTO/Compliance/IA/GRC publicly named. Capital A Chief Legal Officer Fiona Fong (non-target) may indirectly cover legal/compliance. Recommend approaching via Capital A investor relations.]')
        updates_log.append(('BigPay Malaysia Sdn Bhd', 1))
        break

# 4. ShopeePay Malaysia Sdn Bhd - CFO (inherited from parent Sea Limited)
for row in rows:
    if row.get('Institution_Name', '').strip() == 'ShopeePay Malaysia Sdn Bhd':
        set_cell(row, 'Chief Financial Officer',
                 'Tony Hou (Chief Financial Officer, Sea Limited - parent) [Official: sea.com/aboutus/leadership, conf 80 - inherited to ShopeePay Malaysia. ShopeePay = Monee (formerly SeaMoney, rebranded May 2025) digital financial services arm of Sea Limited. Malaysia Head: Alain Yee (Head of ShopeePay Malaysia + President AEMI 2026/27-2027/28, LinkedIn linkedin.com/company/shopeepay, conf 85, non-target). No MY-specific CISO/CRO/CTO/Compliance/IA/GRC found.]')
        set_cell(row, 'Chief Information Security Officer',
                 'NOT FOUND [ShopeePay Malaysia = Sea Limited/Monee subsidiary, BNM e-money issuer. Malaysia Head Alain Yee (AEMI president) confirmed. Parent Sea Ltd execs (Forrest Li CEO, Gang Ye COO, Chris Feng President - non-target). No MY-specific CISO/CRO/CTO/Compliance/IA/GRC publicly listed.]')
        updates_log.append(('ShopeePay Malaysia Sdn Bhd', 1))
        break

# 5. Setel by PETRONAS Dagangan Berhad - 3 roles (inherited from parent PDB)
for row in rows:
    if row.get('Institution_Name', '').strip() == 'Setel by PETRONAS Dagangan Berhad':
        set_cell(row, 'Chief Financial Officer',
                 'Mazlie Minhat (Chief Financial Officer, PETRONAS Dagangan Berhad - parent) [Official: mymesra.com.my/about-us/leadership-team, conf 80 - inherited to Setel Ventures Sdn Bhd. Appointed Jan 2026 to Setel board.]')
        set_cell(row, 'Chief Information Officer',
                 'Sazlina Ahamad (Chief Technology Officer, PETRONAS Dagangan Berhad - parent) [Official: mymesra.com.my/about-us/leadership-team, conf 80 - inherited to Setel.]')
        set_cell(row, 'Head of Internal Audit',
                 'Nik Fariza Nik Hamdan (Chief Audit Executive, PETRONAS Dagangan Berhad - parent) [Official: mymesra.com.my/about-us/leadership-team, conf 80 - inherited to Setel.]')
        set_cell(row, 'Chief Information Security Officer',
                 'NOT FOUND [Setel Ventures Sdn Bhd = PETRONAS Dagangan Berhad subsidiary, BNM e-money issuer. Setel CEO: Abdullah Ayman Awaluddin (mymesra.com.my, conf 95, non-target). Setel board: Azrul Osman Rani (Chairman), Nirmala Doraisamy (Independent Dir), Mohd Yuzaidi Mohd Yusoff, Azureen Azita Abdullah. Parent PDB CFO/CTO/Chief Audit Executive inherited. No CISO/CRO/Compliance/GRC found at Setel or PDB level.]')
        updates_log.append(('Setel by PETRONAS Dagangan Berhad', 3))
        break

# === AUDIT NOTES (institutions researched with 0 target roles) ===

# 6. Billplz Sdn Bhd - CEO confirmed (non-target), no public C-suite
for row in rows:
    if row.get('Institution_Name', '').strip() == 'Billplz Sdn Bhd':
        set_cell(row, 'Chief Information Security Officer',
                 'NOT FOUND [Malaysian payment gateway (Shah Alam, part of Billplz Qapital Berhad). CEO/Founder: Nazroof Hakim (Crunchbase + LinkedIn my.linkedin.com/in/nazroof, conf 95, non-target). billplz.com has no leadership page. ~34 employees per LinkedIn. RocketReach (blocked) mentioned Vinod Varma (Compliance Manager) + Nik Faudzi (Accounts) - UNVERIFIED. 0/7 target roles publicly disclosed.]')
        updates_log.append(('Billplz Sdn Bhd (0/7 note)', 0))
        break

# 7. ToyyibPay Sdn Bhd - no leadership found
for row in rows:
    if row.get('Institution_Name', '').strip() == 'ToyyibPay Sdn Bhd':
        set_cell(row, 'Chief Information Security Officer',
                 'NOT FOUND [Malaysian Shariah-compliant payment gateway founded 2019 (Bandar Tasik Selatan KL, 11-50 employees). toyyibpay.com has no leadership/team info. 5 LinkedIn employee names found (Zaiem Bakar, Muhammad Anwar, Atiqah Ghaffar, Nur Syakilah Rohaney, Ahmad Shahril Ibrahim) but individual profiles blocked - titles unknown. 0/7 target roles.]')
        updates_log.append(('ToyyibPay Sdn Bhd (0/7 note)', 0))
        break

# 8. GrabPay Malaysia Sdn Bhd - parent CEO/COO confirmed (non-target), CFO not verifiable
for row in rows:
    if row.get('Institution_Name', '').strip() == 'GrabPay Malaysia Sdn Bhd':
        set_cell(row, 'Chief Information Security Officer',
                 'NOT FOUND [GrabPay = Grab Holdings (Nasdaq:GRAB) digital payments arm, BNM e-money issuer. grab.com/my has no leadership names. Parent CEO: Anthony Tan, COO: Alex Hungate (Wikipedia, conf 85, non-target). CFO NOT VERIFIABLE - SEC EDGAR 20-F + investors.grab.com blocked by antibot in research session. Grab Financial Group owns GrabPay; no separate leadership published. 0/7 target roles verified.]')
        updates_log.append(('GrabPay Malaysia Sdn Bhd (0/7 note)', 0))
        break

# 9. Razer Pay Malaysia Sdn Bhd - DEFUNCT, flag for removal
for row in rows:
    if row.get('Institution_Name', '').strip() == 'Razer Pay Malaysia Sdn Bhd':
        set_cell(row, 'Chief Information Security Officer',
                 'ENTITY DEFUNCT [Razer Pay (Beta) e-wallet shut down in Malaysia AND Singapore in 2021 per Wikipedia. Both razerfintech.com and razerpay.com.my domains EXPIRED (DNS resolution fails). Razer Inc. delisted from HKEX May 2022 (now private). Only known Razer Inc. execs: Min-Liang Tan (CEO), Patricia Liu (Exec Dir), Khaw Kheng Joo (COO) - all non-target. RECOMMEND REMOVAL from active campaign list - entity non-operational.]')
        updates_log.append(('Razer Pay Malaysia Sdn Bhd (DEFUNCT flag)', 0))
        break

# === Write v5.6 ===
with open(DST, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f'\nWrote {len(rows)} rows to v5.6')
print(f'\nUpdates applied ({len(updates_log)}):')
for name, count in updates_log:
    print(f'  - {name}: +{count} role(s)')

# === Coverage stats ===
def is_real_contact(v):
    v = v.strip()
    if not v:
        return False
    return not (v.startswith('NOT FOUND') or v.startswith('DUPLICATE') or v.startswith('ENTITY'))

buckets = defaultdict(int)
total_filled = 0
role_fill = {c: 0 for c in STAKEHOLDER_COLS}
for row in rows:
    name = row.get('Institution_Name', '').strip()
    if not name:
        continue
    filled = 0
    for c in STAKEHOLDER_COLS:
        v = row.get(c, '').strip()
        if is_real_contact(v):
            filled += 1
            role_fill[c] += 1
    buckets[filled] += 1
    total_filled += filled

total_inst = sum(buckets.values())
print(f'\n=== Coverage Statistics v5.6 ===')
print(f'Total institutions: {total_inst}')
print(f'Total roles found: {total_filled}')
print(f'Total possible: {total_inst * 7}')
print(f'Overall coverage: {total_filled / (total_inst * 7) * 100:.1f}%')
print(f'\nCoverage distribution:')
for k in sorted(buckets.keys()):
    print(f'  {k}/7: {buckets[k]}')

print(f'\nPer-role completion:')
for c in STAKEHOLDER_COLS:
    print(f'  {c}: {role_fill[c]}/{total_inst} ({role_fill[c]/total_inst*100:.1f}%)')

print(f'\n=== v5.6 file: {DST}')

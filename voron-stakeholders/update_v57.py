#!/usr/bin/env python3
"""Update script for v5.7 enrichment - adds 5 new contacts from CISO/CIO research of 6/7 institutions."""
import csv
import shutil
from datetime import datetime

BASE = "/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders"
SRC = f"{BASE}/prospect-database-enriched-v5.6.csv"
DST = f"{BASE}/prospect-database-enriched-v5.7.csv"
MASTER_SRC = f"/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv"

# Column order in the CSV
ROLE_COLS = [
    "Chief Information Security Officer",
    "Head of Governance Risk & Compliance",
    "Chief Financial Officer",
    "Chief Risk Officer",
    "Head of Compliance",
    "Chief Information Officer",
    "Head of Internal Audit",
]

# New contacts to add: (institution_name_match_substring, role_column, cell_value)
NEW_CONTACTS = [
    # 1. ASNB - CIO/CTO (Ts Izzat Aziz, CTO PNB Group) — clean match, HIGH 90
    (
        "Amanah Saham Nasional Berhad",
        "Chief Information Officer",
        'Ts Izzat Aziz — Chief Technology Officer, PNB Group [Official: PNB Integrated Report 2024, pnb.com.my/en/leadership-en] | conf 90 | ASNB is "Managed by PNB"; no separate ASNB CIO/CTO. Ts Izzat Aziz won PIKOM CIO of the Year Award for AI Adoption. Inherited from PNB Group.',
    ),
    # 2. Great Eastern Life — CISO-equivalent (Vincent Chin, Division Head IT)
    (
        "Great Eastern Life Assurance",
        "Chief Information Security Officer",
        'Vincent Chin — Division Head, Information Technology (CISO-equivalent: handles technology risk management & IT governance) [Official: greateasternlife.com/my/en/about-us/company-profile/our-leaders/key-executive.html] | conf 75 | No dedicated CISO role listed; IT division covers infosec function.',
    ),
    # 3. Hong Leong Assurance — CISO-equivalent (Low Tek Chee, CTO)
    (
        "Hong Leong Assurance Berhad",
        "Chief Information Security Officer",
        'Low Tek Chee — Chief Technology Officer (CISO-equivalent) [Official: hla.com.my/en/know-us/leadership.html] | conf 75 | No dedicated CISO/Head of Information Security role among 13 executives. CTO is closest equivalent.',
    ),
    # 4. Liberty General Insurance — CISO-equivalent (Ganesan Vaithilingam, CIO)
    (
        "Liberty General Insurance Berhad",
        "Chief Information Security Officer",
        'Ganesan Vaithilingam — Chief Information Officer (CISO-equivalent: responsibilities include "information security" and "Secure IT environment development") [Official: libertyinsurance.com.my/corporate/management-team] | conf 72 | No dedicated CISO role; CIO handles infosec.',
    ),
    # 5. Kenanga Investment Bank — CISO-equivalent (Low Jia Yee, CTO)
    (
        "Kenanga Investment Bank Berhad",
        "Chief Information Security Officer",
        'Low Jia Yee — Chief Technology Officer (CISO-equivalent) [Official: kenanga.com.my/who-we-are/our-people/company/kenanga-investment-bank-berhad/] | conf 75 | No dedicated CISO/Head of IT Security among 25+ executives. CTO is closest equivalent.',
    ),
]

# Audit notes for confirmed NOT FOUND (institution_substring, role_column, note)
AUDIT_NOTES = [
    (
        "Agrobank Malaysia",
        "Chief Information Security Officer",
        'NOT FOUND [CISO not listed on official Senior Leadership page (11 execs). Closest: Nolan Jeffrey A/L Abdul Hai — Group CITO (Group Chief Information Technology Officer), appointed ~May 2026. Source: agrobank.com.my/my/home/corporate-info/senior-leadership/]',
    ),
    (
        "Bank Pembangunan Malaysia Berhad",
        "Chief Information Security Officer",
        'NOT FOUND [CISO not listed on Group ExCo (16 members). Closest: Hairil Izwar Abd Rahman — Group Chief Digital & Technology Officer. Note: "Group CSO" title = Chief Strategy Officer, NOT Chief Security Officer. Source: bpmb.com.my/about-us/leadership/]',
    ),
    (
        "EXIM Bank Malaysia",
        "Chief Information Security Officer",
        'NOT FOUND [CISO not on leadership page. Since 1 May 2025, EXIM Bank merged with BPMB — CISO function consolidated at BPMB Group level, which also has no CISO. Source: exim.com.my/about-us/our-leadership/]',
    ),
    (
        "SME Bank Berhad",
        "Chief Information Security Officer",
        'NOT FOUND [No management team listing; BOD page lists only directors. Since 1 May 2025, merged with BPMB Group — CISO function at BPMB Group level (no CISO listed). Source: smebank.com.my/board-of-directors]',
    ),
    (
        "Tabung Haji",
        "Chief Information Security Officer",
        'NOT FOUND [CISO not in 2025 Annual Report (100pp). Cybersecurity oversight embedded in Risk & Compliance dept. Closest: Syahril Nizam Abu Hasan — Chief Risk & Compliance Officer. Source: tabunghaji.gov.my 2025 AR]',
    ),
    (
        "Lembaga Tabung Haji",
        "Chief Information Security Officer",
        'NOT FOUND [Same entity as Tabung Haji. CISO not in 2025 Annual Report. Cybersecurity under Risk & Compliance dept.]',
    ),
    (
        "Public Bank Berhad",
        "Chief Information Security Officer",
        'NOT FOUND [No CISO title among 25 Heads of Division. Closest: Fam Yoke Fong — Senior General Manager, Information Technology (infosec likely embedded in IT dept). Also: Tuan Haji A Wahab bin A Raman — Director, Security (physical/corporate security, NOT infosec). Source: publicbankgroup.com/about-us/leadership/heads-of-division/]',
    ),
    (
        "Public Islamic Bank Berhad",
        "Chief Information Security Officer",
        'NOT FOUND [Shares Group leadership with Public Bank Berhad — same 25 Heads of Division, no CISO. CEO: Syamsul Azuan bin Ahmad Fauzi. Source: publicbankgroup.com]',
    ),
    (
        "Bank Rakyat Malaysia",
        "Head of Internal Audit",
        'NOT FOUND [Position exists (confirmed in Sustainability Report 2024 org chart) but NAME not publicly published. Mgmt Committee (8 members) does not include Internal Audit. Likely kept confidential for governance independence. Source: bankrakyat.com.my/portal-main/leaders/management-committee]',
    ),
    (
        "Hong Leong Investment Bank Berhad",
        "Chief Information Security Officer",
        'NOT FOUND [No CISO in Annual Report 2024 "Key Senior Management" (8 people). Website is JS SPA. Source: hlib.com.my/Files/AnnualReports/HL_Capital_AR2024.pdf]',
    ),
    (
        "Public Investment Bank Berhad",
        "Chief Information Security Officer",
        'NOT FOUND [Domain publicinvest.com does not resolve (DNS failure). Subsidiary of Public Bank — shares Group leadership. No separate CISO info found.]',
    ),
    (
        "Great Eastern General Insurance",
        "Chief Information Security Officer",
        'NOT FOUND [No dedicated CISO. COO Jarron Khoo Eng Siong oversees "operations and technology". Source: greateasternlife.com/my/en/about-us/company-profile/our-leaders/key-executive.html]',
    ),
    (
        "Phillip Securities",
        "Head of Governance Risk & Compliance",
        'NOT FOUND [Now Phillip Capital Sdn Bhd (rebranded Aug 2022). phillip.com.my/about-us/our-management returns 404. Website has no management listings. SC Malaysia Capital Markets Services License holder.]',
    ),
    (
        "Tekun Nasional",
        "Head of Governance Risk & Compliance",
        'NOT FOUND [Small microcredit institution under Ministry of Entrepreneur Development. Website (tekun.gov.my) has no management/leadership/governance pages. Likely no dedicated GRC role.]',
    ),
]


def match_institution(inst_name, substring):
    """Case-insensitive substring match for institution name."""
    return substring.lower() in inst_name.lower()


def main():
    # Read source CSV
    with open(SRC, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames

    updated_count = 0
    audit_count = 0

    # Apply new contacts
    for substring, role_col, cell_value in NEW_CONTACTS:
        for r in rows:
            if match_institution(r.get("Institution_Name", ""), substring):
                existing = r.get(role_col, "").strip()
                if not existing or "NOT FOUND" in existing:
                    r[role_col] = cell_value
                    updated_count += 1
                    print(f"  + NEW CONTACT: [{r.get('Segment','')}] {r.get('Institution_Name','')} -> {role_col}")
                    break

    # Apply audit notes for NOT FOUND
    for substring, role_col, cell_value in AUDIT_NOTES:
        for r in rows:
            if match_institution(r.get("Institution_Name", ""), substring):
                existing = r.get(role_col, "").strip()
                if not existing:
                    r[role_col] = cell_value
                    audit_count += 1
                    print(f"  ~ AUDIT NOTE: [{r.get('Segment','')}] {r.get('Institution_Name','')} -> {role_col}")
                    break

    # Write enriched v5.7
    with open(DST, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Compute coverage stats
    filled_total = 0
    for r in rows:
        for c in ROLE_COLS:
            val = r.get(c, "").strip()
            if val and "NOT FOUND" not in val:
                filled_total += 1

    total_possible = len(rows) * 7
    print(f"\n=== v5.7 UPDATE COMPLETE ===")
    print(f"New contacts added: {updated_count}")
    print(f"Audit notes added: {audit_count}")
    print(f"Total rows: {len(rows)}")
    print(f"Total roles found: {filled_total}/{total_possible} ({100*filled_total/total_possible:.1f}%)")
    print(f"Output: {DST}")

    # Copy to master locations
    shutil.copy2(DST, MASTER_SRC)
    print(f"Master synced: {MASTER_SRC}")


if __name__ == "__main__":
    main()

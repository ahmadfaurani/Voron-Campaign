#!/usr/bin/env python3
"""
Master CSV Update Script for v5.14
Applies the same changes to prospect-database-7stakeholders.csv (206 rows, the reporting basis)
"""
import csv
import shutil

MASTER = "/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv"
BACKUP = MASTER + ".bak-pre-v5.14-" + "20260719-133000"

ROLE_COLS = [
    "Chief Information Security Officer",
    "Head of Governance Risk & Compliance",
    "Chief Financial Officer",
    "Chief Risk Officer",
    "Head of Compliance",
    "Chief Information Officer",
    "Head of Internal Audit",
]

def is_filled(val):
    v = (val or "").strip()
    return bool(v) and not v.upper().startswith("NOT FOUND")

# NEW FILLS
NEW_FILLS = {
    "Manulife Takaful Malaysia Berhad": {
        "Chief Risk Officer": "Mohd Naim Bin Mohd Arsad (Chief Risk Officer, Manulife Insurance Berhad - management shared) [Official: Manulife Holdings Berhad Annual Report 2025, p.13 Key Senior Management's Profile, conf 85]",
        "Head of Compliance": "Senthil Woon Wai Keong (Chief Compliance Officer, Manulife Insurance Berhad - management shared) [Official: Manulife Holdings Berhad Annual Report 2025, p.13 Key Senior Management's Profile, conf 85]",
        "Head of Internal Audit": "Krishna Rajaa Ramalingam (Head of Audit Services - Malaysia) [Official: Manulife Holdings Berhad Annual Report 2025, p.91 Group Audit Committee Report, conf 90 - CIA, FAIA. Scope covers all Manulife Malaysia entities including Takaful]",
    },
}

# CORRECTIONS
CORRECTIONS = {
    "Zurich Life Insurance Malaysia Berhad": {
        "Chief Information Security Officer": "NOT FOUND [CORRECTION: Previous entry 'Pauline Teoh' is the CEO of Zurich Life Insurance Malaysia Berhad, NOT the CISO. Verified via official zurich.com.my/about-zurich/the-zurich-story/our-leaders (conf 95). Actual CISO not publicly disclosed. Sources checked: Zurich Our Leaders page, Zurich Life AR 2024 & 2025 CG Statements, web/LinkedIn search.]",
    },
    "MARA (Majlis Amanah Rakyat)": {
        "Chief Information Security Officer": "NOT FOUND [CORRECTION: Previous entry 'Datuk Zulfikri Osman' is the Ketua Pengarah (CEO/Director General) of MARA, NOT the CISO. Verified via Wikipedia Majlis_Amanah_Rakyat (conf 95). Actual CISO not publicly identified. MARA management team page (mara.gov.my) is image-based. Sources: mara.gov.my, MARA org chart PNG, Wikipedia, firecrawl_agent.]",
    },
}

CIO_CORRECTION_MARA = "Dr. Azmi bin Amat Murjan (Timbalan Ketua Pengarah MARA (Khidmat Pengurusan) / Ketua Pegawai Digital (CDO) - title is CDO not strictly CIO; portfolio includes cybersecurity action plan coordination) [Official: mara.gov.my, conf 80 - TITLE CORRECTED from CIO to CDO per Wikipedia verification]"

PRUBSN_CRO_FLAG = "Anita Menon (Chief Risk Officer) [Malaysian Insurance Directory 2025/2026, conf 85 - STALE WARNING: NOT on current PruBSN ExCo as of Jul 2026 scrape (prubsn.com.my our-leaders lists 8 ExCo members, Anita Menon not among them). May refer to different Prudential entity or below ExCo level. Recommend verification.]"

# NOT FOUND audit trails (master CSV institution names)
NOT_FOUND_ENTRIES = {
    "PayNet (PayNet Malaysia Sdn Bhd)": {
        "Chief Risk Officer": "NOT FOUND [PayNet leadership page (8 execs, no CRO). Group Risk Committee confirms function exists. 3 Senior Directors have generic titles. Sources: paynet.my leadership/committees/careers, firecrawl agents.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [PayNet splits GRC across Group Risk + Audit Committees. No combined GRC head. Sources: paynet.my leadership/committees/corporate-governance, firecrawl agents.]",
        "Head of Compliance": "NOT FOUND [Compliance via Integrity Unit overseen by Group Audit Committee. No head named. Sources: paynet.my corporate-governance, firecrawl agents.]",
        "Head of Internal Audit": "NOT FOUND [Group Audit Committee oversees IA. Head not on leadership page. Sources: paynet.my leadership/committees, firecrawl agents.]",
    },
    "DuitNow (by PayNet)": {
        "Chief Information Security Officer": "NOT FOUND [Inherited from PayNet. CISO Office exists but VACANT (active job posting at Senior Manager level). Sources: paynet.my careers page.]",
        "Chief Risk Officer": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership/committees.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership.]",
        "Head of Compliance": "NOT FOUND [Inherited from PayNet. Sources: paynet.my corporate-governance.]",
        "Head of Internal Audit": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership/committees.]",
    },
    "FPX (by PayNet)": {
        "Chief Information Security Officer": "NOT FOUND [Inherited from PayNet. CISO VACANT. Sources: paynet.my careers.]",
        "Chief Risk Officer": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership/committees.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership.]",
        "Head of Compliance": "NOT FOUND [Inherited from PayNet. Sources: paynet.my corporate-governance.]",
        "Head of Internal Audit": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership/committees.]",
    },
    "JomPAY (by PayNet)": {
        "Chief Information Security Officer": "NOT FOUND [Inherited from PayNet. CISO VACANT. Sources: paynet.my careers.]",
        "Chief Risk Officer": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership/committees.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership.]",
        "Head of Compliance": "NOT FOUND [Inherited from PayNet. Sources: paynet.my corporate-governance.]",
        "Head of Internal Audit": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership/committees.]",
    },
    "Me2U (by PayNet)": {
        "Chief Information Security Officer": "NOT FOUND [Inherited from PayNet. CISO VACANT. Sources: paynet.my careers.]",
        "Chief Risk Officer": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership/committees.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership.]",
        "Head of Compliance": "NOT FOUND [Inherited from PayNet. Sources: paynet.my corporate-governance.]",
        "Head of Internal Audit": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership/committees.]",
    },
    "PayDirect (by PayNet)": {
        "Chief Information Security Officer": "NOT FOUND [Inherited from PayNet. CISO VACANT. Sources: paynet.my careers.]",
        "Chief Risk Officer": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership/committees.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership.]",
        "Head of Compliance": "NOT FOUND [Inherited from PayNet. Sources: paynet.my corporate-governance.]",
        "Head of Internal Audit": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership/committees.]",
    },
    "PayNet Card (by PayNet)": {
        "Chief Information Security Officer": "NOT FOUND [Inherited from PayNet. CISO VACANT. Sources: paynet.my careers.]",
        "Chief Risk Officer": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership/committees.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership.]",
        "Head of Compliance": "NOT FOUND [Inherited from PayNet. Sources: paynet.my corporate-governance.]",
        "Head of Internal Audit": "NOT FOUND [Inherited from PayNet. Sources: paynet.my leadership/committees.]",
    },
    "Allianz General Insurance Company (Malaysia) Berhad": {
        "Chief Information Security Officer": "NOT FOUND [Allianz Malaysia website lists only Board of Directors. IAR 2024 PDF located but anti-bot blocked (4 methods tried). Sources: allianz.com.my, IAR 2024 PDF (blocked), firecrawl agents.]",
        "Chief Risk Officer": "NOT FOUND [Board Risk Management Committee is board-level. Executive CRO not disclosed. Sources: allianz.com.my, IAR 2024 PDF (blocked), firecrawl agents.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Not disclosed. Sources: allianz.com.my, IAR 2024 PDF (blocked), firecrawl agents.]",
        "Head of Compliance": "NOT FOUND [Not disclosed. Sources: allianz.com.my, IAR 2024 PDF (blocked), firecrawl agents.]",
        "Head of Internal Audit": "NOT FOUND [Audit Committee is board-level. Executive IA head not disclosed. Sources: allianz.com.my, IAR 2024 PDF (blocked), firecrawl agents.]",
    },
    "Allianz Life Insurance Malaysia Berhad": {
        "Chief Information Security Officer": "NOT FOUND [Shared AMB group. Not disclosed. Sources: allianz.com.my, IAR 2024 (blocked), firecrawl agents.]",
        "Chief Risk Officer": "NOT FOUND [Shared AMB group. Not disclosed. Sources: allianz.com.my, IAR 2024 (blocked).]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Shared AMB group. Not disclosed. Sources: allianz.com.my, IAR 2024 (blocked).]",
        "Head of Compliance": "NOT FOUND [Shared AMB group. Not disclosed. Sources: allianz.com.my, IAR 2024 (blocked).]",
        "Head of Internal Audit": "NOT FOUND [Shared AMB group. Board Audit Committee is board-level. Sources: allianz.com.my, IAR 2024 (blocked).]",
    },
    "Allianz Takaful Berhad": {
        "Chief Information Security Officer": "NOT FOUND [Shared AMB group. Not disclosed. Sources: allianz.com.my, IAR 2024 (blocked), firecrawl agents.]",
        "Chief Risk Officer": "NOT FOUND [Shared AMB group. Not disclosed. Sources: allianz.com.my, IAR 2024 (blocked).]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Shared AMB group. Not disclosed. Sources: allianz.com.my, IAR 2024 (blocked).]",
        "Head of Compliance": "NOT FOUND [Shared AMB group. Not disclosed. Sources: allianz.com.my, IAR 2024 (blocked).]",
        "Head of Internal Audit": "NOT FOUND [Shared AMB group. Not disclosed. Sources: allianz.com.my, IAR 2024 (blocked).]",
    },
    "Zurich Life Insurance Malaysia Berhad": {
        "Chief Financial Officer": "NOT FOUND [Zurich Our Leaders page lists only 4 entity CEOs. AR 2024 & 2025 CG Statements name only Board Directors. Sources: zurich.com.my, Zurich Life AR 2024/2025, firecrawl agents.]",
        "Chief Risk Officer": "NOT FOUND [Board Risk Committee chaired by Donald Joshua Jaganathan (board-level). Executive CRO not disclosed. Sources: zurich.com.my, AR 2024/2025, firecrawl agents.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Not disclosed. Sources: zurich.com.my, AR 2024/2025, firecrawl agents.]",
        "Head of Compliance": "NOT FOUND [Not disclosed. Sources: zurich.com.my, AR 2024/2025, firecrawl agents.]",
        "Chief Information Officer": "NOT FOUND [Not disclosed. Sources: zurich.com.my, AR 2024/2025, firecrawl agents.]",
    },
    "HSBC Amanah Takaful (Malaysia) Berhad": {
        "Chief Information Security Officer": "NOT FOUND [Entity now FWD Takaful Berhad (FWD Group acquired from HSBC 2019). Official team (fwd.com.my) lists 6 execs, no CISO. Functions likely at FWD Group (HK) level. Sources: fwd.com.my, firecrawl agents.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [No combined GRC role. Risk and compliance separate. Sources: fwd.com.my, firecrawl agents.]",
        "Chief Risk Officer": "NOT FOUND [Not on Malaysia leadership page. May be regional FWD Group role. Sources: fwd.com.my, firecrawl agents.]",
        "Chief Information Officer": "NOT FOUND [Not on Malaysia leadership page. Sources: fwd.com.my, firecrawl agents.]",
        "Head of Internal Audit": "NOT FOUND [Not publicly disclosed. Sources: fwd.com.my, firecrawl agents.]",
    },
    "Manulife Takaful Malaysia Berhad": {
        "Chief Information Security Officer": "NOT FOUND [No CISO in MHB AR 2025. CIO (Bernard Sia) likely oversees IT security. Sources: MHB AR 2025, manulife.com.my, firecrawl agents.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [No combined GRC role. Risk and Compliance separate. Sources: MHB AR 2025, firecrawl agents.]",
    },
    "Prudential BSN Takaful Berhad": {
        "Chief Information Security Officer": "NOT FOUND [Not on PruBSN ExCo (8 members). Sources: prubsn.com.my, PruBSN Board Charter v4.0, firecrawl agents.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Board Charter refers to 'Control Function Heads' (plural). Sources: prubsn.com.my, Board Charter v4.0, firecrawl agents.]",
        "Head of Compliance": "NOT FOUND [Not on ExCo. Per BNM must exist but not named. Sources: prubsn.com.my, Board Charter v4.0, firecrawl agents.]",
        "Chief Information Officer": "NOT FOUND [Not on ExCo. IT likely at Prudential Malaysia group. Sources: prubsn.com.my, firecrawl agents.]",
        "Head of Internal Audit": "NOT FOUND [Role exists per Board Charter but not named. Sources: prubsn.com.my, Board Charter v4.0, firecrawl agents.]",
    },
    "MARA (Majlis Amanah Rakyat)": {
        "Head of Governance Risk & Compliance": "NOT FOUND [MARA management page is image-based, 29 positions as image cards. GRC equivalent would be Timbalan Ketua Pengarah. Sources: mara.gov.my, MARA org chart PNG, firecrawl agents.]",
        "Chief Financial Officer": "NOT FOUND [CFO equivalent = Timbalan Ketua Pengarah (Kewangan). Not identified. mara.gov.my is image-based. Sources: mara.gov.my, firecrawl agents.]",
        "Chief Risk Officer": "NOT FOUND [CRO equivalent may not exist as standalone role at government agency. Sources: mara.gov.my, firecrawl agents.]",
        "Head of Compliance": "NOT FOUND [Compliance likely under corporate services portfolio. Sources: mara.gov.my, firecrawl agents.]",
        "Head of Internal Audit": "NOT FOUND [IA likely reports to Auditor General. Sources: mara.gov.my, firecrawl agents.]",
    },
    "GrabPay (Grab Malaysia)": {
        "Chief Information Security Officer": "NOT FOUND [No executive directory on grab.com. CISO likely at Grab Holdings (Singapore). Sources: grab.com/my/, Wikipedia Grab Holdings, firecrawl agents.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Likely at Grab Financial Group (regional) or Grab Holdings. Sources: grab.com, Wikipedia, firecrawl agents.]",
        "Chief Risk Officer": "NOT FOUND [Likely at Grab Holdings group level. Sources: grab.com, Wikipedia, firecrawl agents.]",
        "Head of Compliance": "NOT FOUND [Per BNM e-money requirements must have local compliance officer but not publicly disclosed. Sources: grab.com, firecrawl agents.]",
        "Head of Internal Audit": "NOT FOUND [Likely at Grab Holdings group level. Sources: grab.com, firecrawl agents.]",
    },
}

def main():
    # Backup
    shutil.copy2(MASTER, BACKUP)
    print(f"Backed up to {BACKUP}")

    with open(MASTER, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    stats = {"new_fills": 0, "corrections": 0, "not_found": 0, "title_corr": 0, "stale": 0, "touched": set()}

    for row in rows:
        inst = row.get("Institution_Name", "")

        if inst in NEW_FILLS:
            for role, val in NEW_FILLS[inst].items():
                if role in row and not is_filled(row[role]):
                    row[role] = val
                    stats["new_fills"] += 1
                    stats["touched"].add(inst)

        if inst in CORRECTIONS:
            for role, val in CORRECTIONS[inst].items():
                if role in row:
                    row[role] = val
                    stats["corrections"] += 1
                    stats["touched"].add(inst)

        if inst in NOT_FOUND_ENTRIES:
            for role, val in NOT_FOUND_ENTRIES[inst].items():
                if role in row and not row[role].strip():
                    row[role] = val
                    stats["not_found"] += 1
                    stats["touched"].add(inst)
                elif role in row and not is_filled(row[role]) and len(val) > len(row[role].strip()) + 50:
                    row[role] = val
                    stats["not_found"] += 1
                    stats["touched"].add(inst)

        if inst == "MARA (Majlis Amanah Rakyat)" and is_filled(row.get("Chief Information Officer", "")):
            row["Chief Information Officer"] = CIO_CORRECTION_MARA
            stats["title_corr"] += 1
            stats["touched"].add(inst)

        if inst == "Prudential BSN Takaful Berhad" and "Anita Menon" in row.get("Chief Risk Officer", ""):
            row["Chief Risk Officer"] = PRUBSN_CRO_FLAG
            stats["stale"] += 1
            stats["touched"].add(inst)

    with open(MASTER, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Stats
    filled = sum(sum(1 for r in ROLE_COLS if is_filled(row.get(r,""))) for row in rows)
    total = len(rows) * 7
    cluster = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
    for row in rows:
        fc = sum(1 for r in ROLE_COLS if is_filled(row.get(r,"")))
        cluster[fc] = cluster.get(fc,0)+1

    print(f"\nWritten {len(rows)} rows to {MASTER}")
    print(f"\n=== Master CSV v5.14 Stats ===")
    print(f"  Filled: {filled}/{total} = {filled/total*100:.1f}%")
    for k in sorted(cluster.keys()):
        if cluster[k]:
            print(f"  {k}/7: {cluster[k]}")
    print(f"\n  New fills: {stats['new_fills']}")
    print(f"  Corrections: {stats['corrections']}")
    print(f"  NOT FOUND added: {stats['not_found']}")
    print(f"  Title corrections: {stats['title_corr']}")
    print(f"  Stale flags: {stats['stale']}")
    print(f"  Institutions touched: {len(stats['touched'])}")

if __name__ == "__main__":
    main()

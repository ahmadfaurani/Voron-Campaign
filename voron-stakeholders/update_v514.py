#!/usr/bin/env python3
"""
VoronDRQ Enrichment Update Script v5.14
2/7 Cluster Resolution - PayNet, Allianz, Takaful, Zurich, MARA, GrabPay

Changes:
  NEW FILLS (3): Manulife Takaful - CRO, Head of Compliance, Head of Internal Audit
  CORRECTIONS (3): Zurich Life CISO (CEO misclassified), MARA CISO x2 rows (CEO misclassified)
  NOT FOUND audit trails: ~80+ entries across 17 institutions
"""
import csv
import shutil
import os

ENRICHED_SRC = "/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.13.csv"
ENRICHED_DST = "/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.14.csv"
MASTER_SRC  = "/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv"

ROLE_COLS = [
    "Chief Information Security Officer",
    "Head of Governance Risk & Compliance",
    "Chief Financial Officer",
    "Chief Risk Officer",
    "Head of Compliance",
    "Chief Information Officer",
    "Head of Internal Audit",
]

# --- NEW ROLE FILLS ---
NEW_FILLS = {
    "Manulife Takaful Malaysia Berhad": {
        "Chief Risk Officer": "Mohd Naim Bin Mohd Arsad (Chief Risk Officer, Manulife Insurance Berhad - management shared) [Official: Manulife Holdings Berhad Annual Report 2025, p.13 Key Senior Management's Profile, conf 85]",
        "Head of Compliance": "Senthil Woon Wai Keong (Chief Compliance Officer, Manulife Insurance Berhad - management shared) [Official: Manulife Holdings Berhad Annual Report 2025, p.13 Key Senior Management's Profile, conf 85]",
        "Head of Internal Audit": "Krishna Rajaa Ramalingam (Head of Audit Services - Malaysia) [Official: Manulife Holdings Berhad Annual Report 2025, p.91 Group Audit Committee Report, conf 90 - CIA, FAIA. Scope covers all Manulife Malaysia entities including Takaful]",
    },
}

# --- CORRECTIONS (misclassifications: CEO filed as CISO) ---
CORRECTIONS = {
    "Zurich Life Insurance Malaysia Berhad": {
        "Chief Information Security Officer": "NOT FOUND [CORRECTION: Previous entry 'Pauline Teoh' is the CEO of Zurich Life Insurance Malaysia Berhad, NOT the CISO. Verified via official zurich.com.my/about-zurich/the-zurich-story/our-leaders (conf 95). Actual CISO not publicly disclosed. Sources checked: Zurich Our Leaders page, Zurich Life AR 2024 & 2025 Corporate Governance Statements, web/LinkedIn search.]",
    },
    "MARA": {
        "Chief Information Security Officer": "NOT FOUND [CORRECTION: Previous entry 'Datuk Zulfikri Osman' is the Ketua Pengarah (CEO/Director General) of MARA, NOT the CISO. Verified via Wikipedia Majlis_Amanah_Rakyat (conf 95). Actual CISO not publicly identified. MARA management team page (mara.gov.my) is image-based, 29 senior positions shown as image cards with no extractable titles. Sources checked: mara.gov.my management team, MARA org chart PNG, Wikipedia, firecrawl_agent.]",
    },
    "MARA (Majlis Amanah Rakyat)": {
        "Chief Information Security Officer": "NOT FOUND [CORRECTION: Previous entry 'Datuk Zulfikri Osman' is the Ketua Pengarah (CEO/Director General) of MARA, NOT the CISO. Verified via Wikipedia Majlis_Amanah_Rakyat (conf 95). Actual CISO not publicly identified. MARA management team page (mara.gov.my) is image-based, 29 senior positions shown as image cards with no extractable titles. Sources checked: mara.gov.my management team, MARA org chart PNG, Wikipedia, firecrawl_agent.]",
    },
}

# --- NOT FOUND audit trails ---
# Format: { institution: { role: audit_trail_text } }
NOT_FOUND_ENTRIES = {
    # PayNet group (7 rows) - CRO, GRC, Compliance, IA
    "PayNet (PayNet Malaysia Sdn Bhd)": {
        "Chief Risk Officer": "NOT FOUND [PayNet leadership page (8 execs, no CRO). Group Risk Committee charter confirms function exists. 3 Senior Directors have generic titles, no functional mapping possible. Sources: paynet.my leadership/committees/careers pages, Wikipedia, 2 firecrawl agents, web/LinkedIn search.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [PayNet splits GRC across Group Risk Committee + Group Audit Committee. No combined GRC head named. Sources: paynet.my leadership/committees/corporate-governance pages, firecrawl agents.]",
        "Head of Compliance": "NOT FOUND [Compliance via Integrity Unit overseen by Group Audit Committee. No Head of Compliance named. Sources: paynet.my corporate-governance page (Whistleblowing Policy, Corporate Integrity Statement), firecrawl agents.]",
        "Head of Internal Audit": "NOT FOUND [Group Audit Committee oversees IA (appoints, reviews plan, assesses performance). Head of IA not on leadership page. Sources: paynet.my leadership/committees pages, firecrawl agents.]",
    },
    "DuitNow (by PayNet)": {
        "Chief Information Security Officer": "NOT FOUND [Inherited from PayNet parent. PayNet CISO Office exists per Group Risk Committee charter but is currently VACANT (active job posting at Senior Manager level on paynet.my careers page). Sources: paynet.my leadership/committees/careers pages.]",
        "Chief Risk Officer": "NOT FOUND [Inherited from PayNet parent. CRO not named on PayNet leadership page. Sources: paynet.my leadership/committees pages, firecrawl agents.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Inherited from PayNet parent. No combined GRC head. Sources: paynet.my leadership/committees pages.]",
        "Head of Compliance": "NOT FOUND [Inherited from PayNet parent. Compliance via Integrity Unit. Sources: paynet.my corporate-governance page.]",
        "Head of Internal Audit": "NOT FOUND [Inherited from PayNet parent. Group Audit Committee oversees IA. Head not named. Sources: paynet.my leadership/committees pages.]",
    },
    "FPX (by PayNet)": {
        "Chief Information Security Officer": "NOT FOUND [Inherited from PayNet parent. CISO Office exists but currently VACANT (active job posting). Sources: paynet.my careers page.]",
        "Chief Risk Officer": "NOT FOUND [Inherited from PayNet parent. CRO not named. Sources: paynet.my leadership/committees pages.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my leadership pages.]",
        "Head of Compliance": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my corporate-governance page.]",
        "Head of Internal Audit": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my leadership/committees pages.]",
    },
    "JomPAY (by PayNet)": {
        "Chief Information Security Officer": "NOT FOUND [Inherited from PayNet parent. CISO Office exists but currently VACANT. Sources: paynet.my careers page.]",
        "Chief Risk Officer": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my leadership/committees pages.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my leadership pages.]",
        "Head of Compliance": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my corporate-governance page.]",
        "Head of Internal Audit": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my leadership/committees pages.]",
    },
    "Me2U (by PayNet)": {
        "Chief Information Security Officer": "NOT FOUND [Inherited from PayNet parent. CISO Office exists but currently VACANT. Sources: paynet.my careers page.]",
        "Chief Risk Officer": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my leadership/committees pages.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my leadership pages.]",
        "Head of Compliance": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my corporate-governance page.]",
        "Head of Internal Audit": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my leadership/committees pages.]",
    },
    "PayDirect (by PayNet)": {
        "Chief Information Security Officer": "NOT FOUND [Inherited from PayNet parent. CISO Office exists but currently VACANT. Sources: paynet.my careers page.]",
        "Chief Risk Officer": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my leadership/committees pages.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my leadership pages.]",
        "Head of Compliance": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my corporate-governance page.]",
        "Head of Internal Audit": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my leadership/committees pages.]",
    },
    "PayNet Card (by PayNet)": {
        "Chief Information Security Officer": "NOT FOUND [Inherited from PayNet parent. CISO Office exists but currently VACANT. Sources: paynet.my careers page.]",
        "Chief Risk Officer": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my leadership/committees pages.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my leadership pages.]",
        "Head of Compliance": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my corporate-governance page.]",
        "Head of Internal Audit": "NOT FOUND [Inherited from PayNet parent. Sources: paynet.my leadership/committees pages.]",
    },
    # Allianz group (3 rows) - CISO, CRO, GRC, Compliance, IA
    "Allianz General Insurance Company (Malaysia) Berhad": {
        "Chief Information Security Officer": "NOT FOUND [Allianz Malaysia website only lists Board of Directors publicly. IAR 2024 PDF located (allianz.com.my IAR24 PDF) but anti-bot blocked across 4 methods (basic/stealth/lockdown/web_extract). Sources: allianz.com.my boards-of-directors page, IAR 2024 PDF (blocked), LinkedIn, web search, firecrawl agents.]",
        "Chief Risk Officer": "NOT FOUND [Board Risk Management Committee (Dr. Muhammed Bin Abdul Khalid chairs) is board-level, not executive CRO. Executive CRO not publicly disclosed. Sources: allianz.com.my, IAR 2024 PDF (blocked), firecrawl agents.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Not disclosed in accessible public sources. Sources: allianz.com.my, IAR 2024 PDF (blocked), firecrawl agents.]",
        "Head of Compliance": "NOT FOUND [Not disclosed in accessible public sources. Sources: allianz.com.my, IAR 2024 PDF (blocked), firecrawl agents.]",
        "Head of Internal Audit": "NOT FOUND [Audit Committee member Peter Ho Kok Wai is board-level, not executive IA head. Sources: allianz.com.my, IAR 2024 PDF (blocked), firecrawl agents.]",
    },
    "Allianz Life Insurance Malaysia Berhad": {
        "Chief Information Security Officer": "NOT FOUND [Shared AMB group senior management. Not publicly disclosed. Sources: allianz.com.my, IAR 2024 PDF (blocked), firecrawl agents.]",
        "Chief Risk Officer": "NOT FOUND [Shared AMB group. Not publicly disclosed. Sources: allianz.com.my, IAR 2024 PDF (blocked), firecrawl agents.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Shared AMB group. Not publicly disclosed. Sources: allianz.com.my, IAR 2024 PDF (blocked).]",
        "Head of Compliance": "NOT FOUND [Shared AMB group. Not publicly disclosed. Sources: allianz.com.my, IAR 2024 PDF (blocked).]",
        "Head of Internal Audit": "NOT FOUND [Audit Committee chairman Peter Ho Kok Wai is board-level. Executive IA head not disclosed. Sources: allianz.com.my, IAR 2024 PDF (blocked).]",
    },
    "Allianz Takaful Berhad": {
        "Chief Information Security Officer": "NOT FOUND [Shared AMB group senior management. Not publicly disclosed. Sources: allianz.com.my, IAR 2024 PDF (blocked), firecrawl agents.]",
        "Chief Risk Officer": "NOT FOUND [Shared AMB group. Not publicly disclosed. Sources: allianz.com.my, IAR 2024 PDF (blocked).]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Shared AMB group. Not publicly disclosed. Sources: allianz.com.my, IAR 2024 PDF (blocked).]",
        "Head of Compliance": "NOT FOUND [Shared AMB group. Not publicly disclosed. Sources: allianz.com.my, IAR 2024 PDF (blocked).]",
        "Head of Internal Audit": "NOT FOUND [Shared AMB group. Not publicly disclosed. Sources: allianz.com.my, IAR 2024 PDF (blocked).]",
    },
    # Zurich Life - 5 missing roles (CFO, CRO, GRC, Compliance, CIO)
    "Zurich Life Insurance Malaysia Berhad": {
        "Chief Financial Officer": "NOT FOUND [Zurich Our Leaders page lists only 4 entity CEOs (Junior Cho, Pauline Teoh, Nur Fatihah Mustafa, Shamsul Azman). AR 2024 & 2025 Corporate Governance Statements name only Board Directors/Committee members, no executive officers. Sources: zurich.com.my our-leaders, Zurich Life AR 2024/2025 CG Statements, web/LinkedIn search.]",
        "Chief Risk Officer": "NOT FOUND [Board Risk Management and Sustainability Committee chaired by Donald Joshua Jaganathan (board-level). Executive CRO not publicly disclosed. Sources: zurich.com.my, Zurich Life AR 2024/2025, firecrawl agents.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Not publicly disclosed. Sources: zurich.com.my, Zurich Life AR 2024/2025, firecrawl agents.]",
        "Head of Compliance": "NOT FOUND [Not publicly disclosed. Sources: zurich.com.my, Zurich Life AR 2024/2025, firecrawl agents.]",
        "Chief Information Officer": "NOT FOUND [Not publicly disclosed. Sources: zurich.com.my, Zurich Life AR 2024/2025, firecrawl agents.]",
    },
    # FWD Takaful (formerly HSBC Amanah Takaful) - CISO, GRC, CRO, CIO, IA
    "HSBC Amanah Takaful (Malaysia) Berhad": {
        "Chief Information Security Officer": "NOT FOUND [Entity is now FWD Takaful Berhad (FWD Group acquired from HSBC 2019). Official team page (fwd.com.my) lists 6 execs: CEO Aman Chowla, Acting CFO Muhammad Afiq bin Hamzah, Chong Wen Han, Rohana Idris, Lim Weng Leong (Compliance), Mohd Hafizal Elias (Shariah). No CISO. Functions likely centralized at FWD Group (Hong Kong) level. Sources: fwd.com.my/about-us/tkfl/meet-our-team, firecrawl agents.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [No combined GRC role. Risk and compliance separate. Holder not publicly named. Sources: fwd.com.my, firecrawl agents.]",
        "Chief Risk Officer": "NOT FOUND [Not on Malaysia leadership page. May be regional FWD Group role. Sources: fwd.com.my, FWD Group regional pages, firecrawl agents.]",
        "Chief Information Officer": "NOT FOUND [Not on Malaysia leadership page. May be regional FWD Group role. Sources: fwd.com.my, firecrawl agents.]",
        "Head of Internal Audit": "NOT FOUND [Not publicly disclosed on Malaysia subsidiary site. Sources: fwd.com.my, firecrawl agents.]",
    },
    # Manulife Takaful - CISO, GRC remaining
    "Manulife Takaful Malaysia Berhad": {
        "Chief Information Security Officer": "NOT FOUND [No CISO named in Manulife Holdings Berhad Annual Report 2025 (Key Senior Management p.13, Head Office Management p.225), Corporate Governance Report 2025, manulife.com.my. CIO (Bernard Sia) likely oversees IT security. Sources: MHB AR 2025, manulife.com.my, firecrawl agents.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [No combined GRC role. Risk (CRO Mohd Naim) and Compliance (Senthil Woon) are separate functions. MHB does not use combined GRC title. Sources: MHB AR 2025, firecrawl agents.]",
    },
    # PruBSN Takaful - CISO, GRC, Compliance, CIO, IA
    "Prudential BSN Takaful Berhad": {
        "Chief Information Security Officer": "NOT FOUND [Not on PruBSN ExCo (8 members). Role exists per BNM takaful operator requirements but not publicly named. IT security likely at Prudential Malaysia group level. Sources: prubsn.com.my our-leaders, corporate-governance page, PruBSN Board Charter v4.0, firecrawl agents.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [No combined GRC role. Board Charter refers to 'Control Function Heads' (plural). Sources: prubsn.com.my, PruBSN Board Charter v4.0, firecrawl agents.]",
        "Head of Compliance": "NOT FOUND [Not on PruBSN ExCo. Per BNM requirements, Control Function Head for compliance must exist but not publicly named. Sources: prubsn.com.my, PruBSN Board Charter v4.0, firecrawl agents.]",
        "Chief Information Officer": "NOT FOUND [Not on PruBSN ExCo. IT function likely centralized at Prudential Assurance Malaysia Berhad. Sources: prubsn.com.my, firecrawl agents.]",
        "Head of Internal Audit": "NOT FOUND [Role of Internal Auditor exists per PruBSN Board Charter (overseen by Board Audit Committee) but not publicly named. Sources: prubsn.com.my, PruBSN Board Charter v4.0, firecrawl agents.]",
    },
    # MARA (2 rows) - GRC, CFO, CRO, Compliance, IA
    "MARA": {
        "Head of Governance Risk & Compliance": "NOT FOUND [MARA management team page (mara.gov.my) is fully image-based, 29 senior positions as image cards, no extractable titles. GRC equivalent would be a Timbalan Ketua Pengarah position. Sources: mara.gov.my management team, MARA org chart PNG, Wikipedia, firecrawl agents.]",
        "Chief Financial Officer": "NOT FOUND [CFO equivalent = Timbalan Ketua Pengarah MARA (Kewangan/Finance). Not identified from public sources. mara.gov.my management page is image-based. Sources: mara.gov.my, MARA org chart, firecrawl agents.]",
        "Chief Risk Officer": "NOT FOUND [MARA is non-financial-regulated government agency; CRO equivalent may not exist as standalone role. Risk function may be embedded under another Timbalan Ketua Pengarah portfolio. Sources: mara.gov.my, firecrawl agents.]",
        "Head of Compliance": "NOT FOUND [Compliance likely under corporate services / management services portfolio (Dr. Azmi bin Amat Murjan as Timbalan Ketua Pengarah Khidmat Pengurusan). Specific compliance head not identified. Sources: mara.gov.my, firecrawl agents.]",
        "Head of Internal Audit": "NOT FOUND [IA likely reports to Auditor General's Office or MARA Audit & Risk Committee. Not identified from public sources. Sources: mara.gov.my, firecrawl agents.]",
    },
    "MARA (Majlis Amanah Rakyat)": {
        "Head of Governance Risk & Compliance": "NOT FOUND [MARA management team page is image-based. GRC equivalent would be a Timbalan Ketua Pengarah position. Sources: mara.gov.my, MARA org chart, firecrawl agents.]",
        "Chief Financial Officer": "NOT FOUND [CFO equivalent = Timbalan Ketua Pengarah (Kewangan). Not identified. Sources: mara.gov.my, firecrawl agents.]",
        "Chief Risk Officer": "NOT FOUND [CRO equivalent may not exist as standalone role at government agency. Sources: mara.gov.my, firecrawl agents.]",
        "Head of Compliance": "NOT FOUND [Compliance likely under corporate services portfolio. Sources: mara.gov.my, firecrawl agents.]",
        "Head of Internal Audit": "NOT FOUND [IA likely reports to Auditor General. Sources: mara.gov.my, firecrawl agents.]",
    },
    # GrabPay - CISO, GRC, CRO, Compliance, IA
    "GrabPay (Grab Malaysia)": {
        "Chief Information Security Officer": "NOT FOUND [No executive directory on consumer-facing grab.com sites. CISO likely centralized at Grab Holdings (Singapore) group level. Sources: grab.com/my/, grab.com, Wikipedia Grab Holdings, firecrawl agents.]",
        "Head of Governance Risk & Compliance": "NOT FOUND [Not publicly disclosed. Likely centralized at Grab Financial Group (regional) or Grab Holdings (Singapore) level. Sources: grab.com, Wikipedia, firecrawl agents.]",
        "Chief Risk Officer": "NOT FOUND [Not publicly disclosed. Likely centralized at Grab Holdings group level. Sources: grab.com, Wikipedia, firecrawl agents.]",
        "Head of Compliance": "NOT FOUND [Per BNM e-money issuer requirements, GrabPay Malaysia must have local 'Senior Officer Responsible for Compliance' registered with BNM, but not publicly disclosed. Sources: grab.com, firecrawl agents.]",
        "Head of Internal Audit": "NOT FOUND [Not publicly disclosed. Likely centralized at Grab Holdings group level. Sources: grab.com, firecrawl agents.]",
    },
}

# --- CIO title correction for MARA (both rows) - update existing entry with more accurate title ---
CIO_CORRECTION_MARA = "Dr. Azmi bin Amat Murjan (Timbalan Ketua Pengarah MARA (Khidmat Pengurusan) / Ketua Pegawai Digital (CDO) - title is CDO not strictly CIO; portfolio includes cybersecurity action plan coordination) [Official: mara.gov.my, conf 80 - TITLE CORRECTED from CIO to CDO per Wikipedia verification]"

# --- PruBSN CRO stale flag (keep existing but add warning note) ---
PRUBSN_CRO_FLAG = "Anita Menon (Chief Risk Officer) [Malaysian Insurance Directory 2025/2026, conf 85 - STALE WARNING: NOT on current PruBSN ExCo as of Jul 2026 scrape (prubsn.com.my our-leaders lists 8 ExCo members, Anita Menon not among them). May refer to different Prudential entity or below ExCo level. Recommend verification via Prudential Assurance Malaysia Berhad AR or LinkedIn.]"

def is_filled(val):
    """Check if a cell is filled (not empty and not NOT FOUND)"""
    v = (val or "").strip()
    return bool(v) and not v.upper().startswith("NOT FOUND")

def main():
    # Copy v5.13 -> v5.14
    shutil.copy2(ENRICHED_SRC, ENRICHED_DST)
    print(f"Copied {ENRICHED_SRC} -> {ENRICHED_DST}")

    # Read all rows
    with open(ENRICHED_DST, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    stats = {
        "new_fills": 0,
        "corrections": 0,
        "not_found_added": 0,
        "title_corrections": 0,
        "stale_flags": 0,
        "institutions_touched": set(),
    }

    for row in rows:
        inst = row.get("Institution_Name", "")

        # Apply NEW FILLS
        if inst in NEW_FILLS:
            for role, val in NEW_FILLS[inst].items():
                if role in row and not is_filled(row[role]):
                    row[role] = val
                    stats["new_fills"] += 1
                    stats["institutions_touched"].add(inst)
                    print(f"  NEW FILL: {inst} -> {role}: {val[:60]}...")

        # Apply CORRECTIONS
        if inst in CORRECTIONS:
            for role, val in CORRECTIONS[inst].items():
                if role in row:
                    row[role] = val
                    stats["corrections"] += 1
                    stats["institutions_touched"].add(inst)
                    print(f"  CORRECTION: {inst} -> {role}: {val[:60]}...")

        # Apply NOT FOUND audit trails
        if inst in NOT_FOUND_ENTRIES:
            for role, val in NOT_FOUND_ENTRIES[inst].items():
                if role in row and not is_filled(row[role]) and not row[role].strip():
                    # Only fill empty cells (don't overwrite existing NOT FOUND)
                    row[role] = val
                    stats["not_found_added"] += 1
                    stats["institutions_touched"].add(inst)
                elif role in row and not is_filled(row[role]) and row[role].strip():
                    # Already has NOT FOUND text - check if ours is more detailed
                    if len(val) > len(row[role].strip()) + 50:
                        row[role] = val
                        stats["not_found_added"] += 1
                        stats["institutions_touched"].add(inst)

        # Apply CIO title correction for MARA (both rows)
        if inst in ("MARA", "MARA (Majlis Amanah Rakyat)"):
            if is_filled(row.get("Chief Information Officer", "")):
                row["Chief Information Officer"] = CIO_CORRECTION_MARA
                stats["title_corrections"] += 1
                stats["institutions_touched"].add(inst)
                print(f"  TITLE CORRECTION: {inst} -> CIO: updated to CDO")

        # Apply PruBSN CRO stale flag
        if inst == "Prudential BSN Takaful Berhad":
            if is_filled(row.get("Chief Risk Officer", "")) and "Anita Menon" in row.get("Chief Risk Officer", ""):
                row["Chief Risk Officer"] = PRUBSN_CRO_FLAG
                stats["stale_flags"] += 1
                stats["institutions_touched"].add(inst)
                print(f"  STALE FLAG: {inst} -> CRO: Anita Menon flagged as potentially stale")

    # Write updated enriched CSV
    with open(ENRICHED_DST, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nWritten {len(rows)} rows to {ENRICHED_DST}")

    # Compute coverage stats
    total_roles = len(rows) * 7
    filled = 0
    cluster = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
    for row in rows:
        f_count = sum(1 for r in ROLE_COLS if is_filled(row.get(r, "")))
        filled += f_count
        cluster[f_count] = cluster.get(f_count, 0) + 1

    print(f"\n=== v5.14 Coverage Stats ===")
    print(f"Total roles: {total_roles}, Filled: {filled}, Coverage: {filled/total_roles*100:.1f}%")
    for k in sorted(cluster.keys()):
        print(f"  {k}/7: {cluster[k]} institutions")

    print(f"\n=== Update Stats ===")
    print(f"  New fills: {stats['new_fills']}")
    print(f"  Corrections (misclassification): {stats['corrections']}")
    print(f"  NOT FOUND audit trails added: {stats['not_found_added']}")
    print(f"  Title corrections (MARA CIO->CDO): {stats['title_corrections']}")
    print(f"  Stale flags (PruBSN CRO): {stats['stale_flags']}")
    print(f"  Institutions touched: {len(stats['institutions_touched'])}")

    return cluster, filled, stats

if __name__ == "__main__":
    main()

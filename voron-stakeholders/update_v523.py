#!/usr/bin/env python3
"""
VoronDRQ Stakeholder Database Update Script — v5.23
Fills BigPay roles from TheOrg secondary source (crowd-sourced org chart).

Updates:
  1. BigPay (Capital A) — T4, E-Money — 3 new fills (CISO, CIO, Compliance) + CFO update
  2. BigPay Malaysia Sdn Bhd — T3, MSBs — 3 new fills (CISO, CIO, Compliance) + CFO update

Sources:
  - TheOrg BigPay Leadership Team: https://theorg.com/org/bigpay/teams/leadership-team
  - TheOrg BigPay Finance and Compliance Team: https://theorg.com/org/bigpay/teams/finance-and-compliance-team

Confidence: 65 (TheOrg — crowd-sourced secondary source, "Unverified" tag)
"""

import csv
import shutil
from pathlib import Path

WORKDIR = Path("/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders")
INPUT_FILE = WORKDIR / "prospect-database-enriched-v5.22.csv"
OUTPUT_FILE = WORKDIR / "prospect-database-enriched-v5.23.csv"

# Column order in the CSV
COLS = [
    "Tier", "Segment", "Institution_Name",
    "Chief Information Security Officer",
    "Head of Governance Risk & Compliance",
    "Chief Financial Officer",
    "Chief Risk Officer",
    "Head of Compliance",
    "Chief Information Officer",
    "Head of Internal Audit",
]

# ── BigPay data from TheOrg ──────────────────────────────────────────────
BIGPAY_CISO = (
    "Angus Thorn|Group Chief Information Security Officer|65|"
    "https://theorg.com/org/bigpay/teams/leadership-team|"
    "BigPay Group CISO [TheOrg crowd-sourced org chart, Unverified. "
    "BigPay = Capital A (formerly AirAsia) fintech subsidiary, BNM-licensed e-money issuer.]"
)

BIGPAY_CFO = (
    "Nicholas Chua|Chief Financial Officer|65|"
    "https://theorg.com/org/bigpay/teams/leadership-team|"
    "BigPay-specific CFO [TheOrg crowd-sourced org chart, Unverified]. "
    "Previous entry: Mun Hui Teh (CFO, Capital A Berhad parent, conf 80, capitala.com). "
    "BigPay has its own CFO distinct from parent Capital A CFO."
)

BIGPAY_CIO = (
    "Siddharth (Sid) R.|Group Chief Technology Officer|65|"
    "https://theorg.com/org/bigpay/teams/leadership-team|"
    "BigPay Group CTO [TheOrg crowd-sourced org chart, Unverified]. "
    "CTO function covers CIO/technology leadership at this fintech."
)

BIGPAY_COMPLIANCE = (
    "Divya Das|Head Of Compliance|65|"
    "https://theorg.com/org/bigpay/teams/finance-and-compliance-team|"
    "BigPay Head of Compliance (CAMS, ICA RC Dip) [TheOrg crowd-sourced org chart, Unverified]. "
    "Divya Das listed as 'Head Of Compliance - Bigpay (airasia Group Company)' on TheOrg Finance & Compliance Team page."
)

# Updated NOT FOUND notes for remaining BigPay gaps
BIGPAY_CRO_NOT_FOUND = (
    "NOT FOUND [BigPay does not publicly disclose a Chief Risk Officer. "
    "TheOrg lists Ryan Vinoth as 'Head of Credit Risk' (credit risk subset, not enterprise CRO). "
    "Capital A parent-level risk function may apply. conf 65]"
)

BIGPAY_IA_NOT_FOUND = (
    "NOT FOUND [BigPay does not publicly disclose a Head of Internal Audit. "
    "TheOrg org chart (6 teams, 49 people) lists no IA function. "
    "IA may be handled at Capital A group level. conf 65]"
)

BIGPAY_GRC_NOT_FOUND = (
    "NOT FOUND [BigPay does not publicly disclose a Head of GRC. "
    "GRC function likely split between Compliance (Divya Das) and Risk at Capital A group level. conf 65]"
)


def main():
    # Read input
    with open(INPUT_FILE, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames

    fills_count = 0
    updates_count = 0

    for row in rows:
        inst = row["Institution_Name"]

        if inst in ("BigPay (Capital A)", "BigPay Malaysia Sdn Bhd"):
            # CISO — NEW fill
            old_ciso = row["Chief Information Security Officer"]
            if old_ciso.startswith("NOT FOUND"):
                row["Chief Information Security Officer"] = BIGPAY_CISO
                fills_count += 1
                print(f"  [NEW] {inst}: CISO = Angus Thorn")

            # CFO — UPDATE (replace parent-level with BigPay-specific)
            old_cfo = row["Chief Financial Officer"]
            if "Mun Hui Teh" in old_cfo:
                row["Chief Financial Officer"] = BIGPAY_CFO
                updates_count += 1
                print(f"  [UPD] {inst}: CFO = Nicholas Chua (was Mun Hui Teh/parent)")

            # CIO — NEW fill
            old_cio = row["Chief Information Officer"]
            if old_cio.startswith("NOT FOUND"):
                row["Chief Information Officer"] = BIGPAY_CIO
                fills_count += 1
                print(f"  [NEW] {inst}: CIO = Siddharth (Sid) R.")

            # Compliance — NEW fill
            old_comp = row["Head of Compliance"]
            if old_comp.startswith("NOT FOUND"):
                row["Head of Compliance"] = BIGPAY_COMPLIANCE
                fills_count += 1
                print(f"  [NEW] {inst}: Compliance = Divya Das")

            # CRO — update NOT FOUND note
            row["Chief Risk Officer"] = BIGPAY_CRO_NOT_FOUND

            # IA — update NOT FOUND note
            row["Head of Internal Audit"] = BIGPAY_IA_NOT_FOUND

            # GRC — update NOT FOUND note
            row["Head of Governance Risk & Compliance"] = BIGPAY_GRC_NOT_FOUND

    # Write output
    with open(OUTPUT_FILE, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n=== UPDATE COMPLETE ===")
    print(f"  New fills:    {fills_count}")
    print(f"  CFO updates:  {updates_count}")
    print(f"  Output:       {OUTPUT_FILE}")

    # Quick stats
    named = 0
    not_found = 0
    for row in rows:
        for col in COLS[3:]:
            val = row.get(col, "")
            if val.startswith("NOT FOUND"):
                not_found += 1
            elif val:
                named += 1
    total = named + not_found
    print(f"\n  Total cells:   {total}")
    print(f"  Named:         {named} ({100*named/total:.1f}%)")
    print(f"  NOT FOUND:     {not_found} ({100*not_found/total:.1f}%)")


if __name__ == "__main__":
    main()

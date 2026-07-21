#!/usr/bin/env python3
"""Update v5.23 -> v5.24: 3 new fills (Soft Space CIO, PruBSN CRO, PruBSN Compliance)."""
import csv, shutil

SRC = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.23.csv'
DST = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.24.csv'

# Read preserving BOM + \r\n
with open(SRC, encoding='utf-8-sig', newline='') as f:
    raw = f.read()

# Parse with csv to get fieldnames + rows
rows_list = []
reader = csv.DictReader(open(SRC, encoding='utf-8-sig', newline=''))
fieldnames = reader.fieldnames
for r in reader:
    rows_list.append(r)

print(f"Loaded {len(rows_list)} rows, fields: {fieldnames}")

# Define new values (pipe-delimited structured format)
new_vals = {
    ('Soft Space Sdn Bhd', 'Chief Information Officer'):
        'Nicholas Lim|Chief Technology Officer|65|https://theorg.com/org/soft-space|TheOrg org chart (Unverified) lists Nicholas Lim as Chief Technology Officer at Soft Space (KL HQ, 51-200 employees, softspace.com.my). Corrects prior v5.23 NOT FOUND "does not publicly list C-suite executives" which was based on Firecrawl agent research that missed TheOrg data. Cross-ref: RocketReach also lists Nicholas Lim as CTO.',
    ('Prudential BSN Takaful Berhad', 'Chief Risk Officer'):
        'Anita Menon|Chief Risk Officer|80|https://theorg.com/org/prudential-bsn-takaful-berhad/org-chart/anita-menon-acma|REINSTATED from v5.23 STALE note. Anita Menon confirmed CURRENT CRO via 4 independent sources: (1) TheOrg "joined PruBSN as CRO in 2012, a position they hold to this day"; (2) LeadIQ (May 2026) "Chief Risk Officer: A.M.A." (= Anita Menon ACMA); (3) ContactOut "Anita Menon Acma Chief Risk Officer"; (4) TheOfficialBoard bio. Prior v5.23 note ("not on current ExCo scrape, may have departed") was over-pessimistic - CRO is not on the ExCo page subset. Multi-source cross-referenced, present-tense confirmation.',
    ('Prudential BSN Takaful Berhad', 'Head of Compliance'):
        'Anita Menon|Chief Risk Officer / Chief Compliance Officer (combined role)|70|https://theorg.com/org/prudential-bsn-takaful-berhad/org-chart/anita-menon-acma|Inferred combined role: PruBSN 2025 Audited FS references a single combined "Chief Risk Officer (CRO) / Chief Compliance Officer" position. Anita Menon confirmed as CRO (multi-source, conf 80) -> holds combined CRO/CCO role. No separate Chief Compliance Officer listed in TheOrg, LeadIQ, or ContactOut. Confidence 70 (inference from FS combined-role reference + CRO confirmation).',
}

updated = 0
for r in rows_list:
    inst = r['Institution_Name']
    for (tgt_inst, col), val in new_vals.items():
        if inst == tgt_inst:
            old = r.get(col, '')
            r[col] = val
            updated += 1
            print(f"  UPDATED [{inst}] {col}:")
            print(f"    OLD: {old[:90]}...")
            print(f"    NEW: {val[:90]}...")

print(f"\nTotal cells updated: {updated}")

# Write v5.24 with BOM + \r\n (matching source format)
with open(DST, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator='\r\n')
    writer.writeheader()
    for r in rows_list:
        writer.writerow(r)

# Verify
import os
print(f"\nWrote {DST} ({os.path.getsize(DST)} bytes)")
print(f"Source was {os.path.getsize(SRC)} bytes")

# Recount named/NOT FOUND for v5.24
roles = ['Chief Information Security Officer','Head of Governance Risk & Compliance','Chief Financial Officer','Chief Risk Officer','Head of Compliance','Chief Information Officer','Head of Internal Audit']
named = sum(1 for r in rows_list for col in roles if r.get(col,'').strip() and not r.get(col,'').strip().startswith('NOT FOUND'))
nf = sum(1 for r in rows_list for col in roles if r.get(col,'').strip().startswith('NOT FOUND'))
total = len(rows_list)*7
print(f"\nv5.24 stats: Named={named} ({100*named/total:.1f}%), NOT FOUND={nf} ({100*nf/total:.1f}%), Total={total}")
print(f"v5.23 was: Named=832 (58.0%), NOT FOUND=603")
print(f"Net change: +{named-832} named, -{832-named+0} NOT FOUND")

#!/usr/bin/env python3
"""
VoronDRQ NOT FOUND Cell Cleanup Script
======================================
Strips bracketed/context text from all NOT FOUND cells, leaving them empty.

Handles three patterns:
  1. "NOT FOUND [bracketed context]"  → ""  (386 cells in v5.90)
  2. "NOT FOUND — em-dash context"     → ""  (67 cells in v5.90)
  3. "NOT FOUND" (plain)               → ""

Preserves:
  - Named executives (everything else)
  - ENTITY WOUND DOWN / ENTITY LIKELY INACTIVE / SHARES PARENT classifications
  - All other columns untouched

Usage:
  python3 clean-not-found-cells.py <input.csv> [output.csv]

If no output path given, writes to <input-basename>-clean.csv
"""

import csv
import sys
import os
import re
from datetime import datetime

def is_not_found(value: str) -> bool:
    """Check if a cell value is a NOT FOUND entry (with or without context)."""
    return value.strip().startswith('NOT FOUND')

def clean_cell(value: str) -> str:
    """Strip NOT FOUND context, return empty string."""
    if is_not_found(value):
        return ''
    return value

def is_entity_class(value: str) -> bool:
    """Check if a cell is a legitimate entity classification (not NOT FOUND)."""
    v = value.strip()
    return v.startswith(('ENTITY WOUND DOWN', 'ENTITY LIKELY INACTIVE', 'SHARES PARENT'))

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 clean-not-found-cells.py <input.csv> [output.csv]")
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print(f"ERROR: Input file not found: {input_path}")
        sys.exit(1)

    # Default output path
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}-clean{ext}"

    # VoronDRQ stakeholder role columns
    role_cols = [
        'Chief Information Security Officer',
        'Head of Governance Risk & Compliance',
        'Chief Financial Officer',
        'Chief Risk Officer',
        'Head of Compliance',
        'Chief Information Officer',
        'Head of Internal Audit',
    ]

    # Stats
    stats = {
        'total_cells': 0,
        'named': 0,
        'entity': 0,
        'not_found_cleaned': 0,
        'not_found_bracket': 0,
        'not_found_emdash': 0,
        'not_found_plain': 0,
        'already_empty': 0,
        'rows': 0,
    }

    # Track what was cleaned for the report
    cleaned_log = []

    with open(input_path, 'r', encoding='utf-8-sig') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        # Verify role columns exist
        missing = [c for c in role_cols if c not in fieldnames]
        if missing:
            print(f"WARNING: Role columns not found in CSV: {missing}")
            print(f"Available columns: {fieldnames}")

        with open(output_path, 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                stats['rows'] += 1
                inst_name = row.get('Institution_Name', '')
                for col in role_cols:
                    if col not in row:
                        continue
                    val = (row[col] or '').strip()
                    stats['total_cells'] += 1

                    if not val:
                        stats['already_empty'] += 1
                    elif is_not_found(val):
                        stats['not_found_cleaned'] += 1
                        # Classify the pattern
                        if '[' in val:
                            stats['not_found_bracket'] += 1
                        elif '—' in val or ' - ' in val:
                            stats['not_found_emdash'] += 1
                        else:
                            stats['not_found_plain'] += 1

                        cleaned_log.append({
                            'institution': inst_name,
                            'role': col,
                            'original': val[:100],
                            'pattern': 'bracket' if '[' in val else ('emdash' if '—' in val or ' - ' in val else 'plain'),
                        })
                        row[col] = ''
                    elif is_entity_class(val):
                        stats['entity'] += 1
                    else:
                        stats['named'] += 1

                writer.writerow(row)

    # Print summary
    print("=" * 60)
    print("VoronDRQ NOT FOUND Cleanup Report")
    print("=" * 60)
    print(f"Input:  {input_path}")
    print(f"Output: {output_path}")
    print(f"Date:   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    print(f"Total rows:          {stats['rows']}")
    print(f"Total role cells:    {stats['total_cells']}")
    print()
    print("--- BEFORE ---")
    print(f"  Named:                  {stats['named']}")
    print(f"  Entity-classified:      {stats['entity']}")
    print(f"  NOT FOUND [bracket]:    {stats['not_found_bracket']}")
    print(f"  NOT FOUND — emdash:     {stats['not_found_emdash']}")
    print(f"  NOT FOUND (plain):      {stats['not_found_plain']}")
    print(f"  Already empty:          {stats['already_empty']}")
    print()
    print("--- AFTER ---")
    total_empty = stats['not_found_cleaned'] + stats['already_empty']
    print(f"  Named:                  {stats['named']}")
    print(f"  Entity-classified:      {stats['entity']}")
    print(f"  Empty (was NOT FOUND):  {stats['not_found_cleaned']}")
    print(f"  Empty (was already):    {stats['already_empty']}")
    print(f"  Total empty:            {total_empty}")
    print()
    effective = stats['named'] + stats['entity']
    total = stats['total_cells']
    print(f"  Effective coverage:     {effective}/{total} = {effective/total*100:.1f}%")
    print(f"  Cells cleaned:          {stats['not_found_cleaned']}")
    print()

    # Pattern breakdown
    print("--- CLEANED PATTERNS ---")
    print(f"  'NOT FOUND [context]':   {stats['not_found_bracket']} cells")
    print(f"  'NOT FOUND — context':   {stats['not_found_emdash']} cells")
    print(f"  'NOT FOUND' (plain):     {stats['not_found_plain']} cells")
    print()

    # Sample of cleaned cells
    if cleaned_log:
        print("--- SAMPLE (first 10 cleaned) ---")
        for entry in cleaned_log[:10]:
            print(f"  {entry['institution']} | {entry['role']}")
            print(f"    Pattern: {entry['pattern']}")
            print(f"    Was: {entry['original']}...")
            print()

    print("=" * 60)
    print("Done. Review output file before promoting.")
    print("=" * 60)

if __name__ == '__main__':
    main()

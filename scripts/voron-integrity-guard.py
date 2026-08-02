#!/usr/bin/env python3
"""
VoronDRQ Prospect Database — Version Integrity Guard
Ensures no institutions or named cells are lost during version transitions.

Usage:
  python3 voron-integrity-guard.py <new_csv> <previous_csv> [--fix] [--report <path>]

Modes:
  --check (default)  Report any data loss; exit 1 if institutions dropped
  --fix              Auto-remediate: carry forward dropped institutions + regressed cells

Exit codes:
  0 = clean (no data loss)
  1 = data loss detected (check mode) or fixed (fix mode)
  2 = error

TLP:AMBER — Commercial Intelligence
"""
import csv
import sys
import os
import argparse
from datetime import datetime

ROLE_COLS = [
    'Chief Information Security Officer',
    'Head of Governance Risk & Compliance',
    'Chief Financial Officer',
    'Chief Risk Officer',
    'Head of Compliance',
    'Chief Information Officer',
    'Head of Internal Audit',
]

def is_named(val):
    v = val.strip()
    return v and v != "NOT FOUND" and v != "NOT YET RESEARCHED"

def read_csv(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames
    return rows, fieldnames

def count_named(rows):
    named = 0
    full = 0
    for r in rows:
        inst_named = sum(1 for col in ROLE_COLS if is_named(r.get(col, '')))
        named += inst_named
        if inst_named == 7:
            full += 1
    return named, full

def main():
    parser = argparse.ArgumentParser(description='VoronDRQ Prospect DB Integrity Guard')
    parser.add_argument('new_csv', help='New version CSV path')
    parser.add_argument('prev_csv', help='Previous version CSV path')
    parser.add_argument('--fix', action='store_true', help='Auto-remediate data loss')
    parser.add_argument('--report', default=None, help='Write report to this path')
    parser.add_argument('--output', default=None, help='Write fixed CSV to this path (fix mode)')
    args = parser.parse_args()

    if not os.path.exists(args.new_csv):
        print(f"ERROR: new CSV not found: {args.new_csv}")
        sys.exit(2)
    if not os.path.exists(args.prev_csv):
        print(f"ERROR: previous CSV not found: {args.prev_csv}")
        sys.exit(2)

    new_rows, fieldnames = read_csv(args.new_csv)
    prev_rows, _ = read_csv(args.prev_csv)

    prev_idx = {r['Institution_Name']: r for r in prev_rows}
    new_idx = {r['Institution_Name']: r for r in new_rows}

    prev_named, prev_full = count_named(prev_rows)
    new_named, new_full = count_named(new_rows)

    issues = []

    # 1. Dropped institutions
    dropped = [name for name in prev_idx if name not in new_idx]
    for name in dropped:
        row = prev_idx[name]
        named_count = sum(1 for col in ROLE_COLS if is_named(row.get(col, '')))
        issues.append({
            'type': 'DROPPED_INSTITUTION',
            'severity': 'CRITICAL' if named_count > 0 else 'WARNING',
            'institution': name,
            'tier': row.get('Tier', '?'),
            'segment': row.get('Segment', '?'),
            'named_cells': named_count,
            'detail': f"Institution with {named_count}/7 named cells dropped from new version"
        })

    # 2. Cell regressions (named → empty/NOT FOUND/pending)
    for name in new_idx:
        if name in prev_idx:
            prev_row = prev_idx[name]
            new_row = new_idx[name]
            for col in ROLE_COLS:
                prev_val = prev_row.get(col, '').strip()
                new_val = new_row.get(col, '').strip()
                if is_named(prev_val) and not is_named(new_val):
                    issues.append({
                        'type': 'CELL_REGRESSION',
                        'severity': 'CRITICAL',
                        'institution': name,
                        'role': col,
                        'old_value': prev_val,
                        'new_value': new_val if new_val else '(empty)',
                        'detail': f"Named cell regressed: '{prev_val}' → '{new_val if new_val else '(empty)'}'"
                    })

    # 3. Tier/Segment changes (informational)
    for name in new_idx:
        if name in prev_idx:
            for meta_col in ('Tier', 'Segment'):
                prev_val = prev_idx[name].get(meta_col, '').strip()
                new_val = new_idx[name].get(meta_col, '').strip()
                if prev_val and new_val and prev_val != new_val:
                    issues.append({
                        'type': 'METADATA_CHANGE',
                        'severity': 'INFO',
                        'institution': name,
                        'role': meta_col,
                        'old_value': prev_val,
                        'new_value': new_val,
                        'detail': f"{meta_col} changed: {prev_val} → {new_val}"
                    })

    # Summary
    critical = [i for i in issues if i['severity'] == 'CRITICAL']
    warnings = [i for i in issues if i['severity'] == 'WARNING']
    info = [i for i in issues if i['severity'] == 'INFO']

    print(f"\n{'='*60}")
    print(f"VoronDRQ Integrity Guard — Version Comparison")
    print(f"{'='*60}")
    print(f"Previous: {args.prev_csv} ({len(prev_rows)} institutions, {prev_named} named, {prev_full} full 7/7)")
    print(f"New:      {args.new_csv} ({len(new_rows)} institutions, {new_named} named, {new_full} full 7/7)")
    print(f"{'='*60}")
    print(f"Issues found: {len(critical)} CRITICAL, {len(warnings)} WARNING, {len(info)} INFO")

    if dropped:
        print(f"\n❌ DROPPED INSTITUTIONS ({len(dropped)}):")
        for name in dropped:
            row = prev_idx[name]
            nc = sum(1 for col in ROLE_COLS if is_named(row.get(col, '')))
            flag = "⚠️  HAS NAMED DATA" if nc > 0 else "    (no named data)"
            print(f"  {flag} {name} (T{row.get('Tier','?')}, {row.get('Segment','?')}) — {nc}/7 named")

    cell_regressions = [i for i in issues if i['type'] == 'CELL_REGRESSION']
    if cell_regressions:
        print(f"\n❌ CELL REGRESSIONS ({len(cell_regressions)}):")
        for i in cell_regressions[:20]:
            print(f"  {i['institution']} | {i['role']} | '{i['old_value']}' → '{i['new_value']}'")
        if len(cell_regressions) > 20:
            print(f"  ... and {len(cell_regressions) - 20} more")

    # Fix mode
    if args.fix and issues:
        output_path = args.output or args.new_csv.replace('.csv', '-integrity-fixed.csv')
        fixed_rows = list(new_rows)  # start with new
        fixed_idx = {r['Institution_Name']: r for r in fixed_rows}

        # Restore dropped institutions
        restored = 0
        for name in dropped:
            if name not in fixed_idx:
                fixed_rows.append(dict(prev_idx[name]))
                fixed_idx[name] = prev_idx[name]
                restored += 1

        # Restore regressed cells
        cells_restored = 0
        for name in fixed_idx:
            if name in prev_idx:
                for col in ROLE_COLS:
                    prev_val = prev_idx[name].get(col, '').strip()
                    cur_val = fixed_idx[name].get(col, '').strip()
                    if is_named(prev_val) and not is_named(cur_val):
                        fixed_idx[name][col] = prev_val
                        cells_restored += 1

        with open(output_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(fixed_rows)

        fixed_named, fixed_full = count_named(fixed_rows)
        print(f"\n✅ REMEDIATED:")
        print(f"   Restored {restored} dropped institutions")
        print(f"   Restored {cells_restored} regressed cells")
        print(f"   Output: {output_path} ({len(fixed_rows)} institutions, {fixed_named} named, {fixed_full} full 7/7)")

    # Write report
    report_path = args.report
    if not report_path:
        report_path = os.path.join(os.path.dirname(args.new_csv), 'integrity-guard-report.md')

    report = f"""# VoronDRQ Integrity Guard Report

**Generated:** {datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}
**Previous:** {args.prev_csv} ({len(prev_rows)} institutions, {prev_named} named, {prev_full} full 7/7)
**New:** {args.new_csv} ({len(new_rows)} institutions, {new_named} named, {new_full} full 7/7)

---

## Summary

| Metric | Previous | New | Delta |
|--------|----------|-----|-------|
| Institutions | {len(prev_rows)} | {len(new_rows)} | {len(new_rows) - len(prev_rows):+d} |
| Named cells | {prev_named} | {new_named} | {new_named - prev_named:+d} |
| Full 7/7 | {prev_full} | {new_full} | {new_full - prev_full:+d} |

## Issues: {len(critical)} CRITICAL, {len(warnings)} WARNING, {len(info)} INFO

"""

    if dropped:
        report += "### Dropped Institutions\n\n"
        for name in dropped:
            row = prev_idx[name]
            nc = sum(1 for col in ROLE_COLS if is_named(row.get(col, '')))
            report += f"- **{name}** (T{row.get('Tier','?')}, {row.get('Segment','?')}) — {nc}/7 named cells\n"
        report += "\n"

    if cell_regressions:
        report += "### Cell Regressions\n\n"
        report += "| Institution | Role | Old Value | New Value |\n"
        report += "|-------------|------|-----------|-----------|\n"
        for i in cell_regressions:
            report += f"| {i['institution']} | {i['role']} | {i['old_value']} | {i['new_value']} |\n"
        report += "\n"

    if args.fix:
        report += f"### Remediation\n\n- Restored {restored} dropped institutions\n- Restored {cells_restored} regressed cells\n- Output: `{output_path}`\n"

    with open(report_path, 'w') as f:
        f.write(report)
    print(f"\n📄 Report: {report_path}")

    if critical and not args.fix:
        print(f"\n❌ CRITICAL DATA LOSS DETECTED — use --fix to auto-remediate")
        sys.exit(1)
    elif critical and args.fix:
        print(f"\n✅ Data loss remediated — review output file before promoting to canonical")
        sys.exit(0)
    else:
        print(f"\n✅ No critical data loss detected")
        sys.exit(0)

if __name__ == '__main__':
    main()

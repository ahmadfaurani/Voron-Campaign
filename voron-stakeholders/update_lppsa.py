import csv

infile = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.44.csv'
rows = []
with open(infile, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

updates = 0
src = 'lppsa.gov.my/v3/en/pengurusan (official LPPSA Management page; 22 management profile PNG images extracted via Tesseract OCR, Jul 2025)'

for r in rows:
    if r['Institution_Name'] == 'LPPSA':
        # CFO
        if 'NOT FOUND' in r['Chief Financial Officer']:
            r['Chief Financial Officer'] = f"Mohd Zawawi bin Mohd Muhiddin (Chief Finance Officer, Financial Management & Services Division) [HIGH confidence — Official: {src}]"
            updates += 1
        # CIO
        if 'NOT FOUND' in r['Chief Information Officer']:
            r['Chief Information Officer'] = f"Mohd Nor Ferim bin Mohd Simin (Assistant General Manager, Information Communication and Technology Department) [MEDIUM-HIGH confidence — Official: {src}]"
            updates += 1
        # Head of Compliance
        if 'NOT FOUND' in r['Head of Compliance']:
            r['Head of Compliance'] = f"Zahari bin Mohd Alias (Senior Manager, Integrity & Compliance Department) [MEDIUM-HIGH confidence — Official: {src}]"
            updates += 1
        # Head of Internal Audit
        if 'NOT FOUND' in r['Head of Internal Audit']:
            r['Head of Internal Audit'] = f"Yuzrah binti Mahmud (Assistant General Manager, Internal Audit Department) [MEDIUM-HIGH confidence — Official: {src}]"
            updates += 1
        # CISO - confirmed absence
        if 'NOT FOUND' in r['Chief Information Security Officer']:
            r['Chief Information Security Officer'] = f"NOT FOUND — No dedicated CISO at LPPSA (government agency). ICT function managed by AGM Mohd Nor Ferim bin Mohd Simin. No information security officer among 22 management profiles. [Confirmed: {src}]"
            updates += 1
        # CRO - confirmed absence
        if 'NOT FOUND' in r['Chief Risk Officer']:
            r['Chief Risk Officer'] = f"NOT FOUND — No dedicated CRO at LPPSA. Corporate Assurance Division (GM Nazhalina binti Nazri) covers some risk-adjacent functions. [Confirmed: {src}]"
            updates += 1
        # GRC - confirmed absence
        if 'NOT FOUND' in r['Head of Governance Risk & Compliance']:
            r['Head of Governance Risk & Compliance'] = f"NOT FOUND — No standalone GRC role at LPPSA. Integrity & Compliance Dept (Zahari bin Mohd Alias) covers compliance. [Confirmed: {src}]"
            updates += 1
        print(f"Updated LPPSA: {updates} fields")
        break

with open(infile, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Total updates: {updates}")
print(f"Total rows: {len(rows)}")

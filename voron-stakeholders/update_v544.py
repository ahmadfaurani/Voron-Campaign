import csv

infile = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.44.csv'
rows = []
with open(infile, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for r in reader:
        rows.append(r)

updates = 0
for r in rows:
    name = r['Institution_Name']

    # AmMetLife: upgrade Comp, IA, CISO, GRC from "page failed" to "confirmed absence"
    if name == 'AmMetLife Insurance Berhad':
        r['Head of Compliance'] = 'NOT FOUND [Confirmed absence: Official AmMetLife Management Team page (ammetlife.com/about-us/about-ammetlife/management-team) lists 8 Senior Management members: CEO (Wan Saifulrizal Wan Ismail), CFO (Michelle Cheang), CIO (Loh Tian Hu), CTO (Nelson Yu), CIO-investments (Philomena Jan), CRO (Low Siew Mooi), Chief Bancassurance Officer (Lee Wai Yee), Chief Corporate Solutions Officer (Marc Ooi). No Head of Compliance among them — compliance function may be shared with MetLife APAC or AmBank group. conf 90, Jul 2025]'
        r['Head of Internal Audit'] = 'NOT FOUND [Confirmed absence: Official AmMetLife Management Team page (ammetlife.com/about-us/about-ammetlife/management-team) lists 8 Senior Management members (see Compliance entry). No Head of Internal Audit / Chief Audit Executive among them — internal audit function may be shared with MetLife APAC. conf 90, Jul 2025]'
        r['Chief Information Security Officer'] = 'NOT FOUND [Confirmed absence: Official AmMetLife Management Team page (ammetlife.com/about-us/about-ammetlife/management-team) lists 8 Senior Management members (see Compliance entry). No CISO among them — CISO function likely shared with MetLife APAC regional level. conf 85, Jul 2025]'
        r['Head of Governance Risk & Compliance'] = 'NOT FOUND [Confirmed absence: Official AmMetLife Management Team page (ammetlife.com/about-us/about-ammetlife/management-team) lists 8 Senior Management members. No dedicated Head of GRC; risk function covered by CRO Low Siew Mooi. conf 85, Jul 2025]'
        updates += 4
        print(f"Updated AmMetLife Insurance Berhad: Comp, IA, CISO, GRC -> confirmed absence (official mgmt team page)")

with open(infile, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"\nTotal updates: {updates}")
print(f"Total rows: {len(rows)}")

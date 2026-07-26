import csv, shutil

v551_path = '/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v5.51.csv'
canon_paths = [
    '/home/p62operator/.openclaw/workspace-hoi/vorondrq-rmit-campaign/prospects/prospect-database-7stakeholders.csv',
    '/home/p62operator/.openclaw/workspace-hoi/vorondrq-rmit-campaign/operations/prospect-databases/prospect-database-7stakeholders.csv',
]

# Load v5.51 working DB
with open(v551_path, encoding='utf-8-sig') as f:
    v551 = {r.get('Institution_Name','').strip(): r for r in csv.DictReader(f)}

# The 4 pending T1 fills: (institution, role)
fills = [
    ('Public Bank Berhad', 'Chief Information Security Officer'),
    ('Public Islamic Bank Berhad', 'Chief Information Security Officer'),
    ('Bank Muamalat Malaysia Berhad', 'Chief Information Security Officer'),
    ('ICBC (Malaysia) Berhad', 'Chief Financial Officer'),
]

for cpath in canon_paths:
    with open(cpath, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames
    applied = []
    for inst, role in fills:
        for r in rows:
            if r.get('Institution_Name','').strip() == inst:
                old = r.get(role,'')
                new = v551.get(inst, {}).get(role, '')
                if new and not old.strip():
                    r[role] = new
                    applied.append(f"  {inst} / {role[:35]}: EMPTY -> {new[:70]}")
                elif new and old.strip():
                    applied.append(f"  {inst} / {role[:35]}: already filled (skip)")
                else:
                    applied.append(f"  {inst} / {role[:35]}: v5.51 has no value")
                break
        else:
            applied.append(f"  {inst}: NOT FOUND in canonical")
    with open(cpath, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"=== Applied to {cpath.split('/')[-2]}/{cpath.split('/')[-1]} ===")
    for a in applied:
        print(a)
    print()
print("DONE: 4 T1 fills applied to both canonical CSV copies.")

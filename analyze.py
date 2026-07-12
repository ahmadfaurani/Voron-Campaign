import csv, json, sys
from collections import OrderedDict

CSV = "/home/p62operator/.openclaw/workspace-hoi/vorondrq-rmit-campaign/current.csv"

with open(CSV, newline='', encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))

# stakeholder columns = all except Tier, Segment, Institution_Name
meta_cols = ['Tier', 'Segment', 'Institution_Name']
stake_cols = [c for c in rows[0].keys() if c not in meta_cols] if rows else []

def nonempty(v):
    return v is not None and v.strip() != ''

total = len(rows)
tier_counts = OrderedDict()
seg_counts = OrderedDict()
stake_populated = OrderedDict((c,0) for c in stake_cols)
prospects_with_contacts = 0
fully_enriched = 0
empty_prospects = 0
total_contact_cells = 0
enriched_inst = OrderedDict()   # name -> contact count
tier1_with_contacts = []        # list of (name, count)
institution_contact_counts = {} # name -> count (for diffing)

for r in rows:
    tier = (r.get('Tier') or '').strip()
    seg = (r.get('Segment') or '').strip()
    name = (r.get('Institution_Name') or '').strip()
    tier_counts[tier] = tier_counts.get(tier,0)+1
    seg_counts[seg] = seg_counts.get(seg,0)+1
    cnt = 0
    for c in stake_cols:
        if nonempty(r.get(c)):
            stake_populated[c]+=1
            cnt+=1
            total_contact_cells+=1
    institution_contact_counts[name]=cnt
    if cnt>0:
        prospects_with_contacts+=1
        enriched_inst[name]=cnt
        if cnt==len(stake_cols):
            fully_enriched+=1
    else:
        empty_prospects+=1
    if tier=='1' and cnt>0:
        tier1_with_contacts.append((name,cnt))

enrichment_rate = round(100.0*prospects_with_contacts/total,1) if total else 0.0

# completion rate per role (populated / total prospects)
stake_completion = OrderedDict((c, round(100.0*stake_populated[c]/total,1)) for c in stake_cols)

# sort enriched institutions by contact count desc
enriched_sorted = OrderedDict(sorted(enriched_inst.items(), key=lambda kv: (-kv[1], kv[0])))
tier1_with_contacts.sort(key=lambda x:(-x[1], x[0]))

result = {
  "total_prospects": total,
  "prospects_with_contacts": prospects_with_contacts,
  "empty_prospects": empty_prospects,
  "enrichment_rate": enrichment_rate,
  "fully_enriched": fully_enriched,
  "total_contact_cells": total_contact_cells,
  "stakeholder_role_count": len(stake_cols),
  "tier_counts": dict(tier_counts),
  "segment_counts": dict(seg_counts),
  "stakeholder_populated": dict(stake_populated),
  "stakeholder_completion_pct": dict(stake_completion),
  "enriched_institutions": dict(enriched_sorted),
  "tier1_banks_with_contacts": [n for n,_ in tier1_with_contacts],
  "tier1_banks_with_contacts_detail": [{"name":n,"contacts":c} for n,c in tier1_with_contacts],
  "all_institution_contact_counts": institution_contact_counts,
}
print(json.dumps(result, indent=2, ensure_ascii=False))

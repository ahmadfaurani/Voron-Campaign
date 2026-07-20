import csv, json, re
from collections import Counter

with open('root-csv.csv', encoding='utf-8-sig', newline='') as f:
    rows = list(csv.reader(f))
header = rows[0]; data = rows[1:]

# Exclude phantom: Tier col must be a single digit 1-6
real = [r for r in data if r[0].strip() in ('1','2','3','4','5','6')]
phantom = [r for r in data if r[0].strip() not in ('1','2','3','4','5','6')]
N = len(real)
ROLE_COLS = [('CISO',3),('GRC',4),('CFO',5),('CRO',6),('Compliance',7),('CIO',8),('IA',9)]

def classify(cell):
    c = cell.strip()
    if not c: return ('empty', None)
    cu = c.upper()
    if cu.startswith('NOT FOUND') or 'NOT FOUND' in cu[:25]: return ('notfound', c)
    if cu.startswith('CEO:') or cu.startswith('CEO '): return ('ceo_misfiled', c)
    return ('real', c)

tier=Counter(); seg=Counter()
rnom=Counter(); rtru=Counter(); rnf=Counter(); rceo=Counter()
with_one_real=0; with_one_nom=0; empty=0; no_real=0
full7_nom=[]; full7_true=[]
nom_cells=0; tru_cells=0
ceo_insts=[]; nf_pairs=[]
per=[]

for r in real:
    tier[r[0].strip()]+=1; seg[r[1].strip()]+=1
    name=r[2].strip(); roles={}; nr=0; nn=0
    for role,ci in ROLE_COLS:
        cell=r[ci] if ci<len(r) else ''
        k,t=classify(cell); roles[role]=(k,t)
        if k!='empty': rnom[role]+=1; nom_cells+=1; nn+=1
        if k=='real': rtru[role]+=1; tru_cells+=1; nr+=1
        if k=='notfound': rnf[role]+=1; nf_pairs.append((name,role))
        if k=='ceo_misfiled' and role=='CISO': rceo[role]+=1; ceo_insts.append(name)
    if nr>=1: with_one_real+=1
    if nn>=1: with_one_nom+=1
    if nn==0: empty+=1
    if nr==0: no_real+=1
    if nn==7: full7_nom.append(name)
    if nr==7: full7_true.append(name)
    per.append((r[0].strip(),r[1].strip(),name,nr,nn,roles))

poss=N*7

# v5.8 baseline from memory
base=json.load(open('/home/p62operator/.hermes/memories/voron-prospect-monitor.json'))
bt=base['tier']; brn=base['role_pop_nominal']; brt=base['role_pop_true']
bnf=base.get('role_notfound',{}) if isinstance(base.get('role_notfound'),dict) else {}
bceo=base.get('role_ceo_misfiled_count', base.get('role_ceo_misfiled_in_ciso',27))
bwc_nom=base['with_contacts_nominal']; bwc_tru=base['with_contacts_true']
benr_nom=base['enrichment_rate_nominal']; benr_tru=base['enrichment_rate_true']
bcells_nom=base['total_cells_nominal']; bcells_tru=base['total_cells_true']
bcfr_nom=base['cell_fill_rate_nominal']; bcfr_tru=base['cell_fill_rate_true']
bfull_nom=base['full_all_nominal']; bfull_tru=base['full_all_true']
bt1_full_tru=base['t1_full_true']; bt1_full_nom=base['t1_full_nominal']
bt1_names=set(base['t1_full_names_true'])

print("="*72)
print(f"REAL INSTITUTIONS: {N}  (raw {len(data)} = {N} real + {len(phantom)} phantom)")
print(f"Phantom rows excluded: {len(phantom)}  -> {phantom[0][0][:55] if phantom else 'none'}")
print("="*72)
print("\n--- COMPOSITION (unchanged vs v5.8) ---")
print("Tier:", dict(sorted(tier.items())), " sum=",sum(tier.values()))
print("Segments:", dict(sorted(seg.items(), key=lambda x:-x[1])))

print("\n--- ROLE COMPLETION (TRUE = real contacts only) ---")
print(f"{'Role':11}{'Nom':>6}{'True':>6}{'NF':>5}{'CEOmis':>8}{'Nom%':>7}{'True%':>7}{'dTrue':>7}")
for role,_ in ROLE_COLS:
    nom=rnom[role]; tru=rtru[role]
    dtru = tru - brt.get(role,0)
    print(f"{role:11}{nom:6}{tru:6}{rnf[role]:5}{rceo.get(role,0):8}{nom/N*100:6.1f}%{tru/N*100:6.1f}%{dtru:+7d}")

print("\n--- ENRICHMENT RATE ---")
print(f"NOMINAL >=1 contact: {with_one_nom}/{N} = {with_one_nom/N*100:.1f}%  (v5.8: {bwc_nom}={benr_nom}%)  Δ={with_one_nom-bwc_nom:+d}")
print(f"TRUE    >=1 contact: {with_one_real}/{N} = {with_one_real/N*100:.1f}%  (v5.8: {bwc_tru}={benr_tru}%)  Δ={with_one_real-bwc_tru:+d}")
print(f"Completely empty: {empty}/{N} = {empty/N*100:.1f}%")
print(f"No real contact: {no_real}/{N} = {no_real/N*100:.1f}%  (v5.8: {base['no_real_contact']})  Δ={no_real-base['no_real_contact']:+d}")

print("\n--- CELL FILL ---")
print(f"Nominal cells: {nom_cells}/{poss} = {nom_cells/poss*100:.1f}%  (v5.8: {bcells_nom}={bcfr_nom}%)  Δ={nom_cells-bcells_nom:+d}")
print(f"TRUE cells:    {tru_cells}/{poss} = {tru_cells/poss*100:.1f}%  (v5.8: {bcells_tru}={bcfr_tru}%)  Δ={tru_cells-bcells_tru:+d}")

print("\n--- FULL 7/7 INSTITUTIONS ---")
print(f"Nominal full 7/7: {len(full7_nom)}  (v5.8: {bfull_nom})  Δ={len(full7_nom)-bfull_nom:+d}")
print(f"TRUE full 7/7:    {len(full7_true)}  (v5.8: {bfull_tru})  Δ={len(full7_true)-bfull_tru:+d}")

print("\n--- DATA QUALITY ---")
print(f"CEO-misfiled-in-CISO: {rceo['CISO']}  (v5.8: {bceo})  Δ={rceo['CISO']-bceo:+d}")
print(f"NOT FOUND placeholder cells: {len(nf_pairs)} across {len(set(x[0] for x in nf_pairs))} institutions  (v5.8: 40 cells / 39 inst)")

print("\n--- TIER 1 ---")
t1=[p for p in per if p[0]=='1']
t1_tru_full=[p for p in t1 if p[3]==7]
t1_nom_full=[p for p in t1 if p[4]==7]
print(f"T1 total: {len(t1)} | T1 TRUE full 7/7: {len(t1_tru_full)} (v5.8:{bt1_full_tru}) Δ={len(t1_tru_full)-bt1_full_tru:+d} | T1 NOMINAL full: {len(t1_nom_full)} (v5.8:{bt1_full_nom}) Δ={len(t1_nom_full)-bt1_full_nom:+d}")

# T1 NEW full since v5.8 (compare true-full names)
cur_t1_true_names=set(p[2] for p in t1_tru_full)
new_t1_true = cur_t1_true_names - bt1_names
lost_t1_true = bt1_names - cur_t1_true_names
print(f"T1 TRUE-full NEW since v5.8: {sorted(new_t1_true) if new_t1_true else 'NONE'}")
print(f"T1 TRUE-full LOST since v5.8: {sorted(lost_t1_true) if lost_t1_true else 'NONE'}")

# Which T1 institutions made progress (gained real roles) - need v5.8 per-inst, not stored. Use tier1 nominal-full growth as proxy.
print("\nT1 status sorted by real contacts:")
for p in sorted(t1,key=lambda x:(-x[3],x[2])):
    miss=[r for r,_ in ROLE_COLS if p[5][r][0]!='real']
    flag=''
    if p[5]['CISO'][0]=='notfound': flag=' [CISO=NOTFOUND]'
    elif p[5]['CISO'][0]=='ceo_misfiled': flag=' [CISO=CEO-misfiled]'
    mark='✓FULL' if p[3]==7 else f'{p[3]}/7'
    print(f"  {mark:7} {p[2]:42} miss={miss}{flag}")

# NEW full 7/7 (true) institutions since v5.8 across ALL tiers - need names. We have current set only; v5.8 didn't store all names. 
# But v5.9 commit added Agrobank,BPMB,EXIM,SME Bank,Tabung Haji to 7/7; v5.10 +3 PNB Group; v5.11 AIA CISO; v5.12 +3 roles; v5.13 +10 net roles across 11 inst.
# Identify full-7/7 true institutions by tier for the brief
print("\n--- TRUE FULL 7/7 BY TIER ---")
for t in ['1','2','3','4','5','6']:
    names=[p[2] for p in per if p[0]==t and p[3]==7]
    print(f"  T{t}: {len(names)} -> {names}")

# Save updated state
state={
 "last_check":"2026-07-19T13:30:00Z",
 "git_commit":"7c4941f",
 "git_commit_msg":"v5.13: 3/7 cluster resolution - 11 institutions, +10 net roles",
 "git_commit_at":"2026-07-19T12:56:53Z",
 "csv_source":"ROOT prospect-database-7stakeholders.csv (task URL prospects/ still 404)",
 "baseline_prev":"v5.8 d27e984 (2026-07-18T16:55:20Z) - 6 commits since baseline (v5.9-v5.13 + 1 auto)",
 "total":N,"raw_rows":len(data),
 "raw_row_note":f"+1 PHANTOM row (Sun Life unescaped-quote fragment) persists. Real={N}. UNFIXED since v4.7.",
 "tier":dict(sorted(tier.items())),
 "segment":dict(sorted(seg.items(), key=lambda x:-x[1])),
 "role_pop_nominal":{r:rnom[r] for r,_ in ROLE_COLS},
 "role_pop_true":{r:rtru[r] for r,_ in ROLE_COLS},
 "role_notfound":{r:rnf[r] for r,_ in ROLE_COLS},
 "role_ceo_misfiled_ciso":rceo['CISO'],
 "role_completion_pct_nominal":{r:round(rnom[r]/N*100,1) for r,_ in ROLE_COLS},
 "role_completion_pct_true":{r:round(rtru[r]/N*100,1) for r,_ in ROLE_COLS},
 "role_rank_true":sorted([{r:round(rtru[r]/N*100,1)} for r,_ in ROLE_COLS], key=lambda x:-list(x.values())[0]),
 "with_contacts_nominal":with_one_nom,"with_contacts_true":with_one_real,
 "empty":empty,"no_real_contact":no_real,
 "enrichment_rate_nominal":round(with_one_nom/N*100,1),
 "enrichment_rate_true":round(with_one_real/N*100,1),
 "total_cells_nominal":nom_cells,"total_cells_true":tru_cells,"possible_cells":poss,
 "cell_fill_rate_nominal":round(nom_cells/poss*100,1),"cell_fill_rate_true":round(tru_cells/poss*100,1),
 "full_all_nominal":len(full7_nom),"full_all_true":len(full7_true),
 "t1_total":len(t1),"t1_with_real":len([p for p in t1 if p[3]>=1]),
 "t1_full_nominal":len(t1_nom_full),"t1_full_true":len(t1_tru_full),
 "t1_full_names_true":[p[2] for p in t1_tru_full],
 "t1_ciso_gap":[p[2] for p in t1 if p[5]['CISO'][0] in ('notfound','ceo_misfiled') and p[3]>=5],
 "ceo_misfiled_insts":ceo_insts,
 "notfound_cell_count":len(nf_pairs),"notfound_inst_count":len(set(x[0] for x in nf_pairs)),
 "delta_vs_v58":{
   "enrichment_true_pp":round(with_one_real/N*100,1)-benr_tru,
   "cells_true_delta":tru_cells-bcells_tru,
   "cells_nominal_delta":nom_cells-bcells_nom,
   "full_true_delta":len(full7_true)-bfull_tru,
   "full_nominal_delta":len(full7_nom)-bfull_nom,
   "t1_full_true_delta":len(t1_tru_full)-bt1_full_tru,
   "ceo_misfiled_delta":rceo['CISO']-bceo,
   "role_true_delta":{r:rtru[r]-brt.get(r,0) for r,_ in ROLE_COLS},
 },
 "previous":base.get('previous',{}) if isinstance(base.get('previous'),dict) else {
   "last_check":base['last_check'],"git_commit":base['git_commit'],
   "total":base['total'],"with_contacts_nominal":bwc_nom,"enrichment_rate_nominal":benr_nom,
   "total_cells_nominal":bcells_nom,"cell_fill_rate_nominal":bcfr_nom,
   "full_all_nominal":bfull_nom,"full_all_true":bfull_tru,
   "t1_full_nominal":bt1_full_nom,"t1_full_true":bt1_full_tru,"ceo_misfiled_count":bceo},
 "last_change_commit":"7c4941f","last_change_at":"2026-07-19T12:56:53Z","runs_since_last_change":0
}
json.dump(state,open('state_v513.json','w'),indent=2,ensure_ascii=False)
print("\nSaved state_v513.json")

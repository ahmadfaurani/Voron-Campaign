# VoronDRQ Prospect Database Monitor -- Intelligence Brief
**Generated:** 2026-07-28 01:16 +08 (MYT) | **Brief ID:** VDRQ-MON-20260728-0116
**Classification:** TLP:AMBER | **Source:** canonical prospects/prospect-database-7stakeholders.csv (156 rows; md5 d100a3ff; file mtime 2026-07-26 20:09 MYT)
**Git:** HEAD = 5803b85 (main). **Canonical CSV UNCHANGED -- 4th consecutive static cycle.** Last real DATA commit is still f282a2d (the T1 merge, 20:09 MYT Jul-26); the canonical CSV md5 is still d100a3ff (identical to VDRQ-MON-20260727-1910/-1306/-0701/-0052). Working tree clean. All 3 CSV copies match md5 d100a3ff (primary + mirror + remote re-verified this cycle).
**Previous run:** 2026-07-27 19:10 MYT (VDRQ-MON-20260727-1910) -- approx 6h 6m ago
**Working DB:** now v5.57 (was v5.51 at last brief) -- but v5.57 was gap-CONFIRMATION only (0 new named stakeholders)

## [!] HEADLINE -- STATIC CYCLE #4 POST-MERGE: CANONICAL CSV STILL UNCHANGED (~29h SINCE LAST EDIT); NEW v5.57 ENRICHMENT LANDED BUT WAS GAP-CONFIRMATION ONLY (0 NAMED CONTACTS); v5.51 MERGE SURPLUS NOW 4 CYCLES OVERDUE
1. **No change to the canonical CSV.** md5 is still **d100a3ff** (4th consecutive static cycle). Re-parsed fresh this cycle; every metric matches byte-for-byte: 772/1,092 populated cells (70.7%), 60 full 7/7 rosters, CISO 79 (50.6%), T1 20/28 full. The last real data commit remains f282a2d (the T1 merge, 20:09 MYT Jul-26). Working tree clean. All 3 CSV copies + remote re-verified in sync (d100a3ff).
2. **Time since last content edit = ~29h 7m** (f282a2d landed 2026-07-26 20:09 MYT; now 01:16 MYT Jul-28). 4th consecutive static cycle after the merge. No forward motion on the canonical prospect DB in over a day.
3. **NEW this cycle: a v5.57 enrichment commit landed (5803b85, 00:12 MYT Jul-28) but produced 0 named contacts.** It was a gap-CONFIRMATION pass across 6 Tier-2 insurers + Deutsche Bank -- 16 cells upgraded from speculative to "confirmed NOT FOUND" with official source citations (msig.com.my, sunlifemalaysia.com, manulife.com.my board page, berjayasompo SMT). Commit body states explicitly: *"No new stakeholders were added (existing entries were already accurate); the value of this session is in upgrading gap descriptions from speculative to confirmed-status."* Working DB bumped v5.51 -> v5.57; coverage unchanged at 856/1,337 (64.0%) on the 191-row working baseline.
4. **The pending v5.51 named-contact merge surplus is STILL pending -- now 4 cycles overdue.** First flagged at the 0052 brief (Jul-27), re-flagged at 0701/1306/1910, STILL untouched at 0116 -- now the single longest-overdue action in the pipeline (~29h idle on canonical). The ~25 clean, non-duplicate named contacts across ~19 institutions (6 of which reach full 7/7 on merge) are CONFIRMED preserved in the v5.57 working DB -- verified this cycle that all 6 candidates sit at 7/7 in working DB but only 5-6/7 in canonical.
5. **No new Tier-1 movement.** T1 stays at 20/28 full (71.4%); the 8 partials are unchanged and remain all-foreign. No T1 named-contact surplus exists anywhere.

## 1. Status snapshot -- canonical CSV (re-parsed fresh; UNCHANGED this cycle)
| Metric | Value | Delta vs last brief |
|---|---|---|
| Institutions (rows) | 156 (3 placeholder/non-existent -- standing alert) | 0 |
| Populated stakeholder cells (loose) | **772 / 1,092 (70.7%)** | 0 |
| Real named contacts (strict, refined) | ~759 (69.5%) -- 13 genuine non-name annotation cells | 0 |
| >=1 populated cell (loose) | 156/156 = 100% | 0 |
| >=1 REAL named contact (strict) | 153/156 = 98.1% (3 all-annotation rows: MIIIB, JCL, Maybank-Khazanah) | 0 |
| Full 7/7 (loose tracked) | 60 (38.5%) | 0 |
| Tier split | T1=28 T2=53 T3=20 T4=30 T5=19 T6=6 | 0 |
| md5 / mtime | d100a3ff / Jul-26 20:09 MYT | unchanged |
| Since last content edit | ~29h 7m | +6h 6m |
| Working DB version | v5.57 (was v5.51) | +0.06 (gap-confirmation only) |

## 2. Enrichment progress -- canonical CSV (UNCHANGED; re-confirmed this cycle)
- **Role completion (high to low):** CFO 138 (88.5%) | CIO 123 (78.8%) | Compliance 117 (75.0%) | CRO 110 (70.5%) | GRC 104 (66.7%) | IA 101 (64.7%) | **CISO 79 (50.6% -- still lowest role, the binding constraint)**
- **Distribution (contacts per prospect, loose):** 1/7=23, 2/7=3, 3/7=14, 4/7=11, 5/7=33, 6/7=12, 7/7=60 -- identical to last cycle
- **Per-tier coverage (all tiers 100% have >=1 populated cell):** T1=28 (**20 full** 7/7, 165/196 cells=84.2%) | T2=53 (17 full, 272/371=73.3%) | T3=20 (5 full, 80/140=57.1%) | T4=30 (10 full, 133/210=63.3%) | T5=19 (8 full, 97/133=72.9%) | T6=6 (0 full, 25/42=59.5%)
- **Segments:** Licensed Banks 28 | Insurers 26 | GLC-Linked 19 | Investment Banks 15 | E-Money 14 | Takaful 12 | Development FIs 10 | Card Schemes 10 | MSBs 10 | Payment Operators 6 | Fintech Sandbox 5 | Fintech Registered 1

## 3. Since last check (vs 2026-07-27 19:10 MYT, VDRQ-MON-20260727-1910, ~6h 6m ago)
- **Main CSV delta = 0 cells.** md5 d100a3ff -> d100a3ff (unchanged). No rows touched. File mtime still Jul-26 12:09 UTC (20:09 MYT).
- **Git delta = 1 substantive commit, 0 touching the canonical CSV:**
  - `5803b85` (00:12 MYT Jul-28) -- enrichment v5.57: wrote `enrichment-report-v5.57.md` + `prospect-database-enriched-v5.57.csv` (working DB only). Gap-confirmation pass on 6 Tier-2 insurers + Deutsche Bank; 16 cells upgraded to "confirmed NOT FOUND" with official source citations. **0 new named stakeholders, 0 canonical edits.** (The intervening `125cdef` commit was the 1910 brief itself.)
- **Enrichment delta = 0 named contacts.** Working DB version v5.51 -> v5.57, but v5.57 added only gap descriptions (confirmed-disclosure gaps), not names. The v5.51 named-contact surplus is untouched and confirmed preserved in v5.57.
- **Net for outreach = 0 new named contacts this cycle.** All gains from the 20:09 MYT merge are already captured; nothing additional landed in ~29h.

## 4. Tier-1 priority (28 Licensed Banks -- 20 full 7/7; 8 partials, ALL foreign; UNCHANGED)
**20 full 7/7:** Alliance, Alliance Islamic, AmBank, AmBank Islamic, Bank Islam, Bank of China, Bank Muamalat, CIMB, CIMB Islamic, Hong Leong, Hong Leong Islamic, Maybank, Maybank Islamic, OCBC, Public Bank, Public Islamic, RHB, RHB Islamic, Standard Chartered, UOB.

**8 T1 partials (all foreign banks = CISO/disclosure wall; UNCHANGED):**
| Bank | Coverage | Gap roles | Note |
|---|---|---|---|
| BNP Paribas Malaysia | 5/7 | -CISO,-CIO | foreign-bank wall |
| Citibank Berhad | 5/7 | -CISO,-Compliance | foreign-bank wall |
| HSBC Bank Malaysia | 5/7 | -CISO,-IA | foreign-bank wall |
| Deutsche Bank Malaysia | 3/7 | -GRC,-Compliance,-CIO,-IA | CISO confirmed (Jeng Yean Won, already canonical) |
| Sumitomo Mitsui (SMBC) | 3/7 | -CISO,-GRC,-Compliance,-CIO | foreign-bank wall |
| ICBC Malaysia | 2/7 | -CISO,-GRC,-CRO,-CIO,-IA | improved last merge (1->2) |
| J.P. Morgan Chase Malaysia | 1/7 | 6 missing | foreign-bank wall |
| Mizuho Bank Malaysia | 1/7 | 6 missing | foreign-bank wall |

**No Tier-1 named-contact surplus remains anywhere.** All 8 partials' gaps are confirmed disclosure gaps (v5.57 re-confirmed Deutsche Bank; JPM/Mizuho/BoA/ICBC confirmed as APAC/group-level, max publicly available).

## 5. v5.57 gap-confirmation intelligence (NEW this cycle, 00:12 MYT Jul-28 -- 0 canonical impact but concrete outreach intel)
v5.57 scraped official leadership pages and confirmed several CISO/IT-leader gaps as GENUINE (not enrichment failures). Useful for reframing outreach on these T2 insurers using the named executives that ARE available:
| Institution | Official source | Confirmed finding | Named execs available for outreach |
|---|---|---|---|
| **MSIG Insurance (M) Bhd** (T2) | msig.com.my SMT (12 members) | CISO / Compliance / Audit / GRC are genuine gaps (functions at MS&AD group level, Japan) | CEO Ang Yien Chia; Deputy CEO Toshibumi Suzuki; COO Soh Lai Sim; SVP ERM Kelvin Hii |
| **Sun Life Malaysia Assurance** (T2) | sunlifemalaysia.com mgmt team (16) | CISO / CIO / Compliance not publicly identifiable (titles image-based) | CEO Ho Teck Seng; CFO Ong Le Keat; Takaful CEO Noor Azam |
| **Sun Life Malaysia Takaful** (T2) | 2025 FS | CISO / GRC / Compliance / CIO shared with Assurance entity -- genuine gaps | CEO Noor Azam (shared leadership) |
| **Manulife Holdings Berhad** (T2) | manulife.com.my Board (5 directors) | CISO / Head of GRC not publicly disclosed at mgmt level | Group CEO **Vibha Hamsi Coburn**; Group RMC Chairman **Dato' Khalid Bin Abdol Rahman** (appointed Jan 2026); Group Audit Committee Chair Vijayam Nadarajah |
| **Manulife Takaful Malaysia** (T2) | manulife.com.my | CISO / Head of GRC not publicly disclosed | (shared with Manulife Holdings) |
| **Berjaya Sompo Insurance** (T2) | berjayasompo SMT (8 members) | CIO / Head of IT confirmed genuine gap (no IT leader in SMT) | previously-found roles confirmed accurate |
| **Deutsche Bank Malaysia** (T1) | DB MY FY2024 FS / Pillar 3 / CG | CISO confirmed (Jeng Yean Won, CISM -- already in canonical); Compliance/GRC/CIO/Audit remain APAC-level | CISO Jeng Yean Won; CFO; CRO (3/7) |

> **RMiT outreach angle (NEW):** These confirmed gaps are NOT "we couldn't find them" -- they are officially-attested disclosure gaps (CISO at foreign/group level, IT-leader absent from SMT). For MSIG/Sun Life/Manulife/Berjaya Sompo, lead outreach with the **CEO/CFO/CRO who ARE named** and frame the RMiT conversation around the absence of a disclosed local CISO -- a citable compliance-visibility talking point.

## 6. Actionable intelligence (sales outreach) -- next merge wave NOW 4 CYCLES OVERDUE
1. **#1 PRIORITY (unchanged, now 4 cycles overdue): MERGE THE v5.51 SURPLUS.** ~25 clean, non-duplicate named contacts across ~19 institutions are sitting in the working DB (now v5.57), untouched since the 20:09 MYT merge (~29 hours ago). Verified this cycle that all 6 full-7/7 candidates are at 7/7 in the working DB but only 5-6/7 in canonical. Highest-leverage (each reaches full 7/7 on merge):
   - **ASNB** +CISO (Aishah Farha Mohd Raih) -> 7/7 [T5]
   - **Great Eastern General Insurance** +CISO (Vincent Chin) -> 7/7 [T2]
   - **Hong Leong Investment Bank** +CISO (Dr. Simon Hoh, group) -> 7/7 [T2]
   - **Public Investment Bank** +CISO (Irene Deng, group) -> 7/7 [T2]
   - **Maybank Investment Bank** +CISO (Devinder Singh) +GRC (Cheryl Cheng composite) -> 7/7 [T2]
   - **Tokio Marine Life Insurance** +CISO (Irfan Ismail) +GRC (Andrew Ngou composite) -> 7/7 [T2]
   - Other clean gains: AIA General +CISO, AIA Public Takaful +CISO, Bank Rakyat IB +GRC, BigPay +CISO +Compliance, Boost Bank +GRC, Generali Insurance +GRC, MARA +CFO +CRO +Compliance, Manulife Insurance +IA, Prudential BSN Takaful +CRO/+Compliance, ShopeePay +Compliance, Zurich Life +CFO, iPay88 (M) +CRO, Allianz General +CRO (board-level).
   - **Merging the 6 full-7/7 candidates lifts the full count 60 -> 66 (loose).** This is the single most impactful action available and requires zero new research -- the names are already verified in v5.57.
2. **DEDUP the 3 duplicate-row families BEFORE merging** to avoid reintroducing duplicates: TNG Digital + Touch n Go Visa Prepaid (same CISO Suresh Balachandran + same IA Hairul Imran), Axiata Digital (Boost) + Boost Bank (same CISO Shankar Krishnan + same IA Miraz Ahmed), Maybank (Khazanah-linked) (6 cells all "DUPLICATE: Same as Maybank Berhad").
3. **2nd CLEANUP PASS recommended (standing):** remove the 3 placeholder/non-existent rows (JCL Corporation, Malaysia International Islamic Bank IB, Maybank Khazanah-linked) and empty the 13 residual annotation cells -> 153 real prospects, clean counts. (MIIIB currently inflates the full-7/7 count by 1.)
4. **Tier-1 outreach ready NOW -- 20/28 full rosters.** Top targets unchanged: CIMB, Maybank, RHB, AmBank, Bank Islam, Bank Muamalat, Public Islamic. Lead with the RMiT/compliance angle. **Standing ammo:** DMARC non-compliance at Hong Leong (hlbb.com.my) + RHB (rhbbank.com); CIMB at monitoring-only (p=none) -- concrete RMiT email-security talking points (from VDRQ-MON-20260727-1910).
5. **v5.57 reframes T2-insurer outreach (NEW):** MSIG, Sun Life, Manulife, Berjaya Sompo CISO/IT-leader gaps are now officially-confirmed disclosure gaps. Don't wait -- lead with the named CEO/CFO/CRO (see table in section 5) and frame the RMiT conversation around the absence of a disclosed local CISO. These are citable, source-attributed talking points.
6. **Foreign-bank wall -- reframe outreach, don't wait.** The 8 foreign T1 partials have no real names pending anywhere (v5.57 re-confirmed JPM/Mizuho/BoA/ICBC are APAC/group-level). Lead with the named contacts they DO have (e.g., HSBC: Brian McGuire CRO/Compliance/GRC composite, Elly Neoh CFO, Mei Ling Soo CIO; ICBC: Liau Cheek Compliance + Geng Hao CFO; Deutsche Bank: Jeng Yean Won CISO). No further T1 named gains expected from enrichment.
7. **Enrichment pipeline health (NEW):** search infra is partially degraded -- `firecrawl_scrape` operational, but `web_search`/`firecrawl_search` returning non-MY-specific results. Named-contact discovery is constrained; the v5.57 run relied on direct site scrapes (msig.com.my, sunlifemalaysia.com, manulife.com.my). Expect gap-confirmation to continue outpacing new-name discovery until search infra recovers.

## 7. Data-integrity alerts (all STANDING -- no new findings this cycle)
1. **[Standing] 3 placeholder rows carry zero real named contacts:** JCL Corporation Sdn Bhd (non-existent investment bank, 1 "ENTITY NON-EXISTENT" cell); Malaysia International Islamic Bank IB (non-existent, 7 "ENTITY NON-EXISTENT" cells -- falsely appears 7/7, inflates full count by 1); Maybank (Khazanah-linked) (1 "DUPLICATE OF MAYBANK BERHAD" cell). Recommend removal in 2nd cleanup -> 153 real prospects.
2. **[Standing] 13 genuine non-name annotation cells** ("ENTITY NON-EXISTENT", "DUPLICATE OF", "ENTITY DEFUNCT", "LIKELY NON-EXISTENT", + 1 nameless Public Bank CIO fragment). Real-contact rate (strict, refined) = 759/1,092 (69.5%); the tracked loose rate (772/70.7%) remains the continuity metric.
3. **[Standing] Public Bank CIO cell is an unnamed annotation fragment** ("(Public Bank Group) [Official: publicbankgroup.com]") -- not a named CIO. CISO is filled (Irene Deng) but CIO is effectively still a gap despite the cell being non-empty.
4. **[Standing] Setel semantic duplicate** -- 2 canonical rows (Setel (PETRONAS Dagangan) + Setel by PETRONAS Dagangan Berhad), both T4 E-Money 5/7. Unmerged; inflates count by 1.
5. **[Standing] Foreign-bank CISO wall = 7** (BNP, Citi, HSBC, ICBC, JPM, Mizuho, SMBC) -- confirmed disclosure gap (v5.57 re-confirmed Deutsche Bank CISO present; JPM/Mizuho/BoA/ICBC confirmed APAC/group-level). Mizuho/JPM at 1/7 with no improvement path.

---
*Auto-generated by VoronDRQ monitor cron 2026-07-28 01:16 MYT. Canonical CSV re-parsed fresh (not cached). STATIC CYCLE #4 post-merge: main CSV md5 d100a3ff (unchanged from VDRQ-MON-20260727-1910/-1306/-0701/-0052); 0 canonical edits / 0 new named contacts since last brief (~29h 7m since last content edit f282a2d at 20:09 MYT Jul-26). 1 substantive git commit since last brief: 5803b85 (enrichment v5.57, 00:12 MYT Jul-28) -- gap-confirmation pass on 6 Tier-2 insurers + Deutsche Bank, 16 cells upgraded to confirmed-NOT-FOUND with official source citations, 0 new named stakeholders, 0 canonical edits. Working DB v5.51->v5.57 (coverage unchanged 856/1337=64.0% on 191-row working baseline). All 3 CSV copies + remote in sync (d100a3ff). All canonical metrics re-confirmed identical (772/1092=70.7%, full 60, CISO 79/50.6%, T1 20/28 full). v5.51 surplus (~25 clean contacts, 6 inst->7/7) verified preserved in v5.57 working DB -- remains #1 overdue action, now 4 cycles overdue (flagged 0052, re-flagged 0701/1306/1910/0116). NEW this cycle: v5.57 officially confirms CISO/IT-leader gaps at MSIG, Sun Life, Manulife, Berjaya Sompo as genuine disclosure gaps (citetable outreach intel); search infra partially degraded (firecrawl_scrape OK, web_search/firecrawl_search non-MY). Next: merge the v5.51 surplus (60->66 full), dedup the 3 duplicate-row families, run a 2nd cleanup pass (remove 3 non-existent rows + 13 annotation cells).*

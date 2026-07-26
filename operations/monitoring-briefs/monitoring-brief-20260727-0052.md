# VoronDRQ Prospect Database Monitor -- Intelligence Brief
**Generated:** 2026-07-27 00:52 +08 (MYT) | **Brief ID:** VDRQ-MON-20260727-0052
**Classification:** TLP:AMBER | **Source:** canonical prospects/prospect-database-7stakeholders.csv (156 rows; md5 d100a3ff; file mtime 2026-07-26 20:09 MYT)
**Git:** HEAD = f282a2d (main). 1 new commit since last brief -- the long-awaited T1 merge + working-DB dedup at 20:09 MYT today. All 3 CSV copies match md5 d100a3ff (primary + mirror + remote verified this cycle).
**Previous run:** 2026-07-26 18:46 MYT (VDRQ-MON-20260726-1846) -- approx 6h 6m ago

## [!] HEADLINE -- THE 9-CYCLE OVERDUE TIER-1 MERGE FINALLY LANDED; CANONICAL CSV EDITED FOR THE FIRST TIME IN ~3d 8h; T1 FULL-ROSTER COVERAGE 17 -> 20; CISO CROSSES 50%
1. **The 3-cell Tier-1 CISO merge + ICBC CFO merge -- flagged overdue across 9 prior cycles -- was committed this evening (f282a2d, 2026-07-26 20:09 MYT).** This is the single highest-leverage manual step that had sat untouched ~3d 8h; it is now DONE. Canonical md5 e7a51212 -> d100a3ff (first content edit since the Jul-23 12:18 MYT cleanup), breaking the 11-cycle static streak. All 3 CSV copies + remote re-verified in sync (d100a3ff). Exact 4-cell diff confirmed via git diff.
   - Public Bank Berhad: +CISO **Irene Deng** (RocketReach, conf 65) -> 7/7
   - Public Islamic Bank Berhad: +CISO **Irene Deng** (Group CISO, conf 60) -> 7/7
   - Bank Muamalat Malaysia: +CISO **Ts. Dr. Ismamuradi Abdul Kadir** (CCISO, conf 90) -> 7/7
   - ICBC (Malaysia): +CFO **Geng Hao** (MD/CEO, AR 2024, conf 95) -> 2/7 (was 1/7)
2. **Canonical metrics jump on the merge:** populated stakeholder cells 768 -> **772 (70.7%, +4)**; full 7/7 rosters 57 -> **60 (+3)**; CISO role completion 76 (48.7%) -> **79 (50.6%, +3 -- crosses 50%)**; CFO 137 (87.8%) -> 138 (88.5%, +1). Tier-1 full-roster coverage 17 -> **20 of 28**; Tier-1 partials 11 -> 8 (all 8 remaining are foreign banks).
3. **Working DB advanced to v5.51** (md5 728f808b, mtime 2026-07-26 20:09 MYT): deduped 207 -> 191 rows (15 merge groups) AND merged the 4 T1 fills into canonical in the same commit. Working now holds a genuine non-duplicate named-contact surplus of ~25 contacts across ~19 institutions ready for the next merge wave (after dedup of 3 duplicate-row families).
4. **No Tier-1 named-contact surplus remains in the working file.** All 8 remaining Tier-1 partials are foreign banks (BNP, Citi, Deutsche, HSBC, ICBC, JPM, Mizuho, SMBC); the working file holds only "NOT FOUND" / "ROLE EXISTS, NAME NOT DISCLOSED" / "Not publicly disclosed" annotation cells for their gaps. This confirms the **foreign-bank CISO wall is a disclosure gap, not a research gap** -- no further named T1 gains are pending anywhere.
5. **Data-integrity findings (new this cycle):** a strict re-parse found **3 placeholder rows with zero real named contacts** -- JCL Corporation [non-existent entity], Malaysia International Islamic Bank IB [non-existent entity whose 7 "ENTITY NON-EXISTENT" cells make it falsely appear 7/7 in the tracked count], and Maybank (Khazanah-linked) [duplicate marker]. ~25 residual annotation cells survived the Jul-23 cleanup. A 2nd cleanup pass is recommended (see sec 6). These do not change the headline delta but mean the real prospect count is 153, not 156.

## 1. Status snapshot -- both databases (canonical EDITED this cycle; re-parsed fresh)
| Metric | Canonical CSV (main) | Working DB (v5.51) |
|---|---|---|
| Institutions (rows) | 156 (3 placeholder/non-existent -- see sec 6) | 191 (deduped from 207; 15 merge groups) |
| Populated stakeholder cells | **772 / 1,092 (70.7%)** [+4] | 1,337 cells, of which ~759 real named + ~560 annotation |
| Real named contacts (strict, lower bound) | ~747 (68.4%) | ~759 |
| >=1 populated cell | 156/156 = 100% (loose) | 191/191 |
| >=1 REAL named contact (strict) | 153/156 = 98.1% | -- |
| Full 7/7 (loose tracked) | 60 (38.5%) [+3] | 191 (loose; many annotation-filled) |
| Tier split | T1=28 T2=53 T3=20 T4=30 T5=19 T6=6 | T1=30 T2=54 T3=44 T4=27 T5=24 T6=12 |
| md5 / mtime | d100a3ff / Jul-26 20:09 MYT | 728f808b / Jul-26 20:09 MYT |
| Since last content edit | ~4h 43m ago (this was the merge) | fresh this cycle |

## 2. Enrichment progress -- canonical CSV (post-merge; loose tracked metric)
- **Role completion (high to low):** CFO 138 (88.5%) | CIO 123 (78.8%) | Compliance 117 (75.0%) | CRO 110 (70.5%) | GRC 104 (66.7%) | IA 101 (64.7%) | **CISO 79 (50.6% -- +3 this cycle, crosses 50%, still lowest role)**
- **Distribution (contacts per prospect, loose):** 1/7=23, 2/7=3, 3/7=14, 4/7=11, 5/7=33, 6/7=12, 7/7=60
- **Per-tier coverage (all tiers 100% have >=1 populated cell):** T1=28 (**20 full** 7/7) | T2=53 (17 full) | T3=20 (5 full) | T4=30 (10 full) | T5=19 (8 full) | T6=6 (0 full)
- **Segments:** Licensed Banks 28 | Insurers 26 | GLC-Linked 19 | Investment Banks 15 | E-Money 14 | Takaful 12 | Development FIs 10 | Card Schemes 10 | MSBs 10 | Payment Operators 6 | Fintech Sandbox 5 | Fintech Registered 1
- **Stripped Titles (col K metadata, not a role):** ~22 institutions carry a title (Dr, Datin, Datuk, Dato', Encik, Puan, Hj, etc.).

## 3. Since last check (vs 2026-07-26 18:46 MYT, VDRQ-MON-20260726-1846, ~6h 6m ago)
- **Main CSV delta = +4 cells (the merge).** md5 e7a51212 -> d100a3ff. Git diff shows EXACTLY 4 changed cells: Public Bank CISO, Public Islamic CISO, Bank Muamalat CISO, ICBC CFO. No other rows touched. First canonical content edit since Jul-23 12:18 MYT (was static ~3d 7h 51m).
- **Git delta = 1 commit (f282a2d, 20:09 MYT):** "v5.51: dedup working DB 207->191 (15 merge groups) + merge 4 overdue T1 fills into canonical ... +v5.51 report". Both the dedup and the canonical merge landed together.
- **Working-DB delta: v5.42 -> v5.51.** Deduped 207 -> 191 rows (removed ~16 cooperative/fintech duplicate rows via 15 merge groups) and merged the 4 T1 fills forward. Real named contacts ~759 (strict).
- **Net for outreach: +4 real named Tier-1 contacts this cycle (3 CISOs + 1 CFO).** T1 full rosters +3; ICBC improved 1/7 -> 2/7. This is the first cycle in ~3 days to advance named coverage -- the recommended action was taken.

## 4. Tier-1 priority (28 Licensed Banks -- 20 full 7/7 now; 8 partials, ALL foreign)
**20 full 7/7 (loose) -- the 3 new ones starred (*):**
Alliance, Alliance Islamic, AmBank, AmBank Islamic, Bank Islam, Bank of China, CIMB, CIMB Islamic, Hong Leong, Hong Leong Islamic, Maybank, Maybank Islamic, OCBC, **Public Bank\***, **Public Islamic\***, RHB, RHB Islamic, Standard Chartered, UOB, **Bank Muamalat\***.

**8 T1 partials (all foreign banks = the CISO/disclosure wall):**
| Bank | Main | Gap roles | Note |
|---|---|---|---|
| BNP Paribas Malaysia | 5/7 | -CISO,-CIO | foreign-bank wall |
| Citibank Berhad | 5/7 | -CISO,-Compliance | foreign-bank wall |
| HSBC Bank Malaysia | 5/7 | -CISO,-IA | foreign-bank wall |
| Deutsche Bank Malaysia | 3/7 | -GRC,-Compliance,-CIO,-IA | foreign-bank wall |
| Sumitomo Mitsui (SMBC) | 3/7 | -CISO,-GRC,-Compliance,-CIO | foreign-bank wall |
| ICBC Malaysia | 2/7 | -CISO,-GRC,-CRO,-CIO,-IA | **improved 1/7 -> 2/7 (+CFO merged)** |
| J.P. Morgan Chase Malaysia | 1/7 | 6 missing | foreign-bank wall |
| Mizuho Bank Malaysia | 1/7 | 6 missing | foreign-bank wall |

**No Tier-1 named-contact surplus remains in working v5.51** -- all 8 partials' gaps are annotation cells ("NOT FOUND"/"ROLE EXISTS, NAME NOT DISCLOSED"/"Not publicly disclosed"), not real names. The foreign-bank wall is a confirmed disclosure gap; do not expect more T1 named gains from enrichment.

## 5. Actionable intelligence (sales outreach) -- next merge wave + outreach
1. **The #1 recommended action is DONE.** The 3-cell T1 CISO merge + ICBC CFO landed after 9 cycles. T1 full-roster coverage 17 -> 20 (71%); CISO 48.7% -> 50.6%. No further action needed on those 4 cells.
2. **NEXT MERGE WAVE -- ~25 clean, non-duplicate named contacts across ~19 institutions in v5.51.** Highest-leverage (each reaches full 7/7):
   - **ASNB** +CISO (Aishah Farha Mohd Raih) -> 7/7 [T5]
   - **Great Eastern General Insurance** +CISO (Vincent Chin) -> 7/7 [T2]
   - **Hong Leong Investment Bank** +CISO (Dr. Simon Hoh, group) -> 7/7 [T2]
   - **Public Investment Bank** +CISO (Irene Deng, group) -> 7/7 [T2]
   - **Maybank Investment Bank** +CISO (Devinder Singh) +GRC (Cheryl Cheng composite) -> 7/7 [T2]
   - **Tokio Marine Life Insurance** +CISO (Irfan Ismail) +GRC (Andrew Ngou composite) -> 7/7 [T2]
   - Other clean gains: AIA General +CISO, AIA Public Takaful +CISO, Bank Rakyat IB +GRC, BigPay +CISO +Compliance, Boost Bank +GRC, Generali Insurance +GRC, MARA +CFO +CRO +Compliance, Manulife Insurance +IA, Prudential BSN Takaful +CRO/+Compliance (same person, combined role), ShopeePay +Compliance, Zurich Life +CFO, iPay88 (M) +CRO, Allianz General +CRO (board-level).
   - Merging these 6 full-7/7 candidates lifts the full count 60 -> 66 (loose); real-full ~59 -> ~65.
3. **DEDUP BEFORE MERGING the duplicate-row families.** TNG Digital + Touch n Go Visa Prepaid (same CISO Suresh Balachandran + same IA Hairul Imran in 2 rows), Axiata Digital (Boost) + Boost Bank (same CISO Shankar Krishnan + same IA Miraz Ahmed in 2 rows), and Maybank (Khazanah-linked) (6 cells all marked DUPLICATE: Same as Maybank Berhad). Consolidate these row families first to avoid reintroducing duplicates.
4. **2nd CLEANUP PASS recommended:** remove the 3 placeholder/non-existent rows (JCL Corporation, Malaysia International Islamic Bank IB, Maybank Khazanah-linked) and empty the ~25 residual "ENTITY NON-EXISTENT"/"DUPLICATE" annotation cells -> 153 real prospects, clean counts. (MIIIB currently inflates the full-7/7 count by 1.)
5. **Tier-1 outreach ready NOW -- 20/28 full rosters.** Top targets: CIMB, Maybank, RHB, AmBank, Bank Islam, **Bank Muamalat (newly full)**, **Public Islamic (newly full)**. Public Bank now has CISO Irene Deng -- add to outreach (note: its CIO cell is an unnamed annotation fragment, not a named contact -- CIO effectively still a gap; see sec 6).
6. **Foreign-bank wall -- reframe outreach, don't wait.** The 8 foreign T1 partials have no real names pending anywhere. Use the named contacts they DO have: HSBC (Brian McGuire -- CRO/Compliance/GRC composite; Elly Neoh -- CFO; Mei Ling Soo -- CIO; 5 verified names), Citibank, BNP, SMBC, Deutsche -- lead with the RMiT/compliance angle for these. ICBC now has 2 named (Compliance Liau Cheek + CFO Geng Hao).

## 6. Data-integrity alerts (3 NEW this cycle + standing)
1. **[NEW] 3 placeholder rows carry zero real named contacts (annotation-only):**
   - **JCL Corporation Sdn Bhd** (T2 Investment Banks) -- 1 "ENTITY NON-EXISTENT" cell. Non-existent as a licensed investment bank.
   - **Malaysia International Islamic Bank IB** (T2 Investment Banks) -- 7 "ENTITY NON-EXISTENT" cells. **Falsely appears 7/7 in the loose tracked count** (inflates full-7/7 by 1). Non-existent entity.
   - **Maybank (Khazanah-linked)** (T5 GLC-Linked) -- 1 "DUPLICATE OF MAYBANK BERHAD" cell. Duplicate marker.
   - **Recommendation:** remove these 3 rows in a 2nd cleanup -> 153 real prospects; full-7/7 60 -> 59.
2. **[NEW] ~25 residual annotation cells survived the Jul-23 cleanup** ("ENTITY NON-EXISTENT", "DUPLICATE OF") because they were not "NOT FOUND" markers. Real-contact rate (strict, a lower bound -- it also undercounts some Malay-name cells with single-letter initials like "Hamidi A Razak") = ~747/1,092 (68.4%). A 2nd cleanup should empty these; the tracked loose rate (772/70.7%) remains the continuity metric.
3. **[NEW] Public Bank CIO cell is an unnamed annotation fragment** ("(Public Bank Group) [Official: publicbankgroup.com]") -- not a named CIO. CISO is now filled (Irene Deng) but CIO is effectively still a gap despite the cell being non-empty.
4. **[Standing] Setel semantic duplicate** -- 2 canonical rows (Setel (PETRONAS Dagangan) + Setel by PETRONAS Dagangan Berhad), both T4 E-Money 5/7. Unmerged; inflates count by 1.
5. **[Standing] CISO bottleneck eased** -- 48.7% -> 50.6% (crosses 50%), still the lowest role but the gap narrowed.
6. **[Standing] Foreign-bank CISO wall = 7** (BNP, Citi, HSBC, ICBC, JPM, Mizuho, SMBC) -- confirmed disclosure gap (no real names in working file either). Mizuho/JPM at 1/7 with no improvement.
7. **[CORRECTION to prior briefs]** earlier "high-value non-duplicate merge" estimates were inflated by counting "Not publicly disclosed" annotation cells as contacts. Verified this cycle: Zurich Life is +CFO only (1->2, not 1->7); JCL is 0 (non-existent); HSBC Amanah Takaful is 0 surplus (CFO+Compliance already in canonical, rest annotations); Zurich Takaful is 0 surplus (all "Not publicly disclosed" annotations). The genuine clean surplus is ~25 contacts across ~19 institutions (sec 5).

---
*Auto-generated by VoronDRQ monitor cron 2026-07-27 00:52 MYT. Canonical CSV re-parsed fresh (not cached). BREAKING the 11-cycle static streak: main CSV md5 e7a51212 -> d100a3ff (commit f282a2d, 20:09 MYT) -- the 9-cycle-overdue 4-cell Tier-1 merge (Public Bank CISO, Public Islamic CISO, Bank Muamalat CISO, ICBC CFO) finally landed, lifting T1 full-roster coverage 17 -> 20 and CISO completion 48.7% -> 50.6%. Working DB advanced v5.42 -> v5.51 (deduped 207 -> 191). All 3 CSV copies + remote in sync (d100a3ff). Next: merge the ~25 clean non-duplicate v5.51 surplus (6 institutions reach full 7/7), dedup the 3 duplicate-row families, and run a 2nd cleanup pass to remove 3 non-existent/placeholder rows + 25 residual annotation cells.*

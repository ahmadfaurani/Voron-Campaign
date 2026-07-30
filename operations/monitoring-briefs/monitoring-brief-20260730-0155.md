# VoronDRQ Prospect Database Monitor -- Intelligence Brief
**Generated:** 2026-07-30 01:55 +08 (MYT) | **Brief ID:** VDRQ-MON-20260730-0155
**Classification:** TLP:AMBER | **Source:** canonical prospects/prospect-database-7stakeholders.csv (156 rows; md5 d100a3ff; file mtime 2026-07-26 20:09 MYT)
**Git:** HEAD = 2b6b786 (main). **Canonical CSV UNCHANGED -- 11th consecutive static cycle, NEW longest-idle mark (~77h 46m since last edit).** All 3 CSV copies + remote re-verified in sync (d100a3ff).
**[NEW THIS CYCLE -- ENRICHMENT RESUMED] Working DB jumped v5.65 -> v5.68 (3 new versions, commit 2b6b786 @ 00:08 MYT Jul-30, ~1h 47m ago). 3 NEW NAMED CISO contacts discovered -- including a TIER-1 bank CISO (Mizuho), the first new T1 named contact since the Jul-26 merge. Prior brief expectation of no further T1 named gains is now DISPROVEN. Canonical untouched; merge backlog grows.**
**Previous run:** 2026-07-29 19:52 MYT (VDRQ-MON-20260729-1952) -- approx 6h 3m ago
**Working DB:** advanced v5.65 -> v5.68 (was stalled at v5.65 last cycle).


## [!] HEADLINE -- CANONICAL STILL FROZEN (11th STATIC CYCLE, ~77h 46m IDLE -- NEW RECORD); BUT WORKING-DB ENRICHMENT RESUMED v5.65->v5.68 WITH 3 NEW NAMED CISOs (incl. T1 Mizuho -- first T1 gain since Jul-26); MERGE NOW ~11 CYCLES OVERDUE
1. **Canonical CSV unchanged -- 11th consecutive static cycle, new longest-idle mark (~77h 46m).** md5 still d100a3ff, re-parsed fresh this cycle; every canonical metric matches byte-for-byte: 772/1,092 populated (70.7%), 60 full 7/7 (loose) / 59 strict, CISO 79 (50.6%), T1 20/28 full. Last real data commit to canonical remains f282a2d (20:09 MYT Jul-26). All 3 local CSV copies + remote in sync (d100a3ff). Working tree clean.
2. **[NEW -- MAJOR] Working-DB enrichment RESUMED: v5.65 -> v5.68 (3 new versions) via commit 2b6b786 @ 00:08 MYT Jul-30 (~1h 47m before this brief).** First working-DB advance since v5.65 (last cycle reported it stalled). Commit msg: v5.68: Chubb Malaysia CISO filled (Balaguru Devan); FWD/Manulife NOT FOUND confirmations. Diffing v5.65->v5.68 cell-by-cell surfaced **3 NEW NAMED CISO contacts** (all currently EMPTY in canonical -- mergeable):
   - **Mizuho Bank (Malaysia) Berhad -- CISO = Noorhisham Rusmani** (T1 Licensed Bank). Canonical 1/7 -> working 2/7. **First new T1 named contact since the Jul-26 T1 merge (f282a2d).** Prior brief explicitly listed Mizuho as 1/7, foreign-bank wall and asserted no further T1 named gains expected -- **now disproven.** Source attribution in working DB is bare (name only, no cited URL); verify source before canonical merge, but it is a named, actionable contact.
   - **Chubb Insurance Malaysia Berhad -- CISO = Balaguru Devan Santana Dewan** (T2 Insurer, LinkedIn-cited). Canonical 5/7 -> working 6/7 (Compliance still a confirmed NOT-FOUND gap).
   - **Generali Life Insurance Malaysia Berhad -- CISO = Aaron Ooi Yen Keat** (T2 Insurer, LinkedIn/Indonesian-CIO-Network-cited). Canonical 5/7 -> working 6/7 (CIO not publicly disclosed -- confirmed gap).
3. **[NEW -- MINOR] v5.66->v5.67 also standardized ~13 NOT-FOUND annotations** to cleaner Not publicly disclosed on official leadership page wording across Generali Insurance/Life, Khazanah, Manulife Takaful, Syarikat Takaful, Takaful Am General, Takaful Ikhlas, Berjaya Sompo, GX Bank. No new named contacts in this subset -- purely gap-documentation cleanup (still citable as disclosure-gap evidence).
4. **Mergeable surplus freshly recomputed against v5.68 (strict named-only filter):** **41 named cells across 27 institutions; 13 institutions reach FULL 7/7 on merge.** The 3 new CISOs (Mizuho/Chubb/Generali Life) are NET additions vs the v5.65 baseline -- but none completes a roster (Mizuho stays 2/7, Chubb 6/7, Generali Life 6/7), so the **13 full-7/7 candidates are UNCHANGED** from prior briefs. After dedup of the 3 duplicate-row families (TNG/Touch-n-Go, Axiata/Boost, Maybank-Khazanah placeholder) -> ~37 unique named cells / ~25 institutions / ~11 unique full-7/7 gains.
5. **No new Tier-1 full-7/7 roster movement.** T1 stays at 20/28 full (71.4%); the 8 partials unchanged in canonical. Mizuho new CISO (working-only) would lift it 1/7->2/7 on merge but does NOT close the roster -- Mizuho remains the weakest T1 (5 roles still confirmed gaps: GRC/CFO/CRO/Compliance/CIO).
6. **No new email-recon this cycle.** The 2026-07-29 email-recon run (8 T1 banks, 56 patterns, 5 verified role-mailboxes, 4/8 DMARC-compliant) is the same one the prior brief already reported (commit 1a55887). No re-scan since.

## 1. Status snapshot -- canonical CSV (re-parsed fresh; UNCHANGED this cycle)
| Metric | Value | Delta vs last brief |
|---|---|---|
| Institutions (rows) | 156 (3 placeholder/non-existent -- standing alert) | 0 |
| Populated stakeholder cells (loose) | **772 / 1,092 (70.7%)** | 0 |
| Real named contacts (strict) | ~760 (69.6%) -- ~12 non-name annotation cells | 0 |
| >=1 populated cell (loose) | 156/156 = 100% | 0 |
| >=1 REAL named contact (strict) | ~151/156 (96.8%) -- 5 all-annotation rows incl. 3 placeholders | 0 |
| Full 7/7 (loose / strict) | 60 (38.5%) / 59 | 0 |
| Tier split | T1=28 T2=53 T3=20 T4=30 T5=19 T6=6 | 0 |
| md5 / mtime | d100a3ff / Jul-26 20:09 MYT | unchanged |
| Since last content edit | **~77h 46m** | +6h 3m (NEW longest) |
| Working DB version | **v5.68 (ADVANCED from v5.65)** | **+3 versions** |
| Git commits since last brief | **1** (2b6b786 v5.68 enrichment) -- NEW | +1 |

## 2. Enrichment progress
**Canonical CSV (UNCHANGED; re-confirmed this cycle):**
- **Role completion (high -> low):** CFO 138 (88.5%) | CIO 123 (78.8%) | Compliance 117 (75.0%) | CRO 110 (70.5%) | GRC 104 (66.7%) | IA 101 (64.7%) | **CISO 79 (50.6% -- still lowest role, the binding constraint)**
- **Distribution (contacts per prospect, loose):** 1/7=23, 2/7=3, 3/7=14, 4/7=11, 5/7=33, 6/7=12, 7/7=60 -- identical to last cycle
- **Per-tier coverage (all tiers 100% have >=1 cell):** T1=28 (**20 full** 7/7, 165/196=84.2%) | T2=53 (17 full, 272/371=73.3%) | T3=20 (5 full, 80/140=57.1%) | T4=30 (10 full, 133/210=63.3%) | T5=19 (8 full, 97/133=72.9%) | T6=6 (0 full, 25/42=59.5%)
- **Segments:** Licensed Banks 28 | Insurers 26 | GLC-Linked 19 | Investment Banks 15 | E-Money 14 | Takaful 12 | Development FIs 10 | Card Schemes 10 | MSBs 10 | Payment Operators 6 | Fintech Sandbox 5 | Fintech Registered 1

**Working DB (ADVANCED v5.65 -> v5.68; 191-row baseline, 1,337 slots):** coverage held at ~100% (860+ named, the 3 new CISOs added; gap-confirmations standardized). **Delta vs last brief: +3 named CISO contacts** (Mizuho, Chubb, Generali Life) + ~13 annotation cleanups. The enrichment research phase is NOT dead -- this cycle proved new named T1/T2 contacts can still be found, contradicting prior research-complete framing.

**[NEW] v5.65 -> v5.68 working-DB named gains (all mergeable to canonical):**
| Institution | Tier | Role | New named contact | Canonical -> Working |
|---|---|---|---|---|
| **Mizuho Bank (Malaysia) Berhad** | **T1** | CISO | **Noorhisham Rusmani** | 1/7 -> 2/7 |
| Chubb Insurance Malaysia Berhad | T2 | CISO | Balaguru Devan Santana Dewan | 5/7 -> 6/7 |
| Generali Life Insurance Malaysia Berhad | T2 | CISO | Aaron Ooi Yen Keat | 5/7 -> 6/7 |


## 3. Since last check (vs 2026-07-29 19:52 MYT, VDRQ-MON-20260729-1952, ~6h 3m ago)
- **Canonical CSV delta = 0 cells.** md5 d100a3ff -> d100a3ff (unchanged). File mtime still Jul-26 20:09 MYT. 11th static cycle.
- **Git delta = +1 commit.** HEAD moved dd26b89 (the prior brief) -> **2b6b786 v5.68: Chubb Malaysia CISO filled (Balaguru Devan); FWD/Manulife NOT FOUND confirmations** (00:08 MYT Jul-30). This commit advanced the working DB 3 versions (v5.66, v5.67, v5.68 files all landed) but touched ZERO canonical cells.
- **Working-DB delta = +3 named CISOs + ~13 annotation cleanups.** v5.65 -> v5.68. The 3 new named contacts (Mizuho/Chubb/Generali Life CISOs) are all currently EMPTY in canonical and are mergeable. **This is the first working-DB named gain since v5.65** -- prior brief reported no new named contacts added anywhere.
- **Email-recon delta = 0.** No new re-scan since the 2026-07-29 run already reported last cycle.
- **Net for outreach = 0 new named in canonical this cycle, BUT +3 named in working DB pending merge** -- including a T1 bank CISO (Mizuho), a genuinely new outreach entry point once merged/verified.

## 4. Tier-1 priority (28 Licensed Banks -- 20 full 7/7; 8 partials, ALL foreign; UNCHANGED in canonical)
**20 full 7/7:** Alliance, Alliance Islamic, AmBank, AmBank Islamic, Bank Islam, Bank of China, Bank Muamalat, CIMB, CIMB Islamic, Hong Leong, Hong Leong Islamic, Maybank, Maybank Islamic, OCBC, Public Bank, Public Islamic, RHB, RHB Islamic, Standard Chartered, UOB.

**8 T1 partials (canonical; UNCHANGED -- but Mizuho now has a working-DB CISO pending merge):**
| Bank | Canonical | Working v5.68 | Gap roles (canonical) | Note |
|---|---|---|---|---|
| BNP Paribas Malaysia | 5/7 | 5/7 | -CISO,-CIO | foreign-bank wall |
| Citibank Berhad | 5/7 | 5/7 | -CISO,-Compliance | foreign-bank wall |
| HSBC Bank Malaysia | 5/7 | 5/7 | -CISO,-IA | foreign-bank wall |
| Deutsche Bank Malaysia | 3/7 | 3/7 | -GRC,-Compliance,-CIO,-IA | CISO confirmed (Jeng Yean Won) |
| Sumitomo Mitsui (SMBC) | 3/7 | 3/7 | -CISO,-GRC,-Compliance,-CIO | foreign-bank wall |
| ICBC Malaysia | 2/7 | 2/7 | -CISO,-GRC,-CRO,-CIO,-IA | foreign-bank wall |
| J.P. Morgan Chase Malaysia | 1/7 | 1/7 | 6 missing | foreign-bank wall |
| **Mizuho Bank Malaysia** | **1/7** | **2/7 [NEW]** | 5 missing | **WORKING-DB CISO Noorhisham Rusmani found -- merge to lift to 2/7** |

[NEW] = new this cycle (working DB only, not yet canonical).

## 5. Actionable intelligence (sales outreach) -- MERGE STILL THE SOLE BOTTLENECK (~11 CYCLES OVERDUE); ENRICHMENT PROVED NOT DEAD (+3 NAMED CISOs incl. T1)
1. **#1 PRIORITY (unchanged, now ~11 cycles / ~77h 46m overdue): MERGE THE WORKING-DB NAMED SURPLUS INTO CANONICAL.** Freshly recomputed against v5.68: **41 named cells across 27 institutions** (raw, strict named-only filter) -> after removing the Maybank (Khazanah) placeholder + de-dup of the TNG/Touch-n-Go and Axiata/Boost families -> **~37 unique named contacts across ~25 institutions.** **13 institutions reach FULL 7/7 on merge** (canonical strict full 59 -> ~72; loose 60 -> ~73). The 13 full-7/7 candidates (with the named contact(s) to merge):
   | Institution | Currently | Add | Tier |
   |---|---|---|---|
   | Amanah Saham Nasional Berhad (ASNB) | 6/7 | +CISO Aishah Farha Mohd Raih | T5 |
   | Great Eastern General Insurance | 6/7 | +CISO Vincent Chin | T2 |
   | Hong Leong Investment Bank | 6/7 | +CISO Dr. Simon Hoh (group) | T2 |
   | Public Investment Bank | 6/7 | +CISO Irene Deng (group) | T2 |
   | Maybank Investment Bank | 5/7 | +CISO Devinder Singh +GRC Cheryl Cheng | T2 |
   | Tokio Marine Life Insurance | 5/7 | +CISO Irfan Ismail +GRC Andrew Ngou | T2 |
   | CIMB (Khazanah-linked) | 6/7 | +CISO Charles J. Samuel (group) | T5 |
   | MIDF Amanah Investment Bank | 6/7 | +CISO Ts. Kathiresan Narayanasamy | T2 |
   | Bank Rakyat Investment Bank | 5/7 | +CISO Syed Azlan +GRC Fuhaizad Asmar Omar | T2 |
   | Boost Bank | 4/7 | +CISO Shankar Krishnan +GRC Abid Abdul Adam +IA Miraz Ahmed | T5 |
   | Axiata Digital (Boost) | 5/7 | +CISO Shankar Krishnan +IA Miraz Ahmed | T5 |
   | TNG Digital | 5/7 | +CISO Suresh Balachandran +IA Hairul Imran | T4 |
   | Touch n Go Visa Prepaid | 5/7 | +CISO Suresh Balachandran +IA Hairul Imran | T4 |
   *(TNG/Touch-n-Go and Axiata/Boost are duplicate families -- de-dup to 1 each before merge -> ~11 unique full-7/7 gains.)*
2. **[NEW] +3 named CISOs from v5.68 (NOT reaching full 7/7, but fresh outreach ammo):**
   - **Mizuho Bank Malaysia -- CISO Noorhisham Rusmani (T1).** First new T1 named contact in 4 days. Mizuho is the weakest T1 roster -- this CISO is a direct cyber/security-conversation entry point where before only the Board Audit Committee chair (Lim Kim Seng) existed. WARNING: Source attribution is bare (name only, no cited URL in working DB) -- verify the source before merging to canonical, but it is actionable for outreach framing now.
   - **Chubb Insurance Malaysia -- CISO Balaguru Devan Santana Dewan (T2).** LinkedIn-cited. Chubb now has 6/7 named (only Compliance remains a confirmed gap). Strong roster for a full CISO-led RMiT pitch.
   - **Generali Life Insurance Malaysia -- CISO Aaron Ooi Yen Keat (T2).** LinkedIn/Indonesian-CIO-Network-cited. Generali Life now 6/7 (CIO not publicly disclosed). Combine with Generali Insurance Malaysia existing GRC (Haneeza Abdul Kadir) for a group-level Generali outreach.
3. **Other clean named gains (not reaching full 7/7; unchanged from prior briefs):** AIA General +CISO (Chee Lung Yuen); AIA Public Takaful +CISO (Chee Lung Yuen); Allianz General +CRO (Lim Tuang Ooi, board-level); BigPay +CISO (Angus Thorn) +Compliance (Divya Das) +CIO (Siddharth R.); MARA +CFO (Dr. Azmi) +CRO (Siti Aminah) +Compliance (Shuhaimi); Prudential BSN Takaful +CISO (Eng Fun Darren See) +CRO/+Compliance (Anita Menon); Manulife Insurance +IA (Krishna Rajaa Ramalingam); ShopeePay +Compliance (Fadhli Azman); Zurich Life +CFO (Timothy William Howell); iPay88 +CRO (Khushwant Singh).
4. **DEDUP the 3 duplicate-row families BEFORE merging:** TNG Digital + Touch n Go Visa Prepaid (same CISO Suresh Balachandran + same IA Hairul Imran); Axiata Digital (Boost) + Boost Bank (same CISO Shankar Krishnan + same IA Miraz Ahmed); Maybank (Khazanah-linked) (6 cells all DUPLICATE: Same as Maybank Berhad -- remove the row entirely).
5. **2nd CLEANUP PASS (standing):** remove the 3 placeholder/non-existent rows (JCL Corporation, Malaysia International Islamic Bank IB, Maybank Khazanah-linked) and empty the residual annotation cells -> 153 real prospects, clean counts. (MIIIB currently inflates the loose full-7/7 count by 1.)
6. **Tier-1 outreach ready NOW -- 20/28 full rosters.** Top targets: CIMB, Maybank, RHB, AmBank, Bank Islam, Bank Muamalat, Public Islamic. Lead with the RMiT/compliance angle.
7. **Standing RMiT ammo (unchanged):** DMARC non-compliance at Hong Leong (hlbb.com.my) + RHB (rhbbank.com); CIMB at monitoring-only (p=none). Verified role-mailbox channels (re-confirmed 2026-07-29, 5 verified): CIMB grc@cimb.com, risk@cimb.com, compliance@cimb.com; AmBank compliance@ambankgroup.com; Bank Islam compliance@bankislam.com.my. (cfo@bankislam.com.my did NOT verify last pass -- re-confirm before use.)
8. **v5.57/v5.65 reframes T2-insurer outreach (still current):** MSIG, Sun Life, Manulife, Berjaya Sompo CISO/IT-leader gaps are officially-confirmed disclosure gaps. Lead with the named CEO/CFO/CRO and frame the RMiT conversation around the absence of a disclosed local CISO. **NEW ammo from v5.68:** Chubb + Generali Life now HAVE named CISOs in the working DB -- pivot these from disclosure-gap framing to we-have-your-CISO direct outreach once merged.
9. **Foreign-bank wall -- reframe outreach, do not wait.** 7 of 8 foreign T1 partials have no real names pending (BNP, Citi, HSBC, ICBC, JPM, SMBC confirmed disclosure gaps). **Mizuho is the exception now** -- it gained a CISO (Noorhisham Rusmani) in the working DB. Lead the other 7 with the named contacts they DO have (HSBC: Brian McGuire CRO/Compliance/GRC composite, Elly Neoh CFO, Mei Ling Soo CIO; ICBC: Liau Cheek Compliance + Geng Hao CFO; Deutsche Bank: Jeng Yean Won CISO).
10. **Pipeline health (updated):** canonical idle streak EXTENDED to a new record (~77h 46m, 11th static cycle). **However, the working-DB enrichment is NOT exhausted** -- v5.68 produced 3 new named CISOs (incl. a T1 bank) that prior briefs declared impossible. This re-opens the research pipeline slightly and grows the merge backlog. The single remaining bottleneck remains the MERGE step, now ~11 cycles overdue. With the surplus freshly grown, recommend prioritizing the merge immediately; the daily-enrichment cron should also re-target the remaining T1 foreign-bank CISO gaps (BNP/Citi/HSBC/ICBC/JPM/SMBC) since Mizuho proved a foreign-bank CISO can surface.

## 6. Data-integrity alerts (all STANDING -- no new findings this cycle)
1. **[Standing] 3 placeholder rows carry zero real named contacts:** JCL Corporation Sdn Bhd (non-existent IB, 1 ENTITY-NON-EXISTENT cell); Malaysia International Islamic Bank IB (non-existent, 7 ENTITY-NON-EXISTENT cells -- falsely appears 7/7 loose, inflates loose full count by 1); Maybank (Khazanah-linked) (6 DUPLICATE-OF-MAYBANK-BERHAD cells). Recommend removal in 2nd cleanup -> 153 real prospects.
2. **[Standing] ~12 genuine non-name annotation cells** in canonical. Real-contact rate (strict) ~ 760/1,092 (69.6%); loose rate 772/70.7% remains the continuity metric.
3. **[Standing] Public Bank CIO cell is an unnamed annotation fragment** ((Public Bank Group) [Official: publicbankgroup.com]) -- not a named CIO. CISO is filled (Irene Deng) but CIO is effectively still a gap despite the cell being non-empty.
4. **[Standing] Setel semantic duplicate** -- 2 canonical rows (Setel (PETRONAS Dagangan) + Setel by PETRONAS Dagangan Berhad), both T4 E-Money 5/7. Unmerged; inflates count by 1.
5. **[Standing] Foreign-bank CISO wall = 7** (BNP, Citi, HSBC, ICBC, JPM, Mizuho, SMBC) in canonical -- **Mizuho wall now BREACHED in working DB** (CISO Noorhisham Rusmani found); 6 remain confirmed disclosure gaps (v5.65/v5.68 formally cites each).
6. **[NEW -- verification flag] Mizuho CISO source attribution is bare.** Working-DB v5.68 holds Noorhisham Rusmani with no cited URL/source -- unlike Chubb and Generali Life (both LinkedIn-cited). Verify provenance before promoting to canonical to avoid merging an un-sourced name.

---
*Next check will re-verify canonical md5 and surface any merge activity. The decisive signal to watch remains a canonical md5 change (d100a3ff -> new) indicating the overdue ~11-cycle merge has finally landed. Secondary signal: watch for v5.69+ working-DB versions that may surface more foreign-bank CISOs (Mizuho proved it is possible).*

# VoronDRQ Prospect Database Monitor - Intelligence Brief
**Run:** 2026-07-19 04:56 MYT | **Source:** prospect-database-enriched-v4.5.csv (repo HEAD e9a417d)
**Prev run:** 2026-07-16 09:40 MYT, commit b9a0b2c (v4.2 CSV) | **Classification:** TLP:AMBER

## 1. Database size and composition
- **205 institutions** (206 rows minus 1 ghost row from Sun Life CSV quoting corruption)
- **Tier:** T1=29, T2=53, T3=49, T4=35, T5=24, T6=15
- **Segment:** Licensed Banks 29, Insurers 26, GLC-Linked 24, Cooperatives 21, E-Money 19, MSBs 17, Investment Banks 15, Fintech Sandbox 13, Takaful 12, Dev FIs 11, Card Schemes 10, Payment Ops 6, Fintech Registered 2
- New institutions since last run: **0** (same 205)

## 2. Enrichment progress (current committed CSV)
- **115 / 205** institutions have >=1 stakeholder contact = **56.1%** enrichment rate
- **90** completely empty (43.9%)
- **516 / 1,435** role-cells filled = **36.0%** cell fill rate
- **30** institutions fully enriched (7/7)
- **Role completion (high to low):** CFO 91 (44.4%), Compliance 80 (39.0%), CIO 78 (38.0%), CRO 76 (37.1%), GRC 76 (37.1%), Internal Audit 61 (29.8%), **CISO 54 (26.3%)** = lowest

## 3. Changes since last check (v4.2 to v4.5)
3 new commits since last run: 2edebbe (v4.5 enrichment), 1bcb38b (v4.5 report), e9a417d (auto daily-enrichment 06:26Z).

**Nominal metrics moved DOWN:** enriched 119->115 (-4), cells 524->516 (-8), full7 32->30 (-2), rate 58.0%->56.1% (-1.9pp).

NOTE: This nominal drop is **mostly data-quality cleanup, not real contact loss.** The v4.2 counts were inflated by (a) CEO names misfiled in the CISO column and (b) unquoted commas splitting single CEO contacts across 2-4 columns. v4.5 removed these artifacts but did so **destructively** (deleted data to empty instead of re-filing CEOs correctly).

**Genuine NEW role-mapped contacts ADDED (outreach wins):**
- Citibank Berhad (T1) 3->5: +CRO Mark Fordyce Hart (RMC Chair, 41yr Citi veteran, ex-CFO Citi APAC), +Internal Audit Norazilla Md Tahir (AC Chair, ex-CFO Cagamas, FCA ICAEW)
- Generali Insurance Malaysia (T2) 2->5: +CFO Tony Lin, +CIO Laurent Crouet, +CRO Vincent Fong (official leadership page)
- Chubb Insurance (T2) 2->3: +GRC Dato Mohzani; FWD Insurance (T2) 3->4: +GRC; Manulife Insurance (T2) 4->5: +Compliance; Prudential (T2) +CIO (swapped for removed CEO-misfile)

**Data to RESTORE (destructive cleanup losses):**
- Kurnia Insurans 2->0 (CEO Junior Cho deleted), Manulife Takaful 2->0 (CEO Vibha Hamsi Coburn deleted), Zurich Life 4->0 (CEO Pauline Teoh + board deleted), Zurich Takaful 3->0 (CEO Nur Fatihah + board deleted)
- Sun Life 5->2: **lost legitimate CRO Nigel Hazell + Internal Audit Wong Ah Kow** (real role-mapped contacts)
- Great Eastern General/Life 7->6: CEO-misfile removed from CISO col (correction, but CEO name not re-filed)

## 4. Data-integrity alerts
1. **Report vs CSV mismatch:** v4.5 report claims 124/206 (60%) but the committed CSV is **115/205 (56.1%)**. Report overstates by ~9 institutions / ~4pp (generated from an uncommitted working copy). Do not cite 60%.
2. **Destructive cleanup:** CEO-misfile removal deleted contact data instead of re-filing it; 4 institutions now empty. Needs a restore pass.
3. **CSV quoting corruption persists:** Sun Life unescaped quote -> phantom row 181; unquoted commas split contacts across columns. All multi-word cells must be quoted.
4. **Bank Muamalat 7/7 inflated:** CISO cell = CEO Khairul Kamarudin; true T1 full = **16/29**, not 17.

## 5. Tier-1 priority prospects (sales outreach)
All 29 Tier-1 banks have >=1 contact (100%). 17 nominal / 16 true fully enriched.

**GREEN-LIGHT (new/ready this cycle):**
- **Citibank Berhad (T1) 5/7** - CRO + Internal Audit now mapped from official board PDF. Immediate outreach via CRO Mark Fordyce Hart.
- **Generali Insurance Malaysia (T2) 5/7** - full C-suite from official page. Cross-sell ready.

**Fully enriched T1 (16, ready for outreach):** Maybank, CIMB, RHB, AmBank, Alliance, Hong Leong, Bank Islam, OCBC, StanChart, Bank of China (+ Islamic subsidiaries).

**T1 partials (gap-fill):** Public Bank 6/7, Public Islamic 6/7, UOB 6/7 (-CISO only), BNP 5/7, HSBC 5/7, **Citibank 5/7 [new]**, ICBC 4/7, SMBC 3/7, Deutsche 2/7, Credit Suisse/J.P. Morgan/Mizuho 1/7.

## 6. Actionable next steps
1. **Outreach now:** Citibank (CRO + Audit), Generali (full C-suite), and the 16 fully-enriched T1 banks.
2. **URGENT repair pass:** restore deleted CEO/contacts (Kurnia, Zurich Life/Takaful, Manulife Takaful, Sun Life CRO+IA). Re-file CEOs into a proper CEO column, do not delete.
3. **CSV repair:** quote all multi-word cells; eliminate phantom row 181.
4. **Reconcile report:** re-publish v4.5 metrics against the committed CSV (115/56.1%, not 124/60%).
5. **T1 CISO gap-fill:** Public Bank/Public Islamic/UOB - approach via CRO/Head of IT as alternate entry.
6. **T1 thin foreign (CG Statement PDF strategy):** SMBC, Deutsche, Credit Suisse, J.P. Morgan, Mizuho.
7. **RMiT angle:** Hong Leong (hlbb.com.my) + RHB (rhbbank.com) DMARC non-compliant (auto-scan 06:26Z) - RMiT violation hook. CIMB risk@cimb.com email verified.

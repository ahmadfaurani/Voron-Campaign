# VoronDRQ Prospect Database Monitor — Intelligence Brief
**Run:** 2026-07-19 04:56 MYT | **Source:** prospect-database-7stakeholders.csv (repo HEAD de0fc96, v4.9)
**Prev run:** 2026-07-16 15:40 MYT, commit e9a417d (v4.5 CSV) | **Classification:** TLP:AMBER

## 1. Database size and composition
- **205 institutions** (unchanged from last run — 0 new, 0 removed)
- **Tier:** T1=29, T2=53, T3=49, T4=35, T5=24, T6=15
- **Segment:** Licensed Banks 29, Insurers 26, GLC-Linked 24, Cooperatives 21, E-Money 19, MSBs 17, Investment Banks 15, Fintech Sandbox 13, Takaful 12, Development FIs 11, Card Schemes 10, Payment Operators 6, Fintech Registered 2

## 2. Enrichment progress (current committed CSV)
- **119 / 205** institutions have >=1 stakeholder contact = **58.0%** enrichment rate (+1.9pp)
- **86** completely empty (42.0%)
- **531 / 1,435** role-cells filled = **37.0%** cell fill rate (+15 cells)
- **31** institutions fully enriched (7/7) (+1)
- **Role completion (high → low):** CFO 92 (44.9%), Compliance 81 (39.5%), GRC 80 (39.0%), CIO 79 (38.5%), CRO 78 (38.0%), Internal Audit 62 (30.2%), **CISO 59 (28.8%) = lowest**

## 3. Changes since last check (v4.5 → v4.9, 3 enrichment commits)
Commits: 70f19c7 (v4.6 restore+UOB CISO+Sun Life), f0f1067 (v4.7 +12 roles), de0fc96 (v4.9 QBE GRC, SeaBank→Ryt Bank, Manulife CEO).

**All metrics moved UP (clean progress — 0 contact losses):**

| Metric | v4.5 | v4.9 | Delta |
|--------|------|------|-------|
| Enriched (>=1) | 115 | 119 | +4 |
| Enrichment rate | 56.1% | 58.0% | +1.9pp |
| Filled cells | 516 | 531 | +15 |
| Full 7/7 | 30 | 31 | +1 |
| CISO roles | 54 | 59 | +5 |
| GRC roles | 76 | 80 | +4 |
| CRO roles | 76 | 78 | +2 |

**Previous "URGENT repair pass" EXECUTED:** The destructive cleanup losses flagged in the last brief (Kurnia, Zurich Life/Takaful, Manulife Takaful emptied; Sun Life CRO+IA lost) have all been restored and further enriched. Zero data lost this cycle.

### Newly enriched institutions (were empty → now populated)
- **Zurich Life Insurance Malaysia (T2, Insurers): 0→4/7** — restored CEO Pauline Teoh + Country CEO Junior Cho (CISO, GRC, CFO, CRO cols)
- **Zurich Takaful Malaysia (T2, Takaful): 0→3/7** — restored CEO Nur Fatihah Mustafa + Junior Cho (CISO, GRC, CIO)
- **Manulife Takaful Malaysia (T2, Takaful): 0→2/7** — restored Group CEO Vibha Hamsi Coburn (CISO, GRC)
- **Kurnia Insurans (Malaysia) (T2, Insurers): 0→2/7** — restored Country CEO Junior Cho (CISO, GRC)

### Contact gains (existing institutions enriched further)
- **UOB Malaysia Berhad (T1): 6→7/7** — +CISO Tobias Gondrom (Group CISO, UOB Group) **← T1 CISO GAP FILLED, now fully enriched**
- **Sun Life Malaysia Assurance (T2): 2→5/7** — +CRO Nigel Hazell (Board RMC Chair), +Compliance, +Internal Audit Wong Ah Kow (Board Audit Cmte Chair) — legitimate board-level contacts recovered

### New institutions added
**None.** Database roster unchanged at 205.

## 4. Data-integrity alerts
1. **CEO-misfile-in-CISO-column persists (~25 institutions):** CEOs filed in CISO column instead of true CISO contacts. Affects restored data (Zurich, Manulife Takaful, Kurnia — CEO names in CISO col) and many T3-T6 entries. These inflate CISO count with non-CISO data.
2. **Bank Muamalat (T1) "7/7" is inflated:** CISO cell = CEO Khairul Kamarudin, not a real CISO. True T1 full = **17** (not 18 nominal). Same issue flagged last run, still unresolved.
3. **UOB CISO is Group-level:** Tobias Gondrom is Group CISO (UOB Group, Singapore), not Malaysia-entity-specific. Acceptable as escalation contact but note the scope.

## 5. Tier-1 priority prospects (sales outreach)
All **29/29** Tier-1 banks have >=1 contact (100%). **18 nominal / 17 true** fully enriched.

**GREEN-LIGHT (new this cycle):**
- **UOB Malaysia Berhad (T1) — NOW 7/7** — CISO gap filled (Tobias Gondrom, Group CISO). Ready for full C-suite outreach.

**Fully enriched T1 (17 true, ready for outreach):** Maybank, CIMB, Alliance, AmBank, RHB, Hong Leong, Bank Islam, OCBC, StanChart, Bank of China (+ Islamic subsidiaries). Bank Muamalat nominal 7/7 but CISO = CEO (true 6/7).

**T1 partials (gap-fill priority):**
- Public Bank / Public Islamic: 6/7 (−CISO only) — approach via CRO/Head of IT
- BNP Paribas: 5/7 (−CISO, −CIO) | Citibank: 5/7 (−CISO, −Compliance) | HSBC: 5/7 (−CISO, −IA)
- ICBC: 4/7 (−CFO, −CIO, −GRC) | SMBC: 3/7 (−CRO, −Compliance, −CIO, −IA)
- Deutsche: 2/7 | Credit Suisse / J.P. Morgan / Mizuho: 1/7 (thin foreign banks — CG Statement PDF strategy)

**CISO remains the #1 gap across all tiers (28.8% completion)** — highest-leverage enrichment target.

## 6. Actionable next steps
1. **Outreach now:** UOB Malaysia (newly complete T1, all 7 roles mapped). Plus the 17 true fully-enriched T1 banks.
2. **T2 newly ready:** Sun Life Malaysia (5/7, board-level CRO+IA), Zurich Life (4/7), Zurich Takaful (3/7).
3. **CISO gap-fill (highest ROI):** 146/205 institutions lack a true CISO. T1 priorities: Public Bank, Public Islamic, BNP, Citibank, HSBC, ICBC. Approach via CRO/Head of IT as alternate entry where CISO not public.
4. **Repair CEO-misfile:** Re-file ~25 CEO entries from CISO column into a proper CEO/leadership column; clear CISO column for true CISO data or mark "not publicly listed." Corrects Bank Muamalat T1 inflation.
5. **T1 thin foreign banks:** SMBC, Deutsche, Credit Suisse, J.P. Morgan, Mizuho — target annual report / CG Statement PDFs for board committee chairs.
6. **RMiT angle:** Hong Leong + RHB DMARC non-compliance (prior auto-scan) — RMiT violation hook for outreach.

# VoronDRQ Prospect Database Monitor — Intelligence Brief
**Run:** 2026-07-17 15:55 MYT | **Source:** prospect-database-7stakeholders.csv (repo ROOT, commit 659f4ac, v5.0)
**Prev run:** 2026-07-17 09:53 MYT (reported root v4.6 metrics = 531 cells, 31 full) | **Classification:** TLP:AMBER

## 1. Database size and composition
- **205 real institutions** (UNCHANGED — 0 new, 0 removed). +1 phantom junk row (Sun Life CEO unescaped-quote fragment, line 182) inflates raw count to 206 — REGRESSION: phantom migrated into canonical root.
- **Tier:** T1=29, T2=53, T3=49, T4=35, T5=24, T6=15 (unchanged)
- **Segment:** Licensed Banks 29, Insurers 26, GLC-Linked 24, Cooperatives 21, E-Money 19, MSBs 17, Investment Banks 15, Fintech Sandbox 13, Takaful 12, Development FIs 11, Card Schemes 10, Payment Operators 6, Fintech Registered 2 (unchanged)

## 2. Enrichment progress (canonical root, v5.0)
- **119 / 205** institutions have >=1 stakeholder contact = **58.0%** enrichment rate (unchanged)
- **86** completely empty (42.0%)
- **546 / 1,435** role-cells filled = **38.0%** cell fill rate (+15 cells from 531)
- **32** institutions fully enriched (7/7) (+1) — Lonpac Insurance first insurer to 7/7
- **Role completion (high to low):** CFO 97 (47.3%, +5), Compliance 84 (41.0%, +3), CIO 84 (41.0%, +5), GRC 79 (38.5%, -1), CRO 79 (38.5%, +1), Internal Audit 66 (32.2%, +4), **CISO 57 (27.8%, -2) = lowest**
- CISO count DROPPED 59 to 57 — misfiled-CEO cleanups (Manulife Insurance, Manulife Takaful, Tokio Marine CEOs removed from CISO col). More ACCURATE now.

## 3. Changes since last check (v4.6 root -> v5.0 root, merge +10 new roles)
The v5.0 commit (12:58 MYT) merged the v4.7/v4.9 working copies into canonical root AND added 10 genuinely new roles. Working-copy changes previously narrated (Deutsche CFO, TEKUN +5, Takaful IKHLAS +2, Bank Rakyat CISO, MARA CIO, QBE GRC) are now in root — metrics authoritative.

### NEWLY FULLY ENRICHED (reached 7/7)
- **Lonpac Insurance Bhd (T2, Insurers) 5->7/7** +CFO Ng Seng Khin (Group CFO, LPI Capital official, HIGH-90) +IA Irene Hwang Siew Ling (Group Chief Internal Auditor, LPI Capital official, HIGH-90). FIRST INSURER to achieve full 7-role coverage.

### Genuinely NEW contacts (v5.0, not previously reported)
- **Manulife Insurance Berhad (T2, Insurers) 5->3** — CFO corrected to Ng Chun Nam (Annual Report 2024, OFFICIAL-85), +CIO Bernard Sia (OFFICIAL-85). -2 misfiled CEO entries cleaned from CISO+GRC cols. Net count down but quality UP.
- **Manulife Takaful Malaysia Berhad (T2, Takaful) 2->2** — misfiled CEOs (CISO+GRC) REPLACED with real CFO Ng Chun Nam +CIO Bernard Sia (OFFICIAL, shared mgmt with Manulife Insurance). Count unchanged, quality transformed. NOTE: entity may not exist separately per Annual Report 2024.
- **Sun Life Malaysia Assurance (T2, Insurers) 5->6** +CFO Lim Chin Har / Chew Lim (LinkedIn, MEDIUM-65; official page is image-based). Only -CIO remains.
- **Kurnia Insurans/AmGeneral (T2, Insurers) 2->5** +CIO Ganesan Vaithilingam +Compliance Peter Ong +IA Tan Bee Chuan (theorg.com, MEDIUM-60, source marked Unverified — VERIFY before outreach). CISO still = misfiled CEO Junior Cho; GRC still = rebrand note (junk).

### Misfiled-CEO cleanups (data quality fixes, count drops)
- Manulife Insurance: -CISO (Group CEO Vibha Hamsi Coburn removed) -GRC (CEO fragment removed)
- Manulife Takaful: -CISO (Group CEO) -GRC (CEO fragment) — replaced with real CFO+CIO
- Tokio Marine Life Insurance (T2): 2->1, -CISO (CEO Kang Yu Fen removed from CISO col)

### New institutions added
**None.** Roster unchanged at 205 (real).

## 4. Today's email-verification run (14:13 MYT, separate cron)
8 Tier-1 banks scanned, 56 role-based emails tested, 9 verified (16% rate):
- Maybank 3/7 (ciso, grc, internal.audit verified), CIMB 2/7 (ciso, grc), AmBank 1/7 (compliance), Bank Islam 1/7 (risk), OCBC 1/7 (compliance), UOB 1/7 (compliance)
- Hong Leong + RHB: 0/7 verified — both DMARC NON-COMPLIANT (RMiT violation hook)
- NOTE: these are generic role emails (ciso@bank.com.my), not individual named contacts. Per strict contact confidence model, pattern-inferred emails are NOT activated. Not merged to CSV.

## 5. Data-integrity alerts
1. **Phantom row regression:** Sun Life CEO unescaped-quote fragment (line 182) now in canonical root — inflates raw count to 206. RECURRING issue (was in v4.7 working copy, now merged to root). FIX: quote the Sun Life CISO cell properly.
2. **CEO-misfile partially cleaned:** Manulife Insurance, Manulife Takaful, Tokio Marine CEOs removed from CISO col (good). But Bank Muamalat (T1) CISO still = CEO Khairul Kamarudin; Sun Life CISO still = CEO Ho Teck Seng; Kurnia CISO still = CEO Junior Cho. True T1 full = 17 (not 18 nominal).
3. **Kurnia GRC cell = junk note** ("rebranded as Zurich General Insurance"). Sun Life Compliance cell = junk ("conf 90]"). Inflates their counts.

## 6. Tier-1 priority prospects (sales outreach)
All **29/29** Tier-1 banks have >=1 contact (100%). **18 nominal / 17 true** fully enriched.

**GREEN-LIGHT this cycle:**
- **Deutsche Bank (Malaysia) (T1) NOW 3/7** +CFO Liew Yeh Yin (OFFICIAL country.db.com) — CFO-led entry point. Still missing GRC, Compliance, CIO, IA.

**Fully enriched T1 (17 true, ready for outreach):** Maybank, CIMB, Alliance, AmBank, RHB, Hong Leong, Bank Islam, OCBC, StanChart, Bank of China, UOB (+ Islamic subsidiaries). Bank Muamalat nominal 7/7 but CISO=CEO (true 6/7).

**T1 partials (gap-fill priority):**
- Public Bank / Public Islamic: 6/7 (-CISO only)
- BNP Paribas: 5/7 (-CISO, -CIO) | Citibank: 5/7 (-CISO, -Compliance) | HSBC: 5/7 (-CISO, -IA)
- ICBC: 4/7 (-GRC, -CFO, -CIO) | Deutsche: 3/7 (-GRC, -Compliance, -CIO, -IA) | SMBC: 3/7 (-CRO, -Compliance, -CIO, -IA)
- Credit Suisse / J.P. Morgan / Mizuho: 1/7 (thin foreign banks — CG Statement PDF strategy)

**CISO remains #1 gap (27.8% true completion)** — highest-leverage enrichment target. T1 CISO priorities: Public Bank, BNP, Citibank, HSBC, ICBC.

## 7. Actionable next steps
1. **Outreach now:** Lonpac Insurance (T2, NEW 7/7, both new roles from LPI Capital official — HIGH conf, ready). Plus 17 true fully-enriched T1 banks.
2. **Manulife Insurance + Takaful:** real CFO+CIO now OFFICIAL (Annual Report 2024) — approach via CFO Ng Chun Nam / CIO Bernard Sia. Note shared management.
3. **VERIFY before outreach:** Kurnia/AmGeneral 3 new roles (theorg.com, Unverified) + Sun Life CFO (LinkedIn MEDIUM, image-based official page).
4. **REPAIR:** fix Sun Life phantom row (quote CISO cell); finish CEO-misfile cleanup (Bank Muamalat, Sun Life, Kurnia); remove junk fragments (Kurnia GRC, Sun Life Compliance).
5. **CISO gap-fill (highest ROI):** 148/205 lack true CISO. T1: Public Bank, BNP, Citibank, HSBC, ICBC.
6. **RMiT angle:** Hong Leong (hlbb.com.my) + RHB (rhbbank.com) DMARC non-compliant — RMiT violation hook for outreach.

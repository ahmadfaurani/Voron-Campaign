#!/usr/bin/env python3
"""
Context-Aware Sentiment Analysis for Entity Extraction Cycle
Source: 2026-07-25T14:00+08 entities extraction (274 extracted entity names; Phase-1)
Collection Cycle: 2026-07-25T000456Z (25 sources, 753,267 chars processed)
Method: VADER Sentiment Analysis on FRESH context snippets extracted directly from the
        2026-07-25 raw source collection (full_content + headlines).
Scale: -3 (very negative) to +3 (very positive)
Anomaly Detection: |z-score| > 2
Aggregation: By party and coalition

DATA-FRESHNESS NOTE
-------------------
The 2026-07-25T14:00+08 extraction produced Phase-1 entity name lists only
(`20260725-1400_entities_extracted.json`). Phase-2 per-entity context files (the
`contexts`/`snippet` store VADER normally consumes) had NOT been regenerated for this
cycle -- the per-entity files in persons/organizations/... are still dated 2026-07-16.

To produce a genuine 2026-07-25 sentiment signal (rather than re-scoring stale 2026-07-16
contexts), this run extracts context snippets directly from the 2026-07-25 raw source
collection and scores them with VADER. Coalition/party metadata is sourced from the
canonical per-entity files (2026-07-16 Phase-2 set) for the indexed entities, plus an
analyst-extended affiliation map for newly-extracted figures not yet in the index.
"""

import json
import os
import re
import glob
import statistics
from datetime import datetime, timezone
from collections import defaultdict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# ─────────────────────────── Configuration ───────────────────────────
ENTITIES_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/entities/"
RAW_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/raw/"
OUTPUT_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/sentiment-analysis/"

COLLECTION_TIMESTAMP = "2026-07-25T000456Z"
EXTRACTION_ID = "ext_20260725_1400_phase1"
EXTRACTION_TIMESTAMP = "2026-07-25T14:00:00+08:00"
ROSTER_FILE = os.path.join(ENTITIES_DIR, "20260725-1400_entities_extracted.json")
COLLECTION_GLOB = os.path.join(RAW_DIR, "2026-07-25T000456Z_*.json")
COLLECTION_SKIP = ("political_collection", "source_manifest", "INTELLIGENCE_BRIEF")

# Report timestamp — captured from `TZ=Asia/Kuala_Lumpur date` (MYT, UTC+8).
# Per task instruction: use the exact date-command output for ALL timestamp fields.
REPORT_TIMESTAMP_DISPLAY = "2026-07-25 16:00 +08"
REPORT_TIMESTAMP_FILE = "20260725-1600"
REPORT_DATE = "2026-07-25"

TYPE_SUBDIR = {
    "PERSON": "persons",
    "ORGANIZATION": "organizations",
    "LOCATION": "locations",
    "EVENT": "events",
    "CONCEPT": "concepts",
}
ROSTER_TYPE_KEY = {
    "PERSON": "PERSON",
    "ORGANIZATION": "ORGANIZATION",
    "LOCATION": "LOCATION",
    "EVENT": "EVENT",
    "CONCEPT": "CONCEPT",
}

# ─── Coalition / party mappings (from established sentiment-analysis skill) ───
PARTY_TO_COALITION = {
    "PKR": "PH", "DAP": "PH", "AMANAH": "PH", "MUDA": "PH",
    "UMNO": "BN", "MCA": "BN", "MIC": "BN",
    "BERSATU": "PN", "PAS": "PN",
    "Warisan": "WARISAN", "Parti Warisan": "WARISAN",
    "GPS": "GPS", "GRS": "GRS", "Pejuang": "PEJUANG",
    "BERSAMA": "BERSAMA", "Parti Bersama": "BERSAMA",
    "PRS": "GPS",   # PRS is a GPS component party
}
ORG_TO_COALITION = {
    "PH": "PH", "Pakatan Harapan": "PH",
    "BN": "BN", "Barisan Nasional": "BN",
    "PN": "PN", "Perikatan Nasional": "PN",
    "GPS": "GPS", "Gabungan Parti Sarawak": "GPS",
    "GRS": "GRS",
    "Pejuang": "PEJUANG",
    "PKR": "PH", "Parti Keadilan Rakyat": "PH",
    "DAP": "PH", "Democratic Action Party": "PH",
    "AMANAH": "PH", "Parti Amanah Negara": "PH",
    "MUDA": "PH", "Malaysia United Democratic Alliance": "PH",
    "UMNO": "BN", "United Malays National Organisation": "BN",
    "MCA": "BN", "Malaysian Chinese Association": "BN",
    "MIC": "BN", "Malaysian Indian Congress": "BN",
    "BERSATU": "PN", "Parti Pribumi Bersatu Malaysia": "PN",
    "PAS": "PN", "Parti Islam Se-Malaysia": "PN",
    "BERSAMA": "BERSAMA", "Parti Bersama": "BERSAMA",
    "Warisan": "WARISAN", "Parti Warisan": "WARISAN",
    "PRS": "GPS", "Parti Rakyat Sarawak": "GPS",   # PRS is a GPS component party
    "Keadilan": "PH",                       # Malay name for PKR (in roster since 2026-07-21)
}
# Case-insensitive coalition lookup (roster may use mixed-case e.g. "Bersatu", "WARISAN")
ORG_TO_COALITION_LOWER = {k.lower(): v for k, v in ORG_TO_COALITION.items()}


def org_coalition_lookup(key):
    """Case-insensitive coalition lookup for an org name / short_name."""
    if not key:
        return None
    return ORG_TO_COALITION_LOWER.get(key.lower())
FIGURE_AFFILIATIONS = {
    "Anwar Ibrahim": "PH", "Anwar": "PH", "PM Anwar": "PH",
    "Nurul Izzah Anwar": "PH", "Nurul Izzah": "PH",
    "Rafizi Ramli": "PH", "Rafizi": "PH",
    "Nik Nazmi Nik Ahmad": "PH", "Nik Nazmi": "PH",
    "Aminuddin Harun": "PH",
    "Hassan Abdul Karim": "PH",
    "Ahmad Zahid Hamidi": "BN", "Ahmad Zahid": "BN", "Zahid": "BN", "Zahid Hamidi": "BN",
    "Mohamad Hasan": "BN", "Tok Mat": "BN",
    "Jalaluddin Abdul Rahman": "BN",
    "Ab Rauf Yusoh": "BN",
    "Khairy Jamaluddin": "BN",
    "Muhyiddin Yassin": "PN", "Muhyiddin": "PN",
    "Mahathir Mohamad": "PEJUANG", "Mahathir": "PEJUANG",
    "Tiong King Sing": "GPS",
    "Sim Kui Hian": "GPS",
    "Mohd Ghazali Sabari": None,
}

# ─── Analyst-extended affiliations for newly-extracted figures ───
#    (party, coalition). Only well-established, publicly-known affiliations included.
#    Where an affiliation is reported in the collected source material itself, the
#    entity is grounded in the cycle's evidence (not fabricated).
NEW_FIGURE_AFFIL = {
    "Syed Saddiq": ("MUDA", "PH"),
    "Anthony Loke": ("DAP", "PH"),
    "Fahmi Fadzil": ("PKR", "PH"),
    "Hannah Yeoh": ("DAP", "PH"),
    "Maszlee": ("AMANAH", "PH"),
    "Mohamad Sabu": ("AMANAH", "PH"),
    "Asyraf Wajdi Dusuki": ("UMNO", "BN"),
    "Najib": ("UMNO", "BN"),
    "Najib Razak": ("UMNO", "BN"),
    "Shamsul Anuar Nasarah": ("UMNO", "BN"),
    "Mas Ermieyati Samsudin": ("BERSATU", "PN"),
    # 2026-07-18 cycle additions (publicly-known affiliations)
    "Onn Hafiz": ("UMNO", "BN"),          # Johor MB (UMNO/BN)
    "Onn Hafiz Ghazi": ("UMNO", "BN"),
    "Tan See Leng": ("PKR", "PH"),         # Minister (PKR/PH)
    "Tun Faisal Ismail Aziz": ("UMNO", "BN"),  # UMNO supreme council member
    "Azanna Ahmad Kamar": ("BERSATU", "PN"),   # contests under Bersatu (per source data)
    "Rajeentheran Suntheralingam": (None, None),
    # 2026-07-19 cycle additions (publicly-known affiliations)
    "Abdul Hadi Awang": ("PAS", "PN"),    # PAS President (PAS/PN)
    "Hadi Awang": ("PAS", "PN"),
    "Sanusi": ("PAS", "PN"),              # Sanusi Nor, PAS Kedah MB (PAS/PN)
    "Wee Ka Siong": ("MCA", "BN"),        # MCA President (MCA/BN)
    "Steven Sim": ("DAP", "PH"),          # Penang DCM (DAP/PH)
    # 2026-07-20 cycle additions (publicly-known affiliations)
    "Hajiji Noor": ("GRS", "GRS"),        # Sabah Chief Minister, GRS president (GRS)
    # 2026-07-21 cycle additions (publicly-known affiliations)
    "Abang Johari": ("PBB", "GPS"),       # Sarawak Premier, PBB president (GPS)
    "Joachim": ("GRS", "GRS"),            # Sabah DCM Joachim Gunsalam (GRS)
    "Bung Moktar Radin": ("UMNO", "BN"),  # Sabah UMNO chief / Kinabatangan MP (UMNO/BN)
    "Nga": ("DAP", "PH"),                 # Nga Kor Ming, DAP Minister (DAP/PH)
    # 2026-07-23 cycle additions (publicly-known affiliations)
    "Saifuddin Nasution": ("PKR", "PH"),  # Saifuddin Nasution Ismail, Home Minister (PKR/PH)
    "Saifuddin": ("PKR", "PH"),
    # 2026-07-24 cycle additions (publicly-known affiliations)
    "Hamzah Zainudin": ("BERSATU", "PN"),       # Bersatu Sec-Gen / PN opposition leader (BERSATU/PN)
    "Jalaluddin Alias": ("UMNO", "BN"),         # UMNO supreme council member (UMNO/BN)
    "Saarani Mohamad": ("UMNO", "BN"),          # Menteri Besar Perak (UMNO/BN)
    "Dzulkefly Ahmad": ("AMANAH", "PH"),        # Health Minister (AMANAH/PH)
    "Dr Dzul": ("AMANAH", "PH"),
    "Dzul": ("AMANAH", "PH"),
    # 2026-07-25 cycle additions (publicly-known affiliations)
    "Chong Zhemin": ("DAP", "PH"),              # Kampar MP (DAP/PH)
    "Ahmad Samsuri Mokhtar": ("PAS", "PN"),     # Menteri Besar Terengganu (PAS/PN)
    "Ahmad Samsuri": ("PAS", "PN"),
    "Tuan Ibrahim": ("PAS", "PN"),              # Tuan Ibrahim Tuan Man, PAS VP (PAS/PN)
    "Wilson Ugak Kumbong": ("GPS", "GPS"),      # Hulu Rajang MP, PBB (GPS)
    "Firdausi Suffian": (None, None),           # cardiologist, no party affiliation
}
# Merge multi-variant names for newly-extracted figures into one entity.
NEW_FIGURE_ALIASES = {
    "Syed Saddiq": ["Syed Saddiq", "Saddiq", "Syed Saddiq Syed Abdul Rahman",
                    "Syed Saddiq Sujud Syukur", "Saddiq Syed Abdul Rahman",
                    "Saddiq Sujud Syukur", "Saddiq Kutip RM", "Syed Saddiq Kutip RM",
                    "Syed Saddiq Sujud Syukur"],
    "Mohamad Sabu": ["Mohamad Sabu", "Mat Sabu"],
    "Abdul Razak": ["Abdul Razak", "Tun Abdul Razak", "Tun Razak", "Razak"],
    "Zulkifli Hasan": ["Zulkifli Hasan", "Zulkifli"],
    # 2026-07-18 cycle additions
    "Onn Hafiz": ["Onn Hafiz", "Onn Hafiz Ghazi"],
    "Najib Razak": ["Najib Razak", "Najib", "Datuk Seri Najib Razak"],
    "Razak Exchange": ["Razak Exchange", "Tun Razak Exchange"],
    # 2026-07-19 cycle additions
    "Abdul Hadi Awang": ["Abdul Hadi Awang", "Hadi Awang", "Tan Sri Abdul Hadi Awang"],
    # 2026-07-20 cycle additions
    "Hajiji Noor": ["Hajiji Noor", "Datuk Seri Hajiji Noor", "Seri Hajiji Noor"],
    "Tun Faisal Ismail Aziz": ["Tun Faisal Ismail Aziz", "Tun Faisal Ismail",
                               "Datuk Tun Faisal Ismail", "Faisal Ismail Aziz",
                               "Faisal Ismail"],
    # 2026-07-21 cycle additions
    "Abang Johari": ["Abang Johari"],
    "Joachim": ["Joachim", "Dr Joachim"],
    "Bung Moktar Radin": ["Bung Moktar Radin", "Datuk Seri Bung Moktar Radin",
                          "Seri Bung Moktar Radin"],
    "Wilfred Madius Tangau": ["Wilfred Madius Tangau", "Datuk Seri Wilfred Madius Tangau",
                              "Seri Wilfred Madius Tangau"],
    "Siti Hasmah": ["Siti Hasmah", "Dr Siti Hasmah"],
    "Azam Baki": ["Azam Baki", "Tan Sri Azam Baki"],
    "Khatijah Abdullah": ["Khatijah Abdullah", "Prof Khatijah Abdullah"],
    "Zulkifli Mohamad Al-Bakri": ["Zulkifli Mohamad Al-Bakri",
                                  "Dr Zulkifli Mohamad Al-Bakri"],
    "Mohd Faizal Ramli": ["Mohd Faizal Ramli", "Datuk Mohd Faizal Ramli"],
    "Ram Singh": ["Ram Singh", "Datuk Ram Singh"],
    "Mustafa": ["Mustafa", "Dr Mustafa"],
    "Datu Mustapha": ["Datu Mustapha", "Tun Datu Mustapha"],
    # 2026-07-23 cycle additions
    "Saifuddin Nasution": ["Saifuddin Nasution", "Saifuddin", "Datuk Seri Saifuddin Nasution"],
    # 2026-07-24 cycle additions
    "Hamzah Zainudin": ["Hamzah Zainudin", "Datuk Seri Hamzah Zainudin", "Zainudin"],
    "Jalaluddin Alias": ["Jalaluddin Alias", "Datuk Seri Jalaluddin Alias"],
    "Saarani Mohamad": ["Saarani Mohamad", "Datuk Seri Saarani Mohamad"],
    "Dzulkefly Ahmad": ["Dzulkefly Ahmad", "Dr Dzul", "Dzul"],
    # 2026-07-25 cycle additions
    "Chong Zhemin": ["Chong Zhemin", "Ahli Parlimen Chong Zhemin"],
    "Ahmad Samsuri Mokhtar": ["Ahmad Samsuri Mokhtar", "Dr Ahmad Samsuri Mokhtar",
                              "Datuk Seri Dr Ahmad Samsuri Mokhtar"],
    "Tuan Ibrahim": ["Tuan Ibrahim", "Tuan Ibrahim Tuan Man"],
    "Wilson Ugak Kumbong": ["Wilson Ugak Kumbong", "Datuk Wilson Ugak Kumbong"],
    "Firdausi Suffian": ["Firdausi Suffian", "Dr Firdausi Suffian"],
}

SENTIMENT_LABELS = {
    3: "Very Positive", 2: "Positive", 1: "Slightly Positive", 0: "Neutral",
    -1: "Slightly Negative", -2: "Negative", -3: "Very Negative",
}

PREFIX_HONORIFICS = [
    "Datuk Seri Dr", "Datuk Seri", "Datuk Dr", "Dato Sri", "Dato' Sri", "Dato'",
    "Datuk", "Dato", "Datin", "Tan Sri", "Tun Dr", "Tun", "Dr", "Prof",
    "PM", "YAB", "YB", "Haji", "Hjh", "Hj", "Tuan", "Puan", "Seri",
]

CONTEXT_BEFORE = 140
CONTEXT_AFTER = 170
MAX_CONTEXTS_PER_ENTITY = 30
MAX_CONTEXTS_PER_SOURCE = 4


# ─────────────────────────── Helpers ───────────────────────────
def scale_vader_to_score(compound: float) -> int:
    if compound >= 0.6:
        return 3
    elif compound >= 0.3:
        return 2
    elif compound >= 0.1:
        return 1
    elif compound > -0.1:
        return 0
    elif compound > -0.3:
        return -1
    elif compound > -0.6:
        return -2
    else:
        return -3


def clean_markdown(text: str) -> str:
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', text)
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'\*\*([^*]*)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]*)\*', r'\1', text)
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def normalize_name(name: str) -> str:
    s = name.strip()
    changed = True
    while changed:
        changed = False
        low = s.lower()
        for h in PREFIX_HONORIFICS:
            if low.startswith(h.lower() + " "):
                s = s[len(h) + 1:].strip()
                changed = True
                break
    return re.sub(r'\s+', ' ', s.lower()).strip()


def slugify(name: str) -> str:
    return re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')[:50]


def starts_with_honorific(name: str) -> bool:
    low = name.lower().strip()
    return any(low.startswith(h.lower() + " ") for h in PREFIX_HONORIFICS)


def cleanest_display(originals):
    """Pick the longest variant without a leading honorific; fall back to longest."""
    no_hon = [o for o in originals if not starts_with_honorific(o)]
    pool = no_hon if no_hon else originals
    return max(pool, key=len)


def calc_zscore(value, mean, std):
    if std == 0:
        return 0.0
    return (value - mean) / std


# ─────────────────────────── Loaders ───────────────────────────
def load_source_texts():
    texts = {}
    for f in sorted(glob.glob(COLLECTION_GLOB)):
        base = os.path.basename(f)
        if any(skip in base for skip in COLLECTION_SKIP):
            continue
        try:
            d = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        src = d.get("source") or base
        fc = d.get("full_content", "") or ""
        h = " ".join(d.get("headlines", []) or [])
        ph = " ".join(d.get("political_headlines", []) or [])
        texts[src] = (fc + "\n" + h + "\n" + ph).strip()
    return texts


def load_canonical_entities():
    """Load the indexed per-entity files (current authoritative store)."""
    entities = []
    for etype, subdir in TYPE_SUBDIR.items():
        for f in sorted(glob.glob(os.path.join(ENTITIES_DIR, subdir, "*.json"))):
            try:
                d = json.load(open(f, encoding='utf-8'))
            except Exception:
                continue
            name = d.get("name")
            if not name:
                continue
            aliases = [a for a in d.get("aliases", []) if a] if isinstance(d.get("aliases"), list) else []
            entities.append({
                "entity_id": d.get("entity_id") or f"{etype.lower()}_{slugify(name)}_001",
                "name": name,
                "type": etype,
                "subtype": d.get("subtype", ""),
                "coalition": d.get("coalition"),
                "party": d.get("party_affiliation"),
                "short_name": d.get("short_name"),
                "aliases": aliases,
                "is_new": False,
                "active_in_cycle": False,
                "roster_matches": [],
            })
    return entities


def load_roster():
    d = json.load(open(ROSTER_FILE, encoding='utf-8'))
    ents = d.get("entities", {})
    out = {}
    for etype, names in ents.items():
        out[etype] = [n for n in names if isinstance(n, str) and n.strip()]
    return out, d


def determine_coalition_party(ent):
    etype = ent["type"]
    name = ent["name"]
    if etype == "PERSON":
        coalition = ent.get("coalition")
        if coalition:
            party = ent.get("party")
            return coalition, party or _party_from_figure(name, coalition)
        party = ent.get("party")
        if party and PARTY_TO_COALITION.get(party):
            return PARTY_TO_COALITION[party], party
        fa = FIGURE_AFFILIATIONS.get(name)
        if fa is None and ent.get("aliases"):
            fa = FIGURE_AFFILIATIONS.get(ent["aliases"][0])
        if fa:
            return fa, None
        if ent.get("is_new"):
            for cand in [name] + list(ent.get("aliases", [])):
                if cand in NEW_FIGURE_AFFIL:
                    p, c = NEW_FIGURE_AFFIL[cand]
                    return c, p
        return None, party
    if etype == "ORGANIZATION":
        subtype = ent.get("subtype", "")
        short = ent.get("short_name")
        if subtype == "coalition":
            return org_coalition_lookup(short) or org_coalition_lookup(name) or name, None
        if subtype == "political_party":
            coalition = ent.get("coalition")
            if coalition:
                return coalition, short or name
            return org_coalition_lookup(short) or org_coalition_lookup(name), short or name
        # new org (no subtype) — try maps (case-insensitive)
        c = org_coalition_lookup(short) or org_coalition_lookup(name)
        if c:
            return c, short or name
        return None, None
    return None, None


def _party_from_figure(name, coalition):
    return None


# ─────────────────────────── Entity-set builder ───────────────────────────
def build_entity_set(canonical, roster):
    """Merge roster (2026-07-25) names into canonical entities; add new entities."""
    # Lookup: normalized name/alias -> canonical entity (per type)
    lookup = defaultdict(list)
    for e in canonical:
        keys = {normalize_name(e["name"])}
        for a in e.get("aliases", []):
            keys.add(normalize_name(a))
        for k in keys:
            lookup[k].append(e)

    matched_names = set()
    for etype, names in roster.items():
        for nm in names:
            norm = normalize_name(nm)
            cands = [c for c in lookup.get(norm, []) if c["type"] == etype]
            if cands:
                c = cands[0]
                if nm not in c["aliases"] and nm != c["name"]:
                    c["aliases"].append(nm)
                c["active_in_cycle"] = True
                c["roster_matches"].append(nm)
                matched_names.add((etype, nm))

    # Collect unmatched roster names (by type)
    unmatched = defaultdict(list)
    for etype, names in roster.items():
        for nm in names:
            if (etype, nm) not in matched_names:
                unmatched[etype].append(nm)

    # Build new entities
    new_entities = []

    # PERSON alias-rewrite map (multi-variant known figures only).
    rewrite = {}
    for fig, aliases in NEW_FIGURE_ALIASES.items():
        for a in aliases:
            rewrite[a.lower()] = fig
            rewrite[normalize_name(a)] = fig

    # 1) PERSON: group by figure-key (rewrite) else by normalized name.
    person_groups = defaultdict(list)
    person_fig = {}
    for nm in unmatched.get("PERSON", []):
        nk = normalize_name(nm)
        fig = rewrite.get(nk) or rewrite.get(nm.lower())
        key = fig if fig else nk
        person_groups[key].append(nm)
        person_fig[key] = fig
    for key, originals in person_groups.items():
        fig = person_fig[key]
        display = fig if fig else cleanest_display(originals)
        ent = {
            "entity_id": f"person_{slugify(display)}_20260725",
            "name": display, "type": "PERSON", "subtype": "politician",
            "coalition": None, "party": None, "short_name": None,
            "aliases": list(dict.fromkeys(originals)),
            "is_new": True, "active_in_cycle": True,
            "roster_matches": list(originals),
        }
        new_entities.append(ent)

    # 2) Non-PERSON: group by normalized name (handles honorific variants).
    for etype in ("ORGANIZATION", "LOCATION", "EVENT", "CONCEPT"):
        groups = defaultdict(list)
        for nm in unmatched.get(etype, []):
            groups[normalize_name(nm)].append(nm)
        for _key, originals in groups.items():
            display = cleanest_display(originals)
            ent = {
                "entity_id": f"{etype.lower()}_{slugify(display)}_20260725",
                "name": display, "type": etype,
                "subtype": "" if etype in ("LOCATION", "EVENT", "CONCEPT") else "other",
                "coalition": None, "party": None, "short_name": None,
                "aliases": list(dict.fromkeys(originals)),
                "is_new": True, "active_in_cycle": True,
                "roster_matches": list(originals),
            }
            new_entities.append(ent)

    analysis = canonical + new_entities
    # Finalize coalition/party
    for e in analysis:
        c, p = determine_coalition_party(e)
        e["coalition"] = c
        e["party"] = p
    return analysis, matched_names, unmatched


# ─────────────────────────── Context extraction ───────────────────────────
def search_variants(ent):
    variants = []
    seen = set()
    for v in [ent["name"]] + list(ent.get("aliases", [])):
        v = v.strip()
        if v and len(v) >= 2 and v.lower() not in seen:
            seen.add(v.lower())
            variants.append(v)
    return variants


def extract_contexts(variants, source_texts):
    contexts = []
    seen_key = set()
    for src, text in source_texts.items():
        if not text:
            continue
        tl = text.lower()
        per_source = 0
        for var in variants:
            v = var.lower()
            if len(v) < 2:
                continue
            start = 0
            while True:
                idx = tl.find(v, start)
                if idx == -1:
                    break
                a = max(0, idx - CONTEXT_BEFORE)
                b = min(len(text), idx + len(var) + CONTEXT_AFTER)
                snip = clean_markdown(text[a:b])
                if a > 0:
                    snip = "…" + snip
                if b < len(text):
                    snip = snip + "…"
                key = snip[:140].lower()
                if len(snip) > 15 and key not in seen_key:
                    seen_key.add(key)
                    contexts.append({"source": src, "snippet": snip})
                    per_source += 1
                    if len(contexts) >= MAX_CONTEXTS_PER_ENTITY:
                        return contexts
                start = idx + len(var)
                if per_source >= MAX_CONTEXTS_PER_SOURCE:
                    break
            if per_source >= MAX_CONTEXTS_PER_SOURCE:
                break
    return contexts


def analyze_entity(analyzer, ent, source_texts):
    variants = search_variants(ent)
    contexts = extract_contexts(variants, source_texts)
    scores = []
    for ctx in contexts:
        snip = ctx["snippet"]
        if len(snip) > 5:
            scores.append(analyzer.polarity_scores(snip)["compound"])
    if scores:
        mean_c = statistics.mean(scores)
        std_c = statistics.stdev(scores) if len(scores) > 1 else 0.0
        return mean_c, std_c, len(scores), True, contexts
    # fallback: entity name itself, dampened
    vs = analyzer.polarity_scores(ent["name"])
    return vs["compound"] * 0.3, 0.0, 0, False, []


# ─────────────────────────── Markdown report ───────────────────────────
def generate_markdown(report):
    s = report["summary"]
    md = f"""# Sentiment Analysis Report

**Classification:** TLP:AMBER
**Generated:** {report['report_timestamp']}
**Report Date:** {report.get('report_date', '2026-07-25')}
**Report Timestamp:** {report['report_timestamp']}
**Extraction ID:** {report['extraction_id']}
**Extraction Source:** {report['extraction_source']}
**Collection Cycle:** {report['collection_cycle']}
**Source Count:** {report['source_count']}
**Analysis Method:** {report['analysis_method']}
**Score Range:** {report['score_range']}
**Anomaly Threshold:** {report['anomaly_threshold']}

> **Data-freshness note:** The 2026-07-25 extraction produced Phase-1 entity name lists
> only; Phase-2 per-entity context files were not regenerated for this cycle. To produce a
> genuine 2026-07-25 sentiment signal, context snippets were extracted directly from the
> 2026-07-25 raw source collection and scored with VADER. Coalition/party metadata sourced
> from the canonical per-entity files (2026-07-16 Phase-2 set) plus an analyst-extended
> affiliation map for newly-extracted figures.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Roster Entities (Phase-1 names) | {s['roster_total']} |
| Analysis Entities (merged) | {s['total_entities_analyzed']} |
| Canonical Entities (from index) | {s['canonical_entities']} |
| New Entities (this cycle) | {s['new_entities']} |
| Roster Names Matched to Canonical | {s['roster_matched_to_canonical']} |
| Sources Processed | {s['sources_processed']} |
| Entities with Context | {s['entities_with_context']} |
| Entities without Context (fallback) | {s['entities_without_context']} |
| Overall Mean Sentiment | {s['overall_mean_sentiment']:+.3f} |
| Overall Std Deviation | {s['overall_std_dev']:.3f} |
| Overall Median Sentiment | {s['overall_median_sentiment']:+.3f} |
| Overall Raw Mean | {s['overall_raw_mean']:.4f} |
| Overall Raw Std Dev | {s['overall_raw_std']:.4f} |
| Sentiment Range | [{s['sentiment_range'][0]:+d}, {s['sentiment_range'][1]:+d}] |
| Positive Entities | {s['positive_entities']} |
| Neutral Entities | {s['neutral_entities']} |
| Negative Entities | {s['negative_entities']} |
| Anomalies Detected | {s['anomalies_detected']} |
| Coalitions Analyzed | {len(s['coalitions_analyzed'])} |
| Parties Analyzed | {len(s['parties_analyzed'])} |

### Sentiment Distribution

```
Positive ({s['positive_entities']})  {"█" * s['positive_entities']}
Neutral  ({s['neutral_entities']})  {"█" * s['neutral_entities']}
Negative ({s['negative_entities']})  {"█" * s['negative_entities']}
```

---

## Coalition Aggregate Sentiment

| Coalition | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range |
|-----------|:-:|------|:----------:|:-------:|:--------:|:-----:|"""
    for coalition, agg in sorted(report["coalition_aggregates"].items(),
                                 key=lambda x: x[1]["mean_score"], reverse=True):
        md += f"\n| {coalition} | {agg['sentiment_score']:+d} | {agg['sentiment_label']} | {agg['mean_score']:.4f} | {agg['std_dev']:.4f} | {agg['entity_count']} | [{agg['min_score']:.3f}, {agg['max_score']:.3f}] |"
    md += "\n### Coalition Entities\n"
    for coalition, agg in sorted(report["coalition_aggregates"].items(),
                                 key=lambda x: x[1]["mean_score"], reverse=True):
        md += f"- **{coalition}** ({agg['sentiment_score']:+d}, {agg['sentiment_label']}): {', '.join(agg['entities'])}\n"

    md += "\n---\n\n## Party Aggregate Sentiment\n\n"
    md += "| Party | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range | Coalition |\n"
    md += "|-------|:-:|------|:----------:|:-------:|:--------:|:-----:|:---------:|"
    p2c = dict(PARTY_TO_COALITION)
    p2c.update({"GRS": "GRS", "Pejuang": "PEJUANG", "BERSAMA": "BERSAMA", "Warisan": "WARISAN", "GPS": "GPS"})
    for party, agg in sorted(report["party_aggregates"].items(),
                             key=lambda x: x[1]["mean_score"], reverse=True):
        coalition = p2c.get(party, "—")
        md += f"\n| {party} | {agg['sentiment_score']:+d} | {agg['sentiment_label']} | {agg['mean_score']:.4f} | {agg['std_dev']:.4f} | {agg['entity_count']} | [{agg['min_score']:.3f}, {agg['max_score']:.3f}] | {coalition} |"
    md += "\n### Party Entities\n"
    for party, agg in sorted(report["party_aggregates"].items(),
                             key=lambda x: x[1]["mean_score"], reverse=True):
        coalition = p2c.get(party, "—")
        md += f"- **{party}** ({agg['sentiment_score']:+d}, {agg['sentiment_label']}, → {coalition}): {', '.join(agg['entities'])}\n"

    md += "\n---\n\n## Sentiment Anomalies (|z-score| > 2)\n\n"
    if report["anomalies"]:
        md += f"**{len(report['anomalies'])} anomalies detected.**\n\n"
        md += "| # | Entity | Type | Score | Label | Z-Score | Direction | Coalition | Party | Contexts |\n"
        md += "|---|--------|------|:-----:|-------|:-------:|:---------:|-----------|:------:|:--------:|"
        for i, a in enumerate(report["anomalies"], 1):
            coalition = a.get("coalition") or "N/A"
            party = a.get("party") or "—"
            md += f"\n| {i} | {a['entity']} | {a['entity_type']} | {a['sentiment_score']:+d} | {a['sentiment_label']} | {a['z_score']:.4f} | {a['direction']} | {coalition} | {party} | {a['context_count']} |"
    else:
        md += "*No significant anomalies detected (all entity sentiment scores within 2 standard deviations of mean).*\n"

    md += "\n---\n\n## Entity Sentiments by Type\n"
    for etype, entities_dict in report["entity_sentiments"].items():
        md += f"\n### {etype}\n\n"
        md += "| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Coalition | Party | New |\n"
        md += "|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|:-----:|:---:|"
        for entity, data in sorted(entities_dict.items(), key=lambda x: x[1]["raw_compound"], reverse=True):
            anomaly_mark = "⚠️" if data["is_anomaly"] else ""
            coalition = data.get("coalition") or "—"
            party = data.get("party") or "—"
            new_mark = "✚" if data.get("is_new") else ""
            md += f"\n| {entity} | {data['sentiment_score']:+d} | {data['sentiment_label']} | {data['raw_compound']:.4f} | {data['z_score']:.4f} | {anomaly_mark} | {data['context_count']} | {coalition} | {party} | {new_mark} |"

    md += f"""
---

## Methodology

1. **Entity Source:** Loaded from the 2026-07-25T14:00+08 extraction roster ({s['roster_total']} Phase-1 entity names) plus the {s['canonical_entities']} canonical entities from the per-entity index. Roster names were merged into canonical entities by normalized name/alias matching (honorific-stripped); unmerged names were added as new entities ({s['new_entities']} new).
2. **Context Extraction:** For each entity, search variants (canonical name + aliases + roster matches) were located in the 2026-07-25 raw source collection ({s['sources_processed']} sources, {s['sources_processed']} processed, ~{s['total_chars']} chars). A context window (~{CONTEXT_BEFORE}+{CONTEXT_AFTER} chars) was extracted around each mention (markdown stripped, de-duplicated, capped at {MAX_CONTEXTS_PER_ENTITY}/entity).
3. **Sentiment Scoring:** Applied VADER to each context snippet; entity sentiment = mean compound across snippets.
4. **Score Mapping:** VADER compound (-1..+1) → 7-point Likert (-3..+3): +3 ≥0.6, +2 ≥0.3, +1 ≥0.1, 0 (-0.1..0.1), -1 >-0.3, -2 >-0.6, -3 ≤-0.6.
5. **Anomaly Detection:** Z-score on raw compound vs overall mean/std; flagged when |z| > 2.
6. **Coalition/Party Aggregation:** Persons + political-party/coalition orgs mapped via per-entity metadata and affiliation maps (FIGURE_AFFILIATIONS, ORG_TO_COALITION, analyst-extended NEW_FIGURE_AFFIL).

---

*Report generated by OpenCLaw Sentiment Analysis Pipeline (sentiment-analysis skill)*
*VADER: Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.*
"""
    return md


# ─────────────────────────── Main ───────────────────────────
def main():
    print("=" * 72)
    print("SENTIMENT ANALYSIS — Entity Extraction Cycle")
    print(f"Collection: {COLLECTION_TIMESTAMP}")
    print(f"Extraction ID: {EXTRACTION_ID}")
    print("=" * 72)

    analyzer = SentimentIntensityAnalyzer()

    print("\n[1] Loading 2026-07-25 raw source collection...")
    source_texts = load_source_texts()
    total_chars = sum(len(t) for t in source_texts.values())
    print(f"  Sources loaded: {len(source_texts)} | total chars: {total_chars}")

    print("\n[2] Loading canonical per-entity files + extraction roster...")
    canonical = load_canonical_entities()
    roster, roster_meta = load_roster()
    roster_total = sum(len(v) for v in roster.values())
    print(f"  Canonical entities: {len(canonical)} | Roster names: {roster_total}")
    for etype in TYPE_SUBDIR:
        print(f"    {etype}: roster={len(roster.get(etype, []))}")

    print("\n[3] Building analysis entity set (merge roster → canonical; add new)...")
    analysis, matched, unmatched = build_entity_set(canonical, roster)
    canonical_count = sum(1 for e in analysis if not e["is_new"])
    new_count = sum(1 for e in analysis if e["is_new"])
    active_canonical = sum(1 for e in analysis if not e["is_new"] and e["active_in_cycle"])
    print(f"  Analysis entities: {len(analysis)} (canonical={canonical_count}, new={new_count})")
    print(f"  Canonical active in 2026-07-25: {active_canonical}/{canonical_count}")
    print(f"  Roster names matched to canonical: {len(matched)}")

    print(f"\n[4] Extracting fresh contexts + scoring sentiment for {len(analysis)} entities...")
    entity_sentiments = {t: {} for t in TYPE_SUBDIR}
    all_scores, all_raw = [], []
    for i, ent in enumerate(analysis, 1):
        mean_c, std_c, ctx_n, has_ctx, contexts = analyze_entity(analyzer, ent, source_texts)
        score = scale_vader_to_score(mean_c)
        coalition, party = ent["coalition"], ent["party"]
        rec = {
            "entity_id": ent["entity_id"],
            "sentiment_score": score,
            "sentiment_label": SENTIMENT_LABELS.get(score, "Unknown"),
            "raw_compound": round(mean_c, 4),
            "raw_std": round(std_c, 4),
            "context_count": ctx_n,
            "has_context": has_ctx,
            "coalition": coalition,
            "party": party,
            "subtype": ent["subtype"],
            "is_new": ent["is_new"],
            "active_in_cycle": ent["active_in_cycle"],
            "roster_matches": ent["roster_matches"],
        }
        entity_sentiments[ent["type"]][ent["name"]] = rec
        all_scores.append(score)
        all_raw.append(mean_c)
        if i % 25 == 0 or i == len(analysis):
            print(f"  ... {i}/{len(analysis)} done")

    print("\n[5] Overall statistics + anomaly detection (|z|>2)...")
    overall_mean = statistics.mean(all_scores) if all_scores else 0
    overall_std = statistics.stdev(all_scores) if len(all_scores) > 1 else 0
    overall_median = statistics.median(all_scores) if all_scores else 0
    raw_mean = statistics.mean(all_raw) if all_raw else 0
    raw_std = statistics.stdev(all_raw) if len(all_raw) > 1 else 0
    print(f"  Mean: {overall_mean:.3f} | Std: {overall_std:.3f} | Median: {overall_median:.3f}")
    print(f"  Raw mean: {raw_mean:.4f} | Raw std: {raw_std:.4f} | Range: [{min(all_scores)}, {max(all_scores)}]")

    anomalies = []
    for etype, edict in entity_sentiments.items():
        for name, data in edict.items():
            z = calc_zscore(data["raw_compound"], raw_mean, raw_std)
            data["z_score"] = round(z, 4)
            data["is_anomaly"] = abs(z) > 2
            if abs(z) > 2:
                anomalies.append({
                    "entity": name, "entity_id": data["entity_id"], "entity_type": etype,
                    "sentiment_score": data["sentiment_score"], "sentiment_label": data["sentiment_label"],
                    "raw_compound": data["raw_compound"], "z_score": round(z, 4),
                    "direction": "positive" if z > 0 else "negative",
                    "coalition": data["coalition"], "party": data["party"],
                    "context_count": data["context_count"], "is_new": data["is_new"],
                })
    anomalies.sort(key=lambda x: abs(x["z_score"]), reverse=True)
    print(f"  Anomalies: {len(anomalies)}")
    for a in anomalies[:25]:
        print(f"    ⚠️  {a['entity']} ({a['entity_type']}): score={a['sentiment_score']:+d} z={a['z_score']:.4f} ({a['direction']})")

    print("\n[6] Aggregating by coalition + party...")
    coalition_scores = defaultdict(list)
    coalition_entities_map = defaultdict(list)
    party_scores = defaultdict(list)
    party_entities_map = defaultdict(list)
    for etype, edict in entity_sentiments.items():
        for name, data in edict.items():
            c = data["coalition"]; p = data["party"]
            if c:
                coalition_scores[c].append(data["raw_compound"])
                coalition_entities_map[c].append(name)
            if p:
                party_scores[p].append(data["raw_compound"])
                party_entities_map[p].append(name)

    def agg(scores, emap):
        m = statistics.mean(scores)
        sc = scale_vader_to_score(m)
        return {
            "mean_score": round(m, 4), "sentiment_score": sc,
            "sentiment_label": SENTIMENT_LABELS.get(sc, "Unknown"),
            "median_score": round(statistics.median(scores), 4),
            "std_dev": round(statistics.stdev(scores), 4) if len(scores) > 1 else 0.0,
            "min_score": min(scores), "max_score": max(scores),
            "entity_count": len(scores), "entities": emap,
        }

    coalition_aggregates = {c: agg(s, coalition_entities_map[c]) for c, s in sorted(coalition_scores.items())}
    party_aggregates = {p: agg(s, party_entities_map[p]) for p, s in sorted(party_scores.items())}
    for c, a in coalition_aggregates.items():
        print(f"  Coalition {c}: {a['sentiment_score']:+d} ({a['sentiment_label']}) mean={a['mean_score']:.4f} n={a['entity_count']}")
    for p, a in party_aggregates.items():
        print(f"  Party {p}: {a['sentiment_score']:+d} ({a['sentiment_label']}) mean={a['mean_score']:.4f} n={a['entity_count']}")

    print("\n[7] Building + saving reports...")
    # Use the fixed MYT report timestamp captured from `TZ=Asia/Kuala_Lumpur date`
    # (per task instruction — never guess the timestamp).
    report_ts = REPORT_TIMESTAMP_FILE          # filename-safe: 20260725-1600
    report_ts_display = REPORT_TIMESTAMP_DISPLAY  # display:     2026-07-25 16:00 +08
    pos = sum(1 for s in all_scores if s > 0)
    neu = sum(1 for s in all_scores if s == 0)
    neg = sum(1 for s in all_scores if s < 0)
    with_ctx = sum(1 for et in entity_sentiments.values() for d in et.values() if d["has_context"])

    summary = {
        "roster_total": roster_total,
        "total_entities_analyzed": len(analysis),
        "canonical_entities": canonical_count,
        "new_entities": new_count,
        "roster_matched_to_canonical": len(matched),
        "entities_by_type": {k: len(v) for k, v in entity_sentiments.items()},
        "sources_processed": len(source_texts),
        "total_chars": total_chars,
        "entities_with_context": with_ctx,
        "entities_without_context": len(analysis) - with_ctx,
        "overall_mean_sentiment": round(overall_mean, 3),
        "overall_std_dev": round(overall_std, 3),
        "overall_median_sentiment": round(overall_median, 3),
        "overall_raw_mean": round(raw_mean, 4),
        "overall_raw_std": round(raw_std, 4),
        "sentiment_range": [min(all_scores) if all_scores else 0, max(all_scores) if all_scores else 0],
        "positive_entities": pos, "neutral_entities": neu, "negative_entities": neg,
        "anomalies_detected": len(anomalies),
        "coalitions_analyzed": list(coalition_aggregates.keys()),
        "parties_analyzed": list(party_aggregates.keys()),
    }

    report = {
        "report_timestamp": report_ts_display,
        "report_date": REPORT_DATE,
        "extraction_id": EXTRACTION_ID,
        "extraction_source": EXTRACTION_TIMESTAMP,
        "collection_cycle": COLLECTION_TIMESTAMP,
        "source_count": len(source_texts),
        "analysis_method": "VADER Sentiment Analysis on fresh context snippets extracted from 2026-07-25 raw collection",
        "score_range": "-3 (very negative) to +3 (very positive)",
        "anomaly_threshold": "|z-score| > 2",
        "summary": summary,
        "entity_sentiments": entity_sentiments,
        "coalition_aggregates": coalition_aggregates,
        "party_aggregates": party_aggregates,
        "anomalies": anomalies,
    }

    json_path = os.path.join(OUTPUT_DIR, f"sentiment_report_{report_ts}.json")
    md_path = os.path.join(OUTPUT_DIR, f"sentiment_report_{report_ts}.md")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(generate_markdown(report))
    with open(os.path.join(OUTPUT_DIR, "sentiment_latest.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    with open(os.path.join(OUTPUT_DIR, "sentiment_latest.md"), "w", encoding="utf-8") as f:
        f.write(generate_markdown(report))

    print(f"  JSON: {json_path}")
    print(f"  MD:   {md_path}")
    print(f"  Latest symlinks updated")
    print("\n" + "=" * 72)
    print("SENTIMENT ANALYSIS COMPLETE")
    print("=" * 72)
    print(f"  Entities: {len(analysis)} (canonical {canonical_count} + new {new_count})")
    print(f"  With context: {with_ctx} | Mean: {overall_mean:+.3f} | Anomalies: {len(anomalies)}")
    print(f"  Coalitions: {list(coalition_aggregates.keys())}")
    print(f"  Parties: {list(party_aggregates.keys())}")
    # also print a compact result block for the cron log
    print("\n--- RESULT BLOCK ---")
    print(json.dumps({
        "report_timestamp": report_ts_display,
        "report_date": REPORT_DATE,
        "json": json_path, "md": md_path,
        "entities": len(analysis), "with_context": with_ctx,
        "mean": round(overall_mean, 3), "anomalies": len(anomalies),
        "coalitions": {c: coalition_aggregates[c]["sentiment_score"] for c in coalition_aggregates},
        "parties": {p: party_aggregates[p]["sentiment_score"] for p in party_aggregates},
        "anomaly_entities": [a["entity"] for a in anomalies],
    }))


if __name__ == "__main__":
    main()

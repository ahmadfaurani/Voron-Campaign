#!/usr/bin/env python3
"""
Context-Aware Sentiment Analysis for Entity Extraction Cycle
Source: 2026-07-16T001140Z entities extraction (78 entities)
Method: VADER Sentiment Analysis on entity context snippets (from per-entity JSON files)
Scale: -3 (very negative) to +3 (very positive)
Anomaly Detection: |z-score| > 2
Aggregation: By party and coalition
"""

import json
import os
import re
import glob
import statistics
from datetime import datetime, timezone
from collections import defaultdict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Configuration
ENTITIES_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/entities/"
OUTPUT_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/sentiment-analysis/"
EXTRACTION_FILE = os.path.join(ENTITIES_DIR, "extraction_2026-07-16T001140Z_2026-07-16T061213Z.json")
COLLECTION_TIMESTAMP = "2026-07-16T001140Z"
EXTRACTION_ID = "ext_20260716_061213_001"
EXTRACTION_TIMESTAMP = "2026-07-16T06:12:13+00:00"

# ─── Party → Coalition Mapping ───
PARTY_TO_COALITION = {
    "PKR": "PH",
    "DAP": "PH",
    "AMANAH": "PH",
    "MUDA": "PH",
    "UMNO": "BN",
    "MCA": "BN",
    "MIC": "BN",
    "BERSATU": "PN",
    "PAS": "PN",
    "Warisan": "WARISAN",
    "Parti Warisan": "WARISAN",
    "GPS": "GPS",
    "GRS": "GRS",
    "Pejuang": "PEJUANG",
    "BERSAMA": "BERSAMA",
    "Parti Bersama": "BERSAMA",
}

# ─── Organization → Coalition Mapping ───
ORG_TO_COALITION = {
    # Coalitions (map to themselves)
    "PH": "PH", "Pakatan Harapan": "PH",
    "BN": "BN", "Barisan Nasional": "BN",
    "PN": "PN", "Perikatan Nasional": "PN",
    "GPS": "GPS", "Gabungan Parti Sarawak": "GPS",
    "GRS": "GRS",
    "Pejuang": "PEJUANG",
    # Political parties
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
}

# Political figures → coalition affiliation (fallback when extraction metadata is missing)
FIGURE_AFFILIATIONS = {
    "Anwar Ibrahim": "PH", "Anwar": "PH", "PM Anwar": "PH",
    "Nurul Izzah Anwar": "PH", "Nurul Izzah": "PH",
    "Rafizi Ramli": "PH", "Rafizi": "PH",
    "Nik Nazmi Nik Ahmad": "PH",
    "Aminuddin Harun": "PH",
    "Hassan Abdul Karim": "PH",
    "Ahmad Zahid Hamidi": "BN", "Ahmad Zahid": "BN", "Zahid": "BN",
    "Mohamad Hasan": "BN", "Tok Mat": "BN",
    "Jalaluddin Abdul Rahman": "BN",
    "Ab Rauf Yusoh": "BN",
    "Khairy Jamaluddin": "BN",
    "Muhyiddin Yassin": "PN", "Muhyiddin": "PN",
    "Mahathir Mohamad": "PEJUANG",
    "Tiong King Sing": "GPS",
    "Sim Kui Hian": "GPS",
    "Mohd Ghazali Sabari": None,
}

# Sentiment label mapping
SENTIMENT_LABELS = {
    3: "Very Positive",
    2: "Positive",
    1: "Slightly Positive",
    0: "Neutral",
    -1: "Slightly Negative",
    -2: "Negative",
    -3: "Very Negative",
}

# Entity type arrays in extraction JSON
ENTITY_TYPE_KEYS = {
    "PERSON": "persons",
    "ORGANIZATION": "organizations",
    "LOCATION": "locations",
    "EVENT": "events",
    "CONCEPT": "concepts",
}

# Subdirectory for per-entity files
TYPE_SUBDIR = {
    "PERSON": "persons",
    "ORGANIZATION": "organizations",
    "LOCATION": "locations",
    "EVENT": "events",
    "CONCEPT": "concepts",
}


def scale_vader_to_score(compound: float) -> int:
    """Scale VADER compound score (-1 to 1) to integer sentiment score (-3 to +3)."""
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


def clean_markdown_links(text: str) -> str:
    """Strip markdown link syntax to get clean text."""
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', text)
    text = re.sub(r'\*\*([^*]*)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]*)\*', r'\1', text)
    return text.strip()


def load_extraction_data() -> dict:
    """Load the entity extraction JSON for this collection cycle."""
    with open(EXTRACTION_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_entity_file(entity_id: str, entity_type: str) -> dict:
    """Load a per-entity JSON file to get contexts/snippets."""
    subdir = TYPE_SUBDIR.get(entity_type, "")
    filename = f"{entity_id}.json"
    filepath = os.path.join(ENTITIES_DIR, subdir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def determine_coalition(entity_name: str, entity_type: str, entity_meta: dict) -> str:
    """Determine which coalition an entity belongs to, using extraction metadata and mappings."""
    # For persons: use coalition field from extraction, then party→coalition, then figure mapping
    if entity_type == "PERSON":
        coalition = entity_meta.get("coalition")
        if coalition:
            return coalition
        party = entity_meta.get("party")
        if party:
            mapped = PARTY_TO_COALITION.get(party)
            if mapped:
                return mapped
        return FIGURE_AFFILIATIONS.get(entity_name)

    # For organizations: use coalition field, then subtype-based mapping, then org mapping
    if entity_type == "ORGANIZATION":
        # Check if it's a coalition itself
        subtype = entity_meta.get("subtype", "")
        short_name = entity_meta.get("short_name")
        if subtype == "coalition":
            # The entity IS a coalition — map to itself
            if short_name and short_name in ORG_TO_COALITION:
                return ORG_TO_COALITION[short_name]
            return ORG_TO_COALITION.get(entity_name)
        if subtype == "political_party":
            if short_name and short_name in ORG_TO_COALITION:
                return ORG_TO_COALITION[short_name]
            return ORG_TO_COALITION.get(entity_name)
        # Non-political orgs (government, media, international) → no coalition
        return None

    return None


def determine_party(entity_name: str, entity_type: str, entity_meta: dict) -> str:
    """Determine which party an entity belongs to."""
    if entity_type == "PERSON":
        return entity_meta.get("party")

    if entity_type == "ORGANIZATION":
        subtype = entity_meta.get("subtype", "")
        short_name = entity_meta.get("short_name")
        if subtype == "political_party":
            return short_name or entity_name
        return None

    return None


def analyze_entity_sentiment(analyzer, entity_file_data: dict, entity_name: str) -> tuple:
    """
    Analyze sentiment for an entity using its context snippets.
    Returns (mean_compound, std_compound, mention_count, has_context).
    """
    contexts = entity_file_data.get("contexts", [])

    if contexts:
        context_scores = []
        for ctx in contexts:
            snippet = clean_markdown_links(ctx.get("snippet", ""))
            if snippet and len(snippet) > 5:
                vs = analyzer.polarity_scores(snippet)
                context_scores.append(vs["compound"])

        if context_scores:
            mean_compound = statistics.mean(context_scores)
            std_compound = statistics.stdev(context_scores) if len(context_scores) > 1 else 0.0
            return mean_compound, std_compound, len(context_scores), True

    # Fallback: analyze entity name itself (typically neutral)
    vs = analyzer.polarity_scores(entity_name)
    mean_compound = vs["compound"] * 0.3  # Dampen for fallback
    return mean_compound, 0.0, 0, False


def calculate_zscore(value: float, mean: float, std: float) -> float:
    """Calculate z-score for anomaly detection."""
    if std == 0:
        return 0.0
    return (value - mean) / std


def main():
    print("=" * 70)
    print("SENTIMENT ANALYSIS — Entity Extraction Cycle")
    print(f"Collection: {COLLECTION_TIMESTAMP}")
    print(f"Extraction ID: {EXTRACTION_ID}")
    print("=" * 70)

    # Initialize VADER
    analyzer = SentimentIntensityAnalyzer()

    # Load entity extraction data
    print("\n[1] Loading entity extraction data...")
    extraction_data = load_extraction_data()
    source_count = extraction_data.get("source_count", 0)
    sources_processed = extraction_data.get("sources_processed", [])

    total_entities = 0
    entity_lists = {}
    for entity_type, key in ENTITY_TYPE_KEYS.items():
        entity_list = extraction_data.get(key, [])
        entity_lists[entity_type] = entity_list
        total_entities += len(entity_list)
        print(f"  {entity_type}: {len(entity_list)}")

    print(f"  Total entities: {total_entities}")
    print(f"  Sources processed: {source_count}")

    # Analyze sentiment for each entity
    print(f"\n[2] Analyzing sentiment for {total_entities} entities...")
    entity_sentiments = {}
    all_scores = []
    all_raw_compounds = []

    for entity_type, entity_list in entity_lists.items():
        entity_sentiments[entity_type] = {}
        for entity_meta in entity_list:
            entity_id = entity_meta.get("entity_id", "")
            entity_name = entity_meta.get("name", entity_id)
            mention_count_meta = entity_meta.get("mentions", 0)

            # Load per-entity file for contexts
            entity_file_data = load_entity_file(entity_id, entity_type)

            # Analyze sentiment
            mean_compound, std_compound, context_count, has_context = analyze_entity_sentiment(
                analyzer, entity_file_data, entity_name
            )

            sentiment_score = scale_vader_to_score(mean_compound)
            coalition = determine_coalition(entity_name, entity_type, entity_meta)
            party = determine_party(entity_name, entity_type, entity_meta)

            entity_sentiments[entity_type][entity_name] = {
                "entity_id": entity_id,
                "sentiment_score": sentiment_score,
                "sentiment_label": SENTIMENT_LABELS.get(sentiment_score, "Unknown"),
                "raw_compound": round(mean_compound, 4),
                "raw_std": round(std_compound, 4),
                "mention_count": context_count if context_count > 0 else mention_count_meta,
                "context_count": context_count,
                "has_context": has_context,
                "coalition": coalition,
                "party": party,
                "subtype": entity_meta.get("subtype", ""),
                "pir_relevance": entity_meta.get("pir_relevance", []),
            }
            all_scores.append(sentiment_score)
            all_raw_compounds.append(mean_compound)

            ctx_status = f"({context_count} contexts)" if has_context else "(no context - fallback)"
            print(f"  {entity_type}: {entity_name} → {sentiment_score:+d} [{SENTIMENT_LABELS.get(sentiment_score, '')}] {ctx_status}")

    # Calculate overall statistics
    print("\n[3] Calculating overall statistics...")
    overall_mean = statistics.mean(all_scores) if all_scores else 0
    overall_std = statistics.stdev(all_scores) if len(all_scores) > 1 else 0
    overall_median = statistics.median(all_scores) if all_scores else 0
    raw_mean = statistics.mean(all_raw_compounds) if all_raw_compounds else 0
    raw_std = statistics.stdev(all_raw_compounds) if len(all_raw_compounds) > 1 else 0

    print(f"  Mean sentiment: {overall_mean:.3f}")
    print(f"  Std deviation: {overall_std:.3f}")
    print(f"  Median sentiment: {overall_median:.3f}")
    print(f"  Raw mean: {raw_mean:.4f}")
    print(f"  Raw std: {raw_std:.4f}")
    print(f"  Range: [{min(all_scores)}, {max(all_scores)}]")

    # Calculate z-scores and detect anomalies
    print("\n[4] Detecting sentiment anomalies (|z-score| > 2)...")
    anomalies = []
    for entity_type, entities_dict in entity_sentiments.items():
        for entity_name, data in entities_dict.items():
            z_score = calculate_zscore(data["raw_compound"], raw_mean, raw_std)
            data["z_score"] = round(z_score, 4)
            data["is_anomaly"] = abs(z_score) > 2

            if abs(z_score) > 2:
                anomalies.append({
                    "entity": entity_name,
                    "entity_id": data["entity_id"],
                    "entity_type": entity_type,
                    "sentiment_score": data["sentiment_score"],
                    "sentiment_label": data["sentiment_label"],
                    "raw_compound": data["raw_compound"],
                    "z_score": round(z_score, 4),
                    "direction": "positive" if z_score > 0 else "negative",
                    "coalition": data["coalition"],
                    "party": data["party"],
                    "mention_count": data["mention_count"],
                })

    anomalies.sort(key=lambda x: abs(x["z_score"]), reverse=True)
    print(f"  Anomalies detected: {len(anomalies)}")
    for a in anomalies:
        print(f"    ⚠️  {a['entity']} ({a['entity_type']}): score={a['sentiment_score']:+d}, z={a['z_score']:.4f} ({a['direction']})")

    # Aggregate by coalition
    print("\n[5] Aggregating sentiment by coalition...")
    coalition_scores = defaultdict(list)
    coalition_entities_map = defaultdict(list)

    for entity_type, entities_dict in entity_sentiments.items():
        for entity_name, data in entities_dict.items():
            coalition = data.get("coalition")
            if coalition:
                coalition_scores[coalition].append(data["raw_compound"])
                coalition_entities_map[coalition].append(entity_name)

    coalition_aggregates = {}
    for coalition, scores in sorted(coalition_scores.items()):
        agg_score = statistics.mean(scores)
        sentiment_score = scale_vader_to_score(agg_score)
        agg = {
            "mean_score": round(agg_score, 4),
            "sentiment_score": sentiment_score,
            "sentiment_label": SENTIMENT_LABELS.get(sentiment_score, "Unknown"),
            "median_score": round(statistics.median(scores), 4),
            "std_dev": round(statistics.stdev(scores), 4) if len(scores) > 1 else 0.0,
            "min_score": min(scores),
            "max_score": max(scores),
            "entity_count": len(scores),
            "entities": coalition_entities_map[coalition],
        }
        coalition_aggregates[coalition] = agg
        print(f"  {coalition}: score={agg['sentiment_score']:+d} ({agg['sentiment_label']}), "
              f"mean={agg['mean_score']:.4f}, entities={agg['entity_count']}")

    # Aggregate by party
    print("\n[6] Aggregating sentiment by party...")
    party_scores = defaultdict(list)
    party_entities_map = defaultdict(list)

    for entity_type, entities_dict in entity_sentiments.items():
        for entity_name, data in entities_dict.items():
            party = data.get("party")
            if party:
                party_scores[party].append(data["raw_compound"])
                party_entities_map[party].append(entity_name)

    party_aggregates = {}
    for party, scores in sorted(party_scores.items()):
        agg_score = statistics.mean(scores)
        sentiment_score = scale_vader_to_score(agg_score)
        agg = {
            "mean_score": round(agg_score, 4),
            "sentiment_score": sentiment_score,
            "sentiment_label": SENTIMENT_LABELS.get(sentiment_score, "Unknown"),
            "median_score": round(statistics.median(scores), 4),
            "std_dev": round(statistics.stdev(scores), 4) if len(scores) > 1 else 0.0,
            "min_score": min(scores),
            "max_score": max(scores),
            "entity_count": len(scores),
            "entities": party_entities_map[party],
        }
        party_aggregates[party] = agg
        print(f"  {party}: score={agg['sentiment_score']:+d} ({agg['sentiment_label']}), "
              f"mean={agg['mean_score']:.4f}, entities={agg['entity_count']}")

    # Generate timestamp
    report_timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    # Build summary
    positive_count = sum(1 for s in all_scores if s > 0)
    neutral_count = sum(1 for s in all_scores if s == 0)
    negative_count = sum(1 for s in all_scores if s < 0)
    entities_with_context = sum(1 for et in entity_sentiments.values() for d in et.values() if d["has_context"])

    summary = {
        "total_entities_analyzed": total_entities,
        "entities_by_type": {k: len(v) for k, v in entity_lists.items()},
        "sources_processed": source_count,
        "sources_listed": sources_processed,
        "entities_with_context": entities_with_context,
        "entities_without_context": total_entities - entities_with_context,
        "overall_mean_sentiment": round(overall_mean, 3),
        "overall_std_dev": round(overall_std, 3),
        "overall_median_sentiment": round(overall_median, 3),
        "overall_raw_mean": round(raw_mean, 4),
        "overall_raw_std": round(raw_std, 4),
        "sentiment_range": [min(all_scores) if all_scores else 0, max(all_scores) if all_scores else 0],
        "positive_entities": positive_count,
        "neutral_entities": neutral_count,
        "negative_entities": negative_count,
        "anomalies_detected": len(anomalies),
        "coalitions_analyzed": list(coalition_aggregates.keys()),
        "parties_analyzed": list(party_aggregates.keys()),
    }

    # Build full report
    report = {
        "report_timestamp": report_timestamp,
        "extraction_id": EXTRACTION_ID,
        "extraction_source": EXTRACTION_TIMESTAMP,
        "collection_cycle": COLLECTION_TIMESTAMP,
        "source_count": source_count,
        "analysis_method": "VADER Sentiment Analysis on entity context snippets",
        "score_range": "-3 (very negative) to +3 (very positive)",
        "anomaly_threshold": "|z-score| > 2",
        "summary": summary,
        "entity_sentiments": entity_sentiments,
        "coalition_aggregates": coalition_aggregates,
        "party_aggregates": party_aggregates,
        "anomalies": anomalies,
    }

    # Save JSON report
    json_filename = f"sentiment_report_{report_timestamp}.json"
    json_path = os.path.join(OUTPUT_DIR, json_filename)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\n[7] JSON report saved: {json_path}")

    # Generate and save Markdown report
    md_report = generate_markdown_report(report)
    md_filename = f"sentiment_report_{report_timestamp}.md"
    md_path = os.path.join(OUTPUT_DIR, md_filename)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_report)
    print(f"[8] Markdown report saved: {md_path}")

    # Update latest symlinks
    latest_json = os.path.join(OUTPUT_DIR, "sentiment_latest.json")
    latest_md = os.path.join(OUTPUT_DIR, "sentiment_latest.md")
    with open(latest_json, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    with open(latest_md, "w", encoding="utf-8") as f:
        f.write(md_report)
    print(f"[9] Latest symlinks updated")

    print("\n" + "=" * 70)
    print("SENTIMENT ANALYSIS COMPLETE")
    print("=" * 70)
    print(f"\nSummary:")
    print(f"  Total entities: {total_entities}")
    print(f"  Entities with context: {entities_with_context}")
    print(f"  Overall mean sentiment: {overall_mean:.3f}")
    print(f"  Anomalies: {len(anomalies)}")
    print(f"  Coalitions: {list(coalition_aggregates.keys())}")
    print(f"  Parties: {list(party_aggregates.keys())}")

    return report


def generate_markdown_report(report: dict) -> str:
    """Generate a comprehensive Markdown sentiment report."""

    s = report["summary"]

    md = f"""# Sentiment Analysis Report

**Classification:** TLP:AMBER
**Report Timestamp:** {report['report_timestamp']}
**Extraction ID:** {report['extraction_id']}
**Extraction Source:** {report['extraction_source']}
**Collection Cycle:** {report['collection_cycle']}
**Source Count:** {report['source_count']}
**Analysis Method:** {report['analysis_method']}
**Score Range:** {report['score_range']}
**Anomaly Threshold:** {report['anomaly_threshold']}

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Entities Analyzed | {s['total_entities_analyzed']} |
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

    for coalition, agg in sorted(report["coalition_aggregates"].items(), key=lambda x: x[1]["mean_score"], reverse=True):
        md += f"\n| {coalition} | {agg['sentiment_score']:+d} | {agg['sentiment_label']} | {agg['mean_score']:.4f} | {agg['std_dev']:.4f} | {agg['entity_count']} | [{agg['min_score']:.3f}, {agg['max_score']:.3f}] |"

    md += "\n\n### Coalition Entities\n"
    for coalition, agg in sorted(report["coalition_aggregates"].items(), key=lambda x: x[1]["mean_score"], reverse=True):
        md += f"- **{coalition}** ({agg['sentiment_score']:+d}, {agg['sentiment_label']}): {', '.join(agg['entities'])}\n"

    # Party aggregates
    md += "\n---\n\n## Party Aggregate Sentiment\n\n"
    md += "| Party | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range | Coalition |\n"
    md += "|-------|:-:|------|:----------:|:-------:|:--------:|:-----:|:---------:|"

    # Build party→coalition lookup
    party_to_coalition = {
        "PKR": "PH", "DAP": "PH", "AMANAH": "PH", "MUDA": "PH",
        "UMNO": "BN", "MCA": "BN", "MIC": "BN",
        "BERSATU": "PN", "PAS": "PN",
        "Warisan": "WARISAN", "Parti Warisan": "WARISAN",
        "BERSAMA": "BERSAMA", "Parti Bersama": "BERSAMA",
        "Pejuang": "PEJUANG",
        "GPS": "GPS", "GRS": "GRS",
    }

    for party, agg in sorted(report["party_aggregates"].items(), key=lambda x: x[1]["mean_score"], reverse=True):
        coalition = party_to_coalition.get(party, "—")
        md += f"\n| {party} | {agg['sentiment_score']:+d} | {agg['sentiment_label']} | {agg['mean_score']:.4f} | {agg['std_dev']:.4f} | {agg['entity_count']} | [{agg['min_score']:.3f}, {agg['max_score']:.3f}] | {coalition} |"

    md += "\n\n### Party Entities\n"
    for party, agg in sorted(report["party_aggregates"].items(), key=lambda x: x[1]["mean_score"], reverse=True):
        coalition = party_to_coalition.get(party, "—")
        md += f"- **{party}** ({agg['sentiment_score']:+d}, {agg['sentiment_label']}, → {coalition}): {', '.join(agg['entities'])}\n"

    # Anomalies
    md += "\n---\n\n## Sentiment Anomalies (|z-score| > 2)\n\n"

    if report["anomalies"]:
        md += f"**{len(report['anomalies'])} anomalies detected.**\n\n"
        md += "| # | Entity | Type | Score | Label | Z-Score | Direction | Coalition | Party | Mentions |\n"
        md += "|---|--------|------|:-----:|-------|:-------:|:---------:|-----------|:------:|:--------:|\n"
        for i, a in enumerate(report["anomalies"], 1):
            coalition = a.get("coalition") or "N/A"
            party = a.get("party") or "—"
            md += f"| {i} | {a['entity']} | {a['entity_type']} | {a['sentiment_score']:+d} | {a['sentiment_label']} | {a['z_score']:.4f} | {a['direction']} | {coalition} | {party} | {a['mention_count']} |\n"
    else:
        md += "*No significant anomalies detected (all entity sentiment scores within 2 standard deviations of mean).*\n"

    # Entity sentiments by type
    md += "\n---\n\n## Entity Sentiments by Type\n"

    for entity_type, entities_dict in report["entity_sentiments"].items():
        md += f"\n### {entity_type}\n\n"
        md += "| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Contexts | Mentions | Coalition | Party |\n"
        md += "|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|:--------:|-----------|:-----:|\n"

        sorted_entities = sorted(entities_dict.items(), key=lambda x: x[1]["raw_compound"], reverse=True)
        for entity, data in sorted_entities:
            anomaly_mark = "⚠️" if data["is_anomaly"] else ""
            coalition = data.get("coalition") or "—"
            party = data.get("party") or "—"
            md += f"| {entity} | {data['sentiment_score']:+d} | {data['sentiment_label']} | {data['raw_compound']:.4f} | {data['z_score']:.4f} | {anomaly_mark} | {data['context_count']} | {data['mention_count']} | {coalition} | {party} |\n"

    md += f"""
---

## Methodology

1. **Entity Source:** Loaded from the latest entity extraction cycle ({report['collection_cycle']})
2. **Context Extraction:** Used pre-extracted context snippets stored in per-entity JSON files (entity `contexts` field)
3. **Sentiment Scoring:** Applied VADER (Valence Aware Dictionary and sEntiment Reasoner) to each context snippet
4. **Score Mapping:** VADER compound scores (-1 to +1) mapped to 7-point Likert scale (-3 to +3):
   - +3: Very Positive (compound ≥ 0.6)
   - +2: Positive (compound ≥ 0.3)
   - +1: Slightly Positive (compound ≥ 0.1)
   - 0: Neutral (-0.1 < compound < 0.1)
   - -1: Slightly Negative (compound > -0.3)
   - -2: Negative (compound > -0.6)
   - -3: Very Negative (compound ≤ -0.6)
5. **Anomaly Detection:** Z-score calculated using overall mean and standard deviation of raw compound scores; anomalies flagged when |z-score| > 2
6. **Coalition Aggregation:** Entities mapped to coalitions via extraction metadata (party/coalition fields) and organization/figure affiliation mappings
7. **Party Aggregation:** Entities mapped to political parties via extraction metadata

---

*Report generated by OpenCLaw Sentiment Analysis Pipeline*
*VADER: Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.*
"""

    return md


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Context-Aware Sentiment Analysis for Entity Extraction Cycle
Source: 2026-07-12T062116+08 entities extraction
Method: VADER Sentiment Analysis on source article context around entity mentions
Scale: -3 (very negative) to +3 (very positive)
Anomaly Detection: |z-score| > 2
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
RAW_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/raw/"
OUTPUT_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/sentiment-analysis/"
COLLECTION_TIMESTAMP = "2026-07-12T062116+08"

# ─── Coalition / Party Mapping ───
# Maps organizations and political figures to their coalitions for aggregation
COALITION_MAPPING = {
    # Pakatan Harapan (PH)
    "PH": "PH", "Pakatan Harapan": "PH",
    "DAP": "PH",
    "AMANAH": "PH", "Amanah": "PH",
    "MUDA": "PH",
    # Barisan Nasional (BN)
    "BN": "BN", "Barisan Nasional": "BN",
    "UMNO": "BN",
    "MCA": "BN",
    # Perikatan Nasional (PN)
    "PN": "PN", "Perikatan Nasional": "PN",
    "PAS": "PN",
    "BERSATU": "PN", "Bersatu": "PN",
    # GPS
    "GPS": "GPS",
    # GRS
    "GRS": "GRS",
    # Others
    "BERSAMA": "BERSAMA", "Bersama": "BERSAMA", "Parti Bersama": "BERSAMA",
    "Pejuang": "PEJUANG",
    "WARISAN": "WARISAN", "Warisan": "WARISAN",
}

# Political figures → coalition affiliation
FIGURE_AFFILIATIONS = {
    "Anwar": "PH", "Anwar Ibrahim": "PH", "PM Anwar": "PH",
    "Datuk Seri Anwar Ibrahim": "PH",
    "Nurul Izzah": "PH", "Nurul Izzah Anwar": "PH",
    "Fahmi Fadzil": "PH",
    "Maszlee Malik": "PH",
    "Syed Saddiq": "PH",
    "Mat Sabu": "PH", "Mohamad Sabu": "PH",
    "Amirudin Shari": "PH", "Datuk Seri Amirudin Shari": "PH",
    "Anthony Loke": "PH", "Anthony Loke Siew Fook": "PH",
    "Dzulkefly Ahmad": "PH",
    "Onn Hafiz": "BN", "Onn Hafiz Ghazi": "BN",
    "Onn Abu Bakar": "BN",
    "Ahmad Zahid": "BN", "Ahmad Zahid Hamidi": "BN", "Zahid Hamidi": "BN",
    "Dr Ahmad Zahid Hamidi": "BN",
    "Datuk Zahari Sarip": "BN", "Zahari Sarip": "BN",
    "Asyraf Wajdi Dusuki": "BN", "Datuk Dr Asyraf Wajdi Dusuki": "BN",
    "Isham Ishak": "BN",
    "Ramli Ngah Talib": "BN", "Tun Ramli Ngah Talib": "BN",
    "Ramlan Harun": "BN", "Datuk Seri Ramlan Harun": "BN",
    "Abdul Razak": "BN", "Tun Abdul Razak": "BN",
    "Abang Johari": "GPS",
    "Mahathir Mohamad": "PEJUANG", "Dr Mahathir Mohamad": "PEJUANG",
    "Tun Dr Mahathir Mohamad": "PEJUANG",
    "Muhammad Sanusi Md Nor": "PN", "Sanusi": "PN",
    "Noraziah Mohd Razit": "PN",
    "Mustapha": "INDEPENDENT",
    "Hasnah Jusid": "PH",
    "B Nantha Kumar": "INDEPENDENT",
    "Hakim Danish": "INDEPENDENT",
    "Qistina Nadia Dzulqarnain": "INDEPENDENT",
    "Alyaa Alhadjri": "INDEPENDENT",
    "Bridget Welsh": "INDEPENDENT",
    "Massila Kamalrudin": "INDEPENDENT", "Ts Dr Massila Kamalrudin": "INDEPENDENT",
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
    # Replace [text](url) with just text
    text = re.sub(r'\[([^\]]*)\]\([^\)]*\)', r'\1', text)
    # Remove image markdown ![alt](url)
    text = re.sub(r'!\[[^\]]*\]\([^\)]*\)', '', text)
    # Remove remaining markdown formatting
    text = re.sub(r'\*\*([^*]*)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]*)\*', r'\1', text)
    return text.strip()


def load_entities_file() -> dict:
    """Load the latest entity extraction JSON for this collection."""
    # Look for the specific collection's extraction file
    pattern = os.path.join(ENTITIES_DIR, f"{COLLECTION_TIMESTAMP}_entities_extracted.json")
    if os.path.exists(pattern):
        with open(pattern, 'r', encoding='utf-8') as f:
            return json.load(f)

    # Fallback: find most recent entities file
    json_files = sorted(
        glob.glob(os.path.join(ENTITIES_DIR, "*entities_extracted.json")),
        key=os.path.getmtime,
        reverse=True
    )
    if json_files:
        with open(json_files[0], 'r', encoding='utf-8') as f:
            return json.load(f)

    raise FileNotFoundError("No entity extraction files found")


def load_raw_sources() -> dict:
    """Load all raw source files for this collection timestamp."""
    pattern = os.path.join(RAW_DIR, f"{COLLECTION_TIMESTAMP}_*.json")
    raw_files = glob.glob(pattern)

    # Exclude manifest and collection files
    raw_files = [f for f in raw_files if "manifest" not in os.path.basename(f)
                 and "collection" not in os.path.basename(f)
                 and "INTELLIGENCE" not in os.path.basename(f)]

    sources = {}
    for filepath in raw_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            source_name = data.get('source', os.path.basename(filepath))
            sources[source_name] = data
        except (json.JSONDecodeError, IOError) as e:
            print(f"  Warning: Could not load {filepath}: {e}")

    return sources


def extract_article_text(article: dict) -> str:
    """Extract clean text content from a raw source article."""
    parts = []

    # Political headlines (highest signal)
    political_headlines = article.get('political_headlines', [])
    for h in political_headlines:
        clean = clean_markdown_links(h)
        if clean and len(clean) > 10:
            parts.append(clean)

    # All headlines
    headlines = article.get('headlines', [])
    for h in headlines:
        clean = clean_markdown_links(h)
        if clean and len(clean) > 10 and clean not in parts:
            parts.append(clean)

    # Full content
    full_content = article.get('full_content', '')
    if full_content:
        # Clean markdown from full content
        clean_content = clean_markdown_links(full_content)
        parts.append(clean_content)

    return " ".join(parts)


def find_entity_context(entity: str, source_texts: dict) -> list:
    """Find context snippets around entity mentions in source articles."""
    contexts = []
    entity_lower = entity.lower()

    for source_name, text in source_texts.items():
        # Split into sentences
        sentences = re.split(r'(?<=[.!?])\s+', text)
        for sentence in sentences:
            sentence_stripped = sentence.strip()
            if entity_lower in sentence_stripped.lower() and len(sentence_stripped) > 15:
                contexts.append({
                    'source': source_name,
                    'snippet': sentence_stripped[:300],
                })
            if len(contexts) >= 10:
                break
        if len(contexts) >= 10:
            break

    return contexts


def get_coalition(entity: str, entity_type: str) -> str:
    """Determine which coalition an entity belongs to."""
    if entity_type == "ORGANIZATION":
        return COALITION_MAPPING.get(entity, None)
    elif entity_type == "PERSON":
        return FIGURE_AFFILIATIONS.get(entity, None)
    return None


def calculate_zscore(value: float, mean: float, std: float) -> float:
    """Calculate z-score for anomaly detection."""
    if std == 0:
        return 0.0
    return (value - mean) / std


def main():
    print("=" * 70)
    print("SENTIMENT ANALYSIS — Entity Extraction Cycle")
    print(f"Collection: {COLLECTION_TIMESTAMP}")
    print("=" * 70)

    # Initialize VADER
    analyzer = SentimentIntensityAnalyzer()

    # Load entity extraction data
    print("\n[1] Loading entity extraction data...")
    entity_data = load_entities_file()
    entities = entity_data.get('entities', {})
    extraction_timestamp = entity_data.get('extraction_timestamp', 'unknown')
    source_collection = entity_data.get('source_collection', 'unknown')

    total_entities = sum(len(v) for v in entities.values())
    print(f"  Source: {entity_data.get('source_timestamp', 'unknown')}")
    print(f"  Extraction timestamp: {extraction_timestamp}")
    print(f"  Total entities: {total_entities}")
    for etype, elist in entities.items():
        print(f"    {etype}: {len(elist)}")

    # Load raw source articles
    print(f"\n[2] Loading raw source articles for {COLLECTION_TIMESTAMP}...")
    raw_sources = load_raw_sources()
    print(f"  Loaded {len(raw_sources)} source articles")

    # Build source text corpus
    print("\n[3] Building source text corpus...")
    source_texts = {}
    for source_name, article in raw_sources.items():
        if article.get('status') == 'success':
            text = extract_article_text(article)
            if text:
                source_texts[source_name] = text
    print(f"  {len(source_texts)} sources with text content")

    # Analyze sentiment for each entity
    print(f"\n[4] Analyzing sentiment for {total_entities} entities...")
    entity_sentiments = {}
    all_scores = []
    all_raw_compounds = []

    for entity_type, entity_list in entities.items():
        entity_sentiments[entity_type] = {}
        for entity in entity_list:
            # Find context snippets for this entity
            contexts = find_entity_context(entity, source_texts)

            if contexts:
                # Analyze sentiment of each context snippet
                context_scores = []
                for ctx in contexts:
                    vs = analyzer.polarity_scores(ctx['snippet'])
                    context_scores.append(vs['compound'])

                mean_compound = statistics.mean(context_scores)
                if len(context_scores) > 1:
                    std_compound = statistics.stdev(context_scores)
                else:
                    std_compound = 0.0

                sentiment_score = scale_vader_to_score(mean_compound)
                mention_count = len(context_scores)
            else:
                # Fallback: no context found — analyze entity name itself (typically neutral)
                vs = analyzer.polarity_scores(entity)
                mean_compound = vs['compound'] * 0.3  # Dampen for fallback
                std_compound = 0.0
                sentiment_score = scale_vader_to_score(mean_compound)
                mention_count = 0

            entity_sentiments[entity_type][entity] = {
                'sentiment_score': sentiment_score,
                'sentiment_label': SENTIMENT_LABELS.get(sentiment_score, "Unknown"),
                'raw_compound': round(mean_compound, 4),
                'raw_std': round(std_compound, 4),
                'mention_count': mention_count,
                'coalition': get_coalition(entity, entity_type),
                'has_context': mention_count > 0,
            }
            all_scores.append(sentiment_score)
            all_raw_compounds.append(mean_compound)

            ctx_status = f"({mention_count} mentions)" if mention_count > 0 else "(no context - fallback)"
            print(f"  {entity_type}: {entity} → {sentiment_score:+d} [{SENTIMENT_LABELS.get(sentiment_score, '')}] {ctx_status}")

    # Calculate overall statistics
    print("\n[5] Calculating overall statistics...")
    overall_mean = statistics.mean(all_scores) if all_scores else 0
    overall_std = statistics.stdev(all_scores) if len(all_scores) > 1 else 0
    overall_median = statistics.median(all_scores) if all_scores else 0

    print(f"  Mean sentiment: {overall_mean:.3f}")
    print(f"  Std deviation: {overall_std:.3f}")
    print(f"  Median sentiment: {overall_median:.3f}")
    print(f"  Range: [{min(all_scores)}, {max(all_scores)}]")

    # Calculate z-scores and detect anomalies
    print("\n[6] Detecting sentiment anomalies (|z-score| > 2)...")
    anomalies = []
    for entity_type, entities_dict in entity_sentiments.items():
        for entity, data in entities_dict.items():
            z_score = calculate_zscore(data['raw_compound'],
                                       statistics.mean(all_raw_compounds),
                                       statistics.stdev(all_raw_compounds) if len(all_raw_compounds) > 1 else 0)
            data['z_score'] = round(z_score, 4)
            data['is_anomaly'] = abs(z_score) > 2

            if abs(z_score) > 2:
                anomalies.append({
                    'entity': entity,
                    'entity_type': entity_type,
                    'sentiment_score': data['sentiment_score'],
                    'sentiment_label': data['sentiment_label'],
                    'raw_compound': data['raw_compound'],
                    'z_score': round(z_score, 4),
                    'direction': 'positive' if z_score > 0 else 'negative',
                    'coalition': data['coalition'],
                    'mention_count': data['mention_count'],
                })

    anomalies.sort(key=lambda x: abs(x['z_score']), reverse=True)
    print(f"  Anomalies detected: {len(anomalies)}")
    for a in anomalies:
        print(f"    ⚠️  {a['entity']} ({a['entity_type']}): score={a['sentiment_score']:+d}, z={a['z_score']:.4f} ({a['direction']})")

    # Aggregate by coalition
    print("\n[7] Aggregating sentiment by coalition/party...")
    coalition_scores = defaultdict(list)
    coalition_entities_map = defaultdict(list)

    for entity_type, entities_dict in entity_sentiments.items():
        for entity, data in entities_dict.items():
            coalition = data.get('coalition')
            if coalition:
                coalition_scores[coalition].append(data['raw_compound'])
                coalition_entities_map[coalition].append(entity)

    coalition_aggregates = {}
    for coalition, scores in sorted(coalition_scores.items()):
        agg = {
            'mean_score': round(statistics.mean(scores), 4),
            'sentiment_score': scale_vader_to_score(statistics.mean(scores)),
            'sentiment_label': SENTIMENT_LABELS.get(scale_vader_to_score(statistics.mean(scores)), "Unknown"),
            'median_score': round(statistics.median(scores), 4),
            'std_dev': round(statistics.stdev(scores), 4) if len(scores) > 1 else 0.0,
            'min_score': min(scores),
            'max_score': max(scores),
            'entity_count': len(scores),
            'entities': coalition_entities_map[coalition],
        }
        coalition_aggregates[coalition] = agg
        print(f"  {coalition}: score={agg['sentiment_score']:+d} ({agg['sentiment_label']}), "
              f"mean={agg['mean_score']:.4f}, entities={agg['entity_count']}")

    # Generate timestamp
    report_timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    # Build summary
    positive_count = sum(1 for s in all_scores if s > 0)
    neutral_count = sum(1 for s in all_scores if s == 0)
    negative_count = sum(1 for s in all_scores if s < 0)
    entities_with_context = sum(1 for et in entity_sentiments.values() for d in et.values() if d['has_context'])

    summary = {
        'total_entities_analyzed': total_entities,
        'entities_by_type': {k: len(v) for k, v in entities.items()},
        'sources_processed': len(raw_sources),
        'sources_with_content': len(source_texts),
        'entities_with_context': entities_with_context,
        'entities_without_context': total_entities - entities_with_context,
        'overall_mean_sentiment': round(overall_mean, 3),
        'overall_std_dev': round(overall_std, 3),
        'overall_median_sentiment': round(overall_median, 3),
        'sentiment_range': [min(all_scores) if all_scores else 0, max(all_scores) if all_scores else 0],
        'positive_entities': positive_count,
        'neutral_entities': neutral_count,
        'negative_entities': negative_count,
        'anomalies_detected': len(anomalies),
        'coalitions_analyzed': list(coalition_aggregates.keys()),
    }

    # Build full report
    report = {
        'report_timestamp': report_timestamp,
        'extraction_source': extraction_timestamp,
        'source_collection': source_collection,
        'source_timestamp': entity_data.get('source_timestamp', 'unknown'),
        'analysis_method': 'VADER Sentiment Analysis on source article context',
        'score_range': '-3 (very negative) to +3 (very positive)',
        'anomaly_threshold': '|z-score| > 2',
        'summary': summary,
        'entity_sentiments': entity_sentiments,
        'coalition_aggregates': coalition_aggregates,
        'anomalies': anomalies,
    }

    # Save JSON report
    json_filename = f"sentiment_report_{report_timestamp}.json"
    json_path = os.path.join(OUTPUT_DIR, json_filename)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\n[8] JSON report saved: {json_path}")

    # Generate and save Markdown report
    md_report = generate_markdown_report(report)
    md_filename = f"sentiment_report_{report_timestamp}.md"
    md_path = os.path.join(OUTPUT_DIR, md_filename)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_report)
    print(f"[9] Markdown report saved: {md_path}")

    # Update latest symlinks
    latest_json = os.path.join(OUTPUT_DIR, "sentiment_latest.json")
    latest_md = os.path.join(OUTPUT_DIR, "sentiment_latest.md")
    with open(latest_json, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    with open(latest_md, 'w', encoding='utf-8') as f:
        f.write(md_report)
    print(f"[10] Latest symlinks updated")

    print("\n" + "=" * 70)
    print("SENTIMENT ANALYSIS COMPLETE")
    print("=" * 70)
    print(f"\nSummary:")
    print(f"  Total entities: {total_entities}")
    print(f"  Entities with context: {entities_with_context}")
    print(f"  Overall mean sentiment: {overall_mean:.3f}")
    print(f"  Anomalies: {len(anomalies)}")
    print(f"  Coalitions: {list(coalition_aggregates.keys())}")

    return report


def generate_markdown_report(report: dict) -> str:
    """Generate a comprehensive Markdown sentiment report."""

    s = report['summary']

    md = f"""# Sentiment Analysis Report

**Classification:** TLP:AMBER
**Report Timestamp:** {report['report_timestamp']}
**Extraction Source:** {report['extraction_source']}
**Source Collection:** {report['source_collection']}
**Source Timestamp:** {report['source_timestamp']}
**Analysis Method:** {report['analysis_method']}
**Score Range:** {report['score_range']}
**Anomaly Threshold:** {report['anomaly_threshold']}

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Entities Analyzed | {s['total_entities_analyzed']} |
| Sources Processed | {s['sources_processed']} |
| Sources with Content | {s['sources_with_content']} |
| Entities with Context | {s['entities_with_context']} |
| Entities without Context (fallback) | {s['entities_without_context']} |
| Overall Mean Sentiment | {s['overall_mean_sentiment']:+.3f} |
| Overall Std Deviation | {s['overall_std_dev']:.3f} |
| Overall Median Sentiment | {s['overall_median_sentiment']:+.3f} |
| Sentiment Range | [{s['sentiment_range'][0]:+d}, {s['sentiment_range'][1]:+d}] |
| Positive Entities | {s['positive_entities']} |
| Neutral Entities | {s['neutral_entities']} |
| Negative Entities | {s['negative_entities']} |
| Anomalies Detected | {s['anomalies_detected']} |

### Sentiment Distribution

```
Positive ({s['positive_entities']})  {"█" * s['positive_entities']}
Neutral  ({s['neutral_entities']})  {"█" * s['neutral_entities']}
Negative ({s['negative_entities']})  {"█" * s['negative_entities']}
```

---

## Coalition / Party Aggregate Sentiment

| Coalition | Sentiment Score | Label | Mean (raw) | Std Dev | Entities | Range |
|-----------|:-:|------|:----------:|:-------:|:--------:|:-----:|"""

    for coalition, agg in sorted(report['coalition_aggregates'].items(), key=lambda x: x[1]['mean_score'], reverse=True):
        md += f"\n| {coalition} | {agg['sentiment_score']:+d} | {agg['sentiment_label']} | {agg['mean_score']:.4f} | {agg['std_dev']:.4f} | {agg['entity_count']} | [{agg['min_score']:.3f}, {agg['max_score']:.3f}] |"

    md += f"\n\n### Coalition Entities\n"
    for coalition, agg in sorted(report['coalition_aggregates'].items(), key=lambda x: x[1]['mean_score'], reverse=True):
        md += f"- **{coalition}** ({agg['sentiment_score']:+d}, {agg['sentiment_label']}): {', '.join(agg['entities'])}\n"

    md += "\n---\n\n## Sentiment Anomalies (|z-score| > 2)\n\n"

    if report['anomalies']:
        md += f"**{len(report['anomalies'])} anomalies detected.**\n\n"
        md += "| # | Entity | Type | Score | Label | Z-Score | Direction | Coalition | Mentions |\n"
        md += "|---|--------|------|:-----:|-------|:-------:|:---------:|-----------|:--------:|\n"
        for i, a in enumerate(report['anomalies'], 1):
            coalition = a.get('coalition') or 'N/A'
            md += f"| {i} | {a['entity']} | {a['entity_type']} | {a['sentiment_score']:+d} | {a['sentiment_label']} | {a['z_score']:.4f} | {a['direction']} | {coalition} | {a['mention_count']} |\n"
    else:
        md += "*No significant anomalies detected (all entity sentiment scores within 2 standard deviations of mean).*\n"

    md += "\n---\n\n## Entity Sentiments by Type\n"

    for entity_type, entities_dict in report['entity_sentiments'].items():
        md += f"\n### {entity_type}\n\n"
        md += "| Entity | Score | Label | Raw Compound | Z-Score | Anomaly | Mentions | Coalition |\n"
        md += "|--------|:-----:|-------|:------------:|:-------:|:-------:|:--------:|-----------|\n"

        # Sort by sentiment score descending
        sorted_entities = sorted(entities_dict.items(), key=lambda x: x[1]['raw_compound'], reverse=True)
        for entity, data in sorted_entities:
            anomaly_mark = "⚠️" if data['is_anomaly'] else ""
            coalition = data.get('coalition') or '—'
            md += f"| {entity} | {data['sentiment_score']:+d} | {data['sentiment_label']} | {data['raw_compound']:.4f} | {data['z_score']:.4f} | {anomaly_mark} | {data['mention_count']} | {coalition} |\n"

    md += f"""
---

## Methodology

1. **Entity Source:** Loaded from the latest entity extraction cycle ({report['source_timestamp']})
2. **Context Extraction:** For each entity, searched raw source article texts for sentences containing entity mentions
3. **Sentiment Scoring:** Applied VADER (Valence Aware Dictionary and sEntiment Reasoner) to each context snippet
4. **Score Mapping:** VADER compound scores (-1 to +1) mapped to 7-point Likert scale (-3 to +3):
   - +3: Very Positive (compound ≥ 0.6)
   - +2: Positive (compound ≥ 0.3)
   - +1: Slightly Positive (compound ≥ 0.1)
   - 0: Neutral (-0.1 < compound < 0.1)
   - -1: Slightly Negative (compound > -0.3)
   - -2: Negative (compound > -0.6)
   - -3: Very Negative (compound ≤ -0.6)
5. **Anomaly Detection:** Z-score calculated using overall mean and standard deviation of raw compound scores
6. **Coalition Aggregation:** Entities mapped to coalitions via organization/figure affiliation mappings

---

*Report generated by OpenCLaw Sentiment Analysis Pipeline*
*VADER: Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.*
"""

    return md


if __name__ == "__main__":
    main()

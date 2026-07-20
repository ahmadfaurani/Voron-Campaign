#!/usr/bin/env python3
"""
Sentiment Analysis for Extracted Entities - 2026-07-11 Cycle
Analyzes sentiment of entities from OpenCLaw extraction cycle using VADER.
Generates aggregate sentiment for parties/coalitions and detects anomalies.

Entity source: 2026-07-11T081148+08_entities_extracted.json (160 entities, 25 sources)
Collection:    2026-07-11T081148+08_political_collection_25sources_OPERATIONAL.json
"""

import json
import os
import glob
from datetime import datetime
from collections import defaultdict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import statistics

# Configuration
ENTITIES_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/entities/"
RAW_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/raw/"
OUTPUT_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/sentiment-analysis/"

# Target files for this cycle
ENTITIES_FILE = os.path.join(ENTITIES_DIR, "2026-07-11T081148+08_entities_extracted.json")
COLLECTION_PREFIX = "2026-07-11T081148+08"

# Political party/coalition mappings for aggregation
PARTY_COALITIONS = {
    "PH": ["PH", "Pakatan Harapan", "PKR", "BERSAMA", "AMANAH", "DAP"],
    "BN": ["BN", "Barisan Nasional", "UMNO", "MIC"],
    "PN": ["PN", "Perikatan Nasional", "PAS", "Bersatu"],
    "GPS": ["GPS", "Gabungan Parti Sarawak"],
    "GRS": ["GRS", "Gabungan Rakyat Sabah"],
    "MUDA": ["MUDA"],
    "WARISAN": ["WARISAN"],
    "PEJUANG": ["Pejuang"],
}

# Key political figures and their affiliations
FIGURE_AFFILIATIONS = {
    "Anwar": "PH",
    "Anwar Ibrahim": "PH",
    "Datuk Seri Anwar Ibrahim": "PH",
    "PM Anwar": "PH",
    "Ahmad Zahid": "BN",
    "Zahid Hamidi": "BN",
    "Muhyiddin": "PN",
    "Ismail Sabri": "BN",
    "Najib Razak": "BN",
    "Onn Hafiz": "BN",
    "Nik Nazmi": "PH",
    "Mat Sabu": "PH",
    "Mohamad Sabu": "PH",
    "Mohamad": "PH",
    "Saifuddin Nasution": "PH",
    "Nga": "PH",
    "Abang Johari": "GPS",
    "Samsuri": "PN",
    "Hakim Danish": "PH",
    "Mustapha": "INDEPENDENT",
    "Zainudin": "PH",
}

# Entities that are titles/honorifics (not real sentiment targets)
HONORIFICS = {"Datuk", "Datuk Seri", "Tan Sri", "Tun"}


def load_entities(filepath):
    """Load entities from JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def load_source_articles(collection_prefix):
    """Load all source article JSON files from the collection."""
    articles = {}

    # Find all article files matching the collection prefix
    pattern = os.path.join(RAW_DIR, f"{collection_prefix}_*.json")
    all_files = glob.glob(pattern)

    for filepath in all_files:
        basename = os.path.basename(filepath)
        # Skip manifest, collection summary, and intelligence brief files
        if 'political_collection' in basename or 'manifest' in basename or 'INTELLIGENCE_BRIEF' in basename:
            continue

        try:
            with open(filepath, 'r') as f:
                article = json.load(f)
            # Extract source name from filename
            source_name = basename.replace(f'{collection_prefix}_', '').replace('.json', '')
            articles[source_name] = article
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load {filepath}: {e}")

    return articles


def analyze_entity_sentiment(entity, articles, analyzer):
    """
    Analyze sentiment for an entity by searching through source articles.
    Returns sentiment scores and context.
    """
    entity_scores = []
    contexts = []

    for source_name, article in articles.items():
        # Get article text content - try multiple fields
        text_content = []

        if isinstance(article, dict):
            # Try headlines first (most common in our data)
            headlines = article.get('headlines', [])
            for headline in headlines:
                if not isinstance(headline, str):
                    continue
                # Strip markdown links for cleaner text
                clean_headline = headline.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
                if clean_headline and not clean_headline.startswith('!'):
                    text_content.append(clean_headline)

            # Also try political headlines (filtered subset)
            pol_headlines = article.get('political_headlines', [])
            for headline in pol_headlines:
                if not isinstance(headline, str):
                    continue
                clean_headline = headline.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
                if clean_headline and not clean_headline.startswith('!'):
                    text_content.append(clean_headline)

            # Also try content/text/body fields
            content = article.get('content', article.get('text', article.get('body', '')))
            if content and isinstance(content, str) and len(content) > 0:
                text_content.append(content)

            # Try full_content field (this is where the actual article text lives)
            full_content = article.get('full_content', '')
            if full_content and isinstance(full_content, str) and len(full_content) > 0:
                text_content.append(full_content)

            # Try summary field
            summary = article.get('summary', '')
            if summary and isinstance(summary, str) and len(summary) > 0:
                text_content.append(summary)

        # Search for entity mentions in all text content
        for text in text_content:
            if not text:
                continue

            # Find mentions of the entity in the text
            if entity.lower() in text.lower():
                # Extract sentences containing the entity
                sentences = text.split('.')
                for sentence in sentences:
                    if entity.lower() in sentence.lower() and len(sentence.strip()) > 10:
                        # Get VADER scores for this context
                        scores = analyzer.polarity_scores(sentence)
                        entity_scores.append(scores['compound'])
                        contexts.append({
                            'source': source_name,
                            'snippet': sentence[:200] + '...' if len(sentence) > 200 else sentence,
                            'score': round(scores['compound'], 4)
                        })

    # If no context found in articles, use entity name as fallback
    if not entity_scores:
        scores = analyzer.polarity_scores(entity)
        entity_scores.append(scores['compound'] * 0.5)  # Dampen the score for fallback
        contexts.append({
            'source': 'fallback',
            'snippet': f"No specific context found for '{entity}' in source articles",
            'score': round(scores['compound'], 4)
        })

    return {
        'mean_score': statistics.mean(entity_scores) if entity_scores else 0,
        'std_dev': statistics.stdev(entity_scores) if len(entity_scores) > 1 else 0,
        'min_score': min(entity_scores) if entity_scores else 0,
        'max_score': max(entity_scores) if entity_scores else 0,
        'mention_count': len(entity_scores),
        'contexts': contexts[:5]
    }


def calculate_z_scores(sentiment_data):
    """Calculate z-scores for anomaly detection."""
    scores = [d['mean_score'] for d in sentiment_data.values()]

    if len(scores) < 2:
        return {k: 0 for k in sentiment_data}

    mean = statistics.mean(scores)
    std_dev = statistics.stdev(scores)

    if std_dev == 0:
        return {k: 0 for k in sentiment_data}

    z_scores = {}
    for entity, data in sentiment_data.items():
        z_scores[entity] = (data['mean_score'] - mean) / std_dev

    return z_scores


def aggregate_by_coalition(entity_sentiments):
    """Aggregate sentiment scores by political coalition."""
    coalition_scores = defaultdict(list)
    coalition_entities = defaultdict(list)

    for entity, data in entity_sentiments.items():
        for coalition, members in PARTY_COALITIONS.items():
            if entity in members:
                coalition_scores[coalition].append(data['mean_score'])
                coalition_entities[coalition].append(entity)
                break

    aggregates = {}
    for coalition, scores in coalition_scores.items():
        if scores:
            aggregates[coalition] = {
                'mean_sentiment': statistics.mean(scores),
                'entities_count': len(scores),
                'entities': coalition_entities[coalition]
            }

    return aggregates


def aggregate_figures_by_party(entity_sentiments):
    """Aggregate sentiment for political figures by their party affiliation."""
    party_scores = defaultdict(list)
    figure_data = {}

    for entity, data in entity_sentiments.items():
        if entity in FIGURE_AFFILIATIONS:
            party = FIGURE_AFFILIATIONS[entity]
            party_scores[party].append(data['mean_score'])
            figure_data[entity] = {
                **data,
                'party_affiliation': party
            }

    party_aggregates = {}
    for party, scores in party_scores.items():
        if scores:
            party_figures = [e for e, d in figure_data.items() if FIGURE_AFFILIATIONS.get(e) == party]
            party_aggregates[party] = {
                'mean_sentiment': statistics.mean(scores),
                'figures_count': len(scores),
                'figures': party_figures
            }

    return party_aggregates, figure_data


def scale_to_int(score):
    """Scale VADER score (-1 to 1) to integer (-3 to +3)."""
    scaled = score * 3
    return max(-3, min(3, round(scaled)))


def generate_report(entity_data, entity_sentiments, z_scores, coalition_aggregates,
                    party_aggregates, figure_data, anomalies):
    """Generate comprehensive sentiment analysis report."""

    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

    # Get sources processed count from entity data
    sources_processed = 0
    if 'extraction_summary' in entity_data and 'collection_stats' in entity_data['extraction_summary']:
        sources_processed = entity_data['extraction_summary']['collection_stats'].get('successful', 0)

    report = {
        "report_timestamp": timestamp,
        "extraction_source": entity_data.get('extraction_timestamp', 'unknown'),
        "collection_timestamp": entity_data.get('source_timestamp', 'unknown'),
        "source_collection": entity_data.get('source_collection', 'unknown'),
        "sources_processed": sources_processed,
        "analysis_method": "VADER Sentiment Analysis",
        "score_range": "-3 (very negative) to +3 (very positive)",
        "anomaly_threshold": "z-score > 2 or < -2",
        "entity_sentiments": {},
        "coalition_aggregates": coalition_aggregates,
        "party_figure_aggregates": party_aggregates,
        "political_figure_sentiments": {},
        "anomalies": anomalies,
        "summary": {}
    }

    # Process entity sentiments with scaled scores
    for entity_type, entities in entity_data.get('entities', {}).items():
        report["entity_sentiments"][entity_type] = {}
        for entity in entities:
            if entity in entity_sentiments:
                data = entity_sentiments[entity]
                report["entity_sentiments"][entity_type][entity] = {
                    "sentiment_score": scale_to_int(data['mean_score']),
                    "raw_compound": round(data['mean_score'], 4),
                    "mention_count": data['mention_count'],
                    "z_score": round(z_scores.get(entity, 0), 4),
                    "is_anomaly": abs(z_scores.get(entity, 0)) > 2
                }

    # Add political figure sentiments
    for entity, data in figure_data.items():
        report["political_figure_sentiments"][entity] = {
            "sentiment_score": scale_to_int(data['mean_score']),
            "raw_compound": round(data['mean_score'], 4),
            "mention_count": data['mention_count'],
            "z_score": round(z_scores.get(entity, 0), 4),
            "party_affiliation": data['party_affiliation'],
            "is_anomaly": abs(z_scores.get(entity, 0)) > 2
        }

    # Generate summary statistics
    all_scores = [d['mean_score'] for d in entity_sentiments.values()]
    anomaly_count = len([z for z in z_scores.values() if abs(z) > 2])

    report["summary"] = {
        "total_entities_analyzed": len(entity_sentiments),
        "average_sentiment": round(statistics.mean(all_scores), 4) if all_scores else 0,
        "sentiment_std_dev": round(statistics.stdev(all_scores), 4) if len(all_scores) > 1 else 0,
        "positive_entities": len([s for s in all_scores if s > 0.05]),
        "neutral_entities": len([s for s in all_scores if -0.05 <= s <= 0.05]),
        "negative_entities": len([s for s in all_scores if s < -0.05]),
        "anomalies_detected": anomaly_count,
        "coalitions_analyzed": list(coalition_aggregates.keys()),
    }

    return report


def generate_markdown_summary(report):
    """Generate a markdown summary of the sentiment analysis."""

    md = f"""# Sentiment Analysis Report

**Report Generated:** {report['report_timestamp']}
**Extraction Source:** {report['extraction_source']}
**Collection Timestamp:** {report['collection_timestamp']}
**Source Collection:** {report.get('source_collection', 'N/A')}
**Sources Processed:** {report['sources_processed']}
**Analysis Method:** {report['analysis_method']}
**Score Range:** {report['score_range']}
**Anomaly Threshold:** {report['anomaly_threshold']}

---

## Summary

| Metric | Value |
|--------|-------|
| Total Entities Analyzed | {report['summary']['total_entities_analyzed']} |
| Average Sentiment | {scale_to_int(report['summary']['average_sentiment'])} ({report['summary']['average_sentiment']:.4f}) |
| Sentiment Std Dev | {report['summary']['sentiment_std_dev']:.4f} |
| Positive Entities | {report['summary']['positive_entities']} |
| Neutral Entities | {report['summary']['neutral_entities']} |
| Negative Entities | {report['summary']['negative_entities']} |
| Anomalies Detected | {report['summary']['anomalies_detected']} |

---

## Coalition Sentiment Aggregates

| Coalition | Sentiment (-3 to +3) | Raw Score | Entity Count | Member Entities |
|-----------|----------------------|-----------|--------------|-----------------|
"""

    for coalition, data in sorted(report['coalition_aggregates'].items()):
        score = scale_to_int(data['mean_sentiment'])
        entities_str = ', '.join(data.get('entities', []))
        md += f"| {coalition} | {score} | {data['mean_sentiment']:.4f} | {data['entities_count']} | {entities_str} |\n"

    md += """
---

## Political Party Figure Aggregates

| Party | Sentiment (-3 to +3) | Raw Score | Figures Count | Figures |
|-------|----------------------|-----------|---------------|---------|
"""

    for party, data in sorted(report['party_figure_aggregates'].items()):
        score = scale_to_int(data['mean_sentiment'])
        figures_str = ', '.join(data.get('figures', []))
        md += f"| {party} | {score} | {data['mean_sentiment']:.4f} | {data['figures_count']} | {figures_str} |\n"

    md += """
---

## Sentiment Anomalies (|z-score| > 2)
"""

    if report['anomalies']['details']:
        md += "\n| Entity | Z-Score | Sentiment | Type | Category |\n"
        md += "|--------|---------|-----------|------|----------|\n"
        # Determine entity category
        entity_categories = {}
        for etype, entities in report['entity_sentiments'].items():
            for ent in entities:
                entity_categories[ent] = etype
        for entity, data in report['anomalies']['details'].items():
            category = entity_categories.get(entity, 'UNKNOWN')
            md += f"| {entity} | {data['z_score']:.4f} | {data['sentiment_score']} | {data['type']} | {category} |\n"
    else:
        md += "\n*No significant anomalies detected.*\n"

    md += "\n---\n\n## Entity Sentiments by Type\n\n"

    for entity_type, entities in report['entity_sentiments'].items():
        md += f"### {entity_type}\n\n"
        md += "| Entity | Sentiment | Raw Score | Mentions | Z-Score | Anomaly |\n"
        md += "|--------|-----------|-----------|----------|---------|---------|\n"

        for entity, data in sorted(entities.items(), key=lambda x: x[1]['sentiment_score'], reverse=True):
            anomaly_mark = "⚠️" if data['is_anomaly'] else ""
            md += f"| {entity} | {data['sentiment_score']} | {data['raw_compound']:.4f} | {data['mention_count']} | {data['z_score']:.4f} | {anomaly_mark} |\n"

        md += "\n"

    # Political figure sentiments section
    if report.get('political_figure_sentiments'):
        md += "---\n\n## Political Figure Sentiments (with Party Affiliation)\n\n"
        md += "| Figure | Sentiment | Raw Score | Mentions | Z-Score | Party | Anomaly |\n"
        md += "|--------|-----------|-----------|----------|---------|-------|---------|\n"

        for entity, data in sorted(report['political_figure_sentiments'].items(),
                                     key=lambda x: x[1]['sentiment_score'], reverse=True):
            anomaly_mark = "⚠️" if data['is_anomaly'] else ""
            md += f"| {entity} | {data['sentiment_score']} | {data['raw_compound']:.4f} | {data['mention_count']} | {data['z_score']:.4f} | {data['party_affiliation']} | {anomaly_mark} |\n"

        md += "\n"

    md += """---
*Report generated by OpenCLaw Sentiment Analysis Pipeline*
*Classification: TLP:AMBER*
"""

    return md


def main():
    """Main execution function."""
    print("=" * 60)
    print("SENTIMENT ANALYSIS - Entity Extraction Cycle 2026-07-11")
    print("=" * 60)

    # Initialize VADER analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Load entities
    print(f"\nLoading entities from: {ENTITIES_FILE}")
    entity_data = load_entities(ENTITIES_FILE)

    extraction_ts = entity_data.get('extraction_timestamp', 'unknown')
    source_ts = entity_data.get('source_timestamp', 'unknown')
    total_entities = entity_data.get('extraction_summary', {}).get('total_entities', 0)
    print(f"Extraction timestamp: {extraction_ts}")
    print(f"Source timestamp: {source_ts}")
    print(f"Total entities: {total_entities}")

    # Load source articles for context
    print(f"\nLoading source articles from collection: {COLLECTION_PREFIX}")
    articles = load_source_articles(COLLECTION_PREFIX)
    print(f"Loaded {len(articles)} source articles")

    # Collect all unique entities
    all_entities = []
    for entity_type, entities in entity_data.get('entities', {}).items():
        all_entities.extend([(e, entity_type) for e in entities])

    # Deduplicate while preserving type info (first occurrence wins)
    seen = set()
    unique_entities = []
    for entity, etype in all_entities:
        if entity not in seen:
            seen.add(entity)
            unique_entities.append((entity, etype))

    print(f"\nAnalyzing sentiment for {len(unique_entities)} unique entities...")

    # Analyze sentiment for each entity
    entity_sentiments = {}
    for i, (entity, entity_type) in enumerate(unique_entities):
        sentiment_data = analyze_entity_sentiment(entity, articles, analyzer)
        entity_sentiments[entity] = sentiment_data
        score = scale_to_int(sentiment_data['mean_score'])
        mentions = sentiment_data['mention_count']
        if mentions > 1 or score != 0:
            print(f"  [{i+1}/{len(unique_entities)}] {entity_type}: {entity} -> {score} ({mentions} mentions)")
        else:
            print(f"  [{i+1}/{len(unique_entities)}] {entity_type}: {entity} -> {score}")

    # Calculate z-scores for anomaly detection
    print("\nCalculating z-scores for anomaly detection...")
    z_scores = calculate_z_scores(entity_sentiments)

    # Identify anomalies
    anomalies = {
        "high_positive": [],
        "high_negative": [],
        "details": {}
    }
    for entity, z_score in z_scores.items():
        if abs(z_score) > 2:
            anomalies["details"][entity] = {
                "z_score": round(z_score, 4),
                "sentiment_score": scale_to_int(entity_sentiments[entity]['mean_score']),
                "type": "high_positive" if z_score > 2 else "high_negative"
            }
            if z_score > 2:
                anomalies["high_positive"].append(entity)
            else:
                anomalies["high_negative"].append(entity)

    print(f"\nAnomalies detected: {len(anomalies['details'])}")
    for entity, detail in anomalies['details'].items():
        print(f"  ⚠️  {entity}: z={detail['z_score']:.4f}, sentiment={detail['sentiment_score']}, type={detail['type']}")

    # Aggregate by coalition (organizations)
    print("\nAggregating sentiment by coalition...")
    coalition_aggregates = aggregate_by_coalition(entity_sentiments)
    for coalition, data in sorted(coalition_aggregates.items()):
        print(f"  {coalition}: {scale_to_int(data['mean_sentiment'])} ({data['entities_count']} entities)")

    # Aggregate political figures by party
    print("\nAggregating political figures by party...")
    party_aggregates, figure_data = aggregate_figures_by_party(entity_sentiments)
    for party, data in sorted(party_aggregates.items()):
        print(f"  {party}: {scale_to_int(data['mean_sentiment'])} ({data['figures_count']} figures)")

    # Generate report
    print("\nGenerating comprehensive report...")
    report = generate_report(
        entity_data, entity_sentiments, z_scores,
        coalition_aggregates, party_aggregates, figure_data, anomalies
    )

    # Save report
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    output_file = os.path.join(OUTPUT_DIR, f"sentiment_report_{timestamp}.json")

    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"\nReport saved to: {output_file}")

    # Also generate markdown summary
    md_report = generate_markdown_summary(report)
    md_file = os.path.join(OUTPUT_DIR, f"sentiment_report_{timestamp}.md")

    with open(md_file, 'w') as f:
        f.write(md_report)

    print(f"Markdown summary saved to: {md_file}")

    # Also save as latest
    latest_json = os.path.join(OUTPUT_DIR, "sentiment_latest.json")
    latest_md = os.path.join(OUTPUT_DIR, "sentiment_latest.md")
    with open(latest_json, 'w') as f:
        json.dump(report, f, indent=2)
    with open(latest_md, 'w') as f:
        f.write(md_report)
    print(f"Latest symlink saved to: {latest_json} and {latest_md}")

    print("\n" + "=" * 60)
    print("SENTIMENT ANALYSIS COMPLETE")
    print("=" * 60)

    return report


if __name__ == "__main__":
    main()

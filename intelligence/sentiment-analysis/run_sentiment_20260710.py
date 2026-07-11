#!/usr/bin/env python3
"""
Sentiment Analysis for Extracted Entities - 2026-07-10 Cycle
Analyzes sentiment of entities from OpenCLaw extraction cycle using VADER.
Generates aggregate sentiment for parties/coalitions and detects anomalies.
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

# Political party mappings for aggregation
PARTY_COALITIONS = {
    "PH": ["PH", "Pakatan Harapan", "PKR", "BERSAMA", "AMANAH", "DAP"],
    "BN": ["BN", "Barisan Nasional", "UMNO"],
    "PN": ["PN", "Perikatan Nasional", "PAS", "Bersatu", "Parti Pribumi Bersatu Malaysia"],
    "GPS": ["GPS", "Gabungan Parti Sarawak"],
    "GRS": ["GRS", "Gabungan Rakyat Sabah"],
    "MUDA": ["MUDA"],
    "WARISAN": ["WARISAN"],
}

# Key political figures and their affiliations
FIGURE_AFFILIATIONS = {
    "Anwar Ibrahim": "PH",
    "Anwar": "PH",
    "Muhyiddin Yassin": "PN",
    "Muhyiddin": "PN",
    "Zahid Hamidi": "BN",
    "Ahmad Zahid": "BN",
    "Onn Hafiz": "BN",
    "Onn Hafiz Ghazi": "BN",
    "Nik Nazmi": "PH",
    "Mat Sabu": "PH",
    "Mohamad Sabu": "PH",
    "Dzulkefly Ahmad": "PH",
    "Halimah Ali": "PH",
}


def get_latest_entities_file():
    """Find the most recent entities JSON file."""
    # Look for the specific file from the latest extraction
    latest_file = os.path.join(ENTITIES_DIR, "2026-07-10T002125Z_entities_extracted.json")
    if os.path.exists(latest_file):
        return latest_file
    
    # Fallback to glob search
    json_files = glob.glob(os.path.join(ENTITIES_DIR, "entities_*T*.json"))
    if not json_files:
        json_files = glob.glob(os.path.join(ENTITIES_DIR, "entities_*.json"))
    if not json_files:
        raise FileNotFoundError("No entity files found")
    return max(json_files, key=os.path.getmtime)


def load_entities(filepath):
    """Load entities from JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def load_source_articles(collection_timestamp):
    """Load all source articles from the collection."""
    articles = {}
    
    # Pattern for the collection timestamp
    date_part = "2026-07-10T002125Z"
    
    # Find all article files from this collection
    pattern = os.path.join(RAW_DIR, f"{date_part}*.json")
    article_files = glob.glob(pattern)
    
    for filepath in article_files:
        # Skip the main collection file and manifest
        basename = os.path.basename(filepath)
        if 'political_collection' in basename or 'manifest' in basename or 'INTELLIGENCE_BRIEF' in basename:
            continue
            
        try:
            with open(filepath, 'r') as f:
                article = json.load(f)
                # Extract source name from filename
                source_name = basename.replace(f'{date_part}_', '').replace('.json', '')
                articles[source_name] = article
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load {filepath}: {e}")
    
    return articles


def analyze_entity_sentiment(entity, articles, analyzer):
    """
    Analyze sentiment for an entity by searching through articles.
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
                # Strip markdown links for cleaner text
                clean_headline = headline.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
                if clean_headline and not clean_headline.startswith('!'):  # Skip image links
                    text_content.append(clean_headline)
            
            # Also try content/text/body fields
            content = article.get('content', article.get('text', article.get('body', '')))
            if content:
                text_content.append(content)
            
            # Try summary field
            summary = article.get('summary', '')
            if summary:
                text_content.append(summary)
        
        # Search for entity mentions in all text content
        for text in text_content:
            if not text:
                continue
                
            # Find mentions of the entity in the text
            if entity.lower() in text.lower():
                # Extract sentences or headlines containing the entity
                sentences = text.split('.')
                for sentence in sentences:
                    if entity.lower() in sentence.lower() and len(sentence.strip()) > 10:
                        # Get VADER scores for this context
                        scores = analyzer.polarity_scores(sentence)
                        entity_scores.append(scores['compound'])
                        contexts.append({
                            'source': source_name,
                            'snippet': sentence[:200] + '...' if len(sentence) > 200 else sentence,
                            'score': scores['compound']
                        })
    
    # If no context found in articles, use entity name as fallback with neutral baseline
    if not entity_scores:
        # For entities without context, use a slightly positive default (news entities are typically notable)
        scores = analyzer.polarity_scores(entity)
        entity_scores.append(scores['compound'] * 0.5)  # Dampen the score for fallback
        contexts.append({
            'source': 'fallback',
            'snippet': f"No specific context found for '{entity}' in source articles",
            'score': scores['compound']
        })
    
    return {
        'mean_score': statistics.mean(entity_scores) if entity_scores else 0,
        'std_dev': statistics.stdev(entity_scores) if len(entity_scores) > 1 else 0,
        'min_score': min(entity_scores) if entity_scores else 0,
        'max_score': max(entity_scores) if entity_scores else 0,
        'mention_count': len(entity_scores),
        'contexts': contexts[:5]  # Limit to top 5 contexts
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


def aggregate_by_coalition(entity_sentiments, entity_type='ORGANIZATION'):
    """Aggregate sentiment scores by political coalition."""
    coalition_scores = defaultdict(list)
    
    for entity, data in entity_sentiments.items():
        # Check if entity belongs to any coalition
        for coalition, members in PARTY_COALITIONS.items():
            if entity in members:
                coalition_scores[coalition].append(data['mean_score'])
                break
    
    # Calculate aggregates
    aggregates = {}
    for coalition, scores in coalition_scores.items():
        if scores:
            aggregates[coalition] = {
                'mean_sentiment': statistics.mean(scores),
                'entities_count': len(scores),
                'entities': [e for e in entity_sentiments.keys() 
                           if any(e in members for members in [PARTY_COALITIONS[c] for c in PARTY_COALITIONS.keys() if c == coalition])]
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
    
    # Calculate party aggregates
    party_aggregates = {}
    for party, scores in party_scores.items():
        if scores:
            party_aggregates[party] = {
                'mean_sentiment': statistics.mean(scores),
                'figures_count': len(scores),
                'figures': list([e for e, d in figure_data.items() if FIGURE_AFFILIATIONS.get(e) == party])
            }
    
    return party_aggregates, figure_data


def scale_to_int(score):
    """Scale VADER score (-1 to 1) to integer (-3 to +3)."""
    # VADER compound is -1 to 1, scale to -3 to +3
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
        "sources_processed": sources_processed,
        "analysis_method": "VADER Sentiment Analysis",
        "score_range": "-3 (very negative) to +3 (very positive)",
        "anomaly_threshold": "z-score > 2 or < -2",
        
        "entity_sentiments": {},
        "coalition_aggregates": coalition_aggregates,
        "party_figure_aggregates": party_aggregates,
        "political_figure_sentiments": figure_data,
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
**Sources Processed:** {report['sources_processed']}  
**Analysis Method:** {report['analysis_method']}  
**Score Range:** {report['score_range']}

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

| Coalition | Mean Sentiment | Entity Count |
|-----------|---------------|--------------|
"""
    
    for coalition, data in sorted(report['coalition_aggregates'].items()):
        score = scale_to_int(data['mean_sentiment'])
        md += f"| {coalition} | {score} ({data['mean_sentiment']:.4f}) | {data['entities_count']} |\n"
    
    md += """
---

## Political Party Figure Aggregates

| Party | Mean Sentiment | Figures Count |
|-------|---------------|---------------|
"""
    
    for party, data in sorted(report['party_figure_aggregates'].items()):
        score = scale_to_int(data['mean_sentiment'])
        md += f"| {party} | {score} ({data['mean_sentiment']:.4f}) | {data['figures_count']} |\n"
    
    md += """
---

## Sentiment Anomalies (z-score > 2)

"""
    
    if report['anomalies']['details']:
        md += "| Entity | Z-Score | Sentiment | Type |\n"
        md += "|--------|---------|-----------|------|\n"
        for entity, data in report['anomalies']['details'].items():
            md += f"| {entity} | {data['z_score']:.4f} | {data['sentiment_score']} | {data['type']} |\n"
    else:
        md += "*No significant anomalies detected.*\n"
    
    md += """
---

## Entity Sentiments by Type

"""
    
    for entity_type, entities in report['entity_sentiments'].items():
        md += f"### {entity_type}\n\n"
        md += "| Entity | Sentiment | Raw Score | Mentions | Z-Score | Anomaly |\n"
        md += "|--------|-----------|-----------|----------|---------|---------|\n"
        
        for entity, data in sorted(entities.items(), key=lambda x: x[1]['sentiment_score'], reverse=True):
            anomaly_mark = "⚠️" if data['is_anomaly'] else ""
            md += f"| {entity} | {data['sentiment_score']} | {data['raw_compound']:.4f} | {data['mention_count']} | {data['z_score']:.4f} | {anomaly_mark} |\n"
        
        md += "\n"
    
    md += """
---

*Report generated by OpenCLaw Sentiment Analysis Pipeline*
"""
    
    return md


def main():
    """Main execution function."""
    print("=" * 60)
    print("SENTIMENT ANALYSIS - Entity Extraction Cycle 2026-07-10")
    print("=" * 60)
    
    # Initialize VADER analyzer
    analyzer = SentimentIntensityAnalyzer()
    
    # Load latest entities
    entities_file = get_latest_entities_file()
    print(f"\nLoading entities from: {entities_file}")
    entity_data = load_entities(entities_file)
    
    print(f"Extraction timestamp: {entity_data.get('extraction_timestamp', 'unknown')}")
    print(f"Source timestamp: {entity_data.get('source_timestamp', 'unknown')}")
    
    # Load source articles for context
    collection_ts = entity_data.get('source_timestamp', '')
    print(f"\nLoading source articles from collection: {collection_ts}")
    articles = load_source_articles(collection_ts)
    print(f"Loaded {len(articles)} source articles")
    
    # Collect all unique entities
    all_entities = []
    for entity_type, entities in entity_data.get('entities', {}).items():
        all_entities.extend([(e, entity_type) for e in entities])
    
    print(f"\nAnalyzing sentiment for {len(all_entities)} entities...")
    
    # Analyze sentiment for each entity
    entity_sentiments = {}
    for entity, entity_type in all_entities:
        if entity not in entity_sentiments:  # Avoid duplicates
            sentiment_data = analyze_entity_sentiment(entity, articles, analyzer)
            entity_sentiments[entity] = sentiment_data
            print(f"  {entity_type}: {entity} -> {scale_to_int(sentiment_data['mean_score'])}")
    
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
    
    print(f"Anomalies detected: {len(anomalies['details'])}")
    
    # Aggregate by coalition (organizations)
    print("\nAggregating sentiment by coalition...")
    coalition_aggregates = aggregate_by_coalition(entity_sentiments, 'ORGANIZATION')
    for coalition, data in coalition_aggregates.items():
        print(f"  {coalition}: {scale_to_int(data['mean_sentiment'])} ({data['entities_count']} entities)")
    
    # Aggregate political figures by party
    print("\nAggregating political figures by party...")
    party_aggregates, figure_data = aggregate_figures_by_party(entity_sentiments)
    for party, data in party_aggregates.items():
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
    
    # Update latest symlinks
    latest_json = os.path.join(OUTPUT_DIR, "sentiment_latest.json")
    latest_md = os.path.join(OUTPUT_DIR, "sentiment_latest.md")
    
    # Copy to latest
    with open(output_file, 'r') as src:
        with open(latest_json, 'w') as dst:
            dst.write(src.read())
    
    with open(md_file, 'r') as src:
        with open(latest_md, 'w') as dst:
            dst.write(src.read())
    
    print(f"Latest symlinks updated")
    print("\n" + "=" * 60)
    print("SENTIMENT ANALYSIS COMPLETE")
    print("=" * 60)
    
    return report


if __name__ == "__main__":
    main()

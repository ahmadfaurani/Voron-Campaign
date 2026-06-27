#!/usr/bin/env python3
"""
Sentiment Analysis for Extracted Entities
Analyzes sentiment for all entities from the latest extraction cycle.
Scores range from -3 to +3.
Detects anomalies using z-score > 2.
Calculates aggregate sentiment for parties and coalitions.
"""

import json
import os
import statistics
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Configuration
ENTITIES_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/entities"
OUTPUT_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/sentiment-analysis"

# Political entity mappings for coalition analysis
COALITIONS = {
    "PH": ["Anwar", "Anwar Ibrahim", "Datuk Seri Anwar Ibrahim", "PM Anwar", "Ahmad Zahid", "DPM Ahmad Zahid", 
           "UMNO", "BN", "Bersatu", "PAS"],  # Note: Bersatu and PAS are actually PN, will refine
    "PN": ["Muhyiddin", "Ahmad Samsuri Mokhtar", "Samsuri", "PN", "PAS", "Bersatu"],
    "GPS": ["Onn Hafiz", "Abd Mutalip Abd Rahim", "Mazlan Bujang", "Mustapha", "Pairin", "Tiong"],
}

# Refined coalition mappings based on Malaysian politics
COALITION_MEMBERS = {
    "PH-Pakatan Harapan": ["Anwar", "Anwar Ibrahim", "Datuk Seri Anwar Ibrahim", "PM Anwar"],
    "BN-Barisan Nasional": ["Ahmad Zahid", "DPM Ahmad Zahid", "UMNO", "BN"],
    "PN-Perikatan Nasional": ["Muhyiddin", "Ahmad Samsuri Mokhtar", "Samsuri", "PN", "PAS", "Bersatu"],
    "GPS-Gabungan Parti Sarawak": ["Onn Hafiz", "Abd Mutalip Abd Rahim", "Mazlan Bujang", "Mustapha", "Pairin", "Tiong"],
}

def find_latest_entities_file():
    """Find the most recent entities JSON file with the main entity extraction."""
    files = []
    for f in os.listdir(ENTITIES_DIR):
        # Look for main entities files (not pir_analysis, not report.md)
        if f.endswith('.json') and f.startswith('entities_') and 'pir_analysis' not in f and 'report' not in f.lower():
            filepath = os.path.join(ENTITIES_DIR, f)
            # Verify it has the expected structure
            try:
                with open(filepath, 'r') as test_f:
                    data = json.load(test_f)
                    if 'entities' in data and isinstance(data['entities'], dict):
                        files.append((filepath, os.path.getmtime(filepath)))
            except:
                continue
    
    if not files:
        # Try alternative naming pattern
        for f in os.listdir(ENTITIES_DIR):
            if f.endswith('_entities.json'):
                filepath = os.path.join(ENTITIES_DIR, f)
                try:
                    with open(filepath, 'r') as test_f:
                        data = json.load(test_f)
                        if 'entities' in data:
                            files.append((filepath, os.path.getmtime(filepath)))
                except:
                    continue
    
    if not files:
        raise FileNotFoundError("No entities files found")
    
    files.sort(key=lambda x: x[1], reverse=True)
    return files[0][0]

def load_entities(filepath):
    """Load entities from JSON file."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

def analyze_sentiment(text, analyzer):
    """
    Analyze sentiment of text and return score from -3 to +3.
    VADER returns compound score from -1 to 1, we scale to -3 to +3.
    """
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    # Scale from [-1, 1] to [-3, 3]
    scaled_score = compound * 3
    return {
        'raw_compound': compound,
        'scaled_score': round(scaled_score, 2),
        'positive': scores['pos'],
        'neutral': scores['neu'],
        'negative': scores['neg']
    }

def calculate_zscore(value, mean, stdev):
    """Calculate z-score for anomaly detection."""
    if stdev == 0:
        return 0
    return (value - mean) / stdev

def main():
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    
    # Initialize VADER analyzer
    analyzer = SentimentIntensityAnalyzer()
    
    # Find and load latest entities
    entities_file = find_latest_entities_file()
    print(f"Loading entities from: {entities_file}")
    data = load_entities(entities_file)
    
    entities = data.get('entities', {})
    extraction_timestamp = data.get('extraction_timestamp', 'unknown')
    
    # Analyze sentiment for each entity
    results = {
        'analysis_timestamp': timestamp,
        'extraction_timestamp': extraction_timestamp,
        'source_file': os.path.basename(entities_file),
        'entity_sentiments': {},
        'coalition_aggregates': {},
        'anomalies': [],
        'summary': {}
    }
    
    all_scores = []
    
    for entity_type, entity_list in entities.items():
        results['entity_sentiments'][entity_type] = []
        
        for entity in entity_list:
            sentiment = analyze_sentiment(entity, analyzer)
            entity_result = {
                'name': entity,
                'sentiment_score': sentiment['scaled_score'],
                'compound': sentiment['raw_compound'],
                'positive': sentiment['positive'],
                'neutral': sentiment['neutral'],
                'negative': sentiment['negative']
            }
            results['entity_sentiments'][entity_type].append(entity_result)
            all_scores.append(sentiment['scaled_score'])
    
    # Calculate statistics for anomaly detection
    if all_scores:
        mean_score = statistics.mean(all_scores)
        stdev_score = statistics.stdev(all_scores) if len(all_scores) > 1 else 0
        
        results['summary']['mean_sentiment'] = round(mean_score, 3)
        results['summary']['stdev_sentiment'] = round(stdev_score, 3)
        results['summary']['min_sentiment'] = round(min(all_scores), 3)
        results['summary']['max_sentiment'] = round(max(all_scores), 3)
        results['summary']['total_entities'] = len(all_scores)
        
        # Detect anomalies (z-score > 2)
        for entity_type, entity_list in results['entity_sentiments'].items():
            for entity in entity_list:
                zscore = calculate_zscore(entity['sentiment_score'], mean_score, stdev_score)
                if abs(zscore) > 2:
                    results['anomalies'].append({
                        'entity': entity['name'],
                        'type': entity_type,
                        'sentiment_score': entity['sentiment_score'],
                        'z_score': round(zscore, 3),
                        'anomaly_type': 'positive' if zscore > 0 else 'negative'
                    })
    
    # Calculate coalition aggregates
    for coalition, members in COALITION_MEMBERS.items():
        coalition_scores = []
        coalition_entities = []
        
        for entity_type, entity_list in results['entity_sentiments'].items():
            for entity in entity_list:
                if entity['name'] in members:
                    coalition_scores.append(entity['sentiment_score'])
                    coalition_entities.append(entity['name'])
        
        if coalition_scores:
            avg_score = statistics.mean(coalition_scores)
            results['coalition_aggregates'][coalition] = {
                'average_sentiment': round(avg_score, 3),
                'entity_count': len(coalition_scores),
                'entities': coalition_entities,
                'sentiment_label': get_sentiment_label(avg_score)
            }
    
    # Save results
    output_file = os.path.join(OUTPUT_DIR, f"sentiment_report_{timestamp}.json")
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Also save a markdown summary
    md_output = generate_markdown_report(results)
    md_file = os.path.join(OUTPUT_DIR, f"sentiment_report_{timestamp}.md")
    with open(md_file, 'w') as f:
        f.write(md_output)
    
    print(f"Sentiment analysis complete.")
    print(f"JSON report: {output_file}")
    print(f"Markdown report: {md_file}")
    print(f"Total entities analyzed: {results['summary'].get('total_entities', 0)}")
    print(f"Anomalies detected: {len(results['anomalies'])}")
    
    return results

def get_sentiment_label(score):
    """Convert numeric score to label."""
    if score >= 1.5:
        return "Very Positive"
    elif score >= 0.5:
        return "Positive"
    elif score >= -0.5:
        return "Neutral"
    elif score >= -1.5:
        return "Negative"
    else:
        return "Very Negative"

def generate_markdown_report(results):
    """Generate a human-readable markdown report."""
    md = []
    md.append("# Sentiment Analysis Report")
    md.append("")
    md.append(f"**Analysis Timestamp:** {results['analysis_timestamp']}")
    md.append(f"**Extraction Timestamp:** {results['extraction_timestamp']}")
    md.append(f"**Source File:** {results['source_file']}")
    md.append("")
    
    # Summary
    md.append("## Summary")
    md.append("")
    summary = results.get('summary', {})
    md.append(f"- **Total Entities Analyzed:** {summary.get('total_entities', 'N/A')}")
    md.append(f"- **Mean Sentiment:** {summary.get('mean_sentiment', 'N/A')}")
    md.append(f"- **Std Deviation:** {summary.get('stdev_sentiment', 'N/A')}")
    md.append(f"- **Score Range:** [{summary.get('min_sentiment', 'N/A')}, {summary.get('max_sentiment', 'N/A')}]")
    md.append("")
    
    # Coalition Aggregates
    md.append("## Coalition Sentiment Aggregates")
    md.append("")
    md.append("| Coalition | Avg Sentiment | Label | Entity Count |")
    md.append("|-----------|---------------|-------|--------------|")
    for coalition, data in results.get('coalition_aggregates', {}).items():
        md.append(f"| {coalition} | {data['average_sentiment']} | {data['sentiment_label']} | {data['entity_count']} |")
    md.append("")
    
    # Anomalies
    md.append("## Sentiment Anomalies (|z-score| > 2)")
    md.append("")
    anomalies = results.get('anomalies', [])
    if anomalies:
        md.append("| Entity | Type | Score | Z-Score | Anomaly Type |")
        md.append("|--------|------|-------|---------|--------------|")
        for a in anomalies:
            md.append(f"| {a['entity']} | {a['type']} | {a['sentiment_score']} | {a['z_score']} | {a['anomaly_type']} |")
    else:
        md.append("*No significant anomalies detected.*")
    md.append("")
    
    # Entity Sentiments by Type
    md.append("## Entity Sentiments by Type")
    md.append("")
    for entity_type, entities in results.get('entity_sentiments', {}).items():
        md.append(f"### {entity_type}")
        md.append("")
        md.append("| Entity | Sentiment Score |")
        md.append("|--------|-----------------|")
        # Sort by sentiment score
        sorted_entities = sorted(entities, key=lambda x: x['sentiment_score'], reverse=True)
        for e in sorted_entities:
            label = get_sentiment_label(e['sentiment_score'])
            md.append(f"| {e['name']} | {e['sentiment_score']} ({label}) |")
        md.append("")
    
    return "\n".join(md)

if __name__ == "__main__":
    main()

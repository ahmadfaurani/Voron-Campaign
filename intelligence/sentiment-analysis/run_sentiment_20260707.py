#!/usr/bin/env python3
"""
Sentiment Analysis for Extracted Entities - July 7, 2026
Analyzes sentiment of entities from OpenCLaw workspace extraction cycles.
Uses VADER sentiment analysis with scoring from -3 to +3.
Gathers context from raw source files for meaningful sentiment scores.
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path
from statistics import mean, stdev
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Configuration
ENTITIES_DIR = Path("/home/p62operator/.openclaw/workspace-hoi/intelligence/entities")
RAW_DIR = Path("/home/p62operator/.openclaw/workspace-hoi/intelligence/raw")
OUTPUT_DIR = Path("/home/p62operator/.openclaw/workspace-hoi/intelligence/sentiment-analysis")

# Political party/coalition mappings for Malaysia context
COALITIONS = {
    "PH": ["PH", "PKR", "DAP", "AMANAH", "Amanah"],
    "BN": ["BN", "UMNO", "MCA", "MIC"],
    "PN": ["PN", "PAS", "BERSATU"],
    "BERSAMA": ["BERSAMA"],
    "GPS": ["GPS", "PBB", "SUPP", "PRS", "PDP"],
    "GRS": ["GRS"],
    "MUDA": ["MUDA"],
}

# Known political figures and their affiliations
FIGURE_AFFILIATIONS = {
    "Anwar": "PH",
    "Anwar Ibrahim": "PH",
    "Muhyiddin": "PN",
    "Onn Hafiz": "BN",
    "Ahmad Zahid": "BN",
    "Rafizi": "PH",
    "Rafizi Ramli": "PH",
    "Nik Nazmi": "PH",
    "Fahmi": "PH",
    "Azalina": "BN",
    "Najib": "BN",
    "Abdul Hadi Awang": "PN",
    "Tengku Zafrul": "BN",
    "Maszlee": "BERSAMA",
}


def get_latest_entities_file():
    """Find the most recent entities JSON file."""
    json_files = list(ENTITIES_DIR.glob("entities_*.json"))
    if not json_files:
        json_files = list(ENTITIES_DIR.glob("*entities*.json"))
    
    if not json_files:
        raise FileNotFoundError("No entities files found")
    
    json_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    return json_files[0]


def load_raw_sources():
    """Load all raw source files from the collection."""
    sources = {}
    
    if not RAW_DIR.exists():
        print(f"Warning: Raw directory {RAW_DIR} does not exist")
        return sources
    
    # Get the most recent raw files
    raw_files = sorted(RAW_DIR.glob("*.json"), key=lambda f: f.stat().st_mtime, reverse=True)[:50]
    
    for raw_file in raw_files:
        # Skip non-source files (like collection metadata)
        if '_political_collection' in raw_file.name:
            continue
            
        try:
            with open(raw_file, 'r') as f:
                data = json.load(f)
            
            source_name = data.get('source', raw_file.stem.split('_')[-1] if '_' in raw_file.name else raw_file.stem)
            
            # Extract full content for sentiment analysis
            full_content = data.get('full_content', '')
            headlines = data.get('headlines', [])
            
            # Combine all text content
            text_content = full_content
            for headline in headlines:
                if isinstance(headline, str):
                    text_content += " " + headline
            
            sources[source_name] = {
                'file': str(raw_file),
                'content': text_content,
                'headlines': headlines
            }
        except Exception as e:
            print(f"Warning: Could not load {raw_file}: {e}")
    
    return sources


def load_entities(filepath):
    """Load entities from JSON file."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data


def extract_entity_context(entity, sources, entity_type):
    """
    Extract text context around entity mentions from source content.
    Returns concatenated snippets mentioning the entity.
    """
    contexts = []
    
    for source_name, source_data in sources.items():
        content = source_data.get('content', '')
        
        # Find sentences/segments mentioning the entity
        # Split by common delimiters
        segments = re.split(r'[.!?]\s+', content)
        
        for segment in segments:
            if entity.lower() in segment.lower():
                # Get a window around the mention
                contexts.append(segment.strip())
    
    # If no context found, return entity name
    if not contexts:
        return entity
    
    # Return unique contexts, limited to avoid overwhelming the analyzer
    unique_contexts = list(dict.fromkeys(contexts))[:5]
    return ' '.join(unique_contexts)


def analyze_sentiment(text, analyzer):
    """
    Analyze sentiment of text using VADER.
    Returns score normalized to -3 to +3 scale.
    """
    scores = analyzer.polarity_scores(text)
    # VADER compound is -1 to 1, scale to -3 to +3
    compound_scaled = scores['compound'] * 3
    return {
        'compound': round(compound_scaled, 2),
        'positive': scores['pos'],
        'neutral': scores['neu'],
        'negative': scores['neg'],
        'raw_compound': scores['compound']
    }


def calculate_zscore(value, mean_val, std_val):
    """Calculate z-score for anomaly detection."""
    if std_val == 0:
        return 0
    return (value - mean_val) / std_val


def analyze_entities(data, sources):
    """Perform sentiment analysis on all entities with context from sources."""
    analyzer = SentimentIntensityAnalyzer()
    
    # Handle both 'entities' and 'aggregated_entities' keys
    entities = data.get('aggregated_entities', data.get('entities', {}))
    extraction_timestamp = data.get('extraction_timestamp', 'unknown')
    
    results = {
        'extraction_timestamp': extraction_timestamp,
        'analysis_timestamp': datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'),
        'sources_analyzed': list(sources.keys())[:20],  # Limit for readability
        'entity_sentiments': {},
        'category_aggregates': {},
        'coalition_aggregates': {},
        'anomalies': [],
        'summary': {}
    }
    
    all_scores = []
    
    # Analyze each entity by type
    for entity_type, entity_list in entities.items():
        results['entity_sentiments'][entity_type] = []
        category_scores = []
        
        for entity in entity_list:
            # Get context from source files
            context = extract_entity_context(entity, sources, entity_type)
            sentiment = analyze_sentiment(context, analyzer)
            
            # Count sources mentioning this entity
            source_count = sum(1 for src in sources.values() 
                             if entity.lower() in src.get('content', '').lower())
            
            entity_result = {
                'name': entity,
                'type': entity_type,
                'sentiment_score': sentiment['compound'],
                'positive': sentiment['positive'],
                'neutral': sentiment['neutral'],
                'negative': sentiment['negative'],
                'source_count': source_count,
                'context_snippet': context[:200] + '...' if len(context) > 200 else context
            }
            
            results['entity_sentiments'][entity_type].append(entity_result)
            category_scores.append(sentiment['compound'])
            all_scores.append(sentiment['compound'])
        
        # Category aggregate
        if category_scores:
            results['category_aggregates'][entity_type] = {
                'count': len(category_scores),
                'mean_sentiment': round(mean(category_scores), 3),
                'std_sentiment': round(stdev(category_scores), 3) if len(category_scores) > 1 else 0,
                'min_sentiment': min(category_scores),
                'max_sentiment': max(category_scores)
            }
    
    # Calculate coalition/party aggregates
    org_sentiments = {e['name']: e['sentiment_score'] 
                      for e in results['entity_sentiments'].get('ORGANIZATION', [])}
    
    for coalition, members in COALITIONS.items():
        coalition_scores = []
        members_found = []
        
        for member in members:
            if member in org_sentiments:
                coalition_scores.append(org_sentiments[member])
                members_found.append(member)
        
        if coalition_scores:
            results['coalition_aggregates'][coalition] = {
                'members_found': members_found,
                'mean_sentiment': round(mean(coalition_scores), 3),
                'count': len(coalition_scores)
            }
    
    # Add person affiliations to coalition analysis
    person_sentiments = {e['name']: e['sentiment_score'] 
                        for e in results['entity_sentiments'].get('PERSON', [])}
    
    for person, affiliation in FIGURE_AFFILIATIONS.items():
        if person in person_sentiments:
            if affiliation not in results['coalition_aggregates']:
                results['coalition_aggregates'][affiliation] = {'members_found': [], 'count': 0, 'scores': []}
            if person not in results['coalition_aggregates'][affiliation]['members_found']:
                results['coalition_aggregates'][affiliation]['members_found'].append(person)
    
    # Recalculate coalition aggregates with persons included
    for coalition, data_item in results['coalition_aggregates'].items():
        if isinstance(data_item, dict) and 'members_found' in data_item:
            scores = []
            for member in data_item['members_found']:
                if member in org_sentiments:
                    scores.append(org_sentiments[member])
                if member in person_sentiments:
                    scores.append(person_sentiments[member])
            if scores:
                data_item['mean_sentiment'] = round(mean(scores), 3)
                data_item['count'] = len(scores)
    
    # Detect anomalies (z-score > 2)
    if len(all_scores) > 2:
        overall_mean = mean(all_scores)
        overall_std = stdev(all_scores)
        
        for entity_type, entities_list in results['entity_sentiments'].items():
            for entity_data in entities_list:
                zscore = calculate_zscore(entity_data['sentiment_score'], overall_mean, overall_std)
                if abs(zscore) > 2:
                    results['anomalies'].append({
                        'entity': entity_data['name'],
                        'type': entity_type,
                        'sentiment_score': entity_data['sentiment_score'],
                        'z_score': round(zscore, 3),
                        'anomaly_type': 'positive' if zscore > 0 else 'negative'
                    })
    
    # Summary statistics
    results['summary'] = {
        'total_entities': sum(len(v) for v in entities.values()),
        'total_anomalies': len(results['anomalies']),
        'overall_mean_sentiment': round(mean(all_scores), 3) if all_scores else 0,
        'overall_std_sentiment': round(stdev(all_scores), 3) if len(all_scores) > 1 else 0,
        'sentiment_distribution': {
            'positive': len([s for s in all_scores if s > 0.5]),
            'neutral': len([s for s in all_scores if -0.5 <= s <= 0.5]),
            'negative': len([s for s in all_scores if s < -0.5])
        }
    }
    
    return results


def generate_report(results):
    """Generate a markdown report from analysis results."""
    timestamp = results['analysis_timestamp']
    
    report = f"""# Sentiment Analysis Report

**Generated:** {timestamp}
**Extraction Cycle:** {results['extraction_timestamp']}
**Sources Analyzed:** {', '.join(results['sources_analyzed']) if results['sources_analyzed'] else 'None (used entity names only)'}

---

## Executive Summary

- **Total Entities Analyzed:** {results['summary']['total_entities']}
- **Overall Mean Sentiment:** {results['summary']['overall_mean_sentiment']:+.3f}
- **Sentiment Std Dev:** {results['summary']['overall_std_sentiment']:.3f}
- **Anomalies Detected:** {results['summary']['total_anomalies']}

### Sentiment Distribution
- Positive (>0.5): {results['summary']['sentiment_distribution']['positive']} entities
- Neutral (-0.5 to 0.5): {results['summary']['sentiment_distribution']['neutral']} entities
- Negative (<-0.5): {results['summary']['sentiment_distribution']['negative']} entities

---

## Entity Sentiments by Type

"""
    
    for entity_type, entities_list in results['entity_sentiments'].items():
        report += f"### {entity_type}\n\n"
        report += "| Entity | Sentiment (-3 to +3) | Pos | Neu | Neg | Sources |\n"
        report += "|--------|---------------------|-----|-----|-----|---------|\n"
        
        # Sort by sentiment score
        sorted_entities = sorted(entities_list, key=lambda x: x['sentiment_score'], reverse=True)
        for entity in sorted_entities:
            score_display = f"{entity['sentiment_score']:+.2f}"
            report += f"| {entity['name']} | {score_display} | {entity['positive']:.2f} | {entity['neutral']:.2f} | {entity['negative']:.2f} | {entity['source_count']} |\n"
        
        # Category aggregate
        if entity_type in results['category_aggregates']:
            agg = results['category_aggregates'][entity_type]
            report += f"\n**Category Aggregate:** Mean={agg['mean_sentiment']:+.3f}, Std={agg['std_sentiment']:.3f}, Range=[{agg['min_sentiment']:+.2f}, {agg['max_sentiment']:+.2f}]\n\n"
    
    report += "---\n\n## Coalition/Party Aggregates\n\n"
    report += "| Coalition/Party | Mean Sentiment | Members/Entities Found |\n"
    report += "|-----------------|----------------|------------------------|\n"
    
    for coalition, data in sorted(results['coalition_aggregates'].items()):
        if isinstance(data, dict) and 'mean_sentiment' in data:
            members = ', '.join(data.get('members_found', []))
            report += f"| {coalition} | {data['mean_sentiment']:+.3f} | {members} |\n"
    
    report += "\n---\n\n## Sentiment Anomalies (|z-score| > 2)\n\n"
    
    if results['anomalies']:
        report += "| Entity | Type | Sentiment | Z-Score | Anomaly Type |\n"
        report += "|--------|------|-----------|---------|-------------|\n"
        for anomaly in sorted(results['anomalies'], key=lambda x: abs(x['z_score']), reverse=True):
            report += f"| {anomaly['entity']} | {anomaly['type']} | {anomaly['sentiment_score']:+.2f} | {anomaly['z_score']:+.3f} | {anomaly['anomaly_type']} |\n"
    else:
        report += "*No significant anomalies detected.*\n"
    
    report += """
---

## Methodology

- **Sentiment Engine:** VADER (Valence Aware Dictionary and sEntiment Reasoner)
- **Score Range:** -3 (most negative) to +3 (most positive)
- **Anomaly Threshold:** |z-score| > 2
- **Context:** Entity mentions extracted from news source content for sentiment analysis

---

*Report generated by OpenCLaw Sentiment Analysis Pipeline*
"""
    
    return report


def main():
    """Main execution function."""
    print("Starting sentiment analysis...")
    
    # Find latest entities file
    entities_file = get_latest_entities_file()
    print(f"Using entities file: {entities_file}")
    
    # Load entities
    data = load_entities(entities_file)
    entities = data.get('aggregated_entities', data.get('entities', {}))
    entity_count = sum(len(v) for v in entities.values())
    print(f"Loaded {entity_count} entities")
    
    # Load raw sources for context
    sources = load_raw_sources()
    print(f"Loaded {len(sources)} source files")
    
    if not sources:
        print("Warning: No source files found. Sentiment analysis will use entity names only.")
    
    # Perform analysis
    results = analyze_entities(data, sources)
    print(f"Analysis complete. Found {len(results['anomalies'])} anomalies")
    
    # Generate report
    report = generate_report(results)
    
    # Save outputs
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = results['analysis_timestamp']
    
    # Save JSON results
    json_path = OUTPUT_DIR / f"sentiment_{timestamp}.json"
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"Saved JSON results: {json_path}")
    
    # Save markdown report
    md_path = OUTPUT_DIR / f"sentiment_{timestamp}.md"
    with open(md_path, 'w') as f:
        f.write(report)
    print(f"Saved markdown report: {md_path}")
    
    # Also save as latest for easy reference
    latest_json = OUTPUT_DIR / "sentiment_latest.json"
    with open(latest_json, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    latest_md = OUTPUT_DIR / "sentiment_latest.md"
    with open(latest_md, 'w') as f:
        f.write(report)
    
    print("\n=== SUMMARY ===")
    print(f"Overall Sentiment: {results['summary']['overall_mean_sentiment']:+.3f}")
    print(f"Anomalies: {results['summary']['total_anomalies']}")
    print("\nCoalition Sentiments:")
    for coalition, data in sorted(results['coalition_aggregates'].items()):
        if isinstance(data, dict) and 'mean_sentiment' in data:
            print(f"  {coalition}: {data['mean_sentiment']:+.3f}")
    
    return results


if __name__ == '__main__':
    main()

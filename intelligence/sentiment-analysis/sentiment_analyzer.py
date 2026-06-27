#!/usr/bin/env python3
"""
Sentiment Analysis Script for OpenClaw Entity Extraction
Optimized rule-based sentiment analysis on extracted entities
"""

import json
import os
import re
from datetime import datetime
from collections import defaultdict
import statistics

# Compact sentiment lexicons
POSITIVE_WORDS = {
    'favoured': 2, 'favourite': 2, 'popular': 2, 'approved': 2, 'approval': 2,
    'congratulates': 2, 'success': 2, 'successful': 2, 'excel': 2, 'outperform': 2,
    'strengthen': 1, 'boost': 2, 'sustainable': 1, 'strategic': 1, 'collaboration': 1,
    'secure': 1, 'secured': 1, 'support': 1, 'innovation': 1, 'competitive': 1,
    'quality': 1, 'green': 1, 'clean': 1, 'backs': 1, 'resolved': 1, 'stable': 1,
    'remains': 0.5, 'top': 1, 'advance': 1, 'win': 2, 'won': 2, 'victory': 2,
    'capacity': 1, 'special': 1, 'award': 2, 'save': 1, 'approve': 1, 'growth': 1,
    'development': 1, 'better': 1, 'best': 2, 'strong': 1, 'stronger': 1,
    'unity': 1, 'talent': 1, 'agreement': 1, 'deal': 1, 'good': 1, 'promising': 2,
    'breakthrough': 2, 'milestone': 2, 'partnership': 1, 'nurture': 1, 'embrace': 1,
    'foundation': 1, 'rebuild': 1, 'recovery': 1, 'resolve': 1, 'ambition': 1,
}

NEGATIVE_WORDS = {
    'scam': -3, 'syndicate': -2, 'bust': -2, 'illegal': -2, 'outlawed': -2,
    'nabbed': -2, 'arrest': -2, 'crime': -2, 'leaked': -2, 'leak': -2,
    'baseless': -2, 'puppet': -2, 'criticism': -1, 'allegation': -1, 'allegations': -1,
    'quit': -1, 'resign': -1, 'cronyism': -2, 'risk': -1, 'risks': -1, 'tough': -1,
    'concern': -1, 'concerns': -1, 'underrepresentation': -1, 'lag': -1, 'lags': -1,
    'split': -1, 'mixed': -0.5, 'defeat': -2, 'defeated': -2, 'lost': -2, 'loss': -2,
    'out': -1, 'exit': -1, 'warn': -1, 'warned': -1, 'warning': -1, 'alert': -1,
    'haze': -1, 'postponed': -1, 'delay': -1, 'cancel': -2, 'cancelled': -2,
    'reject': -1, 'denies': -1, 'urge': -0.5, 'crisis': -2, 'collapse': -2,
    'dies': -3, 'died': -3, 'death': -3, 'mishap': -2, 'accident': -2,
    'impersonating': -2, 'fake': -2, 'fraud': -3, 'bullying': -2, 'violence': -2,
    'conflict': -2, 'war': -2, 'attack': -2, 'threat': -2, 'sanction': -1,
    'protest': -1, 'terror': -3, 'terrorism': -3, 'scandal': -2, 'controversy': -1,
    'failure': -2, 'failed': -2, 'fail': -2, 'weak': -1, 'weakness': -1,
    'decline': -1, 'crash': -2, 'unemployment': -1, 'inflation': -1, 'recession': -2,
    'poverty': -2, 'discrimination': -2, 'abuse': -2, 'violation': -2, 'breach': -1,
    'unfair': -1, 'unjust': -2, 'injustice': -2, 'error': -1, 'mistake': -1,
    'blame': -1, 'fault': -1, 'guilty': -2, 'suspect': -1, 'suspected': -1,
    'investigation': -1, 'probe': -1, 'penalty': -1, 'fine': -1, 'sentence': -1,
    'sentenced': -2, 'prison': -2, 'jail': -2, 'conviction': -2, 'convicted': -2,
}

# Political entity mappings for coalition analysis
COALITION_MAPPING = {
    'Pakatan Harapan': ['Anwar Ibrahim', 'Anwar', 'PM Anwar', 'Datuk Seri Anwar Ibrahim', 
                        'Ahmad Zahid', 'DPM Ahmad Zahid', 'Zahid', 'Rafizi', 'Rafizi Ramli',
                        'Azmin', 'Azmin Ali', 'Hamzah'],
    'BN': ['Ahmad Zahid', 'Zahid', 'UMNO', 'Umno', 'MCA', 'MIC', 'Barisan Nasional'],
    'PN': ['Muhyiddin', 'Muhyiddin Yassin', 'Hamzah', 'PAS', 'Bersatu', 'Perikatan Nasional'],
    'GPS': ['Abang Johari', 'Sarawak Parties'],
    'GRS': ['Hajiji', 'Sabah Parties'],
}


def load_entities_from_files(entities_dir):
    """Load entities from the most recent extraction files"""
    entities = {'PERSON': [], 'ORGANIZATION': [], 'LOCATION': [], 'EVENT': [], 'CONCEPT': []}
    
    entity_files = []
    for f in os.listdir(entities_dir):
        if f.endswith('-entities.json') or (f.startswith('entities_') and f.endswith('.json')):
            filepath = os.path.join(entities_dir, f)
            entity_files.append((filepath, os.path.getmtime(filepath)))
    
    entity_files.sort(key=lambda x: x[1], reverse=True)
    loaded_files = []
    
    for filepath, _ in entity_files[:2]:
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                if 'entities' in data:
                    for entity_type, entity_list in data['entities'].items():
                        if entity_type in entities:
                            for entity in entity_list:
                                if entity not in entities[entity_type]:
                                    entities[entity_type].append(entity)
                    loaded_files.append(filepath)
        except Exception as e:
            print(f"Error loading {filepath}: {e}")
    
    return entities, loaded_files


def load_source_content(raw_dir):
    """Load source content for context analysis"""
    content_files = []
    for f in os.listdir(raw_dir):
        if f.endswith('.json'):
            filepath = os.path.join(raw_dir, f)
            content_files.append((filepath, os.path.getmtime(filepath)))
    
    content_files.sort(key=lambda x: x[1], reverse=True)
    all_content = []
    
    for filepath, _ in content_files[:3]:
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                if 'results' in data:
                    for result in data['results']:
                        if 'full_content' in result:
                            all_content.append({
                                'source': result.get('source', 'unknown'),
                                'content': result['full_content'].lower()
                            })
        except Exception as e:
            print(f"Error loading {filepath}: {e}")
    
    return all_content


def calculate_sentiment_fast(entity, entity_type, all_content):
    """Fast sentiment calculation using simple word matching"""
    entity_lower = entity.lower()
    total_score = 0
    mention_count = 0
    
    for source_data in all_content:
        content = source_data['content']
        
        # Check if entity is mentioned
        if entity_lower not in content:
            continue
        
        # Find context windows around entity mentions
        idx = 0
        while True:
            pos = content.find(entity_lower, idx)
            if pos == -1:
                break
            
            # Extract context window (200 chars before and after)
            start = max(0, pos - 200)
            end = min(len(content), pos + 200)
            context = content[start:end]
            
            # Score the context
            score = 0
            for word in POSITIVE_WORDS:
                if word in context:
                    score += POSITIVE_WORDS[word]
            for word in NEGATIVE_WORDS:
                if word in context:
                    score += NEGATIVE_WORDS[word]
            
            # Clamp individual context score
            score = max(-5, min(5, score))
            total_score += score
            mention_count += 1
            
            idx = pos + 1
    
    if mention_count == 0:
        return 0, 0, 0
    
    avg_score = total_score / mention_count
    # Clamp to -3 to +3 range
    avg_score = max(-3, min(3, avg_score))
    
    return round(avg_score, 2), mention_count, total_score


def analyze_all_entities(entities, all_content):
    """Analyze sentiment for all entities"""
    results = {}
    
    for entity_type, entity_list in entities.items():
        results[entity_type] = {}
        for entity in entity_list:
            score, mentions, total = calculate_sentiment_fast(entity, entity_type, all_content)
            results[entity_type][entity] = {
                'sentiment_score': score,
                'mention_count': mentions,
                'total_raw_score': total
            }
    
    return results


def calculate_coalition_sentiment(entity_results):
    """Calculate aggregate sentiment for political coalitions"""
    coalition_sentiments = {}
    
    for coalition, members in COALITION_MAPPING.items():
        scores = []
        for member in members:
            member_lower = member.lower()
            for entity_type, entities in entity_results.items():
                for entity, data in entities.items():
                    if member_lower in entity.lower() or entity.lower() in member_lower:
                        scores.append(data['sentiment_score'])
        
        if scores:
            avg = statistics.mean(scores)
            coalition_sentiments[coalition] = {
                'aggregate_sentiment': round(avg, 2),
                'member_count': len(scores),
                'sentiment_range': [round(min(scores), 2), round(max(scores), 2)]
            }
    
    return coalition_sentiments


def detect_anomalies(entity_results, threshold=2.0):
    """Detect sentiment anomalies using z-score"""
    all_scores = []
    score_map = []
    
    for entity_type, entities in entity_results.items():
        for entity, data in entities.items():
            all_scores.append(data['sentiment_score'])
            score_map.append({'entity': entity, 'type': entity_type, 'score': data['sentiment_score']})
    
    if len(all_scores) < 2:
        return []
    
    mean_score = statistics.mean(all_scores)
    std_score = statistics.stdev(all_scores)
    
    anomalies = []
    for item in score_map:
        if std_score > 0:
            z_score = (item['score'] - mean_score) / std_score
            if abs(z_score) > threshold:
                anomalies.append({
                    'entity': item['entity'],
                    'type': item['type'],
                    'sentiment_score': item['score'],
                    'z_score': round(z_score, 2),
                    'direction': 'positive' if z_score > 0 else 'negative'
                })
    
    return sorted(anomalies, key=lambda x: abs(x['z_score']), reverse=True)


def generate_report(entity_results, coalition_sentiments, anomalies, loaded_files, output_dir):
    """Generate comprehensive sentiment analysis report"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Gather statistics
    all_scores = []
    for entity_type, entities in entity_results.items():
        for entity, data in entities.items():
            all_scores.append(data['sentiment_score'])
    
    report = {
        'report_metadata': {
            'generated_at': datetime.now().isoformat(),
            'source_files': loaded_files,
            'analysis_type': 'rule-based sentiment analysis',
            'score_range': '[-3 (very negative) to +3 (very positive)]'
        },
        'entity_sentiment': entity_results,
        'coalition_sentiment': coalition_sentiments,
        'anomalies': {
            'detection_method': 'z-score > 2.0',
            'detected_anomalies': anomalies
        },
        'summary': {
            'total_entities_analyzed': sum(len(entities) for entities in entity_results.values()),
            'entities_by_type': {k: len(v) for k, v in entity_results.items()},
            'anomaly_count': len(anomalies),
            'coalitions_analyzed': len(coalition_sentiments)
        }
    }
    
    if all_scores:
        report['summary']['overall_statistics'] = {
            'mean_sentiment': round(statistics.mean(all_scores), 2),
            'median_sentiment': round(statistics.median(all_scores), 2),
            'std_deviation': round(statistics.stdev(all_scores), 2) if len(all_scores) > 1 else 0,
            'min_sentiment': min(all_scores),
            'max_sentiment': max(all_scores)
        }
    
    # Write JSON report
    json_path = os.path.join(output_dir, f'sentiment_report_{timestamp}.json')
    with open(json_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    # Write Markdown summary
    md_path = os.path.join(output_dir, f'sentiment_summary_{timestamp}.md')
    generate_markdown_summary(report, md_path)
    
    return json_path, md_path


def generate_markdown_summary(report, md_path):
    """Generate markdown summary report"""
    md = f"""# Sentiment Analysis Report

**Generated:** {report['report_metadata']['generated_at']}
**Score Range:** -3 (very negative) to +3 (very positive)

## Summary

| Metric | Value |
|--------|-------|
| Total Entities | {report['summary']['total_entities_analyzed']} |
| Anomalies | {report['summary']['anomaly_count']} |
| Mean Sentiment | {report['summary']['overall_statistics']['mean_sentiment']} |
| Median Sentiment | {report['summary']['overall_statistics']['median_sentiment']} |

## Coalition Sentiment

| Coalition | Score | Members | Range |
|-----------|-------|---------|-------|
"""
    for coalition, data in report['coalition_sentiment'].items():
        md += f"| {coalition} | {data['aggregate_sentiment']} | {data['member_count']} | {data['sentiment_range']} |\n"
    
    md += "\n## Anomalies (z-score > 2.0)\n\n"
    if report['anomalies']['detected_anomalies']:
        md += "| Entity | Type | Score | Z-Score | Direction |\n|--------|------|-------|---------|----------|\n"
        for a in report['anomalies']['detected_anomalies'][:15]:
            md += f"| {a['entity']} | {a['type']} | {a['sentiment_score']} | {a['z_score']} | {a['direction']} |\n"
    else:
        md += "No significant anomalies detected.\n"
    
    md += "\n## Top Entities by Sentiment\n\n"
    for etype in ['PERSON', 'ORGANIZATION']:
        if etype in report['entity_sentiment']:
            md += f"### {etype}\n\n| Entity | Score | Mentions |\n|--------|-------|--------|\n"
            sorted_e = sorted(report['entity_sentiment'][etype].items(), key=lambda x: x[1]['sentiment_score'], reverse=True)[:15]
            for entity, data in sorted_e:
                md += f"| {entity} | {data['sentiment_score']} | {data['mention_count']} |\n"
            md += "\n"
    
    with open(md_path, 'w') as f:
        f.write(md)


def main():
    entities_dir = '/home/p62operator/.openclaw/workspace-hoi/intelligence/entities/'
    raw_dir = '/home/p62operator/.openclaw/workspace-hoi/intelligence/raw/'
    output_dir = '/home/p62operator/.openclaw/workspace-hoi/intelligence/sentiment-analysis/'
    
    os.makedirs(output_dir, exist_ok=True)
    
    print("Loading entities...")
    entities, loaded_files = load_entities_from_files(entities_dir)
    print(f"Files: {loaded_files}")
    print(f"Counts: { {k: len(v) for k, v in entities.items()} }")
    
    print("Loading source content...")
    all_content = load_source_content(raw_dir)
    print(f"Loaded {len(all_content)} documents")
    
    print("Analyzing sentiment...")
    entity_results = analyze_all_entities(entities, all_content)
    
    print("Calculating coalition sentiment...")
    coalition_sentiments = calculate_coalition_sentiment(entity_results)
    
    print("Detecting anomalies...")
    anomalies = detect_anomalies(entity_results)
    print(f"Found {len(anomalies)} anomalies")
    
    print("Generating reports...")
    json_path, md_path = generate_report(entity_results, coalition_sentiments, anomalies, loaded_files, output_dir)
    
    print(f"\n=== COMPLETE ===")
    print(f"JSON: {json_path}")
    print(f"Markdown: {md_path}")
    
    print("\n=== Coalition Sentiments ===")
    for coalition, data in coalition_sentiments.items():
        icon = "🟢" if data['aggregate_sentiment'] > 0.5 else "🔴" if data['aggregate_sentiment'] < -0.5 else "🟡"
        print(f"  {icon} {coalition}: {data['aggregate_sentiment']}")
    
    if anomalies:
        print("\n=== Top Anomalies ===")
        for a in anomalies[:5]:
            icon = "⬆️" if a['direction'] == 'positive' else "⬇️"
            print(f"  {icon} {a['entity']}: {a['sentiment_score']} (z={a['z_score']})")


if __name__ == '__main__':
    main()

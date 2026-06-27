#!/usr/bin/env python3
"""
Sentiment Analysis Script for Political Entities
Political Monitoring Workstream - HOI Agent
Classification: TLP:AMBER

Analyzes sentiment for all entities extracted in the previous extraction cycle.
Uses LLM-based scoring with keyword heuristics and Malaysian political context.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
import re
import math

# Configuration
ENTITIES_DIR = Path("/home/p62operator/.openclaw/workspace-hoi/intelligence/entities")
OUTPUT_DIR = Path("/home/p62operator/.openclaw/workspace-hoi/intelligence/sentiment-analysis")
LEXICON_PATH = Path("/home/p62operator/.openclaw/workspace-hoi/config/sentiment-lexicon.yaml")

# Sentiment scale: -3 to +3
SENTIMENT_SCALE = {
    -3: "Very Negative",
    -2: "Negative", 
    -1: "Slightly Negative",
    0: "Neutral",
    +1: "Slightly Positive",
    +2: "Positive",
    +3: "Very Positive"
}

# Coalition mappings
COALITIONS = {
    "PH": ["PKR", "DAP", "AMANAH"],
    "BN": ["UMNO", "MCA", "MIC"],
    "PN": ["BERSATU", "PAS"],
    "GRB": []  # Sabah coalition
}

def load_lexicon():
    """Load sentiment lexicon from YAML file."""
    lexicon = {
        "positive": {"very_positive": [], "positive": [], "slightly_positive": []},
        "negative": {"very_negative": [], "negative": [], "slightly_negative": []},
        "negations": [],
        "intensifiers": {},
        "context_rules": {},
        "emotion_patterns": {},
        "framing_patterns": {}
    }
    
    if LEXICON_PATH.exists():
        with open(LEXICON_PATH, 'r') as f:
            content = f.read()
        
        # Simple YAML parsing for our lexicon structure
        current_section = None
        current_subsection = None
        
        for line in content.split('\n'):
            line = line.rstrip()
            if not line or line.startswith('#'):
                continue
            
            # Top-level sections
            if line.startswith('positive:'):
                current_section = 'positive'
            elif line.startswith('negative:'):
                current_section = 'negative'
            elif line.startswith('negations:'):
                current_section = 'negations'
            elif line.startswith('intensifiers:'):
                current_section = 'intensifiers'
            elif line.startswith('context_rules:'):
                current_section = 'context_rules'
            elif line.startswith('emotion_patterns:'):
                current_section = 'emotion_patterns'
            elif line.startswith('framing_patterns:'):
                current_section = 'framing_patterns'
            elif current_section == 'positive':
                if 'very_positive:' in line:
                    current_subsection = 'very_positive'
                elif 'positive:' in line and 'slightly' not in line:
                    current_subsection = 'positive'
                elif 'slightly_positive:' in line:
                    current_subsection = 'slightly_positive'
                elif line.strip().startswith('- '):
                    word = line.strip().replace('"', '').replace('- ', '').strip()
                    if current_subsection and current_subsection in lexicon['positive']:
                        lexicon['positive'][current_subsection].append(word)
            elif current_section == 'negative':
                if 'very_negative:' in line:
                    current_subsection = 'very_negative'
                elif 'negative:' in line and 'slightly' not in line:
                    current_subsection = 'negative'
                elif 'slightly_negative:' in line:
                    current_subsection = 'slightly_negative'
                elif line.strip().startswith('- '):
                    word = line.strip().replace('"', '').replace('- ', '').strip()
                    if current_subsection and current_subsection in lexicon['negative']:
                        lexicon['negative'][current_subsection].append(word)
            elif current_section == 'negations':
                if line.strip().startswith('- '):
                    word = line.strip().replace('"', '').replace('- ', '').strip()
                    lexicon['negations'].append(word)
            elif current_section == 'intensifiers':
                if ':' in line and line.strip().startswith('- ') == False:
                    parts = line.strip().split(':')
                    if len(parts) == 2:
                        try:
                            lexicon['intensifiers'][parts[0].strip()] = float(parts[1].strip())
                        except ValueError:
                            pass
            elif current_section == 'emotion_patterns':
                if line.strip().endswith(':') and not line.strip().startswith('-'):
                    current_subsection = line.strip().replace(':', '')
                    if current_subsection not in lexicon['emotion_patterns']:
                        lexicon['emotion_patterns'][current_subsection] = []
                elif line.strip().startswith('- '):
                    word = line.strip().replace('"', '').replace('- ', '').strip()
                    if current_subsection and current_subsection in lexicon['emotion_patterns']:
                        lexicon['emotion_patterns'][current_subsection].append(word)
            elif current_section == 'framing_patterns':
                if line.strip().endswith(':') and not line.strip().startswith('-'):
                    current_subsection = line.strip().replace(':', '')
                    if current_subsection not in lexicon['framing_patterns']:
                        lexicon['framing_patterns'][current_subsection] = []
                elif line.strip().startswith('- '):
                    word = line.strip().replace('"', '').replace('- ', '').strip()
                    if current_subsection and current_subsection in lexicon['framing_patterns']:
                        lexicon['framing_patterns'][current_subsection].append(word)
    
    return lexicon


def load_entities():
    """Load entities from the latest extraction cycle."""
    # Find the most recent entities JSON file
    entity_files = list(ENTITIES_DIR.glob("*_entities.json"))
    
    if not entity_files:
        print("ERROR: No entity files found")
        return None
    
    # Sort by modification time
    entity_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    latest_file = entity_files[0]
    
    print(f"Loading entities from: {latest_file}")
    
    with open(latest_file, 'r') as f:
        data = json.load(f)
    
    return data, latest_file.name


def analyze_entity_sentiment(entity, lexicon, all_entities):
    """
    Analyze sentiment for a single entity based on context and lexicon.
    Returns sentiment score (-3 to +3), confidence, emotion, and framing.
    """
    name = entity.get('name', '')
    context = entity.get('context', '')
    entity_type = entity.get('type', 'UNKNOWN')
    pir_relevance = entity.get('pir_relevance', [])
    
    # Combine name and context for analysis
    text = f"{name} {context}".lower()
    
    # Base sentiment score
    score = 0
    confidence = 0.5
    emotions = []
    frames = []
    
    # Check positive keywords
    for word in lexicon['positive']['very_positive']:
        if word.lower() in text:
            score += 3
            confidence += 0.1
    for word in lexicon['positive']['positive']:
        if word.lower() in text:
            score += 2
            confidence += 0.1
    for word in lexicon['positive']['slightly_positive']:
        if word.lower() in text:
            score += 1
            confidence += 0.05
    
    # Check negative keywords
    for word in lexicon['negative']['very_negative']:
        if word.lower() in text:
            score -= 3
            confidence += 0.1
    for word in lexicon['negative']['negative']:
        if word.lower() in text:
            score -= 2
            confidence += 0.1
    for word in lexicon['negative']['slightly_negative']:
        if word.lower() in text:
            score -= 1
            confidence += 0.05
    
    # Apply context rules for Malaysian politics
    if 'PKR' in name or 'PKR' in context:
        if 'defection' in text or 'crisis' in text or 'faction' in text:
            score -= 0.5
        if 'unity' in text or 'reform' in text:
            score += 0.3
    
    if 'BERSAMA' in name:
        if 'momentum' in text or 'growth' in text or 'alternative' in text:
            score += 0.3
        if 'threat' in text or 'uncertainty' in text:
            score -= 0.3
    
    if 'BN' in name or 'UMNO' in name:
        if 'stability' in text or 'strength' in text:
            score += 0.2
        if 'conflict' in text or 'split' in text:
            score -= 0.4
    
    # Check for event-specific adjustments
    if 'removed' in context.lower() or 'resign' in text:
        score -= 0.4
    if 'endorse' in text or 'support' in text:
        score += 0.3
    
    # Detect emotions
    for emotion, patterns in lexicon['emotion_patterns'].items():
        for pattern in patterns:
            if pattern.lower() in text:
                emotions.append(emotion)
                break
    
    # Detect framing
    for frame, patterns in lexicon['framing_patterns'].items():
        for pattern in patterns:
            if pattern.lower() in text:
                frames.append(frame)
                break
    
    # Normalize score to -3 to +3 range
    score = max(-3, min(3, score))
    confidence = min(1.0, confidence)
    
    # Round score to nearest integer for final sentiment
    final_score = round(score)
    
    # If no specific signals, use context-based default
    if confidence < 0.6:
        # Default based on entity type and PIR relevance
        if pir_relevance:
            # Entities with PIR relevance are typically in news for a reason
            if any(pir in ['PIR-1', 'PIR-4', 'PIR-6', 'PIR-10'] for pir in pir_relevance):
                # These PIRs often involve conflict/crisis
                if final_score == 0:
                    final_score = -1
                    confidence = 0.55
            else:
                confidence = 0.5
    
    # If still no emotion detected, assign based on sentiment
    if not emotions:
        if final_score > 0:
            emotions = ['trust']
        elif final_score < 0:
            emotions = ['fear'] if 'crisis' in text or 'uncertainty' in text else 'surprise'
            if isinstance(emotions, str):
                emotions = [emotions]
        else:
            emotions = ['anticipation']
    
    if not frames:
        if 'conflict' in text or 'dispute' in text or 'crisis' in text:
            frames = ['conflict']
        elif 'economic' in text or 'cost' in text:
            frames = ['economic_consequences']
        else:
            frames = ['responsibility']
    
    return {
        'entity': name,
        'entity_type': entity_type,
        'context': context,
        'score': final_score,
        'raw_score': score,
        'confidence': round(confidence, 2),
        'intensity': min(5, max(1, abs(final_score) + 1)),
        'emotion': emotions[0] if emotions else 'neutral',
        'emotions': list(set(emotions)),
        'frame': frames[0] if frames else 'neutral',
        'frames': list(set(frames)),
        'pir_relevance': pir_relevance,
        'sources': entity.get('sources', [])
    }


def calculate_aggregate_sentiment(entity_sentiments, entity_type):
    """Calculate aggregate sentiment for a group of entities."""
    if not entity_sentiments:
        return {'score': 0, 'confidence': 0, 'count': 0}
    
    total_score = 0
    total_confidence = 0
    count = 0
    
    for sentiment in entity_sentiments:
        weight = sentiment['confidence']
        total_score += sentiment['score'] * weight
        total_confidence += weight
        count += 1
    
    avg_score = total_score / total_confidence if total_confidence > 0 else 0
    avg_confidence = total_confidence / count if count > 0 else 0
    
    return {
        'score': round(avg_score, 2),
        'label': SENTIMENT_SCALE.get(round(avg_score), 'Neutral'),
        'confidence': round(avg_confidence, 2),
        'count': count
    }


def calculate_zscore(sentiments, entity_name):
    """Calculate z-score for an entity's sentiment compared to the distribution."""
    scores = [s['score'] for s in sentiments]
    
    if len(scores) < 3:
        return 0, 0  # Not enough data for meaningful z-score
    
    mean = sum(scores) / len(scores)
    variance = sum((x - mean) ** 2 for x in scores) / len(scores)
    std_dev = math.sqrt(variance)
    
    if std_dev == 0:
        return 0, std_dev
    
    # Find the entity's score
    entity_score = None
    for s in sentiments:
        if s['entity'] == entity_name:
            entity_score = s['score']
            break
    
    if entity_score is None:
        return 0, std_dev
    
    z_score = (entity_score - mean) / std_dev
    return z_score, std_dev


def detect_anomalies(entity_sentiments):
    """Detect sentiment anomalies (z-score > 2)."""
    anomalies = []
    
    scores = [s['score'] for s in entity_sentiments]
    if len(scores) < 3:
        return anomalies
    
    mean = sum(scores) / len(scores)
    variance = sum((x - mean) ** 2 for x in scores) / len(scores)
    std_dev = math.sqrt(variance)
    
    if std_dev == 0:
        return anomalies
    
    for sentiment in entity_sentiments:
        z_score = (sentiment['score'] - mean) / std_dev
        if abs(z_score) > 2:
            anomalies.append({
                'entity': sentiment['entity'],
                'score': sentiment['score'],
                'z_score': round(z_score, 2),
                'severity': 'HIGH' if abs(z_score) > 3 else 'MEDIUM',
                'direction': 'positive' if z_score > 0 else 'negative'
            })
    
    return sorted(anomalies, key=lambda x: abs(x['z_score']), reverse=True)


def generate_report(entity_data, entity_sentiments, output_path):
    """Generate the sentiment analysis report."""
    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    
    # Group sentiments by type
    person_sentiments = [s for s in entity_sentiments if s['entity_type'] == 'PERSON']
    org_sentiments = [s for s in entity_sentiments if s['entity_type'] in ['ORGANIZATION', 'Political Party', 'Political Coalition']]
    location_sentiments = [s for s in entity_sentiments if s['entity_type'] == 'LOCATION']
    event_sentiments = [s for s in entity_sentiments if s['entity_type'] == 'EVENT']
    concept_sentiments = [s for s in entity_sentiments if s['entity_type'] == 'CONCEPT']
    
    # Calculate coalition aggregates
    coalition_sentiments = {}
    for coalition_name, parties in COALITIONS.items():
        coalition_entities = [s for s in org_sentiments if any(p in s['entity'] for p in parties)]
        if coalition_entities:
            coalition_sentiments[coalition_name] = calculate_aggregate_sentiment(coalition_entities, 'COALITION')
    
    # Detect anomalies
    all_sentiments = entity_sentiments
    anomalies = detect_anomalies(all_sentiments)
    
    # Calculate overall statistics
    all_scores = [s['score'] for s in entity_sentiments]
    overall_mean = sum(all_scores) / len(all_scores) if all_scores else 0
    overall_positive = len([s for s in entity_sentiments if s['score'] > 0])
    overall_negative = len([s for s in entity_sentiments if s['score'] < 0])
    overall_neutral = len([s for s in entity_sentiments if s['score'] == 0])
    
    # Find most positive and most negative
    most_positive = sorted(entity_sentiments, key=lambda x: x['score'], reverse=True)[:5]
    most_negative = sorted(entity_sentiments, key=lambda x: x['score'])[:5]
    
    # Build report
    report = f"""# SENTIMENT ANALYSIS REPORT
**Classification:** TLP:AMBER
**Report ID:** SENTIMENT-{timestamp}
**Generated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}
**Source Data:** {entity_data['metadata'].get('collection_cycle', 'Unknown')}
**Entities Analyzed:** {len(entity_sentiments)}

---

## Executive Summary

**Overall Sentiment Landscape:**
- Mean Sentiment Score: {overall_mean:.2f} ({SENTIMENT_SCALE.get(round(overall_mean), 'Neutral')})
- Positive Entities: {overall_positive} ({100*overall_positive/len(entity_sentiments):.1f}%)
- Negative Entities: {overall_negative} ({100*overall_negative/len(entity_sentiments):.1f}%)
- Neutral Entities: {overall_neutral} ({100*overall_neutral/len(entity_sentiments):.1f}%)

**Key Findings:**
- Anomalies Detected: {len(anomalies)} entities with z-score > 2.0
- Most Positive: {most_positive[0]['entity']} (score: +{most_positive[0]['score']}) if most_positive else 'N/A'
- Most Negative: {most_negative[0]['entity']} (score: {most_negative[0]['score']}) if most_negative else 'N/A'

---

## Aggregate Sentiment by Coalition

| Coalition | Score | Label | Confidence | Entities |
|-----------|-------|-------|------------|----------|
"""
    
    for coalition, agg in coalition_sentiments.items():
        report += f"| {coalition} | {agg['score']:+.2f} | {agg['label']} | {agg['confidence']:.2f} | {agg['count']} |\n"
    
    if not coalition_sentiments:
        report += "| N/A | N/A | N/A | N/A |\n"
    
    report += """
---

## Aggregate Sentiment by Entity Type

"""
    
    for type_name, sentiments in [
        ('PERSON', person_sentiments),
        ('ORGANIZATION', org_sentiments),
        ('LOCATION', location_sentiments),
        ('EVENT', event_sentiments),
        ('CONCEPT', concept_sentiments)
    ]:
        if sentiments:
            agg = calculate_aggregate_sentiment(sentiments, type_name)
            report += f"### {type_name}\n"
            report += f"- **Mean Score:** {agg['score']:+.2f} ({agg['label']})\n"
            report += f"- **Confidence:** {agg['confidence']:.2f}\n"
            report += f"- **Count:** {agg['count']}\n\n"
    
    report += """---

## Sentiment Anomalies (Z-Score > 2.0)

"""
    
    if anomalies:
        report += "| Entity | Score | Z-Score | Severity | Direction |\n"
        report += "|--------|-------|---------|----------|----------|\n"
        for a in anomalies:
            report += f"| {a['entity']} | {a['score']:+d} | {a['z_score']:+.2f} | {a['severity']} | {a['direction']} |\n"
    else:
        report += "*No significant anomalies detected.*\n"
    
    report += """
---

## Most Positive Entities

| Entity | Type | Score | Confidence | Context |
|--------|------|-------|------------|---------|
"""
    
    for s in most_positive:
        report += f"| {s['entity']} | {s['entity_type']} | {s['score']:+d} | {s['confidence']:.2f} | {s['context'][:50]}... |\n"
    
    report += """
---

## Most Negative Entities

| Entity | Type | Score | Confidence | Context |
|--------|------|-------|------------|---------|
"""
    
    for s in most_negative:
        report += f"| {s['entity']} | {s['entity_type']} | {s['score']:+d} | {s['confidence']:.2f} | {s['context'][:50]}... |\n"
    
    report += """
---

## Detailed Entity Sentiment Breakdown

### Persons

| Entity | Score | Confidence | Emotion | Frame | PIR Relevance |
|--------|-------|------------|---------|-------|---------------|
"""
    
    for s in sorted(person_sentiments, key=lambda x: x['score'], reverse=True):
        pir_str = ', '.join(s['pir_relevance']) if s['pir_relevance'] else '-'
        report += f"| {s['entity']} | {s['score']:+d} | {s['confidence']:.2f} | {s['emotion']} | {s['frame']} | {pir_str} |\n"
    
    report += """
### Organizations

| Entity | Score | Confidence | Emotion | Frame | Type |
|--------|-------|------------|---------|-------|------|
"""
    
    for s in sorted(org_sentiments, key=lambda x: x['score'], reverse=True):
        org_type = s.get('entity_type', 'ORGANIZATION')
        report += f"| {s['entity']} | {s['score']:+d} | {s['confidence']:.2f} | {s['emotion']} | {s['frame']} | {org_type} |\n"
    
    report += """
### Locations

| Entity | Score | Confidence | Emotion | Frame | Context |
|--------|-------|------------|---------|-------|---------|
"""
    
    for s in sorted(location_sentiments, key=lambda x: x['score'], reverse=True):
        report += f"| {s['entity']} | {s['score']:+d} | {s['confidence']:.2f} | {s['emotion']} | {s['frame']} | {s['context'][:30]}... |\n"
    
    report += """
### Events

| Entity | Score | Confidence | Emotion | Frame | Type |
|--------|-------|------------|---------|-------|------|
"""
    
    for s in sorted(event_sentiments, key=lambda x: x['score'], reverse=True):
        event_type = s.get('context', 'Event')[:30]
        report += f"| {s['entity']} | {s['score']:+d} | {s['confidence']:.2f} | {s['emotion']} | {s['frame']} | {event_type}... |\n"
    
    report += """
### Concepts

| Entity | Score | Confidence | Emotion | Frame | Category |
|--------|-------|------------|---------|-------|----------|
"""
    
    for s in sorted(concept_sentiments, key=lambda x: x['score'], reverse=True):
        report += f"| {s['entity']} | {s['score']:+d} | {s['confidence']:.2f} | {s['emotion']} | {s['frame']} | - |\n"
    
    report += f"""
---

## Methodology Notes

- **Sentiment Scale:** 7-point Likert scale (-3 to +3)
- **Anomaly Detection:** Z-score threshold > 2.0 (Medium), > 3.0 (High)
- **Confidence Scoring:** Based on keyword match strength and context clarity
- **Emotion Detection:** Primary emotion from lexicon pattern matching
- **Framing Detection:** News frame classification (Conflict, Human Interest, etc.)

---

*Report generated by HOI Agent Political Monitoring Workstream*
*Classification: TLP:AMBER - Internal Operational Use*
"""
    
    return report


def main():
    """Main execution function."""
    print("=" * 60)
    print("SENTIMENT ANALYSIS - Political Monitoring Workstream")
    print("=" * 60)
    
    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Load lexicon
    print("\n[1/5] Loading sentiment lexicon...")
    lexicon = load_lexicon()
    print(f"  - Positive keywords: {sum(len(v) for v in lexicon['positive'].values())}")
    print(f"  - Negative keywords: {sum(len(v) for v in lexicon['negative'].values())}")
    print(f"  - Emotion patterns: {len(lexicon['emotion_patterns'])}")
    print(f"  - Framing patterns: {len(lexicon['framing_patterns'])}")
    
    # Load entities
    print("\n[2/5] Loading entities from latest extraction...")
    result = load_entities()
    if not result:
        sys.exit(1)
    
    entity_data, source_file = result
    entities = entity_data.get('entities', {})
    
    total_entities = sum(len(v) for v in entities.values())
    print(f"  - Source file: {source_file}")
    print(f"  - Total entities: {total_entities}")
    print(f"  - PERSON: {len(entities.get('PERSON', []))}")
    print(f"  - ORGANIZATION: {len(entities.get('ORGANIZATION', []))}")
    print(f"  - LOCATION: {len(entities.get('LOCATION', []))}")
    print(f"  - EVENT: {len(entities.get('EVENT', []))}")
    print(f"  - CONCEPT: {len(entities.get('CONCEPT', []))}")
    
    # Analyze sentiment for each entity
    print("\n[3/5] Analyzing sentiment for each entity...")
    entity_sentiments = []
    
    for entity_type, type_entities in entities.items():
        for entity in type_entities:
            # Map entity type
            mapped_type = entity_type
            if entity_type == 'ORGANIZATION':
                org_type = entity.get('type', 'ORGANIZATION')
                if 'Coalition' in org_type:
                    mapped_type = 'Political Coalition'
                elif 'Party' in org_type:
                    mapped_type = 'Political Party'
                else:
                    mapped_type = 'ORGANIZATION'
            
            entity['type'] = mapped_type
            sentiment = analyze_entity_sentiment(entity, lexicon, entities)
            entity_sentiments.append(sentiment)
    
    print(f"  - Analyzed {len(entity_sentiments)} entities")
    
    # Calculate aggregates
    print("\n[4/5] Calculating aggregate sentiment...")
    
    # Coalition aggregates
    for coalition_name, parties in COALITIONS.items():
        coalition_entities = [s for s in entity_sentiments if any(p in s['entity'] for p in parties)]
        if coalition_entities:
            agg = calculate_aggregate_sentiment(coalition_entities, 'COALITION')
            print(f"  - {coalition_name}: {agg['score']:+.2f} ({agg['label']})")
    
    # Detect anomalies
    anomalies = detect_anomalies(entity_sentiments)
    print(f"\n[5/5] Detecting anomalies...")
    print(f"  - Anomalies found: {len(anomalies)}")
    for a in anomalies[:5]:
        print(f"    * {a['entity']}: z-score {a['z_score']:+.2f} ({a['severity']})")
    
    # Generate report
    print("\n" + "=" * 60)
    print("Generating sentiment report...")
    
    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    report_path = OUTPUT_DIR / f"sentiment-report-{timestamp}.md"
    
    report = generate_report(entity_data, entity_sentiments, report_path)
    
    with open(report_path, 'w') as f:
        f.write(report)
    
    print(f"\nReport saved to: {report_path}")
    
    # Also save JSON data
    json_path = OUTPUT_DIR / f"sentiment-data-{timestamp}.json"
    
    json_output = {
        'metadata': {
            'generated_at': datetime.utcnow().isoformat() + 'Z',
            'source_file': source_file,
            'collection_cycle': entity_data.get('metadata', {}).get('collection_cycle', 'Unknown'),
            'total_entities': len(entity_sentiments)
        },
        'entity_sentiments': entity_sentiments,
        'anomalies': anomalies,
        'coalition_aggregates': {},
        'summary': {
            'mean_sentiment': sum(s['score'] for s in entity_sentiments) / len(entity_sentiments) if entity_sentiments else 0,
            'positive_count': len([s for s in entity_sentiments if s['score'] > 0]),
            'negative_count': len([s for s in entity_sentiments if s['score'] < 0]),
            'neutral_count': len([s for s in entity_sentiments if s['score'] == 0])
        }
    }
    
    # Calculate coalition aggregates for JSON
    for coalition_name, parties in COALITIONS.items():
        coalition_entities = [s for s in entity_sentiments if any(p in s['entity'] for p in parties)]
        if coalition_entities:
            json_output['coalition_aggregates'][coalition_name] = calculate_aggregate_sentiment(coalition_entities, 'COALITION')
    
    with open(json_path, 'w') as f:
        json.dump(json_output, f, indent=2)
    
    print(f"JSON data saved to: {json_path}")
    
    print("\n" + "=" * 60)
    print("SENTIMENT ANALYSIS COMPLETE")
    print("=" * 60)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())

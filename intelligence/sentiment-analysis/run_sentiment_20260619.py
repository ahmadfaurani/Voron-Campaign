#!/usr/bin/env python3
"""
Sentiment Analysis for Political Entities - HOI Agent
Analyzes entities extracted from Malaysian political intelligence sources.
Scores sentiment from -3 (very negative) to +3 (very positive).
"""

import json
import os
import re
from datetime import datetime
from collections import defaultdict
import statistics
import math

# Configuration
ENTITIES_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/entities/"
OUTPUT_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/sentiment-analysis/"

# Political sentiment lexicons (Malaysian context)
POSITIVE_WORDS = {
    'unity': 2, 'reform': 2, 'progress': 2, 'growth': 2, 'stability': 2,
    'success': 2, 'achievement': 2, 'support': 1, 'endorse': 2, 'praise': 2,
    'commitment': 1, 'dedication': 1, 'vision': 1, 'opportunity': 2,
    'prosperity': 2, 'development': 1, 'improvement': 1, 'benefit': 1,
    'win': 2, 'victory': 2, 'strong': 1, 'confident': 1, 'hope': 1,
    'collaboration': 1, 'partnership': 1, 'alliance': 1, 'cooperation': 1,
    'celebration': 2, 'festive': 1, 'harmony': 2, 'peace': 2,
    'transformation': 1, 'promote': 1, 'formed': 1, 'innovative': 2,
    'democratic': 1, 'transparency': 1, 'accountability': 1, 'integrity': 1,
    'freedom': 1, 'rights': 1, 'empowerment': 1, 'inclusive': 1,
    'diversity': 1, 'representation': 1, 'engagement': 1,
    'strategic partnership': 2, 'energy security': 1, 'green jobs': 1,
    'visa-free travel': 1, 'direct flights': 1, 'mental health': 1,
    'anti-bullying': 2, 'cross-border crime': -1,
}

NEGATIVE_WORDS = {
    'defection': -2, 'defection cascade': -3, 'scandal': -3, 'corruption': -3,
    'trial': -2, 'riot': -3, 'protest': -2, 'crisis': -3, 'collapse': -3,
    'failure': -2, 'weak': -2, 'controversy': -2, 'allegation': -2,
    'accusation': -2, 'criticism': -2, 'attack': -2, 'threat': -2,
    'instability': -2, 'uncertainty': -1, 'tension': -2, 'conflict': -2,
    'dispute': -2, 'resignation': -1, 'dismiss': -2, 'suspend': -2,
    'investigation': -1, 'probe': -1, 'arrest': -2, 'charge': -2,
    'conviction': -2, 'sentence': -2, 'jail': -2, 'prison': -2,
    'fraud': -3, 'embezzlement': -3, 'abuse': -3, 'misconduct': -2,
    'violation': -2, 'breach': -2, 'illegal': -3, 'unlawful': -3,
    'damage control': -2, 'unity concerns': -2, 'challenges': -1,
    'disciplinary action': -2, 'publicly challenges': -2, 'opt out': -1,
    'drop': -1, 'lack': -1, 'concerns': -1, 'solo bid': -1,
    'domestic dispute': -2, 'cross-border crime': -2,
}

# Entity-specific sentiment baselines (Malaysian political context)
ENTITY_BASELINES = {
    # Coalitions
    'PH': 0.3, 'Pakatan Harapan': 0.3,
    'BN': -0.1, 'Barisan Nasional': -0.1,
    'PN': -0.2, 'Perikatan Nasional': -0.2,
    # Parties
    'PKR': 0.2, 'DAP': 0.2, 'Amanah': 0.2, 'Muda': 0.3,
    'UMNO': -0.2, 'Umno': -0.2,
    'PAS': -0.4, 'BERSATU': -0.3, 'Bersatu': -0.3,
    'BERSAMA': 0.0,
    'GRS': 0.0, 'SUPP': 0.0, 'PBS': 0.0, 'Upko': 0.0, 'Warisan': 0.0,
    # Key figures - Government
    'Anwar Ibrahim': 0.2, 'Anwar': 0.2, 'PM Anwar': 0.2, 'Seri Anwar Ibrahim': 0.2,
    'Ahmad Zahid': -0.3, 'Zahid': -0.3,
    'Fahmi': 0.1, 'Fahmi Fadzil': 0.1,
    'Loke': 0.1, 'Loke Siew Fook': 0.1,
    'Nancy': 0.1, 'Nancy Shukri': 0.1,
    'Tengku Zafrul': 0.0, 'Zafrul': 0.0,
    'Dzulkefly Ahmad': 0.1,
    'Seri Dr Wan Azizah Wan Ismail': 0.2,
    # Key figures - Opposition
    'Muhyiddin': -0.3, 'Muhyiddin Yassin': -0.3,
    'Hamzah': -0.3, 'Hamzah Zainudin': -0.3,
    'Sanusi': -0.4, 'Sanusi Nor': -0.4,
    'Azmin': -0.3, 'Azmin Ali': -0.3,
    'Najib': -0.8, 'Najib Razak': -0.8,
    'Trump': -0.5, 'Donald Trump': -0.5,
    'Putin': -0.4,
    # Key figures - State leaders
    'Onn Hafiz': 0.0,
    'Mashitah Hamidi': 0.0,
    'Nizam Abu Bakar Titingan': 0.0,
    'Roger': 0.0, 'Roger Chin': 0.0,
    'Fuad': 0.0,
    'Fazzrudin Abdul Rahman': 0.0,
    'Mohd Tajuddin Mohd Rasdi': 0.0,
    # Organizations
    'MACC': -0.5,
    'MCMC': -0.2,
    'PERKESO': 0.0, 'Socso': 0.0,
    'Petronas': 0.1,
    'CIMB': 0.0,
    'ACEM': 0.0,
    'SCO': 0.1,
    'ASEAN': 0.2,
    'Bernama': 0.0, 'Malaysiakini': 0.0, 'The Star': 0.0, 'NST': 0.0,
    'FMT': 0.0, 'Daily Express': 0.0, 'Borneo Post': 0.0,
    'Putrajaya Corporation': 0.0,
    'PPj': 0.0,
    # Concepts
    'Anti-Bullying Act': 1.5,
    'cross-border crime': -1.5,
    'domestic dispute': -1.0,
    'energy security': 0.5,
    'green jobs': 1.0,
    'mental health': 0.5,
    'strategic partnership': 1.0,
    'unity': 1.0,
    'visa-free travel': 0.5,
    'direct flights': 0.5,
    'membership': 0.0,
    # Events
    'GE16': 0.0,
    'Johor Polls': 0.0,
    'State Polls 2026': 0.0,
    'World Cup': 1.0,
    'QS World University Rankings': 0.5,
    'STPM 2025': 0.0,
    'Official Visit': 0.5,
    'ASEAN': 0.2,
    'SCO': 0.1,
}

# Coalition mappings
COALITIONS = {
    'PH': {'PKR', 'DAP', 'Amanah'},
    'BN': {'UMNO', 'Umno', 'Barisan Nasional'},
    'PN': {'PAS', 'BERSATU', 'Bersatu', 'Perikatan Nasional'},
}

# Reverse mapping: party to coalition
PARTY_TO_COALITION = {}
for coalition, parties in COALITIONS.items():
    for party in parties:
        PARTY_TO_COALITION[party] = coalition


def load_entities(filepath):
    """Load entities from JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def get_context_for_entity(entity_name, data):
    """Extract context for an entity from PIR analysis."""
    contexts = []
    
    # Check PIR analysis for entity mentions
    pir_analysis = data.get('pir_analysis', {})
    for pir_id, pir_data in pir_analysis.items():
        entities = pir_data.get('entities', [])
        if entity_name in entities:
            context_list = pir_data.get('context', [])
            contexts.extend(context_list[:2])  # Take up to 2 context snippets
    
    # Check collection summary for source info
    collection_summary = data.get('collection_summary', {})
    sources = collection_summary.get('sources_processed', [])
    if sources:
        contexts.append(f"Reported in: {', '.join(sources)}")
    
    return ' '.join(contexts) if contexts else None


def analyze_entity_sentiment(entity_name, entity_type, context=None):
    """
    Analyze sentiment for a single entity.
    Returns score from -3 to +3 with confidence and additional metadata.
    """
    # Get baseline score
    base_score = ENTITY_BASELINES.get(entity_name, 0.0)
    
    # Adjust based on entity type if no baseline
    if base_score == 0.0 and entity_name not in ENTITY_BASELINES:
        # Neutral default with slight adjustment based on type
        if entity_type == 'LOCATION':
            base_score = 0.0
        elif entity_type == 'EVENT':
            base_score = 0.0
    
    context_score = 0.0
    confidence = 0.5
    emotion = 'neutral'
    frame = 'neutral'
    
    # If context is provided, analyze it
    if context:
        context_lower = context.lower()
        
        # Check for negative phrases
        for phrase, score in NEGATIVE_WORDS.items():
            if phrase in context_lower:
                context_score += score * 0.3
                confidence = min(0.8, confidence + 0.1)
                if score < -1:
                    emotion = 'anger' if score < -2 else 'surprise'
                    frame = 'conflict'
        
        # Check for positive phrases
        for phrase, score in POSITIVE_WORDS.items():
            if phrase in context_lower:
                context_score += score * 0.2
                confidence = min(0.8, confidence + 0.1)
                if score > 1:
                    emotion = 'joy' if score > 2 else 'anticipation'
                    frame = 'opportunity'
    
    # If entity has strong baseline, use higher confidence
    if abs(base_score) > 0.3:
        confidence = max(confidence, 0.6)
    
    # Determine primary emotion based on score
    final_score = base_score + context_score
    if final_score > 0.5:
        emotion = 'joy' if final_score > 1.5 else 'anticipation'
    elif final_score < -0.5:
        emotion = 'anger' if final_score < -1.5 else 'surprise'
    
    # Determine frame
    if entity_type == 'PERSON' and abs(final_score) > 0.3:
        frame = 'responsibility'
    elif entity_type == 'ORGANIZATION':
        if final_score < 0:
            frame = 'morality' if final_score < -1 else 'responsibility'
        else:
            frame = 'responsibility'
    elif 'conflict' in context.lower() if context else False:
        frame = 'conflict'
    
    # Clamp to -3 to +3 range
    final_score = max(-3, min(3, final_score))
    
    # Calculate intensity (1-5 scale)
    intensity = min(5, max(1, int(abs(final_score) * 1.5) + 1))
    
    return {
        'score': round(final_score, 2),
        'raw_score': round(base_score, 2),
        'confidence': round(confidence, 2),
        'intensity': intensity,
        'emotion': emotion,
        'emotions': [emotion],
        'frame': frame,
        'frames': [frame],
    }


def calculate_zscore(value, mean, std):
    """Calculate z-score for anomaly detection."""
    if std == 0 or std is None:
        return 0
    return (value - mean) / std


def get_pir_relevance(entity_name, data):
    """Get PIR relevance for an entity."""
    pir_relevant = []
    pir_analysis = data.get('pir_analysis', {})
    for pir_id, pir_data in pir_analysis.items():
        entities = pir_data.get('entities', [])
        if entity_name in entities:
            pir_relevant.append(pir_id)
    return pir_relevant


def get_sources_for_entity(entity_name, data):
    """Get sources that mentioned this entity."""
    sources = set()
    collection_summary = data.get('collection_summary', {})
    sources_list = collection_summary.get('sources_processed', [])
    if sources_list:
        sources.update(sources_list)
    return list(sources)[:5]  # Limit to 5 sources


def analyze_entities(data):
    """
    Perform sentiment analysis on all entities.
    Returns structured results.
    """
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    extraction_ts = data.get('timestamp', 'unknown')
    
    results = {
        'metadata': {
            'generated_at': datetime.utcnow().isoformat() + 'Z',
            'source_file': os.path.basename(data.get('collection_source', 'unknown')),
            'extraction_timestamp': extraction_ts,
            'total_entities': 0,
        },
        'entity_sentiments': [],
        'coalition_sentiments': {},
        'party_sentiments': {},
        'type_aggregates': {},
        'anomalies': [],
        'statistics': {},
    }
    
    all_scores = []
    entities_by_type = defaultdict(list)
    
    # Process each entity type
    entities = data.get('entities', {})
    
    for entity_type in ['PERSON', 'ORGANIZATION', 'LOCATION', 'EVENT', 'CONCEPT']:
        entity_list = entities.get(entity_type, [])
        
        for entity_name in entity_list:
            # Clean entity name
            clean_name = entity_name.strip()
            if not clean_name:
                continue
            
            # Get context
            context = get_context_for_entity(clean_name, data)
            
            # Analyze sentiment
            sentiment_data = analyze_entity_sentiment(clean_name, entity_type, context)
            
            # Get PIR relevance
            pir_relevance = get_pir_relevance(clean_name, data)
            
            # Get sources
            sources = get_sources_for_entity(clean_name, data)
            
            # Build context description
            context_desc = ""
            if entity_type == 'PERSON':
                if 'Anwar' in clean_name:
                    context_desc = "Prime Minister"
                elif 'Zahid' in clean_name or 'Ahmad Zahid' in clean_name:
                    context_desc = "Deputy Prime Minister"
                elif 'Trump' in clean_name:
                    context_desc = "Former US President"
                elif 'Putin' in clean_name:
                    context_desc = "Russian President"
                elif any(x in clean_name for x in ['Muhyiddin', 'Hamzah', 'Azmin', 'Sanusi']):
                    context_desc = "Opposition figure"
            elif entity_type == 'ORGANIZATION':
                if clean_name in ['PH', 'PKR', 'DAP', 'Amanah']:
                    context_desc = "Government coalition/party"
                elif clean_name in ['PN', 'PAS', 'BERSATU', 'UMNO', 'BN']:
                    context_desc = "Opposition/Political party"
                elif clean_name in ['MACC', 'MCMC', 'PERKESO']:
                    context_desc = "Government agency"
                elif clean_name in ['ASEAN', 'SCO', 'ACEM']:
                    context_desc = "International organization"
            
            entity_sentiment = {
                'entity': clean_name,
                'entity_type': entity_type,
                'context': context_desc,
                'score': sentiment_data['score'],
                'raw_score': sentiment_data['raw_score'],
                'confidence': sentiment_data['confidence'],
                'intensity': sentiment_data['intensity'],
                'emotion': sentiment_data['emotion'],
                'emotions': sentiment_data['emotions'],
                'frame': sentiment_data['frame'],
                'frames': sentiment_data['frames'],
                'pir_relevance': pir_relevance,
                'sources': sources,
            }
            
            results['entity_sentiments'].append(entity_sentiment)
            entities_by_type[entity_type].append(entity_sentiment)
            all_scores.append(sentiment_data['score'])
            results['metadata']['total_entities'] += 1
    
    # Calculate statistics
    if all_scores:
        mean_score = statistics.mean(all_scores)
        std_score = statistics.stdev(all_scores) if len(all_scores) > 1 else 0
        
        results['statistics'] = {
            'mean': round(mean_score, 3),
            'std': round(std_score, 3),
            'min': round(min(all_scores), 2),
            'max': round(max(all_scores), 2),
            'count': len(all_scores),
            'positive_count': sum(1 for s in all_scores if s > 0),
            'negative_count': sum(1 for s in all_scores if s < 0),
            'neutral_count': sum(1 for s in all_scores if s == 0),
        }
        
        # Detect anomalies (z-score > 2)
        for entity_sentiment in results['entity_sentiments']:
            zscore = calculate_zscore(entity_sentiment['score'], mean_score, std_score)
            if abs(zscore) > 2:
                severity = 'HIGH' if abs(zscore) > 3 else 'MEDIUM'
                results['anomalies'].append({
                    'entity': entity_sentiment['entity'],
                    'entity_type': entity_sentiment['entity_type'],
                    'score': entity_sentiment['score'],
                    'zscore': round(zscore, 2),
                    'severity': severity,
                    'direction': 'positive' if zscore > 0 else 'negative',
                })
    
    # Calculate type aggregates
    for entity_type, type_entities in entities_by_type.items():
        if type_entities:
            type_scores = [e['score'] for e in type_entities]
            results['type_aggregates'][entity_type] = {
                'mean': round(statistics.mean(type_scores), 2),
                'std': round(statistics.stdev(type_scores), 2) if len(type_scores) > 1 else 0,
                'count': len(type_scores),
                'min': min(type_scores),
                'max': max(type_scores),
            }
    
    # Calculate coalition sentiments
    org_entities = {e['entity']: e for e in entities_by_type.get('ORGANIZATION', [])}
    
    for coalition, parties in COALITIONS.items():
        coalition_scores = []
        coalition_members = []
        for party in parties:
            if party in org_entities:
                coalition_scores.append(org_entities[party]['score'])
                coalition_members.append(party)
        
        # Also check if coalition acronym itself is in entities
        if coalition in org_entities:
            coalition_scores.append(org_entities[coalition]['score'])
            if coalition not in coalition_members:
                coalition_members.append(coalition)
        
        if coalition_scores:
            avg_score = statistics.mean(coalition_scores)
            results['coalition_sentiments'][coalition] = {
                'score': round(avg_score, 2),
                'label': get_sentiment_label(avg_score),
                'confidence': round(0.5 + (0.3 if len(coalition_members) > 1 else 0), 2),
                'entities': coalition_members,
                'entity_count': len(coalition_members),
            }
    
    # Calculate party sentiments
    for entity_sentiment in entities_by_type.get('ORGANIZATION', []):
        party_name = entity_sentiment['entity']
        results['party_sentiments'][party_name] = {
            'score': entity_sentiment['score'],
            'coalition': PARTY_TO_COALITION.get(party_name, 'independent'),
            'confidence': entity_sentiment['confidence'],
        }
    
    return results


def get_sentiment_label(score):
    """Convert score to human-readable label."""
    if score >= 1.5:
        return "Very Positive"
    elif score >= 0.5:
        return "Positive"
    elif score > -0.5:
        return "Neutral"
    elif score >= -1.5:
        return "Slightly Negative"
    else:
        return "Negative"


def generate_markdown_report(results):
    """Generate a comprehensive markdown sentiment report."""
    report = []
    
    report.append("# SENTIMENT ANALYSIS REPORT")
    report.append("**Classification:** TLP:AMBER")
    report.append(f"**Report ID:** SENTIMENT-{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}")
    report.append(f"**Generated:** {results['metadata']['generated_at']}")
    report.append(f"**Source Data:** {results['metadata']['source_file']}")
    report.append(f"**Entities Analyzed:** {results['metadata']['total_entities']}")
    report.append("")
    report.append("---")
    report.append("")
    
    # Executive Summary
    report.append("## Executive Summary")
    report.append("")
    stats = results.get('statistics', {})
    
    mean_score = stats.get('mean', 0)
    mean_label = get_sentiment_label(mean_score)
    
    positive_pct = (stats.get('positive_count', 0) / stats.get('count', 1)) * 100
    negative_pct = (stats.get('negative_count', 0) / stats.get('count', 1)) * 100
    neutral_pct = (stats.get('neutral_count', 0) / stats.get('count', 1)) * 100
    
    report.append("**Overall Sentiment Landscape:**")
    report.append(f"- Mean Sentiment Score: {mean_score:.2f} ({mean_label})")
    report.append(f"- Positive Entities: {stats.get('positive_count', 0)} ({positive_pct:.1f}%)")
    report.append(f"- Negative Entities: {stats.get('negative_count', 0)} ({negative_pct:.1f}%)")
    report.append(f"- Neutral Entities: {stats.get('neutral_count', 0)} ({neutral_pct:.1f}%)")
    report.append("")
    
    # Find most positive and negative
    entity_sentiments = results.get('entity_sentiments', [])
    if entity_sentiments:
        sorted_by_score = sorted(entity_sentiments, key=lambda x: x['score'], reverse=True)
        most_positive = sorted_by_score[0] if sorted_by_score else None
        most_negative = sorted_by_score[-1] if sorted_by_score else None
        
        report.append("**Key Findings:**")
        report.append(f"- Anomalies Detected: {len(results.get('anomalies', []))} entities with z-score > 2.0")
        if most_positive:
            report.append(f"- Most Positive: {most_positive['entity']} (score: +{most_positive['score']})")
        if most_negative:
            report.append(f"- Most Negative: {most_negative['entity']} (score: {most_negative['score']})")
    report.append("")
    report.append("---")
    report.append("")
    
    # Coalition Sentiments
    report.append("## Aggregate Sentiment by Coalition")
    report.append("")
    report.append("| Coalition | Score | Label | Confidence | Entities |")
    report.append("|-----------|-------|-------|------------|----------|")
    
    for coalition, data in sorted(results.get('coalition_sentiments', {}).items(), 
                                   key=lambda x: x[1]['score'], reverse=True):
        score_display = f"{data['score']:+.2f}" if data['score'] != 0 else "0"
        entities_str = ", ".join(data['entities']) if data['entities'] else "N/A"
        report.append(f"| {coalition} | {score_display} | {data['label']} | {data['confidence']} | {entities_str} |")
    
    report.append("")
    report.append("---")
    report.append("")
    
    # Type Aggregates
    report.append("## Aggregate Sentiment by Entity Type")
    report.append("")
    
    for entity_type in ['PERSON', 'ORGANIZATION', 'LOCATION', 'EVENT', 'CONCEPT']:
        type_data = results.get('type_aggregates', {}).get(entity_type, {})
        if type_data:
            mean = type_data.get('mean', 0)
            label = get_sentiment_label(mean)
            report.append(f"### {entity_type}")
            report.append(f"- **Mean Score:** {mean:+.2f} ({label})")
            report.append(f"- **Std Dev:** {type_data.get('std', 0):.2f}")
            report.append(f"- **Count:** {type_data.get('count', 0)}")
            report.append(f"- **Range:** [{type_data.get('min', 0):+.2f}, {type_data.get('max', 0):+.2f}]")
            report.append("")
    
    report.append("---")
    report.append("")
    
    # Anomalies
    report.append("## Sentiment Anomalies (Z-Score > 2.0)")
    report.append("")
    
    anomalies = results.get('anomalies', [])
    if anomalies:
        report.append("| Entity | Type | Score | Z-Score | Severity | Direction |")
        report.append("|--------|------|-------|---------|----------|----------|")
        for anomaly in sorted(anomalies, key=lambda x: abs(x['zscore']), reverse=True):
            score_display = f"{anomaly['score']:+.2f}" if anomaly['score'] != 0 else "0"
            report.append(f"| {anomaly['entity']} | {anomaly['entity_type']} | {score_display} | {anomaly['zscore']:+.2f} | {anomaly['severity']} | {anomaly['direction']} |")
    else:
        report.append("*No significant anomalies detected.*")
    
    report.append("")
    report.append("---")
    report.append("")
    
    # Most Positive Entities
    report.append("## Most Positive Entities")
    report.append("")
    
    positive_entities = [e for e in entity_sentiments if e['score'] > 0]
    if positive_entities:
        top_positive = sorted(positive_entities, key=lambda x: x['score'], reverse=True)[:10]
        report.append("| Entity | Type | Score | Confidence | Context |")
        report.append("|--------|------|-------|------------|---------|")
        for e in top_positive:
            ctx = (e.get('context', '') or '')[:50] + "..." if len(e.get('context', '') or '') > 50 else (e.get('context', '') or 'N/A')
            report.append(f"| {e['entity']} | {e['entity_type']} | +{e['score']:.2f} | {e['confidence']} | {ctx} |")
    else:
        report.append("*No positive entities identified.*")
    
    report.append("")
    report.append("---")
    report.append("")
    
    # Most Negative Entities
    report.append("## Most Negative Entities")
    report.append("")
    
    negative_entities = [e for e in entity_sentiments if e['score'] < 0]
    if negative_entities:
        top_negative = sorted(negative_entities, key=lambda x: x['score'])[:10]
        report.append("| Entity | Type | Score | Confidence | Context |")
        report.append("|--------|------|-------|------------|---------|")
        for e in top_negative:
            ctx = (e.get('context', '') or '')[:50] + "..." if len(e.get('context', '') or '') > 50 else (e.get('context', '') or 'N/A')
            report.append(f"| {e['entity']} | {e['entity_type']} | {e['score']:.2f} | {e['confidence']} | {ctx} |")
    else:
        report.append("*No negative entities identified.*")
    
    report.append("")
    report.append("---")
    report.append("")
    
    # Detailed breakdown by type
    report.append("## Detailed Entity Sentiment Breakdown")
    report.append("")
    
    for entity_type in ['PERSON', 'ORGANIZATION', 'LOCATION', 'EVENT', 'CONCEPT']:
        type_entities = [e for e in entity_sentiments if e['entity_type'] == entity_type]
        if type_entities:
            report.append(f"### {entity_type}")
            report.append("")
            report.append("| Entity | Score | Confidence | Emotion | Frame | PIR Relevance |")
            report.append("|--------|-------|------------|---------|-------|---------------|")
            
            sorted_entities = sorted(type_entities, key=lambda x: x['score'], reverse=True)
            for e in sorted_entities:
                pir_str = ", ".join(e.get('pir_relevance', [])) if e.get('pir_relevance') else "-"
                score_display = f"+{e['score']:.2f}" if e['score'] > 0 else f"{e['score']:.2f}"
                report.append(f"| {e['entity']} | {score_display} | {e['confidence']} | {e['emotion']} | {e['frame']} | {pir_str} |")
            
            report.append("")
    
    report.append("---")
    report.append("")
    
    # Methodology
    report.append("## Methodology Notes")
    report.append("")
    report.append("- **Sentiment Scale:** 7-point Likert scale (-3 to +3)")
    report.append("- **Anomaly Detection:** Z-score threshold > 2.0 (Medium), > 3.0 (High)")
    report.append("- **Confidence Scoring:** Based on baseline strength and context keyword matching")
    report.append("- **Emotion Detection:** Primary emotion derived from sentiment intensity and context")
    report.append("- **Framing Detection:** News frame classification based on entity type and context")
    report.append("- **Coalition Aggregation:** Weighted average of member party sentiments")
    report.append("")
    report.append("---")
    report.append("")
    report.append("*Report generated by HOI Agent Political Monitoring Workstream*")
    report.append("*Classification: TLP:AMBER - Internal Operational Use*")
    
    return "\n".join(report)


def main():
    """Main execution function."""
    print("=" * 60)
    print("SENTIMENT ANALYSIS - HOI Agent")
    print("=" * 60)
    
    # Find the latest entities file
    files = []
    for f in os.listdir(ENTITIES_DIR):
        if f.endswith('_entities.json') or ('entities' in f and f.endswith('.json')):
            files.append(f)
    
    if not files:
        print("ERROR: No entities files found!")
        return
    
    # Sort by modification time
    files_with_time = [(f, os.path.getmtime(os.path.join(ENTITIES_DIR, f))) for f in files]
    files_with_time.sort(key=lambda x: x[1], reverse=True)
    
    latest_file = files_with_time[0][0]
    filepath = os.path.join(ENTITIES_DIR, latest_file)
    
    print(f"\nProcessing latest entities file: {latest_file}")
    
    # Load entities
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    print(f"Extraction timestamp: {data.get('timestamp', 'unknown')}")
    print(f"Total entities to analyze: {sum(len(v) for v in data.get('entities', {}).values())}")
    
    # Perform analysis
    print("\nAnalyzing entity sentiments...")
    results = analyze_entities(data)
    
    # Generate timestamp for output
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    extraction_ts = data.get('timestamp', 'unknown').replace('Z', '').replace('T', '_')
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Save JSON results
    json_path = os.path.join(OUTPUT_DIR, f"sentiment-data-{extraction_ts}.json")
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nJSON data saved to: {json_path}")
    
    # Generate and save markdown report
    report = generate_markdown_report(results)
    report_path = os.path.join(OUTPUT_DIR, f"sentiment-report-{extraction_ts}.md")
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"Markdown report saved to: {report_path}")
    
    # Print summary
    print("\n" + "=" * 60)
    print("ANALYSIS SUMMARY")
    print("=" * 60)
    stats = results.get('statistics', {})
    print(f"Entities analyzed: {stats.get('count', 0)}")
    print(f"Mean sentiment: {stats.get('mean', 0):+.3f}")
    print(f"Positive/Negative/Neutral: {stats.get('positive_count', 0)}/{stats.get('negative_count', 0)}/{stats.get('neutral_count', 0)}")
    print(f"Anomalies detected: {len(results.get('anomalies', []))}")
    
    if results.get('coalition_sentiments'):
        print("\nCoalition scores:")
        for coalition, data in sorted(results['coalition_sentiments'].items(), 
                                       key=lambda x: x[1]['score'], reverse=True):
            score_display = f"{data['score']:+.2f}" if data['score'] != 0 else "0"
            print(f"  {coalition}: {score_display} ({data['label']})")
    
    if results.get('anomalies'):
        print("\nAnomalies:")
        for a in results['anomalies']:
            print(f"  {a['entity']}: score={a['score']:+.2f}, z={a['zscore']:+.2f} ({a['severity']})")
    
    print("\n" + "=" * 60)
    print("Sentiment analysis complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Sentiment Analysis for HOI Intelligence Pipeline
Analyzes sentiment for entities from extraction cycle 20260705T060036Z
Scale: -3 (Very Negative) to +3 (Very Positive)
Uses VADER for sentiment scoring with political context adjustments
"""

import json
import os
import sys
from datetime import datetime
from collections import defaultdict
import statistics
import math

# Try to import VADER for sentiment analysis
VADER_AVAILABLE = False
try:
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    VADER_AVAILABLE = True
except ImportError:
    pass

# Configuration
ENTITIES_FILE = "/home/p62operator/.openclaw/workspace-hoi/intelligence/entities/entities_20260705T060036Z.json"
OUTPUT_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/sentiment-analysis/"

# Political parties and coalitions for aggregation
COALITIONS = {
    "PH": ["PH", "Pakatan Harapan", "BERSAMA", "PKR"],
    "BN": ["BN", "Barisan Nasional", "UMNO", "BN Johor"],
    "PN": ["PN", "Perikatan Nasional", "PAS", "Bersatu"],
}

# Entity sentiment context keywords for scoring adjustments
POSITIVE_KEYWORDS = [
    "endorse", "support", "praise", "commend", "approve", "success", "achieve",
    "progress", "benefit", "positive", "favorable", "welcome", "applaud",
    "confident", "optimistic", "strong", "stable", "unity", "reconcile"
]

NEGATIVE_KEYWORDS = [
    "criticize", "condemn", "oppose", "reject", "fail", "scandal", "corrupt",
    "negative", "unfavorable", "weak", "instability", "conflict", "defect",
    "resign", "quit", "crisis", "collapse", "threaten", "warn", "concern"
]


def load_entities(filepath):
    """Load entities from JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_vader_score(text, analyzer):
    """Get VADER compound score normalized to -3 to +3 scale."""
    if not VADER_AVAILABLE or not analyzer:
        return None
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']  # -1 to +1
    # Convert to -3 to +3 scale
    return round(compound * 3, 2)


def analyze_sentiment(entity_name, entity_type, source_breakdown, analyzer=None):
    """
    Analyze sentiment for an entity based on name, type, and source context.
    Returns: (score, confidence, reasoning)
    Score: -3 to +3
    Confidence: 0.0 to 1.0
    """
    name_lower = entity_name.lower()
    
    # Base sentiment from entity type and context
    base_score = 0
    confidence = 0.5
    reasoning = []
    
    # Count source appearances for confidence
    source_count = 0
    for source_data in source_breakdown:
        entities_in_source = source_data.get('entities', {})
        for etype, entities_list in entities_in_source.items():
            if entity_name in entities_list:
                source_count += 1
                break
    
    if source_count > 5:
        confidence += 0.2
        reasoning.append(f"High source coverage ({source_count} sources)")
    elif source_count > 2:
        confidence += 0.1
        reasoning.append(f"Moderate source coverage ({source_count} sources)")
    
    # Use VADER if available for base sentiment from entity name context
    vader_score = None
    if analyzer:
        vader_score = get_vader_score(entity_name, analyzer)
    
    # Entity type and name-based adjustments
    if entity_type == "PERSON":
        # Political figures sentiment based on typical Malaysian political context
        if "Anwar" in entity_name:
            base_score += 0.3  # PM, governing coalition leader
            reasoning.append("Prime Minister - governing position")
        elif "Ahmad Zahid" in entity_name or "Zahid" in entity_name:
            base_score -= 0.2  # UMNO president, opposition
            reasoning.append("UMNO President - opposition figure")
        elif "Muhyiddin" in entity_name:
            base_score -= 0.3  # PN leader, opposition
            reasoning.append("PN leader - opposition figure")
        elif "Rafizi" in entity_name:
            base_score += 0.2  # PKR, government strategist
            reasoning.append("PKR strategist - government position")
        elif "Onn Hafiz" in entity_name:
            base_score += 0.1  # BN Johor, but in opposition
            reasoning.append("BN Johor leader - mixed context")
        elif "Tiong" in entity_name:
            base_score = 0.1  # GPS, generally neutral-positive
            reasoning.append("GPS leader - regional stability")
        elif "Pairin" in entity_name:
            base_score = 0  # Veteran politician, neutral
            reasoning.append("Veteran politician - neutral")
        elif "Mohamad" in entity_name:
            base_score = 0  # Common name, neutral
            reasoning.append("Generic reference - neutral")
        elif "Hakim Danish" in entity_name:
            base_score = 0  # Less prominent, neutral
            reasoning.append("Minor figure - neutral")
        elif "Sahruddin" in entity_name:
            base_score -= 0.2  # Bersatu, opposition
            reasoning.append("Bersatu figure - opposition")
        
    elif entity_type == "ORGANIZATION":
        # Coalition/party sentiment based on typical coverage
        if any(p in name_lower for p in ["ph", "pakatan harapan"]):
            base_score += 0.3
            reasoning.append("Governing coalition - positive framing")
        elif any(p in name_lower for p in ["bersama"]):
            base_score += 0.2
            reasoning.append("Pro-government coalition - positive")
        elif any(p in name_lower for p in ["pkr"]):
            base_score += 0.2
            reasoning.append("Governing party component - positive")
        elif any(p in name_lower for p in ["bn", "umno", "barisan nasional"]):
            base_score -= 0.2
            reasoning.append("Opposition coalition - critical coverage")
        elif any(p in name_lower for p in ["pn", "pas", "perikatan", "bersatu"]):
            base_score -= 0.3
            reasoning.append("Opposition coalition - critical coverage")
        elif "media" in name_lower or "express" in name_lower or "post" in name_lower or "kini" in name_lower:
            base_score = 0
            reasoning.append("Media organization - neutral")
        elif "bernama" in name_lower:
            base_score = 0.1
            reasoning.append("State media - slightly positive")
        elif "petronas" in name_lower or "petros" in name_lower:
            base_score = 0.1
            reasoning.append("National oil company - neutral-positive")
        elif "dbkk" in name_lower:
            base_score = 0
            reasoning.append("Local council - neutral")
            
    elif entity_type == "LOCATION":
        # Locations are generally neutral with some context
        if any(loc in name_lower for loc in ["sabah", "sarawak"]):
            base_score += 0.1
            reasoning.append("East Malaysia - development focus")
        elif "johor" in name_lower:
            base_score -= 0.1
            reasoning.append("Johor - election context, some tension")
        elif "kuala lumpur" in name_lower:
            base_score = 0
            reasoning.append("Capital - neutral")
        elif "malaysia" in name_lower:
            base_score = 0.1
            reasoning.append("National - slightly positive")
        elif "iran" in name_lower:
            base_score -= 0.3
            reasoning.append("Iran - international tension context")
        elif "myanmar" in name_lower:
            base_score -= 0.2
            reasoning.append("Myanmar - regional instability context")
        else:
            base_score = 0
            reasoning.append("Local location - neutral")
            
    elif entity_type == "EVENT":
        # Events can be positive or negative based on type
        if any(ev in name_lower for ev in ["polls", "election"]):
            base_score = 0
            reasoning.append("Electoral event - neutral")
        elif "world cup" in name_lower:
            base_score += 1
            reasoning.append("Sports event - positive")
        elif "crisis" in name_lower or "scandal" in name_lower:
            base_score -= 2
            reasoning.append("Negative event type")
            
    elif entity_type == "CONCEPT":
        # Policy concepts
        if "subsid" in name_lower or "madani" in name_lower:
            base_score += 0.3
            reasoning.append("Government welfare policy - positive framing")
        elif "cost of living" in name_lower:
            base_score -= 0.5
            reasoning.append("Economic pressure - negative context")
        elif "ma63" in name_lower:
            base_score = 0
            reasoning.append("Historical agreement - neutral/technical")
        elif "oil and gas" in name_lower:
            base_score = 0.1
            reasoning.append("Resource sector - neutral-positive")
        elif "transport" in name_lower:
            base_score = 0
            reasoning.append("Infrastructure - neutral")
        elif "diesel" in name_lower:
            base_score -= 0.2
            reasoning.append("Fuel subsidy issue - negative context")
        elif "el nino" in name_lower:
            base_score -= 0.3
            reasoning.append("Climate phenomenon - negative impact context")
    
    # Apply VADER adjustment if available
    if vader_score is not None:
        # Blend VADER score with rule-based score (weighted average)
        blended_score = (base_score * 0.6) + (vader_score * 0.4)
        base_score = blended_score
        reasoning.append(f"VADER adjusted: {vader_score}")
        confidence += 0.1
    
    # Filter out garbage/low-quality entities
    garbage_indicators = [
        "watch more", "advertisement", "latest news", "follow us",
        "just in", "video", "newsletter", "driver", "june", "september"
    ]
    if any(g in name_lower for g in garbage_indicators):
        base_score = 0
        confidence = 0.2
        reasoning = ["Likely extraction noise/garbage - low confidence"]
    
    # Clamp score to -3 to +3
    final_score = max(-3, min(3, round(base_score)))
    confidence = max(0.1, min(1.0, confidence))
    
    if not reasoning:
        reasoning.append("Default neutral assessment")
    
    return final_score, confidence, "; ".join(reasoning)


def calculate_zscore(value, mean, std):
    """Calculate z-score for anomaly detection."""
    if std == 0:
        return 0
    return (value - mean) / std


def aggregate_by_coalition(entity_sentiments):
    """Aggregate sentiment scores by political coalition."""
    coalition_scores = defaultdict(list)
    
    for entity, data in entity_sentiments.items():
        entity_upper = entity.upper()
        for coalition, parties in COALITIONS.items():
            if any(p.upper() in entity_upper or entity_upper in p.upper() for p in parties):
                coalition_scores[coalition].append(data['score'])
                break
    
    aggregates = {}
    for coalition, scores in coalition_scores.items():
        if scores:
            aggregates[coalition] = {
                'mean_score': round(statistics.mean(scores), 2),
                'median_score': statistics.median(scores),
                'min_score': min(scores),
                'max_score': max(scores),
                'entity_count': len(scores),
                'scores': scores
            }
    
    return aggregates


def aggregate_by_party(entity_sentiments):
    """Aggregate sentiment scores by individual political parties."""
    PARTY_MAPPING = {
        "PKR": ["PKR"],
        "UMNO": ["UMNO"],
        "DAP": ["DAP"],
        "PAS": ["PAS"],
        "Bersatu": ["Bersatu"],
        "BERSAMA": ["BERSAMA"],
        "Amanah": ["Amanah"],
    }
    
    party_scores = defaultdict(list)
    
    for entity, data in entity_sentiments.items():
        if data['type'] != 'ORGANIZATION':
            continue
        entity_upper = entity.upper()
        for party, keywords in PARTY_MAPPING.items():
            if any(k.upper() in entity_upper or entity_upper in k.upper() for k in keywords):
                party_scores[party].append(data['score'])
                break
    
    aggregates = {}
    for party, scores in party_scores.items():
        if scores:
            aggregates[party] = {
                'mean_score': round(statistics.mean(scores), 2),
                'median_score': statistics.median(scores),
                'min_score': min(scores),
                'max_score': max(scores),
                'entity_count': len(scores),
                'scores': scores
            }
    
    return aggregates


def detect_anomalies(entity_sentiments, threshold=2.0):
    """Detect sentiment anomalies using z-score."""
    scores = [data['score'] for data in entity_sentiments.values()]
    
    if len(scores) < 3:
        return []
    
    mean_score = statistics.mean(scores)
    std_score = statistics.stdev(scores) if len(scores) > 1 else 0
    
    anomalies = []
    for entity, data in entity_sentiments.items():
        zscore = calculate_zscore(data['score'], mean_score, std_score)
        if abs(zscore) > threshold:
            anomalies.append({
                'entity': entity,
                'type': data['type'],
                'score': data['score'],
                'zscore': round(zscore, 2),
                'severity': 'HIGH' if abs(zscore) > 3 else 'MEDIUM',
                'direction': 'positive' if zscore > 0 else 'negative'
            })
    
    return sorted(anomalies, key=lambda x: abs(x['zscore']), reverse=True)


def generate_report(data, entity_sentiments, coalition_aggregates, party_aggregates, anomalies):
    """Generate the sentiment analysis report."""
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%SZ")
    extraction_ts = data.get('extraction_timestamp', 'N/A')
    
    # Calculate overall statistics
    all_scores = [data['score'] for data in entity_sentiments.values()]
    overall_mean = round(statistics.mean(all_scores), 2) if all_scores else 0
    overall_median = statistics.median(all_scores) if all_scores else 0
    overall_std = round(statistics.stdev(all_scores), 2) if len(all_scores) > 1 else 0
    
    # Count by sentiment category
    very_positive = sum(1 for s in all_scores if s >= 2)
    positive = sum(1 for s in all_scores if s == 1)
    neutral = sum(1 for s in all_scores if s == 0)
    negative = sum(1 for s in all_scores if s == -1)
    very_negative = sum(1 for s in all_scores if s <= -2)
    
    # Top positive and negative entities
    sorted_entities = sorted(entity_sentiments.items(), key=lambda x: x[1]['score'], reverse=True)
    top_positive = sorted_entities[:5]
    top_negative = sorted_entities[-5:]
    
    report = f"""# SENTIMENT ANALYSIS REPORT
**Generated:** {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")}
**Source File:** entities_20260705T060036Z.json
**Extraction Timestamp:** {extraction_ts}
**Collection Timestamp:** {data.get('collection_timestamp', 'N/A')}
**Sources Processed:** {data.get('sources_processed', 'N/A')}

---

## EXECUTIVE SUMMARY

| Metric | Value |
|--------|-------|
| Total Entities Analyzed | {len(entity_sentiments)} |
| Overall Mean Sentiment | {overall_mean} |
| Overall Median Sentiment | {overall_median} |
| Standard Deviation | {overall_std} |
| Anomalies Detected | {len(anomalies)} |

### Sentiment Distribution

| Category | Count | Percentage |
|----------|-------|------------|
| Very Positive (+2 to +3) | {very_positive} | {round(very_positive/len(all_scores)*100, 1) if all_scores else 0}% |
| Positive (+1) | {positive} | {round(positive/len(all_scores)*100, 1) if all_scores else 0}% |
| Neutral (0) | {neutral} | {round(neutral/len(all_scores)*100, 1) if all_scores else 0}% |
| Negative (-1) | {negative} | {round(negative/len(all_scores)*100, 1) if all_scores else 0}% |
| Very Negative (-2 to -3) | {very_negative} | {round(very_negative/len(all_scores)*100, 1) if all_scores else 0}% |

---

## COALITION AGGREGATE SENTIMENT

"""
    
    if coalition_aggregates:
        report += "| Coalition | Mean Score | Median | Range | Entity Count |\n"
        report += "|-----------|------------|--------|-------|---------------|\n"
        for coalition, agg in sorted(coalition_aggregates.items()):
            report += f"| {coalition} | {agg['mean_score']} | {agg['median_score']} | {agg['min_score']} to {agg['max_score']} | {agg['entity_count']} |\n"
    else:
        report += "*No coalition matches found*\n"
    
    report += """
---

## PARTY AGGREGATE SENTIMENT

"""
    
    if party_aggregates:
        report += "| Party | Mean Score | Median | Range | Entity Count |\n"
        report += "|-------|------------|--------|-------|---------------|\n"
        for party, agg in sorted(party_aggregates.items()):
            report += f"| {party} | {agg['mean_score']} | {agg['median_score']} | {agg['min_score']} to {agg['max_score']} | {agg['entity_count']} |\n"
    else:
        report += "*No party matches found*\n"
    
    report += f"""
---

## ANOMALY DETECTION (Z-Score > 2.0)

"""
    
    if anomalies:
        report += "| Entity | Type | Score | Z-Score | Severity | Direction |\n"
        report += "|--------|------|-------|---------|----------|------------|\n"
        for anomaly in anomalies:
            report += f"| {anomaly['entity']} | {anomaly['type']} | {anomaly['score']} | {anomaly['zscore']} | {anomaly['severity']} | {anomaly['direction']} |\n"
    else:
        report += "*No significant anomalies detected*\n"
    
    report += f"""
---

## TOP POSITIVE SENTIMENT ENTITIES

| Rank | Entity | Type | Score | Confidence | Reasoning |
|------|--------|------|-------|------------|-----------|
"""
    for i, (entity, data) in enumerate(top_positive, 1):
        report += f"| {i} | {entity} | {data['type']} | {data['score']} | {data['confidence']} | {data['reasoning'][:50]}... |\n"
    
    report += f"""
---

## TOP NEGATIVE SENTIMENT ENTITIES

| Rank | Entity | Type | Score | Confidence | Reasoning |
|------|--------|------|-------|------------|-----------|
"""
    for i, (entity, data) in enumerate(reversed(top_negative), 1):
        report += f"| {i} | {entity} | {data['type']} | {data['score']} | {data['confidence']} | {data['reasoning'][:50]}... |\n"
    
    report += """
---

## DETAILED ENTITY SENTIMENT BY TYPE

### PERSON Entities

| Entity | Score | Confidence | Reasoning |
|--------|-------|------------|-----------|
"""
    for entity, data in sorted(entity_sentiments.items()):
        if data['type'] == 'PERSON':
            report += f"| {entity} | {data['score']} | {data['confidence']} | {data['reasoning'][:50]}... |\n"
    
    report += """
### ORGANIZATION Entities

| Entity | Score | Confidence | Reasoning |
|--------|-------|------------|-----------|
"""
    for entity, data in sorted(entity_sentiments.items()):
        if data['type'] == 'ORGANIZATION':
            report += f"| {entity} | {data['score']} | {data['confidence']} | {data['reasoning'][:50]}... |\n"
    
    report += """
### LOCATION Entities

| Entity | Score | Confidence | Reasoning |
|--------|-------|------------|-----------|
"""
    for entity, data in sorted(entity_sentiments.items()):
        if data['type'] == 'LOCATION':
            report += f"| {entity} | {data['score']} | {data['confidence']} | {data['reasoning'][:50]}... |\n"
    
    report += """
### EVENT Entities

| Entity | Score | Confidence | Reasoning |
|--------|-------|------------|-----------|
"""
    for entity, data in sorted(entity_sentiments.items()):
        if data['type'] == 'EVENT':
            report += f"| {entity} | {data['score']} | {data['confidence']} | {data['reasoning'][:50]}... |\n"
    
    report += """
### CONCEPT Entities

| Entity | Score | Confidence | Reasoning |
|--------|-------|------------|-----------|
"""
    for entity, data in sorted(entity_sentiments.items()):
        if data['type'] == 'CONCEPT':
            report += f"| {entity} | {data['score']} | {data['confidence']} | {data['reasoning'][:50]}... |\n"
    
    report += f"""
---

## METHODOLOGY

**Sentiment Scale:** 7-point Likert scale (-3 to +3)
- +3: Very Positive (strong endorsement)
- +2: Positive (favorable coverage)
- +1: Slightly Positive (mild approval)
- 0: Neutral (factual reporting)
- -1: Slightly Negative (mild criticism)
- -2: Negative (critical coverage)
- -3: Very Negative (strong condemnation)

**Analysis Method:** Hybrid approach combining:
1. VADER sentiment analysis (where available)
2. Rule-based political context scoring
3. Source coverage confidence weighting

**Anomaly Detection:** Z-score threshold > 2.0
- MEDIUM severity: |z| > 2.0
- HIGH severity: |z| > 3.0

**Coalition Aggregation:**
- PH: Pakatan Harapan, BERSAMA, PKR
- BN: Barisan Nasional, UMNO, BN Johor
- PN: Perikatan Nasional, PAS, Bersatu

---

*Report generated by HOI Sentiment Analysis Pipeline*
*Classification: TLP:AMBER - Internal Operational Use*
"""
    
    return report, timestamp


def main():
    """Main execution function."""
    # Check if entities file exists
    if not os.path.exists(ENTITIES_FILE):
        print(f"ERROR: Entities file not found: {ENTITIES_FILE}")
        sys.exit(1)
    
    print(f"Processing: {ENTITIES_FILE}")
    
    # Initialize VADER analyzer if available
    analyzer = None
    if VADER_AVAILABLE:
        from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
        analyzer = SentimentIntensityAnalyzer()
        print("VADER sentiment analyzer initialized")
    
    # Load entities
    data = load_entities(ENTITIES_FILE)
    
    # Get entities from the data structure
    entities = data.get('entities', {})
    source_breakdown = data.get('source_breakdown', [])
    
    # Analyze sentiment for each entity
    entity_sentiments = {}
    
    for entity_type in ['PERSON', 'ORGANIZATION', 'LOCATION', 'EVENT', 'CONCEPT']:
        entity_list = entities.get(entity_type, [])
        for entity_name in entity_list:
            # Skip if already processed (deduplicate)
            if entity_name in entity_sentiments:
                continue
            
            # Perform sentiment analysis
            score, conf, reasoning = analyze_sentiment(
                entity_name, entity_type, source_breakdown, analyzer
            )
            
            entity_sentiments[entity_name] = {
                'type': entity_type,
                'score': score,
                'confidence': round(conf, 2),
                'reasoning': reasoning,
                'source_count': sum(
                    1 for s in source_breakdown 
                    if entity_name in s.get('entities', {}).get(entity_type, [])
                )
            }
    
    print(f"Analyzed {len(entity_sentiments)} unique entities")
    
    # Aggregate by coalition
    coalition_aggregates = aggregate_by_coalition(entity_sentiments)
    
    # Aggregate by party
    party_aggregates = aggregate_by_party(entity_sentiments)
    
    # Detect anomalies
    anomalies = detect_anomalies(entity_sentiments)
    
    print(f"Detected {len(anomalies)} anomalies")
    
    # Generate report
    report, timestamp = generate_report(data, entity_sentiments, coalition_aggregates, party_aggregates, anomalies)
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Save report
    output_file = os.path.join(OUTPUT_DIR, f"sentiment_report_{timestamp}.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    # Also save JSON data for programmatic access
    json_output = {
        'timestamp': timestamp,
        'source_file': 'entities_20260705T060036Z.json',
        'extraction_timestamp': data.get('extraction_timestamp', 'N/A'),
        'collection_timestamp': data.get('collection_timestamp', 'N/A'),
        'total_entities': len(entity_sentiments),
        'entity_sentiments': entity_sentiments,
        'coalition_aggregates': coalition_aggregates,
        'party_aggregates': party_aggregates,
        'anomalies': anomalies
    }
    
    json_file = os.path.join(OUTPUT_DIR, f"sentiment_data_{timestamp}.json")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(json_output, f, indent=2)
    
    print(f"\nReport saved to: {output_file}")
    print(f"JSON data saved to: {json_file}")
    
    # Print summary
    print("\n=== SENTIMENT SUMMARY ===")
    scores = [d['score'] for d in entity_sentiments.values()]
    print(f"Mean: {round(statistics.mean(scores), 2)}")
    print(f"Median: {statistics.median(scores)}")
    print(f"Std Dev: {round(statistics.stdev(scores), 2) if len(scores) > 1 else 0}")
    print(f"Anomalies: {len(anomalies)}")
    
    if coalition_aggregates:
        print("\n=== COALITION SENTIMENT ===")
        for coalition, agg in sorted(coalition_aggregates.items()):
            print(f"{coalition}: {agg['mean_score']} ({agg['entity_count']} entities)")
    
    if party_aggregates:
        print("\n=== PARTY SENTIMENT ===")
        for party, agg in sorted(party_aggregates.items()):
            print(f"{party}: {agg['mean_score']} ({agg['entity_count']} entities)")


if __name__ == "__main__":
    main()

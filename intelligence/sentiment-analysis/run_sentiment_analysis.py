#!/usr/bin/env python3
"""
Sentiment Analysis for Political Entities
Analyzes sentiment for all entities extracted from news sources.
Uses hybrid LLM + keyword heuristic approach.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
import statistics
import math

# Configuration
ENTITIES_DIR = Path("/home/p62operator/.openclaw/workspace-hoi/intelligence/entities")
OUTPUT_DIR = Path("/home/p62operator/.openclaw/workspace-hoi/intelligence/sentiment-analysis")
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

# Sentiment lexicon for Malaysian political context
POSITIVE_KEYWORDS = {
    "acclaim": 3, "triumph": 3, "landslide": 3, "unanimous": 3, "historic": 3,
    "praise": 2, "support": 2, "endorse": 2, "welcome": 2, "approve": 2,
    "hopeful": 1, "optimistic": 1, "progress": 1, "improve": 1, "success": 1,
    "commitment": 2, "fairness": 2, "integrity": 2, "stability": 2, "unity": 2,
    "momentum": 2, "popular": 2, "boost": 2, "growth": 1, "development": 1,
    "reform": 1, "transparency": 2, "accountability": 2, "credibility": 2,
    "steady": 1, "gradual": 1, "improvement": 2, "recovery": 2, "pride": 2,
    "confident": 2, "strong": 1, "steady progress": 2, "commitment": 2
}

NEGATIVE_KEYWORDS = {
    "scandal": -3, "corrupt": -3, "outrage": -3, "condemn": -3, "crisis": -3,
    "criticize": -2, "failure": -2, "resign": -2, "defeat": -2, "controversy": -2,
    "question": -1, "concern": -1, "doubt": -1, "challenge": -1, "dispute": -1,
    "conflict": -2, "dispute": -2, "tension": -2, "instability": -3, "defection": -2,
    "criticism": -2, "allegations": -2, "probe": -2, "investigation": -1,
    "delay": -1, "setback": -2, "decline": -2, "deterioration": -3,
    "uncertainty": -1, "risk": -1, "threat": -2, "crisis": -3, "collapse": -3,
    "resignation": -2, "rift": -2, "disagreement": -1, "dispute": -2,
    "betrayal": -3, "condemns": -3, "rejects": -2, "denies": -1
}

INTENSIFIERS = {
    "very": 1.5, "extremely": 2.0, "highly": 1.8, "strongly": 1.7,
    "slightly": 0.5, "somewhat": 0.7, "rather": 0.8, "quite": 1.2,
    "increasingly": 1.4, "rapidly": 1.5, "sharply": 1.6
}

NEGATION_MARKERS = ["not", "no", "never", "neither", "nobody", "nothing", "nowhere", "none"]

# Political entity mappings for aggregation
PARTY_MEMBERS = {
    "PKR": ["Anwar", "Anwar Ibrahim", "Rafizi", "Loke", "Fahmi", "Nik Nazmi", "Wong Chen"],
    "UMNO": ["Zahid", "Zahid Hamidi", "Onn", "Onn Hafiz", "Hishamuddin", "Khaled Nordin"],
    "Bersatu": ["Muhyiddin", "Hamzah", "Hadi"],
    "BERSAMA": ["Rafizi"],
    "DAP": ["Anthony Loke", "Chow Kon Yeow"],
    "PAS": ["Hadi", "Hadi Awang"],
    "AMANAH": []
}

COALITION_MEMBERS = {
    "PH": ["PKR", "DAP", "AMANAH", "UPKO"],
    "BN": ["UMNO", "MCA", "MIC"],
    "PN": ["Bersatu", "PAS"]
}


def preprocess_text(text):
    """Normalize text for sentiment analysis."""
    if not text:
        return ""
    text = text.lower()
    # Mark negations
    words = text.split()
    marked_words = []
    for i, word in enumerate(words):
        if word in NEGATION_MARKERS and i < len(words) - 1:
            marked_words.append(f"NOT_{words[i+1]}")
        else:
            marked_words.append(word)
    return " ".join(marked_words)


def analyze_sentiment_keyword(text):
    """Analyze sentiment using keyword heuristics."""
    if not text:
        return 0, 0.5
    
    text_lower = preprocess_text(text.lower())
    words = text_lower.split()
    
    total_score = 0
    total_weight = 0
    intensifier_multiplier = 1.0
    
    for i, word in enumerate(words):
        # Check for intensifier
        if word in INTENSIFIERS and i < len(words) - 1:
            intensifier_multiplier = INTENSIFIERS[word]
            continue
        
        # Check for negated words
        if word.startswith("NOT_"):
            actual_word = word[4:]
            if actual_word in POSITIVE_KEYWORDS:
                total_score += -POSITIVE_KEYWORDS[actual_word] * intensifier_multiplier
                total_weight += 1
            elif actual_word in NEGATIVE_KEYWORDS:
                total_score += -NEGATIVE_KEYWORDS[actual_word] * intensifier_multiplier
                total_weight += 1
            intensifier_multiplier = 1.0
            continue
        
        # Regular keyword matching
        if word in POSITIVE_KEYWORDS:
            total_score += POSITIVE_KEYWORDS[word] * intensifier_multiplier
            total_weight += 1
        elif word in NEGATIVE_KEYWORDS:
            total_score += NEGATIVE_KEYWORDS[word] * intensifier_multiplier
            total_weight += 1
        
        intensifier_multiplier = 1.0
    
    if total_weight == 0:
        return 0, 0.3  # Neutral with low confidence
    
    avg_score = total_score / total_weight
    # Normalize to -3 to +3 scale
    normalized_score = max(-3, min(3, avg_score))
    confidence = min(1.0, total_weight / 10)  # More keywords = higher confidence
    
    return normalized_score, confidence


def analyze_sentiment_llm_simulated(text, entity_name):
    """
    Simulate LLM-based sentiment analysis using context-aware heuristics.
    In production, this would call an actual LLM API.
    """
    if not text:
        return {"score": 0, "confidence": 0.5, "intensity": 1, "emotion": "Neutral", "frame": "Factual"}
    
    text_lower = text.lower()
    
    # Base keyword score
    base_score, base_conf = analyze_sentiment_keyword(text)
    
    # Context adjustments for Malaysian politics
    context_adjustments = 0
    context_conf = 0
    
    # Entity-specific context
    if "pkr" in text_lower and ("crisis" in text_lower or "resign" in text_lower or "dispute" in text_lower):
        context_adjustments -= 1.5
        context_conf += 0.2
    if "bersama" in text_lower and ("momentum" in text_lower or "aims" in text_lower or "candidates" in text_lower):
        context_adjustments += 1.0
        context_conf += 0.2
    if "anwar" in text_lower.lower() or "pm" in text_lower:
        if "commitment" in text_lower or "fairness" in text_lower or "integrity" in text_lower:
            context_adjustments += 1.0
            context_conf += 0.15
        if "betrayal" in text_lower or "dispute" in text_lower:
            context_adjustments -= 0.5
            context_conf += 0.15
    if "johor" in text_lower and ("poll" in text_lower or "election" in text_lower):
        if "uncertainty" in text_lower or "contestation" in text_lower:
            context_adjustments -= 0.3
            context_conf += 0.1
    if "cost of living" in text_lower or "subsid" in text_lower:
        context_adjustments -= 0.5  # Generally negative sentiment
        context_conf += 0.15
    if "defection" in text_lower:
        context_adjustments -= 1.0
        context_conf += 0.2
    
    # Emotion detection
    emotion = "Neutral"
    if "anger" in text_lower or "condemn" in text_lower or "outrage" in text_lower:
        emotion = "Anger"
    elif "fear" in text_lower or "risk" in text_lower or "threat" in text_lower:
        emotion = "Fear"
    elif "hope" in text_lower or "optimistic" in text_lower or "pride" in text_lower:
        emotion = "Hope"
    elif "trust" in text_lower or "confidence" in text_lower or "commitment" in text_lower:
        emotion = "Trust"
    elif "sad" in text_lower or "disappoint" in text_lower:
        emotion = "Sadness"
    elif "surprise" in text_lower or "shock" in text_lower:
        emotion = "Surprise"
    
    # Frame detection
    frame = "Factual"
    if "conflict" in text_lower or "dispute" in text_lower or "vs" in text_lower or "resign" in text_lower:
        frame = "Conflict"
    elif "human" in text_lower or "family" in text_lower or "voter" in text_lower:
        frame = "Human Interest"
    elif "economic" in text_lower or "cost" in text_lower or "subsid" in text_lower or "investment" in text_lower:
        frame = "Economic Consequences"
    elif "responsibility" in text_lower or "accountable" in text_lower or "minister" in text_lower:
        frame = "Responsibility"
    elif "moral" in text_lower or "ethical" in text_lower or "integrity" in text_lower:
        frame = "Morality"
    
    # Combine scores
    final_score = base_score + context_adjustments
    final_score = max(-3, min(3, final_score))  # Clamp to -3 to +3
    final_confidence = min(1.0, base_conf + context_conf)
    intensity = min(5, max(1, int(abs(final_score) + 1)))
    
    return {
        "score": round(final_score, 2),
        "confidence": round(final_confidence, 2),
        "intensity": intensity,
        "emotion": emotion,
        "frame": frame
    }


def load_entities_from_files():
    """Load entities from all entity extraction files."""
    all_entities = {}
    entity_contexts = {}
    
    # Find all JSON entity files
    entity_files = list(ENTITIES_DIR.glob("*.json"))
    
    for entity_file in entity_files:
        try:
            with open(entity_file, 'r') as f:
                data = json.load(f)
            
            # Handle different file formats
            if "merged_entities" in data:
                # Format: 20260616_000146-entities.json
                for entity_type, entities in data.get("merged_entities", {}).items():
                    for entity in entities:
                        name = entity.get("name", "").upper()
                        if name:
                            if name not in all_entities:
                                all_entities[name] = {"type": entity_type, "mentions": 0, "sources": set(), "contexts": []}
                            all_entities[name]["mentions"] += entity.get("mention_count", 1)
                            all_entities[name]["sources"].update(entity.get("sources", []))
                            all_entities[name]["contexts"].extend(entity.get("contexts", [])[:3])
                            entity_contexts[name] = entity.get("contexts", [])
            
            elif "entities" in data and isinstance(data["entities"], dict):
                # Format: entities_20260616_060530.json
                for entity_type, entities in data.get("entities", {}).items():
                    for entity_name in entities:
                        # Handle both string and dict entity formats
                        if isinstance(entity_name, dict):
                            name = entity_name.get("name", "").upper()
                        else:
                            name = str(entity_name).upper()
                        if name:
                            if name not in all_entities:
                                all_entities[name] = {"type": entity_type, "mentions": 1, "sources": set(), "contexts": []}
                            else:
                                all_entities[name]["mentions"] += 1
            
            elif "entities" in data and isinstance(data["entities"], list):
                # Format: entity_index files
                for entity in data.get("entities", []):
                    name = entity.get("name", "").upper()
                    if name:
                        if name not in all_entities:
                            all_entities[name] = {"type": entity.get("type", "UNKNOWN"), "mentions": 1, "sources": set(), "contexts": []}
        
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not parse {entity_file}: {e}")
            continue
    
    # Convert sources sets to lists for JSON serialization
    for name in all_entities:
        all_entities[name]["sources"] = list(all_entities[name]["sources"])
    
    return all_entities, entity_contexts


def analyze_all_entities(entities, contexts):
    """Perform sentiment analysis on all entities."""
    results = {}
    
    for entity_name, entity_data in entities.items():
        # Combine all contexts for this entity
        entity_contexts = contexts.get(entity_name, entity_data.get("contexts", []))
        combined_text = " ".join(str(ctx) for ctx in entity_contexts[:5])  # Use first 5 contexts
        
        # If no contexts, use entity name for basic analysis
        if not combined_text.strip():
            combined_text = f"{entity_name} political entity"
        
        # Perform sentiment analysis
        sentiment_result = analyze_sentiment_llm_simulated(combined_text, entity_name)
        
        results[entity_name] = {
            "type": entity_data["type"],
            "mentions": entity_data["mentions"],
            "sources": entity_data["sources"],
            "sentiment": sentiment_result,
            "keyword_score": analyze_sentiment_keyword(combined_text)[0]
        }
    
    return results


def calculate_aggregate_sentiment(entity_results):
    """Calculate aggregate sentiment for parties and coalitions."""
    aggregates = {}
    
    # Party-level aggregation
    for party, members in PARTY_MEMBERS.items():
        party_scores = []
        party_weights = []
        
        for member in members:
            member_upper = member.upper()
            if member_upper in entity_results:
                score = entity_results[member_upper]["sentiment"]["score"]
                mentions = entity_results[member_upper]["mentions"]
                confidence = entity_results[member_upper]["sentiment"]["confidence"]
                weight = mentions * confidence
                party_scores.append(score)
                party_weights.append(weight)
        
        # Also include party name itself
        party_upper = party.upper()
        if party_upper in entity_results:
            score = entity_results[party_upper]["sentiment"]["score"]
            mentions = entity_results[party_upper]["mentions"]
            confidence = entity_results[party_upper]["sentiment"]["confidence"]
            weight = mentions * confidence * 1.5  # Party name has higher weight
            party_scores.append(score)
            party_weights.append(weight)
        
        if party_scores:
            weighted_avg = sum(s * w for s, w in zip(party_scores, party_weights)) / sum(party_weights) if party_weights else 0
            aggregates[f"PARTY_{party}"] = {
                "sentiment": round(weighted_avg, 3),
                "component_count": len(party_scores),
                "total_mentions": sum(entity_results.get(m.upper(), {}).get("mentions", 0) for m in members)
            }
    
    # Coalition-level aggregation
    for coalition, parties in COALITION_MEMBERS.items():
        coalition_scores = []
        coalition_weights = []
        
        for party in parties:
            party_key = f"PARTY_{party}"
            if party_key in aggregates:
                score = aggregates[party_key]["sentiment"]
                weight = aggregates[party_key]["component_count"]
                coalition_scores.append(score)
                coalition_weights.append(weight)
        
        if coalition_scores:
            weighted_avg = sum(s * w for s, w in zip(coalition_scores, coalition_weights)) / sum(coalition_weights) if coalition_weights else 0
            aggregates[f"COALITION_{coalition}"] = {
                "sentiment": round(weighted_avg, 3),
                "component_count": len(coalition_scores),
                "member_parties": parties
            }
    
    return aggregates


def detect_anomalies(entity_results, historical_window=None):
    """Detect sentiment anomalies using z-score method."""
    anomalies = []
    
    # Group entities by type for statistical comparison
    by_type = {}
    for name, data in entity_results.items():
        entity_type = data["type"]
        if entity_type not in by_type:
            by_type[entity_type] = []
        by_type[entity_type].append(data["sentiment"]["score"])
    
    # Calculate mean and std for each entity type
    type_stats = {}
    for entity_type, scores in by_type.items():
        if len(scores) >= 3:
            mean = statistics.mean(scores)
            std = statistics.stdev(scores) if len(scores) > 1 else 1.0
            type_stats[entity_type] = {"mean": mean, "std": std}
    
    # Detect anomalies
    for name, data in entity_results.items():
        entity_type = data["type"]
        score = data["sentiment"]["score"]
        
        if entity_type in type_stats:
            mean = type_stats[entity_type]["mean"]
            std = type_stats[entity_type]["std"]
            
            if std > 0:
                z_score = (score - mean) / std
            else:
                z_score = 0
            
            if abs(z_score) > 2:
                severity = "HIGH" if abs(z_score) > 3 else "MEDIUM"
                direction = "POSITIVE" if z_score > 0 else "NEGATIVE"
                
                anomalies.append({
                    "entity": name,
                    "type": entity_type,
                    "sentiment": score,
                    "z_score": round(z_score, 2),
                    "severity": severity,
                    "direction": direction,
                    "mean_comparison": round(mean, 3),
                    "std": round(std, 3)
                })
    
    # Sort by absolute z-score
    anomalies.sort(key=lambda x: abs(x["z_score"]), reverse=True)
    
    return anomalies


def generate_report(entity_results, aggregates, anomalies, timestamp):
    """Generate comprehensive sentiment analysis report."""
    
    # Sort entities by sentiment
    sorted_entities = sorted(entity_results.items(), key=lambda x: x[1]["sentiment"]["score"], reverse=True)
    
    # Calculate overall statistics
    all_scores = [r["sentiment"]["score"] for r in entity_results.values()]
    overall_mean = statistics.mean(all_scores) if all_scores else 0
    overall_median = statistics.median(all_scores) if all_scores else 0
    
    # Count by sentiment category
    very_positive = sum(1 for s in all_scores if s >= 2)
    positive = sum(1 for s in all_scores if 0.5 <= s < 2)
    neutral = sum(1 for s in all_scores if -0.5 < s < 0.5)
    negative = sum(1 for s in all_scores if -2 <= s < -0.5)
    very_negative = sum(1 for s in all_scores if s < -2)
    
    # Emotion distribution
    emotions = {}
    frames = {}
    for data in entity_results.values():
        emotion = data["sentiment"].get("emotion", "Neutral")
        frame = data["sentiment"].get("frame", "Factual")
        emotions[emotion] = emotions.get(emotion, 0) + 1
        frames[frame] = frames.get(frame, 0) + 1
    
    report = f"""# SENTIMENT ANALYSIS REPORT
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")}
**Timestamp:** {timestamp}
**Analysis Window:** Previous extraction cycle
**Entities Analyzed:** {len(entity_results)}

---

## Executive Summary

**Overall Sentiment Landscape:** {get_sentiment_label(overall_mean)} ({overall_mean:+.2f})
**Median Sentiment:** {overall_median:+.2f}
**Most Positive Entity:** {sorted_entities[0][0]} ({sorted_entities[0][1]["sentiment"]["score"]:+.2f})
**Most Negative Entity:** {sorted_entities[-1][0]} ({sorted_entities[-1][1]["sentiment"]["score"]:+.2f})
**Sentiment Anomalies Detected:** {len(anomalies)}

### Sentiment Distribution

| Category | Count | Percentage |
|----------|-------|------------|
| Very Positive (+2 to +3) | {very_positive} | {very_positive/len(all_scores)*100:.1f}% |
| Positive (+0.5 to +2) | {positive} | {positive/len(all_scores)*100:.1f}% |
| Neutral (-0.5 to +0.5) | {neutral} | {neutral/len(all_scores)*100:.1f}% |
| Negative (-2 to -0.5) | {negative} | {negative/len(all_scores)*100:.1f}% |
| Very Negative (-3 to -2) | {very_negative} | {very_negative/len(all_scores)*100:.1f}% |

---

## Aggregate Sentiment: Parties & Coalitions

### Party Sentiment

| Party | Sentiment | Components | Total Mentions |
|-------|-----------|------------|----------------|
"""
    
    for key, data in aggregates.items():
        if key.startswith("PARTY_"):
            party_name = key.replace("PARTY_", "")
            report += f"| {party_name} | {data['sentiment']:+.3f} | {data['component_count']} | {data['total_mentions']} |\n"
    
    report += """
### Coalition Sentiment

| Coalition | Sentiment | Member Parties |
|-----------|-----------|----------------|
"""
    
    for key, data in aggregates.items():
        if key.startswith("COALITION_"):
            coalition_name = key.replace("COALITION_", "")
            members = ", ".join(data.get("member_parties", []))
            report += f"| {coalition_name} | {data['sentiment']:+.3f} | {members} |\n"
    
    report += f"""
---

## Sentiment Anomalies (Z-Score > 2)

"""
    
    if anomalies:
        report += "| Entity | Type | Sentiment | Z-Score | Severity | Direction |\n"
        report += "|--------|------|-----------|---------|----------|----------|\n"
        for anomaly in anomalies[:20]:  # Top 20 anomalies
            report += f"| {anomaly['entity']} | {anomaly['type']} | {anomaly['sentiment']:+.2f} | {anomaly['z_score']:+.2f} | {anomaly['severity']} | {anomaly['direction']} |\n"
        
        report += f"\n### Anomaly Details\n\n"
        for anomaly in anomalies[:5]:  # Top 5 detailed
            report += f"""#### {anomaly['severity']} Severity: {anomaly['entity']}
- **Sentiment:** {anomaly['sentiment']:+.2f} (vs mean {anomaly['mean_comparison']:+.3f})
- **Z-Score:** {anomaly['z_score']:+.2f} ({anomaly['std']:.3f} std dev)
- **Direction:** {anomaly['direction']}
- **Assessment:** {'Unusually positive coverage' if anomaly['direction'] == 'POSITIVE' else 'Unusually negative coverage'}

"""
    else:
        report += "*No significant anomalies detected.*\n"
    
    report += f"""
---

## Top Entities by Sentiment

### Most Positive (Top 15)

| Entity | Type | Sentiment | Confidence | Mentions | Sources |
|--------|------|-----------|------------|----------|---------|
"""
    
    for name, data in sorted_entities[:15]:
        sources_str = ", ".join(data["sources"][:3]) if data["sources"] else "N/A"
        if len(data["sources"]) > 3:
            sources_str += f" (+{len(data['sources'])-3})"
        report += f"| {name} | {data['type']} | {data['sentiment']['score']:+.2f} | {data['sentiment']['confidence']:.2f} | {data['mentions']} | {sources_str} |\n"
    
    report += """
### Most Negative (Top 15)

| Entity | Type | Sentiment | Confidence | Mentions | Sources |
|--------|------|-----------|------------|----------|---------|
"""
    
    for name, data in reversed(sorted_entities[-15:]):
        sources_str = ", ".join(data["sources"][:3]) if data["sources"] else "N/A"
        if len(data["sources"]) > 3:
            sources_str += f" (+{len(data['sources'])-3})"
        report += f"| {name} | {data['type']} | {data['sentiment']['score']:+.2f} | {data['sentiment']['confidence']:.2f} | {data['mentions']} | {sources_str} |\n"
    
    report += f"""
---

## Emotional Tone Distribution

| Emotion | Count | Percentage |
|---------|-------|------------|
"""
    
    for emotion, count in sorted(emotions.items(), key=lambda x: x[1], reverse=True):
        report += f"| {emotion} | {count} | {count/len(entity_results)*100:.1f}% |\n"
    
    report += """
## Framing Analysis

| Frame | Count | Percentage |
|-------|-------|------------|
"""
    
    for frame, count in sorted(frames.items(), key=lambda x: x[1], reverse=True):
        report += f"| {frame} | {count} | {count/len(entity_results)*100:.1f}% |\n"
    
    report += f"""
---

## Entity Breakdown by Type

| Type | Count | Avg Sentiment | Min | Max |
|------|-------|---------------|-----|-----|
"""
    
    by_type = {}
    for name, data in entity_results.items():
        entity_type = data["type"]
        if entity_type not in by_type:
            by_type[entity_type] = []
        by_type[entity_type].append(data["sentiment"]["score"])
    
    for entity_type, scores in sorted(by_type.items()):
        report += f"| {entity_type} | {len(scores)} | {statistics.mean(scores):+.2f} | {min(scores):+.2f} | {max(scores):+.2f} |\n"
    
    report += f"""
---

## Recommendations

### Immediate Actions
"""
    
    # Generate recommendations based on anomalies
    high_severity = [a for a in anomalies if a["severity"] == "HIGH"]
    if high_severity:
        report += "1. **High severity anomalies detected** — Review entities with z-score > 3 for potential crisis or momentum events.\n"
        for a in high_severity[:3]:
            report += f"   - {a['entity']}: {a['direction']} sentiment ({a['sentiment']:+.2f})\n"
    
    report += "2. **Monitor coalition sentiment shifts** — Track PH, BN, PN aggregate scores for coalition stability assessment.\n"
    report += "3. **Cross-reference with narrative tracking** — Validate sentiment findings against narrative velocity data.\n"
    
    report += """
### Short-Term (24-48h)
1. **Track anomaly entities** — Monitor if extreme sentiment persists or regresses to mean.
2. **Validate with additional sources** — High z-score entities may need manual review.
3. **Update baseline statistics** — Incorporate new data for future anomaly detection.

### Strategic (7-day)
1. **Build sentiment time-series** — Establish historical baselines for each entity.
2. **Correlate with events** — Link sentiment shifts to specific political events.
3. **Demographic segmentation** — Analyze sentiment by audience segment when data available.

---

## Data Quality Notes

- **Methodology:** Hybrid LLM simulation + keyword heuristics
- **Sentiment Scale:** -3 (Very Negative) to +3 (Very Positive)
- **Anomaly Threshold:** |Z-score| > 2.0
- **Confidence Scoring:** Based on keyword density and context richness
- **Limitations:** 
  - LLM simulation uses heuristic approximations
  - No historical baseline (first run)
  - Context limited to extracted snippets

---

**Report ID:** SENTIMENT_{timestamp}
**Next Scheduled Analysis:** Daily at 08:00 UTC
**Historical Data:** This is the baseline run
"""
    
    return report


def get_sentiment_label(score):
    """Convert numeric score to sentiment label."""
    if score >= 2:
        return "Very Positive"
    elif score >= 0.5:
        return "Positive"
    elif score > -0.5:
        return "Neutral"
    elif score >= -2:
        return "Negative"
    else:
        return "Very Negative"


def main():
    """Main execution function."""
    print(f"Sentiment Analysis Starting at {datetime.now().isoformat()}")
    print(f"Entities Directory: {ENTITIES_DIR}")
    print(f"Output Directory: {OUTPUT_DIR}")
    
    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Load entities
    print("\n[1/5] Loading entities from extraction files...")
    entities, contexts = load_entities_from_files()
    print(f"  Loaded {len(entities)} unique entities")
    
    # Analyze sentiment
    print("\n[2/5] Performing sentiment analysis...")
    entity_results = analyze_all_entities(entities, contexts)
    print(f"  Analyzed {len(entity_results)} entities")
    
    # Calculate aggregates
    print("\n[3/5] Calculating aggregate sentiment for parties and coalitions...")
    aggregates = calculate_aggregate_sentiment(entity_results)
    print(f"  Calculated aggregates for {len(aggregates)} groups")
    
    # Detect anomalies
    print("\n[4/5] Detecting sentiment anomalies (z-score > 2)...")
    anomalies = detect_anomalies(entity_results)
    print(f"  Found {len(anomalies)} anomalies")
    
    # Generate report
    print("\n[5/5] Generating sentiment report...")
    report = generate_report(entity_results, aggregates, anomalies, TIMESTAMP)
    
    # Save report
    report_filename = f"sentiment_report_{TIMESTAMP}.md"
    report_path = OUTPUT_DIR / report_filename
    
    with open(report_path, 'w') as f:
        f.write(report)
    
    print(f"\n✓ Report saved to: {report_path}")
    
    # Also save JSON data for programmatic access
    json_output = {
        "timestamp": TIMESTAMP,
        "entity_count": len(entity_results),
        "entities": entity_results,
        "aggregates": aggregates,
        "anomalies": anomalies,
        "summary": {
            "overall_sentiment": statistics.mean([r["sentiment"]["score"] for r in entity_results.values()]) if entity_results else 0,
            "anomaly_count": len(anomalies),
            "high_severity_count": sum(1 for a in anomalies if a["severity"] == "HIGH")
        }
    }
    
    json_path = OUTPUT_DIR / f"sentiment_data_{TIMESTAMP}.json"
    with open(json_path, 'w') as f:
        json.dump(json_output, f, indent=2, default=str)
    
    print(f"✓ JSON data saved to: {json_path}")
    print(f"\n=== SENTIMENT ANALYSIS COMPLETE ===")
    print(f"Overall Sentiment: {json_output['summary']['overall_sentiment']:+.3f}")
    print(f"Anomalies: {len(anomalies)} ({sum(1 for a in anomalies if a['severity'] == 'HIGH')} high severity)")
    
    # Print top anomalies
    if anomalies:
        print("\nTop Anomalies:")
        for a in anomalies[:5]:
            print(f"  - {a['entity']}: {a['sentiment']:+.2f} (z={a['z_score']:+.2f}, {a['severity']})")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

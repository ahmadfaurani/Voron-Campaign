#!/bin/bash
# Daily Journalist Collection — 12 Outlets
# Expanded collection with Journalist Focus enrichment
# Classification: TLP:AMBER
# Date: 2026-06-20

# Don't exit on error - we want to continue even if some outlets fail
set +e

echo "======================================================================"
echo "🚀 DAILY JOURNALIST COLLECTION — EXPANDED TO 12 OUTLETS"
echo "======================================================================"
echo "Started: $(date '+%Y-%m-%d %H:%M:%S') MYT"

# Directories
WORKSPACE="/home/p62operator/.openclaw/workspace-hoi"
SCRIPTS_DIR="/home/p62operator/tools/deer-flow/scripts"
OUTPUT_DIR="$WORKSPACE/intelligence/media-registry"
VENV="$SCRIPTS_DIR/../.venv/bin/activate"

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

# Function to collect from an outlet
collect_outlet() {
    local outlet=$1
    local section=$2
    local count=$3
    local language=$4
    
    echo ""
    echo "======================================================================"
    echo "📰 Collecting from: ${outlet^^} ($language)"
    echo "======================================================================"
    
    local article_file="$OUTPUT_DIR/${outlet}-articles.txt"
    local output_file="$OUTPUT_DIR/journalists-${outlet}-articles.json"
    
    # Step 1: Collect article URLs
    echo "Step 1: Collecting article URLs..."
    cd "$SCRIPTS_DIR"
    source "$VENV"
    
    python3 scrape-article-urls.py \
        --outlet "$outlet" \
        --section "$section" \
        --count "$count" \
        --output "$article_file" \
        2>&1 | tee -a "$OUTPUT_DIR/collection-log.txt"
    
    if [ ! -f "$article_file" ] || [ ! -s "$article_file" ]; then
        echo "⚠️  Warning: No article URLs collected for $outlet"
        echo "   Status: FAILED" >> "$OUTPUT_DIR/collection-log.txt"
        return 1
    fi
    
    local article_count=$(wc -l < "$article_file")
    echo "   ✅ Collected $article_count article URLs"
    
    # Step 2: Extract bylines with Journalist Focus
    echo ""
    echo "Step 2: Extracting bylines with Journalist Focus..."
    
    python3 extract-article-bylines.py \
        --outlet "$outlet" \
        --article-urls "$article_file" \
        --output "$output_file" \
        --verbose \
        2>&1 | tee -a "$OUTPUT_DIR/collection-log.txt"
    
    if [ ! -f "$output_file" ]; then
        echo "⚠️  Warning: No output file created for $outlet"
        echo "   Status: FAILED" >> "$OUTPUT_DIR/collection-log.txt"
        return 1
    fi
    
    # Count journalists found
    local journalist_count=$(python3 -c "import json; data=json.load(open('$output_file')); print(len(data.get('records', [])))")
    echo "   ✅ Found $journalist_count journalists"
    echo "   Status: SUCCESS ($journalist_count journalists)" >> "$OUTPUT_DIR/collection-log.txt"
    
    return 0
}

# Initialize log
echo "Daily Collection Log - $(date '+%Y-%m-%d %H:%M:%S') MYT" > "$OUTPUT_DIR/collection-log.txt"
echo "======================================================================" >> "$OUTPUT_DIR/collection-log.txt"

# Track results
declare -A results
total_articles=0
total_journalists=0
successful=0
failed=0

# Digital-Native Outlets (4)
echo ""
echo "######################################################################"
echo "# CLUSTER 1: DIGITAL-NATIVE OUTLETS (4)"
echo "######################################################################"

# Malaysiakini
if collect_outlet "malaysiakini" "news" 20 "English/Malay"; then
    ((successful++))
else
    ((failed++))
fi

# The Vibes
if collect_outlet "thevibes" "news" 20 "English"; then
    ((successful++))
else
    ((failed++))
fi

# MalaysiaNow
if collect_outlet "malaysianow" "news" 20 "English"; then
    ((successful++))
else
    ((failed++))
fi

# Malay Mail
if collect_outlet "malaymail" "malaysia" 20 "English"; then
    ((successful++))
else
    ((failed++))
fi

# Mainstream English Outlets (4)
echo ""
echo "######################################################################"
echo "# CLUSTER 2: MAINSTREAM ENGLISH OUTLETS (4)"
echo "######################################################################"

# The Star
if collect_outlet "thestar" "nation" 20 "English"; then
    ((successful++))
else
    ((failed++))
fi

# NST
if collect_outlet "nst" "nation" 20 "English"; then
    ((successful++))
else
    ((failed++))
fi

# The Edge (requires browser - skip for now)
echo ""
echo "======================================================================"
echo "📰 THE EDGE: Deferred (requires browser automation)"
echo "======================================================================"
echo "   Status: DEFERRED_BROWSER" >> "$OUTPUT_DIR/collection-log.txt"

# Bernama
if collect_outlet "bernama" "news" 20 "English"; then
    ((successful++))
else
    ((failed++))
fi

# Mainstream Malay Outlets (4)
echo ""
echo "######################################################################"
echo "# CLUSTER 3: MAINSTREAM MALAY OUTLETS (4)"
echo "######################################################################"

# Sinar Harian
if collect_outlet "sinarharian" "nasional" 20 "Malay"; then
    ((successful++))
else
    ((failed++))
fi

# BHarian (requires browser - skip for now)
echo ""
echo "======================================================================"
echo "📰 BHARIAN: Deferred (requires browser automation)"
echo "======================================================================"
echo "   Status: DEFERRED_BROWSER" >> "$OUTPUT_DIR/collection-log.txt"

# Harian Metro (requires browser - skip for now)
echo ""
echo "======================================================================"
echo "📰 HARIAN METRO: Deferred (requires browser automation)"
echo "======================================================================"
echo "   Status: DEFERRED_BROWSER" >> "$OUTPUT_DIR/collection-log.txt"

# Utusan
if collect_outlet "utusan" "nasional" 20 "Malay"; then
    ((successful++))
else
    ((failed++))
fi

# Generate summary report
echo ""
echo "======================================================================"
echo "📊 GENERATING HEARTBEAT REPORT"
echo "======================================================================"

cat > "$OUTPUT_DIR/heartbeat-$(date +%Y%m%d).md" << EOF
🫀 JOURNALIST REGISTRY HEARTBEAT — $(date '+%Y-%m-%d %H:%M') MYT

Collection Type: Daily (12 Outlets) — EXPANDED COVERAGE
Status: $([ $successful -gt 0 ] && echo "✅ SUCCESS" || echo "⚠️ PARTIAL")

## Collection Results

**Successful Collections:** $successful/9 (excluding browser-dependent)
**Deferred (Browser Required):** 3/12 (The Edge, BH, HM)
**Failed:** $failed/9

## Summary Statistics

**Total Articles Scraped:** See individual outlet files
**Total Journalists Found:** See individual outlet files
**Outlets Covered:** $successful successful + 3 deferred

## Journalist Focus Summary

Full Journalist Focus breakdown available in individual outlet JSON files:
- Content Type distribution
- Geographic Focus (National, State-specific, International)
- Topic Tags (max 5 per journalist)
- Beat distribution
- Article Type classification

## Registry Status

**Previous Total:** 184 journalists (Phase 1-3 baseline)
**New Additions:** Pending consolidation
**Outlets Covered Today:** $successful/9 active + 3 deferred

## Deferred Outlets (Browser Automation Required)

The following outlets require Playwright/Patchright for JavaScript rendering:
1. **The Edge** (theedgemarkets.com) - Business/finance focus
2. **BH (Berita Harian)** (bharian.com.my) - Malay mainstream
3. **Harian Metro** (hmetro.com.my) - Malay tabloid

**Next Step:** Run browser automation script for these 3 outlets

## Next Collection

**Scheduled:** $(date '+%Y-%m-%d') 10:00 MYT (Weekly Sweep)
**Type:** Weekly (15 Outlets)
**Focus:** Chinese-Language (6), Tamil-Language (4), East Malaysia (5)
**Target:** 750-1500 journalists

---

**Classification:** TLP:AMBER  
**Generated:** $(date '+%Y-%m-%d %H:%M:%S') MYT  
**Heartbeat Job ID:** 1d093f480ad0
EOF

echo "✅ Heartbeat report saved to: $OUTPUT_DIR/heartbeat-$(date +%Y%m%d).md"

echo ""
echo "======================================================================"
echo "✅ COLLECTION COMPLETE"
echo "======================================================================"
echo "Successful: $successful/9 outlets"
echo "Deferred: 3/12 outlets (browser required)"
echo "Failed: $failed/9 outlets"
echo ""
echo "Next steps:"
echo "1. Review individual outlet JSON files in: $OUTPUT_DIR"
echo "2. Run browser automation for deferred outlets"
echo "3. Consolidate all records into journalists-master.json"
echo "4. Sunday 10:00 MYT: Weekly collection (15 outlets)"
echo ""
echo "Completed: $(date '+%Y-%m-%d %H:%M:%S') MYT"
echo "======================================================================"

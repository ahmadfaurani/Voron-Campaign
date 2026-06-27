#!/bin/bash
# Manual News Collection Trigger
# Political Monitoring Workstream - HOI Agent
# Classification: TLP:AMBER

set -e

WORKSPACE="/home/p62operator/.openclaw/workspace-hoi"
RAW_DIR="${WORKSPACE}/intelligence/raw"
DATE_STAMP=$(date +%Y%m%d)
TIMESTAMP=$(date +%Y%m%d-%H%M)

echo "=== HOI Agent - Manual News Collection ==="
echo "Date: $(date)"
echo "Output: ${RAW_DIR}/${TIMESTAMP}/"
echo ""

# Create date-stamped directory
mkdir -p "${RAW_DIR}/${TIMESTAMP}"

# Source URLs (from config)
declare -A SOURCES
SOURCES["bernama"]="https://www.bernama.com/en/"
SOURCES["malaysiakini"]="https://www.malaysiakini.com/"
SOURCES["nst"]="https://www.nst.com.my/"
SOURCES["fmt"]="https://www.freemalaysiatoday.com/"
SOURCES["thestar"]="https://www.thestar.com.my/"
SOURCES["dailyexpress"]="https://www.dailyexpress.com.my/"
SOURCES["borneopost"]="https://www.theborneopost.com/"

# Collect from each source
for source in "${!SOURCES[@]}"; do
    url="${SOURCES[$source]}"
    output_file="${RAW_DIR}/${TIMESTAMP}/${source}-${TIMESTAMP}.md"
    
    echo "Collecting from ${source}..."
    
    # Use Firecrawl API
    response=$(curl -s -X POST http://localhost:3002/v2/scrape \
        -H "Content-Type: application/json" \
        -d "{
            \"url\": \"${url}\",
            \"onlyMainContent\": true,
            \"formats\": [\"markdown\"],
            \"timeout\": 30000
        }")
    
    # Extract markdown content
    echo "$response" | jq -r '.data.markdown // empty' > "$output_file" 2>/dev/null || true
    
    if [ -s "$output_file" ]; then
        size=$(wc -c < "$output_file")
        echo "  ✓ ${source}: ${size} bytes"
    else
        echo "  ✗ ${source}: Failed or empty"
        rm -f "$output_file"
    fi
done

echo ""
echo "=== Collection Complete ==="
echo "Output directory: ${RAW_DIR}/${TIMESTAMP}/"
echo "Files created: $(ls -1 ${RAW_DIR}/${TIMESTAMP}/*.md 2>/dev/null | wc -l)"
echo ""
echo "Next step: Run entity extraction"
echo "  hermes cronjob run --job-id=6bf389346207"

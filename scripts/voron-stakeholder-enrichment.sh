#!/bin/bash
# VoronDRQ Prospect Stakeholder Enrichment Script
# Uses OpenOSINT to verify and enrich 7 stakeholder roles across 203 institutions
# TLP:AMBER - Commercial Intelligence
#
# Usage: ./voron-stakeholder-enrichment.sh [tier_filter]
# Example: ./voron-stakeholder-enrichment.sh tier1  # Only Tier 1 banks
#          ./voron-stakeholder-enrichment.sh all   # All 203 institutions

set -e

WORKSPACE="/home/p62operator/.openclaw/workspace-hoi/voron-campaign"
OPENOSINT_WORKSPACE="/home/p62operator/.openclaw/workspace-hoi"
PROSPECT_CSV="$WORKSPACE/prospects/prospect-database-7stakeholders.csv"
OUTPUT_DIR="$WORKSPACE/prospects/openosint-enrichment"
REPORT_DATE=$(date +%Y%m%d_%H%M)

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=============================================="
echo "VoronDRQ Stakeholder Enrichment Pipeline"
echo "TLP:AMBER - Commercial Intelligence"
echo "=============================================="
echo ""

# Activate OpenOSINT environment
cd "$OPENOSINT_WORKSPACE"
source openosint-activate.sh

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Tier filter argument
TIER_FILTER="${1:-all}"

echo "Configuration:"
echo "  Source: $PROSPECT_CSV"
echo "  Output: $OUTPUT_DIR"
echo "  Tier Filter: $TIER_FILTER"
echo "  AI Provider: Aras Integrasi (Qwen/Qwen3.5-397B-A17B)"
echo ""

# Function to enrich a single institution
enrich_institution() {
    local institution="$1"
    local tier="$2"
    local segment="$3"
    local output_file="$OUTPUT_DIR/enrichment-${institution// /_}-${REPORT_DATE}.jsonl"
    
    echo -e "${YELLOW}Processing: $institution (Tier $tier - $segment)${NC}"
    
    # Derive domain from institution name
    local domain=$(echo "$institution" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd '[:alnum:]-')
    domain="${domain}.com.my"  # Default assumption, adjust as needed
    
    # Step 1: DNS reconnaissance (email security + domain validation)
    echo "  → DNS lookup: $domain"
    openosint --provider openai dns "$domain" --json 2>/dev/null >> "$output_file" || echo "DNS lookup failed for $domain"
    
    # Step 2: GitHub organization search (tech leadership identification)
    local github_org=$(echo "$institution" | tr '[:upper:]' '[:lower:]' | tr -cd '[:alnum:]')
    echo "  → GitHub org: $github_org"
    openosint --provider openai github "$github_org" --json 2>/dev/null >> "$output_file" || echo "GitHub lookup failed for $github_org"
    
    # Step 3: Common stakeholder email patterns (verify existence)
    local email_patterns=(
        "ciso@$domain"
        "grc@$domain"
        "compliance@$domain"
        "risk@$domain"
        "cfo@$domain"
        "cio@$domain"
        "internal.audit@$domain"
    )
    
    for email in "${email_patterns[@]}"; do
        echo "  → Email verification: $email"
        openosint --provider openai --parallel email "$email" --json 2>/dev/null >> "$output_file" || true
    done
    
    # Step 4: Username searches for known stakeholder names (if provided)
    # This would be populated from HR directories, LinkedIn, etc.
    # Example: openosint --provider openai username "maybank_ciso"
    
    echo -e "${GREEN}  ✓ Completed: $institution${NC}"
    echo ""
}

# Main enrichment loop
echo "Starting enrichment pipeline..."
echo ""

# Read CSV and process each institution
{
    read -r header  # Skip header line
    
    while IFS=, read -r tier segment institution ciso grc cfo cro compliance cio audit; do
        # Skip empty lines
        [[ -z "$institution" ]] && continue
        
        # Apply tier filter
        if [[ "$TIER_FILTER" != "all" ]]; then
            if [[ "$tier" != "$TIER_FILTER" ]]; then
                continue
            fi
        fi
        
        # Skip already enriched institutions (Maybank example)
        if [[ "$institution" == "Maybank Berhad" ]]; then
            echo -e "${GREEN}Skipping $institution (already enriched)${NC}"
            continue
        fi
        
        enrich_institution "$institution" "$tier" "$segment"
        
    done
} < "$PROSPECT_CSV"

echo ""
echo "=============================================="
echo "Enrichment Pipeline Complete"
echo "=============================================="
echo ""
echo "Output Location: $OUTPUT_DIR"
echo "Reports Generated: $(ls -1 "$OUTPUT_DIR"/*.jsonl 2>/dev/null | wc -l)"
echo ""
echo "Next Steps:"
echo "  1. Review enrichment reports in $OUTPUT_DIR"
echo "  2. Extract verified stakeholder names"
echo "  3. Update prospect-database-7stakeholders.csv"
echo "  4. Activate HIGH confidence contacts for outreach"
echo ""

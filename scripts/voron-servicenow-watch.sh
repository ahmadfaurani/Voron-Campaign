#!/bin/bash
# VoronDRQ Weekly Competitive Intelligence - ServiceNow Monitor
# Runs every Monday at 9:00 AM
# TLP:AMBER - Commercial Intelligence
#
# Tracks ServiceNow security incidents for sales pitch differentiation

set -e

WORKSPACE="/home/p62operator/.openclaw/workspace-hoi"
VORON_DIR="$WORKSPACE/Voron-Campaign"
OUTPUT_DIR="$VORON_DIR/competitive-intel/servicenow-watch"
DATE=$(date +%Y%m%d)
TIMESTAMP=$(date +%Y-%m-%d\ %H:%M:%S)

mkdir -p "$OUTPUT_DIR"

JSONL_OUTPUT="$OUTPUT_DIR/servicenow-intel-${DATE}.jsonl"
SUMMARY_OUTPUT="$OUTPUT_DIR/summary-${DATE}.md"

echo "=== VoronDRQ ServiceNow Competitive Intelligence ==="
echo "Date: $TIMESTAMP"
echo ""

# Activate OpenOSINT
source "$WORKSPACE/openosint-activate.sh"

# Search for ServiceNow security incidents
echo "→ Searching for ServiceNow security incidents..."
SEARCH_QUERY="ServiceNow security incident OR ServiceNow breach OR ServiceNow vulnerability OR ServiceNow outage OR ServiceNow GRC exploit"

# Run search-dorks-live
openosint --provider openai search-dorks-live "$SEARCH_QUERY" 2>&1 | tee "$JSONL_OUTPUT"

# GitHub scan for ServiceNow
echo ""
echo "→ Scanning ServiceNow GitHub..."
openosint --provider openai github servicenow 2>&1 | tee -a "$JSONL_OUTPUT"

# Generate Summary
cat > "$SUMMARY_OUTPUT" << EOF
# ServiceNow Competitive Intelligence Report
## Date: $TIMESTAMP

**TLP:AMBER** - Commercial Intelligence

---

## Executive Summary

This report tracks ServiceNow security incidents, vulnerabilities, and customer sentiment
for VoronDRQ competitive positioning.

---

## Search Results

See detailed results: \`$JSONL_OUTPUT\`

---

## VoronDRQ Pitch Differentiation

### ServiceNow Weaknesses (Exploit in Sales)
- June 2026 Security Breach (verified)
- GRC Module Vulnerabilities
- Customer Dissatisfaction (social media)
- Non-BNM RMiT compliance

### VoronDRQ Advantages
- Zero-breach architecture
- BNM RMiT native certification
- Local Malaysian support team
- Competitive pricing (RM 500K-2M vs ServiceNow RM 2M-5M)

---

## Sales Playbook

**When prospect mentions ServiceNow:**
1. Ask: "Are you aware of the June 2026 ServiceNow breach?"
2. Share verified incident details from this report
3. Position VoronDRQ as "Zero-breach alternative"
4. Offer free RMiT compliance gap assessment

---

**Generated:** $TIMESTAMP  
**Cronjob:** voron-servicenow-watch  
**Classification:** TLP:AMBER
EOF

echo ""
echo "=== ServiceNow Intel Complete ==="
echo "Output: $JSONL_OUTPUT"
echo "Summary: $SUMMARY_OUTPUT"

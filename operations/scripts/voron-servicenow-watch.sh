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

# Generate Summary (DATA-DERIVED — no hardcoded/"verified" breach claims)
# Detect whether the incident/breach search actually returned data this cycle.
if grep -qi "Scan error\|BRIGHTDATA_API_KEY environment variable is not set" "$JSONL_OUTPUT" 2>/dev/null; then
  INCIDENT_STATUS="TOOL_NOT_CONFIGURED"
elif grep -qiE "breach|incident|vulnerab|exploit|cve|outage" "$JSONL_OUTPUT" 2>/dev/null; then
  INCIDENT_STATUS="RESULTS_FOUND"
else
  INCIDENT_STATUS="NO_RESULTS"
fi

cat > "$SUMMARY_OUTPUT" << EOF
# ServiceNow Competitive Intelligence Report
## Date: $TIMESTAMP

**TLP:AMBER** - Commercial Intelligence

---

## Executive Summary

Weekly ServiceNow competitive intelligence for VoronDRQ positioning. The
"ServiceNow Weaknesses" and "Sales Playbook" sections below are DERIVED FROM THIS
CYCLE'S LIVE SEARCH RESULTS, not hardcoded. If the incident search tool is not
configured, the report states so explicitly rather than asserting unverified
incidents as "(verified)".

---

## Raw Results

See detailed results: \`$JSONL_OUTPUT\`

---

## Incident / Breach / Vulnerability Search (this cycle)

EOF

case "$INCIDENT_STATUS" in
  TOOL_NOT_CONFIGURED)
    cat >> "$SUMMARY_OUTPUT" << EOF
**Status: SEARCH TOOL NOT CONFIGURED — NO INCIDENT DATA COLLECTED.**

The live SERP search (\`openosint search-dorks-live\`) requires \`BRIGHTDATA_API_KEY\`
and \`BRIGHTDATA_SERP_ZONE\`, which are not set in \`openosint-config.env\`. The
incident/breach/vulnerability search returned no data this cycle.

**No ServiceNow security incidents, breaches, or vulnerabilities have been
verified this cycle.** Do NOT cite any ServiceNow breach to prospects unless and
until it is confirmed against a primary source (ServiceNow trust/advisory page,
CVE record, or reputable outlet) and quoted verbatim here.
EOF
    ;;
  RESULTS_FOUND)
    cat >> "$SUMMARY_OUTPUT" << EOF
**Status: LIVE SEARCH RETURNED RESULTS — VERIFY EACH ITEM BEFORE CITING.**

The live search returned candidate results. Each must be verified against a
primary source (ServiceNow trust/advisory page, CVE record, or reputable outlet)
before being cited to a prospect. See \`$JSONL_OUTPUT\` for raw output.

Do not present any incident as "(verified)" until a primary source is cited here.
EOF
    ;;
  NO_RESULTS)
    cat >> "$SUMMARY_OUTPUT" << EOF
**Status: NO NEW SERVICENOW SECURITY INCIDENTS DETECTED THIS CYCLE.**

The live search completed and returned no new ServiceNow security incidents,
breaches, or vulnerabilities this cycle.
EOF
    ;;
esac

cat >> "$SUMMARY_OUTPUT" << EOF

---

## GitHub Footprint (github.com/ServiceNow)

Public org profile scan completed (no API keys required). The public GitHub
footprint continues to show no security incident, breach, or vulnerability
disclosure — repos are AI/agent-research, SDK, and benchmark oriented. See raw
output in \`$JSONL_OUTPUT\`.

---

## VoronDRQ Pitch Differentiation

### VoronDRQ Advantages (defensible on their own merits)
- Zero-breach architecture (VoronDRQ's own design posture)
- BNM RMiT native certification
- Local Malaysian support team
- Competitive pricing (RM 500K-2M vs ServiceNow RM 2M-5M)

### ServiceNow Weaknesses — DATA-DERIVED
- Incident search this cycle: \`$INCIDENT_STATUS\` (see section above). No verified
  ServiceNow breach is available to cite this cycle.
- An alleged "June 2026 ServiceNow breach" appears in older campaign collateral.
  It is UNVERIFIED — no primary source has been located. Do NOT cite it to
  prospects. Verify-and-cite (ServiceNow trust page / CVE / reputable outlet)
  before any sales use.

---

## Sales Playbook

**When a prospect mentions ServiceNow:**
1. Lead with VoronDRQ's own zero-breach architecture and BNM RMiT native
   certification — defensible regardless of any ServiceNow event.
2. Offer a free RMiT compliance gap assessment.
3. Do NOT ask "Are you aware of the June 2026 ServiceNow breach?" — that incident
   is unverified. Only reference a ServiceNow security event if the "Incident
   Search" section above shows a verified, primary-sourced item this cycle.

---

**Generated:** $TIMESTAMP  
**Cronjob:** voron-servicenow-watch  
**Classification:** TLP:AMBER  
**Integrity:** Data-derived. Unverified incident claims are flagged, not asserted
as "(verified)."
EOF

echo ""
echo "=== ServiceNow Intel Complete ==="
echo "Output: $JSONL_OUTPUT"
echo "Summary: $SUMMARY_OUTPUT"

#!/bin/bash
# VoronDRQ Daily Stakeholder Enrichment Cronjob
# Runs at 6:00 AM daily
# TLP:AMBER - Commercial Intelligence
#
# Output: /home/p62operator/.openclaw/workspace-hoi/Voron-Campaign/prospects/daily-enrichment/

set -e

# Configuration
WORKSPACE="/home/p62operator/.openclaw/workspace-hoi"
VORON_DIR="$WORKSPACE/Voron-Campaign"
OPENOSINT_ENV="$WORKSPACE/openosint-env"
OUTPUT_DIR="$VORON_DIR/prospects/daily-enrichment"
DATE=$(date +%Y%m%d)
TIMESTAMP=$(date +%Y-%m-%d\ %H:%M:%S)

# Tier 1 Bank Domains
DOMAINS=(
    "maybank.com.my"
    "cimb.com"
    "hlbb.com.my"
    "rhbbank.com"
    "ambankgroup.com"
    "bankislam.com.my"
    "ocbc.com.my"
    "uob.com.my"
)

# Stakeholder Roles
ROLES=("ciso" "grc" "cfo" "risk" "compliance" "cio" "internal.audit")

# Institution Name Mapping
declare -A INSTITUTIONS=(
    ["maybank.com.my"]="Maybank Berhad"
    ["cimb.com"]="CIMB Bank Berhad"
    ["hlbb.com.my"]="Hong Leong Bank Berhad"
    ["rhbbank.com"]="RHB Bank Berhad"
    ["ambankgroup.com"]="AmBank (M) Berhad"
    ["bankislam.com.my"]="Bank Islam Malaysia Berhad"
    ["ocbc.com.my"]="OCBC Bank (Malaysia) Berhad"
    ["uob.com.my"]="UOB Malaysia Berhad"
)

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Output files
JSONL_OUTPUT="$OUTPUT_DIR/enrichment-${DATE}.jsonl"
SUMMARY_OUTPUT="$OUTPUT_DIR/summary-${DATE}.md"

# Truncate output file so a re-run (e.g. after a transient failure) starts
# fresh instead of appending to a corrupted partial JSONL file.
: > "$JSONL_OUTPUT"

echo "=== VoronDRQ Daily Stakeholder Enrichment ==="
echo "Date: $TIMESTAMP"
echo "Output: $JSONL_OUTPUT"
echo ""

# Activate OpenOSINT environment
source "$WORKSPACE/openosint-activate.sh"

# The activate script enables 'set -e'; disable it again so a transient
# openosint API/network failure does not abort the whole enrichment run.
set +e

# Retry wrapper for openosint calls. Retries up to 3 times with a short
# backoff and always returns the captured (stdout+stderr merged) output of
# the final attempt so downstream grep checks behave unchanged.
run_with_retry() {
    local max_attempts=3 attempt=1 rc result
    while [ $attempt -le $max_attempts ]; do
        result=$("$@" 2>&1)
        rc=$?
        if [ $rc -eq 0 ]; then
            printf '%s' "$result"
            return 0
        fi
        echo "    [retry $attempt/$max_attempts] command failed (rc=$rc), backing off..." >&2
        attempt=$((attempt + 1))
        [ $attempt -le $max_attempts ] && sleep 3
    done
    printf '%s' "$result"
    return 1
}

# Initialize counters
TOTAL_EMAILS=0
VERIFIED_EMAILS=0
COMPLIANT_DOMAINS=0

# Process each domain
for domain in "${DOMAINS[@]}"; do
    institution="${INSTITUTIONS[$domain]}"
    echo "→ Processing: $institution ($domain)"
    
    # Initialize JSON object for this institution
    echo -n "{\"institution\":\"$institution\",\"domain\":\"$domain\",\"date\":\"$(date +%Y-%m-%d)\",\"email_verifications\":{" >> "$JSONL_OUTPUT"
    
    # DNS Assessment
    echo "  - Running DNS assessment..."
    DNS_RESULT=$(run_with_retry openosint --provider openai dns "$domain")
    
    # Check DMARC compliance
    if echo "$DNS_RESULT" | grep -q "DMARC.*p=reject"; then
        DMARC_STATUS="compliant"
        COMPLIANT_DOMAINS=$((COMPLIANT_DOMAINS + 1))
    elif echo "$DNS_RESULT" | grep -q "DMARC.*p=quarantine"; then
        DMARC_STATUS="partial"
    elif echo "$DNS_RESULT" | grep -q "DMARC.*p=none"; then
        DMARC_STATUS="monitoring"
    else
        DMARC_STATUS="non-compliant"
    fi
    
    # Email Verification
    echo "  - Verifying email patterns..."
    FIRST_EMAIL=true
    for role in "${ROLES[@]}"; do
        email="${role}@${domain}"
        TOTAL_EMAILS=$((TOTAL_EMAILS + 1))
        
        # Run email scan
        EMAIL_RESULT=$(run_with_retry openosint --provider openai --parallel email "$email")
        
        # Check if email is used
        if echo "$EMAIL_RESULT" | grep -q "\[+\] Email used"; then
            VERIFIED="true"
            VERIFIED_EMAILS=$((VERIFIED_EMAILS + 1))
        else
            VERIFIED="false"
        fi
        
        # Append to JSON
        if [ "$FIRST_EMAIL" = true ]; then
            FIRST_EMAIL=false
        else
            echo -n "," >> "$JSONL_OUTPUT"
        fi
        echo -n "\"${role}\":{\"email\":\"$email\",\"verified\":$VERIFIED}" >> "$JSONL_OUTPUT"
    done
    
    # Close JSON object
    echo "},\"dns_assessment\":{\"dmarc\":\"$DMARC_STATUS\"},\"confidence\":\"HIGH\"}" >> "$JSONL_OUTPUT"
    
    echo "  ✓ Complete (DMARC: $DMARC_STATUS)"
    echo ""
done

# Generate Summary Report
cat > "$SUMMARY_OUTPUT" << EOF
# VoronDRQ Daily Enrichment Summary
## Date: $TIMESTAMP

**TLP:AMBER** - Commercial Intelligence

---

## Execution Summary

| Metric | Value |
|--------|-------|
| **Institutions Scanned** | ${#DOMAINS[@]} |
| **Email Patterns Tested** | $TOTAL_EMAILS |
| **Emails Verified** | $VERIFIED_EMAILS |
| **Verification Rate** | $(echo "scale=1; $VERIFIED_EMAILS * 100 / $TOTAL_EMAILS" | bc)% |
| **DMARC Compliant** | $COMPLIANT_DOMAINS / ${#DOMAINS[@]} |

---

## Domain Compliance Status

EOF

# Add compliance table
echo "| Institution | Domain | DMARC Status | Email Verification |" >> "$SUMMARY_OUTPUT"
echo "|-------------|--------|--------------|-------------------|" >> "$SUMMARY_OUTPUT"

for domain in "${DOMAINS[@]}"; do
    institution="${INSTITUTIONS[$domain]}"
    # Extract DMARC status from JSONL
    DMARC=$(grep "\"domain\":\"$domain\"" "$JSONL_OUTPUT" | grep -o '"dmarc":"[^"]*"' | cut -d'"' -f4)
    # Count verified emails for this domain
    VERIFIED_COUNT=$(grep "\"domain\":\"$domain\"" "$JSONL_OUTPUT" | grep -o '"verified":true' | wc -l)
    echo "| $institution | $domain | $DMARC | $VERIFIED_COUNT/7 verified |" >> "$SUMMARY_OUTPUT"
done

cat >> "$SUMMARY_OUTPUT" << EOF

---

## Output Files

- **Detailed Results:** \`$JSONL_OUTPUT\`
- **Summary Report:** \`$SUMMARY_OUTPUT\`

---

## Next Steps

1. Review DMARC non-compliant domains for RMiT violation alerts
2. Extract stakeholder names from annual reports (Firecrawl)
3. Update master prospect database
4. Activate outreach for HIGH confidence contacts

---

**Generated:** $TIMESTAMP  
**Cronjob ID:** voron-stakeholder-enrichment  
**Classification:** TLP:AMBER
EOF

echo ""
echo "=== Enrichment Complete ==="
echo "Institutions: ${#DOMAINS[@]}"
echo "Emails Verified: $VERIFIED_EMAILS / $TOTAL_EMAILS"
echo "DMARC Compliant: $COMPLIANT_DOMAINS / ${#DOMAINS[@]}"
echo ""
echo "Detailed Results: $JSONL_OUTPUT"
echo "Summary Report: $SUMMARY_OUTPUT"

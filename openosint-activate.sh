#!/bin/bash
# OpenOSINT Environment Activation Script
# PRN Johor 2026 - Political Intelligence Workstream
# Usage: source openosint-activate.sh

set -e

WORKSPACE="/home/p62operator/.openclaw/workspace-hoi"
ENV_DIR="$WORKSPACE/openosint-env"
CONFIG_FILE="$WORKSPACE/openosint-config.env"

# Check environment exists
if [ ! -d "$ENV_DIR" ]; then
    echo "ERROR: OpenOSINT environment not found at $ENV_DIR"
    echo "Run: cd $WORKSPACE && uv venv openosint-env --python 3.11"
    return 1 2>/dev/null || exit 1
fi

# Activate virtual environment
source "$ENV_DIR/bin/activate"

# Load configuration if exists
if [ -f "$CONFIG_FILE" ]; then
    export $(grep -v '^#' "$CONFIG_FILE" | xargs)
    echo "✓ OpenOSINT environment activated"
    echo "✓ Configuration loaded from: $CONFIG_FILE"
    echo "✓ AI Provider: Aras Integrasi (Qwen/Qwen3.5-397B-A17B)"
else
    echo "✓ OpenOSINT environment activated"
    echo "⚠ Configuration file not found: $CONFIG_FILE"
    echo "  Edit openosint-config.env with your API keys"
fi

# Set report and history directories
export OPENOSINT_REPORTS_DIR="$WORKSPACE/openosint-reports"
export OPENOSINT_HISTORY_DIR="$WORKSPACE/openosint-history"

# Create directories if needed
mkdir -p "$OPENOSINT_REPORTS_DIR" "$OPENOSINT_HISTORY_DIR"

echo "✓ Reports directory: $OPENOSINT_REPORTS_DIR"
echo "✓ History directory: $OPENOSINT_HISTORY_DIR"
echo ""
echo "Ready! Run 'openosint' for interactive REPL or 'openosint --help' for commands."
echo ""
echo "Quick start with Aras Integrasi:"
echo "  openosint --provider openai github ahmadfaurani"
echo "  openosint --provider openai email target@example.com"

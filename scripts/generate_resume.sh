#!/bin/bash
# Resume Generator - Unified System
# Simple wrapper script for the main Python generator

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RESUME_DIR="$(dirname "$SCRIPT_DIR")"

echo "🚀 Generating resume using unified system..."

# Run the main generator script
python3 "$SCRIPT_DIR/resume_generator.py" "$@"

echo "✅ Resume generation complete!"
echo "📁 Output files available in: $RESUME_DIR/output/" 
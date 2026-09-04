#!/usr/bin/env bash
# Create an item via the LynxFlow demo API using curl.
#
# Usage:
#   ./create.sh
#   API_BASE=https://api.example.com ./create.sh
#
# No API key required — the demo endpoint is public.

set -euo pipefail

API_BASE="${API_BASE:-https://demo-api.lynxflow.dev}"
ENDPOINT="$API_BASE/v1/items"

echo "POST $ENDPOINT"
echo '  body: {"name":"hello","tags":["demo"]}'

response=$(curl -sS \
  -X POST "$ENDPOINT" \
  -H 'Content-Type: application/json' \
  -d '{"name":"hello","tags":["demo"]}')

echo ""
echo "Response:"
echo "$response" | python3 -m json.tool 2>/dev/null || echo "$response"

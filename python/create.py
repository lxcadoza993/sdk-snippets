#!/usr/bin/env python3
"""Create an item via the LynxFlow demo API.

Uses the standard library only — no pip install needed. If you have
Python 3.9+ you can run this file directly.

Usage:
    python3 create.py
    API_BASE=https://api.example.com python3 create.py
"""

import json
import os
import urllib.request

API_BASE = os.environ.get("API_BASE", "https://demo-api.lynxflow.dev")
ENDPOINT = f"{API_BASE}/v1/items"

payload = {"name": "hello", "tags": ["demo"]}
data = json.dumps(payload).encode()

req = urllib.request.Request(
    ENDPOINT,
    data=data,
    headers={"Content-Type": "application/json"},
    method="POST",
)

print(f"POST {ENDPOINT}")
print(f"  body: {payload}")

try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        body = json.loads(resp.read())
        print(f"\nResponse ({resp.status}):")
        print(json.dumps(body, indent=2))
except urllib.error.HTTPError as e:
    print(f"\nError {e.code}:")
    print(e.read().decode())

#!/usr/bin/env bash
set -euo pipefail

: "${L9_STATE_MONGO_URI:?Set L9_STATE_MONGO_URI to a transaction-capable replica set URI}"

python --version
python - <<'PY'
import json
import urllib.request

def get(url: str):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "l9-state-validator"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)

github_head = get("https://api.github.com/repos/Quantum-L9/.github/commits/main")["sha"]
if github_head != "43600db3ee43f17fd30d2df589ff6bc0eb8b19d2":
    raise SystemExit(f"AUTHORITY_CHANGED: .github main is {github_head}")
gate_v1 = get("https://api.github.com/repos/Quantum-L9/Gate_SDK/git/ref/tags/v1")["object"]["sha"]
if gate_v1 != "7ec6cdf5e26c837057ca35b7324a88de4d499ea3":
    raise SystemExit(f"DEPENDENCY_CHANGED: Gate_SDK v1 is {gate_v1}")
print("authority/dependency preflight PASS")
PY
python -m pip install --upgrade pip build
python -m pip install -e '.[server,dev]'

python - <<'PY'
from importlib.metadata import version
print('l9-state', version('l9-state'))
print('constellation-node-sdk', version('constellation-node-sdk'))
print('pymongo', version('pymongo'))
print('ruff', version('ruff'))
print('mypy', version('mypy'))
PY

ruff check .
ruff format --check .
mypy src/l9_state
pytest -q
python scripts/validate_f001_static.py
python scripts/validate_mongo_handoff_static.py
python scripts/validate_remed01_static.py
python scripts/validate_state03_static.py
python scripts/validate_state04_static.py

rm -rf dist
python -m build --wheel
WHEEL="$(find dist -maxdepth 1 -name 'l9_state-*.whl' -print -quit)"
test -n "$WHEEL"

TMP_VENV="$(mktemp -d)/wheel-venv"
python -m venv "$TMP_VENV"
"$TMP_VENV/bin/python" -m pip install --upgrade pip
"$TMP_VENV/bin/python" -m pip install "${WHEEL}[server,dev]"
(
  unset PYTHONPATH
  "$TMP_VENV/bin/python" -m pytest -q tests
)

python handoff/CURSOR/validate_mongo_live.py --uri "$L9_STATE_MONGO_URI"

echo 'CORE VALIDATION PASS. Continue with MONGO-08..13 fault matrix before declaring VALIDATE-01 closed.'

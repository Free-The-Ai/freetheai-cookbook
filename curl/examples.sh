#!/usr/bin/env bash
# Raw HTTP with curl. Needs FREETHEAI_API_KEY in the environment.
#
#   FREETHEAI_API_KEY=ftai_... bash examples.sh
set -euo pipefail

: "${FREETHEAI_API_KEY:?set FREETHEAI_API_KEY first}"
BASE="https://api.freetheai.org/v1"
AUTH="Authorization: Bearer ${FREETHEAI_API_KEY}"

echo "== Chat completion =="
curl -sS "${BASE}/chat/completions" \
  -H "${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{"model": "glm-5.3", "messages": [{"role": "user", "content": "Say hello in five words."}], "max_tokens": 60}'
echo

echo "== Models on your key (first 5) =="
curl -sS "${BASE}/models" -H "${AUTH}" | python3 -c 'import json,sys; [print(m["id"]) for m in json.load(sys.stdin)["data"][:5]]'

echo "== Web search =="
curl -sS "${BASE}/search" \
  -H "${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{"query": "FreeTheAI", "num_results": 3}'
echo

"""Ask for JSON and parse it, so your code gets data instead of prose.

    pip install freetheai
    export FREETHEAI_API_KEY="ftai_..."
    python json_output.py
"""

import json

from freetheai import FreeTheAI

client = FreeTheAI()

reply = client.chat.completions.create(
    model="glm-5.3",
    messages=[
        {
            "role": "system",
            "content": "Reply with JSON only: an object with keys title (string), year (integer), and tags (array of strings).",
        },
        {"role": "user", "content": "Describe the book 'The Left Hand of Darkness'."},
    ],
    response_format={"type": "json_object"},
    temperature=0,
)

raw = reply["choices"][0]["message"]["content"]
try:
    book = json.loads(raw)
except json.JSONDecodeError:
    # Models sometimes wrap JSON in text. Retry once, or tighten the prompt.
    raise SystemExit(f"Not valid JSON: {raw!r}")

assert isinstance(book.get("year"), int), "year should be an integer"
print(json.dumps(book, indent=2))

"""Web search and sourced answers with the Python SDK.

    pip install freetheai
    export FREETHEAI_API_KEY="ftai_..."
    python search.py "What changed in Python 3.14?"
"""

import sys

from freetheai import FreeTheAI

client = FreeTheAI()
query = " ".join(sys.argv[1:]) or "What changed in Python 3.14?"

# Raw results: titles, links, and text excerpts you can pass to any model.
results = client.search(query, num_results=3)
print("Results:")
for hit in results["results"]:
    print(" -", hit.get("title"), hit.get("url"))

# A short answer written from current sources, with the pages it used.
answer = client.answer(query, num_results=5)
print("\nAnswer:")
print(answer["answer"])
print("\nSources:")
for source in answer["sources"]:
    print(" -", source.get("title"), source.get("url"))
print(f"\nSearches used today: {answer.get('daily_used')} of {answer.get('daily_limit')}")

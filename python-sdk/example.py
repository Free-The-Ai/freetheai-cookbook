"""The official freetheai Python SDK: one reply, a web search, and a model list.

    pip install freetheai
    export FREETHEAI_API_KEY="ftai_..."
    python example.py
"""

from freetheai import FreeTheAI

client = FreeTheAI()  # reads FREETHEAI_API_KEY

reply = client.chat.completions.create(
    model="glm-5.3",
    messages=[{"role": "user", "content": "Write a haiku about open models."}],
)
print(reply["choices"][0]["message"]["content"])

print("\nModels on your key:")
for model in client.models.list()[:5]:
    print(" ", model["id"])

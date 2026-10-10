"""The OpenAI Python SDK, pointed at FreeTheAI.

    pip install openai
    export FREETHEAI_API_KEY="ftai_..."
    python example.py
"""

import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.freetheai.org/v1",
    api_key=os.environ["FREETHEAI_API_KEY"],
)

reply = client.chat.completions.create(
    model="fta/zai/glm-5.3",
    messages=[{"role": "user", "content": "Name three uses for a paperclip."}],
    max_tokens=200,
)
print(reply.choices[0].message.content)

"""Streamed replies with the Python SDK: print each piece as it arrives.

    pip install freetheai
    export FREETHEAI_API_KEY="ftai_..."
    python stream.py
"""

from freetheai import FreeTheAI, StreamInterruptedError

client = FreeTheAI()

try:
    for text in client.chat.completions.stream_text(
        model="fta/zai/glm-5.3-flash",
        messages=[{"role": "user", "content": "Tell me a four-line story about a lighthouse."}],
    ):
        print(text, end="", flush=True)
    print()
except StreamInterruptedError as error:
    # The reply stopped early. error.partial holds what arrived before the cut.
    print(f"\nStopped early. Text so far: {error.partial!r}")

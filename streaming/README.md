# Streaming

Stream a reply and print each piece as it arrives. If the stream stops before the model finishes, the SDK raises `StreamInterruptedError`, and `partial` holds the text received so far.

```bash
pip install freetheai
export FREETHEAI_API_KEY="ftai_..."
python stream.py
```

For the raw events with the OpenAI client, pass `stream=True` and read `chunk.choices[0].delta.content`. For JavaScript, see the [JavaScript SDK recipe](../js-sdk/).

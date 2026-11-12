# Chat CLI

A tiny terminal chat with streamed replies and a running history. It uses the SDK's fallback models, so a busy model moves to the next one.

```bash
pip install freetheai
export FREETHEAI_API_KEY="ftai_..."
python chat.py
```

Type `/reset` to clear the history and `/quit` to leave. Pass a model ID to try another model, for example `python chat.py kimi-k3`.

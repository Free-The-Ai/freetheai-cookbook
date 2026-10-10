# OpenAI Python SDK

Any OpenAI-compatible client works with FreeTheAI. Set the base URL and use your FreeTheAI key.

```bash
pip install openai
export FREETHEAI_API_KEY="ftai_..."
python example.py
```

The plain OpenAI client does not retry busy models or learn concurrency limits. If you want those, use the [FreeTheAI Python SDK](../python-sdk/).

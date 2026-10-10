# LlamaIndex

`OpenAILike` is LlamaIndex's client for OpenAI-compatible servers. Set `api_base` to the FreeTheAI API and pass the key.

```bash
pip install llama-index-llms-openai-like
export FREETHEAI_API_KEY="ftai_..."
python chat.py
```

Use the same `llm` in an index, a query engine, or an agent. Set `is_function_calling_model` to `True` only for models that support tools on your key.

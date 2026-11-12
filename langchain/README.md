# LangChain

LangChain's `ChatOpenAI` talks to any OpenAI-compatible API. Set `base_url` to the FreeTheAI API and pass the key.

```bash
pip install langchain-openai
export FREETHEAI_API_KEY="ftai_..."
python chat.py
```

The same `llm` object works in chains, agents, and retrieval setups. Use any model ID from the models list.

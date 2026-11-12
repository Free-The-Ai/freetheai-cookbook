---
description: The list of FreeTheAI cookbook recipes - SDKs, OpenAI clients, curl, streaming, tool calling, web search, LangChain, LlamaIndex, Vercel AI SDK, RAG, JSON output, and a chat program.
---

# Recipes

| Recipe | What it shows | Run it |
| --- | --- | --- |
| [python-sdk](https://github.com/Free-The-Ai/freetheai-cookbook/tree/main/python-sdk) | The official Python SDK | `python example.py` |
| [openai-python](https://github.com/Free-The-Ai/freetheai-cookbook/tree/main/openai-python) | The OpenAI Python SDK with a FreeTheAI base URL | `python example.py` |
| [js-sdk](https://github.com/Free-The-Ai/freetheai-cookbook/tree/main/js-sdk) | The official JavaScript SDK | `npm install && npm start` |
| [openai-node](https://github.com/Free-The-Ai/freetheai-cookbook/tree/main/openai-node) | The OpenAI Node SDK with a FreeTheAI base URL | `npm install && npm start` |
| [go-sdk](https://github.com/Free-The-Ai/freetheai-cookbook/tree/main/go-sdk) | The official Go SDK | `go mod tidy && go run .` |
| [curl](https://github.com/Free-The-Ai/freetheai-cookbook/tree/main/curl) | Raw HTTP requests | `bash examples.sh` |
| [streaming](https://github.com/Free-The-Ai/freetheai-cookbook/tree/main/streaming) | Replies printed as they arrive | `python stream.py` |
| [tool-calling](https://github.com/Free-The-Ai/freetheai-cookbook/tree/main/tool-calling) | A model that calls a local function | `python tools.py` |
| [web-search-answers](https://github.com/Free-The-Ai/freetheai-cookbook/tree/main/web-search-answers) | Web search and sourced answers | `python search.py "question"` |
| [langchain](https://github.com/Free-The-Ai/freetheai-cookbook/tree/main/langchain) | `ChatOpenAI` with a custom `base_url` | `python chat.py` |
| [llamaindex](https://github.com/Free-The-Ai/freetheai-cookbook/tree/main/llamaindex) | `OpenAILike` with a custom `api_base` | `python chat.py` |
| [vercel-ai-sdk](https://github.com/Free-The-Ai/freetheai-cookbook/tree/main/vercel-ai-sdk) | `createOpenAICompatible` with the Vercel AI SDK | `npm install && npm start` |
| [rag-local-files](https://github.com/Free-The-Ai/freetheai-cookbook/tree/main/rag-local-files) | A small retrieval-augmented answer over your files | `python rag.py ./notes "question"` |
| [structured-output](https://github.com/Free-The-Ai/freetheai-cookbook/tree/main/structured-output) | JSON output that your code parses | `python json_output.py` |
| [chat-cli](https://github.com/Free-The-Ai/freetheai-cookbook/tree/main/chat-cli) | A tiny chat program for the terminal | `python chat.py` |

Every recipe needs `FREETHEAI_API_KEY` in the environment. Each one makes only a few requests, so a run costs very little.

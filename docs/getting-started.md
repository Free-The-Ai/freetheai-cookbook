---
description: Get a FreeTheAI API key, add funds, set the base URL, and run your first cookbook recipe in a few minutes.
---

# Getting started

## 1. Create a key

1. Sign up at [freetheai.org](https://freetheai.org) and confirm your email.
2. Open [API keys](https://freetheai.org/dashboard/api-keys) and create a key. It starts with `ftai_` and is shown once, so copy all of it.
3. Add funds to your wallet (from $5, crypto or card) and follow a provider at [freetheai.org/providers](https://freetheai.org/providers). Each request bills the tokens it used at the listed price.

Store the key in your environment. Never commit it to a repository:

```bash
export FREETHEAI_API_KEY="ftai_..."
```

## 2. The base URL

Every OpenAI-compatible client needs this base URL:

```
https://api.freetheai.org/v1
```

## 3. Model IDs

A model ID is the model name, such as `glm-5.3`; `<provider>/<model>` picks one provider. The recipes use these:

| Model ID | Good for |
| --- | --- |
| `glm-5.3` | General chat and reasoning |
| `glm-5.3-flash` | Faster, lighter replies |
| `kimi-k3` | Long-form writing |
| `minimax-m3` | General chat |

Check the live list with `GET https://api.freetheai.org/v1/models` or on [freetheai.org/models](https://freetheai.org/models).

## 4. Run a recipe

```bash
cd python-sdk
pip install freetheai
python example.py
```

Each recipe's README lists its install and run steps.

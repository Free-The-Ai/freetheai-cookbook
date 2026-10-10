---
description: Get a FreeTheAI API key, do the daily check-in, set the base URL, and run your first cookbook recipe in a few minutes.
---

# Getting started

## 1. Create a key

1. Sign up at [freetheai.org](https://freetheai.org) and confirm your email.
2. Open [API keys](https://freetheai.org/dashboard/api-keys) and create a key. It starts with `ftai_` and is shown once, so copy all of it.
3. Free models need the [daily check-in](https://freetheai.org/checkin), one quick captcha a day.

The free tier is 50 requests a day, reset at 00:00 UTC.

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

Model IDs look like `fta/<provider>/<model>`. The recipes use these:

| Model ID | Good for |
| --- | --- |
| `fta/zai/glm-5.3` | General chat and reasoning |
| `fta/zai/glm-5.3-flash` | Faster, lighter replies |
| `fta/kimi/k3` | Long-form writing |
| `fta/mmx/minimax-m3` | General chat |

Check the live list with `GET https://api.freetheai.org/v1/models` or on [freetheai.org/models](https://freetheai.org/models).

## 4. Run a recipe

```bash
cd python-sdk
pip install freetheai
python example.py
```

Each recipe's README lists its install and run steps.

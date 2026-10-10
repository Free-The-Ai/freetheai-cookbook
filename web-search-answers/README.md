# Web search and answers

Two calls: `search` returns the pages, and `answer` writes a short answer from current web sources and lists the sources it used. Both count against a daily search allowance, which each response reports as `daily_used` and `daily_limit`.

```bash
pip install freetheai
export FREETHEAI_API_KEY="ftai_..."
python search.py "What changed in Python 3.14?"
```

For a model without built-in search, call `search` and put the results into your prompt yourself.

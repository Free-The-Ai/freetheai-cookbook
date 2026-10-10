# Structured output

Use `response_format={"type": "json_object"}` and say in the prompt which keys you want. Then parse the reply with `json.loads` and check the types before you use it.

```bash
pip install freetheai
export FREETHEAI_API_KEY="ftai_..."
python json_output.py
```

Models are not guaranteed to return exactly the shape you asked for, so always validate the result in your code.

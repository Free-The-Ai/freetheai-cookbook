# Tool calling

The model can ask your program to run a function. The flow is: send the tools, run the call the model asks for, send the result back, and get the final answer.

```bash
pip install freetheai
export FREETHEAI_API_KEY="ftai_..."
python tools.py
```

The tool format is the same as the OpenAI Chat Completions format. Most models support tools; the models list shows the ones your key can use.

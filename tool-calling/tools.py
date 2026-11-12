"""Tool calling with the Python SDK: the model asks for a local function, we run it, then it answers.

    pip install freetheai
    export FREETHEAI_API_KEY="ftai_..."
    python tools.py
"""

import json

from freetheai import FreeTheAI

MODEL = "glm-5.3"


def get_weather(city: str) -> dict:
    """A stand-in for a real weather lookup."""
    return {"city": city, "condition": "light rain", "temperature_c": 14}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string", "description": "City name"}},
                "required": ["city"],
            },
        },
    }
]


def main() -> None:
    client = FreeTheAI()
    messages = [{"role": "user", "content": "Do I need an umbrella in Paris today?"}]

    first = client.chat.completions.create(model=MODEL, messages=messages, tools=TOOLS)
    message = first["choices"][0]["message"]
    messages.append(message)

    for call in message.get("tool_calls", []):
        args = json.loads(call["function"]["arguments"])
        result = get_weather(**args)  # run your real function here
        messages.append({"role": "tool", "tool_call_id": call["id"], "content": json.dumps(result)})

    final = client.chat.completions.create(model=MODEL, messages=messages, tools=TOOLS)
    print(final["choices"][0]["message"]["content"])


if __name__ == "__main__":
    main()

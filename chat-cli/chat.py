"""A tiny chat program for the terminal, with streamed replies and a history.

    pip install freetheai
    export FREETHEAI_API_KEY="ftai_..."
    python chat.py                       # uses fta/zai/glm-5.3-flash
    python chat.py fta/kimi/k3           # pick a model

Type /quit to leave and /reset to clear the history.
"""

import sys

from freetheai import FreeTheAI, StreamInterruptedError

DEFAULT_MODEL = "fta/zai/glm-5.3-flash"


def main() -> None:
    model = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MODEL
    client = FreeTheAI(fallback_models=["fta/zai/glm-5.3-flash"])
    history = [{"role": "system", "content": "You are a friendly, concise assistant."}]
    print(f"Chatting with {model}. /reset clears the history, /quit exits.")

    while True:
        try:
            line = input("\nyou> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line:
            continue
        if line == "/quit":
            break
        if line == "/reset":
            history = history[:1]
            print("History cleared.")
            continue

        history.append({"role": "user", "content": line})
        pieces: list[str] = []
        print("ai>  ", end="", flush=True)
        try:
            for text in client.chat.completions.stream_text(model=model, messages=history):
                pieces.append(text)
                print(text, end="", flush=True)
            print()
        except StreamInterruptedError as error:
            print(f"\n[stopped early: {error}]")
            pieces.append(error.partial)
        except Exception as error:  # show the message and keep the history usable
            print(f"\n[error: {error}]")
            history.pop()
            continue
        history.append({"role": "assistant", "content": "".join(pieces)})


if __name__ == "__main__":
    main()

"""A small retrieval-augmented answer over the text files in a folder.

Chunks every .md and .txt file, scores the chunks against the question by word
overlap (standard library only), and asks a FreeTheAI model to answer from the
best chunks, citing the file names.

    pip install freetheai
    export FREETHEAI_API_KEY="ftai_..."
    python rag.py ./my-notes "What did we decide about the database?"
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from freetheai import FreeTheAI

MODEL = "glm-5.3"
CHUNK_WORDS = 120
TOP_K = 4
WORD = re.compile(r"[a-z0-9]+")
STOP = {"the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "is", "are", "was", "we", "it", "that", "this", "with"}


def load_chunks(folder: Path) -> list[tuple[str, str]]:
    """Returns (file name, text) pairs, split into chunks of about CHUNK_WORDS words."""
    chunks: list[tuple[str, str]] = []
    for path in sorted(folder.rglob("*")):
        if path.suffix.lower() not in {".md", ".txt"} or not path.is_file():
            continue
        words = path.read_text(encoding="utf-8", errors="replace").split()
        for start in range(0, len(words), CHUNK_WORDS):
            chunks.append((str(path.relative_to(folder)), " ".join(words[start : start + CHUNK_WORDS])))
    return chunks


def score(question: str, text: str) -> float:
    query = {w for w in WORD.findall(question.lower()) if w not in STOP}
    if not query:
        return 0.0
    words = WORD.findall(text.lower())
    hits = sum(1 for w in words if w in query)
    return hits / (len(words) ** 0.5 or 1)


def best_chunks(question: str, chunks: list[tuple[str, str]], k: int = TOP_K) -> list[tuple[str, str]]:
    ranked = sorted(chunks, key=lambda item: score(question, item[1]), reverse=True)
    return [item for item in ranked[:k] if score(question, item[1]) > 0]


def main() -> None:
    if len(sys.argv) < 3:
        raise SystemExit("usage: python rag.py <folder> <question>")
    folder, question = Path(sys.argv[1]), " ".join(sys.argv[2:])
    chunks = load_chunks(folder)
    if not chunks:
        raise SystemExit(f"No .md or .txt files found in {folder}")

    picked = best_chunks(question, chunks)
    if not picked:
        raise SystemExit("No passage matched the question. Try different words.")

    context = "\n\n".join(f"[{name}]\n{text}" for name, text in picked)
    client = FreeTheAI()
    reply = client.chat.completions.create(
        model=MODEL,
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": "Answer only from the passages. Cite the file names in square brackets. "
                "If the passages do not contain the answer, say so.",
            },
            {"role": "user", "content": f"Passages:\n\n{context}\n\nQuestion: {question}"},
        ],
    )
    print(reply["choices"][0]["message"]["content"])


if __name__ == "__main__":
    main()

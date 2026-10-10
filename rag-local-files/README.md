# RAG over local files

A small retrieval-augmented generation example with no vector database. It splits your `.md` and `.txt` files into chunks, picks the chunks that best match the question by word overlap, and asks a model to answer from them and cite the file names.

```bash
pip install freetheai
export FREETHEAI_API_KEY="ftai_..."
python rag.py ./my-notes "What did we decide about the database?"
```

To scale up, swap the scoring for embeddings and a real index. The shape stays the same: retrieve, put the passages in the prompt, and ask the model to answer from them.

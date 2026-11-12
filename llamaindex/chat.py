"""LlamaIndex with FreeTheAI: OpenAILike pointed at the FreeTheAI API base.

    pip install llama-index-llms-openai-like
    export FREETHEAI_API_KEY="ftai_..."
    python chat.py
"""

import os

from llama_index.core.llms import ChatMessage
from llama_index.llms.openai_like import OpenAILike

llm = OpenAILike(
    model="glm-5.3",
    api_base="https://api.freetheai.org/v1",
    api_key=os.environ["FREETHEAI_API_KEY"],
    is_chat_model=True,
    is_function_calling_model=False,
    temperature=0.3,
)

reply = llm.chat(
    [
        ChatMessage(role="system", content="You are a concise assistant."),
        ChatMessage(role="user", content="Explain vector search to a new developer in three sentences."),
    ]
)
print(reply.message.content)

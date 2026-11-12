"""LangChain with FreeTheAI: ChatOpenAI pointed at the FreeTheAI base URL.

    pip install langchain-openai
    export FREETHEAI_API_KEY="ftai_..."
    python chat.py
"""

import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOpenAI(
    model="glm-5.3",
    base_url="https://api.freetheai.org/v1",
    api_key=os.environ["FREETHEAI_API_KEY"],
    temperature=0.4,
)

reply = llm.invoke(
    [
        SystemMessage(content="You are a concise assistant."),
        HumanMessage(content="What is retrieval-augmented generation in two sentences?"),
    ]
)
print(reply.content)

# Streaming works the same way through LangChain's standard interface.
for chunk in llm.stream([HumanMessage(content="Give me three names for a coffee shop.")]):
    print(chunk.content, end="", flush=True)
print()

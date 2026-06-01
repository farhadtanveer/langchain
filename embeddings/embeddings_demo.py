import os
# The new, modern way to import Ollama embeddings:
from langchain_ollama import OllamaEmbeddings

# Ollama embeddings (local)
llm = OllamaEmbeddings(model="nomic-embed-text")

text = input("Enter the text: ")
response = llm.embed_query(text)

print(response)
print(len(response))
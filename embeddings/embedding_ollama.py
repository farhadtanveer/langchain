import os
from langchain_ollama import OllamaEmbeddings

llm = OllamaEmbeddings(model="nomic-embed-text")

text = input("Enter the text: ")
response = llm.embed_query(text)
print(response)
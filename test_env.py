import docx
import os
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import streamlit as st

load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")

print("Environment setup successful!")
llm = ChatGroq(model="llama-3.1-8b-instant"
               ,api_key=groq_key)  # Test Groq
response = llm.invoke("Hello, world!")
print(response.content)
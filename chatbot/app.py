from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Optional: Handle missing keys gracefully
groq_key = os.getenv("GROQ_API_KEY")
langchain_key = os.getenv("LANGCHAIN_API_KEY")

if not groq_key or not langchain_key:
    st.error("Please make sure GROQ_API_KEY and LANGCHAIN_API_KEY are set in the .env file.")
    st.stop()

# Set environment variables only if they exist
os.environ["GROQ_API_KEY"] = groq_key
os.environ["LANGCHAIN_API_KEY"] = langchain_key
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt setup
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to user queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("Langchain Demo with GROQ API")
input_text = st.text_input("Search the topic you want")

# LLM setup
llm = ChatGroq(model="llama-3.1-8b-instant")  # Fixed model name too
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))

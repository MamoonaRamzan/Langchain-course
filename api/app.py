from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn
import os 
from langchain_community.llms import Ollama
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

add_routes(
    app,
    ChatGroq(model="llama-3.1-8b-instant"),
    path="/groqai"
)

model = ChatGroq(model="llama-3.1-8b-instant") 
llm = Ollama(model="llama3.2:1b")  

prompt1=ChatPromptTemplate.from_template("Write an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)


from fastapi import FastAPI
from pydantic import BaseModel

from Src.chatbot import ask_question

app = FastAPI()

class ChatRequest(BaseModel):

    question:str


@app.post("/chat")

def chat(data:ChatRequest):

    answer = ask_question(data.question)

    return {

        "question":data.question,

        "answer":answer

    }

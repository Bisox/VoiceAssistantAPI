from fastapi import FastAPI
from app.routes import chat, voice_chat

app = FastAPI()

app.include_router(chat.router, prefix="/api")
# app.include_router(voice_chat.router, prefix="/api")



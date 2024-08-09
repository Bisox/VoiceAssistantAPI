from fastapi import APIRouter, HTTPException
from app.models import ChatRequest, ChatResponse
from app.utils.chatgpt import get_chatgpt_response

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = get_chatgpt_response(request.message)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

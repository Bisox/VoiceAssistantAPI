from fastapi import APIRouter, HTTPException
from app.models import ChatResponse
from app.utils.speech import recognize_speech, speak
from app.utils.chatgpt import get_chatgpt_response

router = APIRouter()


@router.post("/voice-chat", response_model=ChatResponse)
async def voice_chat():
    message = recognize_speech()
    if message:
        try:
            response = get_chatgpt_response(message)
            speak(response)
            return ChatResponse(response=response)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    else:
        raise HTTPException(status_code=400, detail="Не удалось распознать речь")
import openai
from app.config import settings

openai.api_key = settings.API_KEY


def get_chatgpt_response(message: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Укажите модель, например, gpt-3.5-turbo или другую доступную
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message['content'].strip()

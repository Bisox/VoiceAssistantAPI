import openai

from app.config import settings

openai.api_key = settings.API_KEY


def get_chatgpt_response(message: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=150
    )
    return response.choices[0].text.strip()
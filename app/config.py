from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_KEY: str = 'sk-proj-1qf1kLWVTkJIoac0WTUeT3BlbkFJ39tiwItLtFs6vP4HoyAC'

    class Config:
        env_file = ".env"


settings = Settings()


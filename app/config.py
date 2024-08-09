from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_KEY: str

    class Config:
        env_file = ".env"

    @property
    def API_KEY(self):
        return self.API_KEY


settings = Settings()

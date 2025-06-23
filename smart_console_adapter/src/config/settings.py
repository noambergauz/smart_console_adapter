from pydantic import BaseSettings


class Settings(BaseSettings):
    api_base_url: str = "https://api.checkpoint.com"
    api_key: str
    api_secret: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

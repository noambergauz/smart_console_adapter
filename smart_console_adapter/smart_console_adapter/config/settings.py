from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_base_url: str
    domain: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

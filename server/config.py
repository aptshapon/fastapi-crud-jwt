from decouple import config
from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "FastAPI/MongoDB Test CRUD Application"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str = config("db_url")
    DB_NAME: str = config("db_name")


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()

from decouple import config
from pydantic import BaseSettings
from functools import lru_cache


class CommonSettings(BaseSettings):
    app_name: str = "FastAPI/MongoDB Test CRUD Application"
    debug_mode: bool = True


class ServerSettings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 8000


class DatabaseSettings(BaseSettings):
    db_url: str = config("db_url")
    db_name: str = config("db_name")


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache(maxsize=28)
def get_settings():
    print("From caches")
    return Settings()


settings = Settings()

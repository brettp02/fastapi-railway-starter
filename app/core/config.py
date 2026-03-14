from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="APP_",
        extra="ignore",
    )

    app_name: str = "FastAPI Railway Starter"
    app_description: str = "Minimal FastAPI starter template"
    environment: Literal["local", "test", "production"] = "local"
    debug: bool = False
    log_level: Literal["debug", "info", "warning", "error", "critical"] = "info"


@lru_cache
def get_settings() -> Settings:
    return Settings()

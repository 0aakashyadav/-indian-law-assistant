"""Environment-based application settings."""
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Indian Law AI Assistant"
    app_env: str = "development"
    log_level: str = "INFO"
    cors_origins: str = "http://localhost:8000,http://127.0.0.1:8000"
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore", case_sensitive=False)

    @property
    def allowed_origins(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()

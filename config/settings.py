"""Application settings and configuration"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator
from typing import Any, List, Union

class Settings(BaseSettings):
    """Application settings"""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore"
    )

    log_level: str = "INFO"

    # Google
    google_cloud_project: str = ""
    google_api_key: str = ""

    # Agent
    default_model: str = "gemini-2.0-flash-exp"

    # CORS
    cors_origins: List[str] = ["http://localhost", "http://127.0.0.1"]

    # MCP
    mcp_enabled: bool = False
    mcp_server_url: str = "http://mcp-server:3000"

    # Redis
    redis_url: str = "redis://redis:6379"

    @field_validator('cors_origins', mode='before')
    @classmethod
    def parse_cors_origins(cls, v: Any) -> List[str]:
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(',')]
        return v

settings = Settings()

"""Configuración de infraestructura y variables de entorno."""

from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

load_dotenv(BASE_DIR / ".env")


class Settings(BaseSettings):
    """
    Configuración de la aplicación.
    """

    coingecko_base_url: str = "https://api.coingecko.com/api/v3"

    request_timeout: int = 15

    cache_ttl_seconds: int = 60


settings = Settings()
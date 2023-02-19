import logging
from pydantic import BaseSettings
from functools import lru_cache

log  = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = 0


@lru_cache
def get_settings() -> BaseSettings:
    log.info("loading the configuration settings from the environment")
    return Settings()

   
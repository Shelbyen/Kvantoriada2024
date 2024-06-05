from typing import Optional

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class ConfigDataBase(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_ECHO_LOG: bool = False

    @property
    def database_url(self) -> Optional[PostgresDsn]:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings_db = ConfigDataBase()

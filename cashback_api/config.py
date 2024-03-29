import os
from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel, BaseSettings, PostgresDsn, validator


class EnvironmentEnum(Enum):
    LOCAL = "LOCAL"
    PROD = "PROD"


class DatabaseModel(BaseModel):
    DATABASE_USER: str = "cashback"
    DATABASE_PASS: str = "cashback"
    DATABASE_HOST: str = "db_cashback"
    DATABASE_PORT: str = "5432"
    DATABASE_NAME: str = "cashback"
    DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

    @validator("DATABASE_URL", pre=True)
    def make_db_url(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        return PostgresDsn.build(
            scheme="postgresql",
            user=values["DATABASE_USER"],
            password=values["DATABASE_PASS"],
            host=values["DATABASE_HOST"],
            port=values["DATABASE_PORT"],
            path=f"/{values['DATABASE_NAME']}",
        )


class Envs(BaseSettings):
    ENVIRONMENT: Optional[Enum] = EnvironmentEnum.PROD
    DB_URI: str = DatabaseModel().DATABASE_URL
    SECRET_KEY: str = os.environ.get("SECRET_KEY", None)
    JWT_SECRET: str = os.environ.get("JWT_SECRET", None)
    JWT_ALGORITHM: str = os.environ.get("JWT_ALGORITHM", "HS256")
    CPF_MASTER: str = "15350946056"
    ACUMULADO_CASHBACK: str = "https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com"

    class Config:
        case_sensitive = True


envs = Envs()

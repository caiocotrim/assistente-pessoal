import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = os.getenv(
        "APP_NAME",
        "Assistente Pessoal",
    )

    ENVIRONMENT: str = os.getenv(
        "ENVIRONMENT",
        "development",
    )

    DATABASE_DIR: str = os.getenv(
    "DATABASE_DIR",
    "data",
    )

    DATABASE_NAME: str = os.getenv(
        "DATABASE_NAME",
        "assistant.db",
    )

settings = Settings()
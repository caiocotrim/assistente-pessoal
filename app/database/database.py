import sqlite3
from pathlib import Path

from app.core.config import settings


DATABASE_PATH = Path(settings.DATABASE_DIR) / settings.DATABASE_NAME


def get_connection() -> sqlite3.Connection:
    """Retorna uma conexão com o banco de dados."""

    DATABASE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    connection = sqlite3.connect(DATABASE_PATH)

    return connection


def init_database() -> None:
    """Inicializa o banco de dados."""

    connection = get_connection()

    try:
        connection.execute("SELECT 1")
    finally:
        connection.close()
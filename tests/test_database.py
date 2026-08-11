import sqlite3

from app.database.database import get_connection, init_database


def test_get_connection():
    connection = get_connection()

    try:
        assert isinstance(connection, sqlite3.Connection)
    finally:
        connection.close()


def test_database_connection():
    connection = get_connection()

    try:
        result = connection.execute("SELECT 1").fetchone()

        assert result == (1,)
    finally:
        connection.close()


def test_init_database():
    init_database()
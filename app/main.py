from app.core.error_handler import handle_error
from app.core.logging import get_logger, setup_logging
from app.database.database import init_database


def health_check() -> dict:
    return {"status": "ok"}


def main() -> None:
    setup_logging()

    logger = get_logger(__name__)

    try:
        logger.info("Assistente iniciado")

        init_database()

        logger.info("Banco de dados inicializado")

        result = health_check()

        logger.info("Health check: %s", result)

    except Exception as error:
        handle_error(error)


if __name__ == "__main__":
    main()
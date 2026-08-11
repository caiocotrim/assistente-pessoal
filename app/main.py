from app.core.logging import get_logger, setup_logging


def health_check() -> dict:
    return {"status": "ok"}


def main() -> None:
    setup_logging()

    logger = get_logger(__name__)

    logger.info("Assistente iniciado")

    result = health_check()

    logger.info("Health check: %s", result)


if __name__ == "__main__":
    main()
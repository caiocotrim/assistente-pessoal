from app.core.logging import get_logger, setup_logging


def test_get_logger():
    logger = get_logger("test")

    assert logger.name == "test"


def test_setup_logging():
    setup_logging()

    logger = get_logger("test")
    logger.info("Teste de logging")

    assert logger.hasHandlers()
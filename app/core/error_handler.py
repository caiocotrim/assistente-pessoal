import logging

from app.core.exceptions import AppError


logger = logging.getLogger(__name__)


def handle_error(error: Exception) -> None:
    """Registra uma exceção da aplicação."""

    if isinstance(error, AppError):
        logger.error("Erro da aplicação: %s", error)
        return

    logger.exception("Erro inesperado durante a execução")
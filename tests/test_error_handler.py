import logging

from app import main
from app.core.error_handler import handle_error
from app.core.exceptions import AppError


def test_handle_app_error(caplog):
    with caplog.at_level(logging.ERROR):
        handle_error(AppError("Erro de teste"))

    assert "Erro da aplicação: Erro de teste" in caplog.text


def test_handle_unexpected_error(caplog):
    with caplog.at_level(logging.ERROR):
        try:
            raise ValueError("Erro inesperado")
        except ValueError as error:
            handle_error(error)

    assert "Erro inesperado durante a execução" in caplog.text


def test_main_handles_unexpected_error(monkeypatch):
    def failing_database():
        raise RuntimeError("Falha simulada")

    monkeypatch.setattr(main, "init_database", failing_database)

    main.main()

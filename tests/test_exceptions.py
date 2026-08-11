import pytest

from app.core.exceptions import AppError


def test_app_error():
    with pytest.raises(AppError):
        raise AppError("Erro de teste")
from app.core.config import settings


def test_settings():
    assert settings.APP_NAME == "Assistente Pessoal"
    assert settings.ENVIRONMENT == "development"
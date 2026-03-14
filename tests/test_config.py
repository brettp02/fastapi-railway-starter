from app.core.config import get_settings


def test_get_settings_reads_app_prefixed_env_vars(monkeypatch):
    get_settings.cache_clear()
    monkeypatch.setenv("APP_APP_NAME", "Configured Test App")
    monkeypatch.setenv("APP_DEBUG", "true")
    monkeypatch.setenv("APP_ENVIRONMENT", "test")
    monkeypatch.setenv("APP_LOG_LEVEL", "debug")

    settings = get_settings()

    assert settings.app_name == "Configured Test App"
    assert settings.debug is True
    assert settings.environment == "test"
    assert settings.log_level == "debug"

    get_settings.cache_clear()

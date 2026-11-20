import pytest

from src.config import (
    get_model,
    get_temperature,
    get_max_output_tokens,
    get_timeout,
)


def test_model_configuration(monkeypatch):
    monkeypatch.setenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash-lite"
    )

    assert get_model() == "gemini-2.5-flash-lite"


def test_temperature_configuration(monkeypatch):
    monkeypatch.setenv("GEMINI_TEMPERATURE", "0.5")

    assert get_temperature() == 0.5


def test_invalid_temperature(monkeypatch):
    monkeypatch.setenv("GEMINI_TEMPERATURE", "-1")

    with pytest.raises(ValueError):
        get_temperature()


def test_max_output_tokens(monkeypatch):
    monkeypatch.setenv("GEMINI_MAX_OUTPUT_TOKENS", "1024")

    assert get_max_output_tokens() == 1024


def test_invalid_max_output_tokens(monkeypatch):
    monkeypatch.setenv("GEMINI_MAX_OUTPUT_TOKENS", "0")

    with pytest.raises(ValueError):
        get_max_output_tokens()


def test_timeout_configuration(monkeypatch):
    monkeypatch.setenv("GEMINI_TIMEOUT_MS", "15000")

    assert get_timeout() == 15000


def test_invalid_timeout(monkeypatch):
    monkeypatch.setenv("GEMINI_TIMEOUT_MS", "-100")

    with pytest.raises(ValueError):
        get_timeout()
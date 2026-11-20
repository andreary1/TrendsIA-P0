import json

import pytest

from src import client


VALID_RESPONSE = {
    "resumo": "Entrega de trabalho.",
    "tarefas": ["Enviar relatório"],
    "prazos": ["27/11/2026"],
    "requisitos": ["PDF"],
    "observacoes": []
}


class FakeResponse:
    def __init__(self, text):
        self.text = text


class FakeModels:
    def __init__(self, response):
        self.response = response

    def generate_content(self, **kwargs):
        return self.response


class FakeClient:
    def __init__(self, response):
        self.models = FakeModels(response)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False


def configure_fake_client(monkeypatch, response):
    monkeypatch.setattr(
        client,
        "get_api_key",
        lambda: "fake-api-key"
    )

    monkeypatch.setattr(
        client,
        "get_model",
        lambda: "gemini-2.5-flash-lite"
    )

    monkeypatch.setattr(
        client,
        "get_temperature",
        lambda: 0.2
    )

    monkeypatch.setattr(
        client,
        "get_max_output_tokens",
        lambda: 2048
    )

    monkeypatch.setattr(
        client,
        "get_timeout",
        lambda: 30000
    )

    monkeypatch.setattr(
        client.genai,
        "Client",
        lambda **kwargs: FakeClient(response)
    )


def test_generate_valid_response(monkeypatch):
    response = FakeResponse(json.dumps(VALID_RESPONSE))

    configure_fake_client(monkeypatch, response)

    result = client.generate_response(
        "Comunicado de teste"
    )

    assert result == VALID_RESPONSE


def test_generate_empty_response(monkeypatch):
    configure_fake_client(
        monkeypatch,
        FakeResponse("")
    )

    with pytest.raises(ValueError, match="resposta vazia"):
        client.generate_response(
            "Comunicado de teste"
        )


def test_generate_invalid_json(monkeypatch):
    configure_fake_client(
        monkeypatch,
        FakeResponse("JSON inválido")
    )

    with pytest.raises(ValueError, match="JSON inválido"):
        client.generate_response(
            "Comunicado de teste"
        )


def test_missing_api_key(monkeypatch):
    monkeypatch.setattr(
        client,
        "get_api_key",
        lambda: None
    )

    with pytest.raises(ValueError, match="GEMINI_API_KEY"):
        client.generate_response(
            "Comunicado de teste"
        )
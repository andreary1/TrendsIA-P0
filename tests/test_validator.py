import pytest

from src.validators import validate_input, validate_response


def test_valid_input():
    result = validate_input("  Prova amanhã.  ")
    assert result == "Prova amanhã."


def test_empty_input():
    with pytest.raises(ValueError):
        validate_input("   ")


def test_invalid_input_type():
    with pytest.raises(ValueError):
        validate_input(123)


def test_valid_response():
    data = {
        "resumo": "Prova de matemática.",
        "tarefas": ["Estudar"],
        "prazos": ["25/11/2026"],
        "requisitos": [],
        "observacoes": []
    }

    assert validate_response(data) == data


def test_missing_field():
    data = {
        "resumo": "Prova de matemática.",
        "tarefas": [],
        "prazos": [],
        "requisitos": []
    }

    with pytest.raises(ValueError):
        validate_response(data)


def test_invalid_field_type():
    data = {
        "resumo": "Prova de matemática.",
        "tarefas": "Estudar",
        "prazos": [],
        "requisitos": [],
        "observacoes": []
    }

    with pytest.raises(ValueError):
        validate_response(data)


def test_invalid_list_item():
    data = {
        "resumo": "Prova de matemática.",
        "tarefas": [123],
        "prazos": [],
        "requisitos": [],
        "observacoes": []
    }

    with pytest.raises(ValueError):
        validate_response(data)
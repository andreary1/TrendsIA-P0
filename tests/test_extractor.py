from src.extractor import build_prompt
import unicodedata


def normalize_text(text):
    text = text.lower()

    return "".join(
        char
        for char in unicodedata.normalize("NFD", text)
        if unicodedata.category(char) != "Mn"
    )


def test_prompt_contains_announcement():
    announcement = "A prova será na sexta-feira."

    prompt = build_prompt(announcement)

    assert announcement in prompt


def test_prompt_contains_required_fields():
    prompt = normalize_text(
        build_prompt("Comunicado de teste.")
    )

    for field in (
        "resumo",
        "tarefas",
        "prazos",
        "requisitos",
        "observacoes",
    ):
        assert field in prompt


def test_prompt_delimits_announcement():
    prompt = build_prompt("Comunicado de teste.")

    assert "<COMUNICADO>" in prompt
    assert "</COMUNICADO>" in prompt
import json

from google import genai
from google.genai import types

from .config import get_api_key, get_model


ANNOUNCEMENT_SCHEMA = {
    "type": "object",
    "properties": {
        "resumo": {
            "type": "string"
        },
        "tarefas": {
            "type": "array",
            "items": {"type": "string"}
        },
        "prazos": {
            "type": "array",
            "items": {"type": "string"}
        },
        "requisitos": {
            "type": "array",
            "items": {"type": "string"}
        },
        "observacoes": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "required": [
        "resumo",
        "tarefas",
        "prazos",
        "requisitos",
        "observacoes"
    ],
    "additionalProperties": False
}


def generate_response(prompt):
    client = genai.Client(
        api_key=get_api_key()
    )

    response = client.models.generate_content(
        model=get_model(),
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_json_schema=ANNOUNCEMENT_SCHEMA
        )
    )

    return json.loads(response.text)
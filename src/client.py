import json

import httpx
from google import genai
from google.genai import errors, types

from .config import (
    get_api_key,
    get_model,
    get_temperature,
    get_max_output_tokens,
    get_timeout,
)

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
    api_key = get_api_key()

    if not api_key or not api_key.strip():
        raise ValueError(
            "A chave GEMINI_API_KEY não foi configurada."
        )

    try:
        with genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(
                timeout=get_timeout()
            )
        ) as client:
            response = client.models.generate_content(
                model=get_model(),
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_json_schema=ANNOUNCEMENT_SCHEMA,
                    temperature=get_temperature(),
                    max_output_tokens=get_max_output_tokens()
                )
            )

    except errors.APIError as erro:
        codigo = erro.code

        if codigo in (401, 403):
            raise RuntimeError(
                "Não foi possível autenticar no Gemini. "
                "Verifique sua chave de API e suas permissões."
            ) from erro

        if codigo == 400:
            raise RuntimeError(
                "A API rejeitou a solicitação. "
                "Verifique a configuração do modelo."
            ) from erro

        if codigo == 429:
            raise RuntimeError(
                "O limite de requisições do Gemini foi atingido. "
                "Tente novamente mais tarde."
            ) from erro

        if codigo in (500, 502, 503, 504):
            raise RuntimeError(
                "O serviço Gemini está temporariamente indisponível."
            ) from erro

        raise RuntimeError(
            "Não foi possível concluir a solicitação ao Gemini."
        ) from erro

    except httpx.TimeoutException as erro:
        raise RuntimeError(
            "A solicitação demorou demais. "
            "Verifique sua conexão e tente novamente."
        ) from erro

    except httpx.RequestError as erro:
        raise RuntimeError(
            "Não foi possível conectar ao Gemini. "
            "Verifique sua conexão com a internet."
        ) from erro

    if not response.text:
        raise ValueError(
            "A IA retornou uma resposta vazia."
        )

    try:
        dados = json.loads(response.text)

    except json.JSONDecodeError as erro:
        raise ValueError(
            "A IA retornou um JSON inválido."
        ) from erro

    return dados
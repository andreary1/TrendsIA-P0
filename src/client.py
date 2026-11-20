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
from .logger import logger


ANNOUNCEMENT_SCHEMA = {
    "type": "object",
    "properties": {
        "resumo": {"type": "string"},
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
        logger.warning("Chave de API não configurada.")
        raise ValueError(
            "A chave GEMINI_API_KEY não foi configurada."
        )

    # Carrega e valida as configurações antes da requisição.
    model = get_model()
    temperature = get_temperature()
    max_output_tokens = get_max_output_tokens()
    timeout = get_timeout()

    try:
        logger.info("Solicitação ao Gemini iniciada.")

        with genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(timeout=timeout)
        ) as client:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_json_schema=ANNOUNCEMENT_SCHEMA,
                    temperature=temperature,
                    max_output_tokens=max_output_tokens
                )
            )

        logger.info("Resposta recebida do Gemini.")

    except errors.APIError as erro:
        codigo = erro.code

        if codigo in (401, 403):
            logger.error("Falha de autenticação na API.")
            raise RuntimeError(
                "Não foi possível autenticar no Gemini. "
                "Verifique sua chave de API e suas permissões."
            ) from erro

        if codigo == 400:
            logger.error("Solicitação rejeitada pela API.")
            raise RuntimeError(
                "A API rejeitou a solicitação. "
                "Verifique a configuração do modelo."
            ) from erro

        if codigo == 429:
            logger.warning("Limite de requisições atingido.")
            raise RuntimeError(
                "O limite de requisições do Gemini foi atingido. "
                "Tente novamente mais tarde."
            ) from erro

        if codigo in (500, 502, 503, 504):
            logger.error("Serviço Gemini indisponível.")
            raise RuntimeError(
                "O serviço Gemini está temporariamente indisponível."
            ) from erro

        logger.error("Solicitação ao Gemini rejeitada.")
        raise RuntimeError(
            "Não foi possível concluir a solicitação ao Gemini."
        ) from erro

    except httpx.TimeoutException as erro:
        logger.error("Timeout na comunicação com o Gemini.")
        raise RuntimeError(
            "A solicitação demorou demais. "
            "Verifique sua conexão e tente novamente."
        ) from erro

    except httpx.RequestError as erro:
        logger.error("Falha de conexão com o Gemini.")
        raise RuntimeError(
            "Não foi possível conectar ao Gemini. "
            "Verifique sua conexão com a internet."
        ) from erro

    # Verifica se a resposta contém texto.
    if not response.text:
        logger.error("Resposta vazia recebida do Gemini.")
        raise ValueError(
            "A IA retornou uma resposta vazia."
        )

    # Converte a resposta JSON em um dicionário Python.
    try:
        dados = json.loads(response.text)

    except json.JSONDecodeError as erro:
        logger.error("JSON inválido recebido do Gemini.")
        raise ValueError(
            "A IA retornou um JSON inválido."
        ) from erro

    logger.info("JSON convertido com sucesso.")

    return dados
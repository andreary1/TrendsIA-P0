import os

from dotenv import load_dotenv


load_dotenv()


def get_api_key():
    return os.getenv("GEMINI_API_KEY")


def get_model():
    return os.getenv(
        "GEMINI_MODEL",
        "gemini-3.5-flash-lite"
    )


def get_temperature():
    value = float(
        os.getenv("GEMINI_TEMPERATURE", "0.2")
    )

    if not 0 <= value <= 2:
        raise ValueError(
            "GEMINI_TEMPERATURE deve estar entre 0 e 2."
        )

    return value


def get_max_output_tokens():
    value = int(
        os.getenv("GEMINI_MAX_OUTPUT_TOKENS", "2048")
    )

    if value <= 0:
        raise ValueError(
            "GEMINI_MAX_OUTPUT_TOKENS deve ser positivo."
        )

    return value


def get_timeout():
    value = int(
        os.getenv("GEMINI_TIMEOUT_MS", "30000")
    )

    if value <= 0:
        raise ValueError(
            "GEMINI_TIMEOUT_MS deve ser positivo."
        )

    return value
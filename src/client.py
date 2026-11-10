from google import genai

from .config import get_api_key, get_model


def generate_response(prompt):
    client = genai.Client(
        api_key=get_api_key()
    )

    response = client.models.generate_content(
        model=get_model(),
        contents=prompt
    )

    return response.text
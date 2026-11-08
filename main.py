import os

from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

    client = genai.Client(api_key=api_key)

    prompt = (
        "Explique brevemente o que é um comunicado acadêmico "
        "e por que é importante identificar suas informações."
    )

    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )

    print("\nResposta do Gemini:\n")
    print(response.text)


if __name__ == "__main__":
    main()
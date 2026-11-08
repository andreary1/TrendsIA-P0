import os

from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

    client = genai.Client(api_key=api_key)

    print("=" * 50)
    print("       COMUNICADO AI")
    print("=" * 50)

    print("\nDigite o comunicado acadêmico abaixo.")
    print("Pressione ENTER duas vezes para finalizar.\n")

    linhas = []

    while True:
        linha = input()

        if linha == "":
            break

        linhas.append(linha)

    comunicado = "\n".join(linhas)

    response = client.models.generate_content(
        model=model,
        contents=comunicado,
    )

    print("\n" + "=" * 50)
    print("       RESPOSTA DO GEMINI")
    print("=" * 50)

    print(response.text)


if __name__ == "__main__":
    main()
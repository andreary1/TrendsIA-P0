import json

from .extractor import build_prompt
from .client import generate_response


def main():
    print("=" * 50)
    print("                 COMUNICADO AI")
    print("=" * 50)

    print("\nDigite o comunicado acadêmico abaixo.")
    print("Pressione ENTER em uma linha vazia para finalizar.\n")


    linhas = []

    while True:
        linha = input()

        if linha == "":
            break

        linhas.append(linha)

    comunicado = "\n".join(linhas)

    prompt = build_prompt(comunicado)

    dados = generate_response(prompt)

    print("\n" + "=" * 50)
    print("          DADOS EXTRAÍDOS")
    print("=" * 50 + "\n")

    print(
        json.dumps(
            dados,
            ensure_ascii=False,
            indent=2
        )
    )


if __name__ == "__main__":
    main()
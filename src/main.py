from .extractor import build_prompt
from .formatter import display_response
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

    response = generate_response(prompt)

    display_response(response)


if __name__ == "__main__":
    main()
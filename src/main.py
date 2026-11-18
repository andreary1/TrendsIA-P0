from .extractor import build_prompt
from .formatter import display_response
from .client import generate_response


def main():
    # Apresentação do programa
    print("=" * 50)
    print("                 COMUNICADO AI")
    print("=" * 50)

    print("\nDigite o comunicado acadêmico abaixo.")
    print("Pressione ENTER em uma linha vazia para finalizar.\n")

    # Captura a entrada do usuário
    linhas = []

    while True:
        linha = input()

        if linha == "":
            break

        linhas.append(linha)

    comunicado = "\n".join(linhas)

    # Constrói o prompt
    prompt = build_prompt(comunicado)

    # Envia a solicitação ao Gemini
    dados = generate_response(prompt)

    # Apresenta as informações formatadas
    display_response(dados)


if __name__ == "__main__":
    main()
from .extractor import build_prompt
from .formatter import display_response
from .client import generate_response
from .validators import validate_input, validate_response


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

    # Validação da entrada
    try:
        comunicado = validate_input(comunicado)
    except ValueError as erro:
        print(f"\nErro de entrada: {erro}")
        return

    # Construção do prompt
    prompt = build_prompt(comunicado)

    # Comunicação com o Gemini
    dados = generate_response(prompt)

    # Validação da resposta
    try:
        dados = validate_response(dados)
    except ValueError as erro:
        print(f"\nErro na resposta da IA: {erro}")
        return

    # Apresentação
    display_response(dados)


if __name__ == "__main__":
    main()
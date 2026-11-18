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

    try:
        while True:
            linha = input()

            if linha == "":
                break

            linhas.append(linha)

        comunicado = "\n".join(linhas)

        # Valida a entrada
        comunicado = validate_input(comunicado)

        # Constrói o prompt
        prompt = build_prompt(comunicado)

        # Solicita a interpretação ao Gemini
        dados = generate_response(prompt)

        # Valida a resposta
        dados = validate_response(dados)

        # Apresenta o resultado
        display_response(dados)

    except (ValueError, RuntimeError) as erro:
        print(f"\n[ERRO] {erro}")

    except (KeyboardInterrupt, EOFError):
        print("\nOperação cancelada pelo usuário.")


if __name__ == "__main__":
    main()
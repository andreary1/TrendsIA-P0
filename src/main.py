from .extractor import build_prompt
from .formatter import display_response
from .client import generate_response
from .logger import logger, setup_logging
from .validators import validate_input, validate_response


def main():
    setup_logging()

    logger.info("Aplicação iniciada.")

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

        # Validação da entrada
        comunicado = validate_input(comunicado)
        logger.info("Entrada validada.")

        # Construção do prompt
        prompt = build_prompt(comunicado)

        # Comunicação com o Gemini
        dados = generate_response(prompt)

        # Validação da resposta
        dados = validate_response(dados)
        logger.info("Resposta validada.")

        # Apresentação
        display_response(dados)

        logger.info("Processamento concluído.")

    except ValueError:
        logger.warning("Falha na validação dos dados.")
        print("\n[ERRO] Entrada ou resposta inválida.")

    except RuntimeError as erro:
        logger.error("Falha durante o processamento.")
        print(f"\n[ERRO] {erro}")

    except (KeyboardInterrupt, EOFError):
        logger.warning("Execução interrompida pelo usuário.")
        print("\nOperação cancelada pelo usuário.")


if __name__ == "__main__":
    main()
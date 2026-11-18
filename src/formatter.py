def display_response(dados):
    print("\n" + "=" * 50)
    print("          INTERPRETAÇÃO DO COMUNICADO")
    print("=" * 50)

    # Resumo
    print("\nRESUMO")
    print(dados["resumo"] or "Não informado.")

    # Demais categorias
    secoes = {
        "TAREFAS": "tarefas",
        "PRAZOS": "prazos",
        "REQUISITOS": "requisitos",
        "OBSERVAÇÕES": "observacoes"
    }

    for titulo, chave in secoes.items():
        print("\n" + "-" * 50)
        print(titulo)
        print("-" * 50)

        itens = dados[chave]

        if itens:
            for item in itens:
                print(f"• {item}")
        else:
            print("Não informado.")

    print("\n" + "=" * 50)
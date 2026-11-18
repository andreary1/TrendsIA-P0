def validate_input(comunicado):
    if not isinstance(comunicado, str):
        raise ValueError(
            "O comunicado deve ser um texto."
        )

    if not comunicado.strip():
        raise ValueError(
            "O comunicado não pode estar vazio."
        )

    return comunicado.strip()


def validate_response(dados):
    if not isinstance(dados, dict):
        raise ValueError(
            "A resposta da IA deve ser um objeto JSON."
        )

    campos = {
        "resumo": str,
        "tarefas": list,
        "prazos": list,
        "requisitos": list,
        "observacoes": list
    }

    for campo, tipo in campos.items():
        if campo not in dados:
            raise ValueError(
                f"Campo obrigatório ausente: {campo}"
            )

        if not isinstance(dados[campo], tipo):
            raise ValueError(
                f"Tipo inválido para o campo: {campo}"
            )

    for campo in (
        "tarefas",
        "prazos",
        "requisitos",
        "observacoes"
    ):
        if not all(
            isinstance(item, str)
            for item in dados[campo]
        ):
            raise ValueError(
                f"Os itens de '{campo}' devem ser textos."
            )

    return dados
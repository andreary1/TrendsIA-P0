# Relatório de Execução — ComunicadoAI

## 1. Identificação

**Projeto:** ComunicadoAI  
**Repositório:** https://github.com/andreary1/TrendsIA-P0  
**Linguagem:** Python  
**Modelo de IA:** Gemini 3.5 Flash-Lite  
**Interface:** Terminal (CLI)

## 2. Objetivo

O ComunicadoAI foi desenvolvido para interpretar comunicados acadêmicos escritos em linguagem natural e organizar suas principais informações em cinco categorias: resumo, tarefas, prazos, requisitos e observações.

A aplicação utiliza um modelo de linguagem para interpretar o conteúdo, uma estrutura JSON para representar os resultados e mecanismos de validação para identificar respostas incompatíveis com o formato esperado.

## 3. Desenvolvimento

O projeto foi implementado em três níveis incrementais.

### Nível básico

Implementação da primeira versão funcional, incluindo entrada de comunicados pelo terminal, integração com a API do Gemini, construção do prompt e apresentação dos resultados.

### Nível intermediário

Refatoração da aplicação em módulos independentes, extração estruturada em JSON, validação de entradas e respostas e tratamento de falhas relacionadas à API.

### Nível avançado

Implementação de parâmetros configuráveis para o modelo, registros de execução com a biblioteca `logging` e testes automatizados com `pytest`.

Os testes utilizam simulações para verificar o comportamento da aplicação sem depender de chamadas reais ao Gemini.

## 4. Arquitetura

O código-fonte está organizado no pacote `src`, com responsabilidades separadas:

- `main.py`: coordenação da execução.
- `config.py`: carregamento e validação das configurações.
- `extractor.py`: construção do prompt.
- `llm_client.py`: comunicação com o Gemini e tratamento de falhas.
- `validators.py`: validação de entradas e respostas.
- `formatter.py`: apresentação dos resultados.
- `logger.py`: configuração dos logs.

Os testes automatizados estão organizados no diretório `tests`.

## 5. Testes e validação

Os testes automatizados foram desenvolvidos com `pytest` e abrangem validações de entrada, estrutura das respostas, configurações, construção do prompt e comportamento do cliente da API diante de respostas simuladas.

**Comando de execução:**

`python -m pytest -v`

**Resultado da execução:** 21 testes aprovados, 0 falhas e nenhum aviso reportado. Execução em 20/11/2026, com duração de 1,21 segundo.

**Versão do Python:** Python 3.14.2

**Versão do pytest:** pytest 9.2.0

**Validação em ambiente limpo:** Pendente. Os testes foram executados no ambiente virtual existente do projeto.

Além dos testes automatizados, recomenda-se verificar manualmente a interpretação de comunicados reais ou fictícios com diferentes estruturas e prazos.

## 6. Segurança

As credenciais da API são configuradas por variáveis de ambiente e não são incluídas no repositório.

Os logs registram eventos operacionais sem armazenar o conteúdo dos comunicados, as respostas do modelo ou a chave da API.

Os comunicados são enviados a um serviço externo de inteligência artificial, portanto não devem conter informações confidenciais.

## 7. Limitações

O sistema depende da disponibilidade do Gemini e de uma conexão com a internet para interpretar comunicados.

Embora a resposta seja validada estruturalmente, isso não garante a precisão de todas as informações extraídas.

Datas ambíguas e orientações incompletas devem ser conferidas com o comunicado original.

## 8. Resultado final

O ComunicadoAI reúne os componentes previstos nos três níveis do projeto: integração com LLM, interpretação estruturada, validações, tratamento de erros, parâmetros configuráveis, logs e testes automatizados.

A aplicação demonstra a utilização de um modelo de linguagem integrado a um programa Python, com organização modular e mecanismos básicos de robustez e testabilidade.

## 9. Demonstração

**Vídeo de execução:** Ainda será gravado

**Versão final:** `p0-avancado`
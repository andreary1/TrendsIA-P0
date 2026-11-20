# Relatório de Execução — ComunicadoAI

## 1. Identificação

**Projeto:** ComunicadoAI  
**Repositório:** https://github.com/andreary1/TrendsIA-P0  
**Linguagem:** Python  
**Modelo de IA:** Google Gemini  
**Interface:** Terminal (CLI)

## 2. Objetivo

O ComunicadoAI foi desenvolvido para interpretar comunicados acadêmicos escritos em linguagem natural e organizar suas informações em cinco categorias: resumo, tarefas, prazos, requisitos e observações.

A aplicação utiliza um modelo de linguagem para interpretar os textos e retorna informações estruturadas em JSON, posteriormente validadas e apresentadas no terminal.

## 3. Evolução por nível

O desenvolvimento foi organizado em três etapas incrementais, identificadas por tags no repositório.

### Básico (`p0-basico`)

Foi implementada a primeira versão funcional, com entrada de comunicados pelo terminal, integração com a API do Gemini, construção de um prompt especializado e apresentação das informações extraídas.

### Intermediário (`p0-intermediario`)

A aplicação foi reorganizada em módulos independentes. Foram acrescentadas respostas estruturadas em JSON, validação de entradas e respostas e tratamento de falhas de autenticação, conexão e indisponibilidade da API.

### Avançado (`p0-avancado`)

Foram implementados parâmetros configuráveis para temperatura, limite de tokens e timeout, registros de execução com `logging` e testes automatizados com `pytest`, incluindo simulações da API.

Também foi corrigida a leitura de comunicados com múltiplos parágrafos, permitindo preservar linhas vazias por meio do marcador de encerramento `FIM`.

## 4. Decisões principais

| Decisão tomada | Alternativa considerada | Justificativa |
|---|---|---|
| Utilizar Google Gemini | Extração por expressões regulares e regras fixas | Interpretar comunicados com diferentes estruturas e construções de linguagem natural. |
| Solicitar respostas em JSON | Receber respostas em texto livre | Facilitar a validação, organização e apresentação das informações. |
| Utilizar pytest com simulações da API | Depender exclusivamente de requisições reais | Permitir testes reproduzíveis sem depender da conexão ou da disponibilidade do serviço. |
| Utilizar o marcador `FIM` | Encerrar a entrada ao encontrar uma linha vazia | Permitir a inserção de textos com múltiplos parágrafos sem interromper a leitura. |

## 5. Testes e resultados

Os testes automatizados foram desenvolvidos com `pytest` e utilizam simulações para verificar componentes da aplicação sem realizar requisições reais ao Gemini.

| Teste | Entrada ou situação | Resultado esperado | Resultado obtido |
|---|---|---|---|
| Validação de entrada | Comunicado vazio | Rejeitar entrada inválida | Aprovado |
| Validação de resposta | JSON com estrutura incompatível | Identificar resposta inválida | Aprovado |
| Configuração | Parâmetros inválidos | Rejeitar configurações incorretas | Aprovado |
| Construção do prompt | Comunicado válido | Incluir as categorias necessárias | Aprovado |
| Comunicação simulada | Resposta válida da API | Processar o JSON retornado | Aprovado |
| Falha simulada | Erro de comunicação com a API | Apresentar tratamento de erro | Aprovado |
| Entrada multiline | Comunicado com linhas vazias | Preservar o texto até o marcador `FIM` | Aprovado em teste manual |

**Resultados registrados:**

- **Testes automatizados:** 21 aprovados, sem falhas na execução anteriormente registrada.
- **Validação após a correção:** suíte executada novamente com sucesso.
- **Teste manual:** leitura de comunicado com múltiplos parágrafos validada.
- **Python:** 3.14.2.
- **pytest:** 9.2.0.
- **Ambiente limpo:** validação ainda pendente.

Os testes simulados verificam o comportamento do código, mas não comprovam a disponibilidade da API ou a precisão das interpretações em chamadas reais.

## 6. Falhas e limitações

### 6.1. Falha identificada e corrigida

Durante um teste manual, foi identificado que a aplicação encerrava a leitura de comunicados ao encontrar uma linha vazia. Ao colar um texto com múltiplos parágrafos, apenas o primeiro trecho era processado, e as linhas restantes podiam ser interpretadas pelo terminal como comandos.

A falha foi identificada ao testar um comunicado sobre a entrega de um trabalho e uma avaliação acadêmica.

Para corrigir o problema, a lógica de entrada foi modificada para utilizar o marcador `FIM` em uma linha isolada. A correção foi verificada por meio de teste manual, e a suíte automatizada foi executada novamente sem falhas.

### 6.2. Limitações conhecidas

A aplicação depende de conexão com a internet e da disponibilidade da API do Gemini. Além disso, a validação da estrutura JSON não garante a precisão das informações extraídas.

Datas ambíguas e orientações incompletas ainda exigem conferência com o comunicado original.

## 7. Uso de IA no desenvolvimento

O ChatGPT foi utilizado como ferramenta de apoio ao planejamento, à implementação, aos testes e à documentação do projeto.

| Tarefa delegada | Resultado aproveitado | Correções ou alterações realizadas | Forma de verificação |
|---|---|---|---|
| Organização da arquitetura | Separação do código em módulos independentes | Adaptação da estrutura às funcionalidades do projeto | Revisão dos módulos e execução da aplicação |
| Integração com o Gemini | Exemplos de comunicação com a API e tratamento de erros | Ajustes nos parâmetros e na estrutura das respostas | Execução e testes da aplicação |
| Desenvolvimento de testes | Casos de teste com pytest | Correção da comparação de textos com diferenças de maiúsculas e acentuação | Execução da suíte automatizada |
| Documentação | Estruturação do README e do relatório | Revisão conforme os requisitos da atividade e a implementação | Conferência dos arquivos e comandos |

As sugestões geradas por IA foram revisadas e adaptadas durante o desenvolvimento. A validação das funcionalidades foi realizada por meio de testes automatizados e manuais.

## 8. Reflexão final

O principal aprendizado foi compreender como integrar um modelo de linguagem a uma aplicação Python, considerando não apenas a geração de respostas, mas também a validação dos dados, o tratamento de falhas e a organização do código.

A competência mais desenvolvida foi a construção de uma aplicação modular e testável, especialmente com a utilização de testes automatizados e simulações de serviços externos.

Como aspecto a aprimorar, destaca-se a ampliação dos testes de integração real com o Gemini e a implementação de mecanismos adicionais para verificar a precisão das informações extraídas.

## 9. Demonstração

**Vídeo de execução:** Ainda será adicionado

**Repositório:** https://github.com/andreary1/TrendsIA-P0

**Versão:** `p0-avancado`
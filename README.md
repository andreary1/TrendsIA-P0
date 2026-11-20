# TrendsIA-P0 (PRIMEIRO-FLUXO-LLM) — ComunicadoAI

**Interpretador Inteligente de Comunicados Acadêmicos**

O ComunicadoAI é uma aplicação desenvolvida em Python que utiliza a API do Google Gemini para interpretar comunicados acadêmicos, extrair informações estruturadas e apresentá-las de maneira clara e organizada no terminal.

## 1. Problema

Estudantes universitários recebem frequentemente comunicados acadêmicos contendo informações sobre avaliações, trabalhos, prazos, alterações de horários e orientações importantes.

Essas informações podem aparecer em textos extensos, informais ou pouco estruturados, exigindo que os estudantes identifiquem manualmente as atividades e os prazos relevantes.

O ComunicadoAI busca facilitar esse processo por meio da interpretação automatizada desses textos.

### 1.1. Público-alvo

A aplicação é destinada principalmente a estudantes universitários que precisam consultar e organizar informações recebidas em comunicados acadêmicos.

Também pode ser utilizada por professores e pequenas organizações educacionais que desejem identificar rapidamente tarefas, datas e requisitos presentes em textos informativos.

## 2. Objetivo

Desenvolver uma aplicação capaz de receber comunicados acadêmicos escritos em linguagem natural e utilizar um modelo de linguagem para identificar e organizar suas principais informações.

O sistema apresenta cinco categorias:

- **Resumo:** síntese do conteúdo do comunicado.
- **Tarefas:** atividades que o estudante precisa realizar.
- **Prazos:** datas e horários identificados.
- **Requisitos:** formatos, plataformas, materiais e condições necessárias.
- **Observações:** alterações de prazo, cancelamentos e outras informações relevantes.

Além da interpretação dos comunicados, a aplicação realiza validações de entrada e resposta, apresenta mensagens de erro compreensíveis e organiza suas funcionalidades em módulos independentes.

### 2.1. Justificativa para utilizar um LLM

Comunicados acadêmicos podem apresentar informações de maneiras diferentes, utilizando linguagem informal, referências indiretas e expressões temporais como "amanhã" ou "próxima semana".

Uma solução baseada exclusivamente em regras fixas ou expressões regulares teria dificuldades para interpretar essa variedade de construções.

A utilização de um Large Language Model (LLM) permite analisar o contexto do comunicado e identificar informações relevantes mesmo quando não seguem um formato previamente definido.

Entretanto, a interpretação gerada pelo modelo não garante a veracidade dos dados extraídos, sendo necessária a conferência das informações importantes.

## 3. Tecnologias utilizadas

- Python 3.10 ou superior.
- Google Gemini API.
- Modelo Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`, sujeito à conferência com a configuração utilizada).
- `google-genai` para integração com a API.
- `python-dotenv` para carregamento de variáveis de ambiente.
- `httpx` para tratamento de falhas de comunicação.
- `pytest` para testes automatizados.
- `logging`, biblioteca nativa do Python, para registros de execução.
- `unicodedata`, biblioteca nativa utilizada na normalização de textos nos testes.
- JSON para representação estruturada das informações.
- Git e GitHub para versionamento.

## 4. Estrutura do projeto

```text
TrendsIA-P0/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── client.py
│   ├── extractor.py
│   ├── formatter.py
│   ├── validators.py
│   └── logger.py
├── tests/
│   ├── test_validators.py
│   ├── test_config.py
│   ├── test_extractor.py
│   └── test_client.py
├── RELATORIO_EXECUCAO.md
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

**Descrição dos principais arquivos:**

- `src/main.py`: coordena o fluxo principal da aplicação e recebe os comunicados pelo terminal.
- `src/config.py`: carrega e valida as configurações e os parâmetros do modelo.
- `src/client.py`: realiza a comunicação com a API do Gemini e trata falhas operacionais.
- `src/extractor.py`: constrói o prompt utilizado na interpretação.
- `src/formatter.py`: organiza e apresenta as informações extraídas.
- `src/validators.py`: valida as entradas e a estrutura das respostas.
- `src/logger.py`: configura os registros de execução.
- `tests/`: contém os testes automatizados.
- `RELATORIO_EXECUCAO.md`: documenta as decisões, os testes, as falhas e os resultados do desenvolvimento.
- `.env.example`: apresenta as variáveis de ambiente necessárias.
- `requirements.txt`: relaciona as dependências do projeto.

O arquivo `.env` contém a chave de acesso à API e deve permanecer apenas no ambiente local.

## 5. Instalação

### 5.1. Clonar o repositório

```bash
git clone https://github.com/andreary1/TrendsIA-P0.git
cd TrendsIA-P0
```

### 5.2. Criar um ambiente virtual

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

### 5.3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

As principais dependências são:

```text
google-genai
python-dotenv
httpx
pytest
```

As bibliotecas `logging` e `unicodedata` fazem parte da biblioteca padrão do Python e não precisam ser instaladas separadamente.

## 6. Configuração da API

O ComunicadoAI utiliza a API do Google Gemini.

Para obter uma chave de acesso, entre no [Google AI Studio](https://aistudio.google.com/) e gere uma chave para o projeto.

Crie um arquivo chamado `.env` na raiz do repositório, utilizando o `.env.example` como referência.

Exemplo:

```env
GEMINI_API_KEY=sua_chave_aqui
GEMINI_MODEL=gemini-3.5-flash-lite
GEMINI_TEMPERATURE=0.2
GEMINI_MAX_OUTPUT_TOKENS=2048
GEMINI_TIMEOUT_MS=30000
```

**Parâmetros disponíveis:**

| Variável | Finalidade |
|---|---|
| `GEMINI_API_KEY` | Chave de acesso à API. |
| `GEMINI_MODEL` | Modelo utilizado nas requisições. |
| `GEMINI_TEMPERATURE` | Controla a aleatoriedade das respostas. |
| `GEMINI_MAX_OUTPUT_TOKENS` | Define o limite de tokens gerados. |
| `GEMINI_TIMEOUT_MS` | Define o tempo máximo da requisição em milissegundos. |

Os parâmetros são carregados e validados pelo módulo `src/config.py`.

**Importante:** nunca compartilhe a chave de API nem envie o arquivo `.env` ao GitHub.

## 7. Como executar

Com o ambiente virtual ativado e as dependências instaladas, execute o seguinte comando na raiz do projeto:

```bash
python -m src.main
```

O programa solicitará que o usuário digite ou cole um comunicado acadêmico.

É possível inserir textos com múltiplas linhas, incluindo parágrafos separados por linhas vazias.

**Para finalizar a entrada, digite `FIM` em uma linha isolada e pressione Enter.**

O programa validará o comunicado, construirá o prompt e enviará o conteúdo à API do Gemini.

A resposta será recebida em formato JSON, validada e apresentada em seções organizadas no terminal.

## 8. Exemplo de utilização

### 8.1. Entrada

```text
Atenção, turma!

A entrega do trabalho de Programação foi
adiada para 17/11/2026.

O trabalho deverá ser enviado em PDF pelo Moodle.

Além disso, teremos uma avaliação de Álgebra
Linear em 20/11/2026, às 14h, na sala B12.

FIM
```

O marcador `FIM` encerra a leitura e não faz parte do comunicado enviado ao modelo.

### 8.2. Exemplo de saída

```text
==================================================
          INTERPRETAÇÃO DO COMUNICADO
==================================================

RESUMO
O comunicado informa o adiamento do trabalho
de Programação e a realização de uma avaliação
de Álgebra Linear.

--------------------------------------------------
TAREFAS
--------------------------------------------------
• Entregar o trabalho de Programação.
• Participar da avaliação de Álgebra Linear.

--------------------------------------------------
PRAZOS
--------------------------------------------------
• Trabalho de Programação: 17/11/2026.
• Avaliação de Álgebra Linear: 20/11/2026, às 14h.

--------------------------------------------------
REQUISITOS
--------------------------------------------------
• Trabalho em formato PDF.
• Envio pela plataforma Moodle.
• Avaliação na sala B12.

--------------------------------------------------
OBSERVAÇÕES
--------------------------------------------------
• O prazo do trabalho de Programação foi adiado.

==================================================
```

A saída é ilustrativa. Como a interpretação é realizada por um modelo generativo, a redação pode variar entre execuções.

### 8.3. Representação estruturada

Internamente, a aplicação trabalha com uma resposta JSON semelhante a:

```json
{
  "resumo": "O comunicado informa a entrega de um trabalho e uma avaliação.",
  "tarefas": [
    "Entregar o trabalho de Programação",
    "Participar da avaliação de Álgebra Linear"
  ],
  "prazos": [
    "Trabalho: 17/11/2026",
    "Avaliação: 20/11/2026, às 14h"
  ],
  "requisitos": [
    "Enviar o trabalho em PDF pelo Moodle",
    "Avaliação na sala B12"
  ],
  "observacoes": [
    "O prazo do trabalho foi adiado"
  ]
}
```

Essa estrutura permite validar cada categoria individualmente e organizar a apresentação das informações.

## 9. Funcionamento

O processamento ocorre nas seguintes etapas:

1. O usuário executa o programa pelo terminal.
2. O programa recebe o comunicado até encontrar o marcador `FIM`.
3. A entrada é validada para impedir o processamento de textos vazios.
4. O comunicado é incorporado a um prompt especializado.
5. A aplicação envia a solicitação à API do Gemini utilizando os parâmetros configurados.
6. O modelo interpreta o texto e retorna uma resposta estruturada em JSON.
7. A resposta é convertida em um dicionário Python.
8. A estrutura dos dados é validada.
9. As informações são formatadas e apresentadas no terminal.

O prompt orienta o modelo a identificar informações relevantes, evitar a criação de dados inexistentes e sinalizar datas ambíguas.

A aplicação utiliza a data atual do sistema como referência para interpretar expressões temporais relativas.

### 9.1. Validação dos dados

**Validação de entrada:**

- Verifica se o comunicado é um texto.
- Rejeita entradas vazias.
- Rejeita entradas compostas exclusivamente por espaços em branco.

**Validação de resposta:**

- Verifica se a resposta pode ser interpretada como JSON.
- Confirma que o resultado é um objeto.
- Verifica a existência dos campos obrigatórios.
- Confirma os tipos esperados.
- Verifica se os elementos das listas são textos.

Os campos obrigatórios são `resumo`, `tarefas`, `prazos`, `requisitos` e `observacoes`.

### 9.2. Tratamento de erros

A aplicação apresenta mensagens compreensíveis para diferentes situações de falha.

| Situação | Comportamento |
|---|---|
| Entrada vazia | Informa que o comunicado não pode estar vazio. |
| Chave de API ausente | Solicita a configuração de `GEMINI_API_KEY`. |
| Falha de autenticação | Informa que não foi possível autenticar no Gemini. |
| Solicitação rejeitada | Informa que a API rejeitou a solicitação. |
| Limite de requisições | Orienta o usuário a tentar novamente mais tarde. |
| Timeout | Informa que a solicitação demorou demais. |
| Falha de conexão | Orienta a verificar a conexão com a internet. |
| Serviço indisponível | Informa que o Gemini está temporariamente indisponível. |
| Resposta vazia | Informa que a IA não retornou conteúdo. |
| JSON inválido | Informa que a resposta não pôde ser interpretada corretamente. |
| Estrutura inesperada | Identifica campos ausentes ou tipos incompatíveis. |

### 9.3. Registros de execução

A aplicação utiliza a biblioteca nativa `logging` para registrar eventos operacionais e auxiliar na identificação de falhas.

Os registros acompanham o andamento da execução sem armazenar a chave da API, o conteúdo dos comunicados ou as respostas completas do modelo.

### 9.4. Testes automatizados

O ComunicadoAI utiliza o framework `pytest` para verificar seus principais componentes.

Os testes estão organizados no diretório `tests/` e abrangem:

- Validação de entradas e respostas.
- Carregamento e validação de configurações.
- Construção do prompt.
- Simulação de respostas válidas e inválidas da API.
- Tratamento de falhas de comunicação.
- Comportamento diante da ausência de chave de API.

Para executar a suíte completa:

```bash
python -m pytest -v
```

Para executar apenas os testes do módulo de construção do prompt:

```bash
python -m pytest tests/test_extractor.py -v
```

**Testes simulados:** utilizam mocks e `monkeypatch` para simular respostas e falhas da API. Não exigem conexão com o Gemini nem consumo de requisições reais.

**Testes reais:** consistem na execução da aplicação com uma chave de API válida, enviando comunicados ao serviço Gemini para verificar o comportamento da integração.

**Resultados:** a execução documentada no relatório registrou 21 testes automatizados aprovados, sem falhas. Após a correção da entrada multiline, a suíte foi executada novamente com sucesso, e o processamento de um comunicado com múltiplos parágrafos foi validado manualmente.

Os testes simulados não comprovam a disponibilidade da API nem a precisão das respostas em chamadas reais. As evidências e limitações dos testes estão descritas no `RELATORIO_EXECUCAO.md`.

## 10. Limitações

Apesar das melhorias implementadas, a aplicação ainda apresenta algumas limitações:

- Depende de conexão com a internet e da disponibilidade da API do Gemini.
- A interpretação gerada pelo modelo pode conter imprecisões.
- Datas relativas podem ser interpretadas incorretamente quando o contexto é ambíguo.
- A validação JSON verifica a estrutura dos dados, mas não garante sua veracidade.
- O sistema não verifica automaticamente os prazos em calendários acadêmicos.
- Os testes simulados não substituem testes reais de integração.
- O limite de tokens pode interromper respostas extensas e comprometer a estrutura JSON retornada.
- A aplicação utiliza uma interface de terminal, sem interface gráfica.

As informações extraídas devem ser conferidas com o comunicado original, especialmente quando envolverem prazos importantes.

## 11. Evolução do projeto

O desenvolvimento foi organizado em três níveis incrementais.

### Básico (`p0-basico`)

Implementação da primeira versão funcional, incluindo:

- Integração com a API do Gemini.
- Entrada de comunicados pelo terminal.
- Construção de prompt especializado.
- Apresentação da interpretação.
- Configuração da chave de API por variável de ambiente.

### Intermediário (`p0-intermediario`)

Reorganização da aplicação para melhorar sua estrutura e previsibilidade:

- Separação das responsabilidades em módulos.
- Extração estruturada em JSON.
- Formatação das respostas.
- Validação de entradas e respostas.
- Tratamento de erros de autenticação e comunicação.
- Tratamento de timeout e indisponibilidade da API.

### Avançado (`p0-avancado`)

Ampliação da configurabilidade, testabilidade e rastreabilidade:

- Configuração de temperatura, limite de tokens e timeout.
- Implementação de logs com `logging`.
- Criação de testes automatizados com `pytest`.
- Simulação de respostas e falhas da API.
- Atualização da documentação.
- Correção da leitura de comunicados com múltiplos parágrafos.

Cada nível é identificado por uma tag no repositório Git.

As principais decisões técnicas, dificuldades encontradas e reflexões sobre o desenvolvimento estão documentadas no `RELATORIO_EXECUCAO.md`.

## 12. Segurança

As credenciais da API são armazenadas em variáveis de ambiente e não são incluídas diretamente no código-fonte.

O arquivo `.env` é ignorado pelo Git, enquanto o `.env.example` apresenta apenas as variáveis necessárias para configurar a aplicação.

Os logs não devem expor credenciais, o conteúdo dos comunicados ou as respostas completas do modelo.

Os comunicados enviados ao programa são processados por um serviço externo de inteligência artificial. Por isso, recomenda-se não inserir informações pessoais ou confidenciais.

O prompt inclui instruções para que o modelo não execute comandos ou orientações contidos no comunicado que tentem modificar sua tarefa original.

Entretanto, essas instruções não garantem proteção absoluta contra interpretações incorretas ou tentativas de manipulação do modelo.

## 13. Demonstração

**Vídeo de apresentação e execução:** [Adicionar link do vídeo]

O vídeo deverá demonstrar a execução do ComunicadoAI, a entrada de um comunicado acadêmico e a apresentação das informações extraídas.

## 14. Estado do desenvolvimento

**Versão avançada implementada.**

O ComunicadoAI reúne arquitetura modular, integração com o Gemini, extração estruturada em JSON, validação de entradas e respostas, tratamento de falhas operacionais, parâmetros configuráveis, logs e testes automatizados.

A suíte de testes foi executada com sucesso, e a correção da entrada de múltiplos parágrafos foi validada manualmente.

A validação da instalação em ambiente limpo ainda não foi registrada como concluída. O relatório de execução reúne os resultados conhecidos e as limitações identificadas.

**Repositório:** https://github.com/andreary1/TrendsIA-P0

**Relatório de execução:** [RELATORIO_EXECUCAO.md](RELATORIO_EXECUCAO.md)
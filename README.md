# TrendsIA-P0 (PRIMEIRO-FLUXO-LLM) - ComunicadoAI

**Interpretador Inteligente de Comunicados Acadêmicos**

O ComunicadoAI é uma aplicação desenvolvida em Python que utiliza a API do Google Gemini para interpretar comunicados acadêmicos, extrair informações estruturadas e apresentá-las de maneira clara e organizada no terminal.

## 1. Problema

Estudantes universitários recebem comunicados acadêmicos contendo informações sobre avaliações, trabalhos, prazos, alterações de horários e orientações importantes.

Essas informações frequentemente aparecem em textos extensos ou pouco estruturados, exigindo que os estudantes identifiquem manualmente as atividades e os prazos relevantes.

O ComunicadoAI busca facilitar esse processo por meio da interpretação automatizada desses textos.

## 2. Objetivo

Desenvolver uma aplicação capaz de receber comunicados acadêmicos escritos em linguagem natural e utilizar um modelo de linguagem para identificar e organizar suas principais informações.

O sistema apresenta:

- **Resumo:** síntese do conteúdo do comunicado.
- **Tarefas:** atividades que o estudante precisa realizar.
- **Prazos:** datas e horários identificados.
- **Requisitos:** formatos, plataformas, materiais e condições necessárias.
- **Observações:** alterações de prazo, cancelamentos e outras informações relevantes.

Além da interpretação dos comunicados, a aplicação realiza validações de entrada e resposta, apresenta mensagens de erro compreensíveis e organiza suas funcionalidades em módulos independentes.

## 3. Tecnologias utilizadas

- Python 3.10 ou superior.
- Google Gemini API.
- Modelo Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`; conferir o identificador em `src/config.py` e no `.env`).
- Biblioteca `google-genai`.
- Biblioteca `python-dotenv`.
- Biblioteca `httpx`.
- Biblioteca `pytest` para testes automatizados.
- Biblioteca nativa `logging` para registro de eventos.
- Biblioteca nativa `unicodedata` para normalização de textos nos testes.
- JSON para representação estruturada das informações.
- Git e GitHub para versionamento.

A utilização de um LLM permite interpretar comunicados escritos de diferentes maneiras, incluindo textos informais, informações distribuídas em vários parágrafos e referências a datas relativas.

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

**Descrição dos arquivos:**

- `src/main.py`: coordena o fluxo principal da aplicação e recebe os comunicados pelo terminal.
- `src/config.py`: carrega e valida as configurações armazenadas nas variáveis de ambiente, incluindo os parâmetros do modelo.
- `src/client.py`: realiza a comunicação com a API do Gemini, solicita respostas estruturadas e trata falhas de comunicação.
- `src/extractor.py`: constrói o prompt utilizado para interpretar os comunicados acadêmicos.
- `src/formatter.py`: organiza e apresenta as informações extraídas no terminal.
- `src/validators.py`: valida os comunicados recebidos e a estrutura das respostas.
- `src/logger.py`: configura os registros de execução da aplicação.
- `tests/`: contém os testes automatizados de validação, configuração, construção do prompt e comunicação simulada com a API.
- `RELATORIO_EXECUCAO.md`: reúne o registro da execução, dos testes e dos resultados efetivamente obtidos.
- `src/__init__.py`: identifica o diretório `src` como um pacote Python.
- `requirements.txt`: relaciona as dependências necessárias para executar o projeto.
- `.env.example`: apresenta as variáveis de ambiente utilizadas pela aplicação.
- `.gitignore`: define os arquivos e diretórios que não devem ser versionados.
- `README.md`: documentação do projeto.

O arquivo `.env`, utilizado para armazenar a chave da API, deve ser criado localmente e não deve ser enviado ao repositório.

## 5. Instalação

### 5.1. Clonar o repositório

```bash
git clone https://github.com/andreary1/TrendsIA-P0.git
cd TrendsIA-P0
```

### 5.2. Criar o ambiente virtual

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

O arquivo `requirements.txt` deve conter as dependências utilizadas pela aplicação, incluindo:

```text
google-genai
python-dotenv
httpx
pytest
```

As bibliotecas `logging` e `unicodedata` fazem parte da biblioteca padrão do Python e não precisam ser instaladas separadamente.

## 6. Configuração da API

O ComunicadoAI utiliza a API do Google Gemini.

Para obter uma chave de API, acesse o Google AI Studio e crie uma chave para utilização no projeto.

Crie um arquivo chamado `.env` na raiz do repositório, utilizando o `.env.example` como referência.

Exemplo:

```env
GEMINI_API_KEY=sua_chave_aqui
GEMINI_MODEL=gemini-3.5-flash-lite
GEMINI_TEMPERATURE=0.2
GEMINI_MAX_OUTPUT_TOKENS=2048
GEMINI_TIMEOUT_MS=30000
```

Substitua `sua_chave_aqui` pela sua chave real.

O identificador `gemini-3.5-flash-lite` foi mantido conforme a documentação original. Confira se ele corresponde ao modelo configurado em `src/config.py` e no `.env`, bem como à disponibilidade na API utilizada.

**Parâmetros de configuração:**

| Variável | Valor do exemplo | Finalidade |
|---|---|---|
| `GEMINI_API_KEY` | `sua_chave_aqui` | Chave de acesso à API do Gemini. |
| `GEMINI_MODEL` | `gemini-3.5-flash-lite` | Identificador do modelo utilizado nas requisições. |
| `GEMINI_TEMPERATURE` | `0.2` | Controla a aleatoriedade das respostas; valores menores tendem a reduzir a variação. |
| `GEMINI_MAX_OUTPUT_TOKENS` | `2048` | Define o limite de tokens da resposta gerada. |
| `GEMINI_TIMEOUT_MS` | `30000` | Define o tempo máximo da requisição em milissegundos, equivalente a 30 segundos. |

Os parâmetros são carregados e validados pelo módulo `src/config.py` e utilizados pelo cliente do Gemini. O limite de tokens não corresponde a uma quantidade fixa de palavras, e uma temperatura baixa não garante respostas idênticas ou livres de imprecisões.

**Importante:** o arquivo `.env` contém informações sensíveis e não deve ser compartilhado ou enviado ao GitHub.

## 7. Como executar

Com o ambiente virtual ativado e as dependências instaladas, execute o seguinte comando na raiz do projeto:

```bash
python -m src.main
```

O programa solicitará que o usuário digite um comunicado acadêmico.

É possível inserir textos com várias linhas. Para finalizar a entrada, pressione Enter em uma linha vazia.

Antes de enviar o comunicado ao Gemini, o programa verifica se a entrada contém um texto válido.

O comunicado será incorporado a um prompt especializado e enviado ao modelo, que retornará informações estruturadas em JSON.

A aplicação validará os dados recebidos e apresentará o resultado em seções organizadas no terminal.

## 8. Exemplo de utilização

### Entrada

```text
Atenção, turma!

A entrega do trabalho de Programação foi
adiada para 17/11/2026.

O trabalho deverá ser enviado em PDF pelo Moodle.

Além disso, teremos uma avaliação de Álgebra
Linear em 20/11/2026, às 14h, na sala B12.
```

### Exemplo de saída

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

A saída apresentada é ilustrativa. Como a interpretação é realizada por um modelo generativo, a redação pode variar entre execuções.

### 8.1. Representação estruturada

Internamente, o Gemini retorna informações em formato JSON.

Exemplo:

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

Essa estrutura permite acessar individualmente cada categoria de informação e facilita a validação dos resultados.

## 9. Funcionamento

O processamento ocorre nas seguintes etapas:

1. O usuário executa o programa pelo terminal.
2. O programa recebe o comunicado acadêmico.
3. A entrada é validada para impedir o envio de textos vazios.
4. O texto é incorporado a um prompt especializado.
5. A aplicação envia a solicitação à API do Gemini utilizando o modelo, a temperatura, o limite de tokens e o timeout configurados.
6. O modelo interpreta o comunicado e retorna uma resposta estruturada em JSON.
7. O programa converte o JSON em um dicionário Python.
8. A estrutura da resposta é validada.
9. As informações são formatadas e apresentadas no terminal.

O prompt orienta o modelo a identificar informações relevantes, evitar a criação de dados inexistentes e sinalizar datas ambíguas.

A aplicação utiliza a data atual do sistema como referência para interpretar expressões como "amanhã" e "próxima semana".

### 9.1. Validação dos dados

O ComunicadoAI realiza dois tipos principais de validação.

**Validação de entrada:**

- Verifica se o comunicado é um texto.
- Rejeita entradas vazias.
- Rejeita entradas compostas exclusivamente por espaços em branco.

**Validação de resposta:**

- Verifica se a resposta pode ser interpretada como JSON.
- Confirma que o resultado é um objeto.
- Verifica a existência dos campos obrigatórios.
- Confirma os tipos esperados para cada campo.
- Verifica se os elementos das listas são textos.

Os campos obrigatórios são `resumo`, `tarefas`, `prazos`, `requisitos` e `observacoes`.

### 9.2. Tratamento de erros

A aplicação apresenta mensagens compreensíveis para diferentes situações de falha.

| Situação | Comportamento |
|---|---|
| Entrada vazia | Informa que o comunicado não pode estar vazio. |
| Chave de API ausente | Solicita a configuração da variável `GEMINI_API_KEY`. |
| Falha de autenticação | Informa que não foi possível autenticar no Gemini. |
| Solicitação rejeitada | Informa que a API rejeitou a solicitação. |
| Limite de requisições | Orienta o usuário a tentar novamente mais tarde. |
| Timeout | Informa que a solicitação demorou demais. |
| Falha de conexão | Orienta o usuário a verificar a conexão com a internet. |
| Serviço indisponível | Informa que o Gemini está temporariamente indisponível. |
| Resposta vazia | Informa que a IA não retornou conteúdo. |
| JSON inválido | Informa que a resposta não pôde ser interpretada corretamente. |
| Estrutura inesperada | Identifica campos ausentes ou tipos incompatíveis. |

O objetivo é evitar que falhas operacionais previstas sejam apresentadas diretamente ao usuário como mensagens técnicas do Python.

### 9.3. Registros de execução

A aplicação utiliza a biblioteca nativa `logging`, configurada em `src/logger.py`, para registrar eventos operacionais e auxiliar na identificação de falhas.

Os logs registram o andamento da execução e situações de erro sem armazenar a chave da API, o conteúdo dos comunicados ou as respostas completas do modelo.

### 9.4. Testes automatizados

O ComunicadoAI utiliza o framework `pytest` para verificar os principais componentes da aplicação.

Os testes estão organizados no diretório `tests/` e abrangem:

- Validação de entradas e da estrutura das respostas.
- Carregamento e validação dos parâmetros de configuração.
- Construção do prompt e presença das categorias esperadas.
- Simulação de respostas válidas, inválidas e falhas na comunicação com o Gemini.
- Comportamento diante da ausência de chave de API.

Os testes utilizam mocks e `monkeypatch` para simular a comunicação com a API, sem realizar requisições reais e sem exigir uma chave de API válida. A normalização com `unicodedata` permite verificar os títulos do prompt independentemente de maiúsculas e acentuação.

Com o ambiente virtual ativado e as dependências instaladas, execute na raiz do projeto:

```bash
python -m pytest -v
```

Para executar apenas os testes de construção do prompt:

```bash
python -m pytest tests/test_extractor.py -v
```

Os testes com respostas simuladas verificam o comportamento local da aplicação, mas não comprovam a disponibilidade da API nem a qualidade das interpretações em chamadas reais.

Os resultados efetivamente obtidos devem ser registrados no `RELATORIO_EXECUCAO.md`, incluindo a quantidade de testes aprovados, falhas, avisos e versões utilizadas. Este README não declara resultados de testes nem validação em ambiente limpo sem evidências de execução.

## 10. Limitações

Apesar das melhorias implementadas, a aplicação ainda possui algumas limitações:

- Depende de conexão com a internet e da disponibilidade da API do Gemini.
- A interpretação gerada pelo modelo pode conter imprecisões.
- Datas relativas podem ser interpretadas incorretamente quando o contexto é ambíguo.
- A validação JSON verifica a estrutura dos dados, mas não garante a veracidade das informações.
- O sistema não realiza verificação automática dos prazos em calendários acadêmicos.
- Os testes com respostas simuladas não substituem a verificação da integração real com o Gemini.
- O limite de tokens pode interromper respostas extensas e comprometer a estrutura JSON retornada.

As informações extraídas devem ser conferidas com o comunicado original, especialmente quando envolverem prazos importantes.

## 11. Evolução do projeto

O desenvolvimento está organizado em três níveis incrementais.

### Básico (`p0-basico`)

Implementação da aplicação funcional, integração com a API do Gemini, entrada de comunicados pelo terminal e apresentação da interpretação.

**Funcionalidades implementadas:**

- Integração com a API do Gemini.
- Entrada de comunicados pelo terminal.
- Construção de prompt especializado.
- Apresentação da interpretação.
- Configuração da chave de API por variável de ambiente.

### Intermediário (`p0-intermediario`)

Reorganização da aplicação e implementação de mecanismos para tornar sua execução mais previsível.

**Funcionalidades implementadas:**

- Separação das responsabilidades em módulos.
- Extração de informações estruturadas em JSON.
- Formatação da resposta no terminal.
- Validação de entradas.
- Validação da estrutura das respostas.
- Tratamento de erros de autenticação e comunicação.
- Tratamento de timeout e indisponibilidade da API.
- Atualização da documentação.

### Avançado (`p0-avancado`)

Ampliação da configurabilidade, testabilidade e rastreabilidade da aplicação.

**Funcionalidades implementadas:**

- Configuração de temperatura, limite de tokens e timeout por variáveis de ambiente.
- Implementação de logs seguros com `logging` e `src/logger.py`.
- Criação de testes automatizados com `pytest` no diretório `tests/`.
- Simulação de respostas e falhas da API com mocks e `monkeypatch`, sem requisições reais.
- Atualização das instruções de configuração, execução e testes.

**Verificações para conclusão da entrega:**

- Executar a suíte e registrar os resultados reais no `RELATORIO_EXECUCAO.md`.
- Verificar a instalação e a execução em ambiente limpo e documentar o resultado.
- Consolidar o relatório final com as evidências obtidas.

A implementação dos recursos não equivale à comprovação dessas verificações.

Cada nível é identificado por uma tag no repositório Git após sua conclusão.

## 12. Segurança

As credenciais da API são armazenadas em variáveis de ambiente e não são incluídas diretamente no código-fonte.

O arquivo `.env` é ignorado pelo Git, enquanto o `.env.example` apresenta apenas as variáveis necessárias para configurar a aplicação.

A aplicação também evita incluir a chave de API nas mensagens de erro apresentadas ao usuário. Os registros de execução não devem expor credenciais, o conteúdo dos comunicados ou as respostas completas do modelo.

Os comunicados enviados ao programa são processados por um serviço externo de IA. Por isso, recomenda-se não inserir informações pessoais ou confidenciais.

O prompt inclui instruções para que o modelo não execute comandos ou orientações contidos no comunicado que tentem modificar sua tarefa original.

Entretanto, essas instruções não garantem proteção absoluta contra interpretações incorretas ou tentativas de manipulação do modelo.

## 13. Estado do desenvolvimento

**Recursos da versão avançada implementados; verificações finais pendentes de comprovação.**

O ComunicadoAI reúne arquitetura modular, integração com o Gemini, extração estruturada em JSON, validação de entradas e respostas, apresentação formatada, tratamento de falhas operacionais, parâmetros configuráveis, logs seguros e testes automatizados com `pytest`.

O modelo documentado permanece `gemini-3.5-flash-lite`, sujeito à conferência com `src/config.py` e o `.env` utilizado na execução.

A conclusão da entrega depende do registro dos resultados reais dos testes, da validação da instalação e execução em ambiente limpo e da consolidação do `RELATORIO_EXECUCAO.md`. Não são declarados aqui testes aprovados ou validações concluídas sem comprovação.

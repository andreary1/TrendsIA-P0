# TrendsIA-P0 (PRIMEIRO-FLUXO-LLM) - ComunicadoAI

**Interpretador Inteligente de Comunicados Acadêmicos**

O ComunicadoAI é uma aplicação desenvolvida em Python que utiliza a API do Google Gemini para interpretar comunicados acadêmicos e apresentar suas informações de maneira clara e organizada.

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

## 3. Tecnologias utilizadas

- Python 3.10 ou superior.
- Google Gemini API.
- Modelo Gemini 2.5 Flash-Lite.
- Biblioteca `google-genai`.
- Biblioteca `python-dotenv`.
- Git e GitHub para versionamento.

A utilização de um LLM permite interpretar comunicados escritos de diferentes maneiras, incluindo textos informais, informações distribuídas em vários parágrafos e referências a datas relativas.

## 4. Estrutura do projeto

```text
comunicado-ai/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

**Descrição dos arquivos:**

- `main.py`: implementação principal da aplicação.
- `requirements.txt`: dependências necessárias.
- `.env.example`: exemplo das variáveis de ambiente.
- `.gitignore`: arquivos que não devem ser versionados.
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

## 6. Configuração da API

O ComunicadoAI utiliza a API do Google Gemini.

Para obter uma chave de API, acesse o Google AI Studio e crie uma chave para utilização no projeto.

Crie um arquivo chamado `.env` na raiz do repositório, utilizando o `.env.example` como referência.

Exemplo:

```env
GEMINI_API_KEY=sua_chave_aqui
GEMINI_MODEL=gemini-2.5-flash-lite
```

Substitua `sua_chave_aqui` pela sua chave real.

**Importante:** o arquivo `.env` contém informações sensíveis e não deve ser compartilhado ou enviado ao GitHub.

## 7. Como executar

Com o ambiente virtual ativado e as dependências instaladas, execute:

```bash
python main.py
```

O programa solicitará que o usuário digite um comunicado acadêmico.

É possível inserir textos com várias linhas. Para finalizar a entrada, pressione Enter em uma linha vazia.

O texto será enviado ao Gemini, que retornará uma interpretação organizada.

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
RESUMO
O comunicado informa o adiamento do trabalho
de Programação e a realização de uma avaliação
de Álgebra Linear.

TAREFAS
- Entregar o trabalho de Programação.
- Participar da avaliação de Álgebra Linear.

PRAZOS
- Trabalho de Programação: 17/11/2026.
- Avaliação de Álgebra Linear: 20/11/2026, às 14h.

REQUISITOS
- Trabalho em formato PDF.
- Envio pela plataforma Moodle.
- Avaliação na sala B12.

OBSERVAÇÕES
- O prazo do trabalho de Programação foi adiado.
```

A saída apresentada é ilustrativa. Como a interpretação é realizada por um modelo generativo, a redação pode variar entre execuções.

## 9. Funcionamento

O processamento ocorre nas seguintes etapas:

1. O usuário executa o programa pelo terminal.
2. O programa recebe o comunicado acadêmico.
3. O texto é incorporado a um prompt especializado.
4. A aplicação envia a solicitação à API do Gemini.
5. O modelo interpreta o comunicado.
6. A resposta é apresentada no terminal.

O prompt orienta o modelo a identificar informações relevantes, evitar a criação de dados inexistentes e sinalizar datas ambíguas.

A aplicação utiliza a data atual do sistema como referência para interpretar expressões como "amanhã" e "próxima semana".

## 10. Limitações da versão básica

A primeira versão possui as seguintes limitações:

- Não realiza validação específica para entradas vazias.
- Não apresenta tratamento personalizado para falhas de autenticação ou comunicação com a API.
- Depende de conexão com a internet e disponibilidade do serviço Gemini.
- Não verifica automaticamente se a resposta segue o formato solicitado.
- Não utiliza uma estrutura JSON validada para representar as informações extraídas.
- Datas relativas podem ser interpretadas incorretamente quando o contexto é ambíguo.
- A interpretação gerada pelo LLM pode conter imprecisões.

As informações extraídas devem ser conferidas com o comunicado original, especialmente quando envolverem prazos importantes.

## 11. Evolução do projeto

O desenvolvimento está organizado em três níveis incrementais:

**Básico (`p0-basico`)**

Implementação da aplicação funcional, integração com a API do Gemini, entrada de comunicados pelo terminal e apresentação da interpretação.

**Intermediário (`p0-intermediario`)**

Separação das responsabilidades do código, validação das entradas, tratamento de falhas e aprimoramento da estrutura das respostas.

**Avançado (`p0-avancado`)**

Configuração de parâmetros, implementação de logs, testes automatizados e validação da execução em um ambiente limpo.

Cada nível será identificado por uma tag no repositório Git.

## 12. Segurança

As credenciais da API são armazenadas em variáveis de ambiente e não são incluídas diretamente no código-fonte.

O arquivo `.env` é ignorado pelo Git, enquanto o `.env.example` apresenta apenas as variáveis necessárias para configurar a aplicação.

Os comunicados enviados ao programa são processados por um serviço externo de IA. Por isso, recomenda-se não inserir informações pessoais ou confidenciais.

## 13. Estado do desenvolvimento

**Versão básica concluída.**

As funcionalidades principais de entrada, comunicação com o LLM e interpretação de comunicados foram implementadas e verificadas manualmente.

As próximas etapas serão dedicadas à robustez, organização e testabilidade da aplicação.
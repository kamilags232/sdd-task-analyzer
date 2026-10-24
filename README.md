
# TaskAnalyzer

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![SDD](https://img.shields.io/badge/Development-SDD-purple)
![Tests](https://img.shields.io/badge/Tests-Pytest-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Sobre o projeto

O **TaskAnalyzer** é um projeto desenvolvido em Python com base na abordagem **Specification-Driven Development (SDD)**. Seu objetivo é analisar tarefas e gerar indicadores de produtividade a partir dos dados fornecidos.

O sistema permite acompanhar informações gerais das tarefas, calcular o tempo médio de conclusão e apresentar indicadores organizados por prioridade, seguindo as regras estabelecidas na especificação do projeto.

## Funcionalidades

- Análise geral das tarefas cadastradas.
- Contagem de tarefas de acordo com seu estado.
- Cálculo do tempo médio de conclusão.
- Geração de indicadores por prioridade.
- Cálculo da taxa de atraso conforme a regra definida na especificação.
- Validação dos dados de entrada.
- Tratamento de situações inválidas por meio de exceções específicas.
- Tratamento de casos de borda, como entradas vazias e tarefas pendentes.
- Testes automatizados para verificar os comportamentos especificados.

## Estrutura do projeto

```text
sdd-task-analyzer/
├── .github/
│   └── workflows/
│       └── ci.yml
├── specs/
│   ├── task_analyzer_spec.md
│   └── system_design_document.pdf
├── src/
│   └── task_analyzer.py
├── tests/
│   └── test_harness.py
├── .gitignore
├── CONTEXT_RULES.md
├── Dockerfile
├── docker-compose.yml
├── README.md
├── requirements.txt
└── requirements.yaml
```

## Tecnologias e ferramentas

- **Python 3.11+:** linguagem utilizada na implementação.
- **Pytest:** execução dos testes automatizados.
- **Git e GitHub:** versionamento e hospedagem do código.
- **GitHub Actions:** integração contínua.
- **Docker:** empacotamento e execução em contêineres.
- **Specification-Driven Development (SDD):** desenvolvimento orientado por especificações.

## Requisitos

- Python 3.11 ou superior.
- Git.
- pip.
- Docker e Docker Compose, caso sejam utilizados os arquivos de contêineres.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/kamilags232/sdd-task-analyzer.git
```

Entre no diretório:

```bash
cd sdd-task-analyzer
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual.

**Windows — PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows — Git Bash:**

```bash
source .venv/Scripts/activate
```

**Linux ou macOS:**

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executando os testes

Execute na raiz do projeto:

```bash
python -m pytest -v
```

Os cenários de teste contemplam:

- Análise bem-sucedida das tarefas e cálculo dos indicadores.
- Cálculo da taxa de atraso.
- Validação de datas inválidas, como conclusão anterior à criação.
- Tratamento de entrada vazia.
- Tratamento de tarefas exclusivamente pendentes.
- Arredondamento dos resultados para duas casas decimais.

## Executando com Docker

O projeto contém um `Dockerfile` e um `docker-compose.yml` para configuração do ambiente com contêineres.

Para construir a imagem e iniciar os serviços:

```bash
docker compose up --build
```

Para interromper os serviços:

```bash
docker compose down
```

**Observação:** os comandos dependem da configuração dos arquivos Docker. A presença desses arquivos não garante, por si só, que a execução esteja funcionando.

## Especificação e regras de desenvolvimento

O TaskAnalyzer segue a abordagem **Specification-Driven Development (SDD)**. A especificação orienta a implementação, e os testes verificam se o comportamento desenvolvido corresponde aos requisitos definidos.

As regras de desenvolvimento incluem:

- Utilização de Python 3.11 ou superior.
- Type hints em funções e métodos.
- Conformidade com a PEP 8.
- Docstrings no padrão Google.
- Princípio da Responsabilidade Única (SRP).
- Uso de exceções específicas para erros previstos.
- Utilização de logging estruturado.
- Testes automatizados para validar comportamentos.
- Ausência de persistência em arquivos ou banco de dados, conforme as restrições do projeto.
- Não inclusão de funcionalidades sem aprovação e testes correspondentes.
- Não alteração da especificação apenas para acomodar uma implementação divergente.

As regras detalhadas estão documentadas em `CONTEXT_RULES.md`, enquanto os requisitos funcionais estão descritos em `specs/task_analyzer_spec.md`.

## Considerações sobre a taxa de atraso

A interpretação da taxa de atraso deve respeitar a definição estabelecida na especificação do projeto. Caso não exista um campo de prazo ou uma regra formal para determinar o atraso, essa definição precisa ser esclarecida antes de se estabelecer uma fórmula definitiva.

## Autoria

**Aluna:** Kamila Gomes da Silva  
**Curso:** Ciência da Computação  
**Instituição:** CEUB — Asa Norte  
**Turma:** A  
**Projeto:** TaskAnalyzer  
**Abordagem:** Specification-Driven Development (SDD)

## Licença

Este projeto está identificado como MIT. Para distribuir o projeto sob essa licença, inclua um arquivo `LICENSE` contendo o texto da licença MIT.

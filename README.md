# TaskAnalyzer — Análise de Métricas de Produtividade

![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)
![Test Harness](https://img.shields.io/badge/tests-pytest%20100%25%20passed-brightgreen.svg)
![Architecture](https://img.shields.io/badge/architecture-SDD%20%7C%20Spec--Driven-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

O **TaskAnalyzer** é um módulo em Python concebido para analisar conjuntos de tarefas e calcular indicadores estratégicos de produtividade, tais como o tempo médio de conclusão (geral e por prioridade) e a taxa de atraso. 

Este projeto foi desenvolvido na disciplina **Bootcamp III** (Ciência da Computação — CEUB) utilizando a metodologia **Spec-Driven Development (SDD)**, onde o código-fonte e os testes automatizados são orientados estritamente por contratos técnicos executáveis e regras de governança de IA.

---

##  Principais Funcionalidades

- ** Indicadores Gerais de Produtividade:** Contagem automática do total de tarefas, tarefas concluídas e tarefas pendentes.
- ** Tempo Médio de Conclusão:** Cálculo do tempo médio gasto para concluir tarefas (em horas), com precisão de duas casas decimais.
- ** Métricas Agrupadas por Prioridade:** Análise detalhada dos tempos e volumes de tarefas segmentados por nível de prioridade (ex.: *Alta*, *Média*, *Baixa*).
- ** Taxa de Atraso Percentual:** Métricas percentuais sobre o cumprimento dos estados das tarefas.
- ** Validação Rigorosa de Dados:** Tratamento e rejeição automática de inconsistências nas datas (ex.: `data_conclusao` anterior à `data_criacao`) através da exceção personalizada `TaskValidationError`.
- ** Prevenção de Erros Em Tempo de Execução:** Proteção total contra divisão por zero para cenários com zero tarefas concluídas ou listas vazias.

---

##  Estrutura do Repositório

```text
sdd-task-analyzer/
├── specs/
│   └── task_analyzer_spec.md  # Contrato técnico SDD (fonte da verdade)
├── src/
│   └── task_analyzer.py       # Módulo principal com a função analyze_tasks
├── tests/
│   └── test_harness.py        # Suíte de testes automatizados com pytest
├── .gitignore                 # Arquivos e pastas ignorados pelo Git (.venv, cache)
├── CONTEXT_RULES.md           # Regras de governança e restrições para IA
├── README.md                  # Documentação do projeto
└── requirements.txt           # Dependências do projeto (pytest)

```

---

##  Como Executar o Projeto Localmente

### 1. Pré-requisitos

Certifica-te de ter o **Python 3.11** ou superior e o **Git** instalados na tua máquina.

### 2. Clonar o Repositório

```bash
git clone [https://github.com/SEU_USUARIO/sdd-task-analyzer.git](https://github.com/SEU_USUARIO/sdd-task-analyzer.git)
cd sdd-task-analyzer

```

### 3. Criar e Ativar o Ambiente Virtual

No terminal (Git Bash ou VS Code):

* **Windows (Git Bash):**
```bash
python -m venv .venv
source .venv/Scripts/activate

```


* **Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate

```



### 4. Instalar as Dependências

Com o ambiente virtual ativo (`(.venv)` no início da linha do terminal):

```bash
python -m pip install -r requirements.txt

```

---

##  Execução dos Testes Automatizados (Test Harness)

O projeto conta com um **Test Harness** completo construído sobre o framework `pytest`. Para executar a suíte de testes unitários e validar os cenários de aceite:

```bash
python -m pytest -v

```

### Resultado Esperado:

```text
collected 6 items

tests/test_harness.py::test_cenario_1_analise_com_sucesso_calculos_gerais_e_por_prioridade PASSED [ 16%]
tests/test_harness.py::test_cenario_1_taxa_atraso_percentual PASSED                         [ 33%]
tests/test_cenario_2_excecao_data_conclusao_anterior_a_data_criacao PASSED                 [ 50%]
tests/test_caso_borda_entrada_vazia PASSED                                                  [ 66%]
tests/test_caso_borda_apenas_tarefas_pendentes PASSED                                       [ 83%]
tests/test_arredondamento_duas_casas_decimais PASSED                                        [100%]

============================== 6 passed in 0.04s ==============================

```

---

## Exemplo de Uso do Módulo

```python
from datetime import datetime, timedelta
from src.task_analyzer import analyze_tasks

agora = datetime.now()

# Lista de tarefas para análise
tarefas = [
    {
        "id": 1,
        "titulo": "Implementar Test Harness",
        "prioridade": "Alta",
        "data_criacao": agora - timedelta(hours=6),
        "data_conclusao": agora - timedelta(hours=2),
        "status": "concluida"
    },
    {
        "id": 2,
        "titulo": "Documentar README",
        "prioridade": "Média",
        "data_criacao": agora - timedelta(hours=1),
        "data_conclusao": None,
        "status": "pendente"
    }
]

# Executa a análise
resultado = analyze_tasks(tarefas)

print(resultado)
# Saída esperada:
# {
#     'total_tarefas': 2,
#     'total_concluidas': 1,
#     'total_pendentes': 1,
#     'taxa_atraso_percentual': 0.0,
#     'tempo_medio_conclusao_horas': 4.0,
#     'metricas_por_prioridade': {
#         'Alta': {'total_tarefas': 1, 'total_concluidas': 1, 'total_pendentes': 0, 'tempo_medio_conclusao_horas': 4.0},
#         'Média': {'total_tarefas': 1, 'total_concluidas': 0, 'total_pendentes': 1, 'tempo_medio_conclusao_horas': 0.0}
#     }
# }

```

---

##  Governança e Diretrizes de Desenvolvimento (SDD)

Este projeto foi desenvolvido aplicando diretrizes estritas de qualidade de software:

* **Spec-Driven Development (SDD):** Todo o comportamento foi derivado a partir do contrato estipulado em `specs/task_analyzer_spec.md`.


* **Type Hints & Pep 8:** Anotação explicita de tipos em 100% dos parâmetros e retornos das funções.


* **Documentação:** Google Style Docstrings presentes em todas as funções e módulos.


* **Rastreabilidade e Logs:** Registo estruturado de operações através do módulo padrão `logging`.



---

## Créditos e Reconhecimentos

###  Autoria e Desenvolvimento
* **Kamila Gomes da Silva**
  * **Curso:** Ciência da Computação — CEUB (Asa Norte)
  * **E-mail Institucional:** `kamila.gs@sempreceub.com`
  * **Papel no Projeto:** Piloto de Agentes de IA, Desenvolvedora e Homologadora Crítica

---

###  Instituição e Disciplina
* **Instituição:** Centro Universitário de Brasília (CEUB)
* **Disciplina:** Bootcamp III (Modalidade EAD - Disciplina Virtual)
* **Atividade:** Desafio Entrega Intermediária (Fase 2 - Implementação com IA, Test Harness e Versionamento)

---

###  Tecnologias e Ferramentas Utilizadas
* **Linguagem de Programação:** [Python 3.11+](https://www.python.org/)
* **Framework de Testes:** [Pytest](https://docs.pytest.org/)
* **Controlo de Versões & Git Bash:** [Git](https://git-scm.com/) & [GitHub](https://github.com/)
* **Metodologia:** Spec-Driven Development (SDD)
* **Assistente de IA:** Modelo Gemini (Google AI) — Utilizado para geração e auxílio na homologação do código-fonte e da suíte de testes

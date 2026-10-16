# Especificação SDD — TaskAnalyzer

**Aluno:** Kamila Gomes da Silva  
**Curso:** Ciência da Computação  
**Polo/Turma:** Turma A (CEUB – Asa Norte)  
**E-mail institucional:** kamila.gs@sempreceub.com  
**Disciplina:** Bootcamp III  
**Atividade:** Desafio – Entrega Inicial  
**Versão:** 1.0  
**Data:** 12/09/2026

---

## Sumário

1. [Visão Geral e Contrato de Negócio](#1-visão-geral-e-contrato-de-negócio)
2. [Contrato Executável de Interface](#2-contrato-executável-de-interface)
3. [Saídas do Sistema](#3-saídas-do-sistema)
4. [Regras de Negócio](#4-regras-de-negócio)
5. [Cenários de Aceite](#5-cenários-de-aceite)
6. [Planejamento do Test Harness](#6-planejamento-do-test-harness)
7. [Governança de Contexto e Regras para Agentes de IA](#7-governança-de-contexto-e-regras-para-agentes-de-ia)
8. [Regras Restritivas](#8-regras-restritivas)
9. [Arquitetura do Repositório](#9-arquitetura-do-repositório)
10. [Plano de Homologação Humana](#10-plano-de-homologação-humana)
11. [Fluxo do Projeto Cumulativo](#11-fluxo-do-projeto-cumulativo)
12. [Conclusão](#12-conclusão)
13. [Vídeo de Apresentação da Documentação](#13-vídeo-de-apresentação-da-documentação)

---

## 1. Visão Geral e Contrato de Negócio

### 1.1 Propósito do módulo TaskAnalyzer

O TaskAnalyzer é um módulo destinado à análise de tarefas e à geração de métricas de produtividade.

O sistema deverá receber um conjunto de tarefas e analisar suas informações para produzir indicadores que auxiliem na avaliação da produtividade e do cumprimento dos prazos.

As principais métricas a serem disponibilizadas são:

- Tempo médio de conclusão das tarefas;
- Taxa de atraso;
- Quantidade e indicadores de tarefas por prioridade;
- Indicadores gerais relacionados às tarefas analisadas.

O objetivo desta especificação é estabelecer um contrato claro para orientar a implementação do sistema por ferramentas de Inteligência Artificial, reduzindo ambiguidades e permitindo que o código gerado seja posteriormente validado por testes automatizados.

## 2. Contrato Executável de Interface

### 2.1 Entrada

O TaskAnalyzer deverá receber um conjunto ou uma lista de tarefas.

Cada tarefa deverá possuir informações suficientes para permitir a análise de produtividade.

### 2.2 Estrutura esperada de uma tarefa

| Campo | Tipo | Descrição | Obrigatório |
|---|---|---|---|
| `id` | Inteiro ou string | Identificador único da tarefa | Sim |
| `titulo` | String | Nome ou descrição resumida da tarefa | Sim |
| `prioridade` | String | Prioridade atribuída à tarefa | Sim |
| `data_criacao` | `datetime` | Data e hora em que a tarefa foi criada | Sim |
| `data_conclusao` | `datetime` ou `null` | Data e hora de conclusão | Não |
| `status` | String | Estado atual da tarefa | Sim |

As datas deverão ser válidas e consistentes entre si.

## 3. Saídas do Sistema

Após analisar as tarefas recebidas, o TaskAnalyzer deverá produzir métricas de produtividade.

As principais saídas serão:

### 3.1 Tempo médio de conclusão

Representa o tempo médio utilizado para concluir as tarefas consideradas na análise.

O cálculo deverá considerar a diferença entre a data de criação e a data de conclusão das tarefas concluídas.

### 3.2 Taxa de atraso

Representa a proporção de tarefas que foram consideradas atrasadas em relação ao conjunto de tarefas analisado.

O resultado deverá ser apresentado de forma numérica e consistente com as regras definidas para o cálculo.

**Observação:** a especificação original não define um campo de prazo final nem uma regra completa para identificar uma tarefa atrasada. Essa definição deverá ser confirmada com o professor ou documentada explicitamente antes da implementação.

### 3.3 Indicadores por prioridade

O sistema deverá permitir a identificação das métricas de acordo com a prioridade das tarefas.

Isso possibilita comparar o comportamento das tarefas de diferentes níveis de prioridade.

### 3.4 Indicadores gerais

O sistema deverá fornecer informações gerais sobre o conjunto analisado, permitindo uma visão resumida da produtividade.

## 4. Regras de Negócio

As seguintes regras deverão ser respeitadas pelo código gerado:

1. As tarefas utilizadas na análise deverão possuir dados válidos.
2. O cálculo do tempo de conclusão deverá utilizar a diferença entre a data de criação e a data de conclusão.
3. Tarefas sem data de conclusão não deverão ser consideradas como tarefas concluídas.
4. Datas inválidas deverão gerar uma exceção específica.
5. As datas utilizadas pelo sistema deverão ser consistentes.
6. Os cálculos deverão evitar divisão por zero.
7. Caso não existam tarefas concluídas para determinado cálculo, o sistema deverá tratar essa situação adequadamente por meio de uma exceção ou de um resultado definido no contrato.
8. Os resultados numéricos deverão ser arredondados para duas casas decimais quando aplicável.
9. O sistema deverá utilizar tratamento de exceções específico e apresentar mensagens claras.
10. O sistema não deverá assumir comportamentos que não estejam definidos nesta especificação.

## 5. Cenários de Aceite

Os cenários de aceite serão utilizados como referência para a criação dos testes automatizados na próxima fase do projeto.

### Cenário 1 — Análise realizada com sucesso

**Dado** um conjunto de tarefas válidas, contendo informações de criação, conclusão, status e prioridade;

**Quando** o TaskAnalyzer for executado;

**Então** o sistema deverá retornar corretamente as métricas de produtividade, incluindo o tempo médio de conclusão, a taxa de atraso, os indicadores por prioridade e os indicadores gerais.

### Cenário 2 — Entrada inválida ou situação de divisão por zero

**Dado** uma entrada contendo datas inválidas ou uma situação em que determinado cálculo resulte em divisão por zero;

**Quando** o TaskAnalyzer for executado;

**Então** o sistema deverá realizar o tratamento da situação e disparar uma exceção específica, com uma mensagem clara e adequada ao problema identificado.

## 6. Planejamento do Test Harness

O Test Harness será utilizado na Fase 2 para transformar os cenários de aceite definidos nesta especificação em testes automatizados utilizando a ferramenta `pytest`.

O processo será realizado da seguinte maneira:

1. Os cenários de aceite serão convertidos em casos de teste.
2. Os testes serão implementados utilizando `pytest`.
3. O código gerado pela Inteligência Artificial será executado contra esses testes.
4. Os resultados serão analisados para verificar se o comportamento implementado corresponde ao contrato definido.
5. Caso algum teste falhe, o código deverá ser revisado e corrigido.
6. Após a validação, o código poderá ser submetido à homologação humana.

### 6.1 Fluxo de validação

```text
Especificação
     ↓
Cenários de aceite
     ↓
Testes pytest
     ↓
Código gerado por IA
     ↓
Execução dos testes
     ↓
Homologação humana
```

O Test Harness terá como objetivo impedir que o código gerado seja considerado correto apenas por parecer funcional. A implementação deverá demonstrar, por meio dos testes, que atende ao contrato estabelecido.

## 7. Governança de Contexto e Regras para Agentes de IA

### 7.1 Diretrizes arquiteturais obrigatórias

As regras abaixo deverão ser utilizadas como diretrizes obrigatórias para os agentes de Inteligência Artificial responsáveis pela geração do código.

1. Utilizar Python 3.11 ou versão superior.
2. Utilizar *type hints* em todas as funções e métodos.
3. Seguir o princípio *Single Responsibility Principle* (SRP).
4. Seguir as boas práticas da PEP 8.
5. Utilizar código limpo, legível e manutenível.
6. Utilizar nomes de variáveis, funções e classes descritivos.
7. Utilizar *Google Style Docstrings* para módulos, classes, funções e parâmetros.
8. Manter as funções pequenas, coesas e com uma única responsabilidade.
9. Utilizar tratamento de exceções específico e mensagens claras.
10. Utilizar logs estruturados por meio do módulo padrão `logging`.

## 8. Regras Restritivas

O agente de IA deverá obedecer às seguintes restrições:

1. Não utilizar bibliotecas externas que não tenham sido autorizadas.
2. Não alterar, remover ou adaptar os testes fornecidos.
3. Não modificar a estrutura de pastas definida na especificação.
4. Não persistir dados em arquivos ou bancos de dados.
5. Não alterar a assinatura das funções públicas sem autorização.
6. Não gerar novas funcionalidades sem testes correspondentes.
7. Não inserir código duplicado ou desnecessário.
8. Não assumir comportamentos que não estejam especificados no contrato de negócio.
9. Não inserir comentários ou código desnecessários.
10. Não modificar requisitos definidos na especificação para adequá-los ao código.
11. Não ignorar erros ou exceções.
12. Sempre priorizar a conformidade com o contrato definido.
13. Toda alteração relevante deverá ser validada pelos testes automatizados.
14. O código gerado deverá passar por revisão humana antes de ser considerado aprovado.

## 9. Arquitetura do Repositório

A estrutura planejada para o repositório Git/GitHub na Fase 2 será:

```text
sdd-task-analyzer/
├── README.md
├── CONTEXT_RULES.md
├── specs/
│   └── task_analyzer_spec.md
├── tests/
│   └── test_harness.py
└── src/
    └── task_analyzer.py
```

### 9.1 Descrição dos arquivos

| Arquivo | Descrição |
|---|---|
| `README.md` | Conterá uma visão geral do projeto, seu objetivo e instruções básicas de utilização. |
| `CONTEXT_RULES.md` | Conterá as regras persistentes que deverão orientar os agentes de Inteligência Artificial durante a geração e manutenção do código. |
| `specs/task_analyzer_spec.md` | Conterá a especificação SDD e o contrato utilizado como fonte da verdade para o desenvolvimento. |
| `tests/test_harness.py` | Conterá os testes automatizados responsáveis por validar o código gerado. |
| `src/task_analyzer.py` | Conterá a implementação do TaskAnalyzer gerada e posteriormente homologada. |

## 10. Plano de Homologação Humana

Na Fase 2, todo código gerado pela Inteligência Artificial deverá passar por uma revisão crítica humana antes de ser aceito e versionado.

A homologação seguirá as seguintes etapas:

1. Executar todos os testes automatizados.
2. Verificar se o código está de acordo com o contrato de negócio.
3. Verificar se as regras definidas no `CONTEXT_RULES.md` foram respeitadas.
4. Avaliar a qualidade, a legibilidade e a organização do código.
5. Verificar o tratamento de erros e exceções.
6. Confirmar que não foram introduzidos comportamentos não especificados.
7. Realizar correções quando necessário.
8. Aprovar o código somente após a validação completa.
9. Versionar a implementação aprovada no Git/GitHub.

A revisão humana é importante porque a utilização de Inteligência Artificial não elimina a responsabilidade do desenvolvedor. O desenvolvedor permanece responsável por verificar se o resultado gerado atende aos requisitos técnicos e de negócio.

## 11. Fluxo do Projeto Cumulativo

O projeto será desenvolvido em três etapas.

### Fase 1 — Especificação

Nesta etapa será construída a especificação SDD, incluindo:

- Contrato de negócio;
- Cenários de aceite;
- Regras de contexto;
- Estrutura planejada do repositório;
- Planejamento do Test Harness.

### Fase 2 — Implementação

Na próxima etapa, a especificação será utilizada como base para:

- Geração do código por agentes de IA;
- Criação dos testes automatizados;
- Execução do Test Harness;
- Versionamento utilizando Git/GitHub;
- Revisão e homologação humana.

### Fase 3 — Entrega final

Na etapa final serão incorporados:

- Automação;
- Integração contínua;
- GitHub Actions;
- Governança;
- Segurança;
- Monitoramento;
- Revisão ética;
- Homologação final.

## 12. Conclusão

A utilização do *Spec-Driven Development* permite estabelecer uma especificação técnica clara antes da implementação do sistema.

No TaskAnalyzer, o contrato define as entradas, saídas, regras de negócio e comportamentos esperados. Os cenários de aceite estabelecem como esses comportamentos serão validados, enquanto o Test Harness permitirá automatizar essa validação na Fase 2.

As `CONTEXT_RULES` estabelecem limites e padrões para os agentes de Inteligência Artificial, contribuindo para que o código gerado permaneça alinhado às necessidades do projeto.

Dessa forma, a especificação funciona como uma fonte da verdade para o desenvolvimento, facilitando a validação, a rastreabilidade e a homologação humana do código produzido com auxílio de Inteligência Artificial.

## 13. Vídeo de Apresentação da Documentação

[Assistir ao vídeo de apresentação da documentação](https://youtu.be/U-Og4mQcw-8)

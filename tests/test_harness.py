"""Suíte de testes automatizados (Test Harness) para o módulo TaskAnalyzer.

Este módulo traduz os cenários de aceite e casos de borda definidos no contrato
de negócio (task_analyzer_spec.md) em testes automatizados executados via pytest.
"""

from datetime import datetime, timedelta
from typing import Any, Dict, List

import pytest

from src.task_analyzer import TaskValidationError, analyze_tasks


def test_cenario_1_analise_com_sucesso_calculos_gerais_e_por_prioridade() -> None:
    """Valida os cálculos de métricas gerais e por prioridade para um conjunto de tarefas válidas.

    Cenário de Aceite 1:
    - Tarefa 1 (Alta): Criada há 10h, concluída após 4h (4.0 horas).
    - Tarefa 2 (Alta): Criada há 8h, concluída após 2h (2.0 horas).
      -> Média Prioridade Alta: (4.0 + 2.0) / 2 = 3.0 horas.
    - Tarefa 3 (Baixa): Criada há 12h, concluída após 6h (6.0 horas).
      -> Média Prioridade Baixa: 6.0 horas.
    - Tarefa 4 (Baixa): Pendente (sem data_conclusao).

    Métricas Gerais Esperadas:
    - total_tarefas: 4
    - total_concluidas: 3
    - total_pendentes: 1
    - tempo_medio_conclusao_horas: (4.0 + 2.0 + 6.0) / 3 = 4.0 horas.
    """
    agora = datetime.now()

    tarefas_teste: List[Dict[str, Any]] = [
        {
            "id": 1,
            "titulo": "Tarefa Alta 1",
            "prioridade": "Alta",
            "data_criacao": agora - timedelta(hours=10),
            "data_conclusao": agora - timedelta(hours=6),
            "status": "concluida",
        },
        {
            "id": 2,
            "titulo": "Tarefa Alta 2",
            "prioridade": "Alta",
            "data_criacao": agora - timedelta(hours=8),
            "data_conclusao": agora - timedelta(hours=6),
            "status": "concluida",
        },
        {
            "id": 3,
            "titulo": "Tarefa Baixa 1",
            "prioridade": "Baixa",
            "data_criacao": agora - timedelta(hours=12),
            "data_conclusao": agora - timedelta(hours=6),
            "status": "concluida",
        },
        {
            "id": 4,
            "titulo": "Tarefa Baixa 2 Pendente",
            "prioridade": "Baixa",
            "data_criacao": agora - timedelta(hours=2),
            "data_conclusao": None,
            "status": "pendente",
        },
    ]

    resultado = analyze_tasks(tarefas_teste)

    # Validação dos totais
    assert resultado["total_tarefas"] == 4
    assert resultado["total_concluidas"] == 3
    assert resultado["total_pendentes"] == 1

    # Validação dos tempos médios gerais
    assert resultado["tempo_medio_conclusao_horas"] == 4.0

    # Validação das métricas agrupadas por prioridade
    metricas_prio = resultado["metricas_por_prioridade"]
    assert "Alta" in metricas_prio
    assert metricas_prio["Alta"]["total_tarefas"] == 2
    assert metricas_prio["Alta"]["total_concluidas"] == 2
    assert metricas_prio["Alta"]["total_pendentes"] == 0
    assert metricas_prio["Alta"]["tempo_medio_conclusao_horas"] == 3.0

    assert "Baixa" in metricas_prio
    assert metricas_prio["Baixa"]["total_tarefas"] == 2
    assert metricas_prio["Baixa"]["total_concluidas"] == 1
    assert metricas_prio["Baixa"]["total_pendentes"] == 1
    assert metricas_prio["Baixa"]["tempo_medio_conclusao_horas"] == 6.0


def test_cenario_1_taxa_atraso_percentual() -> None:
    """Valida o cálculo da taxa de atraso percentual quando o status indica atraso.

    Cenário:
    - 4 tarefas no total.
    - 1 tarefa com status 'atrasada' (1 / 4 = 25.0%).
    """
    agora = datetime.now()

    tarefas_teste: List[Dict[str, Any]] = [
        {
            "id": 101,
            "titulo": "Tarefa Atrasada",
            "prioridade": "Média",
            "data_criacao": agora - timedelta(days=2),
            "data_conclusao": None,
            "status": "atrasada",
        },
        {
            "id": 102,
            "titulo": "Tarefa Normal",
            "prioridade": "Média",
            "data_criacao": agora - timedelta(hours=5),
            "data_conclusao": agora - timedelta(hours=1),
            "status": "concluida",
        },
        {
            "id": 103,
            "titulo": "Tarefa Em Dia 1",
            "prioridade": "Alta",
            "data_criacao": agora - timedelta(hours=3),
            "data_conclusao": None,
            "status": "em_andamento",
        },
        {
            "id": 104,
            "titulo": "Tarefa Em Dia 2",
            "prioridade": "Baixa",
            "data_criacao": agora - timedelta(hours=1),
            "data_conclusao": None,
            "status": "em_andamento",
        },
    ]

    resultado = analyze_tasks(tarefas_teste)

    assert resultado["total_tarefas"] == 4
    assert resultado["taxa_atraso_percentual"] == 25.0


def test_cenario_2_excecao_data_conclusao_anterior_a_data_criacao() -> None:
    """Valida o disparo de TaskValidationError para datas inconsistentes.

    Cenário de Aceite 2:
    - data_conclusao é anterior à data_criacao.
    """
    agora = datetime.now()

    tarefas_involucradas: List[Dict[str, Any]] = [
        {
            "id": 99,
            "titulo": "Tarefa com Data Invalida",
            "prioridade": "Alta",
            "data_criacao": agora,
            "data_conclusao": agora - timedelta(hours=2),  # Conclusão no passado!
            "status": "concluida",
        }
    ]

    with pytest.raises(TaskValidationError) as exc_info:
        analyze_tasks(tarefas_involucradas)

    assert "data_conclusao" in str(exc_info.value)
    assert "é anterior à" in str(exc_info.value)


def test_caso_borda_entrada_vazia() -> None:
    """Valida o comportamento da função ao receber uma lista vazia de tarefas.

    Garante retorno zerado sem disparar exceções não tratadas (ZeroDivisionError).
    """
    resultado = analyze_tasks([])

    assert resultado["total_tarefas"] == 0
    assert resultado["total_concluidas"] == 0
    assert resultado["total_pendentes"] == 0
    assert resultado["taxa_atraso_percentual"] == 0.0
    assert resultado["tempo_medio_conclusao_horas"] == 0.0
    assert resultado["metricas_por_prioridade"] == {}


def test_caso_borda_apenas_tarefas_pendentes() -> None:
    """Valida a execução quando existem apenas tarefas sem data de conclusão.

    Garante prevenção contra divisão por zero nos cálculos de média de tempo.
    """
    agora = datetime.now()

    tarefas_pendentes: List[Dict[str, Any]] = [
        {
            "id": 1,
            "titulo": "Pendente 1",
            "prioridade": "Alta",
            "data_criacao": agora - timedelta(hours=5),
            "data_conclusao": None,
            "status": "pendente",
        },
        {
            "id": 2,
            "titulo": "Pendente 2",
            "prioridade": "Alta",
            "data_criacao": agora - timedelta(hours=3),
            "data_conclusao": None,
            "status": "pendente",
        },
    ]

    resultado = analyze_tasks(tarefas_pendentes)

    assert resultado["total_tarefas"] == 2
    assert resultado["total_concluidas"] == 0
    assert resultado["total_pendentes"] == 2
    assert resultado["tempo_medio_conclusao_horas"] == 0.0
    assert resultado["metricas_por_prioridade"]["Alta"]["tempo_medio_conclusao_horas"] == 0.0


def test_arredondamento_duas_casas_decimais() -> None:
    """Valida se as médias e taxas numéricas são devidamente arredondadas para 2 casas decimais.

    Cenário:
    - 3 tarefas concluídas com tempos: 1h (1.0), 2h (2.0) e 2h (2.0) -> Média = 5/3 = 1.6666...
    - Resultado esperado: 1.67
    """
    agora = datetime.now()

    tarefas_para_arredondar: List[Dict[str, Any]] = [
        {
            "id": 1,
            "prioridade": "Média",
            "data_criacao": agora - timedelta(hours=1),
            "data_conclusao": agora,
            "status": "concluida",
        },
        {
            "id": 2,
            "prioridade": "Média",
            "data_criacao": agora - timedelta(hours=2),
            "data_conclusao": agora,
            "status": "concluida",
        },
        {
            "id": 3,
            "prioridade": "Média",
            "data_criacao": agora - timedelta(hours=2),
            "data_conclusao": agora,
            "status": "concluida",
        },
    ]

    resultado = analyze_tasks(tarefas_para_arredondar)

    assert resultado["tempo_medio_conclusao_horas"] == 1.67
    assert resultado["metricas_por_prioridade"]["Média"]["tempo_medio_conclusao_horas"] == 1.67
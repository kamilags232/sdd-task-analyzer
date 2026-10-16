import logging
from datetime import datetime
from typing import Any, Dict, List, Optional

# Configuração do logger estruturado
logger = logging.getLogger(__name__)


class TaskValidationError(Exception):
    """Exceção personalizada para erros de validação e consistência nos dados de tarefas."""

    pass


def _converter_e_validar_data(
    valor_data: Any, nome_campo: str, id_tarefa: Any
) -> Optional[datetime]:
    """Valida e converte um valor para o tipo datetime.

    Args:
        valor_data: O valor a ser validado (datetime, string ISO ou None).
        nome_campo: Nome do campo para contexto no log e na mensagem de erro.
        id_tarefa: Identificador da tarefa para rastreabilidade.

    Returns:
        Um objeto datetime válido ou None se o valor for ausente.

    Raises:
        TaskValidationError: Se o tipo ou formato da data for inválido.
    """
    if valor_data is None:
        return None

    if isinstance(valor_data, datetime):
        return valor_data

    if isinstance(valor_data, str):
        try:
            return datetime.fromisoformat(valor_data)
        except ValueError:
            msg = (
                f"Tarefa ID '{id_tarefa}': O campo '{nome_campo}' "
                f"possui uma string de data com formato inválido ('{valor_data}')."
            )
            logger.error(msg)
            raise TaskValidationError(msg)

    msg = f"Tarefa ID '{id_tarefa}': O campo '{nome_campo}' possui tipo inválido."
    logger.error(msg)
    raise TaskValidationError(msg)


def analyze_tasks(tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analisa um conjunto de tarefas e calcula métricas de produtividade.

    Args:
        tasks: Lista de dicionários, onde cada dicionário representa uma tarefa.

    Returns:
        Dicionário contendo métricas gerais (totais, médias e taxas) e
        médias agrupadas por prioridade.

    Raises:
        TaskValidationError: Se houver campos obrigatórios ausentes, tipos
            inválidos ou datas inconsistentes (ex.: data_conclusao < data_criacao).
    """
    logger.info("Iniciando a análise de %d tarefas.", len(tasks))

    # Tratamento para entrada vazia (Caso de borda)
    if not tasks:
        logger.info("A lista de tarefas fornecida está vazia.")
        return {
            "total_tarefas": 0,
            "total_concluidas": 0,
            "total_pendentes": 0,
            "taxa_atraso_percentual": 0.0,
            "tempo_medio_conclusao_horas": 0.0,
            "metricas_por_prioridade": {},
        }

    total_tarefas = len(tasks)
    total_concluidas = 0
    total_pendentes = 0
    total_atrasadas = 0
    tempos_conclusao_geral: List[float] = []

    # Estrutura para agrupar dados por prioridade
    dados_prioridade: Dict[str, Dict[str, Any]] = {}

    for idx, tarefa in enumerate(tasks):
        id_tarefa = tarefa.get("id", f"indice_{idx}")

        # Validação de campos obrigatórios conforme especificação SDD
        if "data_criacao" not in tarefa or tarefa["data_criacao"] is None:
            msg = f"Tarefa ID '{id_tarefa}': Campo obrigatório 'data_criacao' está ausente."
            logger.error(msg)
            raise TaskValidationError(msg)

        data_criacao = _converter_e_validar_data(
            tarefa["data_criacao"], "data_criacao", id_tarefa
        )
        data_conclusao = _converter_e_validar_data(
            tarefa.get("data_conclusao"), "data_conclusao", id_tarefa
        )

        prioridade = str(tarefa.get("prioridade", "NÃO ESPECIFICADA"))
        status = str(tarefa.get("status", "")).strip().lower()

        # Inicialização do agrupador por prioridade
        if prioridade not in dados_prioridade:
            dados_prioridade[prioridade] = {
                "total_tarefas": 0,
                "total_concluidas": 0,
                "total_pendentes": 0,
                "tempos_conclusao": [],
            }

        dados_prioridade[prioridade]["total_tarefas"] += 1

        # Processamento de tarefas concluídas vs pendentes
        if data_conclusao is not None:
            # Validação lógica de datas
            if data_conclusao < data_criacao:  # type: ignore
                msg = (
                    f"Tarefa ID '{id_tarefa}': Inconsistência de datas. "
                    f"data_conclusao ({data_conclusao}) não pode ser anterior "
                    f"data_conclusao ({data_conclusao}) é anterior à data_criacao ({data_criacao})."
                )
                logger.error(msg)
                raise TaskValidationError(msg)

            total_concluidas += 1
            dados_prioridade[prioridade]["total_concluidas"] += 1

            # Cálculo da diferença em horas
            diferenca = data_conclusao - data_criacao  # type: ignore
            horas = diferenca.total_seconds() / 3600.0
            tempos_conclusao_geral.append(horas)
            dados_prioridade[prioridade]["tempos_conclusao"].append(horas)
        else:
            total_pendentes += 1
            dados_prioridade[prioridade]["total_pendentes"] += 1

        # Verificação de atraso sem assumir regras não especificadas
        if status == "atrasada" or tarefa.get("atrasada") is True:
            total_atrasadas += 1

    # Prevenção de divisão por zero - Tempo médio geral
    tempo_medio_geral = 0.0
    if tempos_conclusao_geral:
        tempo_medio_geral = sum(tempos_conclusao_geral) / len(tempos_conclusao_geral)

    # Prevenção de divisão por zero - Taxa de atraso geral
    taxa_atraso_geral = 0.0
    if total_tarefas > 0:
        taxa_atraso_geral = (total_atrasadas / total_tarefas) * 100.0

    # Construção dos indicadores por prioridade
    metricas_por_prioridade: Dict[str, Dict[str, Any]] = {}
    for prio, info in dados_prioridade.items():
        tempos = info["tempos_conclusao"]
        tempo_medio_prio = 0.0
        if tempos:
            tempo_medio_prio = sum(tempos) / len(tempos)

        metricas_por_prioridade[prio] = {
            "total_tarefas": info["total_tarefas"],
            "total_concluidas": info["total_concluidas"],
            "total_pendentes": info["total_pendentes"],
            "tempo_medio_conclusao_horas": round(tempo_medio_prio, 2),
        }

    resultado = {
        "total_tarefas": total_tarefas,
        "total_concluidas": total_concluidas,
        "total_pendentes": total_pendentes,
        "taxa_atraso_percentual": round(taxa_atraso_geral, 2),
        "tempo_medio_conclusao_horas": round(tempo_medio_geral, 2),
        "metricas_por_prioridade": metricas_por_prioridade,
    }

    logger.info("Análise de tarefas concluída com sucesso.")
    return resultado
#  Implementação Core — TaskAnalyzer

Esta ramificação (`feature/task-analyzer-impl`) contém o código-fonte da aplicação desenvolvido em Python 3.11+.

---

## Conteúdo da Ramificação

- **`src/task_analyzer.py`:** Módulo principal contendo a função `analyze_tasks`, o tratamento de erros com `TaskValidationError` e os cálculos de métricas de produtividade.
- **`CONTEXT_RULES.md`:** Diretrizes de governança aplicadas durante a geração de código com IA.
- **`.gitignore` & `requirements.txt`:** Configurações de ambiente.

---

##  Funcionalidades Implementadas

- Validação estrita dos dados de entrada (campos obrigatórios, datas e formatos).
- Cálculo do tempo médio de conclusão (geral e por prioridade).
- Identificação da taxa de tarefas em atraso e contagem por status.

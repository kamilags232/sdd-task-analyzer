# Test Harness — TaskAnalyzer

Esta ramificação (`feature/test-harness`) armazena a suíte de testes automatizados com `pytest` para validação da regra de negócio e cenários de borda.

---

##  Conteúdo da Ramificação

- **`tests/test_harness.py`:** Suíte de testes (100% de aprovação) cobrindo cálculos de métricas, datas inconsistentes e tratamento de exceções.
- **`src/task_analyzer.py`:** Código-fonte analisado pela suíte de testes.
- **`requirements.txt`:** Dependências de teste (`pytest`).

---

## Como Executar os Testes

```bash
python -m pytest -v

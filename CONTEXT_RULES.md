# CONTEXT_RULES — TaskAnalyzer

## 1. Objetivo

Este documento define as regras obrigatórias que deverão orientar os agentes de Inteligência Artificial durante a geração, implementação e manutenção do código do projeto TaskAnalyzer.

O objetivo é garantir que o código permaneça alinhado à especificação SDD, respeitando os requisitos técnicos, as regras de negócio e as restrições definidas para o projeto.

## 2. Diretrizes Arquiteturais Obrigatórias

O código gerado deverá respeitar as seguintes diretrizes:

1. **Versão do Python:** utilizar Python 3.11 ou superior.
2. **Type hints:** utilizar anotações de tipo em todas as funções e métodos.
3. **Responsabilidade única (SRP):** cada função, método ou classe deverá possuir uma responsabilidade bem definida.
4. **Padrão PEP 8:** seguir as boas práticas de estilo e formatação do Python.
5. **Código limpo:** produzir código legível, organizado e manutenível.
6. **Nomenclatura:** utilizar nomes de variáveis, funções e classes descritivos.
7. **Google Style Docstrings:** documentar módulos, classes, funções e parâmetros utilizando o padrão Google Style.
8. **Coesão:** manter as funções pequenas, coesas e com uma única responsabilidade.
9. **Tratamento de exceções:** utilizar exceções específicas e mensagens claras para identificar os erros.
10. **Logging:** utilizar o módulo padrão `logging` para registrar eventos relevantes durante a execução.

## 3. Regras Restritivas

O agente de Inteligência Artificial deverá obedecer às seguintes restrições:

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
12. Priorizar sempre a conformidade com o contrato definido.
13. Validar toda alteração relevante por meio dos testes automatizados.
14. Submeter o código gerado à revisão humana antes de considerá-lo aprovado.

## 4. Conformidade com a Especificação SDD

O arquivo `specs/task_analyzer_spec.md` é a fonte da verdade para o desenvolvimento do TaskAnalyzer.

O agente de IA deverá:

- Respeitar os campos de entrada definidos na especificação.
- Implementar as métricas e saídas previstas no contrato.
- Seguir as regras de negócio e os cenários de aceite.
- Validar os dados de entrada e tratar erros conforme o contrato.
- Não inventar regras de negócio ou comportamentos não especificados.
- Identificar e documentar ambiguidades antes de implementar decisões que dependam delas.

### 4.1 Tratamento de ambiguidades

A especificação original não define completamente como identificar tarefas atrasadas, pois não estabelece um campo de prazo final nem uma regra completa para o cálculo da taxa de atraso.

Portanto, o agente de IA não deverá inventar silenciosamente essa regra. A interpretação deverá ser confirmada com o professor ou documentada explicitamente antes da implementação.

## 5. Testes e Validação

O código deverá ser validado por testes automatizados utilizando `pytest`, conforme o planejamento do Test Harness.

As seguintes regras deverão ser respeitadas:

- Não modificar os testes fornecidos apenas para fazer o código passar.
- Corrigir a implementação quando ela não atender aos requisitos.
- Verificar os casos de sucesso, as entradas inválidas e as situações de limite.
- Evitar erros de divisão por zero.
- Garantir que as exceções sejam tratadas conforme a especificação.
- Não considerar o código aprovado apenas porque parece funcionar.
- Realizar revisão humana antes da aprovação final.

## 6. Restrições Técnicas

- Utilizar somente bibliotecas autorizadas.
- Não utilizar arquivos ou bancos de dados para persistência.
- Não alterar a estrutura de pastas definida.
- Não alterar contratos públicos sem autorização.
- Não adicionar funcionalidades sem testes correspondentes.
- Manter o código simples, coeso e consistente com a especificação.

## 7. Prioridade das Regras

Em caso de dúvida durante a implementação:

1. Respeitar o contrato de negócio definido em `specs/task_analyzer_spec.md`.
2. Identificar requisitos ambíguos e solicitar esclarecimento ou documentar a decisão antes de implementá-los.
3. Preservar os testes e corrigir a implementação para atender aos requisitos.
4. Manter a conformidade com as diretrizes arquiteturais e restrições deste documento.
5. Submeter as alterações relevantes à validação automatizada e à revisão humana.

Nenhuma decisão de implementação deverá modificar silenciosamente os requisitos definidos na especificação SDD.
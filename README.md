# Construção de Projeto Ágil no GitHub: Da Gestão ao Controle de Qualidade

**Objetivo:** Simular o desenvolvimento de um sistema de gerenciamento de tarefas aplicando metodologias ágeis e boas práticas de Engenharia de Software.

## Escopo Inicial
- Sistema web básico para gerenciamento de tarefas (CRUD).
- Kanban no GitHub Projects com colunas: A Fazer, Em Progresso, Concluído.
- CI com GitHub Actions rodando testes automatizados (pytest).
- Histórico de commits semânticos.
- Simulação de mudança de escopo: adicionar campo `priority` e filtro por prioridade.

## Metodologia
Híbrido: Kanban para fluxo contínuo + Sprints curtos (1 semana) organizados via Issues e Projects.

## Estrutura do Repositório
```
/src
  app.py
  models.py
  storage.py
  requirements.txt
/tests
  test_tasks.py
/docs
  use_cases.puml
  classes.puml
.github/workflows/ci.yml
COMMITS.md
README.md
```


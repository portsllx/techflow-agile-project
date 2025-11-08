# Construindo um Projeto Ágil no GitHub: Da Gestão ao Controle de Qualidade

**Objetivo:** Simular o desenvolvimento de um sistema de gerenciamento de tarefas aplicando metodologias ágeis e boas práticas de Engenharia de Software.

## Escopo Inicial
- Sistema web básico para gerenciamento de tarefas (CRUD).
- Kanban no GitHub Projects com colunas: A Fazer, Em Progresso, Concluído.
- CI com GitHub Actions rodando testes automatizados (pytest).
- Histórico de commits semânticos (mínimo 10).
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
## Como executar (local)
1. Crie um ambiente virtual Python 3.8+:
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```
2. Instale dependências:
   ```
   pip install -r src/requirements.txt
   ```
3. Execute a aplicação:
   ```
   python src/app.py
   ```
4. Abra no navegador: http://127.0.0.1:5000

## Testes
Para rodar os testes:
```
pytest -q
```

## Mudança de Escopo (simulada)
Em commit posterior foi adicionada a feature **Prioridade de Tarefas**:
- Justificativa: cliente pediu priorização automática de entregas críticas.
- Ações: Adicionado campo `priority` em `models.py`, endpoints atualizados e testes modificados.
- Kanban: criado card "Adicionar prioridade e filtro" em To Do → Em Progresso → Done.

## Links importantes (para entrega)
- GitHub Projects: quadro Kanban (obrigatório — criar no repositório público).
- Workflow: `.github/workflows/ci.yml` — executa pytest.

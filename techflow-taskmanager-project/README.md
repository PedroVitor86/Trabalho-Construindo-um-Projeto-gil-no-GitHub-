# Construindo um Projeto Ágil no GitHub: Da Gestão ao Controle de Qualidade

**Projeto:** TechFlow Task Manager (sistema de gerenciamento de tarefas)  
**Autor:** Pedro Vitor (estudante)  
**Objetivo:** Simular o desenvolvimento ágil de um sistema de gerenciamento de tarefas usando GitHub (Projects, Actions, Commits) e práticas de engenharia de software.

## Escopo inicial
- Aplicação web simples com CRUD de tarefas (Create, Read, Update, Delete).
- Backend em Python (Flask) + SQLite (arquivo `tasks.db`).
- Rotas RESTful e interface mínima (HTML).
- Testes automatizados (pytest).
- Pipeline CI com GitHub Actions rodando os testes.
- Quadro Kanban no GitHub Projects com colunas: **A Fazer**, **Em Progresso**, **Concluído**.

## Como executar localmente
1. Criar um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate      # linux/mac
venv\Scripts\activate       # windows
pip install -r requirements.txt
python -m src.app
```
2. Acessar `http://127.0.0.1:5000` no navegador.

## Estrutura do repositório
```
/src
  ├─ app.py            # Flask app (CRUD)
  ├─ models.py         # ORM simples (sqlite)
  └─ templates/
      └─ index.html
/tests
  └─ test_app.py
/.github/workflows/ci.yml
/docs
  ├─ use_cases.puml
  └─ classes.puml
COMMIT_HISTORY.md
KANBAN.md
CHANGE_SCOPE.md
```

## Metodologia adotada
- Híbrido Kanban + Sprints curtos (2 semanas): Kanban para fluxo contínuo de trabalho, sprints para entregas incrementais.
- Daily standups (15 min), revisão de sprint, retrospective curta.

## Simulação de mudança de escopo
Ver `CHANGE_SCOPE.md` — adicionamos autenticação básica (login) como feature adicional justificada pelo cliente.

## Testes automatizados
- Pytest usado para testes unitários.
- GitHub Actions executa `pytest -q` em cada push/pull request.

## Evidências técnicas (prints e instruções)
- Crie o GitHub Project com as colunas **A Fazer / Em Progresso / Concluído**.
- Faça pelo menos 10 commits com mensagens semânticas (ver `COMMIT_HISTORY.md`).
- Configure GitHub Actions: arquivo `.github/workflows/ci.yml`.

## Observações finais
Este repositório é um scaffold para a atividade acadêmica. Substitua/expanda conforme sua linguagem preferida.

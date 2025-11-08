# Simulação de Mudança de Escopo

## Justificativa
O cliente solicitou que apenas membros autenticados possam criar e editar tarefas, para auditar mudanças no backlog. Essa necessidade surgiu após análise de riscos de operação.

## Alteração
- Adicionar autenticação simples (login/logout) com sessão.
- Restringir rotas de criação/edição/deleção a usuários autenticados.
- Atualizar README.md com instruções.

## Tarefas realizadas (exemplo)
- Criar card no Kanban: "Adicionar autenticação básica"
- Criar branch: feature/auth
- Commit: feat(auth): adicionar login simples e proteção de rotas
- Merge para main após revisão e testes

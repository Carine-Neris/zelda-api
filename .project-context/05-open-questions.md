# 05 — Questões em Aberto

> Memória do projeto. Atualize com fatos verificáveis, evidências e confiança.
> Última atualização: 2026-11-09

## Alta prioridade

### [Hipótese] Como `game_ids` de `Character` é persistido?
- Hipótese atual: tabela de associação many-to-many no banco, ou coluna JSON/TEXT
- O que verificar: `modules/characters/infrastructure/persistence/character_model.py`
- Importância: impacta integridade referencial e queries futuras

### [Hipótese] O módulo characters segue o mesmo padrão de factories que games?
- Hipótese: sim, por simetria
- O que verificar: `modules/characters/infrastructure/web/dependencies.py` e `modules/characters/router.py`

## Média prioridade

### [Lacuna] Não há testes de integração/funcionais (apenas arquitetura)
- Evidência: `tests/` contém apenas `test_architecture.py`
- Questão: a intenção é manter só testes de arquitetura? Há plano de adicionar testes de endpoints?

### [Lacuna] `release_date` sem validação de formato
- Questão: qual é o formato esperado? ISO 8601 (`YYYY-MM-DD`)? Livre?

### [Lacuna] Sem paginação em `GET /games/` e `GET /characters/`
- Use case `GetAllGameUseCase` retorna todos os registros sem limit/offset
- Questão: volume de dados esperado? Paginação será necessária?

## Baixa prioridade

### [Hipótese] `GameModel.id` default (`uuid.uuid4`) nunca é usado
- O domínio sempre gera o UUID antes de persistir
- O que confirmaria: adicionar log ou breakpoint no `GameModel.__init__`

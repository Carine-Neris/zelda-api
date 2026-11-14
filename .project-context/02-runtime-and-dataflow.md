# 02 — Runtime e Dataflow

> Memória do projeto. Atualize com fatos verificáveis, evidências e confiança.
> Última atualização: 2026-11-09

## Ciclo de uma request: POST /games/

```
Cliente HTTP
  → FastAPI router (modules/games/router.py)
    → FastAPI Depends resolve factory_create_game_use_case
      → factory_game_repository(db=get_db())   # abre sessão SQLAlchemy
        → SqlAlchemyGameRepository(db)
      → CreateGameUseCase(repo)
    → endpoint recebe CreateGameUseCase injetado
    → use_case.execute(GameCreateDTO)
      → constrói Game(dataclass) com uuid4() gerado no domínio
      → repo.create(game)
        → GameModel(**game.__dict__)
        → db.add → db.commit → db.refresh
        → retorna a entidade Game original (não o model!)
    → FastAPI serializa a resposta
  ← HTTP 201 Created
```

### [Fato | confiança: alta] UUID gerado no domínio, não no banco
- Evidência: `Game` dataclass usa `field(default_factory=uuid4)`; `GameModel` tem `default=uuid.uuid4` mas o objeto já chega com ID preenchido.
- Entendimento: O domínio controla a geração de identidade. Isso é consistente com Clean Architecture mas significa que `GameModel.id` default nunca é usado na prática.
- Atualizado em: 2026-11-09

### [Fato | confiança: alta] create() retorna a entidade de domínio, não o model
- Evidência: `sqlalchemy_game_repository.py` L20 — `return game` (o parâmetro recebido, não `db_game`)
- Entendimento: Funciona porque o `uuid4` já está no objeto. Mas se o banco modificasse algum campo (ex: timestamp auto), o retorno não refletiria. Atenção ao expandir o modelo.
- Atualizado em: 2026-11-09

## Ciclo de uma request: GET /games/{id}

```
Cliente HTTP
  → FastAPI router
    → db = Depends(get_db)  ← instanciado inline no router (não via factory)
    → SqlAlchemyGameRepository(db) instanciado inline no router
    → GetGameByIdUseCase(repository).execute(id)
      → repo.get_by_id(id) → query SQLAlchemy por UUID
      → retorna Game ou None
      → use_case levanta ValueError se None
    → router captura ValueError → HTTPException 404
  ← HTTP 200 / 404
```

### [Inferência | confiança: média] Inconsistência no padrão de injeção
- Hipótese: `POST /games/` usa factory via Depends; os demais endpoints (GET, PUT, DELETE) instanciam repositório e use case diretamente no corpo da função.
- Evidência: `router.py` L26-29 e L33-39 — instanciação inline; L18-22 — usa `Depends(factory_create_game_use_case)`.
- O que confirmaria: Verificar se existe intenção de migrar todos para o padrão factory.
- Atualizado em: 2026-11-09

## Autenticação e autorização

### [Fato | confiança: alta] Sem autenticação implementada
- Evidência: Nenhum middleware de auth em `main.py`, nenhuma dependência de token nos routers, nenhuma lib de auth no `pyproject.toml`.
- Atualizado em: 2026-11-09

## Tratamento de erros

- Use cases levantam `ValueError` para "não encontrado"
- Routers capturam `ValueError` e mapeiam para `HTTPException(404)`
- Erros de validação Pydantic são tratados automaticamente pelo FastAPI (422 Unprocessable Entity)

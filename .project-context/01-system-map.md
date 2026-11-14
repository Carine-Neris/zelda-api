# 01 — System Map

> Memória do projeto. Atualize com fatos verificáveis, evidências e confiança.
> Última atualização: 2026-11-09

## Arquitetura geral

O projeto segue **Clean Architecture** com separação explícita em 3 camadas por módulo:

```
modules/
  games/
    domain/           ← entidades puras + interfaces de repositório
    application/      ← use cases + DTOs (Pydantic)
    infrastructure/
      persistence/    ← implementação SQLAlchemy dos repositórios
      web/            ← factories de dependência (FastAPI Depends)
  characters/
    (mesma estrutura)
config/
  database.py         ← engine, SessionLocal, Base, get_db()
main.py               ← app FastAPI, registro de routers
```

## Componentes e responsabilidades

| Símbolo | Arquivo | Responsabilidade |
|---------|---------|-----------------|
| `app` (FastAPI) | `main.py` | Ponto de entrada HTTP; registra routers |
| `game_router` | `modules/games/router.py` | Endpoints REST de games (`/games`) |
| `character_router` | `modules/characters/router.py` | Endpoints REST de characters (`/characters`) |
| `Game` (dataclass) | `modules/games/domain/entities.py` | Entidade de domínio pura; sem dependência de infra |
| `IGameRepository` (ABC) | `modules/games/domain/repositories.py` | Contrato que a infra deve satisfazer |
| `GameCreateDTO / GameUpdateDTO / GameResponseDTO` | `modules/games/application/game_dto.py` | Contrato HTTP (Pydantic) |
| `CreateGameUseCase` etc. | `modules/games/application/use_cases/` | Lógica de aplicação; recebem repositório via construtor |
| `SqlAlchemyGameRepository` | `modules/games/infrastructure/persistence/sqlalchemy_game_repository.py` | Implementação concreta de `IGameRepository` |
| `GameModel` | `modules/games/infrastructure/persistence/game_model.py` | Mapeamento ORM → tabela `games` |
| `factory_*` | `modules/games/infrastructure/web/dependencies.py` | Factories injetadas pelo FastAPI Depends |
| `Base`, `get_db` | `config/database.py` | Base ORM compartilhada; gerador de sessão |

## Fronteiras de camada (regras verificadas por pytest-archon)

- **Domain** não importa Infrastructure
- **Application** não importa Infrastructure.web
- **Games** não importa Characters (e vice-versa)
- **Use cases** não se importam entre si dentro do mesmo módulo

## Banco de dados

- SQLite com arquivo `zelda.db` na raiz
- Tabelas criadas automaticamente no startup via `Base.metadata.create_all(bind=engine)`
- `check_same_thread=False` habilitado (necessário para FastAPI + SQLite)

### [Fato | confiança: alta] Importação de dialect PostgreSQL em contexto SQLite
- Evidência: `modules/games/infrastructure/persistence/game_model.py` L3 — `from sqlalchemy.dialects.postgresql import UUID`
- Entendimento: O tipo `UUID` do dialect PostgreSQL é usado no SQLite. SQLAlchemy aceita isso, mas pode gerar inconsistência se migrar para PostgreSQL real (o tipo já seria nativo). É uma mistura que funciona mas pode causar confusão.
- Atualizado em: 2026-11-09

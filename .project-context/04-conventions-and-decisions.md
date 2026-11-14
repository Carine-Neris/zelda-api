# 04 — Convenções e Decisões

> Memória do projeto. Atualize com fatos verificáveis, evidências e confiança.
> Última atualização: 2026-11-09

## Padrões observados

### [Fato | confiança: alta] Clean Architecture por módulo
- Cada módulo (`games`, `characters`) tem camadas: `domain/` → `application/` → `infrastructure/`
- Regras de isolamento verificadas automaticamente por `pytest-archon` em `tests/test_architecture.py`
- Atualizado em: 2026-11-09

### [Fato | confiança: alta] Repositório como interface + implementação separada
- Interface: `IGameRepository` (ABC) em `domain/repositories.py`
- Implementação: `SqlAlchemyGameRepository` em `infrastructure/persistence/`
- Use cases recebem o repositório via construtor (injeção de dependência manual)
- Atualizado em: 2026-11-09

### [Fato | confiança: alta] DTOs Pydantic separados da entidade de domínio
- `GameCreateDTO`, `GameUpdateDTO`, `GameResponseDTO` em `application/game_dto.py`
- A entidade de domínio `Game` é um `@dataclass` puro (sem Pydantic)
- Atualizado em: 2026-11-09

### [Fato | confiança: alta] Factories de Depends em `infrastructure/web/dependencies.py`
- Padrão identificado no módulo games; provavelmente replicado em characters
- Apenas `factory_create_game_use_case` está em uso; outros endpoints instanciam inline
- Atualizado em: 2026-11-09

## Decisões e trade-offs

### [Decisão | confiança: alta] SQLite como banco de dados
- Facilita setup local sem Docker; zero configuração
- Limitação: não adequado para produção com concorrência alta; UUID do dialect PostgreSQL importado (ver `01-system-map.md`)

### [Decisão | confiança: alta] UUID gerado no domínio
- O `id` é gerado por `uuid4()` na entidade de domínio, não delegado ao banco
- Vantagem: entidade sempre tem identidade antes de persistir
- Atualizado em: 2026-11-09

## Anti-padrões observados

### [Anti-padrão | confiança: alta] Injeção inconsistente nos endpoints
- `POST /games/` usa factory/Depends; `GET`, `PUT`, `DELETE` instanciam repositório inline no corpo do endpoint
- Evidência: `modules/games/router.py`
- Risco: dificulta testes unitários dos endpoints que não usam factory
- Atualizado em: 2026-11-09

### [Anti-padrão | confiança: média] `release_date` como string sem validação
- Campo `str` sem formato definido; pode receber "25/05/2026" ou "2026-05-25" indistintamente
- Evidência: `Game` dataclass e `GameCreateDTO`
- Atualizado em: 2026-11-09

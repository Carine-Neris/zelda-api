# 00 — Índice do Projeto

> Memória do projeto. Atualize com fatos verificáveis, evidências e confiança.
> Última atualização: 2026-11-09

## Stack detectada

| Componente        | Tecnologia                              |
|-------------------|-----------------------------------------|
| Linguagem         | Python ≥ 3.14                          |
| Framework web     | FastAPI 0.136.x                         |
| ORM               | SQLAlchemy 2.x (DeclarativeBase)        |
| Banco de dados    | SQLite (`zelda.db` — arquivo local)     |
| Servidor          | Uvicorn                                 |
| Validação HTTP    | Pydantic (via FastAPI)                  |
| Gerenc. de pacotes| Poetry (package-mode = false)           |
| Testes            | pytest + pytest-archon                  |
| Lint/Hooks        | pre-commit                              |
| Debug             | ipdb                                    |

## Entrypoint principal

- [`main.py`](../main.py) — cria o app FastAPI, registra routers e chama `Base.metadata.create_all`

## Comandos importantes

```bash
# Rodar o servidor
uvicorn main:app --reload

# Rodar testes (incluindo regras de arquitetura)
pytest

# Instalar dependências
poetry install
```

## Módulos

- `modules/games/` → CRUD completo de jogos da franquia Zelda
- `modules/characters/` → CRUD de personagens, com vínculo a games via `game_ids`

## Navegação por capítulo

| Arquivo                       | Conteúdo                                      |
|-------------------------------|-----------------------------------------------|
| `01-system-map.md`            | Componentes, fronteiras, camadas              |
| `02-runtime-and-dataflow.md`  | Ciclo de uma request de ponta a ponta         |
| `03-domain-glossary.md`       | Entidades e regras de negócio                 |
| `04-conventions-and-decisions.md` | Padrões, decisões e anti-padrões observados |
| `05-open-questions.md`        | Lacunas e hipóteses a confirmar               |
| `06-task-notes.md`            | Notas temporárias por task                    |

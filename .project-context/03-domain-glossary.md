# 03 — Domain Glossary

> Memória do projeto. Atualize com fatos verificáveis, evidências e confiança.
> Última atualização: 2026-11-09

## Entidades

### Game
- **Arquivo:** `modules/games/domain/entities.py`
- **Tipo:** `@dataclass`
- **Campos:** `id: UUID`, `name: str`, `release_date: str`, `description: str`, `developer: str`, `publisher: str`, `is_spin_off: bool`
- **Regras de negócio observadas:** nenhuma validação explícita na entidade (campos obrigatórios apenas por tipo).
- **Nota:** `release_date` é `str`, não `date` — sem validação de formato.

### Character
- **Arquivo:** `modules/characters/domain/entities.py`
- **Tipo:** `@dataclass`
- **Campos:** `id: UUID`, `name: str`, `race: str`, `age: int`, `gender: str`, `description: str`, `image_url: str | None`, `game_ids: list[UUID]`
- **Regras de negócio verificadas em `__post_init__`:**
  - `age >= 0` (levanta `ValueError` se negativo)
  - `game_ids` não pode ser vazio (levanta `ValueError`)
- **Relação com Game:** referência por `game_ids` (lista de UUIDs), sem FK no banco verificada até agora.

## Termos de negócio

| Termo | Definição observada |
|-------|---------------------|
| `is_spin_off` | Flag booleana no `Game` que indica se o título é spin-off da franquia principal. Default `False`. |
| `game_ids` | Lista de IDs dos jogos aos quais um `Character` pertence. Mínimo 1 (regra no domínio). |
| `race` | Raça do personagem (ex: Hylian, Gerudo, Kokiri). Sem enum definido — campo livre. |

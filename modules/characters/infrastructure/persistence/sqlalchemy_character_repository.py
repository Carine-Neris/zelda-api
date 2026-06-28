from typing import Optional
from uuid import UUID

from sqlalchemy import Table, Column, ForeignKey, delete, insert, select
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Session

from config.database import Base
from modules.characters.domain.entities import Character
from modules.characters.domain.repositories import ICharacterRepository
from modules.characters.infrastructure.persistence.character_model import CharacterModel


character_games = Table(
    "character_games",
    Base.metadata,
    Column("character_id", PGUUID(as_uuid=True), ForeignKey("characters.id"), primary_key=True),
    Column("game_id", PGUUID(as_uuid=True), ForeignKey("games.id"), primary_key=True),
)


class SqlAlchemyCharacterRepository(ICharacterRepository):
    def __init__(self, db: Session):
        self.db = db

    def _games_table(self):
        games_table = Base.metadata.tables.get("games")
        if games_table is None:
            raise RuntimeError("Games table is not available in metadata")
        return games_table

    def _character_game_ids(self, character_id: UUID) -> list[UUID]:
        rows = self.db.execute(
            select(character_games.c.game_id).where(character_games.c.character_id == character_id)
        ).scalars().all()
        return list(rows)

    def _ensure_games_exist(self, game_ids: list[UUID]) -> None:
        existing_ids = set(
            self.db.execute(
                select(self._games_table().c.id).where(self._games_table().c.id.in_(game_ids))
            ).scalars().all()
        )
        missing_ids = set(game_ids) - existing_ids
        if missing_ids:
            missing_list = ", ".join(str(game_id) for game_id in sorted(missing_ids, key=str))
            raise ValueError(f"Game(s) not found: {missing_list}")

    def _to_domain(self, db_character: CharacterModel) -> Character:
        return Character(
            id=db_character.id,
            name=db_character.name,
            race=db_character.race,
            age=db_character.age,
            gender=db_character.gender,
            description=db_character.description,
            image_url=db_character.image_url,
            game_ids=self._character_game_ids(db_character.id),
        )

    def create(self, character: Character) -> Character:
        self._ensure_games_exist(character.game_ids)

        db_character = CharacterModel(
            id=character.id,
            name=character.name,
            race=character.race,
            age=character.age,
            gender=character.gender,
            description=character.description,
            image_url=character.image_url,
        )
        self.db.add(db_character)
        self.db.flush()

        self.db.execute(
            insert(character_games),
            [{"character_id": character.id, "game_id": game_id} for game_id in character.game_ids],
        )
        self.db.commit()
        return self._to_domain(db_character)

    def get_all(self) -> list[Character]:
        db_characters = self.db.query(CharacterModel).all()
        return [self._to_domain(db_character) for db_character in db_characters]

    def get_by_id(self, id: UUID) -> Optional[Character]:
        db_character = self.db.query(CharacterModel).filter(CharacterModel.id == id).first()
        if db_character is None:
            return None
        return self._to_domain(db_character)

    def update(self, character: Character) -> Character:
        self._ensure_games_exist(character.game_ids)

        db_character = self.db.query(CharacterModel).filter(CharacterModel.id == character.id).first()
        if db_character is None:
            raise ValueError("Character not found")

        db_character.name = character.name
        db_character.race = character.race
        db_character.age = character.age
        db_character.gender = character.gender
        db_character.description = character.description
        db_character.image_url = character.image_url

        self.db.execute(delete(character_games).where(character_games.c.character_id == character.id))
        self.db.execute(
            insert(character_games),
            [{"character_id": character.id, "game_id": game_id} for game_id in character.game_ids],
        )
        self.db.commit()
        return self._to_domain(db_character)

    def delete(self, id: UUID) -> None:
        self.db.execute(delete(character_games).where(character_games.c.character_id == id))
        db_character = self.db.query(CharacterModel).filter(CharacterModel.id == id).first()
        if db_character is not None:
            self.db.delete(db_character)
            self.db.commit()
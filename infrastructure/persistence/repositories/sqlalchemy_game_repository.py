from sqlalchemy.orm import Session
from uuid import UUID
from typing import Optional
from domain.entities import Game
from domain.repositories import IGameRepository
from infrastructure.persistence.models.game_model import GameModel


class SqlAlchemyGameRepository(IGameRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, game: Game) -> Game:
        db_game = GameModel(**game.__dict__)

        self.db.add(db_game)
        self.db.commit()
        self.db.refresh(db_game)

        return game

    def get_all(self) -> list[Game]:
        db_games = self.db.query(GameModel).all()

        return [
            Game(
                id=g.id,
                name=g.name,
                release_date=g.release_date,
                description=g.description,
                developer=g.developer,
                publisher=g.publisher,
                is_spin_off=g.is_spin_off,
            )
            for g in db_games
        ]

    def get_by_id(self, id: UUID) -> Optional[Game]:
        db_game = self.db.query(GameModel).filter(GameModel.id == id).first()

        if db_game is None:
            return None

        return Game(
            id=db_game.id,
            name=db_game.name,
            release_date=db_game.release_date,
            description=db_game.description,
            developer=db_game.developer,
            publisher=db_game.publisher,
            is_spin_off=db_game.is_spin_off,
        )

    def update(self, game: Game) -> Game:
        db_game = self.db.query(GameModel).filter(GameModel.id == game.id).first()

        db_game.name = game.name
        db_game.release_date = game.release_date
        db_game.description = game.description
        db_game.developer = game.developer
        db_game.publisher = game.publisher
        db_game.is_spin_off = game.is_spin_off

        self.db.commit()
        self.db.refresh(db_game)

        return game

    def delete(self, id: UUID) -> None:
        db_game = self.db.query(GameModel).filter(GameModel.id == id).first()

        self.db.delete(db_game)
        self.db.commit()

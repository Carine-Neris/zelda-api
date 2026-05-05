from fastapi import Depends
from sqlalchemy.orm import Session
from infrastructure.persistence.database import get_db
from infrastructure.persistence.repositories.sqlalchemy_game_repository import SqlAlchemyGameRepository
from application.use_cases.create_game import CreateGameUseCase
from application.use_cases.get_game_by_id import GetGameByIdUseCase

# Fábrica para o Repositório
def factory_game_repository(db: Session = Depends(get_db)):
    return SqlAlchemyGameRepository(db)

# Fábrica para o CreateUseCase
def factory_create_game_use_case(repo = Depends(factory_game_repository)):
    return CreateGameUseCase(repo)

# Fábrica para o GetByIdUseCase
def factory_get_game_use_case(repo = Depends(factory_game_repository)):
    return GetGameByIdUseCase(repo)

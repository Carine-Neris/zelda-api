from fastapi import Depends
from sqlalchemy.orm import Session

from config.database import get_db
from modules.characters.application.use_cases.create_character import CreateCharacterUseCase
from modules.characters.application.use_cases.delete_character import DeleteCharacterUseCase
from modules.characters.application.use_cases.get_all_character import GetAllCharacterUseCase
from modules.characters.application.use_cases.get_character_by_id import GetCharacterByIdUseCase
from modules.characters.application.use_cases.update_character import UpdateCharacterUseCase
from modules.characters.infrastructure.persistence.sqlalchemy_character_repository import SqlAlchemyCharacterRepository


def factory_character_repository(db: Session = Depends(get_db)):
    return SqlAlchemyCharacterRepository(db)


def factory_create_character_use_case(repo = Depends(factory_character_repository)):
    return CreateCharacterUseCase(repo)


def factory_get_all_character_use_case(repo = Depends(factory_character_repository)):
    return GetAllCharacterUseCase(repo)


def factory_get_character_by_id_use_case(repo = Depends(factory_character_repository)):
    return GetCharacterByIdUseCase(repo)


def factory_update_character_use_case(repo = Depends(factory_character_repository)):
    return UpdateCharacterUseCase(repo)


def factory_delete_character_use_case(repo = Depends(factory_character_repository)):
    return DeleteCharacterUseCase(repo)
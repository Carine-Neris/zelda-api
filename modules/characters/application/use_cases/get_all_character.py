from modules.characters.domain.entities import Character
from modules.characters.domain.repositories import ICharacterRepository
from typing import List


class GetAllCharacterUseCase:
    def __init__(self, character_repo: ICharacterRepository):
        self.character_repo = character_repo

    def execute(self) -> List[Character]:
        characters = self.character_repo.get_all()
        return characters

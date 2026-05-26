from modules.characters.domain.entities import Character
from modules.characters.domain.repositories import ICharacterRepository
from uuid import UUID


class GetCharacterByIdUseCase:
    def __init__(self, character_repo: ICharacterRepository):
        self.character_repo = character_repo

    def execute(self, id: UUID) -> Character:
        character = self.character_repo.get_by_id(id)
        if not character:
            raise ValueError(f"Personagem com ID {id} não encontrado.")

        return character

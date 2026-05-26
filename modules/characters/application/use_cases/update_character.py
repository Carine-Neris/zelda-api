from modules.characters.domain.entities import Character
from modules.characters.domain.repositories import ICharacterRepository
from modules.characters.application.characters_dto import CharacterUpdateDTO
from uuid import UUID


class UpdateCharacterUseCase:
    def __init__(self, character_repo: ICharacterRepository):
        self.character_repo = character_repo

    def execute(self, character_id: UUID, data: CharacterUpdateDTO) -> Character:
        character = self.character_repo.get_by_id(character_id)
        if not character:
            raise ValueError("Character not found")

        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(character, key, value)

        updated_character = self.character_repo.update(character)
        return updated_character

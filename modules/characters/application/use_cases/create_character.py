from modules.characters.domain.entities import Character
from modules.characters.domain.repositories import ICharacterRepository
from modules.characters.application.characters_dto import CharacterCreateDTO


class CreateCharacterUseCase:
    def __init__(self, character_repo: ICharacterRepository):
        self.character_repo = character_repo

    def execute(self, data: CharacterCreateDTO) -> Character:
        new_character = Character(
            name=data.name,
            race=data.race,
            age=data.age,
            gender=data.gender,
            description=data.description,
            game_ids=data.game_ids,
            image_url=data.image_url
        )
        return self.character_repo.create(new_character)

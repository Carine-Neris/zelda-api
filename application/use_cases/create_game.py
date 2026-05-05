from domain.entities import Game
from domain.repositories import IGameRepository
from application.dto.game_dto import GameCreateDTO


class CreateGameUseCase:
    def __init__(self,game_repo:IGameRepository):
        self.game_repo = game_repo
    
    def execute(self, data: GameCreateDTO) -> Game:
        new_game = Game(
            name=data.name,
            release_date=data.release_date,
            description=data.description,
            developer=data.developer,
            publisher=data.publisher,
            is_spin_off=data.is_spin_off
        )
        return self.game_repo.create(new_game)
        
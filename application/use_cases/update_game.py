from domain.entities import Game
from domain.repositories import IGameRepository
from application.dto.game_dto import GameUpdateDTO
from uuid import UUID


class UpdateGameUseCase:
    def __init__(self, game_repo:IGameRepository):
        self.game_repo = game_repo
    

    def execute(self, game_id:UUID,data:GameUpdateDTO)->Game:
        game = self.game_repo.get_by_id(game_id)
        if not game:
            raise ValueError("Game not found")
        
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(game,key,value)

        updated_game = self.game_repo.update(game)
        return updated_game

    

from modules.games.domain.repositories import IGameRepository
from modules.games.domain.entities import Game
from uuid  import UUID


class DeleteGameUseCase:
    def __init__(self, game_repo: IGameRepository):
        self.game_repo = game_repo

    def execute(self,id:UUID):
        game = self.game_repo.get_by_id(id)
        if not game:
            raise ValueError(f"Jogo com ID {id} não encontrado.")
        self.game_repo.delete(id)
        return True





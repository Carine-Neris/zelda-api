from modules.games.domain.entities import Game
from modules.games.domain.repositories import IGameRepository
from uuid import UUID


class GetGameByIdUseCase:
    def __init__(self, game_repo: IGameRepository):
        self.game_repo = game_repo

    def execute(self, id: UUID) -> Game:
        game = self.game_repo.get_by_id(id)
        if not game:
            raise ValueError(f"Jogo com ID {id} não encontrado.")

        return game
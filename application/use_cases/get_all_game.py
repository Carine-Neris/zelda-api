from domain.entities import Game
from domain.repositories import IGameRepository
from typing import List


class GetAllGameUseCase:
    def __init__(self,game_repo:IGameRepository):
        self.game_repo = game_repo

    def execute(self) -> List[Game]:
        games = self.game_repo.get_all()

        return games

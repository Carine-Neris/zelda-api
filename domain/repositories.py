from abc import ABC, abstractmethod
from uuid import UUID
from .entities import Game
from typing import Optional

class IGameRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Games]:
        """Get all games"""
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self,id:UUID) -> Optional[Games]:
        """Get game by id"""
        raise NotImplementedError

    @abstractmethod
    def create(self,game:Games) -> Games:
        """Create game"""
        raise NotImplementedError

    @abstractmethod
    def update(self,game:Games) -> Games:
        """Update game"""
        raise NotImplementedError

    @abstractmethod
    def delete(self,id:UUID) -> None:
        """Delete game"""
        raise NotImplementedError
    
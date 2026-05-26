from abc import ABC, abstractmethod
from uuid import UUID
from .entities import Character
from typing import Optional

class ICharacterRepository(ABC):

    @abstractmethod
    def get_all(self)->list[Character]:
        """Get all characters"""
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self,id:UUID)->Optional[Character]:
        """Get character by id"""
        raise NotImplementedError

    @abstractmethod
    def delete(self,id:UUID)->None:
        """Delete character"""
        raise NotImplementedError
    
    @abstractmethod
    def create(self,character:Character) -> Character:
        """Create character"""
        raise NotImplementedError
    
    @abstractmethod
    def update(self,character:Character) -> Character:
        """Update character"""
        raise NotImplementedError
    

        
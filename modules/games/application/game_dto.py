from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class GameCreateDTO(BaseModel):
    name: str
    release_date: str
    description: str
    developer: str
    publisher: str
    is_spin_off: bool = False


class GameResponseDTO(BaseModel):
    name: str
    description: str
    is_spin_off: bool
    release_date: str
    id: UUID


class GameUpdateDTO(BaseModel):
    description:Optional[str]=None
    is_spin_off:Optional[bool]=None
    name:Optional[str]=None   
from pydantic import BaseModel
from uuid import UUID


class CharacterCreateDTO(BaseModel):
    name: str
    race: str
    age: int
    gender: str
    description: str
    image_url: str | None


class CharacterUpdateDTO(BaseModel):
    name: str | None
    race: str | None
    age: int | None
    gender: str | None
    description: str | None
    image_url: str | None

class CharacterResponseDTO(BaseModel):
    name: str
    race: str
    age: int
    gender: str
    description: str
    image_url: str | None
    id: UUID


class CharacterDeleteResponseDTO(BaseModel):
    id: UUID
    name: str
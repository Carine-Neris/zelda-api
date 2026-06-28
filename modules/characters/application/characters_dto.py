from pydantic import BaseModel, Field
from uuid import UUID


class CharacterCreateDTO(BaseModel):
    name: str
    race: str
    age: int
    gender: str
    description: str
    image_url: str | None
    game_ids: list[UUID] = Field(min_length=1)


class CharacterUpdateDTO(BaseModel):
    name: str | None = None
    race: str | None = None
    age: int | None = None
    gender: str | None = None
    description: str | None = None
    image_url: str | None = None
    game_ids: list[UUID] | None = None

class CharacterResponseDTO(BaseModel):
    name: str
    race: str
    age: int
    gender: str
    description: str
    image_url: str | None
    game_ids: list[UUID]
    id: UUID


class CharacterDeleteResponseDTO(BaseModel):
    id: UUID
    name: str
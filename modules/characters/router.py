from fastapi import APIRouter, Depends, HTTPException, status
from uuid import UUID

from modules.characters.application.characters_dto import (
    CharacterCreateDTO,
    CharacterResponseDTO,
    CharacterUpdateDTO,
)
from modules.characters.application.use_cases.create_character import CreateCharacterUseCase
from modules.characters.application.use_cases.delete_character import DeleteCharacterUseCase
from modules.characters.application.use_cases.get_all_character import GetAllCharacterUseCase
from modules.characters.application.use_cases.get_character_by_id import GetCharacterByIdUseCase
from modules.characters.application.use_cases.update_character import UpdateCharacterUseCase
from modules.characters.infrastructure.web.dependencies import (
    factory_create_character_use_case,
    factory_delete_character_use_case,
    factory_get_all_character_use_case,
    factory_get_character_by_id_use_case,
    factory_update_character_use_case,
)


router = APIRouter(prefix="/characters", tags=["Characters"])


def _raise_http_error_from_value_error(error: ValueError) -> None:
    detail = str(error)
    status_code = status.HTTP_404_NOT_FOUND if "not found" in detail.lower() else status.HTTP_400_BAD_REQUEST
    raise HTTPException(status_code=status_code, detail=detail)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CharacterResponseDTO)
def create_character(
    data: CharacterCreateDTO,
    use_case: CreateCharacterUseCase = Depends(factory_create_character_use_case),
):
    try:
        return use_case.execute(data)
    except ValueError as error:
        _raise_http_error_from_value_error(error)


@router.get("/", response_model=list[CharacterResponseDTO])
def get_all_characters(use_case: GetAllCharacterUseCase = Depends(factory_get_all_character_use_case)):
    return use_case.execute()


@router.get("/{id}", response_model=CharacterResponseDTO)
def get_character_by_id(
    id: UUID,
    use_case: GetCharacterByIdUseCase = Depends(factory_get_character_by_id_use_case),
):
    try:
        return use_case.execute(id)
    except ValueError as error:
        _raise_http_error_from_value_error(error)


@router.put("/{id}", response_model=CharacterResponseDTO)
def update_character(
    id: UUID,
    data: CharacterUpdateDTO,
    use_case: UpdateCharacterUseCase = Depends(factory_update_character_use_case),
):
    try:
        return use_case.execute(id, data)
    except ValueError as error:
        _raise_http_error_from_value_error(error)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_character(
    id: UUID,
    use_case: DeleteCharacterUseCase = Depends(factory_delete_character_use_case),
):
    try:
        use_case.execute(id)
    except ValueError as error:
        _raise_http_error_from_value_error(error)
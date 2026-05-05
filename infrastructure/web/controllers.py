from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from infrastructure.persistence.database import get_db
from infrastructure.persistence.repositories.sqlalchemy_game_repository import SqlAlchemyGameRepository
from application.use_cases.create_game import CreateGameUseCase
from application.use_cases.get_all_game import GetAllGameUseCase
from application.use_cases.get_game_by_id import GetGameByIdUseCase
from application.use_cases.update_game import UpdateGameUseCase
from application.use_cases.delete_game import DeleteGameUseCase
from application.dto.game_dto import GameCreateDTO, GameUpdateDTO, GameResponseDTO
from infrastructure.web.dependencies import factory_create_game_use_case

router = APIRouter(prefix="/games", tags=["Games"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_game(
    data: GameCreateDTO, 
    use_case: CreateGameUseCase = Depends(factory_create_game_use_case)):

    return use_case.execute(data)


@router.get("/", response_model=list[GameResponseDTO])
def get_all_games(db: Session = Depends(get_db)):
    repository = SqlAlchemyGameRepository(db)
    use_case = GetAllGameUseCase(repository)
    return use_case.execute()


@router.get("/{id}", response_model=GameResponseDTO)
def get_game_by_id(id: UUID, db: Session = Depends(get_db)):
    repository = SqlAlchemyGameRepository(db)
    use_case = GetGameByIdUseCase(repository)
    try:
        return use_case.execute(id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put("/{id}", response_model=GameResponseDTO)
def update_game(id: UUID, data: GameUpdateDTO, db: Session = Depends(get_db)):
    repository = SqlAlchemyGameRepository(db)
    use_case = UpdateGameUseCase(repository)
    try:
        return use_case.execute(id, data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_game(id: UUID, db: Session = Depends(get_db)):
    repository = SqlAlchemyGameRepository(db)
    use_case = DeleteGameUseCase(repository)
    try:
        use_case.execute(id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

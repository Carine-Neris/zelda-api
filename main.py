from fastapi import FastAPI
from infrastructure.web.controllers import router as game_router
from infrastructure.persistence.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(game_router)

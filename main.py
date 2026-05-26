from fastapi import FastAPI
from modules.games.router import router as game_router
from config.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(game_router)

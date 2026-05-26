from fastapi import FastAPI
from modules.games.router import router as game_router
from config.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Zelda API",
    description="API de jogos da franquia The Legend of Zelda",
    version="1.0.0",
)

app.include_router(game_router)

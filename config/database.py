from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# 1. Define o endereço do banco de dados (SQLite cria um ficheiro zelda.db)
SQLALCHEMY_DATABASE_URL = "sqlite:///./zelda.db"

# 2. Cria o motor (Engine)
# O check_same_thread é necessário apenas para o SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Cria a fábrica de sessões (SessionLocal)
# Cada pedido à API terá a sua própria sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Cria a Classe Base
# É esta que vais importar no teu GameModel
class Base(DeclarativeBase):
    pass

# Dependência para o FastAPI obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
import uuid
from infrastructure.persistence.database import Base


class GameModel(Base):
    __tablename__ = "games"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    release_date: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    developer: Mapped[str] = mapped_column(String, nullable=False)
    publisher: Mapped[str] = mapped_column(String, nullable=False)
    is_spin_off: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

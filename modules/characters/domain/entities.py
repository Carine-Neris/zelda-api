from dataclasses import field, dataclass
from uuid import UUID, uuid4


@dataclass
class Character:
    name: str
    race: str
    age: int
    gender: str
    origin: str
    description: str
    image_url: str | None
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age must be a positive number")
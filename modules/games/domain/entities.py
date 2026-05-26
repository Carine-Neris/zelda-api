from dataclasses import field,dataclass
from uuid import UUID, uuid4


@dataclass
class Game:
    name: str
    release_date: str
    description: str
    developer: str
    publisher: str
    is_spin_off: bool
    id: UUID = field(default_factory=uuid4)


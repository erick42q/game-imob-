from random import randrange
from dataclasses import dataclass, field
from .player import Player


@dataclass
class Ground:
    sale_value: int = field(init=False)
    rent_value: int = field(init=False)
    owner: Player = None

    def __post_init__(self):
        self.sale_value = randrange(50, 300)
        self.rent_value = int(self.sale_value * 0.2)

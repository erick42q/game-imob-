from random import  randrange
from dataclasses import dataclass, field
from .player import Player

@dataclass
class Propriedade:
    valor_venda: int = field(init=False)
    valor_aluguel: int = field(init=False)
    owner: Player = None

    def __post_init__(self):
        self.valor_venda = randrange(50,300)
        self.valor_aluguel = int(self.valor_venda*0.2)
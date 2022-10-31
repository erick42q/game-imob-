from dataclasses import dataclass
from .tools import vprint

@dataclass
class Player:
    id: int
    tipo: str
    place: int = 0
    balance: int = 100

    def andar_casas(self, dado):
        
        if self.place+dado <= 19:
            self.place += dado
        else:
            self.place -= 20
            self.balance += 100
            self.place += dado

    def pagar(self, valor):
        self.balance = round(self.balance - valor, 2)

    def prop_owned(self, grounds: list):
        props = []
        for count, prop in enumerate(grounds):
            if prop.owner == self:
                props.append(count)
        
        return props

    def buy_prop(self, propriedade: dataclass):
        self.pagar(propriedade.sale_value)
        propriedade.owner = self
        vprint(f"            ## player {self.tipo} comprou a propriedade")    
        


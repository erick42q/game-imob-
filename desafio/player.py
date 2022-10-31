from dataclasses import dataclass


@dataclass
class Player:
    id: int
    tipo: str
    casa_atual: int = 0
    saldo: int = 100

    def andar_casas(self, dado):
        
        if self.casa_atual+dado <= 19:
            self.casa_atual += dado
        else:
            self.casa_atual -= 20
            self.saldo += 100
            self.casa_atual += dado

    def pagar(self, valor):
        self.saldo = round(self.saldo - valor, 2)

    def prop_owned(self, propriedades: list):
        props = []
        for count, prop in enumerate(propriedades):
            if prop.owner == self:
                props.append(count)
        
        return props

    def buy_prop(self, propriedade: dataclass):
        self.pagar(propriedade.valor_venda)
        propriedade.owner = self
        print(f"            ## player {self.tipo} comprou a propriedade")    
        


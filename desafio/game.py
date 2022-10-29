from random import  randint
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
            print("Volta no tabuleiro!!!")
            self.casa_atual -= 19
            self.saldo += 100
            self.casa_atual += dado

    def pagar(self, valor):
        self.saldo -= valor
        

@dataclass
class Propriedade:
    dono: int = None
    valor_venda: float = 200
    valor_aluguel: float = 20

        
class Match:

    def roll_dice(self, player:dataclass):
        steps = randint(0, 6)
        casa_anterior = player.casa_atual
        player.andar_casas(steps)
        print(
            f'''{player.tipo}: 
            dado: {steps} 
            casa anterior:  {casa_anterior}
            casa atual: {player.casa_atual}
            
            saldo: {Player.saldo}'''
        )

    def transaction(self, player:dataclass, propriedade:dataclass):
        
        if propriedade.dono and propriedade.dono != player.id:
            player.pagar(propriedade.valor_aluguel)
            return

        if player.saldo >= propriedade.valor_venda:
            player.pagar(propriedade.valor_venda)
            propriedade.dono = player.id
            print(propriedade)


        






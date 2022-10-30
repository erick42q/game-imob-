from os import remove
from random import  randint, randrange
from dataclasses import dataclass, field


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
            return "Volta no tabuleiro!!!"

    def pagar(self, valor):
        self.saldo -= valor

    def prop_owned(self, propriedades: list):
        props = []
        for count, prop in enumerate(propriedades):
            if prop.owner == self:
                props.append(count)
        
        return props

        

@dataclass
class Propriedade:
    valor_venda: int = field(init=False)
    valor_aluguel: float = field(init=False)
    owner: Player = None

    def __post_init__(self):
        self.valor_venda = int(randrange(50,300))
        self.valor_aluguel = self.valor_venda*0.2


@dataclass    
class Match:
    
    players: list[Player]


    def roll_dice(self):
        steps = randint(1, 6)
        return steps


    def transaction(self, player:dataclass, propriedade:dataclass):
        if propriedade.owner and propriedade.owner != player:
            player.pagar(propriedade.valor_aluguel)
            return
        if player.saldo >= propriedade.valor_venda:
            player.pagar(propriedade.valor_venda)
            propriedade.owner = player
            print(f"player {player.tipo} comprou a propriedade")    
        
        print(propriedade)

    def game_over(self, player:dataclass):
        if player.saldo <= 0:
            self.players.remove(player)
            print(f"player {player.tipo} não tem mais recursos e está fora do jogo")

    def winner(self):
        if len(self.players) == 1:
            return True
        return False

    def show_players(self):
        msg = ''
        for player in self.players:
            msg += f'''
                jogador: {player.tipo}
                saldo: {player.saldo}            
                '''
        return msg

    def victory_announce(self, winner:Player, propriedades: list[Propriedade]):
        print(f"------------------")
        print(f"O GANHADOR É O {winner.tipo}")
        print(f'''
            saldo: {winner.saldo}
            total de propriedades: {winner.prop_owned(propriedades)}
            ''')



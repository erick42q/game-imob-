from .player import  Player
from .ground import  Propriedade
from dataclasses import dataclass
from random import  randint, getrandbits


@dataclass    
class Match:
    
    players: list[Player]
    winner: Player = None

    def roll_dice(self):
        steps = randint(1, 6)
        return steps


    def transaction(self, player:dataclass, propriedade:dataclass):
        if propriedade.owner and propriedade.owner != player:
            player.pagar(propriedade.valor_aluguel)
            return
        
        if player.saldo >= propriedade.valor_venda:
            if player.tipo == 'inpulsivo':
                player.buy_prop(propriedade)

            elif player.tipo == 'exigente' and propriedade.valor_aluguel > 50:
                player.buy_prop(propriedade)
                
            elif player.tipo == 'cauteloso' and (player.saldo - propriedade.valor_venda) >= 80 :
                player.buy_prop(propriedade)

            elif player.tipo == 'aleatório':
                if bool(getrandbits(1)):
                    player.buy_prop(propriedade)

                else:
                    print(f"{player.tipo} não quis comprar a propriedade")



    def game_over(self, player:dataclass):
        if player.saldo <= 0:
            self.players.remove(player)
            print(f"O jogador {player.tipo} não tem mais recursos e está fora da partida\n")

    def has_winner(self):
        if len(self.players) == 1:
            self.winner = self.players[0]
            return True
        return False

    def show_players(self):
        msg = ''
        print("Começando o game:\n")
        for player in self.players:
            msg += f"    jogador: {player.tipo}\n    saldo: {player.saldo}\n\n"
        return msg

    def victory_announce(self, winner:Player, propriedades: list[Propriedade]):
        print("====================================================")
        print("TEMOS UM VENCEDOR \o/")
        print(f'{winner.tipo}:')
        print(f'''
            saldo: {winner.saldo}
            total de propriedades: {winner.prop_owned(propriedades)}
            ''')

    def timeout(self):    

        for player in self.players:
            if not self.winner:
                self.winner = player
            if self.winner.saldo < player.saldo:
                self.winner = player


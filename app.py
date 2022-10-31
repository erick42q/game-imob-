import math
import random
from cmath import polar

from desafio.game import Player, Match, Propriedade

# criar propriedades
propriedades = []

for index in range(20):
    propriedades.append(Propriedade())

# criar jogadores
players = [
    Player(0, "inpulsivo"),
    Player(1, "exigente"),
    Player(2, "cauteloso"),
    Player(3, "aleatório"),
]

random.shuffle(players)

match = Match([ player for player in players])

print(match.show_players())


for id_round in range(100):
    print(f"-----------------")
    print(f"round: {id_round}")


    for player in match.players:
        propriedade = propriedades[player.casa_atual]

        steps = match.roll_dice()
        print(f"----------------------------------------------------")

        print(
            f'''\n{player.tipo}: \nid: {player.id} 
            dado: {steps}
             
            casa:  {player.casa_atual}
            saldo: {player.saldo}
            propriedades: {player.prop_owned(propriedades)}
            ''')

        msg=player.andar_casas(steps)
        match.transaction(player, propriedade)

        print(f'''            se movel para a casa: {player.casa_atual}
            valor: {propriedade.valor_venda}
            aluguel: {propriedade.valor_aluguel}
            proprietário: {propriedade.owner.tipo if propriedade.owner else 'sem proprietário'}''')
        
        print(f'''
            saldo: {player.saldo}
            propriedades: {player.prop_owned(propriedades)}
            '''
        )

        match.game_over(player)
        if match.winner():
            break

    if match.winner():
        winner = match.players[0]
        match.victory_announce(winner, propriedades)

        break

# radomisa ordem dos players
# for player in players:
#     round(player)





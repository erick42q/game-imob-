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

        casa_anterior = player.casa_atual

        msg=player.andar_casas(steps)
        print(
            f'''{player.tipo} id: {player.id}: 
            dado: {steps} 
            casa anterior:  {casa_anterior}
            {msg if msg is not None else ''}
            casa atual: {player.casa_atual}
            propriedades: {player.prop_owned(propriedades)}
            saldo: {player.saldo}
            '''
        )

        match.transaction(player, propriedade)
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





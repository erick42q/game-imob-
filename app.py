import random
from cmath import polar

from desafio.game import Player, Propriedade, Match

match = Match()

# criar jogadores
players = [
    Player(0, "inpulsivo"),
    Player(1, "exigente"),
    Player(2, "cauteloso"),
    Player(3, "aleatório"),
]
random.shuffle(players)


# criar propriedades
propriedades = []

for index in range(20):
    propriedades.append(Propriedade())


for id_round in range(50):
    print(f"-----------------")
    print(f"round: {id_round}")

    player = players[0]
    propriedade = propriedades[player.casa_atual]

    match.roll_dice(player)
    match.transaction(player, propriedade)

    # print(player)
    # print(propriedade)


# radomisa ordem dos players
# for player in players:
#     round(player)





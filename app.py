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


for id_round in range(10):
    print(f"-----------------")
    print(f"round: {id_round}")


    for player in match.players:
        
        propriedade = propriedades[player.casa_atual]

        match.roll_dice(player)
        match.transaction(player, propriedade)
        player.pagar(30)
        match.game_over(player)
        if match.winner():
            break

    if match.winner():
        winner = match.players[0]
        print(f"------------------")
        print(f"O GANHADOR É O {winner.tipo}")
        print(f'''
            saldo: {winner.saldo}
            total de propriedades: {[count for count, prop in enumerate(propriedades) if prop.owner == winner]}
            ''')



        break

# radomisa ordem dos players
# for player in players:
#     round(player)





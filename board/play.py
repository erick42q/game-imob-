from random import shuffle

from .player import Player
from .match import Match
from .ground import Ground

def play(rounds=1000):

# criar propriedades
    grounds = []

    for index in range(20):
        grounds.append(Ground())

    # criar jogadores
    players = [
        Player(0, "inpulsivo"),
        Player(1, "exigente"),
        Player(2, "cauteloso"),
        Player(3, "aleatório"),
    ]

    shuffle(players)

    match = Match([ player for player in players])

    print(match.show_players())

    for round in range(rounds):
        print(f"-----------------")
        print(f"round: {round}")


        for player in match.players:
            propriedade = grounds[player.place]

            steps = match.roll_dice()
            print(f"----------------------------------------------------")

            print(
                f'''\n{player.tipo}: \nid: {player.id} 
                dado: {steps}
                
                casa:  {player.place}
                saldo: {player.balance}
                propriedades: {player.prop_owned(grounds)}
                ''')

            msg=player.andar_casas(steps)
            match.transaction(player, propriedade)

            print(f'''            se movel para a casa: {player.place}
                valor: {propriedade.sale_value}
                aluguel: {propriedade.rent_value}
                proprietário: {propriedade.owner.tipo if propriedade.owner else 'sem proprietário'}''')
            
            print(f'''
                saldo: {player.balance}
                propriedades: {player.prop_owned(grounds)}
                '''
            )

            match.game_over(player)

            if match.has_winner():
                break

        match.rounds = round + 1

        if match.has_winner():
            break

    if not match.has_winner():
        match.timeout()
        match.victory_announce(match.winner, grounds)
        print(f"timeout = {match._timeout}\n")
    else:
        match.victory_announce(match.winner, grounds)

    return {
            "timeout": match._timeout,
            "rounds": match.rounds,
            "comportamento": match.winner.tipo
        }

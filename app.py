from board.play import play
from board.tools import winner
import statistics

def main():
    timeout = 0
    rounds = []
    comportamentos = {
    }
    percents = {

    }

    for index in range(300):
        hist = play(1000)

        if hist['timeout']:
            timeout += 1    

        rounds.append(hist['rounds'])

        if hist['comportamento'] not in comportamentos:
            comportamentos[hist['comportamento']] = 1    
        else:
            comportamentos[hist['comportamento']] += 1

    total = sum(comportamentos.values())

    for key, value in comportamentos.items():
        percents[key] = "{:.2f}%".format(value*100/total)



    print(f"total de timeouts: {timeout}")
    print(f"media de rounds: {round(statistics.fmean(rounds))}")
    print(f"porcentagem de vitorias: {percents}")
    print(f"comportamento que mais vence: {winner(comportamentos)[0]}")


if __name__ == "__main__":
    main()
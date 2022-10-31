from board.play import play
from board.tools import winner
import statistics

def main():
    timeout = 0
    rounds = []
    comportamentos = {
    }

    for index in range(50):
        hist = play(100)

        if hist['timeout']:
            timeout += 1    

        rounds.append(hist['rounds'])

        if hist['comportamento'] not in comportamentos:
            comportamentos[hist['comportamento']] = 0    
        else:
            comportamentos[hist['comportamento']] += 1


    print(timeout)
    print(statistics.fmean(rounds))
    print(comportamentos)
    print(winner(comportamentos)[0])


if __name__ == "__main__":
    main()
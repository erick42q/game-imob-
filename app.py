from board.play import play
from board.tools import winner
import statistics
import argparse
import config


parser = argparse.ArgumentParser(prog='Bord')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()


def main():

    print(f'Olá, o game está rolando 😁')
    print(
        f'Caso queira ter uma visão de tudo o que está acontecendo, basta rodar o comando com o -v ou --verbose\n'
    )

    config.verbose = args.verbose

    timeout = 0
    rounds = []
    comportamentos = {}
    percents = {}

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
        percents[key] = '{:.2f}%'.format(value * 100 / total)

    print(f'Total de timeouts: {timeout}')
    print(f'Media de rounds: {round(statistics.fmean(rounds))}')
    print(f'Porcentagem de vitorias: {percents}')
    print(f'Comportamento que mais vence: {winner(comportamentos)[0]}\n')


if __name__ == '__main__':
    main()

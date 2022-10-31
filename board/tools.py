
def winner(comportamentos):
    ganhador = ('', 0)
    for key, value in comportamentos.items():
        if not ganhador:
            ganhador = (key, value)
        if ganhador[1] < value:
            ganhador = (key, value)

    return ganhador

from desafio.game import Player, Propriedade, Match

propriedades = []

for index in range(20):
    propriedades.append(Propriedade())


def test_criação_de_player():
    p = Player(0, "inpulsivo")

    assert p.id == 0

def test_mover_casas():
    p = Player(0, "inpulsivo")
    p.andar_casas(5)

    assert p.casa_atual == 5

def test_volta_tabuleiro():
    p = Player(0, "inpulsivo")
    p.casa_atual = 0
    p.andar_casas(20)

    assert p.casa_atual == 0

def test_volta_tabuleiro_add_bonus():
    p = Player(0, "inpulsivo")
    p.casa_atual = 0
    p.andar_casas(20)

    assert p.saldo == 200

def test_rodar_dados():
    p = Player(0, "inpulsivo")

    match = Match([ p ])

    dado = match.roll_dice()
    
    assert dado <= 6 and dado >= 1


def test_comprar_propriedade():
    # criar propriedades
    propriedades = []

    for index in range(20):
        propriedades.append(Propriedade())
        

    p = Player(0, "inpulsivo")
    p.saldo = 1000

    match = Match([ p ])

    match.transaction(p, propriedades[0])
    match.transaction(p, propriedades[3])
    match.transaction(p, propriedades[4])


    assert propriedades[0].owner == p


def test_testar_total_de_propriedades_compradas():
    # criar propriedades
    propriedades = []

    for index in range(20):
        propriedades.append(Propriedade())
        

    p = Player(0, "inpulsivo")
    p.saldo = 5000

    match = Match([ p ])

    match.transaction(p, propriedades[0])
    match.transaction(p, propriedades[3])
    match.transaction(p, propriedades[4])
    match.transaction(p, propriedades[15])



    assert p.prop_owned(propriedades) == [0, 3, 4, 15]


def test_inpulsivo_compras():
    player = Player(0, "inpulsivo")
    player.saldo = 300
    prop1 = Propriedade()

    match = Match([ player ])

    match.transaction(player, prop1)

    assert prop1.owner == player

def test_exigente_nao_compra_aluguel_49():
    player = Player(0, "exigente")
    player.saldo = 300
    prop1 = Propriedade()
    prop1.valor_venda = 250
    prop1.valor_aluguel = 45

    match = Match([ player ])

    match.transaction(player, prop1)

    assert prop1.owner == None


def test_exigente_nao_compra_aluguel_51():
    player = Player(0, "exigente")
    player.saldo = 300
    prop1 = Propriedade()
    prop1.valor_venda = 250
    prop1.valor_aluguel = 51

    match = Match([ player ])

    match.transaction(player, prop1)

    assert prop1.owner == player


def test_cauteloso_compra():
    player = Player(0, "cauteloso")
    player.saldo = 280
    prop1 = Propriedade()
    prop1.valor_venda = 200

    match = Match([ player ])

    match.transaction(player, prop1)

    assert prop1.owner == player

def test_cauteloso_nao_compra():
    player = Player(0, "cauteloso")
    player.saldo = 280
    prop1 = Propriedade()
    prop1.valor_venda = 201

    match = Match([ player ])

    match.transaction(player, prop1)

    assert prop1.owner == None
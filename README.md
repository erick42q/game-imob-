python 3.10

Sobre o game:

Jogo semelhante a Banco Imobiliário quer roda de forma automática, com a 
finalidade de retornar alguns dados para análise de estratégia no game. 


### Instalar e ativar o virtualenv:
```
python3.10 -m venv venv

source ./venv/bin/activate
```

### Instalar dependências:
```
pip install -r requirements.txt
```

### Rodar projeto:
```
python app.py
```

### Rodar o comando com <code>-v</code> ou <code>--verbose</code> para receber logs dos players, rounds e partidas.

```
 $ python app.py -v
```

Assim que começar a rodar, serão criado 4 players, cada player inicia com $100 e terá uma condição para decidir se compra uma propriedades(falarei mais sobre as condições abaixo). Cada propriedade do tabuleiro tem um valor de compra e um valor de aluguel que é definido no inicio da partida, o valor de compra de cada propriedade é aleatório entre $50 e $300 e o valor do aluguel é 20% do valor da propriedade.

Vence quem tiver mais saldo ao longo de 1000 rounds ou quem for o único restante com saldo ao longo da partida.

Por fim é feito uma análise rodando o jogo 300 partidas (1000 rounds em casa) para retornar o total de partidas que termina em timeout, a media do total de rounds em uma partida, a porcentagem de vitorias por condição do jogador e o comportamento do jogador que mais vence.

    
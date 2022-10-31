python 3.10

Game:

    Jogo semelhante a Banco Imobiliário quer roda de forma automática, com a 
finalidade de retornar alguns tados para analise de estrategia no game. 


###Instalar e ativar o virtualenv:
```
python3.10 -m venv venv

source ./venv/bin/activate
```

###instalar dependências:
````
pip install -r requirements.txt
```

###rodar projeto:
```
python app.py
```

###rodar o comando com <code>-v<code>> ou <code>--verbose<code> para receber logs dos players, rounds e partidas.
``````

    Assim que começar a rodar, será criado 4 players, cada player inicia com $100 e tem uma 
condição para decidir se compra uma propriedades(falarei mais sobre as condições abaixo) cada 
propriedade do tabuleiro tem um valor de compra e um valor de alugel que é definido no incio 
da partida, o valor de compra de cada propriedade é aleatório entre $50 e $300, e o valor do 
aluguél é 20% do valor da propriedade. 

    Vence quem tiver mais saldo ao longo de 1000 rounds ou quem for o único restante com saldo 
ao longo partida

    Por fim é feito uma analize rodando o jogo 300 vezes para retornar o total de rounds que 
termina em timeout, a media do total de rounds em uma partida, a porcentagem de vitorias por
condição do jogador e o comportamento de jogador que mais vence.
    
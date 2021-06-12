from random import randint as r

jogador = str(input('Você gostaria de jogar o dado? [S/N]:')).upper()
if jogador == 'S':
    aleatorio = r(1, 6)
    print('(jogou o dado)')
    print('O dado caiu com o número ', aleatorio)
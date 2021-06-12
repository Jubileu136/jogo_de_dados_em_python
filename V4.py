#VERSÃO FINAL
from random import randint as r
from time import sleep as s

jogador = str(input('Você gostaria de jogar o dado? [S/N]:')).upper()
if jogador == 'S':
    aleatorio = r(1, 6)
    tempo = r(3, 6)
    s(1)
    print('(jogou o dado)')
    s(tempo)
    print('O dado caiu com o número ', aleatorio)
    carrega = True
    while carrega:
        s(1)
        de_novo = str(input('Quer jogar o dado novamente? [S/N]:')).upper()
        if de_novo == 'S':
            aleatorio = r(1, 6)
            tempo = r(1, 6)
            s(1)
            print('(jogou o dado novamente)')
            s(tempo)
            print('O dado caiu com o número {} desta vez'.format(aleatorio))
        elif de_novo == 'N':
            s(1)
            print('OK')
            break
elif jogador == 'N':
    print('OK')
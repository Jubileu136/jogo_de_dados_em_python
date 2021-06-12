from random import randint as r

jogador = str(input('Você gostaria de jogar o dado? [S/N]:')).upper()
if jogador == 'S':
    aleatorio = r(1, 6)
    print('(jogou o dado)')
    print('O dado caiu com o número ', aleatorio)
    carrega = True
    while carrega:
        de_novo = str(input('Quer jogar o dado novamente? [S/N]:')).upper()
        if de_novo == 'S':
            aleatorio = r(1, 6)
            print('O dado caiu com o número {} desta vez'.format(aleatorio))
        elif de_novo == 'N':
            print('OK')
            break
elif jogador == 'N':
    print('OK')
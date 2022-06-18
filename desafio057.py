from time import sleep
from random import randint
computador = randint(0, 10)
tentativa = 1
print('SOU SEU COMPUTADOR \nVamos jogar?')
sleep(2)
print('...')
sleep(2)
jogador = int(input('estou pensando em um numero entre 0 e 10, tente adivinhar: '))
while jogador != computador:
    tentativa +=1
    if jogador < computador:
        jogador = int(input('MAIS. tente novamente: '))
    else:
        jogador = int(input('MENOS. tente novamente: '))
print('ACERTOU!!!')
print('total de tentativas: {}'.format(tentativa))
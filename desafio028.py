from random import randint
computador = randint(0,5)
print('-=-' *20)
print('estou pensando em um numero entre 0 e 5, consegue adivinhar')
jogador = int(input('resposta: '))
if jogador == computador:
    print('parabens, voce venceu')
else:
    print('vcoe perdeu, o numero que eu estava pensando era: {}'.format(computador))
print('-=-'*20)


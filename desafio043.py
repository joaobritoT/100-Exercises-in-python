from random import randint
from time import sleep
print('-=' *20)
print('            JOGO DO JOKENPO           ')
print('-='*20)
print('escolha suas opcoes : \n [0] pedra \n [1] papel \n [2] tesoura')
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
jogador = int(input(':'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
if jogador == 0 and computador == 0:
    print('empate, eu escolhi {}'.format(itens[computador]))
elif jogador == 1 and computador == 1:
    print('empate, eu escolhi {}'.format(itens[computador]))
elif jogador == 2 and computador == 2:
    print('empate, eu escolhi {}'.format(itens[computador]))
elif jogador == 0 and computador == 2:
    print('VOCE ganhou, eu escolhi {}'.format(itens[computador]))
elif jogador == 1 and computador == 0:
    print('VOCE ganhou, eu escolhi {}'.format(itens[computador]))
elif jogador == 2 and computador == 1:
    print('VOCE ganhou, eu escolhi {}'.format(itens[computador]))
elif jogador == 0 and computador == 1:
    print('COMPUTADOR WINS, escolhi {}'.format(itens[computador]))
elif jogador == 1 and computador == 2:
    print('COMPUTADOR WINS, escolhi {}'.format(itens[computador]))
elif jogador == 2 and computador == 0:
    print('COMPUTADOR WINS, escolhi {}'.format(itens[computador]))


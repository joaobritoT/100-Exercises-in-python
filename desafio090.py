from random import randint
from operator import itemgetter
import re
from time import sleep
segundo = 0

jogadores = {'jogador 1': randint(1,6),
            'jogador 2':randint(1,6),
            'jogador 3':randint(1,6),
            'jogador 4':randint(1,6)}
ranking= []

print("valors sorteados: ")

for k,v in jogadores.items():
    print("jogador {} tirou {}".format(k,v))
    sleep(1)

ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True)

for i,v in enumerate(ranking):
    print("{} {}".format(i+1,v))





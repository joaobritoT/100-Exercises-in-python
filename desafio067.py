
from random import randint
from time import sleep
resultado = 'teste'
cont = 0
while True:
    print("-="*15)
    print("VAMOS JOGAR PAR OU IMPAR")
    print('-='*15)
    jogador = int(input("Digite um valor: "))
    pi = str(input("Par ou impar? [p/i]? ")).lower().strip()[0]
    while pi not in "PpIi":
        pi = str(input("Par ou impar? [p/i]? "))
    computador = randint(0,10)
    print("computador escolheu {}".format(computador))
    soma = jogador + computador
    print('a soma dos numeros deu {}'.format(soma))
    if soma %2 == 0:
        print("caiu par")
    else:
        print("deu impar")

    if pi in 'Ii':
        resultadojogador = 'impar'
    elif pi in 'Pp':
        resultadojogador = 'par'

    if resultadojogador == 'impar' and soma %2 == 0:
        print("perdeu")
    elif resultadojogador == 'impar' and soma %2 != 0:
        print("ganhou")
        resultado = 'ganhou'
    elif resultadojogador == 'par' and soma %2 == 0:
        print("ganhou")
        resultado = 'ganhou'
    elif resultadojogador == 'par' and soma %2 != 0:
        print("perdeu")
    cont+=1
    sleep(1)
    if resultado == 'ganhou':
        break
print("ganhou com {} tentativas".format(cont))
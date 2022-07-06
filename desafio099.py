from random import randint
lista = []
soma =0

def sorteador():
    print("sorteando os numeros da lista: ",end=' ')
    for c in range(0,5):
        numero = randint(0,5)
        lista.append(numero)
        print(numero,end=' ')

def par():
    soma = 0
    for valor in lista:
        if valor % 2  == 0:
            soma += valor
    print()
    print("a soma dos valores pares da lista deu {}".format(soma))



sorteador()
par()

        
        


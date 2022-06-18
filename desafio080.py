lista = []
cont = 1

while True:
    valor = int(input("digite um valor: "))
    if valor not in lista:
        lista.append(valor)
    else:
        print("valor ja cadastrado")
    resp = str(input("desja continuar? s/n: ")).lower()[0]
    if resp == 'n':
        break
    cont+=1

print("-=-"*20)
print("voce digitou {} elementos".format(cont))
lista.sort(reverse=True)
print("os valores em ordem decresente sao: {}".format(lista))
if 5 in lista:
    print("o valor 5 faz parte da lista")
else:
    print("o valor 5 nao faz parte da lista")
    

lista = []
impares = []
pares = []

while True:
    valor = int(input("digite um valor: "))
    lista.append(valor)
    if valor % 2 ==0 :
        pares.append(valor)
    else:
        impares.append(valor)
    resp = str(input("dejesa continuar? s/n: ")).lower()[0]
    if resp == 'n':
        break
print("lista completa: {}".format(lista))
print("lista de pares: {}".format(pares))
print("lista de impares: {}".format(impares))
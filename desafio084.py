print("cadastro de numeros")
print("-=-"*20)
num = [[],[]]

for c in range(0,7):
    valor = int(input("digite o {} valor: ".format(c+1)))
    if valor %2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print("numeros pares: {}".format(num[0]))
print("numeros impares: {}".format(num[1]))
print("lista completa: {}".format(num))

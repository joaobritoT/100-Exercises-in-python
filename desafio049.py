soma =  0
cont = 0 
for c in range (1, 7):
    num = int(input("digite {} valor: ".format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont +1
print(" voce digitou {} numeros pares e a soma desses numeros da {}".format(cont, soma))

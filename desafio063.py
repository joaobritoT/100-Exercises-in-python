n = 0
cont = 0
soma = 0


while n != 999:
    n = int(input("DIGITE 999 para parar: "))
    soma = soma + n
    cont +=1
print("voce digitou {} numeros e a soma deles deu {}".format(cont,soma - 999))
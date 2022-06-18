soma = 0 
cont = 0
while True:
    n = int(input("digite um numero inteiro (999 para parar): "))
    cont+=1
    if n == 999:
        break
    soma +=n
print("a soma dos {} numeros digitados valem: {} ".format(cont,soma))

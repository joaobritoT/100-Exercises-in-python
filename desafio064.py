resp = 's'
media = 0
qnt = 0
soma = 0
maior = 0
menor = 0
while resp in 'Ss':
    n = int(input("digite um numero: "))
    resp = str(input("deseja continuar? [s/n]")).upper().strip()[0]
    soma = soma + n
    qnt +=1
    if qnt == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
media = soma / qnt
print("vc digitou {} numeros e a media entre esses numeros eh de {:.2f}".format(qnt,media))
print("maior: {}, menor: {}".format(maior,menor))




    
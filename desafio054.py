maior = 0
menor = 0
for c in range (1,6):
    peso = float(input('qual o peso da {} pessoas: '.format(c)))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso lido foi {}'.format(maior))
print('o menor peso lido foi {}'.format(menor))



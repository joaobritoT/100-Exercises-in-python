cont = 0
num = (int(input('digite um numero: ')),
int(input('digite outro numero: ')),
int(input('digite outro numero: ')),
int(input('digite outro numero: ')))
print("o numero 9 apareceu {} vezes".format(num.count(9)))
print("o valor 3 aparecu {} na posicao".format(num.index(3)))
for n in num:
    if n %2 ==0:
        cont+=1
print('foram digitados {} numeros pares'.format(cont))

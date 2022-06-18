num = int(input('digite um numero: '))
tot = 0
for c in range (1, num +1):
    print('{}'.format(c), end= ' ')
    if num %c ==0:
        tot +=1 
print("\no numero foi dividido {} vezes".format(tot))

if tot == 2:
    print('o numero eh primo')
else:
    print('o numero nao eh primo')


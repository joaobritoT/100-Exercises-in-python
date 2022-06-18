a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))

if a<b and a<c:
    menor = a 
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c 
if a>b and a>c:
    maior = a 
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c 
print('o menor numero eh o: {}'.format(menor))
print('o maior numero eh o: {}'.format(maior))
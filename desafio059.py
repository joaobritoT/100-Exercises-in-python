from math import factorial
n = int(input('digite um numero para calcular o fatorial: '))
c = n
while c > 0:
   print('{}'.format(c), end=' ')
   print('x' if c > 1 else '=', end=' ')
   c-=1
print('{}'.format(factorial(n)), end=' ')
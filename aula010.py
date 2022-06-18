n1 = float(input('digite a nota 1: '))
n2 = float(input('digite a nota 2: '))
m = (n1 + n2) / 2
print('a sua media foi de {}'.format(m))
if m >= 6:
    print('voce passou de ano, parabens!')
else:
    print('voce reprovou de ano, estude mais da proxima vez!')
    
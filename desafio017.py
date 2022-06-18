import math
co = float(input('qual o valor do cateto oposto?: '))
ca = float(input('qual o valor do cateto adjacente?: '))
h = co **2 + ca **2
print('o valor da hipotenusa eh de {:.2f} '.format(math.sqrt(h)))
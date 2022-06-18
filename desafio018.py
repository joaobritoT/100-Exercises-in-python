import math
an = float(input('digite um anguilo qualquer: '))
s = math.sin(math.radians(an))
c = math.cos(math.radians(an))
t = math.tan(math.radians(an))
print('SENO = {:.2f}'.format(s))
print('COSSENO = {:.2f}'.format(c))
print('TANGENTE = {:.2f}'.format(t))
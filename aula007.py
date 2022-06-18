n1 = int(input('um valor: '))
n2= int(input('outro valor: '))
s = n1 + n2 
su = n1 - n2 
m = n1 * n2 
d = n1 / n2 
di = n1 // n2 
e = n1 ** n2
print('a soma vale {}, a subtracao vale {}, \n a multiplicacao vale {} e a divisao vale {:.2f} '.format(s, su, m, d ))
print('a divisao inteira vale {} e a potenciacao vale {}'.format(di, e))
cont = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
'onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoioto','dezenove','vinte')

while True:
    num = int(input("digite um numero entre 0 e 20: "))
    if num <=0 and num >=20:
        break
    print("tente novamente")
print('voce digitou o numero {}'.format(cont[num]))


distancia = float(input('qual foi a distancia da sua viagem em KM? '))
preco1 = (distancia * 0.50)
preco2 = (distancia * 0.45)
if distancia <= 200:
    print('o valor da sua viagem foi de R${}'.format(preco1))
else:
    print('o valor da su viagem foi de R${}'.format(preco2))
v = float(input('qual a velocidade atual do carro? '))
multa = (v - 80)*7
if v >=80:
    print('Voce exedeu o limite de velocidade e sera multado, o valor de multa sera de {}' .format(multa))
else:
    print('Prossiga, tenha um bom dia e diriga com cuidado!!')

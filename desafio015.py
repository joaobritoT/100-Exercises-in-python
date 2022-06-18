dias = int(input('voce alugou o carro por quantos dias?'))
km = float(input('quantos kms vc rodou com o carro? '))
pagar = (60 * dias) + (km * 0.15)
print('o total a pagar sera o valor de R${:.2f}'.format(pagar))
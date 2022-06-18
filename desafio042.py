preco = float(input('qual o valor da compra? :'))
print('como gostaria de pagar? [1] A VISTA [2] A VISTA NO CARTAO [3] ATE 2X NO CARTAO [4] 3X OU MAIS NO CARTAO')
forma = int(input(':'))
if forma == 1:
    d = preco - (0.10 * preco)
    print('o valor da compra sera de {}'.format(d))
elif forma == 2:
    d = preco - (0.05 * preco)
    print('o valor da compra sera de {}'.format(d))
elif forma == 3:
    print('o valor da compra sera de {}'.format(preco))
elif forma == 4:
    d = preco + (0.20 * preco)
    print('o valor da compra sera de {}'.format(d))
else:
    print('OPCAO INVALIDA')
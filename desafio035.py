casa = float(input('qual o valor da casa? R$:'))
salario = float(input('qual o seu salario? R$:'))
anos = int(input('em quantos anos vc quer pagar a casa?: '))
prest = casa / anos / 12
limite = 0.30 * salario
print('o valor das parcelas ficarao R${:.2f} durante {} anos'.format(prest, anos))
if limite <= prest:
    print('Emprestimo Negado!')
else:
    print('emprestimo concedido com sucesso!')

salario = float(input('qual o salario do funcionario? R$: '))
if salario <= 1200:
    novo = salario + (0.15 * salario)
else: novo = salario + (0.10 * salario)
print('o trabalhador passara a receber: {}'.format(novo))
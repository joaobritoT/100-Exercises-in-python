s = float(input('qual eh o salario do funcionario? '))
reajuste = 0.15 * s 
sr = reajuste + s 
print('o salario de {}, com um reajuste de 15% passou a valer {:.2f}'.format(s, sr))
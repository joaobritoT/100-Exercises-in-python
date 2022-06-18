nome = str(input('digite seu nome: ')).strip()
print('seu nome em maiusculo fica: {}'.format(nome.upper()))
print('seu nome em minusculo fica: {}'.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))



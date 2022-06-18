n = str(input('digite seu nome completo: ')).strip
nome = n.split()
print('seu primeiro nome eh: {}'.format(nome[0]))
print('seu ultimo nome eh: {}'.format(nome[len(nome) - 1]))
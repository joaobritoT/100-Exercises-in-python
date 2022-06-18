sexo = str(input('Escolha seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('opcao invalida tente novamente: ')).strip().upper()[0]
print('validacao concluida')
print('sexo {} cadastrado com sucesso'.format(sexo))

nome = str(input('qual eh o seu nome? '))
if nome == 'joao':
    print('que nome lindo, tenha um otimo dia ')
elif nome == 'maria' or nome == 'pedro':
    print('seu nome eh bem comum, tenha um bom dia')
else:
    print('seu nome nao tem nada de especial')
    print('tenha um bom dia {}'.format(nome))

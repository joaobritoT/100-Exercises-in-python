from datetime import date
ano = int(input('qual sua data de nascimento?: '))
idade = date.today().year - ano
if idade <= 9:
    c = 'mirim'
    print('o atleta tem {} anos \n CLASSIFICACAO: {}'.format(idade, c))
elif idade <= 14:
    c = 'infantil'
    print('o atleta tem {} anos \n CLASSIFICACAO: {}'.format(idade, c))
elif idade <= 19:
    c = 'junior'
    print('o atleta tem {} anos \n CLASSIFICACAO: {}'.format(idade, c))
elif idade <= 25:
    c = 'senior'
    print('o atleta tem {} anos \n CLASSIFICACAO: {}'.format(idade, c))
elif idade > 25:
    c = 'master'
    print('o atleta tem {} anos \n CLASSIFICACAO: {}'.format(idade, c))

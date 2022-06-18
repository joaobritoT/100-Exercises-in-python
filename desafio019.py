import random
p = str(input('PRIMEIRO ALUNO: '))
s = str(input('SEGUNDO ALUNO: '))
t = str(input('TERCEIRO ALUNO: '))
q = str(input('QUARTO ALUNO: '))
lista = [p, s, t, q]
escolhido = random.choice(lista)
print('o aluno escolhido foi: {}'.format(escolhido))


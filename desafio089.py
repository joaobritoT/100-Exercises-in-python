dicionario = {}

dicionario['nome'] = str(input("Nome: "))
dicionario['media'] = float(input("Media de {}: ".format(dicionario['nome'])))

if dicionario['media'] >=6:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

print("-=-"*15)

print("nome: {}".format(dicionario['nome']))
print("media: {}".format(dicionario['media']))
print("situacao: {}".format(situacao))
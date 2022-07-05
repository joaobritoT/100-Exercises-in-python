jogador = {}
gols = []
soma = 0


jogador['nome'] = str(input("nome do jogador: "))
partidas = int(input("quantas partidas ele jogou? "))

for p in range(0,partidas):
    valor = int(input("gols na {} partida: ".format(p+1)))
    soma = valor+soma
    gols.append(valor)

jogador['gols'] = gols
jogador['total de gols'] = soma

print("-=-"*15)
print(jogador)
print("-=-"*15)

print("o campo nome tem o valor: {}".format(jogador['nome']))
print("o campo gols tem o valor: {}".format(jogador['gols']))
print("o campo total tem o valor: {}".format(jogador["total de gols"]))

print("-=-"*15)
print("o jogador {} jogou {} partidas".format(jogador["nome"],partidas))

for i, v in enumerate(jogador["gols"]):
    print("na partida {}, fez {} gols".format(i+1,v))

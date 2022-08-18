def jogador(nome = "desconhecido",gols = 0):
    if len(nome) == 0:
        nome = "<desconhecido>"
    if len(gols) == 0:
        gols = 0
    return f'o jogador {nome}, fez {gols} gols'
print(jogador(str(input("nome: ")),(int(input("gols: ")))))
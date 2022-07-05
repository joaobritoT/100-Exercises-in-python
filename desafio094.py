jogador = {}
gols = []
time = []

while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome: "))
    total = int(input("quantas partidas ele jogou?: "))
    for p in range(0,total):
        gols.append(int(input("quantos gols ele fez na {} partida? ".format(p+1))))
    jogador['gols'] = gols[:]
    jogador['total de gols'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    resp = str(input("deseja continuar? s/n: "))[0]
    while resp not in 'sSnN':
        resp = str(input("ERRO! responda apenas s/n: "))
    if resp in 'Nn':
        break
print("-=-"*15)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print("-=-"*15)
while True:
    mostrar = int(input("deseja mostrar os dados de qual jogador? (999 para parar): "))
    if mostrar == 999:
        break
    if mostrar >len(time):
        print("erro, n existe jogador com esse numero")
    else:
        for i, g in enumerate(time[mostrar]['gols']):
            print("no jogo {} ele fez {} gols".format(i+1,g))
    print("-=-"*15)
print("volte sempre")
    

    

    
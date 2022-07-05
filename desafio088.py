
from time import sleep


ficha = []
fichario = []

while True:
    nome = str(input("nome: "))
    nota1 = float(input("nota 1: "))
    nota2 = float(input("nota 2: "))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("deseja continuar? s/n: ")).lower()[0]
    if resp in'Nn':
        break
print(f'{"no.":4<}{"nome":<10}{"media":>8}')

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print("-=-"*15)
    opc = int(input("mostrar notas de qual anluno? (999 interrompe): "))
    if opc == 999:
        print("finalizando...")
        sleep(0.5)
        break
    if opc<= len(ficha) - 1:
        print(f'notas de {ficha[opc][0]} sao {ficha[opc][1]}')
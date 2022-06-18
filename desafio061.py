print('Gerador de PA')
primeiro = int(input('digite o termo da PA: '))
razao = int(input('digite a razao da PA: '))
termo = primeiro
cont = 1
while cont <=10:
    print(termo, end=" ")
    termo += razao
    cont += 1
print('pausa')

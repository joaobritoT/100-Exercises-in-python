print('Gerador de PA')
primeiro = int(input('digite o termo da PA: '))
razao = int(input('digite a razao da PA: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais !=0:
    total = total + mais
    while cont <=total:
        print(termo, end=" ")
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('quantos termos mostrar a mais? :'))
    
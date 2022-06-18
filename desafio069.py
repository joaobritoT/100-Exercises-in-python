soma = 0
contmil = 0 
menor = 0
cont = 0
barato = ' '
print("="*20)
print("Loja do joao victor ")
print("="*20)
while True:
    produto = str(input("Nome do Produto: "))
    valor = float(input('valor do produto: R$'))
    continuar = str(input("deseja continuar? [s/n]")).upper().strip()[0]
    cont +=1
    if cont == 1:
        menor = valor
        barato = produto
    elif valor < menor:
        menor = valor
        barato = produto
    soma = soma + valor
    if valor >1000:
        contmil+=1
    if continuar in 'Nn':
        break
print("-=-=-=-=-=-FIM DO PROGRAMA-=-=-=-=-=-=-=")
print('O total da compra deu: R${}'.format(soma))
print('localizei {} produtos que custam mais de R$1.000'.format(contmil))
print('o produto mais barato eh {} e custa {:.2f}'.format(produto, menor))
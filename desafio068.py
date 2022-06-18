cont_idadae = 0
cont_homem = 0
mulher_20 = 0
while True:
    print('-='*20)
    print("CADASTRE UMA PESSOA")
    print('-='*20)
    idade = int(input("Idade: "))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    continuar = str(input("deseja continuar? [S/N] ")).upper().strip()[0]
    if idade >= 18:
        cont_idadae +=1
    if sexo in 'Mm':
        cont_homem +=1
    if sexo in 'Ff' and idade <20:
        mulher_20 +=1
    if continuar in 'Nn':
        break
print("total de pessoas com mais de 18 anos: {}".format(cont_idadae))
print("temos {} homems cadastrados".format(cont_homem))
print("Temos {} mulheres com menos de 20 anos".format(mulher_20))

    
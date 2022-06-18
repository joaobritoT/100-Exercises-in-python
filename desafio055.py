mvelho = 0
mnovo = 0
somaidade = 0
homem = 0
mulher = 0
mulher20 = 0
for c in range (1, 6):
    print('----- {} Pessoa -----'.format(c))
    Nome = str(input('Nome: '))
    idade = int(input('idade: '))
    sexo = str(input('[M/F]: ')).upper()
    print("--------------------")
    somaidade+= idade
    media = somaidade / 5
    if idade == 1:
        mvelho = idade
        mnovo = idade
    else:
        if idade > mvelho:
            mvelho = idade
        if idade < mnovo:
            mnovo = idade
    if sexo == 'M':
        homem+=1 
    elif sexo =='F':
        mulher+=1 
    if idade <20 and sexo == 'F':
        mulher20 +=1
print('A media de idade do grupo eh de: {}'.format(media))
print('A pessoa mais velha do grupo tem {} anos'.format(mvelho))
print('O grupo tem {} homens e {} mulheres'.format(homem, mulher))
print('A quantidade de mulheres com menos de 20 anos eh de {}'.format(mulher20))

    


ano = int(input('que ano deseja analisar?: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} eh bissexto'.format(ano))
else:
    print('o ano {} nao eh bissexto'.format(ano))

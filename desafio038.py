from datetime import date
atual = date.today().year 
nasc = int(input('qual o seu ano de nascmento? '))
idade = atual - nasc 
if idade == 18:
    print('voce deve se alistar IMEDIATAMENTE')
elif idade <18:
    saldo = 18 -idade
    print('voce tem {} anos no ano de {}'.format(idade, atual))
    print('faltam {} anos para vc se alistar'.format(saldo))
    print('seu alistamento sera em {}'.format(atual + saldo))
elif idade > 18:
    saldo = idade - 18 
    print('voce tem {} anos no ano de {}'.format(idade, atual))
    print('voce deveria ter se alistado ha {} anos'.format(saldo))
    print('seu alistamento foi em {}'.format(atual - saldo ))
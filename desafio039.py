n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media >= 6.0:
    print('sua media foi de {} e voce foi aprovado'.format(media))
elif media < 5.0:
    print('sua media foi de {} e voce foi reprovado '.format(media))
elif media < 6.0 and media >= 5.0:
    print('a sua media foi de {} e voce esta de RECUPERACAO'.format(media))
num = int(input('digite um numero para a conersao: '))
print('escolha uma das bases para conversao')
print("-=-"*15)
print('[ 1 ] converter para binario')
print('[ 2 ] converter para octal')
print('[ 3 ] converter para hexadecimal')
print("-=-"*15)
resposta = int(input(':'))
if resposta == 1:
    print('{}'.format(bin(num)[2:]))
elif resposta == 2:
    print('{}'.format(oct(num)[2:]))
elif resposta == 3:
    print('{}'.format(hex(num)[2:]))
else:
    print('opcao invalida')

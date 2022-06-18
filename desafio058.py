from time import sleep
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
opcao = int(input('[1] somar \n[2] Multiplicar \n[3] Maior \n[4] Novos numeros \n[5] Sair do programa \n:'))
soma = n1 + n2
mult = n1 * n2 
if n1 > n2:
    maior = n1
else:
    maior = n2
if opcao == 1:
    print('a soma dos numeros deu {} '.format(soma))
elif opcao == 2:
    print('a multiplicacao dos numeros deu {}'.format(mult))
elif opcao == 3:
    print('entre {} e {} o maior eh {}'.format(n1, n2, maior))
print('-='*20)
sleep(1.3)
while opcao != 5:
    sleep(1.3)
    opcao = int(input('[1] somar \n[2] Multiplicar \n[3] Maior \n[4] Novos numeros \n[5] Sair do programa \n:'))
    if opcao == 1:
        print('a soma dos dois numeros da {} '.format(soma))
    elif opcao == 2:
        print('A multiplicacao dos numeros da {}'.format(mult))
    elif opcao == 3:
        print('Ente {} e {} o maior eh {}'.format(n1, n2, maior))
    print('-='*20)
print('Fim')

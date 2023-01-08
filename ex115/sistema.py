from interface import *
from time import sleep
from arquivo import *


arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'cadastrar pessoas', 'sair do sistema'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        sleep(2)
        cabecalho('novo cadastro')
        nome = str(input("nome: "))
        idade = leiaint('idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabecalho('saindo do sistema...')
        sleep(2)
        break
    else:
        print("erro, digite uma opcao valida")
    sleep(2)


        


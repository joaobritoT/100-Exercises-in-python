def leiaint(msg):
    while True:
        try:
            n = int(input("digite uma opcao: "))
        except(ValueError,TypeError):
            print('erro, por favor, digite um numero inteiro valido. ')
            continue
        except(KeyboardInterrupt):
            print("entrada de dados interrompida pelo usuario")
            return 0
        else:
            return n




def linha(tamanho = 42):
    return '-' * tamanho

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('menu principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc = leiaint('sua opcao')
    return opc
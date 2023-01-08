from typing import Type


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

def leiafloat(msg):
    while True:
        try:
            f = float(input("digite um numero real: "))
        except(ValueError,TypeError):
            print("Erro, digite um numero real valido. ")
            continue
        except(KeyboardInterrupt):
            print("entrada de dados interrompida pelo usuario")
            return 0
        else:
            return f


num = leiaint('digite um valor: ')
numf = leiafloat("digite um valor: ")
print("o numero inteiro digitado foi {}".format(num))
print("o numero real digitado foi: {}".format(numf))

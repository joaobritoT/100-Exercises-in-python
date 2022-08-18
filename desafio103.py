def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('erro, digite um numero valido')
        if ok:
            break
    return valor
n = leiaint('digite um numero: ')
print("voce digitou o valor {}".format(n))
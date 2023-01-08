def resumo(n,a,r):
    print('-'*15)
    print("RSEUMO DO VALOR")
    print('-'*15)
    n=n
    dobro = n*2
    metade = n/2
    aumento = ((a/100) *n) + n
    reducao = n - ((a/100) *n) 
    print("Preco analisado: {}".format(n))
    print("dobro do preco {}".format(dobro))
    print("metade do preco: {}".format(metade))
    print("{}%. de aumento: {:.2f}".format(a,aumento))
    print("{}%. de reducao : {:.2f}".format(r,reducao))
    print('-'*30)
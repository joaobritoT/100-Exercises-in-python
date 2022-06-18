
lista = []
while True:
    valor = int(input("digite um valor para ser colocado na lista: "))
    if valor not in lista:
        lista.append(valor)
    else:
        print("valor duplicado")
    resposta = str(input("dejesa continuar? s/n: ").upper()[0])
    if resposta == "N":
        break
print("-=-"*20)
print("valores cadastrados: {}".format(sorted(lista)))
    
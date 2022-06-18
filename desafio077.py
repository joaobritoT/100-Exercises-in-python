
lista = []

for c in range(0,5):
    valores = int(input("digite um valor para a posicao {}: ".format(c)))
    lista.append(valores)

print("voce digitou os valores: {}".format(lista))
print("o maior valor digitado foi {} na posicao ".format(max(lista),))
for i, v in enumerate(lista):
    if v == max(lista):
        print("{}...".format(i), end=' ')
print("o menor valor digitado foi {} encontrado na posicao ".format(min(lista)))
for i, v in enumerate(lista):
    if v == min(lista):
        print("{}...".format(i),end=' ')

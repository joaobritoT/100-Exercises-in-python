def metade(n):
    return n /2
def dobro(n):
    return n *2 
def porcentagem(n):
    valor = 0.10 * n
    return valor + n
def moeda(preco =0, moeda="R$"):
    return f'{moeda}{preco}'.replace('.',',')

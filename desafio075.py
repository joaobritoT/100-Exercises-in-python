listagem = ('lapis',1.10,
'borracha',2.00,
'caderno',3.00,
'caneta',4.00)
for pos in range(0,len(listagem)):
    if pos %2 ==0:
        print(f"{listagem[pos]:.<25}", end=' ')
    else:
        print(f"{listagem[pos]:.<3}")
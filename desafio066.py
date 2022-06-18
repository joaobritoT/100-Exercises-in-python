teste = 1
while teste >0:
    n = int(input("valor para tabuada: "))
    cont = 0
    if n <0:
        break
    while cont <10:
        cont+=1
        valor = n *cont
        print("{} x {} = {} ".format(n,cont,valor))
print("fim")  
   


    

    
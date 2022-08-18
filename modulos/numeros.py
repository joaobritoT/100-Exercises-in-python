import uteis


num = int(input("digite um valor: "))

fat = uteis.fatorial(num)
print("o fatorial de {} eh {}".format(num,fat))
print("o dobro de {} eh {}".format(num,uteis.dobro(num)))
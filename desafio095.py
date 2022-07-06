def calculo(largura, comprimento):
    area = largura * comprimento
    print("a area de {}x{} eh de {}m2".format(largura,comprimento,area))


l = int(input("largura: "))
c = int(input("comprimeto: "))

calculo(l,c)
from time import sleep


def contador(p,i,v):
    print("-=-"*15)
    print("contando ate {}".format(i))
    for c in range(p,i,v):
        print(c, end=' ')
        sleep(0.5)
    print()
    print("-=-"*15,)
    

contador(1,10,1)
contador(10,0,-2)
print("agora eh a sua vez de contar: ")
inicio = int(input("inicio: "))
fim = int(input("fim: "))
passo = int(input("passo: "))
if fim < inicio:
    passo = -passo
elif inicio<fim:
    passo = +passo



contador(inicio,fim,passo)

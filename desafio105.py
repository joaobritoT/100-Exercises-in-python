def ajuda(com):
    help(com)

def titulo(msg):
    tam = len(msg)
    print("="*tam)
    print(msg)
    print("="*tam)

comando=''
while True:
    print(titulo("sistema de ajuda python"))
    comado = str(input("digite um comando para ver a documentacao > "))
    if comado.upper().strip() == "FIM":
        break
    else:
        ajuda(comado)
    comado = str(input("digite um comando para ver a documentacao > "))
print(titulo("ate logo"))


matriz  = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
maicol = 0
mailin = 0 
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input("digite um numero para a posicao [{},{}]: ".format(i,j)))

for i in range(0,3):
    for j in range(0,3):
        print("[{}]".format(matriz[i][j]), end='')
        if matriz[i][j] % 2 == 0:
            soma = matriz[i][j] + soma
    print()

for i in range(0,3):
    maicol = maicol + matriz[i][2]
for j in range(0,3):
    mailin = mailin + matriz[1][j]
print("a soma dos numeros pares deu: {}".format(soma))
print("a soma da terceira coluna eh igual a {}".format(maicol))
print("a soma da segunda linha da matriz deu {}".format(mailin))
            

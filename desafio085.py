num = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        num[i][j] = (int(input("valor para [{},{}]:".format(i,j))))
        
for i in range(0,3):
    for j in range(0,3):
        print("[{}]".format(num[i][j]), end='')
    print()
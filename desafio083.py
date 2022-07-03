temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input("nome: ")))
    temp.append(float(input("peso: ")))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resposta = str(input("deseja continuar? s/n: ")).lower()[0]
    if resposta == 'n':
        break

print("-=-"*30)
print("voce cadastrou {} pessoas".format(len(princ)))
print("o maior peso foi de {}kg".format(mai))
for p in princ:
    if p[1] == mai:
        print(p[0])
print("o menor peso foi de {}kg".format(men))
for p in princ:
    if p[1] == men:
        print(p[0])

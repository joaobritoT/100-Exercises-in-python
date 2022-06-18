n = 0
s = 0
while True:
    n = int(input("digite um numero: "))
    if n == 999:
        break
    s += n
print("a soma dos numeros digitados eh de {}".format(s))
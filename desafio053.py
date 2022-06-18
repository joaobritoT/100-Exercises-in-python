from datetime import date
ano = 0
totmaior = 0
totmenor = 0
for c in range(0, 7):
    ano+= 1
    data = (int(input('em que a ano a pessoa {} naseu?'.format(ano))))
    idade = date.today().year - data
    if idade >= 18:
        totmaior+=1
    else:
        totmenor+=1
print("tivemos {} maiores de idades e {} menores de idade".format(totmaior, totmenor))

from time import sleep


pessoas = {}
lista = []
total  = 1
total_idade = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input("Nome: "))
    pessoas['idade'] = int(input("idade: "))
    total_idade = pessoas["idade"] + total_idade
    pessoas['sexo'] = str(input("sexo M/F: "))[0]
    while pessoas['sexo'] not in 'mfMF':
        pessoas['sexo'] = str(input("Erro! responda apenas M/F: "))[0]
    lista.append(pessoas.copy())
    resp = str(input("deseja continuar? s/n: ")).lower()[0]
    while resp not in 'snSN':
        resp = str(input("Erro! responda apenas s/n: ")).lower()[0]
    if resp in 'Nn':
        break
    total+=1
media_idades = total_idade / total
print("-=-"*20)
print("A) ao todo temos {} pessoas cadastradas".format(total))
sleep(0.5)
print("B) a media das idades eh de {:.2f} anos".format(media_idades))
sleep(0.5)
print("C) as mulheres cadastradas foram ", end='')
sleep(0.5)
for p in lista:
    if p["sexo"] in 'Ff':
        print(p["nome"])
print()
print("D) lista as pessoas q estao acima da media: ", end='')
for p in lista:
    if p['idade'] > media_idades:
        print(p['nome'])
print("-=-"*20)
print("ENCERRANDO...")
sleep(1)

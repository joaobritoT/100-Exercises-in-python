frase = str(input('digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = "".join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('{} digitado de traz para frente fica {}'.format(junto, inverso))
if inverso == junto:
    print('a frase eh palindromo')
else:
    print('nao eh palindromo')
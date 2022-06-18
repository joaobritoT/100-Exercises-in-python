frase = str(input('digite uma frase qualaquer: ')).lower().strip()
print('a letra "a" aprace {} vezes na sua frase'.format(frase.count('a')))
print('a primeira letra a apareceu na posicao {}'.format(frase.find('a') + 1))
print('a ultima letra a apareceu na posicao {} '.format(frase.rfind('a') + 1))


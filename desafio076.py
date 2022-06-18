lista = ('aprender', 'programar', 'linguagem','python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador','futuro')

for p in lista:
    print('\nna palavra {} temos '.format(p), end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end='')
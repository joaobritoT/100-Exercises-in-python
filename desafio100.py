


def votar(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <16:
        return f'com {idade} anos nao vota'
    elif idade <18 and idade >=16 or idade >65:
        return f'com {idade} anos o voto eh opicional'
    else:
        return f'com {idade} anos eh obrigatorio votar'

print(votar(int(input("em que ano vc nasceu?:  "))))

peso = float(input('qual seu peso? (KG): '))
altura = float(input('qual sua altutura?: '))
imc = peso / altura **2 
if imc <= 18.5:
    print('o seu IMC eh de {:.2f} e eh considerado MAGREZA'.format(imc))
elif imc > 18.5 and imc <= 24.9:
    print('seu IMC eh de {:.2f} e eh considerado NORMAL'.format(imc))
elif imc > 24.9 and imc <= 30:
    print('seu IMC eh de {:.2f} e eh considerado SOBREPESO'.format(imc))
elif imc > 30:
    print('seu IMC eh de {:.2f} e eh considerado OBESIDADE'.format(imc))
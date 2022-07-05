from datetime import date


dados = {}

dados['nome'] = str(input("nome: "))
dados['nasc'] = int(input("ano de nascimento: "))
dados['carteira de trab'] = int(input("carteira de trabalho (0 n tem): "))
if dados['carteira de trab'] == 0:
    print("nome: {}".format(dados['nome']))
    print("ano de nasc: {}".format(dados['nasc']))
    
else:
    dados['contratacao'] = int(input("ano de contratacao: "))
    dados['salario'] = float(input("salario: "))
    idade = date.today().year - dados['nasc']
    dados['aposentadoria'] = dados['contratacao'] + 24 + idade - 2000
    print("-=-"*15)
    print("nome: {}".format(dados['nome']))
    print("ano de nasc: {}".format(dados['nasc']))
    print("carteira de trabalho: {}".format(dados['carteira de trab']))
    print("salario: {}".format(dados['salario']))
    print("aposentadoria: {} anos".format(dados['aposentadoria']))
    

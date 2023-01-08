
from interface import cabecalho


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print("erro na criacao do arquivo")
    else:
       print("arquivo {} criado com sucesso".format(nome)) 


def lerarquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print("erro ao ler o arquivo")
    else:
        cabecalho('pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            print(f'{dado[0]}{dado[1]} anos')
    finally:
        a.close()

def cadastrar(arq,nome = "desconhecido",idade = 0):
    try:
        a = open(arq,'at')
    except:
        print("erro na abertura do arquivo")
    else:
        try:
            a.write(f'{nome};{idade}')
        except:
            print("erro ao escrever os dados")
        else:
            print("novo registro de {} adicionado".format(nome))
            a.close()
        
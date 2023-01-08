try:
    a = int(input("numerador: "))
    b = int(input("denominador: "))
    r = a/b
except Exception as erro:
    print("infelizmente tivemos o problema {} ".format(erro.__class__))

else:
    print("o resultado eh {}".format(r))

finally:
    print("volte sempre")
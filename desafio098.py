from time import sleep


def maior(*num):
    print("analisado os valores passados...")
    for valor in num:
        print(valor,end=' ')
        sleep(0.5)
    print("o maior valor eh {}".format(max(num)))



maior(0,4,5,6,73,1)
sleep(0.5)
maior(0,3,4,5,)
sleep(0.5)
maior(0)

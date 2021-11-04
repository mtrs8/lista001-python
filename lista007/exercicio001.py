# 1. Entrar como n's números e imprimir o triplo de cada. o programa encerra quando entrar com o numero 999;

loop = 1
while loop:
    num1 = int(input("Digite um valor: "))
    if(num1 == 999):
        print("Programa Encerrado!")
        loop = 0
        break

    print("Triplo: {}".format(num1*3))
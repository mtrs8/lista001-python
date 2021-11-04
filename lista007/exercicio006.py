# 6.Entrar com vários números ate entrar com o numero 999. para cada numero imprimir seus divisores;

sair = 1
while sair != 0:
    numero = int(input("Insira valor: "))
    if(numero == 999):
        print("Programa encerrado!")
        sair = 0
        break
    else:
       for divisor in range(1, numero):
            if(numero % divisor == 0):
                print("Divisores: {}".format(divisor))
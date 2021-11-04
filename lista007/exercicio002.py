# 2.Entrar com números enquanto forem positivos, e imprimir quantos números foram digitados;

loop = 1
while loop:
    num1 = int(input("Digite um valor: "))
    if(num1 < 0):
        print("Programa Encerrado!")
        loop = 0
        break

    print("Valor: ", num1)
# 5.Entrar com 3 números, e imprimir o maior número]

valor1 = int(input("Entre com qualquer valor: "))
valor2 = int(input("Entre com mais um valor: "))
valor3 = int(input("Entre com mais um valor: "))

if(valor1 > valor2 and valor1 > valor3):
    print(valor1)
elif(valor2 > valor1 and valor2 > valor3):
    print(valor2)
elif(valor3 > valor1 and valor3 > valor2):
    print(valor3)
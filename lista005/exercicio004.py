# 4.Entrar com 2 números e imprimir o maior número

valor1 = int(input("Entre com qualquer valor: "))
valor2 = int(input("Entre com mais um valor: "))

if(valor1 > valor2):
    print(valor1)
elif(valor2 > valor1):
    print(valor2)
elif(valor1 == valor2):
    print("Valores iguais!")
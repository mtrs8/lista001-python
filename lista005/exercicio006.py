# 6.entrar com 3 números e imprimi-los em ordem crescente

valor1 = int(input("Entre com qualquer valor: "))
valor2 = int(input("Entre com mais um valor: "))
valor3 = int(input("Entre com mais um valor: "))

valores = [valor1, valor2, valor3]

print(sorted(valores))
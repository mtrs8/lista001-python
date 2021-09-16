# 2. Entrar com quatro números e imprimir a media ponderada, sabendo-se que os pesos são respectivamente 1,2,3,4.

n1 = float(input("Digite nota da primeira unidade: "))
n2 = float(input("\nDigite nota da segunda unidade: "))
n3 = float(input("\nDigite nota da terceira unidade: "))
n4 = float(input("\nDigite nota da quarta unidade: "))

media = ((1*n1) + (2*n2) + (3*n3) + (4*n4)) / (1 + 2 + 3 + 4)

print("Média Ponderada: {:.1f}".format(media))
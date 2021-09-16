# 3. Entrar com um nome e imprimir: a) todo o nome; b) primeiro carcater; c) ultimo carcater; d) do primeiro
# ate o terceiro caracter; e)quarto caracter; f) os dois últimos.

string1 = input("Entre com uma string qualquer: ")

print("Todo a string: ", string1)
print("Primeiro caracter: ", string1[0])
print("Quarto caracter: ", string1[3])
print("Último caracter: ", string1[-1])
print("Dois ultimos: ", string1[-2:])
print("do primeiro ao terceiro: ", string1[:3])
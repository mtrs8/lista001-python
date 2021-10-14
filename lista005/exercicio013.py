# 13. Entrar com um número e escrever uma das mensagens: “é múltiplo de 3", ou "não é múltiplo de 3"

num = int(input("Digite um número: "))

if(num % 3 == 0):
    print("É múltiplo de 3!")
else:
    print("Não é múltiplo de 3!")

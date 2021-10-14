# 12. Entrar com dois números inteiros e efetuar a adição. Caso o valor somado seja maior que 20, este
# deverá ser apresentado somando-se a ele mais 8; caso o valor somado seja menor ou igual a 20, este
# deverá ser apresentado subtraindo-se 5.

a, b = input("Digite dois valores: ").split(" ")
soma = int(a) + int(b)
if(soma >= 20):
    soma += 8
    print("Novo valor de soma: ", soma)
else: 
    soma -= 5
    print("Novo valor de soma: ", soma)
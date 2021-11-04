# 10.Criar um programa que deixe entrar com 10 números positivos e imprima a raiz quadrada de cada numero. 
# Para cada entrada de dados devera haver um trecho de "proteção" para que um numero negativo não seja aceito

import math

sair = 1
while sair != 0:
    numero = int(input("Insira valor: "))
    if(numero < 0):
        print("Não é possível calcular raiz quadrada de números negativos, insira novamente!")
        continue
    else:
        print("Raiz quadrada: {:.2f}".format(math.sqrt(numero)))
        sair = int(input("\nDigite qualquer número para continuar ou 0 (zero) para sair: "))
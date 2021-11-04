# 1. Ler vários números inteiros ate o usuario digitar um numero negativo, 
# e apresente o fatorial de cada numero;
# Aluno: MATHEUS ALVES RODRIGUES

import math

sair = 1
while sair:
    numero = int(input("Insira valor: "))
    if(numero < 0):
        print("Programa Encerrado!")
        sair = 0
        break
    else:
        print("Fatorial: {:.2f}".format(math.factorial(numero)))
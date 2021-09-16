# 8. Dado um numero de conta corrente com três dígitos, retorne o seu digito verificador, 
# o qual é calculado da seguinte maneira. Exemplo: numero conta 235, somar o numero da 
# conta com seu inverso : 235+532=767. Multiplicar cada digito pela sua ordem posicional 
# e somar estes resultados: 7 6 7 (7x1+6x2+7x3) = 40. 
# O ultimo digito desse resultado é o digito verificador da conta (40-> 0)

import math

valor = int(input("Digite o número da conta(3 digitos): "))
valor_invertido: int = int(str(valor)[::-1])
soma_valores = valor + valor_invertido
dezena: int = math.trunc((soma_valores - soma_valores % 100) / 100)
centena: int = math.trunc(soma_valores % 100 / 10)
milhar: int = soma_valores % 100
digito_verificador = (dezena * 1 + centena * 2 + milhar * 3) % 10
print("Digito Verificador: ", digito_verificador)
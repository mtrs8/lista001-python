# Funcao para calculo da area de um circulo

import math

def area_circulo(raio):
    return math.pi * math.pow(raio, 2)

raio = float(input('Digite o raio do circulo: '))
print('A area do circulo é {:.2f}'. format(area_circulo(raio)))

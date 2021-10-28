# 2) Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em 
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
# para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que
# custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
import math

area_em_m2 = float(input("Insira a área(em m²): "))

litros = area_em_m2 / 6
latas = math.ceil(litros / 18)
galoes = litros / 3.6
mistura_latas = math.ceil(litros / 18)
mistura_galao = math.ceil((litros - (mistura_latas * 18)) / 3.6)

if(latas % 18 != 0):
    latas += 1
valor_latas = latas * 80

if(galoes % 3.6 != 0):
    galoes += 1
valor_galoes = galoes * 25


if(litros - (mistura_latas * 18) % 3.6 != 0):
    mistura_galao += 1

print("Situação 1 - Latas de 18 Litros:\n Latas: {} \n Preço: {}".format(latas, valor_latas))
print("\nSituação 2 - Galões de 3.6 litros:\n Galões: {:.2f}\n Preço: {:.2f}".format(galoes, valor_galoes))
print("\nSituação 3 - Mistura: {} Latas e {} galões = {}". 
    format(mistura_latas, mistura_galao, ((mistura_latas * 80) + (mistura_galao * 25))))

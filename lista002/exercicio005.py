# 5. Calcular a quantidade de litros de combustível gastos em uma viagem, sabendo-se que o carro faz 12km
# com 1 litro. Deverão. Ser fornecidos a) tempo gasto na viagem; b) e a velocidade media. Apresentar os
# valores da velocidade media, tempo gasto, distancia percorrida e quatidade de litros gastos.

tempo_viagem = int(input("Tempo para realização da viagem: "))
vel_media = int(input("Velocidade média do veículo: "))

distancia_percorrida = tempo_viagem * vel_media

qtd_litros = distancia_percorrida / 12

print("Velocidade Média: ", vel_media, "Km/h")
print("Tempo gasto: ", tempo_viagem, "horas")
print("Distancia Percorrida: ", distancia_percorrida, "quilometros")
print("Quantidade de Litros gastos: {:.2f}".format(qtd_litros))
# 9.Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores deconsumo. 
# Para cada consumidor, são digitados os seguintes dados:
# a)num_consumidor do consumidor; 
# b)Quantidade de kWh consumidos durante o mês; 
# c)tipo do consumidor -> 1-residencial, preço em reias de kWh = 0,3 / 2-comercial, 
# preço em reais de kWh = 0,5 / 3-industrial, preço em reais de kWh = 0,7. 
# Os dados devem ser lidos ate que seja encontrado um consumidor com num_consumidor 0(zero). 
# Calcular e imprimir: 
# a) o custo total para cada consumidor; 
# b) o total de consumo para os 3(três) tipos de consumidor; 
# c) a media de consumo dos tipos 1 e 2.

consumidores = []
qtd_kwh = 0
tipo_consumidor = 1
sair = 1
while sair != 0:
    num_consumidor = int(input("Número do consumidor: "))
    if(num_consumidor == 0):
        print("Programa encerrado!")
        sair = 0
        break
    else:
        qtd_kwh = float(input("Quantidade de KWh consumidos por mês: "))
        tipo_consumidor = int(input("Qual tipo de consumidor você é?\n1) Residencial\n2) Comercial\n3) Industrial.\n"))
        if tipo_consumidor == 1: 
            print("Preço mensal: {:.2f}".format(qtd_kwh * 0.3))
        elif tipo_consumidor == 2:
            print("Preço mensal: {:.2f}".format(qtd_kwh * 0.5))
        elif tipo_consumidor == 3:
            print("Preço mensal: {:.2f}".format(qtd_kwh * 0.7))
        
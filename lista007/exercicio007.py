# 7.Dado um pais A, com 5.000.0000 de habitantes e uma taxa de natalidade de 3% ao ano,
#  e um pais B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano. 
# Calcular e imprimir o tempo necessário para que a população do pais A ultrapasse a população do pais B;

habitante_pais_a = 50000000
taxa_natalidade_a = 0.03
habitante_pais_b = 70000000
taxa_natalidade_b = 0.02
tempo = 0

while habitante_pais_a < habitante_pais_b:
    #print(tempo)
    natalidade_anual_a = habitante_pais_a * taxa_natalidade_a
    habitante_pais_a += natalidade_anual_a
    natalidade_anual_b = habitante_pais_b * taxa_natalidade_b
    habitante_pais_b += natalidade_anual_b
    tempo+=1 

    if(habitante_pais_a > habitante_pais_b):
        print("Tempo necessário para ultrapassagem entre as natalidades dos países é de {} anos.".format(tempo))

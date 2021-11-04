# 8. Chico tem 1.50m e cresce 2 centímetros por ano, enquanto Juca tem 1.10m e cresce 3 cm por ano. 
# Construir um programa que calcule e imprima quantos anos serão necessários para Juca seja maior que Chico;

chico = 1.50
crescimento_chico = 0.2
juca = 1.10
crescimento_juca = 0.3
tempo = 0

while juca < chico:
    #print(tempo)
    chico += crescimento_chico
    juca += crescimento_juca
    tempo+=1

    if(juca > chico):
        print(f"Juca será maior que chico em {tempo} anos!") 

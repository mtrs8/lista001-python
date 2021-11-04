# 3. Na usina de Angra dos Reis, os técnicos analisam a perda de massa de um material
# radioativo. Sabendo-se que este perde 25% de sua massa a cada 30
# segundos, criar um programa que imprima o tempo necessário para que a
# massa deste material se torne menor que 0,10 gramas. O programa pode
# calcular o tempo para varias massas.
# Aluno: MATHEUS ALVES RODRIGUES

massa_perdida = 0.25
tempo = 0
sair = 1
while sair:
    massa = int(input("Insira valor da massa em Kg: "))
    if(massa < 0):
        print("Não é possível calcular massa de números negativos, insira novamente!")
        continue
    else:
       while massa >= 0.10:
           massa *= massa_perdida
           tempo += 30    

    print("O tempo necessário para a massa chegue em menos de 0.10 gramas é de {} segundos!".format(tempo))
    sair = int(input("\nDigite qualquer número para continuar ou 0 (zero) para sair: "))
# 4) Um posto está vendendo combustíveis com a seguinte tabela de descontos:

# a. Álcool:
# b. até 20 litros, desconto de 3% por litro
# c. acima de 20 litros, desconto de 5% por litro

# d. Gasolina:
# e. até 20 litros, desconto de 4% por litro
# f. acima de 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago
# pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool
# é R$ 1,90.

tipo_combustivel = input("A-Alcool ou G-Gasolina[A/G]?\n")
qtd_litros = int(input("Quantos litros?\n"))

if(tipo_combustivel.upper() == 'A'):
    preço_alcool = 1.90
    custo = qtd_litros * preço_alcool
    if(qtd_litros <= 20):
        desconto_alcool = custo * 0.03
        print("\n*** ALCOOL ****")
        print("Desconto: {:.2f}\nPreço: {:.2f}".format(desconto_alcool, custo - desconto_alcool))
    else:
        desconto_alcool = custo * 0.05
        print("\n*** ALCOOL ****")
        print("Desconto: {:.2f}\nPreço: {:.2f}".format(desconto_alcool, custo - desconto_alcool))

elif(tipo_combustivel.upper() == 'G'):
    preço_gasolina = 2.50
    custo = qtd_litros * preço_gasolina
    if(qtd_litros <= 20):
        desconto_gasolina = custo * 0.04
        print("\n*** GASOLINA ****")
        print("Desconto: {:.2f}\nPreço: {:.2f}".format(desconto_gasolina, custo - desconto_gasolina))
    else:
        desconto_gasolina = custo * 0.06
        print("\n*** GASOLINA ****")
        print("Desconto: {:.2f}\nPreço: {:.2f}".format(desconto_gasolina, custo - desconto_gasolina))
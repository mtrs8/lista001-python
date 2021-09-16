# Inversor de algarismos
valor = 123
dezena = valor % 10
centena = valor % 100 / 10
milhar = valor % 1000 / 100

print("Número a ser invertido:", valor)
print(round(dezena), round(centena), round(milhar))
# calculo de compras para 4 pessoas

valor_cerveja = 2.20 * 75
valor_macarrao = 2 * 8.73
valor_molho = 3.45
valor_cebola = (420 * 5.40) / 1000 
valor_alho = (250 * 30) / 1000
valor_paes = (450 * 25) / 1000

valor_total = valor_cerveja + valor_macarrao + valor_molho + valor_cebola + valor_alho + valor_paes
valor_para_cada = valor_total / 5

print("Valor total da compra: {:.2f}".format(valor_total))
print("Valor Individual p/ 4 pessoas: {:.2f}".format(valor_para_cada))
# 7. Criar um programa que leia a quantidade de fotas de uma locadora de vídeo possui
# e o valor que ela cobra por cada aluguel, mostrando as informações pedidas a seguir: 
# a) sabendo que um terço das fitas são alugadas por mês, exiba o faturamento anual da locadora; 
# b)Quando o cliente atrasa a entrega, é cobrada uma multa de 10% sobre o valor do aluguel. 
# Sabendo que um decimo das fitas alugadas no mês são devolvidas com atraso, 
# calcule o valor ganho com multas por mês; c) sabendo ainda que 2% de fitas se estragam
# ao longo do ano, e um decimo do total é comprado para reposição, exiba a quantidade de fitas 
# que a locadora terá no final do ano.

qtd_fitas_total = int(input("Quantidade de fitas de vídeo da locadora: "))
valor_por_aluguel = float(input("Valor do aluguel: "))

# letra A
total_fitas_mensal = qtd_fitas_total / 3
faturamento_anual = (valor_por_aluguel * total_fitas_mensal) * 12
print("Faturamento Anual: ", faturamento_anual)

# Letra B
fitas_com_atraso = total_fitas_mensal / 10
faturamento_multas = (fitas_com_atraso * valor_por_aluguel) * 0.10
print("Faturamento com multas mensal: ", faturamento_multas)

# Letra C
fitas_restantes = qtd_fitas_total - ((qtd_fitas_total * 0.02) + (qtd_fitas_total / 10))
print("Fitas restantes: ", fitas_restantes)

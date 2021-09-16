# 4. Calcular o salario liquido de um professor. Os dados fornecidos serão:
#  a) valor hora aula; b) numero de aulas dadas; c) percentual de desconto INSS.
# Aliquota INSS: **Janeiro de 2021**
# 0.075 se salario for até 1.100
# 0.09 se for até 2.203
# 0.12 se for até 3.305
# 0.14 se for até 6.433

valor_hora_aula = float(input("Valor da hora-aula do professor: "))
total_aulas = int(input("Total de aulas dadas pelo professor: "))
percent_inss = float(input("Percentual de desconto do INSS: ")) 


salario_liquido = (valor_hora_aula * total_aulas) * percent_inss

print("Salário Liquido do Professor: {:.2f}".format(salario_liquido))





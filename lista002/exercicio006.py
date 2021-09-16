# 6. Entrar com valor de um empréstimo, a taxa de juros e a quantidade de meses. Fazer um programa que 
# calcule o valor da prestação.

valor_emprestimo = float(input("Valor de empréstimo: "))
taxa_juros = float(input("Porcentagem de juros: ")) #Calculo com base nos juros simples
qtd_parcelas = int(input("Quantidade de parcelas: "))

valor_juros = valor_emprestimo * taxa_juros
valor_parcelas = (valor_emprestimo + valor_juros) / qtd_parcelas

print("Valor da parcela:", valor_parcelas)
print("Valor Total: ", valor_emprestimo + valor_juros)



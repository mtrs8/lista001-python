#15. A prefeitura do Rio de Janeiro abriu uma linha de crédito para seus funcionários. O valor máximo da
# prestação não poderá ultrapassar 30% do salário bruto. Fazer um programa que permita entrar com o
# salário bruto e o valor da prestação e informar se o empréstimo pode ou não ser concedido.

salario_bruto = float(input("Salário bruto: "))
valor_prestacao = float(input("Valor da prestação: "))

if((salario_bruto * 0.30) >= valor_prestacao):
    print("Empréstimo realizado com sucesso!")
else:
    print("Empréstimo não pode ser concedido!")

# 9.Um comerciante comprou um produto e quer vende-lo com um lucro de 45% se o valor da compra for
# menor que 20,00, caso contrário o lucro será de 30%. entrar com o valor do produto 
# e imprimir o valor da venda.

valor_produto = float(input("Digite o valor do produto: "))
lucro = 0;

if(valor_produto < 20):
    lucro = valor_produto * 0.45
else:
    lucro = valor_produto * 0.30
    
print("Valor da venda: ", valor_produto + lucro)
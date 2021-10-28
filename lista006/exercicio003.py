# 3) O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#    Até 5 Kg                   Acima de 5 Kg
# File Duplo R$ 4,90 Kg         R$ 5,80 por Kg
# Alcatra R$ 5,90 Kg            R$ 6,80 por Kg
# Picanha R$ 6,90 Kg            R$ 7,80 por kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da
# promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no
# cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o parcial da compra. Escreva
# um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom
# fiscal, contendo as informações da compra: tipo e quantidade de carne, preço parcial, tipo de
# pagamento, valor do desconto e valor a pagar.

def menu():
    print("Promoção de carnes:\n")
    print("1) File Duplo\n")
    print("2) Alcatra\n")
    print("3) Picanha\n")
    print("0) Sair do programa\n")
    opcao = eval(input("Escolha sua opção: "))
    while not 0 <= opcao <= 3:
        opcao = eval(input("Escolha uma opção de 0 a 3: "))
    else:
        return opcao

def gerar_cupom(parcial, qtd_carne, tipo_carne, has_cartao):
    desconto = parcial * 0.05
    print("******** COMPROVANTE FISCAL **************")
    if(tipo_carne == 1):
        if(has_cartao.upper() == 'S'):
            print("Tipo: File Duplo\nQuantidade em Kg: {}\nValor da compra: {:.2f}\nDesconto: {:.2f}\n\n"
                    .format(qtd_carne, parcial - desconto, desconto))
        else:    
            print("Tipo: File Duplo\nQuantidade em Kg: {}\nValor da compra: {:.2f}".format(qtd_carne, parcial))
    elif(tipo_carne == 2):
        if(has_cartao.upper() == 'S'):
            print("Tipo: Alcatra\nQuantidade em Kg: {}\nValor da compra: {:.2f}\nDesconto: {:.2f}\n\n"
                    .format(qtd_carne, parcial - desconto, desconto))
        else:    
            print("Tipo: Alcatra\nQuantidade em Kg: {}\nValor da compra: {:.2f}\n\n".format(qtd_carne, parcial))
    elif(tipo_carne == 3):
        if(has_cartao.upper() == 'S'):
            print("Tipo: Picanha\nQuantidade em Kg: {}\nValor da compra: {:.2f}\nDesconto: {:.2f}\n\n"
                    .format(qtd_carne, parcial - desconto, desconto))
        else:    
            print("Tipo: Picanha\nQuantidade em Kg: {}\nValor da compra: {:.2f}\n\n".format(qtd_carne, parcial))

print("Bem-vindo ao Supermercado Tabajara:\n")
loop = 1
while loop:
    valor_parcial = 0
    op = int(menu())
    if(op == 0):
        loop = 0
        print("Programa encerrado!!")
        break

    qtd_carne = int(input("Quantos kg você deseja?\n"))
    has_cartao = input("Possui cartão tabajara [S/N]?\n")
    if(op == 1):
        if(qtd_carne <= 5):
            valor_parcial = 4.90 * qtd_carne
        else:
            valor_parcial = 5.80 * qtd_carne
    elif(op == 2):
        if(qtd_carne <= 5):
            valor_parcial = 5.90 * qtd_carne
        else:
            valor_parcial = 6.80 * qtd_carne
    elif(op == 3):
        if(qtd_carne <= 5):
            valor_parcial = 6.90 * qtd_carne
        else:
            valor_parcial = 7.80 * qtd_carne
    #valor_parcial = has_cartao.upper() == 'S' if valor_parcial * 0.05 else valor_parcial
    gerar_cupom(valor_parcial, qtd_carne, op, has_cartao)
    









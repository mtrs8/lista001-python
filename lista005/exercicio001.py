# 1. Entre com um número e informe se o mesmo está compreendido entre 20 e 90;

valor = int(input("Entre com um valor qualquer: "))
if(valor >=20 and valor <= 90):
    print("Valor está entre 20 e 90!!")
else: 
    print("Valor {valor} não está entre 20 e 90")
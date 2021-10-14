# 7.entrar com 3 números e armazená-los em três variáveis diferentes:
# maior, menor e intermediário.

menor, maior, intermediario = 0;
a, b, c = int(input("Digite 3 valores: "))
# menor
if(a < b):
    if(a < c):
        menor = a
    else:
        menor = c
else: 
    if(b < c): 
        menor = b
    else:
        menor = c

# maior
if(a > b):
    if(a > c):
        maior = a
    else:
        maior = c
else: 
    if(b > c):
        maior = b
    else:
        maior = c

# intermediario
if(menor != a):
    if(menor != b):
        intermediario = c
    

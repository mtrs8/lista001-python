# 4.Entrar com vários números e informar quantos números entre 100 e 200 foram digitados. 
# Quando o valor 0 for digitado o programa deve encerrar;
count = 0;
loop = 1
while loop:
    n1 = int(input("Digite um valor: "))
    if(n1 == 0): 
        print("Números entre 100 e 200 encontrados: {}".format(count))
        loop = 0
    elif(n1 >= 100 and n1 <= 200):
        count+=1




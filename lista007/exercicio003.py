# 3.Entrar com vários números positivos e imprimir a media dos números digitados. 
# O programa acaba quando se informar que não deseja mais continuar.

sair = 1
soma_valores = 0
count = 0
while sair != 0:
    n1 = int(input("Insira valor positivo: "))
    if(n1 < 0):
        continue
    else:
        soma_valores =+ n1
        count += 1

    print("\nMédia: {:.2f}".format(soma_valores/count))
    sair = int(input("\nDigite qualquer tecla para continuar ou 0 (zero) para sair [0/1]: "))
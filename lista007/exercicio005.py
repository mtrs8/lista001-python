# 5.Entrar com nomes enquanto forem diferentes de FIM e imprimir o primeiro caracter de cada nome;

sair = ''
primeiro_caracter = ''
count = 0
while sair != 0:
    nome = input("Insira um nome: ")
    if(nome == 'Fim'):
        continue
    else:
        primeiro_caracter = nome[0]

    print("\nPrimeiro caracter: {}".format(primeiro_caracter))
    sair = int(input("\nDigite qualquer tecla para continuar ou 0 (zero) para sair [0/1]: "))
# 2. Sabendo-se que a UAL calcula a divisão através de subtrações 
# sucessivas, criar m programa que calcule e imprima o resto da divisão de
# números inteiros lidos. suponha que os números lidos sejam positivos e
# que o dividendo seja maior que o divisor.
# Aluno: MATHEUS ALVES RODRIGUES

sair = 1
while sair:
    dividendo = int(input("Insira dividendo: "))
    divisor = dividendo - 1
    if(dividendo < 0):
        print("Não é possível resto da divisão de números negativos, insira novamente!")
        continue
    else:
        while divisor > 0:
            print(f'O resto da divisão de {dividendo} por {divisor} é igual a {dividendo % divisor}')
            divisor -= 1

        sair = int(input("\nDigite qualquer número para continuar ou 0 (zero) para sair: "))
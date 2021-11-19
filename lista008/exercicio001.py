# Funcao par ou impar

def par_impar(x):
    if x % 2 == 0:
        return 'par'
    return 'impar'
    
numero = int(input('Digite um valor: '))
print('O numero {} é {}'.format(numero, par_impar(numero)))
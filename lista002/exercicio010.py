# 10. Dada a frase “Python é muito legal". use fatiamento para dar nome às variáveis contendo cada palavra. 
# Qual o tamanho dessa frase? E qual o tamanho de cada palavra?

frase = 'Python é muito legal'
primeiro_trecho = frase[0:7]
segundo_trecho = frase[7]
terceiro_trecho = frase[9:14]
quarto_trecho = frase[15: len(frase)]

print(primeiro_trecho)
print(segundo_trecho)
print(terceiro_trecho)
print(quarto_trecho)
print("Tamanho da frase completa:", len(frase))
print("Tamanho do trecho 1:", len(primeiro_trecho))
print("Tamanho do trecho 2:", len(segundo_trecho))
print("Tamanho do trecho 3:", len(terceiro_trecho))
print("Tamanho do trecho 4:", len(quarto_trecho))

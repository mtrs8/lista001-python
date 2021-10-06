# 1. Crie uma lista com o nome das 3 pessoas mais próximas.

nomes_pessoas_prox = ['Daniel', 'Vanda', 'Even']

print(nomes_pessoas_prox)

# 2. Crie três listas, uma lista de cada coisa a seguir:
# • frutas
# • docinhos de festa (não se esqueça de brigadeiros!!)
# • ingredientes de feijoada
# Lembre-se de salvá-las em alguma variável!
# Nessa lista de listas (vou chamar de listona):
# de festa? 

frutas = ['Banana', 'Maçã', 'Uva']
doces = ['brigadeiro', 'beijinho', 'tortinhas']
feijoada = ['carne de charque', 'linguica', 'feijão preto', 'bacon', 'temperos']

# a. Agora crie uma lista que contém essas três listas.
listona = [frutas, doces, feijoada]

# b. você consegue acessar o elemento brigadeiro?
print(listona[1:0])

# c. Adicione mais brigadeiros à segunda lista de listona. O que aconteceu com a lista de docinhos
listona[1].append('brigadeiro1')

# d. Adicione bebidas ao final da listona, mas sem criar uma lista!
listona.append('refrigerante')

print(listona)

# 3. Utilizando o del, remova todos os elementos da lista criada anteriormente até a lista ficar vazia.
del listona
# print(listona)

# 4. Faça uma lista de compras do mês, não se esqueça de comprar produtos de limpeza e sorvete!
lista_compras = ['Água sanitária', 'Detergente', 'Desinfetante', 'Escova', 'Sorvete']
print(lista_compras)
# Agora «vá ao mercado» e delete apenas os produtos de limpeza da lista.
del lista_compras[:4]
print(lista_compras)

# Agora «vá à sorveteria» e se empanturre de sorvete e tire o sorvete da lista.
del lista_compras[0]
print(lista_compras)

# 5. Dado uma lista de números, faça com que os números sejam ordenados e, em seguida, inverta a 
# ordem da lista usando slicing.
valores = [23, 235, 5, 65, 877, 0, 40]
valores.sort()
print(valores)
print(valores[::-1])



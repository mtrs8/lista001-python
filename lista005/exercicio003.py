# 3.Entrar com a sigla do estado de uma pessoa, e imprimir se é carioca, Paulista, 
# mineira ou outros estados.

sigla = input("Entre com a sigla do seu estado: ")

if(sigla == 'BA'):
    print("Baiana")
elif(sigla == 'RJ'):
    print("Carioca")
elif(sigla == 'MG'):
    print("Mineira")
elif(sigla == 'SP'):
    print("Paulista")
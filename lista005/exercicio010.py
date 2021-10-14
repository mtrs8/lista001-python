# 10. sabendo-se que somente os municípios que possuem mais de 20 mil eleitores
# aptos tem segundo turno nas eleições para prefeito caso o primeiro colocado
# não tenha mais do que 50% DOS VOTOS. FAZER UM PROGRAMA QUE LEIA O NOME do município, a
# quantidade de eleitores aptos, o número de votos do candidato 
# mais votado e informar se ele terá ou não segundo turno.

nome_municipio = input("Município: ")
qtd_eleitores = int(input("\nQuantidade de eleitores: "))
candidato_mais_votado = int(input("\nQuantidade de votos do candidato mais votado: "))

if(qtd_eleitores >= 20000):
    if(qtd_eleitores * 0.50 >= candidato_mais_votado):
        print("No munícipio de", nome_municipio, "haverá segundo turno.\n")
    else:
        print("No munícipio de", nome_municipio, "NÃO haverá segundo turno.\n")
else:
    print("\nNo munícipio ", nome_municipio, " existem menos de 20 mil eleitores válidos.")
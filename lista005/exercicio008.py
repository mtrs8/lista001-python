# 8. entrar com o nome, nota 1 e nota 2 de um aluno, imprimir nome, Nota1, nota2, média e a mensagem
# aprovado, reprovado ou em prova final. (a média é 7 para aprovado, 3 para reprovado, e as demais para
# prova final.

nome = input("Digite seu nome: ")
nota1 = float(input("Digite 1a nota do aluno: "))
nota2 = float(input("Digite 2a nota do aluno: "))
nota3 = float(input("Digite 3a nota do aluno: "))
media = (nota1 + nota2 + nota3) / 3

if(media >= 7):
    print("Parabéns,", nome,"!","\nVocê foi aprovado.\nNotas: ",
         nota1, nota2, nota3, "\nMédia: ",  media)
elif(media <= 3):
    print("Nome: ", nome, "\nReprovado!\nNotas: ", nota1, nota2, nota3, "\nMédia: ", media)
else:
    print("Nome: ", nome, "\nVocê está habilitado para fazer prova final.\nNotas: ", 
        nota1, nota2, nota3, "\nMédia: {0:.2f}".format(media))

#2.Entrar como nome, idade e sexo de uma pessoa. se a pessoa for do sexo feminino e tiver menos de 25 
# anos, imprimir a mensagem (ACEITA), caso contrário, imprimir NAO ACEITA

nome = input("Seu nome: ")
idade = int(input("Sua idade: "))
sexo = int(input("Seu sexo: \n[1] Masculino\n[2] Feminino\n[3] Não dizer"))

if(sexo == 2 and idade < 25):
    print("Pessoa aceita!")
else:
    print("Pessoa não aceita!")
# 1.Faça um dicionário com as 5 pessoas mais perto de você, tendo o nome como chave e a cor da 
# camisa que está usando como valor.

pessoas = {
        "jeferson": "branca", 
        "maria": "azul", 
        "joao": "verde", 
        "jose": "vermelho", 
        "geovane": "cinza"
}
print("Questão 1:", pessoas, "\n")

# 2. Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana, 
# tendo como seu valor uma lista com as aulas que você tem nesse dia (sábado e domingo
# recebem listas vazias, ou você tem aula?).  

semana = {
        "segunda": ["engenharia de software", "tópicos avançados"], 
        "terca": ["eng. de software"],
        "quarta": [], 
        "quinta": ["programacao python"], 
        "sexta": ["metodos cientificos em computacao"],
        "sabado": [], 
        "domingo": []
}
print("Questão 2: ", semana, "\n")

# 3. Crie um dicionário vazio filmes = {}. Utilize o nome de um filme como chave. E, como valor,
# outro dicionário contendo o vilão e o ano em que o filme foi lançado. Preencha 5 filmes.

filmes = {
        "interestelar": {
                "ano de lancamento": 2014, 
                "vilao": "terra"
        }, 
        "ironman 1": {
                "ano de lancamento": 2008, 
                "vilao": "modok"
        },
        "avengers endgame": {
                "ano de lancamento": 2019, 
                "vilao": "thanos"
        },
        "aquaman": {
                "ano de lancamento": 2018, 
                "vilao": "Orm"
        },
        "american beauty": {
                "ano de lancamento": 1999, 
                "vilao": "nenhum"
        }
}
print("Questão 3: ", filmes, "\n")

# 4. Crie um dicionário d e coloque nele seus dados: nome, idade, telefone, endereço,
# usando o dicionário d criado anteriormente. Imprima seu nome.

d = {
        "nome": "Matheus Alves", 
        "idade": 23, 
        "telefone": "(71) 9 0000-0000", 
        "endereco": "rua x, bairro y, Salvador-Ba"
}
print("Questão 4:", d["nome"], "\n")

# 5. Crie um dicionário que é uma agenda e coloque nele os seguintes dados: chave (cpf), nome, 
# idade, telefone. O programa deve ler os 5 dados completos, e imprimir todos os itens do
# dicionário no formato chave: nome-idade-fone.

agenda = {
        "José da Silva" : {
                "cpf": "999.999.999-00", 
                "nome": "José da Silva", 
                "idade": 44, "telefone": 
                "(71) 9 1234-5678",
        }, 

        "João de Souza": {
                "cpf": "888.888.888-11", 
                "nome": "João de Souza", 
                "idade": 50, 
                "telefone": "(71) 9 5678-1234",
        },

        "Maria José": {
                "cpf": "777.777.77-22", 
                "nome": "Maria José", 
                "idade": 30, 
                "telefone": "(71) 9 1223-3328",
        },

        "Joana da Silva": {
                "cpf": "666.666.666-33", 
                "nome": "Joana da Silva", 
                "idade": 24, 
                "telefone": "(71) 9 4534-5342",
        },
        "Pedro da Hora": {
                "cpf": "555.555.555-44", 
                "nome": "Pedro da Hora", 
                "idade": 18, 
                "telefone": "(71) 9 2345-6644"
        }
}

print("Questão 5: ", agenda)


import os 


os.system('cls')

# criando uma agenda de contatos
agenda = {

}

# adicionando nome e telefone a agenda
nome = []
telefone = []

# inserindo nome e telefone 
Nome = input('entre com o nome: ')
telefone = input('entre com o numero do telefone: ')
agenda[Nome] = telefone
print(f'contato{nome}: {telefone} adicionado')

# verfifcando se o nome e numero constam na agenda
for nome, telefone in agenda.items():
    if nome == "agenda":
        print
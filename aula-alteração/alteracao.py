import csv
import os


os.system('cls')

arquivo = 'arquivos_csv/gravacao/alunas.csv' # nome do arquivo
nome_para_alterar = input('digite o nome que deseja alterar: ') # solicitando o nome a ser alterado

# novo_cadastro = [] # lista para receber cadastro atualizado
alterado = False

# abrindo o arquivo csv para leitura
with open(arquivo, 'r') as arquivo_csv:
    # criando leitor para ler arquivo como dicionário
    leitura = csv.DictReader(arquivo_csv, delimiter=';')
    # convertendo o dicinário em uma lista
    cadastro = list(leitura)


 # atualizando o dicionário utilizando update()
    while True:
        novo_arquivo = input('digite o arquivo a ser alterado: ')

        if  'novo_arquivo':

            novo_arquivo = novo_arquivo.split(':')

        for registro in cadastro: # para cada registro em cadastro (fazendo uma varredura)           
            if registro['nome'] == nome_para_alterar: # se o nome for igual ao nome declarado
                alterado = True  # confirmar a alteração

# reescrevendo  o arquivo com a alteração
        with open(arquivo, 'w', newline='') as arquivo_csv:
            campos = ['nome', 'telefone', 'cidade']
            escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')

            escrever.writeheader()
            escrever.writerows(cadastro)

        if alterado:
            print(f'registro com nome{nome_para_alterar} foi alterado')
        else:
            print(f'registro com nome {nome_para_alterar} não encontrado.')

            print()    
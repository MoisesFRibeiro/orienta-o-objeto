import csv
import os


os.system('cls')

arquivo = 'arquivo_csv/gravacao/alunas.csv' # nome do arquivo
nome_para_apagar = input('digite o nome que deseja apagar: ') # solicitando o nome a ser apagado dentro da lista 

# lendo os dados do arquivo
with open(arquivo, 'r') as arquivo_csv:
    leitura = csv.DictReader(arquivo_csv, delimiter=';')
    cadastro = list (leitura)

# verificando se o nome existe e apagendo o registro
apagado = False
novo_cadastro = [registro for registro in cadastro \
                 if registro['nome'] != nome_para_apagar]
 
if len(novo_cadastro) < len(cadastro):
    apagado = True 

# reescrevendo o arquivo com os dados atualizados
with open(arquivo, 'w', newline='') as arquivo_csv:
    campos = ['nome', 'telefone', 'cidade']
    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')

    escrever.writeheader()
    escrever.writerows(novo_cadastro)
print('-'*70)
if apagado:
    print(f"regisstro com nome {nome_para_apagar} apagado com sucesso.")
else:
    print(f"registro com nome {nome_para_apagar} não encontrado.")
    print('-'*70)    
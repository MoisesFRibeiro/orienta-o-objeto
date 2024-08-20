import csv
import os


# nome do arquivo csv
arquivo = "arquivos_csv/gravcao/alunas.csv"
 
# lista para armazenar os dados
lista = []

# abrindo o arquivo csv para leitura
with open(arquivo, 'r') as arquivo_csv:
    # criando um leitor csv que lê o oqrquivo como dicionario
    leitura = csv.DictReader(arquivo_csv, delimiter=';')

    # iterando sobre cada linha (registro) no arquivo csv e adicionado a lista
    for linha in leitura:
        lista.append(linha)

os.system('cls')
print('-'*70)
print('nome\ttelefone\tcidade')
print('='*70)
# exibindo a lista resultante
for registro in lista:
    flag = 0 
    for k, v  in registro.items():
        print(v, end='\t')
        flag += 1 
        if flag == 3: 
            print()
print('-'*70)            
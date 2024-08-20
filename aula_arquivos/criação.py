# importar a biblioteca csv
import csv
import os


# craindo uma lista de dicionários: cada dicionário é uma linha (registro)
lista =[
    {'nome': 'agata', 'telefone' : '(32)99196-0000' , 'cidade' : 'juiz de fora'},
    {'nome': 'bia', 'telefone' : '(32)99196-1111' , 'cidade' : 'juiz de fora' },
    {'nome': 'coly', 'telefone' : '(32)99196-2222' , 'cidade' : 'juiz de fora'},
    {'nome': 'isis', 'telefone' : '(32)99196-3333' , 'cidade' : 'juiz de fora'},
]

# caminho para a pasta onde o arquivo csv será salvo
pasta = 'arquivos._csv/gravacao/'

# verificando se a pasta existe, se não, irá cria-lá
os.makedirs(pasta, exist_ok=True)

# nome para o arquivo csv para gravar as informações
arquivo = 'arquivo_csv/gravacao/alunas.csv'

# caminho completo para o arquivo csv
caminho_arquivo = os.path.join(pasta, arquivo)

# abre o arquivo 'arquivo' no modo escrita('w')
# se o arquivo não existir, ele será criado; será truncado (esvaziado)
# newline='': evita adição de linhas em branco extras ao gravar o arquivo em algumas plataformas.
# as arquivo_csv: atribui o objeto arquivo ao 'arquivo_csv' para ser usado dentro do bloco with.
with open(arquivo, 'w', newline='') as arquivo_csv:

    # campos = ['name', 'telefone', 'cidade']: define a lista de nomes de campos
    # (cabeçalhos das colunas do csv).
    campos = ['nome', 'telefone', 'cidade']

    # writer = csv.dictwriter(arquivo_csv, fieldnames=campos):
    # cria um objeto dictwriter que usara "arquivo_csv" para gravar os campos.
    # fieldnames define a ordem  dos campos do arquivo csv.
    # delimiter=';' : é o separador.
    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')

    # writer.writeheader(): gravaa linha de cabeçalho no
    # arquivo csv usando os nomes campos definidosem fieldnames.
    escrever.writeheader()

    # writer.writerows(lista): grava todas as linhas da lista no arquivo csv.
    # cada dicionário em 'lista' se torna uma linha do arquivo.
    escrever.writerows(lista)

os.system('cls')
# exibe uma mensagem indicando que o arquivo foi gravado com sucesso.
print(f'arquivo { arquivo} gravado com sucesso!')        
import os 


os.system('cls')

nomes = ['ágata', 'Bia', 'Coly', 'Isis']

for indice, nome in enumerate(nomes):
    # cria uma tupla contendo o indice eo nome da pessoa atual. 
    minha_tupla = ( indice, nome)
    # a variavel tupla é utilizada para acessar o 
    # indice e o nome armazenado na tupla. 
    # mas posso acessar diretamente os elementos 'indice' e 'nome'
    print(f'o nome "{minha_tupla[1]}" , posição {minha_tupla[0]} da lista.')
    print(f' o nome "{nome}", posição {indice} da lista.')
    print('_'*70)
import os


os.system('cls'*70)

# definindo uma função para empacotar
def empacotar(*lista_numeros):
    print(f'empacotados: {lista_numeros}')
    for i in lista_numeros:
        print(f'empacotado: {i}')

# chamando a função empacotar 
empacotar(1, 2, 3, 4, 5)

# desempacotando a lista 
def desempacotar(a, b, c, d, e):
    print('desempacotar:')
    print(f'a -{a}')
    print(f'b - {b}')
    print(f'c - {c}')
    print(f'd - {d}')
    print(f'e - {e}')

# chamando a função empacotar
lista_numeros = [1, 2, 3, 4, 5] # lista 
desempacotar(*lista_numeros) # *args 

# packing dicionário
def empacotar_dicionario(**dados_dicionario): # **kargs
    print(f'dados do dicionario: {dados_dicionario}')
    for k, v in dados_dicionario.items():
        print(f'chave : {k}, valor {v}')

print('-'*70)
print        
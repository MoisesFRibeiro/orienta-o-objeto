# Outros exemplos

import os 


os.system('cls')

# inicialização do dicionário e da lista
elementos = {} # dicionário
periodica = [] # lista

# entrada de dados
for c in range (2) # considerando a entrada de 2 elementos 
    print(f"entrada de dados {c + 1}:")
    simbolo = str(input('simbolo do elemento: '))
    nome = str(input('nome do elemento: '))

# adciona os dados ao dicionário
    elementos['simbolo'] = simbolo
    elementos['nome'] = nome

    # usa append() com copy() para adicionar uma coópia do dicionário a lista
    periodica.append(elementos.copy())

print()
print('-'*70)
print("elementos na tabela periodica:")
print(periodica) 
print('-'*70)
print() 

# for aninhado para percorrer a liksta eo dicionário
print("detalhe dos elementos:")
for elemento in periodica: # para cada elemento na lista
    for chave, valor in elemento.items(): # para cada chave e valor do dicionário
        print('f{chave.capitalize()}: {valor}') # imprime a chave eo valor de maneira legivel
        print('-'*70) # linha separadora entre elementos 

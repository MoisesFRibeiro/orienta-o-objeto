import os


os.system('cls')

# solicita ao usuario para inserir varios numeros separados por espaço
entrada = input('digite numeros separados por espaço: ')

# divide a string de entrada em uma lsita de string
numeros_str = entrada.split()

# converte a lista de strings em uma lista de inteiros 
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

# soliciata ao usuario  poara inserir o numeros que deseja  encontrar na lista 
busca_numero = int(input('digite o numeros que deseja encontrar: '))

# tenta encontrarr o indice do numero fornecido
if busca_numero in numeros:
    indice = numeros.index(busca_numero)
    print(f'o numero {busca_numero} esta no indice {indice}')
else:
    print(f'o numero {busca_numero} não foi encontrado na lista') 

# exibe a lista fornecida para referencia
print(f'lista fornecida: {numeros}')       
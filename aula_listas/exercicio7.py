import os


os.system('cls')

# solicita ao usuario inserir numeros separados por espaços
entrada = input('digite os numeros separados por espaço: ')

# divide a string de entrad em uma lista de string
numeros_str = entrada.split()

# converte a lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

# solicita ao usuario para inserir o numero que deseja contar na lista 
numero_para_contar = int(input('digite o numero que deseja contar: '))

# conta o numero de vezes que o numero fornecido aparece na linha 
contagem = numeros.count(numero_para_contar)

if contagem > 0:
    print(f' o numero {numero_para_contar} aparece {contagem} vezes na lista')
else:
    print(f'o numero {numero_para_contar} não aparece na lista')

# exibe a lista fornecida para referencia
print(f' lista fornecidas: {numeros}')     
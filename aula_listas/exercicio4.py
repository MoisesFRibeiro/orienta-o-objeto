import os


os.system('cls')

# inicializa uma lista vazia
lista_numeros = []

# solicita ao usuario para inserir os numeors com espaço
entrada = input('digite numeros separados por espaço: ')

# divide uma lista de entrada em uma lista de strings
numeros = entrada.split()

#  cria uam lista para armazernar os numeros pares
pares = []

# itera sobre os numeros inseridos
for numero in numeros:
    # converte a string para inteiro
    numero_aux = int(numero)
    # verifica se o numero é par 
    if numero_aux % 2 == 0:
        # adiciona o numero par a lista de pares
        pares.append(numero_aux)

# usa extend() para adicionartodos os numeros pares a lista principal
lista_numeros.extend(pares)

# exibe a lista resultante
print(f"numeros pares adicionados a lista: {lista_numeros}")
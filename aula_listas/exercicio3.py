import os 


os.system('cls')

# inicilizando uma lista vazia
lista_numeros = []

# pede ao usuario para inserir tres numeros
for i in range(3):
    numero = int(input("digite um numero: "))

    # adiciona um numeero a lista 
    lista_numeros.append(numero)

# verificar se o numero inserido esta na lista e 
# exibe uma mensagem correspondente
numero_verificar = int(input("digite um numero: "))

if numero_verificar in lista_numeros:
    print(f'o numero {numero_verificar} esta na lista!')
else:
    print(f'o numero {numero_verificar} não esta na lista!')    
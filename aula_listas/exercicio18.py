import os 


os.system('cls')

print('-'*70)
print('estrutura de dados: list comprehensions[ ]')
print('='*70)

lista_numeros = [100, 200, 300, 500, 600]

# triplicar os valores
lista_com_juros = []

for item in lista_numeros:

    lista_com_juros.append(item + (item * .10))

print('aplicar 10% de jurios: forma normal')
print(f'lista triplicada: {lista_com_juros}')
print()

# list comprehensions
lista_com_juros_2 = [item + (item * .10) for item in lista_numeros]
print('aplicar 10% de juros: list comprehensions')
print(f'lista triplicada: {lista_com_juros_2}\n')

import os


os.system('cls')

print('_'*50)
print('estrutura de controle com input e if')
print('='*50)

print()

soma = 0

for var_iteradora in range(0, 4):
    numero = int(input(f'{var_iteradora +1}º numero: '))
    if (numero % 2== 0):
        print(f'o numero{numero} é par')
    else:
        print(f'o numero{numero} é impar') 

print('_'*50)
print()           
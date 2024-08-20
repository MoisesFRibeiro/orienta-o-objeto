import math
import os


os.system('cls')

print('_'*50)
print('estudo da biblioteca math')
print('='*50)
print()

# entrada de dados
numero_decimal = float(input('entre com o numero decimal: '))

# processamento
arredondar_para_cima = math.ceil(numero_decimal)
arredondar_para_baixo = math.floor(numero_decimal)

# saida
print('-'*50)
print(f'o numero {numero_decimal} arredondado para cima é: {arredondar_para_cima}')
print(f' o numero {numero_decimal} arrendomdado para baixo é: {arredondar_para_baixo}')
print('-'*50)

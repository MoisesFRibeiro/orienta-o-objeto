# D) A empresa "SalaryBoost" está implementando um sistema automatizado para calcular os aumentos salariais de seus funcionários
# com base em critérios específicos. Eles precisam de um programa que receba como entrada o salário atual de um funcionário e,
# em seguida, calcule o novo salário com base em determinadas condições. Essas condições incluem um aumento de 5%
# caso o salário atual seja superior a R$1500,00, e um aumento de 10% caso o salário atual seja inferior a R$1000,00.
# Além disso, o programa deve garantir que o salário informado não seja igual a zero ou negativo, pois isso não seria válido.

# importando a biblioteca
import os


# limpar biblioteca
os.system('cls')

print('_'*70)
print('atividade de condicionais: D')
print('='* 70)

# entrada
salario = float(input('digite aqui o seu salario '))
print('='*70)

# condição
if salario >= 1500:
    salario1500 = salario * (5/100)
    salario_atual = salario + salario1500
    print(f' seu novo salariio é {salario_atual} ')
    
elif (salario > 0 and salario < 1499)
    salario1000 = salario * (10/100)
    salario_atual2 = salario + salario1000 
    print(f'seu novo salario é {salario_atual2}')
    
else:    
    print(f'salario {salario} invalido')    
# curso de desenvolvimento de sistemas 
# turma 0152(Braba)
# autor: Moises de souza ribeiro
# data: 26/04/2024
# atividade de condicionais: B

# importando a biblioteca 
import os


# limpando a biblioteca
os.system('cls')

print('_'*70)
print('atividade de condicional: B')
print('='*70)

# entrada
a = float(input('digite o primeiro numero'))
b = float(input('digite o segundo numero'))
c = float(input('digite o terceiro numero'))


# maior que (>)
if a > b > c:
    print('_'*70)
    print(f'{a} é maior que {b} ou maior que {c} ')
    print('='*70)
elif b > a > c:
    print(f'{b} é maior que {a} é maior que {c}')
    
else:
    print(f'{a} não é maior que {b} nem maior que {c}')

# menor que (<)
if a < b < c:
    print('_'*70)
    print(f'{a} é menor que {b} ou menor que {c}')
    print('='*70)
elif c < a < b:
    print(f'{c} é menor que {a} que é menor que {b}')    
else:
    print(f'{a} não e menor que {b} ou menor que {c}')
                
# igualdade (==) 
if a == b == c:
    
    print('_'*70)
    print(f'{a} é igual a {b} ou igual a {c}')
    print('='*70)
else:
    print(f'{a} nao é igual a {b} ou não é igual a {c}')
    
print('fim do programa!')    
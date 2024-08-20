# curso de desenvolvimento de sistemas 
# turma 0152(braba)
# autor: moises de souza ribeiro
# data: 25/04/2024
# estudo de condicionais parte 3
# operações relacionais

import os


os.system('cls')

a = 10
b = 5
c = 'jose'
d = 'jose'

print('_'*70)
print('condicionais: operadores relacionais')
print("_"*70)

# igualdade(==)
if c == d:
    print('_'*70)
    print(f' {c} e igual{d}')
    print("_"*70)
else:
    print(f'{c} nao e igual a {d}')

# diferença (!=) 
if a != c:
    print('_'*70)
    print(f'{a} e diferente de {c}')
    print("_"*70)
else:
    print(f' {a} nao e diferente de {c}')
    
# maior que (>)
if a > b:
    print('_'*70)
    print(f' {a} e maior que {b}')
    print('='*70) 
else:
    print(f'{a} não e maior que {b}')
    
# menor  que (<)
if b < a:
    print('_'*70)
    print(f'{b} e menor que {a}')
    print('='*70)
else:
    print(f'{b} não e menor que {a}')
    
# maior ou igual a (>=)
if a >= b:
    print('_'*70)
    print(f'{a} e maior ou igual a {b}')
    print('='*70)
else:
    print(f'{a} nao e maior ou igual a {b}')
    
# menor ou igual a (<=)
if b <= a:
    print('_'*70)
    print(f'{b} e menor ou igual a {a}')
    print('='*70)
else:
    print(f'{b} nao é menor ou igual a {a}')
    
print('fim do programa!')
print('_'*70)
print()                           
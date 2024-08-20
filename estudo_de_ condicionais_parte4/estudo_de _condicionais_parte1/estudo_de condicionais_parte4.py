# curso de densenvolvimento de sistemas 
# turma 0152(babra)
# autor: moises de souza ribeiro
# data: 25/04/2024
# Estudo de condicionais: parte4
# operadores logicos

# importando as bibliotecas
import os 


# limpando o terminal
os.system('cls')

# declaração
a = 10
b = 5 
c = 'Jhon'
 
print('_'*70)
print('condicionais: operadores logicos') 
print('='*70)

# E (and) VERDADEIRO
print('E (and) VERDADEIRO')
if (a > 5 and b!= c):
    print('VERDADEIRO: bloco executado')
else:
    print('falso: bloco executado')
        
print('_'*70)
# E (and) FALSO
print('E (and) FALSO')
if(a > 5 and b ==c):
    print('verdadeiro: bloco executado') 
else:
    print('falso: bloco executado')
    
print('_'*70)

# ou (or) VERDADEIRO
print('ou(or)VERDADEIRO')
      
# importando a biblioteca do sistema
import os


# limpando o terminal
os.system('cls')

print('-'*70) # firula
print('estudo de variaveis')
print('='*70)

# as variaveis são declaradas por inferencia
nome  = 'John Doe'
nascimento = 1978
altura = 1.80
peso = 75.5
doador = True
complexo = 3j # phyton trabalha diretamente com numeros complexos
PI = 3.14 # isso é uma constante, seu valor não deve ser alterado

# saida utilizando o metodo type() para verificar o
# tipo da variavel
print('\033[0m \033[31mtipos declarados:\033[0m')
print('\033[0m a var \033[32 nome \033[0m é do tipo: ', type(nome))
print('\033[0m a var \033[32m altura \033[0m é do tipo: ', type(altura))
